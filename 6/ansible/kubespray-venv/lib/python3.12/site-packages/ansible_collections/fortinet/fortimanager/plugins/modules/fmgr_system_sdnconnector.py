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
module: fmgr_system_sdnconnector
short_description: Configure connection to SDN Connector.
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
    system_sdnconnector:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            _local_cert:
                type: str
                description: Local cert.
            access-key:
                type: str
                description: Deprecated, please rename it to access_key. AWS access key ID.
            azure-region:
                type: str
                description: Deprecated, please rename it to azure_region. Azure server region.
                choices:
                    - 'global'
                    - 'china'
                    - 'germany'
                    - 'usgov'
                    - 'local'
            client-id:
                type: str
                description: Deprecated, please rename it to client_id. Azure client ID
            client-secret:
                type: raw
                description: (list) Deprecated, please rename it to client_secret. Azure client secret
            compartment-id:
                type: str
                description: Deprecated, please rename it to compartment_id. Compartment ID.
            external-ip:
                type: list
                elements: dict
                description: Deprecated, please rename it to external_ip. External ip.
                suboptions:
                    name:
                        type: str
                        description: External IP name.
            gcp-project:
                type: str
                description: Deprecated, please rename it to gcp_project. GCP project name.
            key-passwd:
                type: raw
                description: (list) Deprecated, please rename it to key_passwd. Private key password.
            login-endpoint:
                type: str
                description: Deprecated, please rename it to login_endpoint. Azure Stack login enpoint.
            name:
                type: str
                description: SDN connector name.
                required: true
            nic:
                type: list
                elements: dict
                description: Nic.
                suboptions:
                    ip:
                        type: list
                        elements: dict
                        description: Ip.
                        suboptions:
                            name:
                                type: str
                                description: IP configuration name.
                            public-ip:
                                type: str
                                description: Deprecated, please rename it to public_ip. Public IP name.
                            resource-group:
                                type: str
                                description: Deprecated, please rename it to resource_group. Resource group of Azure public IP.
                    name:
                        type: str
                        description: Network interface name.
            nsx-cert-fingerprint:
                type: str
                description: Deprecated, please rename it to nsx_cert_fingerprint. NSX certificate fingerprint.
            oci-cert:
                type: str
                description: Deprecated, please rename it to oci_cert. OCI certificate.
            oci-fingerprint:
                type: str
                description: Deprecated, please rename it to oci_fingerprint. Oci fingerprint.
            oci-region:
                type: str
                description: Deprecated, please rename it to oci_region. OCI server region.
                choices:
                    - 'phoenix'
                    - 'ashburn'
                    - 'frankfurt'
                    - 'london'
                    - 'toronto'
            password:
                type: raw
                description: (list) Password of the remote SDN connector as login credentials.
            private-key:
                type: str
                description: Deprecated, please rename it to private_key. Private key of GCP service account.
            region:
                type: str
                description: AWS region name.
            resource-group:
                type: str
                description: Deprecated, please rename it to resource_group. Azure resource group.
            resource-url:
                type: str
                description: Deprecated, please rename it to resource_url. Azure Stack resource URL.
            rest-interface:
                type: str
                description: Deprecated, please rename it to rest_interface. Interface name for REST service to listen on.
                choices:
                    - 'mgmt'
                    - 'sync'
            rest-password:
                type: raw
                description: (list) Deprecated, please rename it to rest_password. Password for REST service.
            rest-sport:
                type: int
                description: Deprecated, please rename it to rest_sport. REST service access port
            rest-ssl:
                type: str
                description: Deprecated, please rename it to rest_ssl. Rest ssl.
                choices:
                    - 'disable'
                    - 'enable'
            route:
                type: list
                elements: dict
                description: Route.
                suboptions:
                    name:
                        type: str
                        description: Route name.
            route-table:
                type: list
                elements: dict
                description: Deprecated, please rename it to route_table. Route table.
                suboptions:
                    name:
                        type: str
                        description: Route table name.
                    route:
                        type: list
                        elements: dict
                        description: Route.
                        suboptions:
                            name:
                                type: str
                                description: Route name.
                            next-hop:
                                type: str
                                description: Deprecated, please rename it to next_hop. Next hop address.
                    resource-group:
                        type: str
                        description: Deprecated, please rename it to resource_group. Resource group of Azure route table.
                    subscription-id:
                        type: str
                        description: Deprecated, please rename it to subscription_id. Subscription ID of Azure route table.
            secret-key:
                type: raw
                description: (list) Deprecated, please rename it to secret_key. AWS secret access key.
            server:
                type: str
                description: Server address of the remote SDN connector.
            server-port:
                type: int
                description: Deprecated, please rename it to server_port. Port number of the remote SDN connector.
            service-account:
                type: str
                description: Deprecated, please rename it to service_account. GCP service account email.
            status:
                type: str
                description: Enable/disable connection to the remote SDN connector.
                choices:
                    - 'disable'
                    - 'enable'
            subscription-id:
                type: str
                description: Deprecated, please rename it to subscription_id. Azure subscription ID.
            tenant-id:
                type: str
                description: Deprecated, please rename it to tenant_id. Tenant ID
            type:
                type: str
                description: Type of SDN connector.
                choices:
                    - 'aci'
                    - 'aws'
                    - 'nsx'
                    - 'nuage'
                    - 'azure'
                    - 'gcp'
                    - 'oci'
                    - 'openstack'
                    - 'kubernetes'
                    - 'vmware'
                    - 'acs'
                    - 'alicloud'
                    - 'sepm'
                    - 'aci-direct'
                    - 'ibm'
                    - 'nutanix'
                    - 'sap'
            update-interval:
                type: int
                description: Deprecated, please rename it to update_interval. Dynamic object update interval
            use-metadata-iam:
                type: str
                description: Deprecated, please rename it to use_metadata_iam. Enable/disable using IAM role from metadata to call API.
                choices:
                    - 'disable'
                    - 'enable'
            user-id:
                type: str
                description: Deprecated, please rename it to user_id. User ID.
            username:
                type: str
                description: Username of the remote SDN connector as login credentials.
            vmx-image-url:
                type: str
                description: Deprecated, please rename it to vmx_image_url. URL of web-hosted VMX image.
            vmx-service-name:
                type: str
                description: Deprecated, please rename it to vmx_service_name. VMX Service name.
            vpc-id:
                type: str
                description: Deprecated, please rename it to vpc_id. AWS VPC ID.
            domain:
                type: str
                description: Openstack domain.
            ha-status:
                type: str
                description: Deprecated, please rename it to ha_status. Enable/disable use for FortiGate HA service.
                choices:
                    - 'disable'
                    - 'enable'
            last-update:
                type: int
                description: Deprecated, please rename it to last_update. Last update.
            oci-region-type:
                type: str
                description: Deprecated, please rename it to oci_region_type. OCI region type.
                choices:
                    - 'commercial'
                    - 'government'
            secret-token:
                type: str
                description: Deprecated, please rename it to secret_token. Secret token of Kubernetes service account.
            updating:
                type: int
                description: Updating.
            server-ip:
                type: str
                description: Deprecated, please rename it to server_ip. IP address of the remote SDN connector.
            group-name:
                type: str
                description: Deprecated, please rename it to group_name. Group name of computers.
            api-key:
                type: raw
                description: (list) Deprecated, please rename it to api_key. IBM cloud API key or service ID API key.
            compute-generation:
                type: int
                description: Deprecated, please rename it to compute_generation. Compute generation for IBM cloud infrastructure.
            ibm-region:
                type: str
                description: Deprecated, please rename it to ibm_region. IBM cloud region name.
                choices:
                    - 'us-south'
                    - 'us-east'
                    - 'germany'
                    - 'great-britain'
                    - 'japan'
                    - 'australia'
                    - 'dallas'
                    - 'washington-dc'
                    - 'london'
                    - 'frankfurt'
                    - 'sydney'
                    - 'tokyo'
                    - 'osaka'
                    - 'toronto'
                    - 'sao-paulo'
                    - 'dallas-private'
                    - 'washington-dc-private'
                    - 'london-private'
                    - 'frankfurt-private'
                    - 'sydney-private'
                    - 'tokyo-private'
                    - 'osaka-private'
                    - 'toronto-private'
                    - 'sao-paulo-private'
            ibm-region-gen1:
                type: str
                description: Deprecated, please rename it to ibm_region_gen1. Ibm region gen1.
                choices:
                    - 'us-south'
                    - 'us-east'
                    - 'germany'
                    - 'great-britain'
                    - 'japan'
                    - 'australia'
            ibm-region-gen2:
                type: str
                description: Deprecated, please rename it to ibm_region_gen2. Ibm region gen2.
                choices:
                    - 'us-south'
                    - 'us-east'
                    - 'great-britain'
            vcenter-password:
                type: raw
                description: (list) Deprecated, please rename it to vcenter_password. VCenter server password for NSX quarantine.
            vcenter-server:
                type: str
                description: Deprecated, please rename it to vcenter_server. VCenter server address for NSX quarantine.
            vcenter-username:
                type: str
                description: Deprecated, please rename it to vcenter_username. VCenter server username for NSX quarantine.
            server-list:
                type: raw
                description: (list) Deprecated, please rename it to server_list. Server address list of the remote SDN connector.
            external-account-list:
                type: list
                elements: dict
                description: Deprecated, please rename it to external_account_list. External account list.
                suboptions:
                    region-list:
                        type: raw
                        description: (list) Deprecated, please rename it to region_list. AWS region name list.
                    role-arn:
                        type: str
                        description: Deprecated, please rename it to role_arn. AWS role ARN to assume.
                    external-id:
                        type: str
                        description: Deprecated, please rename it to external_id. AWS external ID.
            forwarding-rule:
                type: list
                elements: dict
                description: Deprecated, please rename it to forwarding_rule. Forwarding rule.
                suboptions:
                    rule-name:
                        type: str
                        description: Deprecated, please rename it to rule_name. Forwarding rule name.
                    target:
                        type: str
                        description: Target instance name.
            gcp-project-list:
                type: list
                elements: dict
                description: Deprecated, please rename it to gcp_project_list. Gcp project list.
                suboptions:
                    gcp-zone-list:
                        type: raw
                        description: (list) Deprecated, please rename it to gcp_zone_list. Configure GCP zone list.
                    id:
                        type: str
                        description: GCP project ID.
            verify-certificate:
                type: str
                description: Deprecated, please rename it to verify_certificate. Enable/disable server certificate verification.
                choices:
                    - 'disable'
                    - 'enable'
            alt-resource-ip:
                type: str
                description: Deprecated, please rename it to alt_resource_ip. Enable/disable AWS alternative resource IP.
                choices:
                    - 'disable'
                    - 'enable'
            server-ca-cert:
                type: str
                description: Deprecated, please rename it to server_ca_cert. Trust only those servers whose certificate is directly/indirectly signed b...
            server-cert:
                type: str
                description: Deprecated, please rename it to server_cert. Trust servers that contain this certificate only.
            compartment-list:
                type: list
                elements: dict
                description: Deprecated, please rename it to compartment_list. Compartment list.
                suboptions:
                    compartment-id:
                        type: str
                        description: Deprecated, please rename it to compartment_id. OCI compartment ID.
            oci-region-list:
                type: list
                elements: dict
                description: Deprecated, please rename it to oci_region_list. Oci region list.
                suboptions:
                    region:
                        type: str
                        description: OCI region.
            proxy:
                type: str
                description: SDN proxy.
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
    - name: Configure connection to SDN Connector.
      fortinet.fortimanager.fmgr_system_sdnconnector:
        bypass_validation: false
        adom: ansible
        state: present
        system_sdnconnector:
          azure-region: global # <value in [global, china, germany, ...]>
          # compartment-id: 1
          name: ansible-test-sdn
          password: fortinet
          server: ALL
          status: disable
          type: aws # <value in [aci, aws, nsx, ...]>

