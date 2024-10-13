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
module: fmgr_gtp_messagefilterv2
short_description: Message filter for GTPv2 messages.
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
    gtp_messagefilterv2:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            bearer-resource-cmd-fail:
                type: str
                description: Deprecated, please rename it to bearer_resource_cmd_fail. Bearer resource
                choices:
                    - 'allow'
                    - 'deny'
            change-notification:
                type: str
                description: Deprecated, please rename it to change_notification. Change notification
                choices:
                    - 'allow'
                    - 'deny'
            create-bearer:
                type: str
                description: Deprecated, please rename it to create_bearer. Create bearer
                choices:
                    - 'allow'
                    - 'deny'
            create-session:
                type: str
                description: Deprecated, please rename it to create_session. Create session
                choices:
                    - 'allow'
                    - 'deny'
            delete-bearer-cmd-fail:
                type: str
                description: Deprecated, please rename it to delete_bearer_cmd_fail. Delete bearer
                choices:
                    - 'allow'
                    - 'deny'
            delete-bearer-req-resp:
                type: str
                description: Deprecated, please rename it to delete_bearer_req_resp. Delete bearer
                choices:
                    - 'allow'
                    - 'deny'
            delete-pdn-connection-set:
                type: str
                description: Deprecated, please rename it to delete_pdn_connection_set. Delete PDN connection set
                choices:
                    - 'allow'
                    - 'deny'
            delete-session:
                type: str
                description: Deprecated, please rename it to delete_session. Delete session
                choices:
                    - 'allow'
                    - 'deny'
            echo:
                type: str
                description: Echo
                choices:
                    - 'allow'
                    - 'deny'
            modify-bearer-cmd-fail:
                type: str
                description: Deprecated, please rename it to modify_bearer_cmd_fail. Modify bearer
                choices:
                    - 'allow'
                    - 'deny'
            modify-bearer-req-resp:
                type: str
                description: Deprecated, please rename it to modify_bearer_req_resp. Modify bearer
                choices:
                    - 'allow'
                    - 'deny'
            name:
                type: str
                description: Message filter name.
                required: true
            resume:
                type: str
                description: Resume
                choices:
                    - 'allow'
                    - 'deny'
            suspend:
                type: str
                description: Suspend
                choices:
                    - 'allow'
                    - 'deny'
            trace-session:
                type: str
                description: Deprecated, please rename it to trace_session. Trace session
                choices:
                    - 'allow'
                    - 'deny'
            unknown-message:
                type: str
                description: Deprecated, please rename it to unknown_message. Allow or Deny unknown messages.
                choices:
                    - 'allow'
                    - 'deny'
            unknown-message-white-list:
                type: raw
                description: (list) Deprecated, please rename it to unknown_message_white_list. White list
            update-bearer:
                type: str
                description: Deprecated, please rename it to update_bearer. Update bearer
                choices:
                    - 'allow'
                    - 'deny'
            update-pdn-connection-set:
                type: str
                description: Deprecated, please rename it to update_pdn_connection_set. Update PDN connection set
                choices:
                    - 'allow'
                    - 'deny'
            version-not-support:
                type: str
                description: Deprecated, please rename it to version_not_support. Version not supported
                choices:
                    - 'allow'
                    - 'deny'
            context-req-res-ack:
                type: str
                description: Deprecated, please rename it to context_req_res_ack. Context request/response/acknowledge
                choices:
                    - 'allow'
                    - 'deny'
            forward-relocation-cmp-notif-ack:
                type: str
                description: Deprecated, please rename it to forward_relocation_cmp_notif_ack. Forward relocation complete notification/acknowledge
                choices:
                    - 'allow'
                    - 'deny'
            forward-relocation-req-res:
                type: str
                description: Deprecated, please rename it to forward_relocation_req_res. Forward relocation request/response
                choices:
                    - 'allow'
                    - 'deny'
            alert-mme-notif-ack:
                type: str
                description: Deprecated, please rename it to alert_mme_notif_ack. Alert MME notification/acknowledge
                choices:
                    - 'allow'
                    - 'deny'
            configuration-transfer-tunnel:
                type: str
                description: Deprecated, please rename it to configuration_transfer_tunnel. Configuration transfer tunnel
                choices:
                    - 'allow'
                    - 'deny'
            create-forwarding-tunnel-req-resp:
                type: str
                description: Deprecated, please rename it to create_forwarding_tunnel_req_resp. Create forwarding tunnel request/response
                choices:
                    - 'allow'
                    - 'deny'
            create-indirect-forwarding-tunnel-req-resp:
                type: str
                description: Deprecated, please rename it to create_indirect_forwarding_tunnel_req_resp. Create indirect data forwarding tunnel request...
                choices:
                    - 'allow'
                    - 'deny'
            cs-paging:
                type: str
                description: Deprecated, please rename it to cs_paging. CS paging indication
                choices:
                    - 'allow'
                    - 'deny'
            delete-indirect-forwarding-tunnel-req-resp:
                type: str
                description: Deprecated, please rename it to delete_indirect_forwarding_tunnel_req_resp. Delete indirect data forwarding tunnel request...
                choices:
                    - 'allow'
                    - 'deny'
            detach-notif-ack:
                type: str
                description: Deprecated, please rename it to detach_notif_ack. Detach notification/acknowledge
                choices:
                    - 'allow'
                    - 'deny'
            dlink-data-notif-ack:
                type: str
                description: Deprecated, please rename it to dlink_data_notif_ack. Downlink data notification/acknowledge
                choices:
                    - 'allow'
                    - 'deny'
            dlink-notif-failure:
                type: str
                description: Deprecated, please rename it to dlink_notif_failure. Downlink data notification failure indication
                choices:
                    - 'allow'
                    - 'deny'
            forward-access-notif-ack:
                type: str
                description: Deprecated, please rename it to forward_access_notif_ack. Forward access context notification/acknowledge
                choices:
                    - 'allow'
                    - 'deny'
            identification-req-resp:
                type: str
                description: Deprecated, please rename it to identification_req_resp. Identification request/response
                choices:
                    - 'allow'
                    - 'deny'
            isr-status:
                type: str
                description: Deprecated, please rename it to isr_status. ISR status indication
                choices:
                    - 'allow'
                    - 'deny'
            mbms-session-start-req-resp:
                type: str
                description: Deprecated, please rename it to mbms_session_start_req_resp. MBMS session start request/response
                choices:
                    - 'allow'
                    - 'deny'
            mbms-session-stop-req-resp:
                type: str
                description: Deprecated, please rename it to mbms_session_stop_req_resp. MBMS session stop request/response
                choices:
                    - 'allow'
                    - 'deny'
            mbms-session-update-req-resp:
                type: str
                description: Deprecated, please rename it to mbms_session_update_req_resp. MBMS session update request/response
                choices:
                    - 'allow'
                    - 'deny'
            modify-access-req-resp:
                type: str
                description: Deprecated, please rename it to modify_access_req_resp. Modify access bearers request/response
                choices:
                    - 'allow'
                    - 'deny'
            pgw-dlink-notif-ack:
                type: str
                description: Deprecated, please rename it to pgw_dlink_notif_ack. PGW downlink triggering notification/acknowledge
                choices:
                    - 'allow'
                    - 'deny'
            pgw-restart-notif-ack:
                type: str
                description: Deprecated, please rename it to pgw_restart_notif_ack. PGW restart notification/acknowledge
                choices:
                    - 'allow'
                    - 'deny'
            ran-info-relay:
                type: str
                description: Deprecated, please rename it to ran_info_relay. RAN information relay
                choices:
                    - 'allow'
                    - 'deny'
            release-access-bearer-req-resp:
                type: str
                description: Deprecated, please rename it to release_access_bearer_req_resp. Release access bearers request/response
                choices:
                    - 'allow'
                    - 'deny'
            relocation-cancel-req-resp:
                type: str
                description: Deprecated, please rename it to relocation_cancel_req_resp. Relocation cancel request/response
                choices:
                    - 'allow'
                    - 'deny'
            remote-ue-report-notif-ack:
                type: str
                description: Deprecated, please rename it to remote_ue_report_notif_ack. Remote UE report notification/acknowledge
                choices:
                    - 'allow'
                    - 'deny'
            reserved-for-earlier-version:
                type: str
                description: Deprecated, please rename it to reserved_for_earlier_version. Reserved for earlier version of the GTP specification
                choices:
                    - 'allow'
                    - 'deny'
            stop-paging-indication:
                type: str
                description: Deprecated, please rename it to stop_paging_indication. Stop Paging Indication
                choices:
                    - 'allow'
                    - 'deny'
            ue-activity-notif-ack:
                type: str
                description: Deprecated, please rename it to ue_activity_notif_ack. UE activity notification/acknowledge
                choices:
                    - 'allow'
                    - 'deny'
            ue-registration-query-req-resp:
                type: str
                description: Deprecated, please rename it to ue_registration_query_req_resp. UE registration query request/response
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
    - name: Message filter for GTPv2 messages.
      fortinet.fortimanager.fmgr_gtp_messagefilterv2:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: present # <value in [present, absent]>
        gtp_messagefilterv2:
          bearer_resource_cmd_fail: <value in [allow, deny]>
          change_notification: <value in [allow, deny]>
          create_bearer: <value in [allow, deny]>
          create_session: <value in [allow, deny]>
          delete_bearer_cmd_fail: <value in [allow, deny]>
          delete_bearer_req_resp: <value in [allow, deny]>
          delete_pdn_connection_set: <value in [allow, deny]>
          delete_session: <value in [allow, deny]>
          echo: <value in [allow, deny]>
          modify_bearer_cmd_fail: <value in [allow, deny]>
          modify_bearer_req_resp: <value in [allow, deny]>
          name: <string>
          resume: <value in [allow, deny]>
          suspend: <value in [allow, deny]>
          trace_session: <value in [allow, deny]>
          unknown_message: <value in [allow, deny]>
          unknown_message_white_list: <list or integer>
          update_bearer: <value in [allow, deny]>
          update_pdn_connection_set: <value in [allow, deny]>
          version_not_support: <value in [allow, deny]>
          context_req_res_ack: <value in [allow, deny]>
          forward_relocation_cmp_notif_ack: <value in [allow, deny]>
          forward_relocation_req_res: <value in [allow, deny]>
          alert_mme_notif_ack: <value in [allow, deny]>
          configuration_transfer_tunnel: <value in [allow, deny]>
          create_forwarding_tunnel_req_resp: <value in [allow, deny]>
          create_indirect_forwarding_tunnel_req_resp: <value in [allow, deny]>
          cs_paging: <value in [allow, deny]>
          delete_indirect_forwarding_tunnel_req_resp: <value in [allow, deny]>
          detach_notif_ack: <value in [allow, deny]>
          dlink_data_notif_ack: <value in [allow, deny]>
          dlink_notif_failure: <value in [allow, deny]>
          forward_access_notif_ack: <value in [allow, deny]>
          identification_req_resp: <value in [allow, deny]>
          isr_status: <value in [allow, deny]>
          mbms_session_start_req_resp: <value in [allow, deny]>
          mbms_session_stop_req_resp: <value in [allow, deny]>
          mbms_session_update_req_resp: <value in [allow, deny]>
          modify_access_req_resp: <value in [allow, deny]>
          pgw_dlink_notif_ack: <value in [allow, deny]>
          pgw_restart_notif_ack: <value in [allow, deny]>
          ran_info_relay: <value in [allow, deny]>
          release_access_bearer_req_resp: <value in [allow, deny]>
          relocation_cancel_req_resp: <value in [allow, deny]>
          remote_ue_report_notif_ack: <value in [allow, deny]>
          reserved_for_earlier_version: <value in [allow, deny]>
          stop_paging_indication: <value in [allow, deny]>
          ue_activity_notif_ack: <value in [allow, deny]>
          ue_registration_query_req_resp: <value in [allow, deny]>
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
        '/pm/config/adom/{adom}/obj/gtp/message-filter-v2',
        '/pm/config/global/obj/gtp/message-filter-v2'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/gtp/message-filter-v2/{message-filter-v2}',
        '/pm/config/global/obj/gtp/message-filter-v2/{message-filter-v2}'
    ]

    url_params = ['adom']
    module_primary_key = 'name'
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'gtp_messagefilterv2': {
            'type': 'dict',
            'v_range': [['6.0.0', '']],
            'options': {
                'bearer-resource-cmd-fail': {'choices': ['allow', 'deny'], 'type': 'str'},
                'change-notification': {'choices': ['allow', 'deny'], 'type': 'str'},
                'create-bearer': {'choices': ['allow', 'deny'], 'type': 'str'},
                'create-session': {'choices': ['allow', 'deny'], 'type': 'str'},
                'delete-bearer-cmd-fail': {'choices': ['allow', 'deny'], 'type': 'str'},
                'delete-bearer-req-resp': {'choices': ['allow', 'deny'], 'type': 'str'},
                'delete-pdn-connection-set': {'choices': ['allow', 'deny'], 'type': 'str'},
                'delete-session': {'choices': ['allow', 'deny'], 'type': 'str'},
                'echo': {'choices': ['allow', 'deny'], 'type': 'str'},
                'modify-bearer-cmd-fail': {'choices': ['allow', 'deny'], 'type': 'str'},
                'modify-bearer-req-resp': {'choices': ['allow', 'deny'], 'type': 'str'},
                'name': {'required': True, 'type': 'str'},
                'resume': {'choices': ['allow', 'deny'], 'type': 'str'},
                'suspend': {'choices': ['allow', 'deny'], 'type': 'str'},
                'trace-session': {'choices': ['allow', 'deny'], 'type': 'str'},
                'unknown-message': {'choices': ['allow', 'deny'], 'type': 'str'},
                'unknown-message-white-list': {'type': 'raw'},
                'update-bearer': {'choices': ['allow', 'deny'], 'type': 'str'},
                'update-pdn-connection-set': {'choices': ['allow', 'deny'], 'type': 'str'},
                'version-not-support': {'choices': ['allow', 'deny'], 'type': 'str'},
                'context-req-res-ack': {'v_range': [['7.0.2', '']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'forward-relocation-cmp-notif-ack': {'v_range': [['7.0.2', '']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'forward-relocation-req-res': {'v_range': [['7.0.2', '']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'alert-mme-notif-ack': {'v_range': [['7.2.1', '']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'configuration-transfer-tunnel': {'v_range': [['7.2.1', '']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'create-forwarding-tunnel-req-resp': {'v_range': [['7.2.1', '']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'create-indirect-forwarding-tunnel-req-resp': {'v_range': [['7.2.1', '']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'cs-paging': {'v_range': [['7.2.1', '']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'delete-indirect-forwarding-tunnel-req-resp': {'v_range': [['7.2.1', '']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'detach-notif-ack': {'v_range': [['7.2.1', '']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'dlink-data-notif-ack': {'v_range': [['7.2.1', '']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'dlink-notif-failure': {'v_range': [['7.2.1', '']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'forward-access-notif-ack': {'v_range': [['7.2.1', '']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'identification-req-resp': {'v_range': [['7.2.1', '']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'isr-status': {'v_range': [['7.2.1', '']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'mbms-session-start-req-resp': {'v_range': [['7.2.1', '']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'mbms-session-stop-req-resp': {'v_range': [['7.2.1', '']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'mbms-session-update-req-resp': {'v_range': [['7.2.1', '']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'modify-access-req-resp': {'v_range': [['7.2.1', '']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'pgw-dlink-notif-ack': {'v_range': [['7.2.1', '']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'pgw-restart-notif-ack': {'v_range': [['7.2.1', '']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'ran-info-relay': {'v_range': [['7.2.1', '']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'release-access-bearer-req-resp': {'v_range': [['7.2.1', '']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'relocation-cancel-req-resp': {'v_range': [['7.2.1', '']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'remote-ue-report-notif-ack': {'v_range': [['7.2.1', '']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'reserved-for-earlier-version': {'v_range': [['7.2.1', '']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'stop-paging-indication': {'v_range': [['7.2.1', '']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'ue-activity-notif-ack': {'v_range': [['7.2.1', '']], 'choices': ['allow', 'deny'], 'type': 'str'},
                'ue-registration-query-req-resp': {'v_range': [['7.2.1', '']], 'choices': ['allow', 'deny'], 'type': 'str'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('full crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'gtp_messagefilterv2'),
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
