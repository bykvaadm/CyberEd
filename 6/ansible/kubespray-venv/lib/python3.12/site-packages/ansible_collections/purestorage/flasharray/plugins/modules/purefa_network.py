#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2020, Simon Dodsley (simon@purestorage.com)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}


DOCUMENTATION = """
---
module: purefa_network
short_description:  Manage network interfaces in a Pure Storage FlashArray
version_added: '1.0.0'
description:
    - This module manages the physical and virtual network interfaces on a Pure Storage FlashArray.
    - To manage VLAN interfaces use the I(purestorage.flasharray.purefa_vlan) module.
    - To manage network subnets use the I(purestorage.flasharray.purefa_subnet) module.
    - To remove an IP address from a non-management port use 0.0.0.0/0
author: Pure Storage Ansible Team (@sdodsley) <pure-ansible-team@purestorage.com>
options:
  name:
    description:
      - Interface name (physical or virtual).
    required: true
    type: str
  state:
    description:
      - State of existing interface (on/off).
    required: false
    default: present
    choices: [ "present", "absent" ]
    type: str
  address:
    description:
      - IPv4 or IPv6 address of interface in CIDR notation.
      - To remove an IP address from a non-management port use 0.0.0.0/0
    required: false
    type: str
  gateway:
    description:
      - IPv4 or IPv6 address of interface gateway.
    required: false
    type: str
  mtu:
    description:
      - MTU size of the interface. Range is 1280 to 9216.
    required: false
    default: 1500
    type: int
  servicelist:
    description:
      - Assigns the specified (comma-separated) service list to one or more specified interfaces.
      - Replaces the previous service list.
      - Supported service lists depend on whether the network interface is Ethernet or Fibre Channel.
      - Note that I(system) is only valid for Cloud Block Store.
    elements: str
    type: list
    choices: [ "replication", "management", "ds", "file", "iscsi", "scsi-fc", "nvme-fc", "nvme-tcp", "nvme-roce", "system"]
    version_added: '1.15.0'
  interface:
    description:
      - Type of interface to create if subinterfaces is supplied
    type: str
    choices: [ "vif", "lacp" ]
    version_added: '1.22.0'
  subordinates:
    description:
     - List of one or more child devices to be added to a LACP interface
     - Subordinates must be on the same controller, therefore the full device needs
       to be provided.
    type: list
    elements: str
    version_added: '1.22.0'
  subinterfaces:
    description:
     - List of one or more child devices to be added to a VIF interface
     - Only the 'eth' name needs to be provided, such as 'eth6'. This interface on
       all controllers will be assigned to the interface.
    type: list
    elements: str
    version_added: '1.22.0'
  subnet:
    description:
     - Name of the subnet which interface is to be attached
    type: str
    version_added: '1.22.0'
  enabled:
    description:
    - State of the network interface
    type: bool
    default: true
    version_added: '1.22.0'
extends_documentation_fragment:
    - purestorage.flasharray.purestorage.fa
"""

EXAMPLES = """
- name: Configure and enable network interface ct0.eth8
  purestorage.flasharray.purefa_network:
    name: ct0.eth8
    gateway: 10.21.200.1
    address: "10.21.200.18/24"
    mtu: 9000
    state: present
    fa_url: 10.10.10.2
    api_token: c6033033-fe69-2515-a9e8-966bb7fe4b40

- name: Disable physical interface ct1.eth2
  purestorage.flasharray.purefa_network:
    name: ct1.eth2
    state: absent
    fa_url: 10.10.10.2
    api_token: c6033033-fe69-2515-a9e8-966bb7fe4b40

- name: Enable virtual network interface vir0
  purestorage.flasharray.purefa_network:
    name: vir0
    state: present
    fa_url: 10.10.10.2
    api_token: c6033033-fe69-2515-a9e8-966bb7fe4b40

- name: Remove an IP address from iSCSI interface ct0.eth4
  purestorage.flasharray.purefa_network:
    name: ct0.eth4
    address: 0.0.0.0/0
    gateway: 0.0.0.0
    fa_url: 10.10.10.2
    api_token: c6033033-fe69-2515-a9e8-966bb7fe4b40

- name: Change service list for FC interface ct0.fc1
  purestorage.flasharray.purefa_network:
    name: ct0.fc1
    servicelist:
      - replication
    fa_url: 10.10.10.2
    api_token: c6033033-fe69-2515-a9e8-966bb7fe4b40
"""

