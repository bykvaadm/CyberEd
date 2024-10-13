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
module: fmgr_endpointcontrol_fctems
short_description: Configure FortiClient Enterprise Management Server
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
    endpointcontrol_fctems:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            call-timeout:
                type: int
                description: Deprecated, please rename it to call_timeout. FortiClient EMS call timeout in seconds
            capabilities:
                type: list
                elements: str
                description: List of EMS capabilities.
                choices:
                    - 'fabric-auth'
                    - 'silent-approval'
                    - 'websocket'
                    - 'websocket-malware'
                    - 'push-ca-certs'
                    - 'common-tags-api'
                    - 'tenant-id'
                    - 'single-vdom-connector'
                    - 'client-avatars'
                    - 'fgt-sysinfo-api'
                    - 'ztna-server-info'
            certificate-fingerprint:
                type: str
                description: Deprecated, please rename it to certificate_fingerprint. EMS certificate fingerprint.
            cloud-server-type:
                type: str
                description: Deprecated, please rename it to cloud_server_type. Cloud server type.
                choices:
                    - 'production'
                    - 'alpha'
                    - 'beta'
            fortinetone-cloud-authentication:
                type: str
                description: Deprecated, please rename it to fortinetone_cloud_authentication. Enable/disable authentication of FortiClient EMS Cloud t...
                choices:
                    - 'disable'
                    - 'enable'
            https-port:
                type: int
                description: Deprecated, please rename it to https_port. FortiClient EMS HTTPS access port number.
            name:
                type: str
                description: FortiClient Enterprise Management Server
                required: true
            out-of-sync-threshold:
                type: int
                description: Deprecated, please rename it to out_of_sync_threshold. Outdated resource threshold in seconds
            preserve-ssl-session:
                type: str
                description: Deprecated, please rename it to preserve_ssl_session. Enable/disable preservation of EMS SSL session connection.
                choices:
                    - 'disable'
                    - 'enable'
            pull-avatars:
                type: str
                description: Deprecated, please rename it to pull_avatars. Enable/disable pulling avatars from EMS.
                choices:
                    - 'disable'
                    - 'enable'
            pull-malware-hash:
                type: str
                description: Deprecated, please rename it to pull_malware_hash. Enable/disable pulling FortiClient malware hash from EMS.
                choices:
                    - 'disable'
                    - 'enable'
            pull-sysinfo:
                type: str
                description: Deprecated, please rename it to pull_sysinfo. Enable/disable pulling SysInfo from EMS.
                choices:
                    - 'disable'
                    - 'enable'
            pull-tags:
                type: str
                description: Deprecated, please rename it to pull_tags. Enable/disable pulling FortiClient user tags from EMS.
                choices:
                    - 'disable'
                    - 'enable'
            pull-vulnerabilities:
                type: str
                description: Deprecated, please rename it to pull_vulnerabilities. Enable/disable pulling vulnerabilities from EMS.
                choices:
                    - 'disable'
                    - 'enable'
            server:
                type: str
                description: FortiClient EMS FQDN or IPv4 address.
            source-ip:
                type: str
                description: Deprecated, please rename it to source_ip. REST API call source IP.
            websocket-override:
                type: str
                description: Deprecated, please rename it to websocket_override. Enable/disable override behavior for how this FortiGate unit connects ...
                choices:
                    - 'disable'
                    - 'enable'
            status-check-interval:
                type: int
                description: Deprecated, please rename it to status_check_interval. FortiClient EMS call timeout in seconds
            certificate:
                type: str
                description: FortiClient EMS certificate.
            admin-username:
                type: str
                description: Deprecated, please rename it to admin_username. FortiClient EMS admin username.
            serial-number:
                type: str
                description: Deprecated, please rename it to serial_number. FortiClient EMS Serial Number.
            admin-password:
                type: raw
                description: (list) Deprecated, please rename it to admin_password. FortiClient EMS admin password.
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
            dirty-reason:
                type: str
                description: Deprecated, please rename it to dirty_reason. Dirty Reason for FortiClient EMS.
                choices:
                    - 'none'
                    - 'mismatched-ems-sn'
            ems-id:
                type: int
                description: Deprecated, please rename it to ems_id. EMS ID in order
            status:
                type: str
                description: Enable or disable this EMS configuration.
                choices:
                    - 'disable'
                    - 'enable'
            ca-cn-info:
                type: str
                description: Deprecated, please rename it to ca_cn_info. Ca cn info.
            trust-ca-cn:
                type: str
                description: Deprecated, please rename it to trust_ca_cn. Trust ca cn.
                choices:
                    - 'disable'
                    - 'enable'
            tenant-id:
                type: str
                description: Deprecated, please rename it to tenant_id. EMS Tenant ID.
            send-tags-to-all-vdoms:
                type: str
                description: Deprecated, please rename it to send_tags_to_all_vdoms. Relax restrictions on tags to send all EMS tags to all VDOMs
                choices:
                    - 'disable'
                    - 'enable'
            verified-cn:
                type: str
                description: Deprecated, please rename it to verified_cn. EMS certificate CN.
            verifying-ca:
                type: str
                description: Deprecated, please rename it to verifying_ca. Lowest CA cert on Fortigate in verified EMS cert chain.
            cloud-authentication-access-key:
                type: str
                description: Deprecated, please rename it to cloud_authentication_access_key. FortiClient EMS Cloud multitenancy access key
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
    - name: Configure FortiClient Enterprise Management Server
      fortinet.fortimanager.fmgr_endpointcontrol_fctems:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: present # <value in [present, absent]>
        endpointcontrol_fctems:
          call_timeout: <integer>
          capabilities:
            - fabric-auth
            - silent-approval
            - websocket
            - websocket-malware
            - push-ca-certs
            - common-tags-api
            - tenant-id
            - single-vdom-connector
            - client-avatars
            - fgt-sysinfo-api
            - ztna-server-info
          certificate_fingerprint: <string>
          cloud_server_type: <value in [production, alpha, beta]>
          fortinetone_cloud_authentication: <value in [disable, enable]>
          https_port: <integer>
          name: <string>
          out_of_sync_threshold: <integer>
          preserve_ssl_session: <value in [disable, enable]>
          pull_avatars: <value in [disable, enable]>
          pull_malware_hash: <value in [disable, enable]>
          pull_sysinfo: <value in [disable, enable]>
          pull_tags: <value in [disable, enable]>
          pull_vulnerabilities: <value in [disable, enable]>
          server: <string>
          source_ip: <string>
          websocket_override: <value in [disable, enable]>
          status_check_interval: <integer>
          certificate: <string>
          admin_username: <string>
          serial_number: <string>
          admin_password: <list or string>
          interface: <string>
          interface_select_method: <value in [auto, sdwan, specify]>
          dirty_reason: <value in [none, mismatched-ems-sn]>
          ems_id: <integer>
          status: <value in [disable, enable]>
          ca_cn_info: <string>
          trust_ca_cn: <value in [disable, enable]>
          tenant_id: <string>
          send_tags_to_all_vdoms: <value in [disable, enable]>
          verified_cn: <string>
          verifying_ca: <string>
          cloud_authentication_access_key: <string>
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
        '/pm/config/adom/{adom}/obj/endpoint-control/fctems',
        '/pm/config/global/obj/endpoint-control/fctems'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/endpoint-control/fctems/{fctems}',
        '/pm/config/global/obj/endpoint-control/fctems/{fctems}'
    ]

    url_params = ['adom']
    module_primary_key = 'name'
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'endpointcontrol_fctems': {
            'type': 'dict',
            'v_range': [['7.0.2', '']],
            'options': {
                'call-timeout': {'v_range': [['7.0.2', '']], 'type': 'int'},
                'capabilities': {
                    'v_range': [['7.0.2', '']],
                    'type': 'list',
                    'choices': [
                        'fabric-auth', 'silent-approval', 'websocket', 'websocket-malware', 'push-ca-certs', 'common-tags-api', 'tenant-id',
                        'single-vdom-connector', 'client-avatars', 'fgt-sysinfo-api', 'ztna-server-info'
                    ],
                    'elements': 'str'
                },
                'certificate-fingerprint': {'v_range': [['7.0.2', '']], 'type': 'str'},
                'cloud-server-type': {'v_range': [['7.0.2', '']], 'choices': ['production', 'alpha', 'beta'], 'type': 'str'},
                'fortinetone-cloud-authentication': {'v_range': [['7.0.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'https-port': {'v_range': [['7.0.2', '']], 'type': 'int'},
                'name': {'v_range': [['7.0.2', '']], 'required': True, 'type': 'str'},
                'out-of-sync-threshold': {'v_range': [['7.0.5', '']], 'type': 'int'},
                'preserve-ssl-session': {'v_range': [['7.0.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'pull-avatars': {'v_range': [['7.0.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'pull-malware-hash': {'v_range': [['7.0.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'pull-sysinfo': {'v_range': [['7.0.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'pull-tags': {'v_range': [['7.0.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'pull-vulnerabilities': {'v_range': [['7.0.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'server': {'v_range': [['7.0.2', '']], 'type': 'str'},
                'source-ip': {'v_range': [['7.0.2', '']], 'type': 'str'},
                'websocket-override': {'v_range': [['7.0.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'status-check-interval': {'v_range': [['7.0.2', '']], 'type': 'int'},
                'certificate': {'v_range': [['7.0.2', '']], 'type': 'str'},
                'admin-username': {'v_range': [['7.0.2', '']], 'type': 'str'},
                'serial-number': {'v_range': [['7.0.2', '']], 'type': 'str'},
                'admin-password': {'v_range': [['7.0.2', '']], 'no_log': True, 'type': 'raw'},
                'interface': {'v_range': [['7.0.4', '7.0.12'], ['7.2.1', '']], 'type': 'str'},
                'interface-select-method': {'v_range': [['7.0.4', '7.0.12'], ['7.2.1', '']], 'choices': ['auto', 'sdwan', 'specify'], 'type': 'str'},
                'dirty-reason': {'v_range': [['7.0.5', '7.0.12'], ['7.2.1', '']], 'choices': ['none', 'mismatched-ems-sn'], 'type': 'str'},
                'ems-id': {'v_range': [['7.0.5', '7.0.12'], ['7.2.1', '']], 'type': 'int'},
                'status': {'v_range': [['7.0.5', '7.0.12'], ['7.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ca-cn-info': {'v_range': [['7.0.6', '7.0.12'], ['7.2.2', '']], 'type': 'str'},
                'trust-ca-cn': {'v_range': [['7.0.6', '7.0.12'], ['7.2.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'tenant-id': {'v_range': [['7.2.1', '']], 'type': 'str'},
                'send-tags-to-all-vdoms': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'verified-cn': {'v_range': [['7.4.2', '']], 'type': 'str'},
                'verifying-ca': {'v_range': [['7.4.2', '']], 'type': 'str'},
                'cloud-authentication-access-key': {'v_range': [['7.4.3', '']], 'no_log': True, 'type': 'str'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('full crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'endpointcontrol_fctems'),
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
