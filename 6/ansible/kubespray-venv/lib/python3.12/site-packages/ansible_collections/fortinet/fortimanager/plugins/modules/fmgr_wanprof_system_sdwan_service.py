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
module: fmgr_wanprof_system_sdwan_service
short_description: Create SD-WAN rules
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
    wanprof:
        description: The parameter (wanprof) in requested url.
        type: str
        required: true
    wanprof_system_sdwan_service:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            addr-mode:
                type: str
                description: Deprecated, please rename it to addr_mode. Address mode
                choices:
                    - 'ipv4'
                    - 'ipv6'
            bandwidth-weight:
                type: int
                description: Deprecated, please rename it to bandwidth_weight. Coefficient of reciprocal of available bidirectional bandwidth in the fo...
            default:
                type: str
                description: Enable/disable use of SD-WAN as default service.
                choices:
                    - 'disable'
                    - 'enable'
            dscp-forward:
                type: str
                description: Deprecated, please rename it to dscp_forward. Enable/disable forward traffic DSCP tag.
                choices:
                    - 'disable'
                    - 'enable'
            dscp-forward-tag:
                type: str
                description: Deprecated, please rename it to dscp_forward_tag. Forward traffic DSCP tag.
            dscp-reverse:
                type: str
                description: Deprecated, please rename it to dscp_reverse. Enable/disable reverse traffic DSCP tag.
                choices:
                    - 'disable'
                    - 'enable'
            dscp-reverse-tag:
                type: str
                description: Deprecated, please rename it to dscp_reverse_tag. Reverse traffic DSCP tag.
            dst:
                type: raw
                description: (list or str) Destination address name.
            dst-negate:
                type: str
                description: Deprecated, please rename it to dst_negate. Enable/disable negation of destination address match.
                choices:
                    - 'disable'
                    - 'enable'
            dst6:
                type: raw
                description: (list or str) Destination address6 name.
            end-port:
                type: int
                description: Deprecated, please rename it to end_port. End destination port number.
            gateway:
                type: str
                description: Enable/disable SD-WAN service gateway.
                choices:
                    - 'disable'
                    - 'enable'
            groups:
                type: raw
                description: (list or str) User groups.
            hash-mode:
                type: str
                description: Deprecated, please rename it to hash_mode. Hash algorithm for selected priority members for load balance mode.
                choices:
                    - 'round-robin'
                    - 'source-ip-based'
                    - 'source-dest-ip-based'
                    - 'inbandwidth'
                    - 'outbandwidth'
                    - 'bibandwidth'
            health-check:
                type: raw
                description: (list or str) Deprecated, please rename it to health_check. Health check list.
            hold-down-time:
                type: int
                description: Deprecated, please rename it to hold_down_time. Waiting period in seconds when switching from the back-up member to the pr...
            id:
                type: int
                description: SD-WAN rule ID
                required: true
            input-device:
                type: raw
                description: (list or str) Deprecated, please rename it to input_device. Source interface name.
            input-device-negate:
                type: str
                description: Deprecated, please rename it to input_device_negate. Enable/disable negation of input device match.
                choices:
                    - 'disable'
                    - 'enable'
            internet-service:
                type: str
                description: Deprecated, please rename it to internet_service. Enable/disable use of Internet service for application-based load balancing.
                choices:
                    - 'disable'
                    - 'enable'
            internet-service-app-ctrl:
                type: raw
                description: (list) Deprecated, please rename it to internet_service_app_ctrl. Application control based Internet Service ID list.
            internet-service-app-ctrl-group:
                type: raw
                description: (list or str) Deprecated, please rename it to internet_service_app_ctrl_group. Application control based Internet Service ...
            internet-service-custom:
                type: raw
                description: (list or str) Deprecated, please rename it to internet_service_custom. Custom Internet service name list.
            internet-service-custom-group:
                type: raw
                description: (list or str) Deprecated, please rename it to internet_service_custom_group. Custom Internet Service group list.
            internet-service-group:
                type: raw
                description: (list or str) Deprecated, please rename it to internet_service_group. Internet Service group list.
            internet-service-name:
                type: raw
                description: (list or str) Deprecated, please rename it to internet_service_name. Internet service name list.
            jitter-weight:
                type: int
                description: Deprecated, please rename it to jitter_weight. Coefficient of jitter in the formula of custom-profile-1.
            latency-weight:
                type: int
                description: Deprecated, please rename it to latency_weight. Coefficient of latency in the formula of custom-profile-1.
            link-cost-factor:
                type: str
                description: Deprecated, please rename it to link_cost_factor. Link cost factor.
                choices:
                    - 'latency'
                    - 'jitter'
                    - 'packet-loss'
                    - 'inbandwidth'
                    - 'outbandwidth'
                    - 'bibandwidth'
                    - 'custom-profile-1'
            link-cost-threshold:
                type: int
                description: Deprecated, please rename it to link_cost_threshold. Percentage threshold change of link cost values that will result in p...
            minimum-sla-meet-members:
                type: int
                description: Deprecated, please rename it to minimum_sla_meet_members. Minimum number of members which meet SLA.
            mode:
                type: str
                description: Control how the SD-WAN rule sets the priority of interfaces in the SD-WAN.
                choices:
                    - 'auto'
                    - 'manual'
                    - 'priority'
                    - 'sla'
                    - 'load-balance'
            name:
                type: str
                description: SD-WAN rule name.
            packet-loss-weight:
                type: int
                description: Deprecated, please rename it to packet_loss_weight. Coefficient of packet-loss in the formula of custom-profile-1.
            priority-members:
                type: raw
                description: (list or str) Deprecated, please rename it to priority_members. Member sequence number list.
            protocol:
                type: int
                description: Protocol number.
            quality-link:
                type: int
                description: Deprecated, please rename it to quality_link. Quality grade.
            role:
                type: str
                description: Service role to work with neighbor.
                choices:
                    - 'primary'
                    - 'secondary'
                    - 'standalone'
            route-tag:
                type: int
                description: Deprecated, please rename it to route_tag. IPv4 route map route-tag.
            sla:
                type: list
                elements: dict
                description: Sla.
                suboptions:
                    health-check:
                        type: str
                        description: Deprecated, please rename it to health_check. SD-WAN health-check.
                    id:
                        type: int
                        description: SLA ID.
            sla-compare-method:
                type: str
                description: Deprecated, please rename it to sla_compare_method. Method to compare SLA value for SLA mode.
                choices:
                    - 'order'
                    - 'number'
            src:
                type: raw
                description: (list or str) Source address name.
            src-negate:
                type: str
                description: Deprecated, please rename it to src_negate. Enable/disable negation of source address match.
                choices:
                    - 'disable'
                    - 'enable'
            src6:
                type: raw
                description: (list or str) Source address6 name.
            standalone-action:
                type: str
                description: Deprecated, please rename it to standalone_action. Enable/disable service when selected neighbor role is standalone while ...
                choices:
                    - 'disable'
                    - 'enable'
            start-port:
                type: int
                description: Deprecated, please rename it to start_port. Start destination port number.
            status:
                type: str
                description: Enable/disable SD-WAN service.
                choices:
                    - 'disable'
                    - 'enable'
            tos:
                type: str
                description: Type of service bit pattern.
            tos-mask:
                type: str
                description: Deprecated, please rename it to tos_mask. Type of service evaluated bits.
            users:
                type: raw
                description: (list or str) User name.
            tie-break:
                type: str
                description: Deprecated, please rename it to tie_break. Method of selecting member if more than one meets the SLA.
                choices:
                    - 'zone'
                    - 'cfg-order'
                    - 'fib-best-match'
                    - 'input-device'
            use-shortcut-sla:
                type: str
                description: Deprecated, please rename it to use_shortcut_sla. Enable/disable use of ADVPN shortcut for quality comparison.
                choices:
                    - 'disable'
                    - 'enable'
            input-zone:
                type: raw
                description: (list) Deprecated, please rename it to input_zone. Source input-zone name.
            internet-service-app-ctrl-category:
                type: raw
                description: (list) Deprecated, please rename it to internet_service_app_ctrl_category. IDs of one or more application control categories.
            passive-measurement:
                type: str
                description: Deprecated, please rename it to passive_measurement. Enable/disable passive measurement based on the service criteria.
                choices:
                    - 'disable'
                    - 'enable'
            priority-zone:
                type: raw
                description: (list or str) Deprecated, please rename it to priority_zone. Priority zone name list.
            agent-exclusive:
                type: str
                description: Deprecated, please rename it to agent_exclusive. Set/unset the service as agent use exclusively.
                choices:
                    - 'disable'
                    - 'enable'
            shortcut:
                type: str
                description: Enable/disable shortcut for this service.
                choices:
                    - 'disable'
                    - 'enable'
            shortcut-stickiness:
                type: str
                description: Deprecated, please rename it to shortcut_stickiness. Enable/disable shortcut-stickiness of ADVPN.
                choices:
                    - 'disable'
                    - 'enable'
            end-src-port:
                type: int
                description: Deprecated, please rename it to end_src_port. End source port number.
            load-balance:
                type: str
                description: Deprecated, please rename it to load_balance. Enable/disable load-balance.
                choices:
                    - 'disable'
                    - 'enable'
            sla-stickiness:
                type: str
                description: Deprecated, please rename it to sla_stickiness. Enable/disable SLA stickiness
                choices:
                    - 'disable'
                    - 'enable'
            start-src-port:
                type: int
                description: Deprecated, please rename it to start_src_port. Start source port number.
            zone-mode:
                type: str
                description: Deprecated, please rename it to zone_mode. Enable/disable zone mode.
                choices:
                    - 'disable'
                    - 'enable'
            shortcut-priority:
                type: str
                description: Deprecated, please rename it to shortcut_priority. High priority of ADVPN shortcut for this service.
                choices:
                    - 'disable'
                    - 'enable'
                    - 'auto'
            comment:
                type: str
                description: Comments.
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
    - name: Create SD-WAN rules
      fortinet.fortimanager.fmgr_wanprof_system_sdwan_service:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        adom: <your own value>
        wanprof: <your own value>
        state: present # <value in [present, absent]>
        wanprof_system_sdwan_service:
          addr_mode: <value in [ipv4, ipv6]>
          bandwidth_weight: <integer>
          default: <value in [disable, enable]>
          dscp_forward: <value in [disable, enable]>
          dscp_forward_tag: <string>
          dscp_reverse: <value in [disable, enable]>
          dscp_reverse_tag: <string>
          dst: <list or string>
          dst_negate: <value in [disable, enable]>
          dst6: <list or string>
          end_port: <integer>
          gateway: <value in [disable, enable]>
          groups: <list or string>
          hash_mode: <value in [round-robin, source-ip-based, source-dest-ip-based, ...]>
          health_check: <list or string>
          hold_down_time: <integer>
          id: <integer>
          input_device: <list or string>
          input_device_negate: <value in [disable, enable]>
          internet_service: <value in [disable, enable]>
          internet_service_app_ctrl: <list or integer>
          internet_service_app_ctrl_group: <list or string>
          internet_service_custom: <list or string>
          internet_service_custom_group: <list or string>
          internet_service_group: <list or string>
          internet_service_name: <list or string>
          jitter_weight: <integer>
          latency_weight: <integer>
          link_cost_factor: <value in [latency, jitter, packet-loss, ...]>
          link_cost_threshold: <integer>
          minimum_sla_meet_members: <integer>
          mode: <value in [auto, manual, priority, ...]>
          name: <string>
          packet_loss_weight: <integer>
          priority_members: <list or string>
          protocol: <integer>
          quality_link: <integer>
          role: <value in [primary, secondary, standalone]>
          route_tag: <integer>
          sla:
            -
              health_check: <string>
              id: <integer>
          sla_compare_method: <value in [order, number]>
          src: <list or string>
          src_negate: <value in [disable, enable]>
          src6: <list or string>
          standalone_action: <value in [disable, enable]>
          start_port: <integer>
          status: <value in [disable, enable]>
          tos: <string>
          tos_mask: <string>
          users: <list or string>
          tie_break: <value in [zone, cfg-order, fib-best-match, ...]>
          use_shortcut_sla: <value in [disable, enable]>
          input_zone: <list or string>
          internet_service_app_ctrl_category: <list or integer>
          passive_measurement: <value in [disable, enable]>
          priority_zone: <list or string>
          agent_exclusive: <value in [disable, enable]>
          shortcut: <value in [disable, enable]>
          shortcut_stickiness: <value in [disable, enable]>
          end_src_port: <integer>
          load_balance: <value in [disable, enable]>
          sla_stickiness: <value in [disable, enable]>
          start_src_port: <integer>
          zone_mode: <value in [disable, enable]>
          shortcut_priority: <value in [disable, enable, auto]>
          comment: <string>
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
        '/pm/config/adom/{adom}/wanprof/{wanprof}/system/sdwan/service'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/wanprof/{wanprof}/system/sdwan/service/{service}'
    ]

    url_params = ['adom', 'wanprof']
    module_primary_key = 'id'
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'wanprof': {'required': True, 'type': 'str'},
        'wanprof_system_sdwan_service': {
            'type': 'dict',
            'v_range': [['6.4.1', '']],
            'options': {
                'addr-mode': {'v_range': [['6.4.1', '']], 'choices': ['ipv4', 'ipv6'], 'type': 'str'},
                'bandwidth-weight': {'v_range': [['6.4.1', '']], 'type': 'int'},
                'default': {'v_range': [['6.4.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'dscp-forward': {'v_range': [['6.4.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'dscp-forward-tag': {'v_range': [['6.4.1', '']], 'type': 'str'},
                'dscp-reverse': {'v_range': [['6.4.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'dscp-reverse-tag': {'v_range': [['6.4.1', '']], 'type': 'str'},
                'dst': {'v_range': [['6.4.1', '']], 'type': 'raw'},
                'dst-negate': {'v_range': [['6.4.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'dst6': {'v_range': [['6.4.1', '']], 'type': 'raw'},
                'end-port': {'v_range': [['6.4.1', '']], 'type': 'int'},
                'gateway': {'v_range': [['6.4.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'groups': {'v_range': [['6.4.1', '']], 'type': 'raw'},
                'hash-mode': {
                    'v_range': [['6.4.2', '']],
                    'choices': ['round-robin', 'source-ip-based', 'source-dest-ip-based', 'inbandwidth', 'outbandwidth', 'bibandwidth'],
                    'type': 'str'
                },
                'health-check': {'v_range': [['6.4.1', '']], 'type': 'raw'},
                'hold-down-time': {'v_range': [['6.4.1', '']], 'type': 'int'},
                'id': {'v_range': [['6.4.1', '']], 'required': True, 'type': 'int'},
                'input-device': {'v_range': [['6.4.1', '']], 'type': 'raw'},
                'input-device-negate': {'v_range': [['6.4.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'internet-service': {'v_range': [['6.4.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'internet-service-app-ctrl': {'v_range': [['6.4.1', '']], 'type': 'raw'},
                'internet-service-app-ctrl-group': {'v_range': [['6.4.1', '']], 'type': 'raw'},
                'internet-service-custom': {'v_range': [['6.4.1', '']], 'type': 'raw'},
                'internet-service-custom-group': {'v_range': [['6.4.1', '']], 'type': 'raw'},
                'internet-service-group': {'v_range': [['6.4.1', '']], 'type': 'raw'},
                'internet-service-name': {'v_range': [['6.4.1', '']], 'type': 'raw'},
                'jitter-weight': {'v_range': [['6.4.1', '']], 'type': 'int'},
                'latency-weight': {'v_range': [['6.4.1', '']], 'type': 'int'},
                'link-cost-factor': {
                    'v_range': [['6.4.1', '']],
                    'choices': ['latency', 'jitter', 'packet-loss', 'inbandwidth', 'outbandwidth', 'bibandwidth', 'custom-profile-1'],
                    'type': 'str'
                },
                'link-cost-threshold': {'v_range': [['6.4.1', '']], 'type': 'int'},
                'minimum-sla-meet-members': {'v_range': [['6.4.2', '']], 'type': 'int'},
                'mode': {'v_range': [['6.4.1', '']], 'choices': ['auto', 'manual', 'priority', 'sla', 'load-balance'], 'type': 'str'},
                'name': {'v_range': [['6.4.1', '']], 'type': 'str'},
                'packet-loss-weight': {'v_range': [['6.4.1', '']], 'type': 'int'},
                'priority-members': {'v_range': [['6.4.1', '']], 'type': 'raw'},
                'protocol': {'v_range': [['6.4.1', '']], 'type': 'int'},
                'quality-link': {'v_range': [['6.4.1', '']], 'type': 'int'},
                'role': {'v_range': [['6.4.1', '']], 'choices': ['primary', 'secondary', 'standalone'], 'type': 'str'},
                'route-tag': {'v_range': [['6.4.1', '']], 'type': 'int'},
                'sla': {
                    'v_range': [['6.4.1', '']],
                    'type': 'list',
                    'options': {'health-check': {'v_range': [['6.4.1', '']], 'type': 'str'}, 'id': {'v_range': [['6.4.1', '']], 'type': 'int'}},
                    'elements': 'dict'
                },
                'sla-compare-method': {'v_range': [['6.4.1', '']], 'choices': ['order', 'number'], 'type': 'str'},
                'src': {'v_range': [['6.4.1', '']], 'type': 'raw'},
                'src-negate': {'v_range': [['6.4.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'src6': {'v_range': [['6.4.1', '']], 'type': 'raw'},
                'standalone-action': {'v_range': [['6.4.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'start-port': {'v_range': [['6.4.1', '']], 'type': 'int'},
                'status': {'v_range': [['6.4.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'tos': {'v_range': [['6.4.1', '']], 'type': 'str'},
                'tos-mask': {'v_range': [['6.4.1', '']], 'type': 'str'},
                'users': {'v_range': [['6.4.1', '']], 'type': 'raw'},
                'tie-break': {'v_range': [['6.4.3', '']], 'choices': ['zone', 'cfg-order', 'fib-best-match', 'input-device'], 'type': 'str'},
                'use-shortcut-sla': {'v_range': [['6.4.4', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'input-zone': {'v_range': [['7.2.0', '']], 'type': 'raw'},
                'internet-service-app-ctrl-category': {'v_range': [['7.2.0', '']], 'type': 'raw'},
                'passive-measurement': {'v_range': [['7.0.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'priority-zone': {'v_range': [['7.0.1', '']], 'type': 'raw'},
                'agent-exclusive': {'v_range': [['7.2.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'shortcut': {'v_range': [['7.4.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'shortcut-stickiness': {'v_range': [['7.4.0', '7.4.1']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'end-src-port': {'v_range': [['7.4.1', '']], 'type': 'int'},
                'load-balance': {'v_range': [['7.4.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'sla-stickiness': {'v_range': [['7.4.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'start-src-port': {'v_range': [['7.4.1', '']], 'type': 'int'},
                'zone-mode': {'v_range': [['7.4.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'shortcut-priority': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable', 'auto'], 'type': 'str'},
                'comment': {'v_range': [['7.6.0', '']], 'type': 'str'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('full crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'wanprof_system_sdwan_service'),
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