RETURN = """
"""

try:
    from netaddr import IPAddress, IPNetwork, valid_ipv4, valid_ipv6

    HAS_NETADDR = True
except ImportError:
    HAS_NETADDR = False

try:
    from pypureclient.flasharray import (
        NetworkInterfacePatch,
        NetworkInterfacePost,
        NetworkinterfacepostEth,
        NetworkinterfacepatchEth,
        FixedReferenceNoId,
        ReferenceNoId,
    )

    HAS_PYPURECLIENT = True
except ImportError:
    HAS_PYPURECLIENT = False

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.purestorage.flasharray.plugins.module_utils.purefa import (
    get_system,
    get_array,
    purefa_argument_spec,
)

FC_ENABLE_API = "2.4"


def _is_cbs(array, is_cbs=False):
    """Is the selected array a Cloud Block Store"""
    model = array.get(controllers=True)[0]["model"]
    is_cbs = bool("CBS" in model)
    return is_cbs


def _get_fc_interface(module, array):
    """Return FC Interface or None"""
    interface = {}
    interface_list = array.get_network_interfaces(names=[module.params["name"]])
    if interface_list.status_code == 200:
        interface = list(interface_list.items)[0]
        return interface
    return None


def _get_interface(module, array):
    """Return Network Interface or None"""
    interface = {}
    if module.params["name"][0] == "v":
        try:
            interface = array.get_network_interface(module.params["name"])
        except Exception:
            return None
    else:
        try:
            interfaces = array.list_network_interfaces()
        except Exception:
            return None
        for ints in range(0, len(interfaces)):
            if interfaces[ints]["name"] == module.params["name"]:
                interface = interfaces[ints]
                break
    return interface


def update_fc_interface(module, array, interface, api_version):
    """Modify FC Interface settings"""
    changed = False
    if FC_ENABLE_API in api_version:
        if not interface.enabled and module.params["state"] == "present":
            changed = True
            if not module.check_mode:
                network = NetworkInterfacePatch(enabled=True, override_npiv_check=True)
                res = array.patch_network_interfaces(
                    names=[module.params["name"]], network=network
                )
                if res.status_code != 200:
                    module.fail_json(
                        msg="Failed to enable interface {0}.".format(
                            module.params["name"]
                        )
                    )
        if interface.enabled and module.params["state"] == "absent":
            changed = True
            if not module.check_mode:
                network = NetworkInterfacePatch(enabled=False, override_npiv_check=True)
                res = array.patch_network_interfaces(
                    names=[module.params["name"]], network=network
                )
                if res.status_code != 200:
                    module.fail_json(
                        msg="Failed to disable interface {0}.".format(
                            module.params["name"]
                        )
                    )
    if module.params["servicelist"] and sorted(module.params["servicelist"]) != sorted(
        interface.services
    ):
        changed = True
        if not module.check_mode:
            network = NetworkInterfacePatch(services=module.params["servicelist"])
            res = array.patch_network_interfaces(
                names=[module.params["name"]], network=network
            )
            if res.status_code != 200:
                module.fail_json(
                    msg="Failed to update interface service list {0}. Error: {1}".format(
                        module.params["name"], res.errors[0].message
                    )
                )

    module.exit_json(changed=changed)


def _check_subinterfaces(module, array):
    subordinates = []
    subinterfaces = list(
        array.get_network_interfaces(names=[module.params["name"]]).items
    )[0].eth.subinterfaces
    for subinterface in range(0, len(subinterfaces)):
        subordinates.append(subinterfaces[subinterface].name)
    return subordinates


