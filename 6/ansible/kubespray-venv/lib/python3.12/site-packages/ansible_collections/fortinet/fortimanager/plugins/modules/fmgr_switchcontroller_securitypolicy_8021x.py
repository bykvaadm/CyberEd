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
module: fmgr_switchcontroller_securitypolicy_8021x
short_description: Configure 802.
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
    switchcontroller_securitypolicy_8021x:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            auth-fail-vlan:
                type: str
                description: Deprecated, please rename it to auth_fail_vlan. Enable to allow limited access to clients that cannot authenticate.
                choices:
                    - 'disable'
                    - 'enable'
            auth-fail-vlan-id:
                type: str
                description: Deprecated, please rename it to auth_fail_vlan_id. VLAN ID on which authentication failed.
            auth-fail-vlanid:
                type: int
                description: Deprecated, please rename it to auth_fail_vlanid. VLAN ID on which authentication failed.
            eap-passthru:
                type: str
                description: Deprecated, please rename it to eap_passthru. Enable/disable EAP pass-through mode, allowing protocols
                choices:
                    - 'disable'
                    - 'enable'
            guest-auth-delay:
                type: int
                description: Deprecated, please rename it to guest_auth_delay. Guest authentication delay
            guest-vlan:
                type: str
                description: Deprecated, please rename it to guest_vlan. Enable the guest VLAN feature to allow limited access to non-802.
                choices:
                    - 'disable'
                    - 'enable'
            guest-vlan-id:
                type: str
                description: Deprecated, please rename it to guest_vlan_id. Guest VLAN name.
            guest-vlanid:
                type: int
                description: Deprecated, please rename it to guest_vlanid. Guest VLAN ID.
            mac-auth-bypass:
                type: str
                description: Deprecated, please rename it to mac_auth_bypass. Enable/disable MAB for this policy.
                choices:
                    - 'disable'
                    - 'enable'
            name:
                type: str
                description: Policy name.
                required: true
            open-auth:
                type: str
                description: Deprecated, please rename it to open_auth. Enable/disable open authentication for this policy.
                choices:
                    - 'disable'
                    - 'enable'
            policy-type:
                type: str
                description: Deprecated, please rename it to policy_type. Policy type.
                choices:
                    - '802.1X'
            radius-timeout-overwrite:
                type: str
                description: Deprecated, please rename it to radius_timeout_overwrite. Enable to override the global RADIUS session timeout.
                choices:
                    - 'disable'
                    - 'enable'
            security-mode:
                type: str
                description: Deprecated, please rename it to security_mode. Port or MAC based 802.
                choices:
                    - '802.1X'
                    - '802.1X-mac-based'
            user-group:
                type: raw
                description: (list or str) Deprecated, please rename it to user_group. Name of user-group to assign to this MAC Authentication Bypass
            framevid-apply:
                type: str
                description: Deprecated, please rename it to framevid_apply. Enable/disable the capability to apply the EAP/MAB frame VLAN to the port ...
                choices:
                    - 'disable'
                    - 'enable'
            eap-auto-untagged-vlans:
                type: str
                description: Deprecated, please rename it to eap_auto_untagged_vlans. Enable/disable automatic inclusion of untagged VLANs.
                choices:
                    - 'disable'
                    - 'enable'
            authserver-timeout-period:
                type: int
                description: Deprecated, please rename it to authserver_timeout_period. Authentication server timeout period
            authserver-timeout-vlan:
                type: str
                description: Deprecated, please rename it to authserver_timeout_vlan. Enable/disable the authentication server timeout VLAN to allow li...
                choices:
                    - 'disable'
                    - 'enable'
            authserver-timeout-vlanid:
                type: str
                description: Deprecated, please rename it to authserver_timeout_vlanid. Authentication server timeout VLAN name.
            authserver-timeout-tagged:
                type: str
                description: Deprecated, please rename it to authserver_timeout_tagged. Configure timeout option for the tagged VLAN which allows limit...
                choices:
                    - 'static'
                    - 'disable'
                    - 'lldp-voice'
            authserver-timeout-tagged-vlanid:
                type: raw
                description: (list) Deprecated, please rename it to authserver_timeout_tagged_vlanid. Tagged VLAN name for which the timeout option is ...
            dacl:
                type: str
                description: Enable/disable dynamic access control list on this interface.
                choices:
                    - 'disable'
                    - 'enable'
            auth-order:
                type: str
                description: Deprecated, please rename it to auth_order. Configure authentication order.
                choices:
                    - 'dot1x-mab'
                    - 'mab-dot1x'
                    - 'mab'
            auth-priority:
                type: str
                description: Deprecated, please rename it to auth_priority. Configure authentication priority.
                choices:
                    - 'dot1x-mab'
                    - 'mab-dot1x'
                    - 'legacy'
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
    - name: Configure 802.
      fortinet.fortimanager.fmgr_switchcontroller_securitypolicy_8021x:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: present # <value in [present, absent]>
        switchcontroller_securitypolicy_8021x:
          auth_fail_vlan: <value in [disable, enable]>
          auth_fail_vlan_id: <string>
          auth_fail_vlanid: <integer>
          eap_passthru: <value in [disable, enable]>
          guest_auth_delay: <integer>
          guest_vlan: <value in [disable, enable]>
          guest_vlan_id: <string>
          guest_vlanid: <integer>
          mac_auth_bypass: <value in [disable, enable]>
          name: <string>
          open_auth: <value in [disable, enable]>
          policy_type: <value in [802.1X]>
          radius_timeout_overwrite: <value in [disable, enable]>
          security_mode: <value in [802.1X, 802.1X-mac-based]>
          user_group: <list or string>
          framevid_apply: <value in [disable, enable]>
          eap_auto_untagged_vlans: <value in [disable, enable]>
          authserver_timeout_period: <integer>
          authserver_timeout_vlan: <value in [disable, enable]>
          authserver_timeout_vlanid: <string>
          authserver_timeout_tagged: <value in [static, disable, lldp-voice]>
          authserver_timeout_tagged_vlanid: <list or string>
          dacl: <value in [disable, enable]>
          auth_order: <value in [dot1x-mab, mab-dot1x, mab]>
          auth_priority: <value in [dot1x-mab, mab-dot1x, legacy]>
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
        '/pm/config/adom/{adom}/obj/switch-controller/security-policy/802-1X',
        '/pm/config/global/obj/switch-controller/security-policy/802-1X'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/switch-controller/security-policy/802-1X/{802-1X}',
        '/pm/config/global/obj/switch-controller/security-policy/802-1X/{802-1X}'
    ]

    url_params = ['adom']
    module_primary_key = 'name'
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'switchcontroller_securitypolicy_8021x': {
            'type': 'dict',
            'v_range': [['6.0.0', '']],
            'options': {
                'auth-fail-vlan': {'choices': ['disable', 'enable'], 'type': 'str'},
                'auth-fail-vlan-id': {'type': 'str'},
                'auth-fail-vlanid': {'type': 'int'},
                'eap-passthru': {'choices': ['disable', 'enable'], 'type': 'str'},
                'guest-auth-delay': {'type': 'int'},
                'guest-vlan': {'choices': ['disable', 'enable'], 'type': 'str'},
                'guest-vlan-id': {'type': 'str'},
                'guest-vlanid': {'type': 'int'},
                'mac-auth-bypass': {'choices': ['disable', 'enable'], 'type': 'str'},
                'name': {'required': True, 'type': 'str'},
                'open-auth': {'choices': ['disable', 'enable'], 'type': 'str'},
                'policy-type': {'choices': ['802.1X'], 'type': 'str'},
                'radius-timeout-overwrite': {'choices': ['disable', 'enable'], 'type': 'str'},
                'security-mode': {'choices': ['802.1X', '802.1X-mac-based'], 'type': 'str'},
                'user-group': {'type': 'raw'},
                'framevid-apply': {'v_range': [['6.2.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'eap-auto-untagged-vlans': {'v_range': [['6.4.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'authserver-timeout-period': {'v_range': [['6.4.3', '']], 'type': 'int'},
                'authserver-timeout-vlan': {'v_range': [['6.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'authserver-timeout-vlanid': {'v_range': [['6.4.3', '']], 'type': 'str'},
                'authserver-timeout-tagged': {'v_range': [['7.4.3', '']], 'choices': ['static', 'disable', 'lldp-voice'], 'type': 'str'},
                'authserver-timeout-tagged-vlanid': {'v_range': [['7.4.3', '']], 'type': 'raw'},
                'dacl': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'auth-order': {'v_range': [['7.6.0', '']], 'choices': ['dot1x-mab', 'mab-dot1x', 'mab'], 'type': 'str'},
                'auth-priority': {'v_range': [['7.6.0', '']], 'choices': ['dot1x-mab', 'mab-dot1x', 'legacy'], 'type': 'str'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('full crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'switchcontroller_securitypolicy_8021x'),
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
