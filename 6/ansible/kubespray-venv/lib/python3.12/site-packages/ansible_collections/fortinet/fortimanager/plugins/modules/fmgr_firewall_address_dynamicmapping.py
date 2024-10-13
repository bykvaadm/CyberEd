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
module: fmgr_firewall_address_dynamicmapping
short_description: Configure IPv4 addresses.
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
    address:
        description: The parameter (address) in requested url.
        type: str
        required: true
    firewall_address_dynamicmapping:
        description: The top level parameters set.
        required: false
        type: dict
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
            allow-routing:
                type: str
                description: Deprecated, please rename it to allow_routing. Allow routing.
                choices:
                    - 'disable'
                    - 'enable'
            associated-interface:
                type: str
                description: Deprecated, please rename it to associated_interface. Associated interface.
            cache-ttl:
                type: int
                description: Deprecated, please rename it to cache_ttl. Cache ttl.
            color:
                type: int
                description: Color.
            comment:
                type: raw
                description: (dict or str) Comment.
            country:
                type: str
                description: Country.
            end-ip:
                type: str
                description: Deprecated, please rename it to end_ip. End ip.
            end-mac:
                type: str
                description: Deprecated, please rename it to end_mac. End mac.
            epg-name:
                type: str
                description: Deprecated, please rename it to epg_name. Epg name.
            filter:
                type: str
                description: Filter.
            fqdn:
                type: str
                description: Fqdn.
            interface:
                type: str
                description: Interface.
            obj-id:
                type: str
                description: Deprecated, please rename it to obj_id. Obj id.
            organization:
                type: str
                description: Organization.
            policy-group:
                type: str
                description: Deprecated, please rename it to policy_group. Policy group.
            sdn:
                type: str
                description: Sdn.
                choices:
                    - 'aci'
                    - 'aws'
                    - 'nsx'
                    - 'nuage'
                    - 'azure'
                    - 'gcp'
                    - 'oci'
                    - 'openstack'
            sdn-addr-type:
                type: str
                description: Deprecated, please rename it to sdn_addr_type. Sdn addr type.
                choices:
                    - 'private'
                    - 'public'
                    - 'all'
            sdn-tag:
                type: str
                description: Deprecated, please rename it to sdn_tag. Sdn tag.
            start-ip:
                type: str
                description: Deprecated, please rename it to start_ip. Start ip.
            start-mac:
                type: str
                description: Deprecated, please rename it to start_mac. Start mac.
            subnet:
                type: str
                description: Subnet.
            subnet-name:
                type: str
                description: Deprecated, please rename it to subnet_name. Subnet name.
            tags:
                type: raw
                description: (list or str) Tags.
            tenant:
                type: str
                description: Tenant.
            type:
                type: str
                description: Type.
                choices:
                    - 'ipmask'
                    - 'iprange'
                    - 'fqdn'
                    - 'wildcard'
                    - 'geography'
                    - 'url'
                    - 'wildcard-fqdn'
                    - 'nsx'
                    - 'aws'
                    - 'dynamic'
                    - 'interface-subnet'
                    - 'mac'
                    - 'fqdn-group'
                    - 'route-tag'
            url:
                type: str
                description: Url.
            uuid:
                type: str
                description: Uuid.
            visibility:
                type: str
                description: Visibility.
                choices:
                    - 'disable'
                    - 'enable'
            wildcard:
                type: str
                description: Wildcard.
            wildcard-fqdn:
                type: str
                description: Deprecated, please rename it to wildcard_fqdn. Wildcard fqdn.
            _image-base64:
                type: str
                description: Deprecated, please rename it to _image_base64. Image base64.
            clearpass-spt:
                type: str
                description: Deprecated, please rename it to clearpass_spt. Clearpass spt.
                choices:
                    - 'unknown'
                    - 'healthy'
                    - 'quarantine'
                    - 'checkup'
                    - 'transition'
                    - 'infected'
                    - 'transient'
            fsso-group:
                type: raw
                description: (list or str) Deprecated, please rename it to fsso_group. Fsso group.
            sub-type:
                type: str
                description: Deprecated, please rename it to sub_type. Sub type.
                choices:
                    - 'sdn'
                    - 'clearpass-spt'
                    - 'fsso'
                    - 'ems-tag'
                    - 'swc-tag'
                    - 'fortivoice-tag'
                    - 'fortinac-tag'
                    - 'fortipolicy-tag'
                    - 'device-identification'
            global-object:
                type: int
                description: Deprecated, please rename it to global_object. Global object.
            obj-tag:
                type: str
                description: Deprecated, please rename it to obj_tag. Obj tag.
            obj-type:
                type: str
                description: Deprecated, please rename it to obj_type. Obj type.
                choices:
                    - 'ip'
                    - 'mac'
            fabric-object:
                type: str
                description: Deprecated, please rename it to fabric_object. Security Fabric global object setting.
                choices:
                    - 'disable'
                    - 'enable'
            macaddr:
                type: raw
                description: (list) Multiple MAC address ranges.
            node-ip-only:
                type: str
                description: Deprecated, please rename it to node_ip_only. Enable/disable collection of node addresses only in Kubernetes.
                choices:
                    - 'disable'
                    - 'enable'
            dirty:
                type: str
                description: To be deleted address.
                choices:
                    - 'dirty'
                    - 'clean'
            pattern-end:
                type: int
                description: Deprecated, please rename it to pattern_end. Pattern end.
            pattern-start:
                type: int
                description: Deprecated, please rename it to pattern_start. Pattern start.
            tag-detection-level:
                type: str
                description: Deprecated, please rename it to tag_detection_level. Tag detection level of dynamic address object.
            tag-type:
                type: str
                description: Deprecated, please rename it to tag_type. Tag type of dynamic address object.
            hw-model:
                type: str
                description: Deprecated, please rename it to hw_model. Dynamic address matching hardware model.
            hw-vendor:
                type: str
                description: Deprecated, please rename it to hw_vendor. Dynamic address matching hardware vendor.
            os:
                type: str
                description: Dynamic address matching operating system.
            route-tag:
                type: int
                description: Deprecated, please rename it to route_tag. Route-tag address.
            sw-version:
                type: str
                description: Deprecated, please rename it to sw_version. Dynamic address matching software version.
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
    - name: Configure dynamic mappings of IPv4 address
      fortinet.fortimanager.fmgr_firewall_address_dynamicmapping:
        bypass_validation: true
        adom: ansible
        address: "ansible-test1" # name
        state: present
        firewall_address_dynamicmapping:
          _scope:
            - name: FGT_AWS # need a valid device name
              vdom: root # need a valid vdom name under the device
          allow-routing: disable # <value in [disable, enable]>
          cache-ttl: 0
          color: 1
          comment: "ansible-comment"
          subnet: "222.222.222.101/32"
          subnet-name: "ansible-test"
          type: ipmask # <value in [ipmask, iprange, fqdn, ...]>
          visibility: enable