def _create_subordinates(module, array):
    subordinates_v1 = []
    subordinates_v2 = []
    all_children = True
    if module.params["subordinates"]:
        for inter in sorted(module.params["subordinates"]):
            if array.get_network_interfaces(names=[inter]).status_code != 200:
                all_children = False
            if not all_children:
                module.fail_json(
                    msg="Subordinate {0} does not exist. Ensure you have specified the controller.".format(
                        inter
                    )
                )
            subordinates_v2.append(FixedReferenceNoId(name=inter))
            subordinates_v1.append(inter)
    return subordinates_v1, subordinates_v2


def _create_subinterfaces(module, array):
    subinterfaces_v1 = []
    subinterfaces_v2 = []
    all_children = True
    purity_vm = bool(len(array.get_controllers().items) == 1)
    if module.params["subinterfaces"]:
        for inter in sorted(module.params["subinterfaces"]):
            # As we may be on a single controller device, only check for the ct0 version of the interface
            if array.get_network_interfaces(names=["ct0." + inter]).status_code != 200:
                all_children = False
            if not all_children:
                module.fail_json(
                    msg="Child subinterface {0} does not exist".format(inter)
                )
            subinterfaces_v2.append(FixedReferenceNoId(name="ct0." + inter))
            subinterfaces_v1.append("ct0." + inter)
            if not purity_vm:
                subinterfaces_v2.append(FixedReferenceNoId(name="ct1." + inter))
                subinterfaces_v1.append("ct1." + inter)
    return subinterfaces_v1, subinterfaces_v2


