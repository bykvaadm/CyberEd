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
module: fmgr_router_routemap_rule
short_description: Rule.
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
    route-map:
        description: Deprecated, please use "route_map"
        type: str
    route_map:
        description: The parameter (route-map) in requested url.
        type: str
    router_routemap_rule:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            action:
                type: str
                description: Action.
                choices:
                    - 'permit'
                    - 'deny'
            id:
                type: int
                description: Rule ID.
                required: true
            match-as-path:
                type: str
                description: Deprecated, please rename it to match_as_path. Match BGP AS path list.
            match-community:
                type: str
                description: Deprecated, please rename it to match_community. Match BGP community list.
            match-community-exact:
                type: str
                description: Deprecated, please rename it to match_community_exact. Enable/disable exact matching of communities.
                choices:
                    - 'disable'
                    - 'enable'
            match-flags:
                type: int
                description: Deprecated, please rename it to match_flags. Match flags.
            match-interface:
                type: str
                description: Deprecated, please rename it to match_interface. Match interface configuration.
            match-ip-address:
                type: str
                description: Deprecated, please rename it to match_ip_address. Match IP address permitted by access-list or prefix-list.
            match-ip-nexthop:
                type: str
                description: Deprecated, please rename it to match_ip_nexthop. Match next hop IP address passed by access-list or prefix-list.
            match-ip6-address:
                type: str
                description: Deprecated, please rename it to match_ip6_address. Match IPv6 address permitted by access-list6 or prefix-list6.
            match-ip6-nexthop:
                type: str
                description: Deprecated, please rename it to match_ip6_nexthop. Match next hop IPv6 address passed by access-list6 or prefix-list6.
            match-metric:
                type: str
                description: Deprecated, please rename it to match_metric. Match metric for redistribute routes.
            match-origin:
                type: str
                description: Deprecated, please rename it to match_origin. Match BGP origin code.
                choices:
                    - 'none'
                    - 'egp'
                    - 'igp'
                    - 'incomplete'
            match-route-type:
                type: str
                description: Deprecated, please rename it to match_route_type. Match route type.
                choices:
                    - '1'
                    - '2'
                    - 'none'
                    - 'external-type1'
                    - 'external-type2'
            match-tag:
                type: str
                description: Deprecated, please rename it to match_tag. Match tag.
            match-vrf:
                type: int
                description: Deprecated, please rename it to match_vrf. Match VRF ID.
            set-aggregator-as:
                type: int
                description: Deprecated, please rename it to set_aggregator_as. BGP aggregator AS.
            set-aggregator-ip:
                type: str
                description: Deprecated, please rename it to set_aggregator_ip. BGP aggregator IP.
            set-aspath:
                type: raw
                description: (list) Deprecated, please rename it to set_aspath. Prepend BGP AS path attribute.
            set-aspath-action:
                type: str
                description: Deprecated, please rename it to set_aspath_action. Specify preferred action of set-aspath.
                choices:
                    - 'prepend'
                    - 'replace'
            set-atomic-aggregate:
                type: str
                description: Deprecated, please rename it to set_atomic_aggregate. Enable/disable BGP atomic aggregate attribute.
                choices:
                    - 'disable'
                    - 'enable'
            set-community:
                type: raw
                description: (list) Deprecated, please rename it to set_community. BGP community attribute.
            set-community-additive:
                type: str
                description: Deprecated, please rename it to set_community_additive. Enable/disable adding set-community to existing community.
                choices:
                    - 'disable'
                    - 'enable'
            set-community-delete:
                type: str
                description: Deprecated, please rename it to set_community_delete. Delete communities matching community list.
            set-dampening-max-suppress:
                type: int
                description: Deprecated, please rename it to set_dampening_max_suppress. Maximum duration to suppress a route
            set-dampening-reachability-half-life:
                type: int
                description: Deprecated, please rename it to set_dampening_reachability_half_life. Reachability half-life time for the penalty
            set-dampening-reuse:
                type: int
                description: Deprecated, please rename it to set_dampening_reuse. Value to start reusing a route
            set-dampening-suppress:
                type: int
                description: Deprecated, please rename it to set_dampening_suppress. Value to start suppressing a route
            set-dampening-unreachability-half-life:
                type: int
                description: Deprecated, please rename it to set_dampening_unreachability_half_life. Unreachability Half-life time for the penalty
            set-extcommunity-rt:
                type: raw
                description: (list) Deprecated, please rename it to set_extcommunity_rt. Route Target extended community.
            set-extcommunity-soo:
                type: raw
                description: (list) Deprecated, please rename it to set_extcommunity_soo. Site-of-Origin extended community.
            set-flags:
                type: int
                description: Deprecated, please rename it to set_flags. Set flags.
            set-ip-nexthop:
                type: str
                description: Deprecated, please rename it to set_ip_nexthop. IP address of next hop.
            set-ip6-nexthop:
                type: str
                description: Deprecated, please rename it to set_ip6_nexthop. IPv6 global address of next hop.
            set-ip6-nexthop-local:
                type: str
                description: Deprecated, please rename it to set_ip6_nexthop_local. IPv6 local address of next hop.
            set-local-preference:
                type: str
                description: Deprecated, please rename it to set_local_preference. BGP local preference path attribute.
            set-metric:
                type: str
                description: Deprecated, please rename it to set_metric. Metric value.
            set-metric-type:
                type: str
                description: Deprecated, please rename it to set_metric_type. Metric type.
                choices:
                    - '1'
                    - '2'
                    - 'none'
                    - 'external-type1'
                    - 'external-type2'
            set-origin:
                type: str
                description: Deprecated, please rename it to set_origin. BGP origin code.
                choices:
                    - 'none'
                    - 'egp'
                    - 'igp'
                    - 'incomplete'
            set-originator-id:
                type: str
                description: Deprecated, please rename it to set_originator_id. BGP originator ID attribute.
            set-priority:
                type: int
                description: Deprecated, please rename it to set_priority. Priority for routing table.
            set-route-tag:
                type: str
                description: Deprecated, please rename it to set_route_tag. Route tag for routing table.
            set-tag:
                type: str
                description: Deprecated, please rename it to set_tag. Tag value.
            set-weight:
                type: str
                description: Deprecated, please rename it to set_weight. BGP weight for routing table.
            match-extcommunity:
                type: str
                description: Deprecated, please rename it to match_extcommunity. Match BGP extended community list.
            match-extcommunity-exact:
                type: str
                description: Deprecated, please rename it to match_extcommunity_exact. Enable/disable exact matching of extended communities.
                choices:
                    - 'disable'
                    - 'enable'
            set-ip-prefsrc:
                type: str
                description: Deprecated, please rename it to set_ip_prefsrc. IP address of preferred source.
            set-vpnv4-nexthop:
                type: str
                description: Deprecated, please rename it to set_vpnv4_nexthop. IP address of VPNv4 next-hop.
            set-vpnv6-nexthop:
                type: str
                description: Deprecated, please rename it to set_vpnv6_nexthop. IPv6 global address of VPNv6 next-hop.
            set-vpnv6-nexthop-local:
                type: str
                description: Deprecated, please rename it to set_vpnv6_nexthop_local. IPv6 link-local address of VPNv6 next-hop.
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
    - name: Rule.
      fortinet.fortimanager.fmgr_router_routemap_rule:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        adom: <your own value>
        route_map: <your own value>
        state: present # <value in [present, absent]>
        router_routemap_rule:
          action: <value in [permit, deny]>
          id: <integer>
          match_as_path: <string>
          match_community: <string>
          match_community_exact: <value in [disable, enable]>
          match_flags: <integer>
          match_interface: <string>
          match_ip_address: <string>
          match_ip_nexthop: <string>
          match_ip6_address: <string>
          match_ip6_nexthop: <string>
          match_metric: <string>
          match_origin: <value in [none, egp, igp, ...]>
          match_route_type: <value in [1, 2, none, ...]>
          match_tag: <string>
          match_vrf: <integer>
          set_aggregator_as: <integer>
          set_aggregator_ip: <string>
          set_aspath: <list or string>
          set_aspath_action: <value in [prepend, replace]>
          set_atomic_aggregate: <value in [disable, enable]>
          set_community: <list or string>
          set_community_additive: <value in [disable, enable]>
          set_community_delete: <string>
          set_dampening_max_suppress: <integer>
          set_dampening_reachability_half_life: <integer>
          set_dampening_reuse: <integer>
          set_dampening_suppress: <integer>
          set_dampening_unreachability_half_life: <integer>
          set_extcommunity_rt: <list or string>
          set_extcommunity_soo: <list or string>
          set_flags: <integer>
          set_ip_nexthop: <string>
          set_ip6_nexthop: <string>
          set_ip6_nexthop_local: <string>
          set_local_preference: <string>
          set_metric: <string>
          set_metric_type: <value in [1, 2, none, ...]>
          set_origin: <value in [none, egp, igp, ...]>
          set_originator_id: <string>
          set_priority: <integer>
          set_route_tag: <string>
          set_tag: <string>
          set_weight: <string>
          match_extcommunity: <string>
          match_extcommunity_exact: <value in [disable, enable]>
          set_ip_prefsrc: <string>
          set_vpnv4_nexthop: <string>
          set_vpnv6_nexthop: <string>
          set_vpnv6_nexthop_local: <string>
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
        '/pm/config/adom/{adom}/obj/router/route-map/{route-map}/rule',
        '/pm/config/global/obj/router/route-map/{route-map}/rule'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/router/route-map/{route-map}/rule/{rule}',
        '/pm/config/global/obj/router/route-map/{route-map}/rule/{rule}'
    ]

    url_params = ['adom', 'route-map']
    module_primary_key = 'id'
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'route-map': {'type': 'str', 'api_name': 'route_map'},
        'route_map': {'type': 'str'},
        'router_routemap_rule': {
            'type': 'dict',
            'v_range': [['7.0.2', '']],
            'options': {
                'action': {'v_range': [['7.0.2', '']], 'choices': ['permit', 'deny'], 'type': 'str'},
                'id': {'v_range': [['7.0.2', '']], 'required': True, 'type': 'int'},
                'match-as-path': {'v_range': [['7.0.2', '']], 'type': 'str'},
                'match-community': {'v_range': [['7.0.2', '']], 'type': 'str'},
                'match-community-exact': {'v_range': [['7.0.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'match-flags': {'v_range': [['7.0.2', '']], 'type': 'int'},
                'match-interface': {'v_range': [['7.0.2', '']], 'type': 'str'},
                'match-ip-address': {'v_range': [['7.0.2', '']], 'type': 'str'},
                'match-ip-nexthop': {'v_range': [['7.0.2', '']], 'type': 'str'},
                'match-ip6-address': {'v_range': [['7.0.2', '']], 'type': 'str'},
                'match-ip6-nexthop': {'v_range': [['7.0.2', '']], 'type': 'str'},
                'match-metric': {'v_range': [['7.0.2', '']], 'type': 'str'},
                'match-origin': {'v_range': [['7.0.2', '']], 'choices': ['none', 'egp', 'igp', 'incomplete'], 'type': 'str'},
                'match-route-type': {'v_range': [['7.0.2', '']], 'choices': ['1', '2', 'none', 'external-type1', 'external-type2'], 'type': 'str'},
                'match-tag': {'v_range': [['7.0.2', '']], 'type': 'str'},
                'match-vrf': {'v_range': [['7.0.2', '']], 'type': 'int'},
                'set-aggregator-as': {'v_range': [['7.0.2', '']], 'type': 'int'},
                'set-aggregator-ip': {'v_range': [['7.0.2', '']], 'type': 'str'},
                'set-aspath': {'v_range': [['7.0.2', '']], 'type': 'raw'},
                'set-aspath-action': {'v_range': [['7.0.2', '']], 'choices': ['prepend', 'replace'], 'type': 'str'},
                'set-atomic-aggregate': {'v_range': [['7.0.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'set-community': {'v_range': [['7.0.2', '']], 'type': 'raw'},
                'set-community-additive': {'v_range': [['7.0.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'set-community-delete': {'v_range': [['7.0.2', '']], 'type': 'str'},
                'set-dampening-max-suppress': {'v_range': [['7.0.2', '']], 'type': 'int'},
                'set-dampening-reachability-half-life': {'v_range': [['7.0.2', '']], 'type': 'int'},
                'set-dampening-reuse': {'v_range': [['7.0.2', '']], 'type': 'int'},
                'set-dampening-suppress': {'v_range': [['7.0.2', '']], 'type': 'int'},
                'set-dampening-unreachability-half-life': {'v_range': [['7.0.2', '']], 'type': 'int'},
                'set-extcommunity-rt': {'v_range': [['7.0.2', '']], 'type': 'raw'},
                'set-extcommunity-soo': {'v_range': [['7.0.2', '']], 'type': 'raw'},
                'set-flags': {'v_range': [['7.0.2', '']], 'type': 'int'},
                'set-ip-nexthop': {'v_range': [['7.0.2', '']], 'type': 'str'},
                'set-ip6-nexthop': {'v_range': [['7.0.2', '']], 'type': 'str'},
                'set-ip6-nexthop-local': {'v_range': [['7.0.2', '']], 'type': 'str'},
                'set-local-preference': {'v_range': [['7.0.2', '']], 'type': 'str'},
                'set-metric': {'v_range': [['7.0.2', '']], 'type': 'str'},
                'set-metric-type': {'v_range': [['7.0.2', '']], 'choices': ['1', '2', 'none', 'external-type1', 'external-type2'], 'type': 'str'},
                'set-origin': {'v_range': [['7.0.2', '']], 'choices': ['none', 'egp', 'igp', 'incomplete'], 'type': 'str'},
                'set-originator-id': {'v_range': [['7.0.2', '']], 'type': 'str'},
                'set-priority': {'v_range': [['7.2.0', '']], 'type': 'int'},
                'set-route-tag': {'v_range': [['7.0.2', '']], 'type': 'str'},
                'set-tag': {'v_range': [['7.0.2', '']], 'type': 'str'},
                'set-weight': {'v_range': [['7.0.2', '']], 'type': 'str'},
                'match-extcommunity': {'v_range': [['7.2.2', '']], 'type': 'str'},
                'match-extcommunity-exact': {'v_range': [['7.2.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'set-ip-prefsrc': {'v_range': [['7.4.0', '']], 'type': 'str'},
                'set-vpnv4-nexthop': {'v_range': [['7.4.1', '']], 'type': 'str'},
                'set-vpnv6-nexthop': {'v_range': [['7.4.2', '']], 'type': 'str'},
                'set-vpnv6-nexthop-local': {'v_range': [['7.4.2', '']], 'type': 'str'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('full crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'router_routemap_rule'),
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
