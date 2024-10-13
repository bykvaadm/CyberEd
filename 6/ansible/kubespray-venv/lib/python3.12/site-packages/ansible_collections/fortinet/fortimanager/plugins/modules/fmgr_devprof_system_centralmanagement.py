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
module: fmgr_devprof_system_centralmanagement
short_description: Configure central management.
description:
    - This module is able to configure a FortiManager device.
    - Examples include all parameters and values which need to be adjusted to data sources before usage.

version_added: "1.0.0"
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
    devprof:
        description: The parameter (devprof) in requested url.
        type: str
        required: true
    devprof_system_centralmanagement:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            include-default-servers:
                type: str
                description: Deprecated, please rename it to include_default_servers. Enable/disable inclusion of public FortiGuard servers in the over...
                choices:
                    - 'disable'
                    - 'enable'
            server-list:
                type: list
                elements: dict
                description: Deprecated, please rename it to server_list. Server list.
                suboptions:
                    addr-type:
                        type: str
                        description: Deprecated, please rename it to addr_type. Indicate whether the FortiGate communicates with the override server us...
                        choices:
                            - 'fqdn'
                            - 'ipv4'
                            - 'ipv6'
                    fqdn:
                        type: str
                        description: FQDN address of override server.
                    id:
                        type: int
                        description: ID.
                    server-address:
                        type: str
                        description: Deprecated, please rename it to server_address. IPv4 address of override server.
                    server-address6:
                        type: str
                        description: Deprecated, please rename it to server_address6. IPv6 address of override server.
                    server-type:
                        type: list
                        elements: str
                        description: Deprecated, please rename it to server_type. FortiGuard service type.
                        choices:
                            - 'update'
                            - 'rating'
                            - 'iot-query'
                            - 'iot-collect'
                            - 'vpatch-query'
            ltefw-upgrade-time:
                type: str
                description: Deprecated, please rename it to ltefw_upgrade_time. Schedule next LTE firmware upgrade time
            vdom:
                type: raw
                description: (list) Virtual domain
            allow-remote-firmware-upgrade:
                type: str
                description: Deprecated, please rename it to allow_remote_firmware_upgrade. Enable/disable remotely upgrading the firmware on this Fort...
                choices:
                    - 'disable'
                    - 'enable'
            local-cert:
                type: str
                description: Deprecated, please rename it to local_cert. Certificate to be used by FGFM protocol.
            allow-push-firmware:
                type: str
                description: Deprecated, please rename it to allow_push_firmware. Enable/disable allowing the central management server to push firmwar...
                choices:
                    - 'disable'
                    - 'enable'
            ltefw-upgrade-frequency:
                type: str
                description: Deprecated, please rename it to ltefw_upgrade_frequency. Set LTE firmware auto pushdown frequency.
                choices:
                    - 'everyHour'
                    - 'every12hour'
                    - 'everyDay'
                    - 'everyWeek'
            mode:
                type: str
                description: Central management mode.
                choices:
                    - 'normal'
                    - 'backup'
            serial-number:
                type: raw
                description: (list) Deprecated, please rename it to serial_number. Serial number.
            fmg-source-ip6:
                type: str
                description: Deprecated, please rename it to fmg_source_ip6. IPv6 source address that this FortiGate uses when communicating with Forti...
            allow-monitor:
                type: str
                description: Deprecated, please rename it to allow_monitor. Enable/disable allowing the central management server to remotely monitor t...
                choices:
                    - 'disable'
                    - 'enable'
            allow-push-configuration:
                type: str
                description: Deprecated, please rename it to allow_push_configuration. Enable/disable allowing the central management server to push co...
                choices:
                    - 'disable'
                    - 'enable'
            ca-cert:
                type: str
                description: Deprecated, please rename it to ca_cert. CA certificate to be used by FGFM protocol.
            fmg-update-port:
                type: str
                description: Deprecated, please rename it to fmg_update_port. Port used to communicate with FortiManager that is acting as a FortiGuard...
                choices:
                    - '443'
                    - '8890'
            use-elbc-vdom:
                type: str
                description: Deprecated, please rename it to use_elbc_vdom. Enable/disable use of special ELBC config sync VDOM to connect to FortiManager.
                choices:
                    - 'disable'
                    - 'enable'
            allow-remote-lte-firmware-upgrade:
                type: str
                description: Deprecated, please rename it to allow_remote_lte_firmware_upgrade. Enable/disable remotely upgrading the lte firmware on t...
                choices:
                    - 'disable'
                    - 'enable'
            interface:
                type: raw
                description: (list) Specify outgoing interface to reach server.
            schedule-script-restore:
                type: str
                description: Deprecated, please rename it to schedule_script_restore. Enable/disable allowing the central management server to restore ...
                choices:
                    - 'disable'
                    - 'enable'
            schedule-config-restore:
                type: str
                description: Deprecated, please rename it to schedule_config_restore. Enable/disable allowing the central management server to restore ...
                choices:
                    - 'disable'
                    - 'enable'
            interface-select-method:
                type: str
                description: Deprecated, please rename it to interface_select_method. Specify how to select outgoing interface to reach server.
                choices:
                    - 'auto'
                    - 'sdwan'
                    - 'specify'
            type:
                type: str
                description: Central management type.
                choices:
                    - 'fortimanager'
                    - 'fortiguard'
                    - 'none'
            fmg-source-ip:
                type: str
                description: Deprecated, please rename it to fmg_source_ip. IPv4 source address that this FortiGate uses when communicating with FortiM...
            fortigate-cloud-sso-default-profile:
                type: raw
                description: (list) Deprecated, please rename it to fortigate_cloud_sso_default_profile. Override access profile.
            fmg:
                type: raw
                description: (list) IP address or FQDN of the FortiManager.
            enc-algorithm:
                type: str
                description: Deprecated, please rename it to enc_algorithm. Encryption strength for communications between the FortiGate and central ma...
                choices:
                    - 'default'
                    - 'high'
                    - 'low'
            allow-remote-modem-firmware-upgrade:
                type: str
                description: Deprecated, please rename it to allow_remote_modem_firmware_upgrade. Enable/disable remotely upgrading the internal cellul...
                choices:
                    - 'disable'
                    - 'enable'
            modem-upgrade-frequency:
                type: str
                description: Deprecated, please rename it to modem_upgrade_frequency. Set internal cellular modem firmware auto pushdown frequency.
                choices:
                    - 'everyHour'
                    - 'every12hour'
                    - 'everyDay'
                    - 'everyWeek'
            modem-upgrade-time:
                type: str
                description: Deprecated, please rename it to modem_upgrade_time. Schedule next internal cellular modem firmware upgrade time
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
    - name: Configure central management.
      fortinet.fortimanager.fmgr_devprof_system_centralmanagement:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        adom: <your own value>
        devprof: <your own value>
        devprof_system_centralmanagement:
          include_default_servers: <value in [disable, enable]>
          server_list:
            -
              addr_type: <value in [fqdn, ipv4, ipv6]>
              fqdn: <string>
              id: <integer>
              server_address: <string>
              server_address6: <string>
              server_type:
                - update
                - rating
                - iot-query
                - iot-collect
                - vpatch-query
          ltefw_upgrade_time: <string>
          vdom: <list or string>
          allow_remote_firmware_upgrade: <value in [disable, enable]>
          local_cert: <string>
          allow_push_firmware: <value in [disable, enable]>
          ltefw_upgrade_frequency: <value in [everyHour, every12hour, everyDay, ...]>
          mode: <value in [normal, backup]>
          serial_number: <list or string>
          fmg_source_ip6: <string>
          allow_monitor: <value in [disable, enable]>
          allow_push_configuration: <value in [disable, enable]>
          ca_cert: <string>
          fmg_update_port: <value in [443, 8890]>
          use_elbc_vdom: <value in [disable, enable]>
          allow_remote_lte_firmware_upgrade: <value in [disable, enable]>
          interface: <list or string>
          schedule_script_restore: <value in [disable, enable]>
          schedule_config_restore: <value in [disable, enable]>
          interface_select_method: <value in [auto, sdwan, specify]>
          type: <value in [fortimanager, fortiguard, none]>
          fmg_source_ip: <string>
          fortigate_cloud_sso_default_profile: <list or string>
          fmg: <list or string>
          enc_algorithm: <value in [default, high, low]>
          allow_remote_modem_firmware_upgrade: <value in [disable, enable]>
          modem_upgrade_frequency: <value in [everyHour, every12hour, everyDay, ...]>
          modem_upgrade_time: <string>
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
        '/pm/config/adom/{adom}/devprof/{devprof}/system/central-management'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/devprof/{devprof}/system/central-management/{central-management}'
    ]

    url_params = ['adom', 'devprof']
    module_primary_key = None
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'devprof': {'required': True, 'type': 'str'},
        'devprof_system_centralmanagement': {
            'type': 'dict',
            'v_range': [['6.0.0', '6.2.5'], ['6.2.7', '6.4.1'], ['6.4.3', '']],
            'options': {
                'include-default-servers': {
                    'v_range': [['6.0.0', '6.2.5'], ['6.2.7', '6.4.1'], ['6.4.3', '']],
                    'choices': ['disable', 'enable'],
                    'type': 'str'
                },
                'server-list': {
                    'v_range': [['6.0.0', '6.2.5'], ['6.2.7', '6.4.1'], ['6.4.3', '']],
                    'type': 'list',
                    'options': {
                        'addr-type': {
                            'v_range': [['6.0.0', '6.2.5'], ['6.2.7', '6.4.1'], ['6.4.3', '']],
                            'choices': ['fqdn', 'ipv4', 'ipv6'],
                            'type': 'str'
                        },
                        'fqdn': {'v_range': [['6.0.0', '6.2.5'], ['6.2.7', '6.4.1'], ['6.4.3', '']], 'type': 'str'},
                        'id': {'v_range': [['6.0.0', '6.2.5'], ['6.2.7', '6.4.1'], ['6.4.3', '']], 'type': 'int'},
                        'server-address': {'v_range': [['6.0.0', '6.2.5'], ['6.2.7', '6.4.1'], ['6.4.3', '']], 'type': 'str'},
                        'server-address6': {'v_range': [['6.0.0', '6.2.5'], ['6.2.7', '6.4.1'], ['6.4.3', '']], 'type': 'str'},
                        'server-type': {
                            'v_range': [['6.0.0', '6.2.5'], ['6.2.7', '6.4.1'], ['6.4.3', '']],
                            'type': 'list',
                            'choices': ['update', 'rating', 'iot-query', 'iot-collect', 'vpatch-query'],
                            'elements': 'str'
                        }
                    },
                    'elements': 'dict'
                },
                'ltefw-upgrade-time': {'v_range': [['7.4.3', '']], 'type': 'str'},
                'vdom': {'v_range': [['7.4.3', '']], 'type': 'raw'},
                'allow-remote-firmware-upgrade': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'local-cert': {'v_range': [['7.4.3', '']], 'type': 'str'},
                'allow-push-firmware': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ltefw-upgrade-frequency': {'v_range': [['7.4.3', '']], 'choices': ['everyHour', 'every12hour', 'everyDay', 'everyWeek'], 'type': 'str'},
                'mode': {'v_range': [['7.4.3', '']], 'choices': ['normal', 'backup'], 'type': 'str'},
                'serial-number': {'v_range': [['7.4.3', '']], 'type': 'raw'},
                'fmg-source-ip6': {'v_range': [['7.4.3', '']], 'type': 'str'},
                'allow-monitor': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'allow-push-configuration': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ca-cert': {'v_range': [['7.4.3', '']], 'type': 'str'},
                'fmg-update-port': {'v_range': [['7.4.3', '']], 'choices': ['443', '8890'], 'type': 'str'},
                'use-elbc-vdom': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'allow-remote-lte-firmware-upgrade': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'interface': {'v_range': [['7.4.3', '']], 'type': 'raw'},
                'schedule-script-restore': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'schedule-config-restore': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'interface-select-method': {'v_range': [['7.4.3', '']], 'choices': ['auto', 'sdwan', 'specify'], 'type': 'str'},
                'type': {'v_range': [['7.4.3', '']], 'choices': ['fortimanager', 'fortiguard', 'none'], 'type': 'str'},
                'fmg-source-ip': {'v_range': [['7.4.3', '']], 'type': 'str'},
                'fortigate-cloud-sso-default-profile': {'v_range': [['7.4.3', '']], 'type': 'raw'},
                'fmg': {'v_range': [['7.4.3', '']], 'type': 'raw'},
                'enc-algorithm': {'v_range': [['7.4.3', '']], 'choices': ['default', 'high', 'low'], 'type': 'str'},
                'allow-remote-modem-firmware-upgrade': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'modem-upgrade-frequency': {'v_range': [['7.4.3', '']], 'choices': ['everyHour', 'every12hour', 'everyDay', 'everyWeek'], 'type': 'str'},
                'modem-upgrade-time': {'v_range': [['7.4.3', '']], 'type': 'str'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('partial crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'devprof_system_centralmanagement'),
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
