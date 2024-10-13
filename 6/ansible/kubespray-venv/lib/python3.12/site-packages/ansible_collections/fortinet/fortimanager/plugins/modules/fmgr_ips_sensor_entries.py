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
module: fmgr_ips_sensor_entries
short_description: IPS sensor filter.
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
    sensor:
        description: The parameter (sensor) in requested url.
        type: str
        required: true
    ips_sensor_entries:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            action:
                type: str
                description: Action taken with traffic in which signatures are detected.
                choices:
                    - 'pass'
                    - 'block'
                    - 'reset'
                    - 'default'
            application:
                type: raw
                description: (list) Applications to be protected.
            exempt-ip:
                type: list
                elements: dict
                description: Deprecated, please rename it to exempt_ip. Exempt ip.
                suboptions:
                    dst-ip:
                        type: str
                        description: Deprecated, please rename it to dst_ip. Destination IP address and netmask.
                    id:
                        type: int
                        description: Exempt IP ID.
                    src-ip:
                        type: str
                        description: Deprecated, please rename it to src_ip. Source IP address and netmask.
            id:
                type: int
                description: Rule ID in IPS database
                required: true
            location:
                type: raw
                description: (list) Protect client or server traffic.
            log:
                type: str
                description: Enable/disable logging of signatures included in filter.
                choices:
                    - 'disable'
                    - 'enable'
            log-attack-context:
                type: str
                description: Deprecated, please rename it to log_attack_context. Enable/disable logging of attack context
                choices:
                    - 'disable'
                    - 'enable'
            log-packet:
                type: str
                description: Deprecated, please rename it to log_packet. Enable/disable packet logging.
                choices:
                    - 'disable'
                    - 'enable'
            os:
                type: raw
                description: (list) Operating systems to be protected.
            protocol:
                type: raw
                description: (list) Protocols to be examined.
            quarantine:
                type: str
                description: Quarantine method.
                choices:
                    - 'none'
                    - 'attacker'
                    - 'both'
                    - 'interface'
            quarantine-expiry:
                type: str
                description: Deprecated, please rename it to quarantine_expiry. Duration of quarantine.
            quarantine-log:
                type: str
                description: Deprecated, please rename it to quarantine_log. Enable/disable quarantine logging.
                choices:
                    - 'disable'
                    - 'enable'
            rate-count:
                type: int
                description: Deprecated, please rename it to rate_count. Count of the rate.
            rate-duration:
                type: int
                description: Deprecated, please rename it to rate_duration. Duration
            rate-mode:
                type: str
                description: Deprecated, please rename it to rate_mode. Rate limit mode.
                choices:
                    - 'periodical'
                    - 'continuous'
            rate-track:
                type: str
                description: Deprecated, please rename it to rate_track. Track the packet protocol field.
                choices:
                    - 'none'
                    - 'src-ip'
                    - 'dest-ip'
                    - 'dhcp-client-mac'
                    - 'dns-domain'
            rule:
                type: raw
                description: (list or str) Identifies the predefined or custom IPS signatures to add to the sensor.
            severity:
                type: raw
                description: (list) Relative severity of the signature, from info to critical.
            status:
                type: str
                description: Status of the signatures included in filter.
                choices:
                    - 'disable'
                    - 'enable'
                    - 'default'
            tags:
                type: str
                description: Assign a custom tag filter to the IPS sensor.
            cve:
                type: raw
                description: (list) List of CVE IDs of the signatures to add to the sensor
            default-action:
                type: str
                description: Deprecated, please rename it to default_action. Signature default action filter.
                choices:
                    - 'block'
                    - 'pass'
                    - 'all'
                    - 'drop'
            default-status:
                type: str
                description: Deprecated, please rename it to default_status. Signature default status filter.
                choices:
                    - 'disable'
                    - 'enable'
                    - 'all'
            last-modified:
                type: raw
                description: (list or str) Deprecated, please rename it to last_modified. Filter by signature last modified date.
            vuln-type:
                type: raw
                description: (list) Deprecated, please rename it to vuln_type. List of signature vulnerability types to filter by.
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
    - name: IPS sensor filter.
      fortinet.fortimanager.fmgr_ips_sensor_entries:
        bypass_validation: false
        adom: ansible
        sensor: "ansible-test-ipssensor" # name
        state: present
        ips_sensor_entries:
          action: block # <value in [pass, block, reset, ...]>
          id: 1

