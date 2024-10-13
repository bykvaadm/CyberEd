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
module: fmgr_user_tacacs
short_description: Configure TACACS+ server entries.
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
    user_tacacs:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            authen-type:
                type: str
                description: Deprecated, please rename it to authen_type. Allowed authentication protocols/methods.
                choices:
                    - 'auto'
                    - 'ascii'
                    - 'pap'
                    - 'chap'
                    - 'mschap'
            authorization:
                type: str
                description: Enable/disable TACACS+ authorization.
                choices:
                    - 'disable'
                    - 'enable'
            dynamic_mapping:
                type: list
                elements: dict
                description: Dynamic mapping.
                suboptions:
                    _scope:
                        type: list
                        elements: dict
                        description: Scope.
                        suboptions:
                            name:
                                type: str
                                description: Name.
                            vdom:
                                type: str
                                description: Vdom.
                    authen-type:
                        type: str
                        description: Deprecated, please rename it to authen_type. Authen type.
                        choices:
                            - 'auto'
                            - 'ascii'
                            - 'pap'
                            - 'chap'
                            - 'mschap'
                    authorization:
                        type: str
                        description: Authorization.
                        choices:
                            - 'disable'
                            - 'enable'
                    key:
                        type: raw
                        description: (list) Key.
                    port:
                        type: int
                        description: Port.
                    secondary-key:
                        type: raw
                        description: (list) Deprecated, please rename it to secondary_key. Secondary key.
                    secondary-server:
                        type: str
                        description: Deprecated, please rename it to secondary_server. Secondary server.
                    server:
                        type: str
                        description: Server.
                    source-ip:
                        type: str
                        description: Deprecated, please rename it to source_ip. Source ip.
                    tertiary-key:
                        type: raw
                        description: (list) Deprecated, please rename it to tertiary_key. Tertiary key.
                    tertiary-server:
                        type: str
                        description: Deprecated, please rename it to tertiary_server. Tertiary server.
                    interface:
                        type: str
                        description: Interface.
                    interface-select-method:
                        type: str
                        description: Deprecated, please rename it to interface_select_method. Interface select method.
                        choices:
                            - 'auto'
                            - 'sdwan'
                            - 'specify'
                    status-ttl:
                        type: int
                        description: Deprecated, please rename it to status_ttl. Time for which server reachability is cached so that when a server is ...
            key:
                type: raw
                description: (list) Key to access the primary server.
            name:
                type: str
                description: TACACS+ server entry name.
                required: true
            port:
                type: int
                description: Port number of the TACACS+ server.
            secondary-key:
                type: raw
                description: (list) Deprecated, please rename it to secondary_key. Key to access the secondary server.
            secondary-server:
                type: str
                description: Deprecated, please rename it to secondary_server. Secondary TACACS+ server CN domain name or IP address.
            server:
                type: str
                description: Primary TACACS+ server CN domain name or IP address.
            source-ip:
                type: str
                description: Deprecated, please rename it to source_ip. Source IP for communications to TACACS+ server.
            tertiary-key:
                type: raw
                description: (list) Deprecated, please rename it to tertiary_key. Key to access the tertiary server.
            tertiary-server:
                type: str
                description: Deprecated, please rename it to tertiary_server. Tertiary TACACS+ server CN domain name or IP address.
            interface:
                type: str
                description: Specify outgoing interface to reach server.
            interface-select-method:
                type: str
                description: Deprecated, please rename it to interface_select_method. Specify how to select outgoing interface to reach server.
                choices:
                    - 'auto'
                    - 'sdwan'
                    - 'specify'
            status-ttl:
                type: int
                description: Deprecated, please rename it to status_ttl. Time for which server reachability is cached so that when a server is unreacha...
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
    - name: Configure TACACS+ server entries.
      fortinet.fortimanager.fmgr_user_tacacs:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: present # <value in [present, absent]>
        user_tacacs:
          authen_type: <value in [auto, ascii, pap, ...]>
          authorization: <value in [disable, enable]>
          dynamic_mapping:
            -
              _scope:
                -
                  name: <string>
                  vdom: <string>
              authen_type: <value in [auto, ascii, pap, ...]>
              authorization: <value in [disable, enable]>
              key: <list or string>
              port: <integer>
              secondary_key: <list or string>
              secondary_server: <string>
              server: <string>
              source_ip: <string>
              tertiary_key: <list or string>
              tertiary_server: <string>
              interface: <string>
              interface_select_method: <value in [auto, sdwan, specify]>
              status_ttl: <integer>
          key: <list or string>
          name: <string>
          port: <integer>
          secondary_key: <list or string>
          secondary_server: <string>
          server: <string>
          source_ip: <string>
          tertiary_key: <list or string>
          tertiary_server: <string>
          interface: <string>
          interface_select_method: <value in [auto, sdwan, specify]>
          status_ttl: <integer>
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
        '/pm/config/adom/{adom}/obj/user/tacacs+',
        '/pm/config/global/obj/user/tacacs+'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/user/tacacs+/{tacacs+}',
        '/pm/config/global/obj/user/tacacs+/{tacacs+}'
    ]

    url_params = ['adom']
    module_primary_key = 'name'
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'user_tacacs': {
            'type': 'dict',
            'v_range': [['6.0.0', '']],
            'options': {
                'authen-type': {'choices': ['auto', 'ascii', 'pap', 'chap', 'mschap'], 'type': 'str'},
                'authorization': {'choices': ['disable', 'enable'], 'type': 'str'},
                'dynamic_mapping': {
                    'type': 'list',
                    'options': {
                        '_scope': {'type': 'list', 'options': {'name': {'type': 'str'}, 'vdom': {'type': 'str'}}, 'elements': 'dict'},
                        'authen-type': {'choices': ['auto', 'ascii', 'pap', 'chap', 'mschap'], 'type': 'str'},
                        'authorization': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'key': {'no_log': True, 'type': 'raw'},
                        'port': {'type': 'int'},
                        'secondary-key': {'no_log': True, 'type': 'raw'},
                        'secondary-server': {'type': 'str'},
                        'server': {'type': 'str'},
                        'source-ip': {'type': 'str'},
                        'tertiary-key': {'no_log': True, 'type': 'raw'},
                        'tertiary-server': {'type': 'str'},
                        'interface': {'v_range': [['6.2.5', '6.2.12'], ['6.4.1', '']], 'type': 'str'},
                        'interface-select-method': {
                            'v_range': [['6.2.5', '6.2.12'], ['6.4.1', '']],
                            'choices': ['auto', 'sdwan', 'specify'],
                            'type': 'str'
                        },
                        'status-ttl': {'v_range': [['7.4.3', '']], 'type': 'int'}
                    },
                    'elements': 'dict'
                },
                'key': {'no_log': True, 'type': 'raw'},
                'name': {'required': True, 'type': 'str'},
                'port': {'type': 'int'},
                'secondary-key': {'no_log': True, 'type': 'raw'},
                'secondary-server': {'type': 'str'},
                'server': {'type': 'str'},
                'source-ip': {'type': 'str'},
                'tertiary-key': {'no_log': True, 'type': 'raw'},
                'tertiary-server': {'type': 'str'},
                'interface': {'v_range': [['6.2.5', '6.2.12'], ['6.4.1', '']], 'type': 'str'},
                'interface-select-method': {'v_range': [['6.2.5', '6.2.12'], ['6.4.1', '']], 'choices': ['auto', 'sdwan', 'specify'], 'type': 'str'},
                'status-ttl': {'v_range': [['7.4.3', '']], 'type': 'int'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('full crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'user_tacacs'),
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