- name: Gathering fortimanager facts
  hosts: fortimanagers
  gather_facts: false
  connection: httpapi
  vars:
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_httpapi_port: 443
  tasks:
    - name: Retrieve all the connections to SDN Connector
      fortinet.fortimanager.fmgr_fact:
        facts:
          selector: "system_sdnconnector"
          params:
            adom: "ansible"
            sdn-connector: "your_value"
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
        '/pm/config/adom/{adom}/obj/system/sdn-connector',
        '/pm/config/global/obj/system/sdn-connector'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/system/sdn-connector/{sdn-connector}',
        '/pm/config/global/obj/system/sdn-connector/{sdn-connector}'
    ]

    url_params = ['adom']
    module_primary_key = 'name'
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'system_sdnconnector': {
            'type': 'dict',
            'v_range': [['6.0.0', '']],
            'options': {
                '_local_cert': {'type': 'str'},
                'access-key': {'no_log': True, 'type': 'str'},
                'azure-region': {'choices': ['global', 'china', 'germany', 'usgov', 'local'], 'type': 'str'},
                'client-id': {'type': 'str'},
                'client-secret': {'no_log': True, 'type': 'raw'},
                'compartment-id': {'type': 'str'},
                'external-ip': {'type': 'list', 'options': {'name': {'type': 'str'}}, 'elements': 'dict'},
                'gcp-project': {'type': 'str'},
                'key-passwd': {'no_log': True, 'type': 'raw'},
                'login-endpoint': {'type': 'str'},
                'name': {'required': True, 'type': 'str'},
                'nic': {
                    'type': 'list',
                    'options': {
                        'ip': {
                            'type': 'list',
                            'options': {
                                'name': {'type': 'str'},
                                'public-ip': {'type': 'str'},
                                'resource-group': {'v_range': [['6.2.3', '']], 'type': 'str'}
                            },
                            'elements': 'dict'
                        },
                        'name': {'type': 'str'}
                    },
                    'elements': 'dict'
                },
                'nsx-cert-fingerprint': {'type': 'str'},
                'oci-cert': {'type': 'str'},
                'oci-fingerprint': {'type': 'str'},
                'oci-region': {'choices': ['phoenix', 'ashburn', 'frankfurt', 'london', 'toronto'], 'type': 'str'},
                'password': {'no_log': True, 'type': 'raw'},
                'private-key': {'no_log': True, 'type': 'str'},
                'region': {'type': 'str'},
                'resource-group': {'type': 'str'},
                'resource-url': {'type': 'str'},
                'rest-interface': {'choices': ['mgmt', 'sync'], 'type': 'str'},
                'rest-password': {'no_log': True, 'type': 'raw'},
                'rest-sport': {'type': 'int'},
                'rest-ssl': {'choices': ['disable', 'enable'], 'type': 'str'},
                'route': {'type': 'list', 'options': {'name': {'type': 'str'}}, 'elements': 'dict'},
                'route-table': {
                    'type': 'list',
                    'options': {
                        'name': {'type': 'str'},
                        'route': {'type': 'list', 'options': {'name': {'type': 'str'}, 'next-hop': {'type': 'str'}}, 'elements': 'dict'},
                        'resource-group': {'v_range': [['6.2.3', '']], 'type': 'str'},
                        'subscription-id': {'v_range': [['6.2.6', '6.2.12'], ['6.4.1', '']], 'type': 'str'}
                    },
                    'elements': 'dict'
                },
                'secret-key': {'no_log': True, 'type': 'raw'},
                'server': {'type': 'str'},
                'server-port': {'type': 'int'},
                'service-account': {'type': 'str'},
                'status': {'choices': ['disable', 'enable'], 'type': 'str'},
                'subscription-id': {'type': 'str'},
                'tenant-id': {'type': 'str'},
                'type': {
                    'choices': [
                        'aci', 'aws', 'nsx', 'nuage', 'azure', 'gcp', 'oci', 'openstack', 'kubernetes', 'vmware', 'acs', 'alicloud', 'sepm',
                        'aci-direct', 'ibm', 'nutanix', 'sap'
                    ],
                    'type': 'str'
                },
                'update-interval': {'type': 'int'},
                'use-metadata-iam': {'choices': ['disable', 'enable'], 'type': 'str'},
                'user-id': {'type': 'str'},
                'username': {'type': 'str'},
                'vmx-image-url': {'type': 'str'},
                'vmx-service-name': {'type': 'str'},
                'vpc-id': {'type': 'str'},
                'domain': {'v_range': [['6.2.0', '']], 'type': 'str'},
                'ha-status': {'v_range': [['6.2.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'last-update': {'v_range': [['6.2.1', '7.2.0']], 'type': 'int'},
                'oci-region-type': {'v_range': [['6.2.1', '']], 'choices': ['commercial', 'government'], 'type': 'str'},
                'secret-token': {'v_range': [['6.2.0', '']], 'no_log': True, 'type': 'str'},
                'updating': {'v_range': [['6.2.1', '7.2.0']], 'type': 'int'},
                'server-ip': {'v_range': [['6.2.0', '6.4.14']], 'type': 'str'},
                'group-name': {'v_range': [['6.2.2', '']], 'type': 'str'},
                'api-key': {'v_range': [['6.4.1', '']], 'no_log': True, 'type': 'raw'},
                'compute-generation': {'v_range': [['6.4.1', '']], 'type': 'int'},
                'ibm-region': {
                    'v_range': [['6.4.2', '']],
                    'choices': [
                        'us-south', 'us-east', 'germany', 'great-britain', 'japan', 'australia', 'dallas', 'washington-dc', 'london', 'frankfurt',
                        'sydney', 'tokyo', 'osaka', 'toronto', 'sao-paulo', 'dallas-private', 'washington-dc-private', 'london-private',
                        'frankfurt-private', 'sydney-private', 'tokyo-private', 'osaka-private', 'toronto-private', 'sao-paulo-private'
                    ],
                    'type': 'str'
                },
                'ibm-region-gen1': {
                    'v_range': [['6.4.1', '']],
                    'choices': ['us-south', 'us-east', 'germany', 'great-britain', 'japan', 'australia'],
                    'type': 'str'
                },
                'ibm-region-gen2': {'v_range': [['6.4.1', '']], 'choices': ['us-south', 'us-east', 'great-britain'], 'type': 'str'},
                'vcenter-password': {'v_range': [['6.4.1', '']], 'no_log': True, 'type': 'raw'},
                'vcenter-server': {'v_range': [['6.4.1', '']], 'type': 'str'},
                'vcenter-username': {'v_range': [['6.4.1', '']], 'type': 'str'},
                'server-list': {'v_range': [['6.4.4', '']], 'type': 'raw'},
                'external-account-list': {
                    'v_range': [['7.0.3', '']],
                    'type': 'list',
                    'options': {
                        'region-list': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                        'role-arn': {'v_range': [['7.0.3', '']], 'type': 'str'},
                        'external-id': {'v_range': [['7.0.5', '7.0.12'], ['7.2.1', '']], 'type': 'str'}
                    },
                    'elements': 'dict'
                },
                'forwarding-rule': {
                    'v_range': [['7.0.2', '']],
                    'type': 'list',
                    'options': {'rule-name': {'v_range': [['7.0.2', '']], 'type': 'str'}, 'target': {'v_range': [['7.0.2', '']], 'type': 'str'}},
                    'elements': 'dict'
                },
                'gcp-project-list': {
                    'v_range': [['6.4.7', '6.4.14'], ['7.0.2', '']],
                    'type': 'list',
                    'options': {
                        'gcp-zone-list': {'v_range': [['6.4.7', '6.4.14'], ['7.0.2', '']], 'type': 'raw'},
                        'id': {'v_range': [['6.4.7', '6.4.14'], ['7.0.2', '']], 'type': 'str'}
                    },
                    'elements': 'dict'
                },
                'verify-certificate': {'v_range': [['6.4.8', '6.4.14'], ['7.0.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'alt-resource-ip': {'v_range': [['7.2.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'server-ca-cert': {'v_range': [['7.2.2', '']], 'type': 'str'},
                'server-cert': {'v_range': [['7.2.2', '']], 'type': 'str'},
                'compartment-list': {
                    'v_range': [['7.4.0', '']],
                    'type': 'list',
                    'options': {'compartment-id': {'v_range': [['7.4.0', '']], 'type': 'str'}},
                    'elements': 'dict'
                },
                'oci-region-list': {
                    'v_range': [['7.4.0', '']],
                    'type': 'list',
                    'options': {'region': {'v_range': [['7.4.0', '']], 'type': 'str'}},
                    'elements': 'dict'
                },
                'proxy': {'v_range': [['7.4.0', '']], 'type': 'str'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('full crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'system_sdnconnector'),
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
