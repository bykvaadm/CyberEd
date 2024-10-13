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
module: fmgr_user_ldap
short_description: Configure LDAP server entries.
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
    user_ldap:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            account-key-filter:
                type: str
                description: Deprecated, please rename it to account_key_filter. Account key filter, using the UPN as the search filter.
            account-key-processing:
                type: str
                description: Deprecated, please rename it to account_key_processing. Account key processing operation, either keep or strip domain stri...
                choices:
                    - 'same'
                    - 'strip'
            ca-cert:
                type: str
                description: Deprecated, please rename it to ca_cert. CA certificate name.
            cnid:
                type: str
                description: Common name identifier for the LDAP server.
            dn:
                type: str
                description: Distinguished name used to look up entries on the LDAP server.
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
                    account-key-filter:
                        type: str
                        description: Deprecated, please rename it to account_key_filter. Account key filter.
                    account-key-name:
                        type: str
                        description: Deprecated, please rename it to account_key_name. Account key name.
                    account-key-processing:
                        type: str
                        description: Deprecated, please rename it to account_key_processing. Account key processing.
                        choices:
                            - 'same'
                            - 'strip'
                    ca-cert:
                        type: str
                        description: Deprecated, please rename it to ca_cert. Ca cert.
                    cnid:
                        type: str
                        description: Cnid.
                    dn:
                        type: str
                        description: Dn.
                    filter:
                        type: str
                        description: Filter.
                    group:
                        type: str
                        description: Group.
                    group-filter:
                        type: str
                        description: Deprecated, please rename it to group_filter. Group filter.
                    group-member-check:
                        type: str
                        description: Deprecated, please rename it to group_member_check. Group member check.
                        choices:
                            - 'user-attr'
                            - 'group-object'
                            - 'posix-group-object'
                    group-object-filter:
                        type: str
                        description: Deprecated, please rename it to group_object_filter. Group object filter.
                    group-object-search-base:
                        type: str
                        description: Deprecated, please rename it to group_object_search_base. Group object search base.
                    group-search-base:
                        type: str
                        description: Deprecated, please rename it to group_search_base. Group search base.
                    member-attr:
                        type: str
                        description: Deprecated, please rename it to member_attr. Member attr.
                    obtain-user-info:
                        type: str
                        description: Deprecated, please rename it to obtain_user_info. Obtain user info.
                        choices:
                            - 'disable'
                            - 'enable'
                    password:
                        type: raw
                        description: (list) Password.
                    password-expiry-warning:
                        type: str
                        description: Deprecated, please rename it to password_expiry_warning. Password expiry warning.
                        choices:
                            - 'disable'
                            - 'enable'
                    password-renewal:
                        type: str
                        description: Deprecated, please rename it to password_renewal. Password renewal.
                        choices:
                            - 'disable'
                            - 'enable'
                    port:
                        type: int
                        description: Port.
                    retrieve-protection-profile:
                        type: str
                        description: Deprecated, please rename it to retrieve_protection_profile. Retrieve protection profile.
                    search-type:
                        type: list
                        elements: str
                        description: Deprecated, please rename it to search_type. Search type.
                        choices:
                            - 'nested'
                            - 'recursive'
                    secondary-server:
                        type: str
                        description: Deprecated, please rename it to secondary_server. Secondary server.
                    secure:
                        type: str
                        description: Secure.
                        choices:
                            - 'disable'
                            - 'starttls'
                            - 'ldaps'
                    server:
                        type: str
                        description: Server.
                    server-identity-check:
                        type: str
                        description: Deprecated, please rename it to server_identity_check. Server identity check.
                        choices:
                            - 'disable'
                            - 'enable'
                    source-ip:
                        type: str
                        description: Deprecated, please rename it to source_ip. Source ip.
                    ssl-min-proto-version:
                        type: str
                        description: Deprecated, please rename it to ssl_min_proto_version. Ssl min proto version.
                        choices:
                            - 'default'
                            - 'TLSv1'
                            - 'TLSv1-1'
                            - 'TLSv1-2'
                            - 'SSLv3'
                            - 'TLSv1-3'
                    tertiary-server:
                        type: str
                        description: Deprecated, please rename it to tertiary_server. Tertiary server.
                    type:
                        type: str
                        description: Type.
                        choices:
                            - 'simple'
                            - 'anonymous'
                            - 'regular'
                    user-info-exchange-server:
                        type: str
                        description: Deprecated, please rename it to user_info_exchange_server. User info exchange server.
                    username:
                        type: str
                        description: Username.
                    two-factor:
                        type: str
                        description: Deprecated, please rename it to two_factor. Two factor.
                        choices:
                            - 'disable'
                            - 'fortitoken-cloud'
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
                    two-factor-authentication:
                        type: str
                        description: Deprecated, please rename it to two_factor_authentication. Two factor authentication.
                        choices:
                            - 'fortitoken'
                            - 'email'
                            - 'sms'
                    two-factor-notification:
                        type: str
                        description: Deprecated, please rename it to two_factor_notification. Two factor notification.
                        choices:
                            - 'email'
                            - 'sms'
                    antiphish:
                        type: str
                        description: Enable/disable AntiPhishing credential backend.
                        choices:
                            - 'disable'
                            - 'enable'
                    password-attr:
                        type: str
                        description: Deprecated, please rename it to password_attr. Name of attribute to get password hash.
                    source-port:
                        type: int
                        description: Deprecated, please rename it to source_port. Source port to be used for communication with the LDAP server.
                    client-cert:
                        type: str
                        description: Deprecated, please rename it to client_cert. Client certificate name.
                    client-cert-auth:
                        type: str
                        description: Deprecated, please rename it to client_cert_auth. Enable/disable using client certificate for TLS authentication.
                        choices:
                            - 'disable'
                            - 'enable'
                    max-connections:
                        type: int
                        description: Deprecated, please rename it to max_connections. Max connections.
                    two-factor-filter:
                        type: str
                        description: Deprecated, please rename it to two_factor_filter. Filter used to synchronize users to FortiToken Cloud.
                    account-key-upn-san:
                        type: str
                        description: Deprecated, please rename it to account_key_upn_san. Define SAN in certificate for user principle name matching.
                        choices:
                            - 'othername'
                            - 'rfc822name'
                            - 'dnsname'
                    account-key-cert-field:
                        type: str
                        description: Deprecated, please rename it to account_key_cert_field. Define subject identity field in certificate for user acce...
                        choices:
                            - 'othername'
                            - 'rfc822name'
                            - 'dnsname'
                            - 'cn'
                    status-ttl:
                        type: int
                        description: Deprecated, please rename it to status_ttl. Time for which server reachability is cached so that when a server is ...
                    source-ip-interface:
                        type: raw
                        description: (list) Deprecated, please rename it to source_ip_interface. Source interface for communication with the LDAP server.
            group-filter:
                type: str
                description: Deprecated, please rename it to group_filter. Filter used for group matching.
            group-member-check:
                type: str
                description: Deprecated, please rename it to group_member_check. Group member checking methods.
                choices:
                    - 'user-attr'
                    - 'group-object'
                    - 'posix-group-object'
            group-object-filter:
                type: str
                description: Deprecated, please rename it to group_object_filter. Filter used for group searching.
            group-search-base:
                type: str
                description: Deprecated, please rename it to group_search_base. Search base used for group searching.
            member-attr:
                type: str
                description: Deprecated, please rename it to member_attr. Name of attribute from which to get group membership.
            name:
                type: str
                description: LDAP server entry name.
                required: true
            password:
                type: raw
                description: (list) Password for initial binding.
            password-expiry-warning:
                type: str
                description: Deprecated, please rename it to password_expiry_warning. Enable/disable password expiry warnings.
                choices:
                    - 'disable'
                    - 'enable'
            password-renewal:
                type: str
                description: Deprecated, please rename it to password_renewal. Enable/disable online password renewal.
                choices:
                    - 'disable'
                    - 'enable'
            port:
                type: int
                description: Port to be used for communication with the LDAP server
            secondary-server:
                type: str
                description: Deprecated, please rename it to secondary_server. Secondary LDAP server CN domain name or IP.
            secure:
                type: str
                description: Port to be used for authentication.
                choices:
                    - 'disable'
                    - 'starttls'
                    - 'ldaps'
            server:
                type: str
                description: LDAP server CN domain name or IP.
            server-identity-check:
                type: str
                description: Deprecated, please rename it to server_identity_check. Enable/disable LDAP server identity check
                choices:
                    - 'disable'
                    - 'enable'
            source-ip:
                type: str
                description: Deprecated, please rename it to source_ip. Source IP for communications to LDAP server.
            ssl-min-proto-version:
                type: str
                description: Deprecated, please rename it to ssl_min_proto_version. Minimum supported protocol version for SSL/TLS connections
                choices:
                    - 'default'
                    - 'TLSv1'
                    - 'TLSv1-1'
                    - 'TLSv1-2'
                    - 'SSLv3'
                    - 'TLSv1-3'
            tertiary-server:
                type: str
                description: Deprecated, please rename it to tertiary_server. Tertiary LDAP server CN domain name or IP.
            type:
                type: str
                description: Authentication type for LDAP searches.
                choices:
                    - 'simple'
                    - 'anonymous'
                    - 'regular'
            username:
                type: str
                description: Username
            obtain-user-info:
                type: str
                description: Deprecated, please rename it to obtain_user_info. Enable/disable obtaining of user information.
                choices:
                    - 'disable'
                    - 'enable'
            search-type:
                type: list
                elements: str
                description: Deprecated, please rename it to search_type. Search type.
                choices:
                    - 'nested'
                    - 'recursive'
            user-info-exchange-server:
                type: str
                description: Deprecated, please rename it to user_info_exchange_server. MS Exchange server from which to fetch user information.
            account-key-name:
                type: str
                description: Deprecated, please rename it to account_key_name. Account key name, using the UPN as the search filter.
            group-object-search-base:
                type: str
                description: Deprecated, please rename it to group_object_search_base. Search base used for group searching.
            two-factor:
                type: str
                description: Deprecated, please rename it to two_factor. Enable/disable two-factor authentication.
                choices:
                    - 'disable'
                    - 'fortitoken-cloud'
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
            two-factor-authentication:
                type: str
                description: Deprecated, please rename it to two_factor_authentication. Authentication method by FortiToken Cloud.
                choices:
                    - 'fortitoken'
                    - 'email'
                    - 'sms'
            two-factor-notification:
                type: str
                description: Deprecated, please rename it to two_factor_notification. Notification method for user activation by FortiToken Cloud.
                choices:
                    - 'email'
                    - 'sms'
            antiphish:
                type: str
                description: Enable/disable AntiPhishing credential backend.
                choices:
                    - 'disable'
                    - 'enable'
            password-attr:
                type: str
                description: Deprecated, please rename it to password_attr. Name of attribute to get password hash.
            source-port:
                type: int
                description: Deprecated, please rename it to source_port. Source port to be used for communication with the LDAP server.
            client-cert:
                type: str
                description: Deprecated, please rename it to client_cert. Client certificate name.
            client-cert-auth:
                type: str
                description: Deprecated, please rename it to client_cert_auth. Enable/disable using client certificate for TLS authentication.
                choices:
                    - 'disable'
                    - 'enable'
            two-factor-filter:
                type: str
                description: Deprecated, please rename it to two_factor_filter. Filter used to synchronize users to FortiToken Cloud.
            account-key-upn-san:
                type: str
                description: Deprecated, please rename it to account_key_upn_san. Define SAN in certificate for user principle name matching.
                choices:
                    - 'othername'
                    - 'rfc822name'
                    - 'dnsname'
            account-key-cert-field:
                type: str
                description: Deprecated, please rename it to account_key_cert_field. Define subject identity field in certificate for user access right...
                choices:
                    - 'othername'
                    - 'rfc822name'
                    - 'dnsname'
                    - 'cn'
            status-ttl:
                type: int
                description: Deprecated, please rename it to status_ttl. Time for which server reachability is cached so that when a server is unreacha...
            source-ip-interface:
                type: raw
                description: (list) Deprecated, please rename it to source_ip_interface. Source interface for communication with the LDAP server.
