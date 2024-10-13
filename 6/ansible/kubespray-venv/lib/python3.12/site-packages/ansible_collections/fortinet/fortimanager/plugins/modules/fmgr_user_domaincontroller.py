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
module: fmgr_user_domaincontroller
short_description: Configure domain controller entries.
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
    user_domaincontroller:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            domain-name:
                type: str
                description: Deprecated, please rename it to domain_name. Domain DNS name.
            extra-server:
                type: list
                elements: dict
                description: Deprecated, please rename it to extra_server. Extra server.
                suboptions:
                    id:
                        type: int
                        description: Server ID.
                    ip-address:
                        type: str
                        description: Deprecated, please rename it to ip_address. Domain controller IP address.
                    port:
                        type: int
                        description: Port to be used for communication with the domain controller
                    source-ip-address:
                        type: str
                        description: Deprecated, please rename it to source_ip_address. FortiGate IPv4 address to be used for communication with the do...
                    source-port:
                        type: int
                        description: Deprecated, please rename it to source_port. Source port to be used for communication with the domain controller.
            ip-address:
                type: str
                description: Deprecated, please rename it to ip_address. Domain controller IP address.
            ldap-server:
                type: raw
                description: (list or str) Deprecated, please rename it to ldap_server. LDAP server name.
            name:
                type: str
                description: Domain controller entry name.
                required: true
            port:
                type: int
                description: Port to be used for communication with the domain controller
            ad-mode:
                type: str
                description: Deprecated, please rename it to ad_mode. Set Active Directory mode.
                choices:
                    - 'none'
                    - 'ds'
                    - 'lds'
            adlds-dn:
                type: str
                description: Deprecated, please rename it to adlds_dn. AD LDS distinguished name.
            adlds-ip-address:
                type: str
                description: Deprecated, please rename it to adlds_ip_address. AD LDS IPv4 address.
            adlds-ip6:
                type: str
                description: Deprecated, please rename it to adlds_ip6. AD LDS IPv6 address.
            adlds-port:
                type: int
                description: Deprecated, please rename it to adlds_port. Port number of AD LDS service
            dns-srv-lookup:
                type: str
                description: Deprecated, please rename it to dns_srv_lookup. Enable/disable DNS service lookup.
                choices:
                    - 'disable'
                    - 'enable'
            hostname:
                type: str
                description: Hostname of the server to connect to.
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
            ip6:
                type: str
                description: Domain controller IPv6 address.
            password:
                type: raw
                description: (list) Password for specified username.
            replication-port:
                type: int
                description: Deprecated, please rename it to replication_port. Port to be used for communication with the domain controller for replica...
            source-ip-address:
                type: str
                description: Deprecated, please rename it to source_ip_address. FortiGate IPv4 address to be used for communication with the domain con...
            source-ip6:
                type: str
                description: Deprecated, please rename it to source_ip6. FortiGate IPv6 address to be used for communication with the domain controller.
            source-port:
                type: int
                description: Deprecated, please rename it to source_port. Source port to be used for communication with the domain controller.
            username:
                type: str
                description: User name to sign in with.
            change-detection:
                type: str
                description: Deprecated, please rename it to change_detection. Enable/disable detection of a configuration change in the Active Directo...
                choices:
                    - 'disable'
                    - 'enable'
            change-detection-period:
                type: int
                description: Deprecated, please rename it to change_detection_period. Minutes to detect a configuration change in the Active Directory ...
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
    - name: Configure domain controller entries.
      fortinet.fortimanager.fmgr_user_domaincontroller:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: present # <value in [present, absent]>
        user_domaincontroller:
          domain_name: <string>
          extra_server:
            -
              id: <integer>
              ip_address: <string>
              port: <integer>
              source_ip_address: <string>
              source_port: <integer>
          ip_address: <string>
          ldap_server: <list or string>
          name: <string>
          port: <integer>
          ad_mode: <value in [none, ds, lds]>
          adlds_dn: <string>
          adlds_ip_address: <string>
          adlds_ip6: <string>
          adlds_port: <integer>
          dns_srv_lookup: <value in [disable, enable]>
          hostname: <string>
          interface: <string>
          interface_select_method: <value in [auto, sdwan, specify]>
          ip6: <string>
          password: <list or string>
          replication_port: <integer>
          source_ip_address: <string>
          source_ip6: <string>
          source_port: <integer>
          username: <string>
          change_detection: <value in [disable, enable]>
          change_detection_period: <integer>
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
        '/pm/config/adom/{adom}/obj/user/domain-controller',
        '/pm/config/global/obj/user/domain-controller'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/user/domain-controller/{domain-controller}',
        '/pm/config/global/obj/user/domain-controller/{domain-controller}'
    ]

    url_params = ['adom']
    module_primary_key = 'name'
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'user_domaincontroller': {
            'type': 'dict',
            'v_range': [['6.2.1', '']],
            'options': {
                'domain-name': {'v_range': [['6.2.1', '']], 'type': 'str'},
                'extra-server': {
                    'v_range': [['6.2.1', '']],
                    'type': 'list',
                    'options': {
                        'id': {'v_range': [['6.2.1', '']], 'type': 'int'},
                        'ip-address': {'v_range': [['6.2.1', '']], 'type': 'str'},
                        'port': {'v_range': [['6.2.1', '']], 'type': 'int'},
                        'source-ip-address': {'v_range': [['7.0.0', '']], 'type': 'str'},
                        'source-port': {'v_range': [['7.0.0', '']], 'type': 'int'}
                    },
                    'elements': 'dict'
                },
                'ip-address': {'v_range': [['6.2.1', '']], 'type': 'str'},
                'ldap-server': {'v_range': [['6.2.1', '']], 'type': 'raw'},
                'name': {'v_range': [['6.2.1', '']], 'required': True, 'type': 'str'},
                'port': {'v_range': [['6.2.1', '']], 'type': 'int'},
                'ad-mode': {'v_range': [['7.0.0', '']], 'choices': ['none', 'ds', 'lds'], 'type': 'str'},
                'adlds-dn': {'v_range': [['7.0.0', '']], 'type': 'str'},
                'adlds-ip-address': {'v_range': [['7.0.0', '']], 'type': 'str'},
                'adlds-ip6': {'v_range': [['7.0.0', '']], 'type': 'str'},
                'adlds-port': {'v_range': [['7.0.0', '']], 'type': 'int'},
                'dns-srv-lookup': {'v_range': [['7.0.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'hostname': {'v_range': [['7.0.0', '']], 'type': 'str'},
                'interface': {'v_range': [['7.0.0', '']], 'type': 'str'},
                'interface-select-method': {'v_range': [['7.0.0', '']], 'choices': ['auto', 'sdwan', 'specify'], 'type': 'str'},
                'ip6': {'v_range': [['7.0.0', '']], 'type': 'str'},
                'password': {'v_range': [['7.0.0', '']], 'no_log': True, 'type': 'raw'},
                'replication-port': {'v_range': [['7.0.0', '']], 'type': 'int'},
                'source-ip-address': {'v_range': [['7.0.0', '']], 'type': 'str'},
                'source-ip6': {'v_range': [['7.0.0', '']], 'type': 'str'},
                'source-port': {'v_range': [['7.0.0', '']], 'type': 'int'},
                'username': {'v_range': [['7.0.0', '']], 'type': 'str'},
                'change-detection': {'v_range': [['7.2.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'change-detection-period': {'v_range': [['7.2.3', '']], 'type': 'int'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('full crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'user_domaincontroller'),
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
