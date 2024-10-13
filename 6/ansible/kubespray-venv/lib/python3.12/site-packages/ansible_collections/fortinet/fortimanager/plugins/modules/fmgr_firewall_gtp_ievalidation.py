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
module: fmgr_firewall_gtp_ievalidation
short_description: IE validation.
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
    gtp:
        description: The parameter (gtp) in requested url.
        type: str
        required: true
    firewall_gtp_ievalidation:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            apn-restriction:
                type: str
                description: Deprecated, please rename it to apn_restriction. Validate APN restriction.
                choices:
                    - 'disable'
                    - 'enable'
            charging-ID:
                type: str
                description: Deprecated, please rename it to charging_ID. Validate charging ID.
                choices:
                    - 'disable'
                    - 'enable'
            charging-gateway-addr:
                type: str
                description: Deprecated, please rename it to charging_gateway_addr. Validate charging gateway address.
                choices:
                    - 'disable'
                    - 'enable'
            end-user-addr:
                type: str
                description: Deprecated, please rename it to end_user_addr. Validate end user address.
                choices:
                    - 'disable'
                    - 'enable'
            gsn-addr:
                type: str
                description: Deprecated, please rename it to gsn_addr. Validate GSN address.
                choices:
                    - 'disable'
                    - 'enable'
            imei:
                type: str
                description: Validate IMEI
                choices:
                    - 'disable'
                    - 'enable'
            imsi:
                type: str
                description: Validate IMSI.
                choices:
                    - 'disable'
                    - 'enable'
            mm-context:
                type: str
                description: Deprecated, please rename it to mm_context. Validate MM context.
                choices:
                    - 'disable'
                    - 'enable'
            ms-tzone:
                type: str
                description: Deprecated, please rename it to ms_tzone. Validate MS time zone.
                choices:
                    - 'disable'
                    - 'enable'
            ms-validated:
                type: str
                description: Deprecated, please rename it to ms_validated. Validate MS validated.
                choices:
                    - 'disable'
                    - 'enable'
            msisdn:
                type: str
                description: Validate MSISDN.
                choices:
                    - 'disable'
                    - 'enable'
            nsapi:
                type: str
                description: Validate NSAPI.
                choices:
                    - 'disable'
                    - 'enable'
            pdp-context:
                type: str
                description: Deprecated, please rename it to pdp_context. Validate PDP context.
                choices:
                    - 'disable'
                    - 'enable'
            qos-profile:
                type: str
                description: Deprecated, please rename it to qos_profile. Validate Quality of Service
                choices:
                    - 'disable'
                    - 'enable'
            rai:
                type: str
                description: Validate RAI.
                choices:
                    - 'disable'
                    - 'enable'
            rat-type:
                type: str
                description: Deprecated, please rename it to rat_type. Validate RAT type.
                choices:
                    - 'disable'
                    - 'enable'
            reordering-required:
                type: str
                description: Deprecated, please rename it to reordering_required. Validate re-ordering required.
                choices:
                    - 'disable'
                    - 'enable'
            selection-mode:
                type: str
                description: Deprecated, please rename it to selection_mode. Validate selection mode.
                choices:
                    - 'disable'
                    - 'enable'
            uli:
                type: str
                description: Validate user location information.
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
    - name: IE validation.
      fortinet.fortimanager.fmgr_firewall_gtp_ievalidation:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        adom: <your own value>
        gtp: <your own value>
        firewall_gtp_ievalidation:
          apn_restriction: <value in [disable, enable]>
          charging_ID: <value in [disable, enable]>
          charging_gateway_addr: <value in [disable, enable]>
          end_user_addr: <value in [disable, enable]>
          gsn_addr: <value in [disable, enable]>
          imei: <value in [disable, enable]>
          imsi: <value in [disable, enable]>
          mm_context: <value in [disable, enable]>
          ms_tzone: <value in [disable, enable]>
          ms_validated: <value in [disable, enable]>
          msisdn: <value in [disable, enable]>
          nsapi: <value in [disable, enable]>
          pdp_context: <value in [disable, enable]>
          qos_profile: <value in [disable, enable]>
          rai: <value in [disable, enable]>
          rat_type: <value in [disable, enable]>
          reordering_required: <value in [disable, enable]>
          selection_mode: <value in [disable, enable]>
          uli: <value in [disable, enable]>
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
        '/pm/config/adom/{adom}/obj/firewall/gtp/{gtp}/ie-validation',
        '/pm/config/global/obj/firewall/gtp/{gtp}/ie-validation'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/firewall/gtp/{gtp}/ie-validation/{ie-validation}',
        '/pm/config/global/obj/firewall/gtp/{gtp}/ie-validation/{ie-validation}'
    ]

    url_params = ['adom', 'gtp']
    module_primary_key = None
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'gtp': {'required': True, 'type': 'str'},
        'firewall_gtp_ievalidation': {
            'type': 'dict',
            'v_range': [['6.0.0', '']],
            'options': {
                'apn-restriction': {'choices': ['disable', 'enable'], 'type': 'str'},
                'charging-ID': {'choices': ['disable', 'enable'], 'type': 'str'},
                'charging-gateway-addr': {'choices': ['disable', 'enable'], 'type': 'str'},
                'end-user-addr': {'choices': ['disable', 'enable'], 'type': 'str'},
                'gsn-addr': {'choices': ['disable', 'enable'], 'type': 'str'},
                'imei': {'choices': ['disable', 'enable'], 'type': 'str'},
                'imsi': {'choices': ['disable', 'enable'], 'type': 'str'},
                'mm-context': {'choices': ['disable', 'enable'], 'type': 'str'},
                'ms-tzone': {'choices': ['disable', 'enable'], 'type': 'str'},
                'ms-validated': {'choices': ['disable', 'enable'], 'type': 'str'},
                'msisdn': {'choices': ['disable', 'enable'], 'type': 'str'},
                'nsapi': {'choices': ['disable', 'enable'], 'type': 'str'},
                'pdp-context': {'choices': ['disable', 'enable'], 'type': 'str'},
                'qos-profile': {'choices': ['disable', 'enable'], 'type': 'str'},
                'rai': {'choices': ['disable', 'enable'], 'type': 'str'},
                'rat-type': {'choices': ['disable', 'enable'], 'type': 'str'},
                'reordering-required': {'choices': ['disable', 'enable'], 'type': 'str'},
                'selection-mode': {'choices': ['disable', 'enable'], 'type': 'str'},
                'uli': {'choices': ['disable', 'enable'], 'type': 'str'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('partial crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'firewall_gtp_ievalidation'),
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