'''

EXAMPLES = '''
- name: Example playbook
  hosts: fortimanagers
  connection: httpapi
  vars:
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_httpapi_port: 443
  tasks:
    - name: Configure LDAP server entries.
      fortinet.fortimanager.fmgr_user_ldap:
        bypass_validation: false
        adom: ansible
        state: present
        user_ldap:
          dn: ansible-test
          name: ansible-test-ldap
          password: fortinet
          port: 9000
          server: ansible

- name: Gathering fortimanager facts
  hosts: fortimanagers
  gather_facts: false
  connection: httpapi
  vars:
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_httpapi_port: 443
  tasks:
    - name: Retrieve all the LDAP server entries
      fortinet.fortimanager.fmgr_fact:
        facts:
          selector: "user_ldap"
          params:
            adom: "ansible"
            ldap: "your_value"
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
        '/pm/config/adom/{adom}/obj/user/ldap',
        '/pm/config/global/obj/user/ldap'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/user/ldap/{ldap}',
        '/pm/config/global/obj/user/ldap/{ldap}'
    ]

    url_params = ['adom']
    module_primary_key = 'name'
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'user_ldap': {
            'type': 'dict',
            'v_range': [['6.0.0', '']],
            'options': {
                'account-key-filter': {'no_log': True, 'type': 'str'},
                'account-key-processing': {'choices': ['same', 'strip'], 'type': 'str'},
                'ca-cert': {'type': 'str'},
                'cnid': {'type': 'str'},
                'dn': {'type': 'str'},
                'dynamic_mapping': {
                    'type': 'list',
                    'options': {
                        '_scope': {'type': 'list', 'options': {'name': {'type': 'str'}, 'vdom': {'type': 'str'}}, 'elements': 'dict'},
                        'account-key-filter': {'no_log': True, 'type': 'str'},
                        'account-key-name': {'no_log': True, 'type': 'str'},
                        'account-key-processing': {'choices': ['same', 'strip'], 'type': 'str'},
                        'ca-cert': {'type': 'str'},
                        'cnid': {'type': 'str'},
                        'dn': {'type': 'str'},
                        'filter': {'type': 'str'},
                        'group': {'type': 'str'},
                        'group-filter': {'type': 'str'},
                        'group-member-check': {'choices': ['user-attr', 'group-object', 'posix-group-object'], 'type': 'str'},
                        'group-object-filter': {'type': 'str'},
                        'group-object-search-base': {'type': 'str'},
                        'group-search-base': {'type': 'str'},
                        'member-attr': {'type': 'str'},
                        'obtain-user-info': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'password': {'no_log': True, 'type': 'raw'},
                        'password-expiry-warning': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'password-renewal': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'port': {'type': 'int'},
                        'retrieve-protection-profile': {'type': 'str'},
                        'search-type': {'type': 'list', 'choices': ['nested', 'recursive'], 'elements': 'str'},
                        'secondary-server': {'type': 'str'},
                        'secure': {'choices': ['disable', 'starttls', 'ldaps'], 'type': 'str'},
                        'server': {'type': 'str'},
                        'server-identity-check': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'source-ip': {'type': 'str'},
                        'ssl-min-proto-version': {'choices': ['default', 'TLSv1', 'TLSv1-1', 'TLSv1-2', 'SSLv3', 'TLSv1-3'], 'type': 'str'},
                        'tertiary-server': {'type': 'str'},
                        'type': {'choices': ['simple', 'anonymous', 'regular'], 'type': 'str'},
                        'user-info-exchange-server': {'type': 'str'},
                        'username': {'type': 'str'},
                        'two-factor': {'v_range': [['6.2.2', '']], 'choices': ['disable', 'fortitoken-cloud'], 'type': 'str'},
                        'interface': {'v_range': [['6.2.5', '6.2.12'], ['6.4.1', '']], 'type': 'str'},
                        'interface-select-method': {
                            'v_range': [['6.2.5', '6.2.12'], ['6.4.1', '']],
                            'choices': ['auto', 'sdwan', 'specify'],
                            'type': 'str'
                        },
                        'two-factor-authentication': {'v_range': [['6.2.5', '']], 'choices': ['fortitoken', 'email', 'sms'], 'type': 'str'},
                        'two-factor-notification': {'v_range': [['6.2.5', '']], 'choices': ['email', 'sms'], 'type': 'str'},
                        'antiphish': {'v_range': [['7.0.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'password-attr': {'v_range': [['7.0.0', '']], 'no_log': True, 'type': 'str'},
                        'source-port': {'v_range': [['7.0.0', '']], 'type': 'int'},
                        'client-cert': {'v_range': [['7.2.0', '']], 'type': 'str'},
                        'client-cert-auth': {'v_range': [['7.2.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'max-connections': {'v_range': [['7.0.11', '7.0.12'], ['7.2.5', '7.2.5'], ['7.4.1', '']], 'type': 'int'},
                        'two-factor-filter': {'v_range': [['7.2.1', '']], 'type': 'str'},
                        'account-key-upn-san': {'v_range': [['7.2.2', '']], 'choices': ['othername', 'rfc822name', 'dnsname'], 'type': 'str'},
                        'account-key-cert-field': {'v_range': [['7.4.1', '']], 'choices': ['othername', 'rfc822name', 'dnsname', 'cn'], 'type': 'str'},
                        'status-ttl': {'v_range': [['7.4.3', '']], 'type': 'int'},
                        'source-ip-interface': {'v_range': [['7.6.0', '']], 'type': 'raw'}
                    },
                    'elements': 'dict'
                },
                'group-filter': {'type': 'str'},
                'group-member-check': {'choices': ['user-attr', 'group-object', 'posix-group-object'], 'type': 'str'},
                'group-object-filter': {'type': 'str'},
                'group-search-base': {'type': 'str'},
                'member-attr': {'type': 'str'},
                'name': {'required': True, 'type': 'str'},
                'password': {'no_log': True, 'type': 'raw'},
                'password-expiry-warning': {'choices': ['disable', 'enable'], 'type': 'str'},
                'password-renewal': {'choices': ['disable', 'enable'], 'type': 'str'},
                'port': {'type': 'int'},
                'secondary-server': {'type': 'str'},
                'secure': {'choices': ['disable', 'starttls', 'ldaps'], 'type': 'str'},
                'server': {'type': 'str'},
                'server-identity-check': {'choices': ['disable', 'enable'], 'type': 'str'},
                'source-ip': {'type': 'str'},
                'ssl-min-proto-version': {'choices': ['default', 'TLSv1', 'TLSv1-1', 'TLSv1-2', 'SSLv3', 'TLSv1-3'], 'type': 'str'},
                'tertiary-server': {'type': 'str'},
                'type': {'choices': ['simple', 'anonymous', 'regular'], 'type': 'str'},
                'username': {'type': 'str'},
                'obtain-user-info': {'v_range': [['6.2.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'search-type': {'v_range': [['6.2.0', '']], 'type': 'list', 'choices': ['nested', 'recursive'], 'elements': 'str'},
                'user-info-exchange-server': {'v_range': [['6.2.0', '']], 'type': 'str'},
                'account-key-name': {'v_range': [['6.2.0', '6.4.14']], 'no_log': True, 'type': 'str'},
                'group-object-search-base': {'v_range': [['6.2.0', '6.2.12']], 'type': 'str'},
                'two-factor': {'v_range': [['6.2.2', '']], 'choices': ['disable', 'fortitoken-cloud'], 'type': 'str'},
                'interface': {'v_range': [['6.2.5', '6.2.12'], ['6.4.1', '']], 'type': 'str'},
                'interface-select-method': {'v_range': [['6.2.5', '6.2.12'], ['6.4.1', '']], 'choices': ['auto', 'sdwan', 'specify'], 'type': 'str'},
                'two-factor-authentication': {'v_range': [['6.2.5', '']], 'choices': ['fortitoken', 'email', 'sms'], 'type': 'str'},
                'two-factor-notification': {'v_range': [['6.2.5', '']], 'choices': ['email', 'sms'], 'type': 'str'},
                'antiphish': {'v_range': [['7.0.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'password-attr': {'v_range': [['7.0.0', '']], 'no_log': True, 'type': 'str'},
                'source-port': {'v_range': [['7.0.0', '']], 'type': 'int'},
                'client-cert': {'v_range': [['7.2.0', '']], 'type': 'str'},
                'client-cert-auth': {'v_range': [['7.2.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'two-factor-filter': {'v_range': [['7.2.1', '']], 'type': 'str'},
                'account-key-upn-san': {'v_range': [['7.2.2', '']], 'choices': ['othername', 'rfc822name', 'dnsname'], 'type': 'str'},
                'account-key-cert-field': {'v_range': [['7.4.1', '']], 'choices': ['othername', 'rfc822name', 'dnsname', 'cn'], 'type': 'str'},
                'status-ttl': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'source-ip-interface': {'v_range': [['7.6.0', '']], 'type': 'raw'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('full crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'user_ldap'),
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