- name: Gathering fortimanager facts
  hosts: fortimanagers
  gather_facts: false
  connection: httpapi
  vars:
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_httpapi_port: 443
  tasks:
    - name: Retrieve all the filters of IPS sensor
      fortinet.fortimanager.fmgr_fact:
        facts:
          selector: "ips_sensor_entries"
          params:
            adom: "ansible"
            sensor: "ansible-test-ipssensor" # name
            entries: "your_value"
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
        '/pm/config/adom/{adom}/obj/ips/sensor/{sensor}/entries',
        '/pm/config/global/obj/ips/sensor/{sensor}/entries',
        '/pm/config/adom/{adom}/obj/global/ips/sensor/{sensor}/entries',
        '/pm/config/global/obj/global/ips/sensor/{sensor}/entries'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/ips/sensor/{sensor}/entries/{entries}',
        '/pm/config/global/obj/ips/sensor/{sensor}/entries/{entries}',
        '/pm/config/adom/{adom}/obj/global/ips/sensor/{sensor}/entries/{entries}',
        '/pm/config/global/obj/global/ips/sensor/{sensor}/entries/{entries}'
    ]

    url_params = ['adom', 'sensor']
    module_primary_key = 'id'
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'sensor': {'required': True, 'type': 'str'},
        'ips_sensor_entries': {
            'type': 'dict',
            'v_range': [['6.0.0', '']],
            'options': {
                'action': {'choices': ['pass', 'block', 'reset', 'default'], 'type': 'str'},
                'application': {'type': 'raw'},
                'exempt-ip': {
                    'type': 'list',
                    'options': {'dst-ip': {'type': 'str'}, 'id': {'type': 'int'}, 'src-ip': {'type': 'str'}},
                    'elements': 'dict'
                },
                'id': {'required': True, 'type': 'int'},
                'location': {'type': 'raw'},
                'log': {'choices': ['disable', 'enable'], 'type': 'str'},
                'log-attack-context': {'choices': ['disable', 'enable'], 'type': 'str'},
                'log-packet': {'choices': ['disable', 'enable'], 'type': 'str'},
                'os': {'type': 'raw'},
                'protocol': {'type': 'raw'},
                'quarantine': {'choices': ['none', 'attacker', 'both', 'interface'], 'type': 'str'},
                'quarantine-expiry': {'type': 'str'},
                'quarantine-log': {'choices': ['disable', 'enable'], 'type': 'str'},
                'rate-count': {'type': 'int'},
                'rate-duration': {'type': 'int'},
                'rate-mode': {'choices': ['periodical', 'continuous'], 'type': 'str'},
                'rate-track': {'choices': ['none', 'src-ip', 'dest-ip', 'dhcp-client-mac', 'dns-domain'], 'type': 'str'},
                'rule': {'type': 'raw'},
                'severity': {'type': 'raw'},
                'status': {'choices': ['disable', 'enable', 'default'], 'type': 'str'},
                'tags': {'v_range': [['6.2.0', '6.4.14']], 'type': 'str'},
                'cve': {'v_range': [['6.4.2', '']], 'type': 'raw'},
                'default-action': {'v_range': [['7.2.0', '']], 'choices': ['block', 'pass', 'all', 'drop'], 'type': 'str'},
                'default-status': {'v_range': [['7.2.0', '']], 'choices': ['disable', 'enable', 'all'], 'type': 'str'},
                'last-modified': {'v_range': [['7.2.0', '']], 'type': 'raw'},
                'vuln-type': {'v_range': [['7.2.0', '']], 'type': 'raw'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('full crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'ips_sensor_entries'),
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
