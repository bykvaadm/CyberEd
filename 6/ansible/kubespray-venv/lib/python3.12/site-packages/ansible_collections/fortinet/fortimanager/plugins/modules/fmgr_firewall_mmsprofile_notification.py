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
module: fmgr_firewall_mmsprofile_notification
short_description: Notification configuration.
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
    mms-profile:
        description: Deprecated, please use "mms_profile"
        type: str
    mms_profile:
        description: The parameter (mms-profile) in requested url.
        type: str
    firewall_mmsprofile_notification:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            alert-int:
                type: int
                description: Deprecated, please rename it to alert_int. Alert notification send interval.
            alert-int-mode:
                type: str
                description: Deprecated, please rename it to alert_int_mode. Alert notification interval mode.
                choices:
                    - 'hours'
                    - 'minutes'
            alert-src-msisdn:
                type: str
                description: Deprecated, please rename it to alert_src_msisdn. Specify from address for alert messages.
            alert-status:
                type: str
                description: Deprecated, please rename it to alert_status. Alert notification status.
                choices:
                    - 'disable'
                    - 'enable'
            bword-int:
                type: int
                description: Deprecated, please rename it to bword_int. Banned word notification send interval.
            bword-int-mode:
                type: str
                description: Deprecated, please rename it to bword_int_mode. Banned word notification interval mode.
                choices:
                    - 'hours'
                    - 'minutes'
            bword-status:
                type: str
                description: Deprecated, please rename it to bword_status. Banned word notification status.
                choices:
                    - 'disable'
                    - 'enable'
            carrier-endpoint-bwl-int:
                type: int
                description: Deprecated, please rename it to carrier_endpoint_bwl_int. Carrier end point black/white list notification send interval.
            carrier-endpoint-bwl-int-mode:
                type: str
                description: Deprecated, please rename it to carrier_endpoint_bwl_int_mode. Carrier end point black/white list notification interval mode.
                choices:
                    - 'hours'
                    - 'minutes'
            carrier-endpoint-bwl-status:
                type: str
                description: Deprecated, please rename it to carrier_endpoint_bwl_status. Carrier end point black/white list notification status.
                choices:
                    - 'disable'
                    - 'enable'
            days-allowed:
                type: list
                elements: str
                description: Deprecated, please rename it to days_allowed. Weekdays on which notification messages may be sent.
                choices:
                    - 'sunday'
                    - 'monday'
                    - 'tuesday'
                    - 'wednesday'
                    - 'thursday'
                    - 'friday'
                    - 'saturday'
            detect-server:
                type: str
                description: Deprecated, please rename it to detect_server. Enable/disable automatic server address determination.
                choices:
                    - 'disable'
                    - 'enable'
            dupe-int:
                type: int
                description: Deprecated, please rename it to dupe_int. Duplicate notification send interval.
            dupe-int-mode:
                type: str
                description: Deprecated, please rename it to dupe_int_mode. Duplicate notification interval mode.
                choices:
                    - 'hours'
                    - 'minutes'
            dupe-status:
                type: str
                description: Deprecated, please rename it to dupe_status. Duplicate notification status.
                choices:
                    - 'disable'
                    - 'enable'
            file-block-int:
                type: int
                description: Deprecated, please rename it to file_block_int. File block notification send interval.
            file-block-int-mode:
                type: str
                description: Deprecated, please rename it to file_block_int_mode. File block notification interval mode.
                choices:
                    - 'hours'
                    - 'minutes'
            file-block-status:
                type: str
                description: Deprecated, please rename it to file_block_status. File block notification status.
                choices:
                    - 'disable'
                    - 'enable'
            flood-int:
                type: int
                description: Deprecated, please rename it to flood_int. Flood notification send interval.
            flood-int-mode:
                type: str
                description: Deprecated, please rename it to flood_int_mode. Flood notification interval mode.
                choices:
                    - 'hours'
                    - 'minutes'
            flood-status:
                type: str
                description: Deprecated, please rename it to flood_status. Flood notification status.
                choices:
                    - 'disable'
                    - 'enable'
            from-in-header:
                type: str
                description: Deprecated, please rename it to from_in_header. Enable/disable insertion of from address in HTTP header.
                choices:
                    - 'disable'
                    - 'enable'
            mms-checksum-int:
                type: int
                description: Deprecated, please rename it to mms_checksum_int. MMS checksum notification send interval.
            mms-checksum-int-mode:
                type: str
                description: Deprecated, please rename it to mms_checksum_int_mode. MMS checksum notification interval mode.
                choices:
                    - 'hours'
                    - 'minutes'
            mms-checksum-status:
                type: str
                description: Deprecated, please rename it to mms_checksum_status. MMS checksum notification status.
                choices:
                    - 'disable'
                    - 'enable'
            mmsc-hostname:
                type: str
                description: Deprecated, please rename it to mmsc_hostname. Host name or IP address of the MMSC.
            mmsc-password:
                type: raw
                description: (list) Deprecated, please rename it to mmsc_password. Password required for authentication with the MMSC.
            mmsc-port:
                type: int
                description: Deprecated, please rename it to mmsc_port. Port used on the MMSC for sending MMS messages
            mmsc-url:
                type: str
                description: Deprecated, please rename it to mmsc_url. URL used on the MMSC for sending MMS messages.
            mmsc-username:
                type: str
                description: Deprecated, please rename it to mmsc_username. User name required for authentication with the MMSC.
            msg-protocol:
                type: str
                description: Deprecated, please rename it to msg_protocol. Protocol to use for sending notification messages.
                choices:
                    - 'mm1'
                    - 'mm3'
                    - 'mm4'
                    - 'mm7'
            msg-type:
                type: str
                description: Deprecated, please rename it to msg_type. MM7 message type.
                choices:
                    - 'submit-req'
                    - 'deliver-req'
            protocol:
                type: str
                description: Protocol.
            rate-limit:
                type: int
                description: Deprecated, please rename it to rate_limit. Rate limit for sending notification messages
            tod-window-duration:
                type: str
                description: Deprecated, please rename it to tod_window_duration. Time of day window duration.
            tod-window-end:
                type: str
                description: Deprecated, please rename it to tod_window_end. Obsolete.
            tod-window-start:
                type: str
                description: Deprecated, please rename it to tod_window_start. Time of day window start.
            user-domain:
                type: str
                description: Deprecated, please rename it to user_domain. Domain name to which the user addresses belong.
            vas-id:
                type: str
                description: Deprecated, please rename it to vas_id. VAS identifier.
            vasp-id:
                type: str
                description: Deprecated, please rename it to vasp_id. VASP identifier.
            virus-int:
                type: int
                description: Deprecated, please rename it to virus_int. Virus notification send interval.
            virus-int-mode:
                type: str
                description: Deprecated, please rename it to virus_int_mode. Virus notification interval mode.
                choices:
                    - 'hours'
                    - 'minutes'
            virus-status:
                type: str
                description: Deprecated, please rename it to virus_status. Virus notification status.
                choices:
                    - 'disable'
                    - 'enable'
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
    - name: Notification configuration.
      fortinet.fortimanager.fmgr_firewall_mmsprofile_notification:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        adom: <your own value>
        mms_profile: <your own value>
        firewall_mmsprofile_notification:
          alert_int: <integer>
          alert_int_mode: <value in [hours, minutes]>
          alert_src_msisdn: <string>
          alert_status: <value in [disable, enable]>
          bword_int: <integer>
          bword_int_mode: <value in [hours, minutes]>
          bword_status: <value in [disable, enable]>
          carrier_endpoint_bwl_int: <integer>
          carrier_endpoint_bwl_int_mode: <value in [hours, minutes]>
          carrier_endpoint_bwl_status: <value in [disable, enable]>
          days_allowed:
            - sunday
            - monday
            - tuesday
            - wednesday
            - thursday
            - friday
            - saturday
          detect_server: <value in [disable, enable]>
          dupe_int: <integer>
          dupe_int_mode: <value in [hours, minutes]>
          dupe_status: <value in [disable, enable]>
          file_block_int: <integer>
          file_block_int_mode: <value in [hours, minutes]>
          file_block_status: <value in [disable, enable]>
          flood_int: <integer>
          flood_int_mode: <value in [hours, minutes]>
          flood_status: <value in [disable, enable]>
          from_in_header: <value in [disable, enable]>
          mms_checksum_int: <integer>
          mms_checksum_int_mode: <value in [hours, minutes]>
          mms_checksum_status: <value in [disable, enable]>
          mmsc_hostname: <string>
          mmsc_password: <list or string>
          mmsc_port: <integer>
          mmsc_url: <string>
          mmsc_username: <string>
          msg_protocol: <value in [mm1, mm3, mm4, ...]>
          msg_type: <value in [submit-req, deliver-req]>
          protocol: <string>
          rate_limit: <integer>
          tod_window_duration: <string>
          tod_window_end: <string>
          tod_window_start: <string>
          user_domain: <string>
          vas_id: <string>
          vasp_id: <string>
          virus_int: <integer>
          virus_int_mode: <value in [hours, minutes]>
          virus_status: <value in [disable, enable]>
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
        '/pm/config/adom/{adom}/obj/firewall/mms-profile/{mms-profile}/notification',
        '/pm/config/global/obj/firewall/mms-profile/{mms-profile}/notification'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/firewall/mms-profile/{mms-profile}/notification/{notification}',
        '/pm/config/global/obj/firewall/mms-profile/{mms-profile}/notification/{notification}'
    ]

    url_params = ['adom', 'mms-profile']
    module_primary_key = None
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'mms-profile': {'type': 'str', 'api_name': 'mms_profile'},
        'mms_profile': {'type': 'str'},
        'firewall_mmsprofile_notification': {
            'type': 'dict',
            'v_range': [['6.0.0', '']],
            'options': {
                'alert-int': {'type': 'int'},
                'alert-int-mode': {'choices': ['hours', 'minutes'], 'type': 'str'},
                'alert-src-msisdn': {'type': 'str'},
                'alert-status': {'choices': ['disable', 'enable'], 'type': 'str'},
                'bword-int': {'type': 'int'},
                'bword-int-mode': {'choices': ['hours', 'minutes'], 'type': 'str'},
                'bword-status': {'choices': ['disable', 'enable'], 'type': 'str'},
                'carrier-endpoint-bwl-int': {'type': 'int'},
                'carrier-endpoint-bwl-int-mode': {'choices': ['hours', 'minutes'], 'type': 'str'},
                'carrier-endpoint-bwl-status': {'choices': ['disable', 'enable'], 'type': 'str'},
                'days-allowed': {
                    'type': 'list',
                    'choices': ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'],
                    'elements': 'str'
                },
                'detect-server': {'choices': ['disable', 'enable'], 'type': 'str'},
                'dupe-int': {'type': 'int'},
                'dupe-int-mode': {'choices': ['hours', 'minutes'], 'type': 'str'},
                'dupe-status': {'choices': ['disable', 'enable'], 'type': 'str'},
                'file-block-int': {'type': 'int'},
                'file-block-int-mode': {'choices': ['hours', 'minutes'], 'type': 'str'},
                'file-block-status': {'choices': ['disable', 'enable'], 'type': 'str'},
                'flood-int': {'type': 'int'},
                'flood-int-mode': {'choices': ['hours', 'minutes'], 'type': 'str'},
                'flood-status': {'choices': ['disable', 'enable'], 'type': 'str'},
                'from-in-header': {'choices': ['disable', 'enable'], 'type': 'str'},
                'mms-checksum-int': {'type': 'int'},
                'mms-checksum-int-mode': {'choices': ['hours', 'minutes'], 'type': 'str'},
                'mms-checksum-status': {'choices': ['disable', 'enable'], 'type': 'str'},
                'mmsc-hostname': {'type': 'str'},
                'mmsc-password': {'no_log': True, 'type': 'raw'},
                'mmsc-port': {'type': 'int'},
                'mmsc-url': {'type': 'str'},
                'mmsc-username': {'type': 'str'},
                'msg-protocol': {'choices': ['mm1', 'mm3', 'mm4', 'mm7'], 'type': 'str'},
                'msg-type': {'choices': ['submit-req', 'deliver-req'], 'type': 'str'},
                'protocol': {'type': 'str'},
                'rate-limit': {'type': 'int'},
                'tod-window-duration': {'type': 'str'},
                'tod-window-end': {'v_range': [['6.0.0', '7.2.0']], 'type': 'str'},
                'tod-window-start': {'type': 'str'},
                'user-domain': {'type': 'str'},
                'vas-id': {'type': 'str'},
                'vasp-id': {'type': 'str'},
                'virus-int': {'type': 'int'},
                'virus-int-mode': {'choices': ['hours', 'minutes'], 'type': 'str'},
                'virus-status': {'choices': ['disable', 'enable'], 'type': 'str'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('partial crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'firewall_mmsprofile_notification'),
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
