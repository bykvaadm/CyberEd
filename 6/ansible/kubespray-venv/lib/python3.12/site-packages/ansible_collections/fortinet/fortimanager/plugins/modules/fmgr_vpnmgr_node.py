#!/usr/bin/python
from __future__ import absolute_import, division, print_function
# Copyright 2019-2024 Fortinet, Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

__metaclass__ = type

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.1'}

DOCUMENTATION = '''
---
module: fmgr_vpnmgr_node
short_description: VPN node for VPN Manager.
description:
    - This module is able to configure a FortiManager device.
    - Examples include all parameters and values which need to be adjusted to data sources before usage.

version_added: "2.0.0"
author:
    - Xinwei Du (@dux-fortinet)
    - Xing Li (@lix-fortinet)
    - Jie Xue (@JieX19)
    - Link Zheng (@chillancezen)
    - Frank Shen (@fshen01)
    - Hongbin Lu (@fgtdev-hblu)
notes:
    - Starting in version 2.4.0, all input arguments are named using the underscore naming convention (snake_case).
      Please change the arguments such as "var-name" to "var_name".
      Old argument names are still available yet you will receive deprecation warnings.
      You can ignore this warning by setting deprecation_warnings=False in ansible.cfg.
    - Running in workspace locking mode is supported in this FortiManager module, the top
      level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
    - To create or update an object, use state present directive.
    - To delete an object, use state absent directive.
    - Normally, running one module can fail when a non-zero rc is returned. you can also override
      the conditions to fail or succeed with parameters rc_failed and rc_succeeded
options:
    access_token:
        description: The token to access FortiManager without using username and password.
        type: str
    bypass_validation:
        description: Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.
        type: bool
        default: false
    enable_log:
        description: Enable/Disable logging for task.
        type: bool
        default: false
    forticloud_access_token:
        description: Authenticate Ansible client with forticloud API access token.
        type: str
    proposed_method:
        description: The overridden method for the underlying Json RPC request.
        type: str
        choices:
          - update
          - set
          - add
    rc_succeeded:
        description: The rc codes list with which the conditions to succeed will be overriden.
        type: list
        elements: int
    rc_failed:
        description: The rc codes list with which the conditions to fail will be overriden.
        type: list
        elements: int
    state:
        description: The directive to create, update or delete an object.
        type: str
        required: true
        choices:
          - present
          - absent
    workspace_locking_adom:
        description: The adom to lock for FortiManager running in workspace mode, the value can be global and others including root.
        type: str
    workspace_locking_timeout:
        description: The maximum time in seconds to wait for other user to release the workspace lock.
        type: int
        default: 300
    adom:
        description: The parameter (adom) in requested url.
        type: str
        required: true
    vpnmgr_node:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            add-route:
                type: str
                description: Deprecated, please rename it to add_route. Add route.
                choices:
                    - 'disable'
                    - 'enable'
            assign-ip:
                type: str
                description: Deprecated, please rename it to assign_ip. Assign ip.
                choices:
                    - 'disable'
                    - 'enable'
            assign-ip-from:
                type: str
                description: Deprecated, please rename it to assign_ip_from. Assign ip from.
                choices:
                    - 'range'
                    - 'usrgrp'
                    - 'dhcp'
                    - 'name'
            authpasswd:
                type: raw
                description: (list) Authpasswd.
            authusr:
                type: str
                description: Authusr.
            authusrgrp:
                type: str
                description: Authusrgrp.
            auto-configuration:
                type: str
                description: Deprecated, please rename it to auto_configuration. Auto configuration.
                choices:
                    - 'disable'
                    - 'enable'
            automatic_routing:
                type: str
                description: Automatic routing.
                choices:
                    - 'disable'
                    - 'enable'
            banner:
                type: str
                description: Banner.
            default-gateway:
                type: str
                description: Deprecated, please rename it to default_gateway. Default gateway.
            dhcp-server:
                type: str
                description: Deprecated, please rename it to dhcp_server. Dhcp server.
                choices:
                    - 'disable'
                    - 'enable'
            dns-mode:
                type: str
                description: Deprecated, please rename it to dns_mode. Dns mode.
                choices:
                    - 'auto'
                    - 'manual'
            dns-service:
                type: str
                description: Deprecated, please rename it to dns_service. Dns service.
                choices:
                    - 'default'
                    - 'specify'
                    - 'local'
            domain:
                type: str
                description: Domain.
            extgw:
                type: str
                description: Extgw.
            extgw_hubip:
                type: str
                description: Extgw hubip.
            extgw_p2_per_net:
                type: str
                description: Extgw p2 per net.
                choices:
                    - 'disable'
                    - 'enable'
            extgwip:
                type: str
                description: Extgwip.
            hub_iface:
                type: raw
                description: (list or str) Hub iface.
            id:
                type: int
                description: Id.
                required: true
            iface:
                type: raw
                description: (list or str) Iface.
            ip-range:
                type: list
                elements: dict
                description: Deprecated, please rename it to ip_range. Ip range.
                suboptions:
                    end-ip:
                        type: str
                        description: Deprecated, please rename it to end_ip. End ip.
                    id:
                        type: int
                        description: Id.
                    start-ip:
                        type: str
                        description: Deprecated, please rename it to start_ip. Start ip.
            ipsec-lease-hold:
                type: int
                description: Deprecated, please rename it to ipsec_lease_hold. Ipsec lease hold.
            ipv4-dns-server1:
                type: str
                description: Deprecated, please rename it to ipv4_dns_server1. Ipv4 dns server1.
            ipv4-dns-server2:
                type: str
                description: Deprecated, please rename it to ipv4_dns_server2. Ipv4 dns server2.
            ipv4-dns-server3:
                type: str
                description: Deprecated, please rename it to ipv4_dns_server3. Ipv4 dns server3.
            ipv4-end-ip:
                type: str
                description: Deprecated, please rename it to ipv4_end_ip. Ipv4 end ip.
            ipv4-exclude-range:
                type: list
                elements: dict
                description: Deprecated, please rename it to ipv4_exclude_range. Ipv4 exclude range.
                suboptions:
                    end-ip:
                        type: str
                        description: Deprecated, please rename it to end_ip. End ip.
                    id:
                        type: int
                        description: Id.
                    start-ip:
                        type: str
                        description: Deprecated, please rename it to start_ip. Start ip.
            ipv4-netmask:
                type: str
                description: Deprecated, please rename it to ipv4_netmask. Ipv4 netmask.
            ipv4-split-include:
                type: str
                description: Deprecated, please rename it to ipv4_split_include. Ipv4 split include.
            ipv4-start-ip:
                type: str
                description: Deprecated, please rename it to ipv4_start_ip. Ipv4 start ip.
            ipv4-wins-server1:
                type: str
                description: Deprecated, please rename it to ipv4_wins_server1. Ipv4 wins server1.
            ipv4-wins-server2:
                type: str
                description: Deprecated, please rename it to ipv4_wins_server2. Ipv4 wins server2.
            local-gw:
                type: str
                description: Deprecated, please rename it to local_gw. Local gw.
            localid:
                type: str
                description: Localid.
            mode-cfg:
                type: str
                description: Deprecated, please rename it to mode_cfg. Mode cfg.
                choices:
                    - 'disable'
                    - 'enable'
            mode-cfg-ip-version:
                type: str
                description: Deprecated, please rename it to mode_cfg_ip_version. Mode cfg ip version.
                choices:
                    - '4'
                    - '6'
            net-device:
                type: str
                description: Deprecated, please rename it to net_device. Net device.
                choices:
                    - 'disable'
                    - 'enable'
            peer:
                type: raw
                description: (list or str) Peer.
            peergrp:
                type: str
                description: Peergrp.
            peerid:
                type: str
                description: Peerid.
            peertype:
                type: str
                description: Peertype.
                choices:
                    - 'any'
                    - 'one'
                    - 'dialup'
                    - 'peer'
                    - 'peergrp'
            protected_subnet:
                type: list
                elements: dict
                description: Protected subnet.
                suboptions:
                    addr:
                        type: raw
                        description: (list or str) Addr.
                    seq:
                        type: int
                        description: Seq.
            public-ip:
                type: str
                description: Deprecated, please rename it to public_ip. Public ip.
            role:
                type: str
                description: Role.
                choices:
                    - 'hub'
                    - 'spoke'
            route-overlap:
                type: str
                description: Deprecated, please rename it to route_overlap. Route overlap.
                choices:
                    - 'use-old'
                    - 'use-new'
                    - 'allow'
            spoke-zone:
                type: raw
                description: (list or str) Deprecated, please rename it to spoke_zone. Spoke zone.
            summary_addr:
                type: list
                elements: dict
                description: Summary addr.
                suboptions:
                    addr:
                        type: str
                        description: Addr.
                    priority:
                        type: int
                        description: Priority.
                    seq:
                        type: int
                        description: Seq.
            tunnel-search:
                type: str
                description: Deprecated, please rename it to tunnel_search. Tunnel search.
                choices:
                    - 'selectors'
                    - 'nexthop'
            unity-support:
                type: str
                description: Deprecated, please rename it to unity_support. Unity support.
                choices:
                    - 'disable'
                    - 'enable'
            usrgrp:
                type: str
                description: Usrgrp.
            vpn-interface-priority:
                type: int
                description: Deprecated, please rename it to vpn_interface_priority. Vpn interface priority.
            vpn-zone:
                type: raw
                description: (list or str) Deprecated, please rename it to vpn_zone. Vpn zone.
            vpntable:
                type: raw
                description: (list or str) Vpntable.
            xauthtype:
                type: str
                description: Xauthtype.
                choices:
                    - 'disable'
                    - 'client'
                    - 'pap'
                    - 'chap'
                    - 'auto'
            exchange-interface-ip:
                type: str
                description: Deprecated, please rename it to exchange_interface_ip. Exchange interface ip.
                choices:
                    - 'disable'
                    - 'enable'
            hub-public-ip:
                type: str
                description: Deprecated, please rename it to hub_public_ip. Hub public ip.
            ipv4-split-exclude:
                type: str
                description: Deprecated, please rename it to ipv4_split_exclude. Ipv4 split exclude.
            scope member:
                type: list
                elements: dict
                description: Deprecated, please rename it to scope_member. Scope member.
                suboptions:
                    name:
                        type: str
                        description: Name.
                    vdom:
                        type: str
                        description: Vdom.
            dhcp-ra-giaddr:
                type: str
                description: Deprecated, please rename it to dhcp_ra_giaddr. Dhcp ra giaddr.
            encapsulation:
                type: str
                description: Encapsulation.
                choices:
                    - 'tunnel-mode'
                    - 'transport-mode'
            ipv4-name:
                type: str
                description: Deprecated, please rename it to ipv4_name. Ipv4 name.
            l2tp:
                type: str
                description: L2tp.
                choices:
                    - 'disable'
                    - 'enable'
            auto-discovery-receiver:
                type: str
                description: Deprecated, please rename it to auto_discovery_receiver. Auto discovery receiver.
                choices:
                    - 'disable'
                    - 'enable'
            auto-discovery-sender:
                type: str
                description: Deprecated, please rename it to auto_discovery_sender. Auto discovery sender.
                choices:
                    - 'disable'
                    - 'enable'
            network-id:
                type: int
                description: Deprecated, please rename it to network_id. Network id.
            network-overlay:
                type: str
                description: Deprecated, please rename it to network_overlay. Network overlay.
                choices:
                    - 'enable'
                    - 'disable'
            protocol:
                type: int
                description: Protocol.
'''