- name: Gathering fortimanager facts
  hosts: fortimanagers
  gather_facts: false
  connection: httpapi
  vars:
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_httpapi_port: 443
  tasks:
    - name: Retrieve all the dynamic mappings of IPv4 address
      fortinet.fortimanager.fmgr_fact:
        facts:
          selector: "firewall_address_dynamicmapping"
          params:
            adom: "ansible"
            address: "ansible-test1" # name
            dynamic_mapping: "your_value"
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
        '/pm/config/adom/{adom}/obj/firewall/address/{address}/dynamic_mapping',
        '/pm/config/global/obj/firewall/address/{address}/dynamic_mapping'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/firewall/address/{address}/dynamic_mapping/{dynamic_mapping}',
        '/pm/config/global/obj/firewall/address/{address}/dynamic_mapping/{dynamic_mapping}'
    ]

    url_params = ['adom', 'address']
    module_primary_key = 'complex:{{module}}["_scope"][0]["name"]+"/"+{{module}}["_scope"][0]["vdom"]'
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'address': {'required': True, 'type': 'str'},
        'firewall_address_dynamicmapping': {
            'type': 'dict',
            'v_range': [['6.0.0', '']],
            'options': {
                '_scope': {'type': 'list', 'options': {'name': {'type': 'str'}, 'vdom': {'type': 'str'}}, 'elements': 'dict'},
                'allow-routing': {'choices': ['disable', 'enable'], 'type': 'str'},
                'associated-interface': {'type': 'str'},
                'cache-ttl': {'type': 'int'},
                'color': {'type': 'int'},
                'comment': {'type': 'raw'},
                'country': {'type': 'str'},
                'end-ip': {'type': 'str'},
                'end-mac': {'type': 'str'},
                'epg-name': {'type': 'str'},
                'filter': {'type': 'str'},
                'fqdn': {'type': 'str'},
                'interface': {'type': 'str'},
                'obj-id': {'type': 'str'},
                'organization': {'type': 'str'},
                'policy-group': {'type': 'str'},
                'sdn': {'choices': ['aci', 'aws', 'nsx', 'nuage', 'azure', 'gcp', 'oci', 'openstack'], 'type': 'str'},
                'sdn-addr-type': {'choices': ['private', 'public', 'all'], 'type': 'str'},
                'sdn-tag': {'type': 'str'},
                'start-ip': {'type': 'str'},
                'start-mac': {'type': 'str'},
                'subnet': {'type': 'str'},
                'subnet-name': {'type': 'str'},
                'tags': {'type': 'raw'},
                'tenant': {'type': 'str'},
                'type': {
                    'choices': [
                        'ipmask', 'iprange', 'fqdn', 'wildcard', 'geography', 'url', 'wildcard-fqdn', 'nsx', 'aws', 'dynamic', 'interface-subnet', 'mac',
                        'fqdn-group', 'route-tag'
                    ],
                    'type': 'str'
                },
                'url': {'type': 'str'},
                'uuid': {'type': 'str'},
                'visibility': {'choices': ['disable', 'enable'], 'type': 'str'},
                'wildcard': {'type': 'str'},
                'wildcard-fqdn': {'type': 'str'},
                '_image-base64': {'v_range': [['6.2.2', '']], 'type': 'str'},
                'clearpass-spt': {
                    'v_range': [['6.2.2', '']],
                    'choices': ['unknown', 'healthy', 'quarantine', 'checkup', 'transition', 'infected', 'transient'],
                    'type': 'str'
                },
                'fsso-group': {'v_range': [['6.2.2', '']], 'type': 'raw'},
                'sub-type': {
                    'v_range': [['6.2.2', '']],
                    'choices': [
                        'sdn', 'clearpass-spt', 'fsso', 'ems-tag', 'swc-tag', 'fortivoice-tag', 'fortinac-tag', 'fortipolicy-tag',
                        'device-identification'
                    ],
                    'type': 'str'
                },
                'global-object': {'v_range': [['6.4.0', '']], 'type': 'int'},
                'obj-tag': {'v_range': [['6.4.2', '']], 'type': 'str'},
                'obj-type': {'v_range': [['6.4.2', '']], 'choices': ['ip', 'mac'], 'type': 'str'},
                'fabric-object': {'v_range': [['6.4.4', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'macaddr': {'v_range': [['7.0.0', '']], 'type': 'raw'},
                'node-ip-only': {'v_range': [['7.0.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'dirty': {'v_range': [['7.0.3', '']], 'choices': ['dirty', 'clean'], 'type': 'str'},
                'pattern-end': {'v_range': [['7.0.3', '']], 'type': 'int'},
                'pattern-start': {'v_range': [['7.0.3', '']], 'type': 'int'},
                'tag-detection-level': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'tag-type': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'hw-model': {'v_range': [['7.4.0', '']], 'type': 'str'},
                'hw-vendor': {'v_range': [['7.4.0', '']], 'type': 'str'},
                'os': {'v_range': [['7.4.0', '']], 'type': 'str'},
                'route-tag': {'v_range': [['7.4.0', '']], 'type': 'int'},
                'sw-version': {'v_range': [['7.4.0', '']], 'type': 'str'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('full crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'firewall_address_dynamicmapping'),
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