def update_interface(module, array, interface):
    """Modify Interface settings"""
    changed = False
    current_state = {
        "enabled": interface["enabled"],
        "mtu": interface["mtu"],
        "gateway": interface["gateway"],
        "address": interface["address"],
        "netmask": interface["netmask"],
        "services": sorted(interface["services"]),
        "slaves": sorted(interface["slaves"]),
    }
    array6 = get_array(module)
    subinterfaces = current_state["slaves"]
    if module.params["subinterfaces"]:
        new_subinterfaces = _check_subinterfaces(module, array6)
        if new_subinterfaces != subinterfaces:
            subinterfaces = new_subinterfaces
        else:
            subinterfaces = current_state["slaves"]
    if module.params["subordinates"]:
        subordinates = _check_subinterfaces(module, array6)
        if sorted(subordinates) != sorted(module.params["subordinates"]):
            subinterfaces = module.params["subordinates"]
        else:
            subinterfaces = subordinates
    if module.params["enabled"] != current_state["enabled"]:
        enabled = module.params["enabled"]
    else:
        enabled = current_state["enabled"]
    if not current_state["gateway"]:
        try:
            if valid_ipv4(interface["address"]):
                current_state["gateway"] = None
            elif valid_ipv6(interface["address"]):
                current_state["gateway"] = None
        except AttributeError:
            current_state["gateway"] = None
    if not module.params["servicelist"]:
        services = sorted(interface["services"])
    else:
        services = sorted(module.params["servicelist"])
    if not module.params["address"]:
        address = interface["address"]
        netmask = interface["netmask"]
    else:
        netmask = current_state["netmask"]
        if module.params["gateway"] and module.params["gateway"] not in [
            "0.0.0.0",
            "::",
        ]:
            if module.params["gateway"] not in IPNetwork(module.params["address"]):
                module.fail_json(msg="Gateway and subnet are not compatible.")
        if not module.params["gateway"] and interface["gateway"] not in [
            None,
            IPNetwork(module.params["address"]),
        ]:
            module.fail_json(msg="Gateway and subnet are not compatible.")
        address = str(module.params["address"].split("/", 1)[0])
        if address in ["0.0.0.0", "::"]:
            address = None
    if not module.params["mtu"]:
        mtu = interface["mtu"]
    else:
        if not 1280 <= module.params["mtu"] <= 9216:
            module.fail_json(
                msg="MTU {0} is out of range (1280 to 9216)".format(
                    module.params["mtu"]
                )
            )
        else:
            mtu = module.params["mtu"]
    if module.params["address"]:
        if address:
            if valid_ipv4(address):
                netmask = str(IPNetwork(module.params["address"]).netmask)
            else:
                netmask = str(module.params["address"].split("/", 1)[1])
        if netmask in ["0.0.0.0", "0"]:
            netmask = None
    else:
        netmask = interface["netmask"]
    if not module.params["gateway"]:
        gateway = interface["gateway"]
    elif module.params["gateway"] in ["0.0.0.0", "::"]:
        gateway = None
    elif valid_ipv4(address):
        cidr = str(IPAddress(netmask).netmask_bits())
        full_addr = address + "/" + cidr
        if module.params["gateway"] not in IPNetwork(full_addr):
            module.fail_json(msg="Gateway and subnet are not compatible.")
        gateway = module.params["gateway"]
    else:
        gateway = module.params["gateway"]

    new_state = {
        "enabled": enabled,
        "address": address,
        "mtu": mtu,
        "gateway": gateway,
        "netmask": netmask,
        "services": sorted(services),
        "slaves": sorted(subinterfaces),
    }
    if new_state["address"]:
        if (
            current_state["address"]
            and IPAddress(new_state["address"]).version
            != IPAddress(current_state["address"]).version
        ):
            if new_state["gateway"]:
                if (
                    IPAddress(new_state["gateway"]).version
                    != IPAddress(new_state["address"]).version
                ):
                    module.fail_json(
                        msg="Changing IP protocol requires gateway to change as well."
                    )
    if new_state != current_state:
        changed = True
        if (
            module.params["servicelist"]
            and sorted(module.params["servicelist"]) != interface["services"]
        ):
            api_version = array._list_available_rest_versions()
            if FC_ENABLE_API in api_version:
                if HAS_PYPURECLIENT:
                    if not module.check_mode:
                        network = NetworkInterfacePatch(
                            services=module.params["servicelist"]
                        )
                        res = array6.patch_network_interfaces(
                            names=[module.params["name"]], network=network
                        )
                        if res.status_code != 200:
                            module.fail_json(
                                msg="Failed to update interface service list {0}. Error: {1}".format(
                                    module.params["name"], res.errors[0].message
                                )
                            )
                else:
                    module.warn_json(
                        "Servicelist not updated as pypureclient module is required"
                    )
        if (
            "management" in interface["services"] or "app" in interface["services"]
        ) and address in ["0.0.0.0/0", "::/0"]:
            module.fail_json(
                msg="Removing IP address from a management or app port is not supported"
            )
        if not module.check_mode:
            try:
                array.set_network_interface(
                    interface["name"], enabled=new_state["enabled"]
                )
                if new_state["gateway"] is not None:
                    array.set_network_interface(
                        interface["name"],
                        address=new_state["address"],
                        mtu=new_state["mtu"],
                        netmask=new_state["netmask"],
                        gateway=new_state["gateway"],
                    )
                    if (
                        current_state["slaves"] != new_state["slaves"]
                        and new_state["slaves"] != []
                    ):
                        array.set_network_interface(
                            interface["name"],
                            subinterfacelist=new_state["slaves"],
                        )
                else:
                    try:
                        if valid_ipv4(new_state["address"]):
                            empty_gateway = "0.0.0.0"
                        else:
                            empty_gateway = "::"
                    except Exception:
                        empty_gateway = "::"
                    array.set_network_interface(
                        interface["name"],
                        address=new_state["address"],
                        mtu=new_state["mtu"],
                        netmask=new_state["netmask"],
                        gateway=empty_gateway,
                    )
                    if (
                        current_state["slaves"] != new_state["slaves"]
                        and new_state["slaves"] != []
                    ):
                        res = array6.delete_network_interfaces(
                            names=[module.params["name"]]
                        )
                        if res.status_code != 200:
                            module.fail_json(
                                msg="Failed to delete network interface {0}. Error: {1}".format(
                                    module.params["name"], res.errors[0].message
                                )
                            )
                        create_interface(module, array6)
            except Exception:
                module.fail_json(
                    msg="Failed to change settings for interface {0}.".format(
                        interface["name"]
                    )
                )
    module.exit_json(changed=changed)