EXAMPLES = '''
- name: Example playbook (generated based on argument schema)
  hosts: fortimanagers
  connection: httpapi
  vars:
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_httpapi_port: 443
  tasks:
    - name: VPN node for VPN Manager.
      fortinet.fortimanager.fmgr_vpnmgr_node:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: present # <value in [present, absent]>
        vpnmgr_node:
          add_route: <value in [disable, enable]>
          assign_ip: <value in [disable, enable]>
          assign_ip_from: <value in [range, usrgrp, dhcp, ...]>
          authpasswd: <list or string>
          authusr: <string>
          authusrgrp: <string>
          auto_configuration: <value in [disable, enable]>
          automatic_routing: <value in [disable, enable]>
          banner: <string>
          default_gateway: <string>
          dhcp_server: <value in [disable, enable]>
          dns_mode: <value in [auto, manual]>
          dns_service: <value in [default, specify, local]>
          domain: <string>
          extgw: <string>
          extgw_hubip: <string>
          extgw_p2_per_net: <value in [disable, enable]>
          extgwip: <string>
          hub_iface: <list or string>
          id: <integer>
          iface: <list or string>
          ip_range:
            -
              end_ip: <string>
              id: <integer>
              start_ip: <string>
          ipsec_lease_hold: <integer>
          ipv4_dns_server1: <string>
          ipv4_dns_server2: <string>
          ipv4_dns_server3: <string>
          ipv4_end_ip: <string>
          ipv4_exclude_range:
            -
              end_ip: <string>
              id: <integer>
              start_ip: <string>
          ipv4_netmask: <string>
          ipv4_split_include: <string>
          ipv4_start_ip: <string>
          ipv4_wins_server1: <string>
          ipv4_wins_server2: <string>
          local_gw: <string>
          localid: <string>
          mode_cfg: <value in [disable, enable]>
          mode_cfg_ip_version: <value in [4, 6]>
          net_device: <value in [disable, enable]>
          peer: <list or string>
          peergrp: <string>
          peerid: <string>
          peertype: <value in [any, one, dialup, ...]>
          protected_subnet:
            -
              addr: <list or string>
              seq: <integer>
          public_ip: <string>
          role: <value in [hub, spoke]>
          route_overlap: <value in [use-old, use-new, allow]>
          spoke_zone: <list or string>
          summary_addr:
            -
              addr: <string>
              priority: <integer>
              seq: <integer>
          tunnel_search: <value in [selectors, nexthop]>
          unity_support: <value in [disable, enable]>
          usrgrp: <string>
          vpn_interface_priority: <integer>
          vpn_zone: <list or string>
          vpntable: <list or string>
          xauthtype: <value in [disable, client, pap, ...]>
          exchange_interface_ip: <value in [disable, enable]>
          hub_public_ip: <string>
          ipv4_split_exclude: <string>
          scope_member:
            -
              name: <string>
              vdom: <string>
          dhcp_ra_giaddr: <string>
          encapsulation: <value in [tunnel-mode, transport-mode]>
          ipv4_name: <string>
          l2tp: <value in [disable, enable]>
          auto_discovery_receiver: <value in [disable, enable]>
          auto_discovery_sender: <value in [disable, enable]>
          network_id: <integer>
          network_overlay: <value in [enable, disable]>
          protocol: <integer>
'''

