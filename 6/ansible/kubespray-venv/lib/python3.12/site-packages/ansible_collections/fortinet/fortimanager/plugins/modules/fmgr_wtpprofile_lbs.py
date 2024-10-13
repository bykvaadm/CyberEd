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
module: fmgr_wtpprofile_lbs
short_description: Set various location based service
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
    wtp-profile:
        description: Deprecated, please use "wtp_profile"
        type: str
    wtp_profile:
        description: The parameter (wtp-profile) in requested url.
        type: str
    wtpprofile_lbs:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            aeroscout:
                type: str
                description: Enable/disable AeroScout Real Time Location Service
                choices:
                    - 'disable'
                    - 'enable'
            aeroscout-ap-mac:
                type: str
                description: Deprecated, please rename it to aeroscout_ap_mac. Use BSSID or board MAC address as AP MAC address in the Aeroscout AP mes...
                choices:
                    - 'bssid'
                    - 'board-mac'
            aeroscout-mmu-report:
                type: str
                description: Deprecated, please rename it to aeroscout_mmu_report. Enable/disable MU compounded report.
                choices:
                    - 'disable'
                    - 'enable'
            aeroscout-mu:
                type: str
                description: Deprecated, please rename it to aeroscout_mu. Enable/disable AeroScout support.
                choices:
                    - 'disable'
                    - 'enable'
            aeroscout-mu-factor:
                type: int
                description: Deprecated, please rename it to aeroscout_mu_factor. AeroScout Mobile Unit
            aeroscout-mu-timeout:
                type: int
                description: Deprecated, please rename it to aeroscout_mu_timeout. AeroScout MU mode timeout
            aeroscout-server-ip:
                type: str
                description: Deprecated, please rename it to aeroscout_server_ip. IP address of AeroScout server.
            aeroscout-server-port:
                type: int
                description: Deprecated, please rename it to aeroscout_server_port. AeroScout server UDP listening port.
            ekahau-blink-mode:
                type: str
                description: Deprecated, please rename it to ekahau_blink_mode. Enable/disable Ekahua blink mode
                choices:
                    - 'disable'
                    - 'enable'
            ekahau-tag:
                type: str
                description: Deprecated, please rename it to ekahau_tag. WiFi frame MAC address or WiFi Tag.
            erc-server-ip:
                type: str
                description: Deprecated, please rename it to erc_server_ip. IP address of Ekahua RTLS Controller
            erc-server-port:
                type: int
                description: Deprecated, please rename it to erc_server_port. Ekahua RTLS Controller
            fortipresence:
                type: str
                description: Enable/disable FortiPresence to monitor the location and activity of WiFi clients even if they dont connect to this WiFi n...
                choices:
                    - 'disable'
                    - 'enable'
                    - 'enable2'
                    - 'foreign'
                    - 'both'
            fortipresence-frequency:
                type: int
                description: Deprecated, please rename it to fortipresence_frequency. FortiPresence report transmit frequency
            fortipresence-port:
                type: int
                description: Deprecated, please rename it to fortipresence_port. FortiPresence server UDP listening port
            fortipresence-project:
                type: str
                description: Deprecated, please rename it to fortipresence_project. FortiPresence project name
            fortipresence-rogue:
                type: str
                description: Deprecated, please rename it to fortipresence_rogue. Enable/disable FortiPresence finding and reporting rogue APs.
                choices:
                    - 'disable'
                    - 'enable'
            fortipresence-secret:
                type: raw
                description: (list) Deprecated, please rename it to fortipresence_secret. FortiPresence secret password
            fortipresence-server:
                type: str
                description: Deprecated, please rename it to fortipresence_server. FortiPresence server IP address.
            fortipresence-unassoc:
                type: str
                description: Deprecated, please rename it to fortipresence_unassoc. Enable/disable FortiPresence finding and reporting unassociated sta...
                choices:
                    - 'disable'
                    - 'enable'
            station-locate:
                type: str
                description: Deprecated, please rename it to station_locate. Enable/disable client station locating services for all clients, whether a...
                choices:
                    - 'disable'
                    - 'enable'
            fortipresence-ble:
                type: str
                description: Deprecated, please rename it to fortipresence_ble. Enable/disable FortiPresence finding and reporting BLE devices.
                choices:
                    - 'disable'
                    - 'enable'
            fortipresence-server-addr-type:
                type: str
                description: Deprecated, please rename it to fortipresence_server_addr_type. FortiPresence server address type
                choices:
                    - 'fqdn'
                    - 'ipv4'
            fortipresence-server-fqdn:
                type: str
                description: Deprecated, please rename it to fortipresence_server_fqdn. FQDN of FortiPresence server.
            polestar:
                type: str
                description: Enable/disable PoleStar BLE NAO Track Real Time Location Service
                choices:
                    - 'disable'
                    - 'enable'
            polestar-accumulation-interval:
                type: int
                description: Deprecated, please rename it to polestar_accumulation_interval. Time that measurements should be accumulated in seconds
            polestar-asset-addrgrp-list:
                type: str
                description: Deprecated, please rename it to polestar_asset_addrgrp_list. Tags and asset addrgrp list to be reported.
            polestar-asset-uuid-list1:
                type: str
                description: Deprecated, please rename it to polestar_asset_uuid_list1. Tags and asset UUID list 1 to be reported
            polestar-asset-uuid-list2:
                type: str
                description: Deprecated, please rename it to polestar_asset_uuid_list2. Tags and asset UUID list 2 to be reported
            polestar-asset-uuid-list3:
                type: str
                description: Deprecated, please rename it to polestar_asset_uuid_list3. Tags and asset UUID list 3 to be reported
            polestar-asset-uuid-list4:
                type: str
                description: Deprecated, please rename it to polestar_asset_uuid_list4. Tags and asset UUID list 4 to be reported
            polestar-protocol:
                type: str
                description: Deprecated, please rename it to polestar_protocol. Select the protocol to report Measurements, Advertising Data, or Locati...
                choices:
                    - 'WSS'
            polestar-reporting-interval:
                type: int
                description: Deprecated, please rename it to polestar_reporting_interval. Time between reporting accumulated measurements in seconds
            polestar-server-fqdn:
                type: str
                description: Deprecated, please rename it to polestar_server_fqdn. FQDN of PoleStar Nao Track Server
            polestar-server-path:
                type: str
                description: Deprecated, please rename it to polestar_server_path. Path of PoleStar Nao Track Server
            polestar-server-port:
                type: int
                description: Deprecated, please rename it to polestar_server_port. Port of PoleStar Nao Track Server
            polestar-server-token:
                type: str
                description: Deprecated, please rename it to polestar_server_token. Access Token of PoleStar Nao Track Server.
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
    - name: Set various location based service
      fortinet.fortimanager.fmgr_wtpprofile_lbs:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        adom: <your own value>
        wtp_profile: <your own value>
        wtpprofile_lbs:
          aeroscout: <value in [disable, enable]>
          aeroscout_ap_mac: <value in [bssid, board-mac]>
          aeroscout_mmu_report: <value in [disable, enable]>
          aeroscout_mu: <value in [disable, enable]>
          aeroscout_mu_factor: <integer>
          aeroscout_mu_timeout: <integer>
          aeroscout_server_ip: <string>
          aeroscout_server_port: <integer>
          ekahau_blink_mode: <value in [disable, enable]>
          ekahau_tag: <string>
          erc_server_ip: <string>
          erc_server_port: <integer>
          fortipresence: <value in [disable, enable, enable2, ...]>
          fortipresence_frequency: <integer>
          fortipresence_port: <integer>
          fortipresence_project: <string>
          fortipresence_rogue: <value in [disable, enable]>
          fortipresence_secret: <list or string>
          fortipresence_server: <string>
          fortipresence_unassoc: <value in [disable, enable]>
          station_locate: <value in [disable, enable]>
          fortipresence_ble: <value in [disable, enable]>
          fortipresence_server_addr_type: <value in [fqdn, ipv4]>
          fortipresence_server_fqdn: <string>
          polestar: <value in [disable, enable]>
          polestar_accumulation_interval: <integer>
          polestar_asset_addrgrp_list: <string>
          polestar_asset_uuid_list1: <string>
          polestar_asset_uuid_list2: <string>
          polestar_asset_uuid_list3: <string>
          polestar_asset_uuid_list4: <string>
          polestar_protocol: <value in [WSS]>
          polestar_reporting_interval: <integer>
          polestar_server_fqdn: <string>
          polestar_server_path: <string>
          polestar_server_port: <integer>
          polestar_server_token: <string>
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
        '/pm/config/adom/{adom}/obj/wireless-controller/wtp-profile/{wtp-profile}/lbs',
        '/pm/config/global/obj/wireless-controller/wtp-profile/{wtp-profile}/lbs'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/wireless-controller/wtp-profile/{wtp-profile}/lbs/{lbs}',
        '/pm/config/global/obj/wireless-controller/wtp-profile/{wtp-profile}/lbs/{lbs}'
    ]

    url_params = ['adom', 'wtp-profile']
    module_primary_key = None
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'wtp-profile': {'type': 'str', 'api_name': 'wtp_profile'},
        'wtp_profile': {'type': 'str'},
        'wtpprofile_lbs': {
            'type': 'dict',
            'v_range': [['6.0.0', '']],
            'options': {
                'aeroscout': {'choices': ['disable', 'enable'], 'type': 'str'},
                'aeroscout-ap-mac': {'choices': ['bssid', 'board-mac'], 'type': 'str'},
                'aeroscout-mmu-report': {'choices': ['disable', 'enable'], 'type': 'str'},
                'aeroscout-mu': {'choices': ['disable', 'enable'], 'type': 'str'},
                'aeroscout-mu-factor': {'type': 'int'},
                'aeroscout-mu-timeout': {'type': 'int'},
                'aeroscout-server-ip': {'type': 'str'},
                'aeroscout-server-port': {'type': 'int'},
                'ekahau-blink-mode': {'choices': ['disable', 'enable'], 'type': 'str'},
                'ekahau-tag': {'type': 'str'},
                'erc-server-ip': {'type': 'str'},
                'erc-server-port': {'type': 'int'},
                'fortipresence': {'choices': ['disable', 'enable', 'enable2', 'foreign', 'both'], 'type': 'str'},
                'fortipresence-frequency': {'type': 'int'},
                'fortipresence-port': {'type': 'int'},
                'fortipresence-project': {'type': 'str'},
                'fortipresence-rogue': {'choices': ['disable', 'enable'], 'type': 'str'},
                'fortipresence-secret': {'no_log': True, 'type': 'raw'},
                'fortipresence-server': {'type': 'str'},
                'fortipresence-unassoc': {'choices': ['disable', 'enable'], 'type': 'str'},
                'station-locate': {'choices': ['disable', 'enable'], 'type': 'str'},
                'fortipresence-ble': {'v_range': [['6.2.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'fortipresence-server-addr-type': {'v_range': [['7.0.2', '']], 'choices': ['fqdn', 'ipv4'], 'type': 'str'},
                'fortipresence-server-fqdn': {'v_range': [['7.0.2', '']], 'type': 'str'},
                'polestar': {'v_range': [['7.4.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'polestar-accumulation-interval': {'v_range': [['7.4.1', '']], 'type': 'int'},
                'polestar-asset-addrgrp-list': {'v_range': [['7.4.1', '']], 'type': 'str'},
                'polestar-asset-uuid-list1': {'v_range': [['7.4.1', '']], 'type': 'str'},
                'polestar-asset-uuid-list2': {'v_range': [['7.4.1', '']], 'type': 'str'},
                'polestar-asset-uuid-list3': {'v_range': [['7.4.1', '']], 'type': 'str'},
                'polestar-asset-uuid-list4': {'v_range': [['7.4.1', '']], 'type': 'str'},
                'polestar-protocol': {'v_range': [['7.4.1', '']], 'choices': ['WSS'], 'type': 'str'},
                'polestar-reporting-interval': {'v_range': [['7.4.1', '']], 'type': 'int'},
                'polestar-server-fqdn': {'v_range': [['7.4.1', '']], 'type': 'str'},
                'polestar-server-path': {'v_range': [['7.4.1', '']], 'type': 'str'},
                'polestar-server-port': {'v_range': [['7.4.1', '']], 'type': 'int'},
                'polestar-server-token': {'v_range': [['7.4.1', '']], 'no_log': True, 'type': 'str'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('partial crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'wtpprofile_lbs'),
                           supports_check_mode=True)

    if not module._socket_path:
        module.fail_json(msg='MUST RUN IN HTTPAPI MODE')
    connection = Connection(module._socket_path)
    fmgr = NAPIManager(jrpc_urls, perobject_jrpc_urls, module_primary_key, url_params, module, connection, top_level_schema_name='data')
    fmgr.validate_parameters(params_validation_blob)
    fmgr.process_partial_curd(argument_specs=module_arg_spec)

    module.exit_json(meta=module.params)


if __name__ == '__main__':
    main()
