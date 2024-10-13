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
module: fmgr_firewall_gtp_messageratelimit
short_description: Message rate limiting.
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
    firewall_gtp_messageratelimit:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            create-aa-pdp-request:
                type: int
                description: Deprecated, please rename it to create_aa_pdp_request. Rate limit for create AA PDP context request
            create-aa-pdp-response:
                type: int
                description: Deprecated, please rename it to create_aa_pdp_response. Rate limit for create AA PDP context response
            create-mbms-request:
                type: int
                description: Deprecated, please rename it to create_mbms_request. Rate limit for create MBMS context request
            create-mbms-response:
                type: int
                description: Deprecated, please rename it to create_mbms_response. Rate limit for create MBMS context response
            create-pdp-request:
                type: int
                description: Deprecated, please rename it to create_pdp_request. Rate limit for create PDP context request
            create-pdp-response:
                type: int
                description: Deprecated, please rename it to create_pdp_response. Rate limit for create PDP context response
            delete-aa-pdp-request:
                type: int
                description: Deprecated, please rename it to delete_aa_pdp_request. Rate limit for delete AA PDP context request
            delete-aa-pdp-response:
                type: int
                description: Deprecated, please rename it to delete_aa_pdp_response. Rate limit for delete AA PDP context response
            delete-mbms-request:
                type: int
                description: Deprecated, please rename it to delete_mbms_request. Rate limit for delete MBMS context request
            delete-mbms-response:
                type: int
                description: Deprecated, please rename it to delete_mbms_response. Rate limit for delete MBMS context response
            delete-pdp-request:
                type: int
                description: Deprecated, please rename it to delete_pdp_request. Rate limit for delete PDP context request
            delete-pdp-response:
                type: int
                description: Deprecated, please rename it to delete_pdp_response. Rate limit for delete PDP context response
            echo-reponse:
                type: int
                description: Deprecated, please rename it to echo_reponse. Rate limit for echo response
            echo-request:
                type: int
                description: Deprecated, please rename it to echo_request. Rate limit for echo requests
            error-indication:
                type: int
                description: Deprecated, please rename it to error_indication. Rate limit for error indication
            failure-report-request:
                type: int
                description: Deprecated, please rename it to failure_report_request. Rate limit for failure report request
            failure-report-response:
                type: int
                description: Deprecated, please rename it to failure_report_response. Rate limit for failure report response
            fwd-reloc-complete-ack:
                type: int
                description: Deprecated, please rename it to fwd_reloc_complete_ack. Rate limit for forward relocation complete acknowledge
            fwd-relocation-complete:
                type: int
                description: Deprecated, please rename it to fwd_relocation_complete. Rate limit for forward relocation complete
            fwd-relocation-request:
                type: int
                description: Deprecated, please rename it to fwd_relocation_request. Rate limit for forward relocation request
            fwd-relocation-response:
                type: int
                description: Deprecated, please rename it to fwd_relocation_response. Rate limit for forward relocation response
            fwd-srns-context:
                type: int
                description: Deprecated, please rename it to fwd_srns_context. Rate limit for forward SRNS context
            fwd-srns-context-ack:
                type: int
                description: Deprecated, please rename it to fwd_srns_context_ack. Rate limit for forward SRNS context acknowledge
            g-pdu:
                type: int
                description: Deprecated, please rename it to g_pdu. Rate limit for G-PDU
            identification-request:
                type: int
                description: Deprecated, please rename it to identification_request. Rate limit for identification request
            identification-response:
                type: int
                description: Deprecated, please rename it to identification_response. Rate limit for identification response
            mbms-de-reg-request:
                type: int
                description: Deprecated, please rename it to mbms_de_reg_request. Rate limit for MBMS de-registration request
            mbms-de-reg-response:
                type: int
                description: Deprecated, please rename it to mbms_de_reg_response. Rate limit for MBMS de-registration response
            mbms-notify-rej-request:
                type: int
                description: Deprecated, please rename it to mbms_notify_rej_request. Rate limit for MBMS notification reject request
            mbms-notify-rej-response:
                type: int
                description: Deprecated, please rename it to mbms_notify_rej_response. Rate limit for MBMS notification reject response
            mbms-notify-request:
                type: int
                description: Deprecated, please rename it to mbms_notify_request. Rate limit for MBMS notification request
            mbms-notify-response:
                type: int
                description: Deprecated, please rename it to mbms_notify_response. Rate limit for MBMS notification response
            mbms-reg-request:
                type: int
                description: Deprecated, please rename it to mbms_reg_request. Rate limit for MBMS registration request
            mbms-reg-response:
                type: int
                description: Deprecated, please rename it to mbms_reg_response. Rate limit for MBMS registration response
            mbms-ses-start-request:
                type: int
                description: Deprecated, please rename it to mbms_ses_start_request. Rate limit for MBMS session start request
            mbms-ses-start-response:
                type: int
                description: Deprecated, please rename it to mbms_ses_start_response. Rate limit for MBMS session start response
            mbms-ses-stop-request:
                type: int
                description: Deprecated, please rename it to mbms_ses_stop_request. Rate limit for MBMS session stop request
            mbms-ses-stop-response:
                type: int
                description: Deprecated, please rename it to mbms_ses_stop_response. Rate limit for MBMS session stop response
            note-ms-request:
                type: int
                description: Deprecated, please rename it to note_ms_request. Rate limit for note MS GPRS present request
            note-ms-response:
                type: int
                description: Deprecated, please rename it to note_ms_response. Rate limit for note MS GPRS present response
            pdu-notify-rej-request:
                type: int
                description: Deprecated, please rename it to pdu_notify_rej_request. Rate limit for PDU notify reject request
            pdu-notify-rej-response:
                type: int
                description: Deprecated, please rename it to pdu_notify_rej_response. Rate limit for PDU notify reject response
            pdu-notify-request:
                type: int
                description: Deprecated, please rename it to pdu_notify_request. Rate limit for PDU notify request
            pdu-notify-response:
                type: int
                description: Deprecated, please rename it to pdu_notify_response. Rate limit for PDU notify response
            ran-info:
                type: int
                description: Deprecated, please rename it to ran_info. Rate limit for RAN information relay
            relocation-cancel-request:
                type: int
                description: Deprecated, please rename it to relocation_cancel_request. Rate limit for relocation cancel request
            relocation-cancel-response:
                type: int
                description: Deprecated, please rename it to relocation_cancel_response. Rate limit for relocation cancel response
            send-route-request:
                type: int
                description: Deprecated, please rename it to send_route_request. Rate limit for send routing information for GPRS request
            send-route-response:
                type: int
                description: Deprecated, please rename it to send_route_response. Rate limit for send routing information for GPRS response
            sgsn-context-ack:
                type: int
                description: Deprecated, please rename it to sgsn_context_ack. Rate limit for SGSN context acknowledgement
            sgsn-context-request:
                type: int
                description: Deprecated, please rename it to sgsn_context_request. Rate limit for SGSN context request
            sgsn-context-response:
                type: int
                description: Deprecated, please rename it to sgsn_context_response. Rate limit for SGSN context response
            support-ext-hdr-notify:
                type: int
                description: Deprecated, please rename it to support_ext_hdr_notify. Rate limit for support extension headers notification
            update-mbms-request:
                type: int
                description: Deprecated, please rename it to update_mbms_request. Rate limit for update MBMS context request
            update-mbms-response:
                type: int
                description: Deprecated, please rename it to update_mbms_response. Rate limit for update MBMS context response
            update-pdp-request:
                type: int
                description: Deprecated, please rename it to update_pdp_request. Rate limit for update PDP context request
            update-pdp-response:
                type: int
                description: Deprecated, please rename it to update_pdp_response. Rate limit for update PDP context response
            version-not-support:
                type: int
                description: Deprecated, please rename it to version_not_support. Rate limit for version not supported
            echo-response:
                type: int
                description: Deprecated, please rename it to echo_response. Rate limit for echo response
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
    - name: Message rate limiting.
      fortinet.fortimanager.fmgr_firewall_gtp_messageratelimit:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        adom: <your own value>
        gtp: <your own value>
        firewall_gtp_messageratelimit:
          create_aa_pdp_request: <integer>
          create_aa_pdp_response: <integer>
          create_mbms_request: <integer>
          create_mbms_response: <integer>
          create_pdp_request: <integer>
          create_pdp_response: <integer>
          delete_aa_pdp_request: <integer>
          delete_aa_pdp_response: <integer>
          delete_mbms_request: <integer>
          delete_mbms_response: <integer>
          delete_pdp_request: <integer>
          delete_pdp_response: <integer>
          echo_reponse: <integer>
          echo_request: <integer>
          error_indication: <integer>
          failure_report_request: <integer>
          failure_report_response: <integer>
          fwd_reloc_complete_ack: <integer>
          fwd_relocation_complete: <integer>
          fwd_relocation_request: <integer>
          fwd_relocation_response: <integer>
          fwd_srns_context: <integer>
          fwd_srns_context_ack: <integer>
          g_pdu: <integer>
          identification_request: <integer>
          identification_response: <integer>
          mbms_de_reg_request: <integer>
          mbms_de_reg_response: <integer>
          mbms_notify_rej_request: <integer>
          mbms_notify_rej_response: <integer>
          mbms_notify_request: <integer>
          mbms_notify_response: <integer>
          mbms_reg_request: <integer>
          mbms_reg_response: <integer>
          mbms_ses_start_request: <integer>
          mbms_ses_start_response: <integer>
          mbms_ses_stop_request: <integer>
          mbms_ses_stop_response: <integer>
          note_ms_request: <integer>
          note_ms_response: <integer>
          pdu_notify_rej_request: <integer>
          pdu_notify_rej_response: <integer>
          pdu_notify_request: <integer>
          pdu_notify_response: <integer>
          ran_info: <integer>
          relocation_cancel_request: <integer>
          relocation_cancel_response: <integer>
          send_route_request: <integer>
          send_route_response: <integer>
          sgsn_context_ack: <integer>
          sgsn_context_request: <integer>
          sgsn_context_response: <integer>
          support_ext_hdr_notify: <integer>
          update_mbms_request: <integer>
          update_mbms_response: <integer>
          update_pdp_request: <integer>
          update_pdp_response: <integer>
          version_not_support: <integer>
          echo_response: <integer>
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
        '/pm/config/adom/{adom}/obj/firewall/gtp/{gtp}/message-rate-limit',
        '/pm/config/global/obj/firewall/gtp/{gtp}/message-rate-limit'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/firewall/gtp/{gtp}/message-rate-limit/{message-rate-limit}',
        '/pm/config/global/obj/firewall/gtp/{gtp}/message-rate-limit/{message-rate-limit}'
    ]

    url_params = ['adom', 'gtp']
    module_primary_key = None
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'gtp': {'required': True, 'type': 'str'},
        'firewall_gtp_messageratelimit': {
            'type': 'dict',
            'v_range': [['6.0.0', '']],
            'options': {
                'create-aa-pdp-request': {'type': 'int'},
                'create-aa-pdp-response': {'type': 'int'},
                'create-mbms-request': {'type': 'int'},
                'create-mbms-response': {'type': 'int'},
                'create-pdp-request': {'type': 'int'},
                'create-pdp-response': {'type': 'int'},
                'delete-aa-pdp-request': {'type': 'int'},
                'delete-aa-pdp-response': {'type': 'int'},
                'delete-mbms-request': {'type': 'int'},
                'delete-mbms-response': {'type': 'int'},
                'delete-pdp-request': {'type': 'int'},
                'delete-pdp-response': {'type': 'int'},
                'echo-reponse': {'type': 'int'},
                'echo-request': {'type': 'int'},
                'error-indication': {'type': 'int'},
                'failure-report-request': {'type': 'int'},
                'failure-report-response': {'type': 'int'},
                'fwd-reloc-complete-ack': {'type': 'int'},
                'fwd-relocation-complete': {'type': 'int'},
                'fwd-relocation-request': {'type': 'int'},
                'fwd-relocation-response': {'type': 'int'},
                'fwd-srns-context': {'type': 'int'},
                'fwd-srns-context-ack': {'type': 'int'},
                'g-pdu': {'type': 'int'},
                'identification-request': {'type': 'int'},
                'identification-response': {'type': 'int'},
                'mbms-de-reg-request': {'type': 'int'},
                'mbms-de-reg-response': {'type': 'int'},
                'mbms-notify-rej-request': {'type': 'int'},
                'mbms-notify-rej-response': {'type': 'int'},
                'mbms-notify-request': {'type': 'int'},
                'mbms-notify-response': {'type': 'int'},
                'mbms-reg-request': {'type': 'int'},
                'mbms-reg-response': {'type': 'int'},
                'mbms-ses-start-request': {'type': 'int'},
                'mbms-ses-start-response': {'type': 'int'},
                'mbms-ses-stop-request': {'type': 'int'},
                'mbms-ses-stop-response': {'type': 'int'},
                'note-ms-request': {'type': 'int'},
                'note-ms-response': {'type': 'int'},
                'pdu-notify-rej-request': {'type': 'int'},
                'pdu-notify-rej-response': {'type': 'int'},
                'pdu-notify-request': {'type': 'int'},
                'pdu-notify-response': {'type': 'int'},
                'ran-info': {'type': 'int'},
                'relocation-cancel-request': {'type': 'int'},
                'relocation-cancel-response': {'type': 'int'},
                'send-route-request': {'type': 'int'},
                'send-route-response': {'type': 'int'},
                'sgsn-context-ack': {'type': 'int'},
                'sgsn-context-request': {'type': 'int'},
                'sgsn-context-response': {'type': 'int'},
                'support-ext-hdr-notify': {'type': 'int'},
                'update-mbms-request': {'type': 'int'},
                'update-mbms-response': {'type': 'int'},
                'update-pdp-request': {'type': 'int'},
                'update-pdp-response': {'type': 'int'},
                'version-not-support': {'type': 'int'},
                'echo-response': {'v_range': [['7.4.3', '']], 'type': 'int'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('partial crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'firewall_gtp_messageratelimit'),
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
