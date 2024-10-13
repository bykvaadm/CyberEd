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
module: fmgr_webproxy_profile
short_description: Configure web proxy profiles.
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
    webproxy_profile:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            header-client-ip:
                type: str
                description: Deprecated, please rename it to header_client_ip. Action to take on the HTTP client-IP header in forwarded requests
                choices:
                    - 'pass'
                    - 'add'
                    - 'remove'
            header-front-end-https:
                type: str
                description: Deprecated, please rename it to header_front_end_https. Action to take on the HTTP front-end-HTTPS header in forwarded req...
                choices:
                    - 'pass'
                    - 'add'
                    - 'remove'
            header-via-request:
                type: str
                description: Deprecated, please rename it to header_via_request. Action to take on the HTTP via header in forwarded requests
                choices:
                    - 'pass'
                    - 'add'
                    - 'remove'
            header-via-response:
                type: str
                description: Deprecated, please rename it to header_via_response. Action to take on the HTTP via header in forwarded responses
                choices:
                    - 'pass'
                    - 'add'
                    - 'remove'
            header-x-authenticated-groups:
                type: str
                description: Deprecated, please rename it to header_x_authenticated_groups. Action to take on the HTTP x-authenticated-groups header in...
                choices:
                    - 'pass'
                    - 'add'
                    - 'remove'
            header-x-authenticated-user:
                type: str
                description: Deprecated, please rename it to header_x_authenticated_user. Action to take on the HTTP x-authenticated-user header in for...
                choices:
                    - 'pass'
                    - 'add'
                    - 'remove'
            header-x-forwarded-for:
                type: str
                description: Deprecated, please rename it to header_x_forwarded_for. Action to take on the HTTP x-forwarded-for header in forwarded req...
                choices:
                    - 'pass'
                    - 'add'
                    - 'remove'
            headers:
                type: list
                elements: dict
                description: Headers.
                suboptions:
                    action:
                        type: str
                        description: Action when HTTP the header forwarded.
                        choices:
                            - 'add-to-request'
                            - 'add-to-response'
                            - 'remove-from-request'
                            - 'remove-from-response'
                            - 'monitor-request'
                            - 'monitor-response'
                    content:
                        type: str
                        description: HTTP headers content.
                    id:
                        type: int
                        description: HTTP forwarded header id.
                    name:
                        type: str
                        description: HTTP forwarded header name.
                    add-option:
                        type: str
                        description: Deprecated, please rename it to add_option. Configure options to append content to existing HTTP header or add new...
                        choices:
                            - 'append'
                            - 'new-on-not-found'
                            - 'new'
                    base64-encoding:
                        type: str
                        description: Deprecated, please rename it to base64_encoding. Enable/disable use of base64 encoding of HTTP content.
                        choices:
                            - 'disable'
                            - 'enable'
                    dstaddr:
                        type: raw
                        description: (list or str) Destination address and address group names.
                    dstaddr6:
                        type: raw
                        description: (list or str) Destination address and address group names
                    protocol:
                        type: list
                        elements: str
                        description: Configure protocol
                        choices:
                            - 'https'
                            - 'http'
            log-header-change:
                type: str
                description: Deprecated, please rename it to log_header_change. Enable/disable logging HTTP header changes.
                choices:
                    - 'disable'
                    - 'enable'
            name:
                type: str
                description: Profile name.
                required: true
            strip-encoding:
                type: str
                description: Deprecated, please rename it to strip_encoding. Enable/disable stripping unsupported encoding from the request header.
                choices:
                    - 'disable'
                    - 'enable'
            header-x-forwarded-client-cert:
                type: str
                description: Deprecated, please rename it to header_x_forwarded_client_cert. Action to take on the HTTP x-forwarded-client-cert header ...
                choices:
                    - 'pass'
                    - 'add'
                    - 'remove'
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
    - name: Configure web proxy profiles.
      fortinet.fortimanager.fmgr_webproxy_profile:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: present # <value in [present, absent]>
        webproxy_profile:
          header_client_ip: <value in [pass, add, remove]>
          header_front_end_https: <value in [pass, add, remove]>
          header_via_request: <value in [pass, add, remove]>
          header_via_response: <value in [pass, add, remove]>
          header_x_authenticated_groups: <value in [pass, add, remove]>
          header_x_authenticated_user: <value in [pass, add, remove]>
          header_x_forwarded_for: <value in [pass, add, remove]>
          headers:
            -
              action: <value in [add-to-request, add-to-response, remove-from-request, ...]>
              content: <string>
              id: <integer>
              name: <string>
              add_option: <value in [append, new-on-not-found, new]>
              base64_encoding: <value in [disable, enable]>
              dstaddr: <list or string>
              dstaddr6: <list or string>
              protocol:
                - https
                - http
          log_header_change: <value in [disable, enable]>
          name: <string>
          strip_encoding: <value in [disable, enable]>
          header_x_forwarded_client_cert: <value in [pass, add, remove]>
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
        '/pm/config/adom/{adom}/obj/web-proxy/profile',
        '/pm/config/global/obj/web-proxy/profile'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/web-proxy/profile/{profile}',
        '/pm/config/global/obj/web-proxy/profile/{profile}'
    ]

    url_params = ['adom']
    module_primary_key = 'name'
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'webproxy_profile': {
            'type': 'dict',
            'v_range': [['6.0.0', '']],
            'options': {
                'header-client-ip': {'choices': ['pass', 'add', 'remove'], 'type': 'str'},
                'header-front-end-https': {'choices': ['pass', 'add', 'remove'], 'type': 'str'},
                'header-via-request': {'choices': ['pass', 'add', 'remove'], 'type': 'str'},
                'header-via-response': {'choices': ['pass', 'add', 'remove'], 'type': 'str'},
                'header-x-authenticated-groups': {'choices': ['pass', 'add', 'remove'], 'type': 'str'},
                'header-x-authenticated-user': {'choices': ['pass', 'add', 'remove'], 'type': 'str'},
                'header-x-forwarded-for': {'choices': ['pass', 'add', 'remove'], 'type': 'str'},
                'headers': {
                    'type': 'list',
                    'options': {
                        'action': {
                            'choices': [
                                'add-to-request', 'add-to-response', 'remove-from-request', 'remove-from-response', 'monitor-request',
                                'monitor-response'
                            ],
                            'type': 'str'
                        },
                        'content': {'type': 'str'},
                        'id': {'type': 'int'},
                        'name': {'type': 'str'},
                        'add-option': {'v_range': [['6.2.0', '']], 'choices': ['append', 'new-on-not-found', 'new'], 'type': 'str'},
                        'base64-encoding': {'v_range': [['6.2.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'dstaddr': {'v_range': [['6.2.0', '']], 'type': 'raw'},
                        'dstaddr6': {'v_range': [['6.2.0', '']], 'type': 'raw'},
                        'protocol': {'v_range': [['6.2.0', '']], 'type': 'list', 'choices': ['https', 'http'], 'elements': 'str'}
                    },
                    'elements': 'dict'
                },
                'log-header-change': {'choices': ['disable', 'enable'], 'type': 'str'},
                'name': {'required': True, 'type': 'str'},
                'strip-encoding': {'choices': ['disable', 'enable'], 'type': 'str'},
                'header-x-forwarded-client-cert': {'v_range': [['7.0.1', '']], 'choices': ['pass', 'add', 'remove'], 'type': 'str'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('full crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'webproxy_profile'),
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