RETURN = '''
meta:
    description: The result of the request.
    type: dict
    returned: always
    contains:
        request_url:
            description: The full url requested.
            returned: always
            type: str
            sample: /sys/login/user
        response_code:
            description: The status of api request.
            returned: always
            type: int
            sample: 0
        response_data:
            description: The api response.
            type: list
            returned: always
        response_message:
            description: The descriptive message of the api response.
            type: str
            returned: always
            sample: OK.
        system_information:
            description: The information of the target system.
            type: dict
            returned: always
rc:
    description: The status the request.
    type: int
    returned: always
    sample: 0
version_check_warning:
    description: Warning if the parameters used in the playbook are not supported by the current FortiManager version.
    type: list
    returned: complex
'''
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.fortinet.fortimanager.plugins.module_utils.napi import NAPIManager
from ansible_collections.fortinet.fortimanager.plugins.module_utils.napi import check_galaxy_version
from ansible_collections.fortinet.fortimanager.plugins.module_utils.napi import check_parameter_bypass
from ansible_collections.fortinet.fortimanager.plugins.module_utils.common import get_module_arg_spec


def main():
    jrpc_urls = [
        '/pm/config/adom/{adom}/obj/vpnmgr/node',
        '/pm/config/global/obj/vpnmgr/node'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/vpnmgr/node/{node}',
        '/pm/config/global/obj/vpnmgr/node/{node}'
    ]

    url_params = ['adom']
    module_primary_key = 'id'
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'vpnmgr_node': {
            'type': 'dict',
            'v_range': [['6.0.0', '']],
            'options': {
                'add-route': {'choices': ['disable', 'enable'], 'type': 'str'},
                'assign-ip': {'choices': ['disable', 'enable'], 'type': 'str'},
                'assign-ip-from': {'choices': ['range', 'usrgrp', 'dhcp', 'name'], 'type': 'str'},
                'authpasswd': {'no_log': True, 'type': 'raw'},
                'authusr': {'type': 'str'},
                'authusrgrp': {'type': 'str'},
                'auto-configuration': {'choices': ['disable', 'enable'], 'type': 'str'},
                'automatic_routing': {'choices': ['disable', 'enable'], 'type': 'str'},
                'banner': {'type': 'str'},
                'default-gateway': {'type': 'str'},
                'dhcp-server': {'choices': ['disable', 'enable'], 'type': 'str'},
                'dns-mode': {'choices': ['auto', 'manual'], 'type': 'str'},
                'dns-service': {'choices': ['default', 'specify', 'local'], 'type': 'str'},
                'domain': {'type': 'str'},
                'extgw': {'type': 'str'},
                'extgw_hubip': {'type': 'str'},
                'extgw_p2_per_net': {'choices': ['disable', 'enable'], 'type': 'str'},
                'extgwip': {'type': 'str'},
                'hub_iface': {'type': 'raw'},
                'id': {'required': True, 'type': 'int'},
                'iface': {'type': 'raw'},
                'ip-range': {
                    'type': 'list',
                    'options': {'end-ip': {'type': 'str'}, 'id': {'type': 'int'}, 'start-ip': {'type': 'str'}},
                    'elements': 'dict'
                },
                'ipsec-lease-hold': {'type': 'int'},
                'ipv4-dns-server1': {'type': 'str'},
                'ipv4-dns-server2': {'type': 'str'},
                'ipv4-dns-server3': {'type': 'str'},
                'ipv4-end-ip': {'type': 'str'},
                'ipv4-exclude-range': {
                    'type': 'list',
                    'options': {'end-ip': {'type': 'str'}, 'id': {'type': 'int'}, 'start-ip': {'type': 'str'}},
                    'elements': 'dict'
                },
                'ipv4-netmask': {'type': 'str'},
                'ipv4-split-include': {'type': 'str'},
                'ipv4-start-ip': {'type': 'str'},
                'ipv4-wins-server1': {'type': 'str'},
                'ipv4-wins-server2': {'type': 'str'},
                'local-gw': {'type': 'str'},
                'localid': {'type': 'str'},
                'mode-cfg': {'choices': ['disable', 'enable'], 'type': 'str'},
                'mode-cfg-ip-version': {'choices': ['4', '6'], 'type': 'str'},
                'net-device': {'choices': ['disable', 'enable'], 'type': 'str'},
                'peer': {'type': 'raw'},
                'peergrp': {'type': 'str'},
                'peerid': {'type': 'str'},
                'peertype': {'choices': ['any', 'one', 'dialup', 'peer', 'peergrp'], 'type': 'str'},
                'protected_subnet': {'type': 'list', 'options': {'addr': {'type': 'raw'}, 'seq': {'type': 'int'}}, 'elements': 'dict'},
                'public-ip': {'type': 'str'},
                'role': {'choices': ['hub', 'spoke'], 'type': 'str'},
                'route-overlap': {'choices': ['use-old', 'use-new', 'allow'], 'type': 'str'},
                'spoke-zone': {'type': 'raw'},
                'summary_addr': {
                    'type': 'list',
                    'options': {'addr': {'type': 'str'}, 'priority': {'type': 'int'}, 'seq': {'type': 'int'}},
                    'elements': 'dict'
                },
                'tunnel-search': {'choices': ['selectors', 'nexthop'], 'type': 'str'},
                'unity-support': {'choices': ['disable', 'enable'], 'type': 'str'},
                'usrgrp': {'type': 'str'},
                'vpn-interface-priority': {'type': 'int'},
                'vpn-zone': {'type': 'raw'},
                'vpntable': {'type': 'raw'},
                'xauthtype': {'choices': ['disable', 'client', 'pap', 'chap', 'auto'], 'type': 'str'},
                'exchange-interface-ip': {'v_range': [['6.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'hub-public-ip': {'v_range': [['6.2.2', '']], 'type': 'str'},
                'ipv4-split-exclude': {'v_range': [['6.4.6', '']], 'type': 'str'},
                'scope member': {
                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                    'type': 'list',
                    'options': {
                        'name': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'str'},
                        'vdom': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'str'}
                    },
                    'elements': 'dict'
                },
                'dhcp-ra-giaddr': {'v_range': [['6.4.8', '6.4.14'], ['7.0.4', '']], 'type': 'str'},
                'encapsulation': {'v_range': [['7.0.2', '']], 'choices': ['tunnel-mode', 'transport-mode'], 'type': 'str'},
                'ipv4-name': {'v_range': [['6.4.8', '6.4.14'], ['7.0.4', '']], 'type': 'str'},
                'l2tp': {'v_range': [['7.0.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'auto-discovery-receiver': {'v_range': [['7.0.8', '7.0.12'], ['7.2.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'auto-discovery-sender': {'v_range': [['7.0.8', '7.0.12'], ['7.2.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'network-id': {'v_range': [['7.0.8', '7.0.12'], ['7.2.3', '']], 'type': 'int'},
                'network-overlay': {'v_range': [['7.0.8', '7.0.12'], ['7.2.3', '']], 'choices': ['enable', 'disable'], 'type': 'str'},
                'protocol': {'v_range': [['7.2.5', '7.2.5'], ['7.4.1', '']], 'type': 'int'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('full crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'vpnmgr_node'),
                           supports_check_mode=True)

    if not module._socket_path:
        module.fail_json(msg='MUST RUN IN HTTPAPI MODE')
    connection = Connection(module._socket_path)
    fmgr = NAPIManager(jrpc_urls, perobject_jrpc_urls, module_primary_key, url_params, module, connection, top_level_schema_name='data')
    fmgr.validate_parameters(params_validation_blob)
    fmgr.process_curd(argument_specs=module_arg_spec)

    module.exit_json(meta=module.params)


if __name__ == '__main__':
    main()