def create_interface(module, array):
    changed = True
    subnet_exists = bool(
        array.get_subnets(names=[module.params["subnet"]]).status_code == 200
    )
    if module.params["subnet"] and not subnet_exists:
        module.fail_json(
            msg="Subnet {0} does not exist".format(module.params["subnet"])
        )

    if module.params["interface"] == "vif":
        dummy, subinterfaces = _create_subinterfaces(module, array)
    else:
        dummy, subinterfaces = _create_subordinates(module, array)

    if not module.check_mode:
        if module.params["address"]:
            address = str(module.params["address"].strip("[]").split("/", 1)[0])
            if valid_ipv4(address):
                netmask = str(IPNetwork(module.params["address"]).netmask)
            else:
                netmask = str(module.params["address"].strip("[]").split("/", 1)[1])
        else:
            netmask = None
            address = None
        if module.params["gateway"]:
            gateway = str(module.params["gateway"].strip("[]"))
            if gateway not in ["0.0.0.0", "::"]:
                if address and gateway not in IPNetwork(module.params["address"]):
                    module.fail_json(msg="Gateway and subnet are not compatible.")
        else:
            gateway = None
        if module.params["interface"] == "vif":
            res = array.post_network_interfaces(
                names=[module.params["name"]],
                network=NetworkInterfacePost(
                    eth=NetworkinterfacepostEth(subtype="vif")
                ),
            )
        else:
            res = array.post_network_interfaces(
                names=[module.params["name"]],
                network=NetworkInterfacePost(
                    eth=NetworkinterfacepostEth(
                        subtype="lacpbond", subinterfaces=subinterfaces
                    ),
                ),
            )

        if res.status_code != 200:
            module.fail_json(
                msg="Failed to create interface {0}. Error: {1}".format(
                    module.params["name"], res.errors[0].message
                )
            )

        if module.params["subinterfaces"] and module.params["subnet"]:
            res = array.patch_network_interfaces(
                names=[module.params["name"]],
                network=NetworkInterfacePatch(
                    enabled=module.params["enabled"],
                    eth=NetworkinterfacepatchEth(
                        subinterfaces=subinterfaces,
                        address=address,
                        gateway=gateway,
                        mtu=module.params["mtu"],
                        netmask=netmask,
                        subnet=ReferenceNoId(name=module.params["subnet"]),
                    ),
                ),
            )
            if res.status_code != 200:
                array.delete_network_interfaces(names=[module.params["name"]])
                module.fail_json(
                    msg="Failed to create interface {0}. Error: {1}".format(
                        module.params["name"], res.errors[0].message
                    )
                )
        elif module.params["subinterfaces"] and not module.params["subnet"]:
            res = array.patch_network_interfaces(
                names=[module.params["name"]],
                network=NetworkInterfacePatch(
                    enabled=module.params["enabled"],
                    eth=NetworkinterfacepatchEth(
                        subinterfaces=subinterfaces,
                        address=address,
                        gateway=gateway,
                        mtu=module.params["mtu"],
                        netmask=netmask,
                    ),
                ),
            )
            if res.status_code != 200:
                array.delete_network_interfaces(names=[module.params["name"]])
                module.fail_json(
                    msg="Failed to create interface {0}. Error: {1}".format(
                        module.params["name"], res.errors[0].message
                    )
                )
        elif not module.params["subinterfaces"] and module.params["subnet"]:
            res = array.patch_network_interfaces(
                names=[module.params["name"]],
                network=NetworkInterfacePatch(
                    enabled=module.params["enabled"],
                    eth=NetworkinterfacepatchEth(
                        address=address,
                        gateway=gateway,
                        mtu=module.params["mtu"],
                        netmask=netmask,
                        subnet=ReferenceNoId(name=module.params["subnet"]),
                    ),
                ),
            )
            if res.status_code != 200:
                array.delete_network_interfaces(names=[module.params["name"]])
                module.fail_json(
                    msg="Failed to create interface {0}. Error: {1}".format(
                        module.params["name"], res.errors[0].message
                    )
                )
        else:
            res = array.patch_network_interfaces(
                names=[module.params["name"]],
                network=NetworkInterfacePatch(
                    enabled=module.params["enabled"],
                    eth=NetworkinterfacepatchEth(
                        address=address,
                        gateway=gateway,
                        mtu=module.params["mtu"],
                        netmask=netmask,
                    ),
                ),
            )
            if res.status_code != 200:
                array.delete_network_interfaces(names=[module.params["name"]])
                module.fail_json(
                    msg="Failed to create interface {0}. Error: {1}".format(
                        module.params["name"], res.errors[0].message
                    )
                )

    module.exit_json(changed=changed)


