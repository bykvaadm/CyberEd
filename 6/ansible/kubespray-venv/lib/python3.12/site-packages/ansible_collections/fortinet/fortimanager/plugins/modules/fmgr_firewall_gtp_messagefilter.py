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
module: fmgr_firewall_gtp_messagefilter
short_description: Message filter.
description:
    - This module is able to configure a FortiManager device.
    - Examples include all parameters and values which need to be adjusted to data sources before usage.

version_added: "2.2.0"
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
    firewall_gtp_messagefilter:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            create-aa-pdp:
                type: str
                description: Deprecated, please rename it to create_aa_pdp. Create AA PDP.
                choices:
                    - 'allow'
                    - 'deny'
            create-mbms:
                type: str
                description: Deprecated, please rename it to create_mbms. Create MBMS.
                choices:
                    - 'allow'
                    - 'deny'
            create-pdp:
                type: str
                description: Deprecated, please rename it to create_pdp. Create PDP.
                choices:
                    - 'allow'
                    - 'deny'
            data-record:
                type: str
                description: Deprecated, please rename it to data_record. Data record.
                choices:
                    - 'allow'
                    - 'deny'
            delete-aa-pdp:
                type: str
                description: Deprecated, please rename it to delete_aa_pdp. Delete AA PDP.
                choices:
                    - 'allow'
                    - 'deny'
            delete-mbms:
                type: str
                description: Deprecated, please rename it to delete_mbms. Delete MBMS.
                choices:
                    - 'allow'
                    - 'deny'
            delete-pdp:
                type: str
                description: Deprecated, please rename it to delete_pdp. Delete PDP.
                choices:
                    - 'allow'
                    - 'deny'
            echo:
                type: str
                description: Echo.
                choices:
                    - 'allow'
                    - 'deny'
            error-indication:
                type: str
                description: Deprecated, please rename it to error_indication. Error indication.
                choices:
                    - 'allow'
                    - 'deny'
            failure-report:
                type: str
                description: Deprecated, please rename it to failure_report. Failure report.
                choices:
                    - 'allow'
                    - 'deny'
            fwd-relocation:
                type: str
                description: Deprecated, please rename it to fwd_relocation. Forward relocation.
                choices:
                    - 'allow'
                    - 'deny'
            fwd-srns-context:
                type: str
                description: Deprecated, please rename it to fwd_srns_context. Forward SRNS context.
                choices:
                    - 'allow'
                    - 'deny'
            gtp-pdu:
                type: str
                description: Deprecated, please rename it to gtp_pdu. GTP PDU.
                choices:
                    - 'allow'
                    - 'deny'
            identification:
                type: str
                description: Identification.
                choices:
                    - 'allow'
                    - 'deny'
            mbms-notification:
                type: str
                description: Deprecated, please rename it to mbms_notification. MBMS notification.
                choices:
                    - 'allow'
                    - 'deny'
            node-alive:
                type: str
                description: Deprecated, please rename it to node_alive. Node alive.
                choices:
                    - 'allow'
                    - 'deny'
            note-ms-present:
                type: str
                description: Deprecated, please rename it to note_ms_present. Note MS present.
                choices:
                    - 'allow'
                    - 'deny'
            pdu-notification:
                type: str
                description: Deprecated, please rename it to pdu_notification. PDU notification.
                choices:
                    - 'allow'
                    - 'deny'
            ran-info:
                type: str
                description: Deprecated, please rename it to ran_info. Ran info.
                choices:
                    - 'allow'
                    - 'deny'
            redirection:
                type: str
                description: Redirection.
                choices:
                    - 'allow'
                    - 'deny'
            relocation-cancel:
                type: str
                description: Deprecated, please rename it to relocation_cancel. Relocation cancel.
                choices:
                    - 'allow'
                    - 'deny'
            send-route:
                type: str
                description: Deprecated, please rename it to send_route. Send route.
                choices:
                    - 'allow'
                    - 'deny'
            sgsn-context:
                type: str
                description: Deprecated, please rename it to sgsn_context. SGSN context.
                choices:
                    - 'allow'
                    - 'deny'
            support-extension:
                type: str
                description: Deprecated, please rename it to support_extension. Support extension.
                choices:
                    - 'allow'
                    - 'deny'
            unknown-message-action:
                type: str
                description: Deprecated, please rename it to unknown_message_action. Unknown message action.
                choices:
                    - 'allow'
                    - 'deny'
            update-mbms:
                type: str
                description: Deprecated, please rename it to update_mbms. Update MBMS.
                choices:
                    - 'allow'
                    - 'deny'
            update-pdp:
                type: str
                description: Deprecated, please rename it to update_pdp. Update PDP.
                choices:
                    - 'allow'
                    - 'deny'
            version-not-support:
                type: str
                description: Deprecated, please rename it to version_not_support. Version not supported.
                choices:
                    - 'allow'
                    - 'deny'
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
    - name: Message filter.
      fortinet.fortimanager.fmgr_firewall_gtp_messagefilter:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        adom: <your own value>
        gtp: <your own value>
        firewall_gtp_messagefilter:
          create_aa_pdp: <value in [allow, deny]>
          create_mbms: <value in [allow, deny]>
          create_pdp: <value in [allow, deny]>
          data_record: <value in [allow, deny]>
          delete_aa_pdp: <value in [allow, deny]>
          delete_mbms: <value in [allow, deny]>
          delete_pdp: <value in [allow, deny]>
          echo: <value in [allow, deny]>
          error_indication: <value in [allow, deny]>
          failure_report: <value in [allow, deny]>
          fwd_relocation: <value in [allow, deny]>
          fwd_srns_context: <value in [allow, deny]>
          gtp_pdu: <value in [allow, deny]>
          identification: <value in [allow, deny]>
          mbms_notification: <value in [allow, deny]>
          node_alive: <value in [allow, deny]>
          note_ms_present: <value in [allow, deny]>
          pdu_notification: <value in [allow, deny]>
          ran_info: <value in [allow, deny]>
          redirection: <value in [allow, deny]>
          relocation_cancel: <value in [allow, deny]>
          send_route: <value in [allow, deny]>
          sgsn_context: <value in [allow, deny]>
          support_extension: <value in [allow, deny]>
          unknown_message_action: <value in [allow, deny]>
          update_mbms: <value in [allow, deny]>
          update_pdp: <value in [allow, deny]>
          version_not_support: <value in [allow, deny]>
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
        '/pm/config/adom/{adom}/obj/firewall/gtp/{gtp}/message-filter',
        '/pm/config/global/obj/firewall/gtp/{gtp}/message-filter'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/firewall/gtp/{gtp}/message-filter/{message-filter}',
        '/pm/config/global/obj/firewall/gtp/{gtp}/message-filter/{message-filter}'
    ]

    url_params = ['adom', 'gtp']
    module_primary_key = None
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'gtp': {'required': True, 'type': 'str'},
        'firewall_gtp_messagefilter': {
            'type': 'dict',
            'v_range': [['6.2.0', '6.2.12']],
            'options': {
                'create-aa-pdp': {'v_range': [['6.2.0', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'create-mbms': {'v_range': [['6.2.0', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'create-pdp': {'v_range': [['6.2.0', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'data-record': {'v_range': [['6.2.0', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'delete-aa-pdp': {'v_range': [['6.2.0', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'delete-mbms': {'v_range': [['6.2.0', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'delete-pdp': {'v_range': [['6.2.0', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'echo': {'v_range': [['6.2.0', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'error-indication': {'v_range': [['6.2.0', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'failure-report': {'v_range': [['6.2.0', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'fwd-relocation': {'v_range': [['6.2.0', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'fwd-srns-context': {'v_range': [['6.2.0', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'gtp-pdu': {'v_range': [['6.2.0', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'identification': {'v_range': [['6.2.0', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'mbms-notification': {'v_range': [['6.2.0', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'node-alive': {'v_range': [['6.2.0', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'note-ms-present': {'v_range': [['6.2.0', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'pdu-notification': {'v_range': [['6.2.0', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'ran-info': {'v_range': [['6.2.0', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'redirection': {'v_range': [['6.2.0', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'relocation-cancel': {'v_range': [['6.2.0', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'send-route': {'v_range': [['6.2.0', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'sgsn-context': {'v_range': [['6.2.0', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'support-extension': {'v_range': [['6.2.0', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'unknown-message-action': {'v_range': [['6.2.0', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'update-mbms': {'v_range': [['6.2.0', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'update-pdp': {'v_range': [['6.2.0', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'version-not-support': {'v_range': [['6.2.0', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('partial crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'firewall_gtp_messagefilter'),
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
