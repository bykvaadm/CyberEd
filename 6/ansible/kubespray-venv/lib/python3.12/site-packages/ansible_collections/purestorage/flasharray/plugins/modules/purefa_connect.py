#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2018, Simon Dodsley (simon@purestorage.com)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: purefa_connect
version_added: '1.0.0'
short_description: Manage replication connections between two FlashArrays
description:
- Manage array connections to specified target array
author:
- Pure Storage Ansible Team (@sdodsley) <pure-ansible-team@purestorage.com>
options:
  state:
    description:
    - Create or delete array connection
    default: present
    type: str
    choices: [ absent, present ]
  target_url:
    description:
    - Management IP address of remote array.
    type: str
    required: true
  target_api:
    description:
    - API token for target array
    type: str
  connection:
    description:
    - Type of connection between arrays.
    type: str
    choices: [ sync, async ]
    default: async
  transport:
    description:
    - Type of transport protocol to use for replication
    type: str
    choices: [ ip, fc ]
    default: ip
  encrypted:
    description:
    - Defines if the array connection will be encryted
    type: bool
    default: false
    version_added: '1.30.0'
extends_documentation_fragment:
- purestorage.flasharray.purestorage.fa
"""

EXAMPLES = r"""
- name: Create an IPv4 async connection to remote array
  purestorage.flasharray.purefa_connect:
    target_url: 10.10.10.20
    target_api: 9c0b56bc-f941-f7a6-9f85-dcc3e9a8f7d6
    connection: async
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
- name: Create an IPv6 async connection to remote array
  purestorage.flasharray.purefa_connect:
    target_url: "[2001:db8:abcd:12::10]"
    target_api: 9c0b56bc-f941-f7a6-9f85-dcc3e9a8f7d6
    connection: async
    fa_url: "[2001:db8:abcd:12::13]"
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
- name: Delete connection to remote array
  purestorage.flasharray.purefa_connect:
    state: absent
    target_url: 10.10.10.20
    target_api: 9c0b56bc-f941-f7a6-9f85-dcc3e9a8f7d6
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
"""

RETURN = r"""
"""

HAS_PYPURECLIENT = True
try:
    from pypureclient import flasharray
except ImportError:
    HAS_PYPURECLIENT = False

HAS_DISTRO = True
try:
    import distro
except ImportError:
    HAS_DISTRO = False

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.purestorage.flasharray.plugins.module_utils.purefa import (
    get_array,
    purefa_argument_spec,
)
from ansible_collections.purestorage.flasharray.plugins.module_utils.version import (
    LooseVersion,
)
import platform
import socket


ENCRYPT_VERSION = "2.33"


def _lookup(address):
    """Perform Reverse DNS lookup on IP address"""
    fqdn = socket.getnameinfo((address, 0), 0)[0]
    shortname = fqdn.split(".")[0]
    return shortname, fqdn


def _check_connected(module, array):
    res = array.get_array_connections()
    if res.status_code != 200:
        return None
    else:
        connected_arrays = list(res.items)
        for target in range(0, len(connected_arrays)):
            remote_mgmt_address = connected_arrays[target].management_address
            if (
                remote_mgmt_address == module.params["target_url"].strip("[]")
                or remote_mgmt_address
                in [_lookup(module.params["target_url"].strip("[]"))]
                and "connected" in connected_arrays[target].status
            ):
                return connected_arrays[target]
        return None


def break_connection(module, array, target_array):
    """Break connection between arrays"""
    changed = True
    source_array = list(array.get_arrays().items)[0].name
    if getattr(target_array, "management_address", None) is None:
        module.fail_json(
            msg="disconnect can only happen from the array that formed the connection"
        )
    if not module.check_mode:
        res = array.delete_array_connections(names=[target_array.name])
        if res.status_code != 200:
            module.fail_json(
                msg="Failed to disconnect {0} from {1}.Error: {2}".format(
                    target_array.name,
                    source_array,
                    res.errors[0].mesaage,
                )
            )
    module.exit_json(changed=changed)


def create_connection(module, array):
    """Create connection between arrays"""
    changed = True
    api_version = array.get_rest_version()
    if HAS_DISTRO:
        user_agent = "%(base)s %(class)s/%(version)s (%(platform)s)" % {
            "base": "Ansible",
            "class": __name__,
            "version": 1.5,
            "platform": distro.name(pretty=True),
        }
    else:
        user_agent = "%(base)s %(class)s/%(version)s (%(platform)s)" % {
            "base": "Ansible",
            "class": __name__,
            "version": 1.5,
            "platform": platform.platform(),
        }
    try:
        remote_system = flasharray.Client(
            target=module.params["target_url"],
            api_token=module.params["target_api"],
            user_agent=user_agent,
        )
        connection_key = list(
            remote_system.get_array_connections_connection_key().items
        )[0].connection_key
        remote_array = list(remote_system.get_arrays().items)[0].name
        # TODO: Refactor when FC async is supported
        if (
            module.params["transport"].lower() == "fc"
            and module.params["connection"].lower() == "async"
        ):
            module.fail_json(
                msg="Asynchronous replication not supported using FC transport"
            )
        if LooseVersion(ENCRYPT_VERSION) >= LooseVersion(api_version):
            if module.params["encrypted"]:
                encrypted = "encrypted"
            else:
                encrypted = "unencrypted"
            array_connection = flasharray.ArrayConnectionPost(
                type=module.params["connection"].lower(),
                management_address=module.params["target_url"].strip("[]"),
                replication_transport=module.params["connection"],
                connection_key=connection_key,
                encypted=encrypted,
            )
        else:
            array_connection = flasharray.ArrayConnectionPost(
                type=module.params["connection"].lower(),
                management_address=module.params["target_url"].strip("[]"),
                replication_transport=module.params["connection"],
                connection_key=connection_key,
            )
        if not module.check_mode:
            res = array.post_array_connections(array_connection=array_connection)
            if res.status_code != 200:
                module.fail_json(
                    msg="Array Connection failed. Error: {0}".format(
                        res.errors[0].message
                    )
                )
    except Exception:
        module.fail_json(
            msg="Failed to connect to remote array {0}.".format(
                module.params["target_url"]
            )
        )
    module.exit_json(changed=changed)


def main():
    argument_spec = purefa_argument_spec()
    argument_spec.update(
        dict(
            state=dict(type="str", default="present", choices=["absent", "present"]),
            connection=dict(type="str", default="async", choices=["async", "sync"]),
            transport=dict(type="str", default="ip", choices=["ip", "fc"]),
            target_url=dict(type="str", required=True),
            target_api=dict(type="str"),
            encrypted=dict(type="bool", default=False),
        )
    )

    required_if = [("state", "present", ["target_api"])]

    module = AnsibleModule(
        argument_spec, required_if=required_if, supports_check_mode=True
    )

    if not HAS_PYPURECLIENT:
        module.fail_json(msg="pypureclient sdk is required for this module")

    state = module.params["state"]
    array = get_array(module)
    target_array = _check_connected(module, array)

    if state == "present" and target_array is None:
        create_connection(module, array)
    elif state == "absent" and target_array is not None:
        break_connection(module, array, target_array)

    module.exit_json(changed=False)


if __name__ == "__main__":
    main()
