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
module: fmgr_casb_useractivity
short_description: Configure CASB user activity.
description:
    - This module is able to configure a FortiManager device.
    - Examples include all parameters and values which need to be adjusted to data sources before usage.

version_added: "2.3.0"
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
    casb_useractivity:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            application:
                type: str
                description: CASB SaaS application name.
            casb-name:
                type: str
                description: Deprecated, please rename it to casb_name. CASB user activity signature name.
            category:
                type: str
                description: CASB user activity category.
                choices:
                    - 'activity-control'
                    - 'tenant-control'
                    - 'domain-control'
                    - 'safe-search-control'
                    - 'other'
            control-options:
                type: list
                elements: dict
                description: Deprecated, please rename it to control_options. Control options.
                suboptions:
                    name:
                        type: str
                        description: CASB control option name.
                    operations:
                        type: list
                        elements: dict
                        description: Operations.
                        suboptions:
                            action:
                                type: str
                                description: CASB operation action.
                                choices:
                                    - 'append'
                                    - 'prepend'
                                    - 'replace'
                                    - 'new'
                                    - 'new-on-not-found'
                                    - 'delete'
                            case-sensitive:
                                type: str
                                description: Deprecated, please rename it to case_sensitive. CASB operation search case sensitive.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            direction:
                                type: str
                                description: CASB operation direction.
                                choices:
                                    - 'request'
                            header-name:
                                type: str
                                description: Deprecated, please rename it to header_name. CASB operation header name to search.
                            name:
                                type: str
                                description: CASB control option operation name.
                            search-key:
                                type: str
                                description: Deprecated, please rename it to search_key. CASB operation key to search.
                            search-pattern:
                                type: str
                                description: Deprecated, please rename it to search_pattern. CASB operation search pattern.
                                choices:
                                    - 'simple'
                                    - 'substr'
                                    - 'regexp'
                            target:
                                type: str
                                description: CASB operation target.
                                choices:
                                    - 'header'
                                    - 'path'
                            value-from-input:
                                type: str
                                description: Deprecated, please rename it to value_from_input. Enable/disable value from user input.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            values:
                                type: list
                                elements: str
                                description: CASB operation new values.
                    status:
                        type: str
                        description: CASB control option status.
                        choices:
                            - 'disable'
                            - 'enable'
            description:
                type: str
                description: CASB user activity description.
            match:
                type: list
                elements: dict
                description: Match.
                suboptions:
                    id:
                        type: int
                        description: CASB user activity match rules ID.
                    rules:
                        type: list
                        elements: dict
                        description: Rules.
                        suboptions:
                            case-sensitive:
                                type: str
                                description: Deprecated, please rename it to case_sensitive. CASB user activity match case sensitive.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            domains:
                                type: list
                                elements: str
                                description: CASB user activity domain list.
                            header-name:
                                type: str
                                description: Deprecated, please rename it to header_name. CASB user activity rule header name.
                            id:
                                type: int
                                description: CASB user activity rule ID.
                            match-pattern:
                                type: str
                                description: Deprecated, please rename it to match_pattern. CASB user activity rule match pattern.
                                choices:
                                    - 'simple'
                                    - 'substr'
                                    - 'regexp'
                            match-value:
                                type: str
                                description: Deprecated, please rename it to match_value. CASB user activity rule match value.
                            methods:
                                type: list
                                elements: str
                                description: CASB user activity method list.
                            negate:
                                type: str
                                description: Enable/disable what the matching strategy must not be.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            type:
                                type: str
                                description: CASB user activity rule type.
                                choices:
                                    - 'domains'
                                    - 'host'
                                    - 'path'
                                    - 'header'
                                    - 'header-value'
                                    - 'method'
                    strategy:
                        type: str
                        description: CASB user activity rules strategy.
                        choices:
                            - 'or'
                            - 'and'
            match-strategy:
                type: str
                description: Deprecated, please rename it to match_strategy. CASB user activity match strategy.
                choices:
                    - 'or'
                    - 'and'
            name:
                type: str
                description: CASB user activity name.
                required: true
            type:
                type: str
                description: CASB user activity type.
                choices:
                    - 'built-in'
                    - 'customized'
            uuid:
                type: str
                description: Universally Unique Identifier
            status:
                type: str
                description: CASB user activity status.
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
    - name: Configure CASB user activity.
      fortinet.fortimanager.fmgr_casb_useractivity:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: present # <value in [present, absent]>
        casb_useractivity:
          application: <string>
          casb_name: <string>
          category: <value in [activity-control, tenant-control, domain-control, ...]>
          control_options:
            -
              name: <string>
              operations:
                -
                  action: <value in [append, prepend, replace, ...]>
                  case_sensitive: <value in [disable, enable]>
                  direction: <value in [request]>
                  header_name: <string>
                  name: <string>
                  search_key: <string>
                  search_pattern: <value in [simple, substr, regexp]>
                  target: <value in [header, path]>
                  value_from_input: <value in [disable, enable]>
                  values: <list or string>
              status: <value in [disable, enable]>
          description: <string>
          match:
            -
              id: <integer>
              rules:
                -
                  case_sensitive: <value in [disable, enable]>
                  domains: <list or string>
                  header_name: <string>
                  id: <integer>
                  match_pattern: <value in [simple, substr, regexp]>
                  match_value: <string>
                  methods: <list or string>
                  negate: <value in [disable, enable]>
                  type: <value in [domains, host, path, ...]>
              strategy: <value in [or, and]>
          match_strategy: <value in [or, and]>
          name: <string>
          type: <value in [built-in, customized]>
          uuid: <string>
          status: <value in [disable, enable]>
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
        '/pm/config/adom/{adom}/obj/casb/user-activity',
        '/pm/config/global/obj/casb/user-activity'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/casb/user-activity/{user-activity}',
        '/pm/config/global/obj/casb/user-activity/{user-activity}'
    ]

    url_params = ['adom']
    module_primary_key = 'name'
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'casb_useractivity': {
            'type': 'dict',
            'v_range': [['7.4.1', '']],
            'options': {
                'application': {'v_range': [['7.4.1', '']], 'type': 'str'},
                'casb-name': {'v_range': [['7.4.1', '']], 'type': 'str'},
                'category': {
                    'v_range': [['7.4.1', '']],
                    'choices': ['activity-control', 'tenant-control', 'domain-control', 'safe-search-control', 'other'],
                    'type': 'str'
                },
                'control-options': {
                    'v_range': [['7.4.1', '']],
                    'type': 'list',
                    'options': {
                        'name': {'v_range': [['7.4.1', '']], 'type': 'str'},
                        'operations': {
                            'v_range': [['7.4.1', '']],
                            'type': 'list',
                            'options': {
                                'action': {
                                    'v_range': [['7.4.1', '']],
                                    'choices': ['append', 'prepend', 'replace', 'new', 'new-on-not-found', 'delete'],
                                    'type': 'str'
                                },
                                'case-sensitive': {'v_range': [['7.4.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'direction': {'v_range': [['7.4.1', '']], 'choices': ['request'], 'type': 'str'},
                                'header-name': {'v_range': [['7.4.1', '']], 'type': 'str'},
                                'name': {'v_range': [['7.4.1', '']], 'type': 'str'},
                                'search-key': {'v_range': [['7.4.1', '']], 'no_log': True, 'type': 'str'},
                                'search-pattern': {'v_range': [['7.4.1', '']], 'choices': ['simple', 'substr', 'regexp'], 'type': 'str'},
                                'target': {'v_range': [['7.4.1', '']], 'choices': ['header', 'path'], 'type': 'str'},
                                'value-from-input': {'v_range': [['7.4.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'values': {'v_range': [['7.4.1', '']], 'type': 'list', 'elements': 'str'}
                            },
                            'elements': 'dict'
                        },
                        'status': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'}
                    },
                    'elements': 'dict'
                },
                'description': {'v_range': [['7.4.1', '']], 'type': 'str'},
                'match': {
                    'v_range': [['7.4.1', '']],
                    'type': 'list',
                    'options': {
                        'id': {'v_range': [['7.4.1', '']], 'type': 'int'},
                        'rules': {
                            'v_range': [['7.4.1', '']],
                            'type': 'list',
                            'options': {
                                'case-sensitive': {'v_range': [['7.4.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'domains': {'v_range': [['7.4.1', '']], 'type': 'list', 'elements': 'str'},
                                'header-name': {'v_range': [['7.4.1', '']], 'type': 'str'},
                                'id': {'v_range': [['7.4.1', '']], 'type': 'int'},
                                'match-pattern': {'v_range': [['7.4.1', '']], 'choices': ['simple', 'substr', 'regexp'], 'type': 'str'},
                                'match-value': {'v_range': [['7.4.1', '']], 'type': 'str'},
                                'methods': {'v_range': [['7.4.1', '']], 'type': 'list', 'elements': 'str'},
                                'negate': {'v_range': [['7.4.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'type': {
                                    'v_range': [['7.4.1', '']],
                                    'choices': ['domains', 'host', 'path', 'header', 'header-value', 'method'],
                                    'type': 'str'
                                }
                            },
                            'elements': 'dict'
                        },
                        'strategy': {'v_range': [['7.4.1', '']], 'choices': ['or', 'and'], 'type': 'str'}
                    },
                    'elements': 'dict'
                },
                'match-strategy': {'v_range': [['7.4.1', '']], 'choices': ['or', 'and'], 'type': 'str'},
                'name': {'v_range': [['7.4.1', '']], 'required': True, 'type': 'str'},
                'type': {'v_range': [['7.4.1', '']], 'choices': ['built-in', 'customized'], 'type': 'str'},
                'uuid': {'v_range': [['7.4.1', '']], 'type': 'str'},
                'status': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('full crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'casb_useractivity'),
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