def delete_interface(module, array):
    changed = True
    if not module.check_mode:
        res = array.delete_network_interfaces(names=[module.params["name"]])
        if res.status_code != 200:
            module.fail_json(
                msg="Failed to delete network interface {0}. Error: {1}".format(
                    module.params["name"], res.errors[0].message
                )
            )
    module.exit_json(changed=changed)


def main():
    argument_spec = purefa_argument_spec()
    argument_spec.update(
        dict(
            name=dict(type="str", required=True),
            state=dict(type="str", default="present", choices=["present", "absent"]),
            address=dict(type="str"),
            gateway=dict(type="str"),
            mtu=dict(type="int", default=1500),
            servicelist=dict(
                type="list",
                elements="str",
                choices=[
                    "replication",
                    "management",
                    "ds",
                    "file",
                    "iscsi",
                    "scsi-fc",
                    "nvme-fc",
                    "nvme-tcp",
                    "nvme-roce",
                    "system",
                ],
            ),
            interface=dict(type="str", choices=["vif", "lacp"]),
            subinterfaces=dict(type="list", elements="str"),
            subordinates=dict(type="list", elements="str"),
            subnet=dict(type="str"),
            enabled=dict(type="bool", default=True),
        )
    )

    module = AnsibleModule(argument_spec, supports_check_mode=True)

    if module.params["state"] == "present":
        if module.params["interface"] == "lacp" and not module.params["subordinates"]:
            module.fail_json(
                msg="interface is lacp but all of the following are missing: subordinates"
            )

    creating_new_if = bool(module.params["interface"])

    if not HAS_NETADDR:
        module.fail_json(msg="netaddr module is required")

    array = get_system(module)
    if module.params["address"]:
        module.params["address"] = module.params["address"].strip("[]")
        if "/" not in module.params["address"]:
            module.fail_json(msg="address must include valid netmask bits")
    if module.params["gateway"]:
        module.params["gateway"] = module.params["gateway"].strip("[]")
    api_version = array._list_available_rest_versions()
    if not _is_cbs(array):
        if module.params["servicelist"] and "system" in module.params["servicelist"]:
            module.fail_json(
                msg="Only Cloud Block Store supports the 'system' service type"
            )
    if "." in module.params["name"]:
        if module.params["name"].split(".")[1][0].lower() == "f":
            if not HAS_PYPURECLIENT:
                module.fail_json(msg="pypureclient module is required")
            array = get_array(module)
            interface = _get_fc_interface(module, array)
            if not interface:
                module.fail_json(msg="Invalid network interface specified.")
            else:
                update_fc_interface(module, array, interface, api_version)
        else:
            interface = _get_interface(module, array)
            if not interface:
                module.fail_json(msg="Invalid network interface specified.")
            else:
                update_interface(module, array, interface)
    else:
        if (module.params["interface"] == "vif" and module.params["subordinates"]) or (
            module.params["interface"] == "lacp" and module.params["subinterfaces"]
        ):
            module.fail_json(
                msg="interface type not compatable with provided subinterfaces | subordinates"
            )
        interface = _get_interface(module, array)
        array6 = get_array(module)
        if not creating_new_if:
            if not interface:
                module.fail_json(msg="Invalid network interface specified.")
            elif module.params["state"] == "present":
                update_interface(module, array, interface)
            else:
                delete_interface(module, array6)
        elif not interface and module.params["state"] == "present":
            create_interface(module, array6)
        elif interface and module.params["state"] == "absent":
            delete_interface(module, array6)
        elif module.params["state"] == "present":
            update_interface(module, array, interface)
        else:
            module.exit_json(changed=False)

    module.exit_json(changed=False)


if __name__ == "__main__":
    main()
