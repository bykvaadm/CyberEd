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
module: fmgr_system_dhcp_server
short_description: Configure DHCP servers.
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
    system_dhcp_server:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            auto-configuration:
                type: str
                description: Deprecated, please rename it to auto_configuration. Enable/disable auto configuration.
                choices:
                    - 'disable'
                    - 'enable'
            conflicted-ip-timeout:
                type: int
                description: Deprecated, please rename it to conflicted_ip_timeout. Time in seconds to wait after a conflicted IP address is removed fr...
            ddns-auth:
                type: str
                description: Deprecated, please rename it to ddns_auth. DDNS authentication mode.
                choices:
                    - 'disable'
                    - 'tsig'
            ddns-key:
                type: raw
                description: (list or str) Deprecated, please rename it to ddns_key. DDNS update key
            ddns-keyname:
                type: str
                description: Deprecated, please rename it to ddns_keyname. DDNS update key name.
            ddns-server-ip:
                type: str
                description: Deprecated, please rename it to ddns_server_ip. DDNS server IP.
            ddns-ttl:
                type: int
                description: Deprecated, please rename it to ddns_ttl. TTL.
            ddns-update:
                type: str
                description: Deprecated, please rename it to ddns_update. Enable/disable DDNS update for DHCP.
                choices:
                    - 'disable'
                    - 'enable'
            ddns-update-override:
                type: str
                description: Deprecated, please rename it to ddns_update_override. Enable/disable DDNS update override for DHCP.
                choices:
                    - 'disable'
                    - 'enable'
            ddns-zone:
                type: str
                description: Deprecated, please rename it to ddns_zone. Zone of your domain name
            default-gateway:
                type: str
                description: Deprecated, please rename it to default_gateway. Default gateway IP address assigned by the DHCP server.
            dns-server1:
                type: str
                description: Deprecated, please rename it to dns_server1. DNS server 1.
            dns-server2:
                type: str
                description: Deprecated, please rename it to dns_server2. DNS server 2.
            dns-server3:
                type: str
                description: Deprecated, please rename it to dns_server3. DNS server 3.
            dns-service:
                type: str
                description: Deprecated, please rename it to dns_service. Options for assigning DNS servers to DHCP clients.
                choices:
                    - 'default'
                    - 'specify'
                    - 'local'
            domain:
                type: str
                description: Domain name suffix for the IP addresses that the DHCP server assigns to clients.
            exclude-range:
                type: list
                elements: dict
                description: Deprecated, please rename it to exclude_range. Exclude range.
                suboptions:
                    end-ip:
                        type: str
                        description: Deprecated, please rename it to end_ip. End of IP range.
                    id:
                        type: int
                        description: ID.
                    start-ip:
                        type: str
                        description: Deprecated, please rename it to start_ip. Start of IP range.
                    vci-match:
                        type: str
                        description: Deprecated, please rename it to vci_match. Enable/disable vendor class identifier
                        choices:
                            - 'disable'
                            - 'enable'
                    vci-string:
                        type: raw
                        description: (list) Deprecated, please rename it to vci_string. One or more VCI strings in quotes separated by spaces.
                    lease-time:
                        type: int
                        description: Deprecated, please rename it to lease_time. Lease time in seconds, 0 means default lease time.
                    uci-match:
                        type: str
                        description: Deprecated, please rename it to uci_match. Enable/disable user class identifier
                        choices:
                            - 'disable'
                            - 'enable'
                    uci-string:
                        type: raw
                        description: (list) Deprecated, please rename it to uci_string. One or more UCI strings in quotes separated by spaces.
            filename:
                type: str
                description: Name of the boot file on the TFTP server.
            forticlient-on-net-status:
                type: str
                description: Deprecated, please rename it to forticlient_on_net_status. Enable/disable FortiClient-On-Net service for this DHCP server.
                choices:
                    - 'disable'
                    - 'enable'
            id:
                type: int
                description: ID.
                required: true
            interface:
                type: str
                description: DHCP server can assign IP configurations to clients connected to this interface.
            ip-mode:
                type: str
                description: Deprecated, please rename it to ip_mode. Method used to assign client IP.
                choices:
                    - 'range'
                    - 'usrgrp'
            ip-range:
                type: list
                elements: dict
                description: Deprecated, please rename it to ip_range. Ip range.
                suboptions:
                    end-ip:
                        type: str
                        description: Deprecated, please rename it to end_ip. End of IP range.
                    id:
                        type: int
                        description: ID.
                    start-ip:
                        type: str
                        description: Deprecated, please rename it to start_ip. Start of IP range.
                    vci-match:
                        type: str
                        description: Deprecated, please rename it to vci_match. Enable/disable vendor class identifier
                        choices:
                            - 'disable'
                            - 'enable'
                    vci-string:
                        type: raw
                        description: (list) Deprecated, please rename it to vci_string. One or more VCI strings in quotes separated by spaces.
                    lease-time:
                        type: int
                        description: Deprecated, please rename it to lease_time. Lease time in seconds, 0 means default lease time.
                    uci-match:
                        type: str
                        description: Deprecated, please rename it to uci_match. Enable/disable user class identifier
                        choices:
                            - 'disable'
                            - 'enable'
                    uci-string:
                        type: raw
                        description: (list) Deprecated, please rename it to uci_string. One or more UCI strings in quotes separated by spaces.
            ipsec-lease-hold:
                type: int
                description: Deprecated, please rename it to ipsec_lease_hold. DHCP over IPsec leases expire this many seconds after tunnel down
            lease-time:
                type: int
                description: Deprecated, please rename it to lease_time. Lease time in seconds, 0 means unlimited.
            mac-acl-default-action:
                type: str
                description: Deprecated, please rename it to mac_acl_default_action. MAC access control default action
                choices:
                    - 'assign'
                    - 'block'
            netmask:
                type: str
                description: Netmask assigned by the DHCP server.
            next-server:
                type: str
                description: Deprecated, please rename it to next_server. IP address of a server
            ntp-server1:
                type: str
                description: Deprecated, please rename it to ntp_server1. NTP server 1.
            ntp-server2:
                type: str
                description: Deprecated, please rename it to ntp_server2. NTP server 2.
            ntp-server3:
                type: str
                description: Deprecated, please rename it to ntp_server3. NTP server 3.
            ntp-service:
                type: str
                description: Deprecated, please rename it to ntp_service. Options for assigning Network Time Protocol
                choices:
                    - 'default'
                    - 'specify'
                    - 'local'
            options:
                type: list
                elements: dict
                description: Options.
                suboptions:
                    code:
                        type: int
                        description: DHCP option code.
                    id:
                        type: int
                        description: ID.
                    ip:
                        type: raw
                        description: (list) DHCP option IPs.
                    type:
                        type: str
                        description: DHCP option type.
                        choices:
                            - 'hex'
                            - 'string'
                            - 'ip'
                            - 'fqdn'
                    value:
                        type: str
                        description: DHCP option value.
                    vci-match:
                        type: str
                        description: Deprecated, please rename it to vci_match. Enable/disable vendor class identifier
                        choices:
                            - 'disable'
                            - 'enable'
                    vci-string:
                        type: raw
                        description: (list) Deprecated, please rename it to vci_string. One or more VCI strings in quotes separated by spaces.
                    uci-match:
                        type: str
                        description: Deprecated, please rename it to uci_match. Enable/disable user class identifier
                        choices:
                            - 'disable'
                            - 'enable'
                    uci-string:
                        type: raw
                        description: (list) Deprecated, please rename it to uci_string. One or more UCI strings in quotes separated by spaces.
            reserved-address:
                type: list
                elements: dict
                description: Deprecated, please rename it to reserved_address. Reserved address.
                suboptions:
                    action:
                        type: str
                        description: Options for the DHCP server to configure the client with the reserved MAC address.
                        choices:
                            - 'assign'
                            - 'block'
                            - 'reserved'
                    description:
                        type: str
                        description: Description.
                    id:
                        type: int
                        description: ID.
                    ip:
                        type: str
                        description: IP address to be reserved for the MAC address.
                    mac:
                        type: str
                        description: MAC address of the client that will get the reserved IP address.
                    circuit-id:
                        type: str
                        description: Deprecated, please rename it to circuit_id. Option 82 circuit-ID of the client that will get the reserved IP address.
                    circuit-id-type:
                        type: str
                        description: Deprecated, please rename it to circuit_id_type. DHCP option type.
                        choices:
                            - 'hex'
                            - 'string'
                    remote-id:
                        type: str
                        description: Deprecated, please rename it to remote_id. Option 82 remote-ID of the client that will get the reserved IP address.
                    remote-id-type:
                        type: str
                        description: Deprecated, please rename it to remote_id_type. DHCP option type.
                        choices:
                            - 'hex'
                            - 'string'
                    type:
                        type: str
                        description: DHCP reserved-address type.
                        choices:
                            - 'mac'
                            - 'option82'
            server-type:
                type: str
                description: Deprecated, please rename it to server_type. DHCP server can be a normal DHCP server or an IPsec DHCP server.
                choices:
                    - 'regular'
                    - 'ipsec'
            status:
                type: str
                description: Enable/disable this DHCP configuration.
                choices:
                    - 'disable'
                    - 'enable'
            tftp-server:
                type: raw
                description: (list) Deprecated, please rename it to tftp_server. One or more hostnames or IP addresses of the TFTP servers in quotes se...
            timezone:
                type: str
                description: Select the time zone to be assigned to DHCP clients.
                choices:
                    - '00'
                    - '01'
                    - '02'
                    - '03'
                    - '04'
                    - '05'
                    - '06'
                    - '07'
                    - '08'
                    - '09'
                    - '10'
                    - '11'
                    - '12'
                    - '13'
                    - '14'
                    - '15'
                    - '16'
                    - '17'
                    - '18'
                    - '19'
                    - '20'
                    - '21'
                    - '22'
                    - '23'
                    - '24'
                    - '25'
                    - '26'
                    - '27'
                    - '28'
                    - '29'
                    - '30'
                    - '31'
                    - '32'
                    - '33'
                    - '34'
                    - '35'
                    - '36'
                    - '37'
                    - '38'
                    - '39'
                    - '40'
                    - '41'
                    - '42'
                    - '43'
                    - '44'
                    - '45'
                    - '46'
                    - '47'
                    - '48'
                    - '49'
                    - '50'
                    - '51'
                    - '52'
                    - '53'
                    - '54'
                    - '55'
                    - '56'
                    - '57'
                    - '58'
                    - '59'
                    - '60'
                    - '61'
                    - '62'
                    - '63'
                    - '64'
                    - '65'
                    - '66'
                    - '67'
                    - '68'
                    - '69'
                    - '70'
                    - '71'
                    - '72'
                    - '73'
                    - '74'
                    - '75'
                    - '76'
                    - '77'
                    - '78'
                    - '79'
                    - '80'
                    - '81'
                    - '82'
                    - '83'
                    - '84'
                    - '85'
                    - '86'
                    - '87'
            timezone-option:
                type: str
                description: Deprecated, please rename it to timezone_option. Options for the DHCP server to set the clients time zone.
                choices:
                    - 'disable'
                    - 'default'
                    - 'specify'
            vci-match:
                type: str
                description: Deprecated, please rename it to vci_match. Enable/disable vendor class identifier
                choices:
                    - 'disable'
                    - 'enable'
            vci-string:
                type: raw
                description: (list) Deprecated, please rename it to vci_string. One or more VCI strings in quotes separated by spaces.
            wifi-ac1:
                type: str
                description: Deprecated, please rename it to wifi_ac1. WiFi Access Controller 1 IP address
            wifi-ac2:
                type: str
                description: Deprecated, please rename it to wifi_ac2. WiFi Access Controller 2 IP address
            wifi-ac3:
                type: str
                description: Deprecated, please rename it to wifi_ac3. WiFi Access Controller 3 IP address
            wins-server1:
                type: str
                description: Deprecated, please rename it to wins_server1. WINS server 1.
            wins-server2:
                type: str
                description: Deprecated, please rename it to wins_server2. WINS server 2.
            dns-server4:
                type: str
                description: Deprecated, please rename it to dns_server4. DNS server 4.
            wifi-ac-service:
                type: str
                description: Deprecated, please rename it to wifi_ac_service. Options for assigning WiFi Access Controllers to DHCP clients
                choices:
                    - 'specify'
                    - 'local'
            auto-managed-status:
                type: str
                description: Deprecated, please rename it to auto_managed_status. Enable/disable use of this DHCP server once this interface has been a...
                choices:
                    - 'disable'
                    - 'enable'
            dhcp-settings-from-fortiipam:
                type: str
                description: Deprecated, please rename it to dhcp_settings_from_fortiipam. Enable/disable populating of DHCP server settings from Forti...
                choices:
                    - 'disable'
                    - 'enable'
            relay-agent:
                type: str
                description: Deprecated, please rename it to relay_agent. Relay agent IP.
            shared-subnet:
                type: str
                description: Deprecated, please rename it to shared_subnet. Enable/disable shared subnet.
                choices:
                    - 'disable'
                    - 'enable'
