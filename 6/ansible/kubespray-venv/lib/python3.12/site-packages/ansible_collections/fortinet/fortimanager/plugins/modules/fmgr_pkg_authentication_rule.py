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
module: fmgr_pkg_authentication_rule
short_description: Configure Authentication Rules.
description:
    - This module is able to configure a FortiManager device.
    - Examples include all parameters and values which need to be adjusted to data sources before usage.

version_added: "2.1.0"
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
    pkg:
        description: The parameter (pkg) in requested url.
        type: str
        required: true
    pkg_authentication_rule:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            active-auth-method:
                type: str
                description: Deprecated, please rename it to active_auth_method. Select an active authentication method.
            comments:
                type: str
                description: Comment.
            ip-based:
                type: str
                description: Deprecated, please rename it to ip_based. Enable/disable IP-based authentication.
                choices:
                    - 'disable'
                    - 'enable'
            name:
                type: str
                description: Authentication rule name.
                required: true
            protocol:
                type: str
                description: Select the protocol to use for authentication
                choices:
                    - 'http'
                    - 'ftp'
                    - 'socks'
                    - 'ssh'
            srcaddr:
                type: raw
                description: (list or str) Select an IPv4 source address from available options.
            srcaddr6:
                type: raw
                description: (list or str) Select an IPv6 source address.
            sso-auth-method:
                type: str
                description: Deprecated, please rename it to sso_auth_method. Select a single-sign on
            status:
                type: str
                description: Enable/disable this authentication rule.
                choices:
                    - 'disable'
                    - 'enable'
            transaction-based:
                type: str
                description: Deprecated, please rename it to transaction_based. Enable/disable transaction based authentication
                choices:
                    - 'disable'
                    - 'enable'
            web-auth-cookie:
                type: str
                description: Deprecated, please rename it to web_auth_cookie. Enable/disable Web authentication cookies
                choices:
                    - 'disable'
                    - 'enable'
            web-portal:
                type: str
                description: Deprecated, please rename it to web_portal. Enable/disable web portal for proxy transparent policy
                choices:
                    - 'disable'
                    - 'enable'
            dstaddr:
                type: raw
                description: (list or str) Select an IPv4 destination address from available options.
            dstaddr6:
                type: raw
                description: (list or str) Select an IPv6 destination address from available options.
            srcintf:
                type: raw
                description: (list or str) Incoming
            cors-depth:
                type: int
                description: Deprecated, please rename it to cors_depth. Depth to allow CORS access
            cors-stateful:
                type: str
                description: Deprecated, please rename it to cors_stateful. Enable/disable allowance of CORS access
                choices:
                    - 'disable'
                    - 'enable'
            cert-auth-cookie:
                type: str
                description: Deprecated, please rename it to cert_auth_cookie. Enable/disable to use device certificate as authentication cookie
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
    - name: Configure Authentication Rules.
      fortinet.fortimanager.fmgr_pkg_authentication_rule:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        adom: <your own value>
        pkg: <your own value>
        state: present # <value in [present, absent]>
        pkg_authentication_rule:
          active_auth_method: <string>
          comments: <string>
          ip_based: <value in [disable, enable]>
          name: <string>
          protocol: <value in [http, ftp, socks, ...]>
          srcaddr: <list or string>
          srcaddr6: <list or string>
          sso_auth_method: <string>
          status: <value in [disable, enable]>
          transaction_based: <value in [disable, enable]>
          web_auth_cookie: <value in [disable, enable]>
          web_portal: <value in [disable, enable]>
          dstaddr: <list or string>
          dstaddr6: <list or string>
          srcintf: <list or string>
          cors_depth: <integer>
          cors_stateful: <value in [disable, enable]>
          cert_auth_cookie: <value in [disable, enable]>
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
        '/pm/config/adom/{adom}/pkg/{pkg}/authentication/rule'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/pkg/{pkg}/authentication/rule/{rule}'
    ]

    url_params = ['adom', 'pkg']
    module_primary_key = 'name'
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'pkg': {'required': True, 'type': 'str'},
        'pkg_authentication_rule': {
            'type': 'dict',
            'v_range': [['6.2.1', '']],
            'options': {
                'active-auth-method': {'v_range': [['6.2.1', '']], 'type': 'str'},
                'comments': {'v_range': [['6.2.1', '']], 'type': 'str'},
                'ip-based': {'v_range': [['6.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'name': {'v_range': [['6.2.1', '']], 'required': True, 'type': 'str'},
                'protocol': {'v_range': [['6.2.1', '']], 'choices': ['http', 'ftp', 'socks', 'ssh'], 'type': 'str'},
                'srcaddr': {'v_range': [['6.2.1', '']], 'type': 'raw'},
                'srcaddr6': {'v_range': [['6.2.1', '']], 'type': 'raw'},
                'sso-auth-method': {'v_range': [['6.2.1', '']], 'type': 'str'},
                'status': {'v_range': [['6.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'transaction-based': {'v_range': [['6.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'web-auth-cookie': {'v_range': [['6.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'web-portal': {'v_range': [['6.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'dstaddr': {'v_range': [['7.0.0', '']], 'type': 'raw'},
                'dstaddr6': {'v_range': [['7.0.0', '']], 'type': 'raw'},
                'srcintf': {'v_range': [['7.0.0', '']], 'type': 'raw'},
                'cors-depth': {'v_range': [['7.4.1', '']], 'type': 'int'},
                'cors-stateful': {'v_range': [['7.4.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'cert-auth-cookie': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('full crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'pkg_authentication_rule'),
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