'''

EXAMPLES = '''
- name: Example playbook
  hosts: fortimanagers
  connection: httpapi
  vars:
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_httpapi_port: 443
  tasks:
    - name: Configure DHCP servers.
      fortinet.fortimanager.fmgr_system_dhcp_server:
        bypass_validation: false
        adom: ansible
        state: present
        system_dhcp_server:
          auto-configuration: enable # <value in [disable, enable]>
          default-gateway: "222.222.222.1"
          filename: ansible-file
          id: 1
          interface: any
          ip-mode: range # <value in [range, usrgrp]>
          ip-range:
            - end-ip: 222.222.222.22
              id: 1
              start-ip: 222.222.222.2
          netmask: 255.255.255.0
          server-type: regular # <value in [regular, ipsec]>
          status: disable # <value in [disable, enable]>

- name: Gathering fortimanager facts
  hosts: fortimanagers
  gather_facts: false
  connection: httpapi
  vars:
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_httpapi_port: 443
  tasks:
    - name: Retrieve all the DHCP servers
      fortinet.fortimanager.fmgr_fact:
        facts:
          selector: "system_dhcp_server"
          params:
            adom: "ansible"
            server: "your_value"
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
        '/pm/config/adom/{adom}/obj/system/dhcp/server',
        '/pm/config/global/obj/system/dhcp/server'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/system/dhcp/server/{server}',
        '/pm/config/global/obj/system/dhcp/server/{server}'
    ]

    url_params = ['adom']
    module_primary_key = 'id'
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'system_dhcp_server': {
            'type': 'dict',
            'v_range': [['6.0.0', '']],
            'options': {
                'auto-configuration': {'choices': ['disable', 'enable'], 'type': 'str'},
                'conflicted-ip-timeout': {'type': 'int'},
                'ddns-auth': {'choices': ['disable', 'tsig'], 'type': 'str'},
                'ddns-key': {'no_log': True, 'type': 'raw'},
                'ddns-keyname': {'no_log': True, 'type': 'str'},
                'ddns-server-ip': {'type': 'str'},
                'ddns-ttl': {'type': 'int'},
                'ddns-update': {'choices': ['disable', 'enable'], 'type': 'str'},
                'ddns-update-override': {'choices': ['disable', 'enable'], 'type': 'str'},
                'ddns-zone': {'type': 'str'},
                'default-gateway': {'type': 'str'},
                'dns-server1': {'type': 'str'},
                'dns-server2': {'type': 'str'},
                'dns-server3': {'type': 'str'},
                'dns-service': {'choices': ['default', 'specify', 'local'], 'type': 'str'},
                'domain': {'type': 'str'},
                'exclude-range': {
                    'type': 'list',
                    'options': {
                        'end-ip': {'type': 'str'},
                        'id': {'type': 'int'},
                        'start-ip': {'type': 'str'},
                        'vci-match': {'v_range': [['7.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'vci-string': {'v_range': [['7.2.1', '']], 'type': 'raw'},
                        'lease-time': {'v_range': [['7.2.2', '']], 'type': 'int'},
                        'uci-match': {'v_range': [['7.2.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'uci-string': {'v_range': [['7.2.2', '']], 'type': 'raw'}
                    },
                    'elements': 'dict'
                },
                'filename': {'type': 'str'},
                'forticlient-on-net-status': {'choices': ['disable', 'enable'], 'type': 'str'},
                'id': {'required': True, 'type': 'int'},
                'interface': {'type': 'str'},
                'ip-mode': {'choices': ['range', 'usrgrp'], 'type': 'str'},
                'ip-range': {
                    'type': 'list',
                    'options': {
                        'end-ip': {'type': 'str'},
                        'id': {'type': 'int'},
                        'start-ip': {'type': 'str'},
                        'vci-match': {'v_range': [['7.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'vci-string': {'v_range': [['7.2.1', '']], 'type': 'raw'},
                        'lease-time': {'v_range': [['7.2.2', '']], 'type': 'int'},
                        'uci-match': {'v_range': [['7.2.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'uci-string': {'v_range': [['7.2.2', '']], 'type': 'raw'}
                    },
                    'elements': 'dict'
                },
                'ipsec-lease-hold': {'type': 'int'},
                'lease-time': {'type': 'int'},
                'mac-acl-default-action': {'choices': ['assign', 'block'], 'type': 'str'},
                'netmask': {'type': 'str'},
                'next-server': {'type': 'str'},
                'ntp-server1': {'type': 'str'},
                'ntp-server2': {'type': 'str'},
                'ntp-server3': {'type': 'str'},
                'ntp-service': {'choices': ['default', 'specify', 'local'], 'type': 'str'},
                'options': {
                    'type': 'list',
                    'options': {
                        'code': {'type': 'int'},
                        'id': {'type': 'int'},
                        'ip': {'type': 'raw'},
                        'type': {'choices': ['hex', 'string', 'ip', 'fqdn'], 'type': 'str'},
                        'value': {'type': 'str'},
                        'vci-match': {'v_range': [['7.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'vci-string': {'v_range': [['7.2.1', '']], 'type': 'raw'},
                        'uci-match': {'v_range': [['7.2.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'uci-string': {'v_range': [['7.2.2', '']], 'type': 'raw'}
                    },
                    'elements': 'dict'
                },
                'reserved-address': {
                    'type': 'list',
                    'options': {
                        'action': {'choices': ['assign', 'block', 'reserved'], 'type': 'str'},
                        'description': {'type': 'str'},
                        'id': {'type': 'int'},
                        'ip': {'type': 'str'},
                        'mac': {'type': 'str'},
                        'circuit-id': {'v_range': [['6.2.0', '']], 'type': 'str'},
                        'circuit-id-type': {'v_range': [['6.2.0', '']], 'choices': ['hex', 'string'], 'type': 'str'},
                        'remote-id': {'v_range': [['6.2.0', '']], 'type': 'str'},
                        'remote-id-type': {'v_range': [['6.2.0', '']], 'choices': ['hex', 'string'], 'type': 'str'},
                        'type': {'v_range': [['6.2.0', '']], 'choices': ['mac', 'option82'], 'type': 'str'}
                    },
                    'elements': 'dict'
                },
                'server-type': {'choices': ['regular', 'ipsec'], 'type': 'str'},
                'status': {'choices': ['disable', 'enable'], 'type': 'str'},
                'tftp-server': {'type': 'raw'},
                'timezone': {
                    'choices': [
                        '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                        '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41',
                        '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62',
                        '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83',
                        '84', '85', '86', '87'
                    ],
                    'type': 'str'
                },
                'timezone-option': {'choices': ['disable', 'default', 'specify'], 'type': 'str'},
                'vci-match': {'choices': ['disable', 'enable'], 'type': 'str'},
                'vci-string': {'type': 'raw'},
                'wifi-ac1': {'type': 'str'},
                'wifi-ac2': {'type': 'str'},
                'wifi-ac3': {'type': 'str'},
                'wins-server1': {'type': 'str'},
                'wins-server2': {'type': 'str'},
                'dns-server4': {'v_range': [['6.2.2', '']], 'type': 'str'},
                'wifi-ac-service': {'v_range': [['6.2.2', '']], 'choices': ['specify', 'local'], 'type': 'str'},
                'auto-managed-status': {'v_range': [['6.4.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'dhcp-settings-from-fortiipam': {'v_range': [['6.4.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'relay-agent': {'v_range': [['7.4.0', '']], 'type': 'str'},
                'shared-subnet': {'v_range': [['7.4.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('full crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'system_dhcp_server'),
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
