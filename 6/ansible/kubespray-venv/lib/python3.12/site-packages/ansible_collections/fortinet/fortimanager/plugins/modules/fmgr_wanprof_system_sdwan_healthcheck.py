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
module: fmgr_wanprof_system_sdwan_healthcheck
short_description: SD-WAN status checking or health checking.
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
    wanprof_system_sdwan_healthcheck:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            _dynamic-server:
                type: str
                description: Deprecated, please rename it to _dynamic_server. Dynamic server.
            addr-mode:
                type: str
                description: Deprecated, please rename it to addr_mode. Address mode
                choices:
                    - 'ipv4'
                    - 'ipv6'
            diffservcode:
                type: str
                description: Differentiated services code point
            dns-match-ip:
                type: str
                description: Deprecated, please rename it to dns_match_ip. Response IP expected from DNS server if the protocol is DNS.
            dns-request-domain:
                type: str
                description: Deprecated, please rename it to dns_request_domain. Fully qualified domain name to resolve for the DNS probe.
            failtime:
                type: int
                description: Number of failures before server is considered lost
            ftp-file:
                type: str
                description: Deprecated, please rename it to ftp_file. Full path and file name on the FTP server to download for FTP health-check to probe.
            ftp-mode:
                type: str
                description: Deprecated, please rename it to ftp_mode. FTP mode.
                choices:
                    - 'passive'
                    - 'port'
            ha-priority:
                type: int
                description: Deprecated, please rename it to ha_priority. HA election priority
            http-agent:
                type: str
                description: Deprecated, please rename it to http_agent. String in the http-agent field in the HTTP header.
            http-get:
                type: str
                description: Deprecated, please rename it to http_get. URL used to communicate with the server if the protocol if the protocol is HTTP.
            http-match:
                type: str
                description: Deprecated, please rename it to http_match. Response string expected from the server if the protocol is HTTP.
            interval:
                type: int
                description: Status check interval in milliseconds, or the time between attempting to connect to the server
            members:
                type: raw
                description: (list or str) Member sequence number list.
            name:
                type: str
                description: Status check or health check name.
                required: true
            packet-size:
                type: int
                description: Deprecated, please rename it to packet_size. Packet size of a twamp test session,
            password:
                type: raw
                description: (list) Twamp controller password in authentication mode
            port:
                type: int
                description: Port number used to communicate with the server over the selected protocol
            probe-count:
                type: int
                description: Deprecated, please rename it to probe_count. Number of most recent probes that should be used to calculate latency and jitter
            probe-packets:
                type: str
                description: Deprecated, please rename it to probe_packets. Enable/disable transmission of probe packets.
                choices:
                    - 'disable'
                    - 'enable'
            probe-timeout:
                type: int
                description: Deprecated, please rename it to probe_timeout. Time to wait before a probe packet is considered lost
            protocol:
                type: str
                description: Protocol used to determine if the FortiGate can communicate with the server.
                choices:
                    - 'ping'
                    - 'tcp-echo'
                    - 'udp-echo'
                    - 'http'
                    - 'twamp'
                    - 'ping6'
                    - 'dns'
                    - 'tcp-connect'
                    - 'ftp'
                    - 'https'
            quality-measured-method:
                type: str
                description: Deprecated, please rename it to quality_measured_method. Method to measure the quality of tcp-connect.
                choices:
                    - 'half-close'
                    - 'half-open'
            recoverytime:
                type: int
                description: Number of successful responses received before server is considered recovered
            security-mode:
                type: str
                description: Deprecated, please rename it to security_mode. Twamp controller security mode.
                choices:
                    - 'none'
                    - 'authentication'
            server:
                type: raw
                description: (list) IP address or FQDN name of the server.
            sla:
                type: list
                elements: dict
                description: Sla.
                suboptions:
                    id:
                        type: int
                        description: SLA ID.
                    jitter-threshold:
                        type: int
                        description: Deprecated, please rename it to jitter_threshold. Jitter for SLA to make decision in milliseconds.
                    latency-threshold:
                        type: int
                        description: Deprecated, please rename it to latency_threshold. Latency for SLA to make decision in milliseconds.
                    link-cost-factor:
                        type: list
                        elements: str
                        description: Deprecated, please rename it to link_cost_factor. Criteria on which to base link selection.
                        choices:
                            - 'latency'
                            - 'jitter'
                            - 'packet-loss'
                            - 'mos'
                            - 'remote'
                    packetloss-threshold:
                        type: int
                        description: Deprecated, please rename it to packetloss_threshold. Packet loss for SLA to make decision in percentage.
                    mos-threshold:
                        type: str
                        description: Deprecated, please rename it to mos_threshold. Minimum Mean Opinion Score for SLA to be marked as pass.
                    priority-in-sla:
                        type: int
                        description: Deprecated, please rename it to priority_in_sla. Value to be distributed into routing table when in-sla
                    priority-out-sla:
                        type: int
                        description: Deprecated, please rename it to priority_out_sla. Value to be distributed into routing table when out-sla
            sla-fail-log-period:
                type: int
                description: Deprecated, please rename it to sla_fail_log_period. Time interval in seconds that SLA fail log messages will be generated
            sla-pass-log-period:
                type: int
                description: Deprecated, please rename it to sla_pass_log_period. Time interval in seconds that SLA pass log messages will be generated
            system-dns:
                type: str
                description: Deprecated, please rename it to system_dns. Enable/disable system DNS as the probe server.
                choices:
                    - 'disable'
                    - 'enable'
            threshold-alert-jitter:
                type: int
                description: Deprecated, please rename it to threshold_alert_jitter. Alert threshold for jitter
            threshold-alert-latency:
                type: int
                description: Deprecated, please rename it to threshold_alert_latency. Alert threshold for latency
            threshold-alert-packetloss:
                type: int
                description: Deprecated, please rename it to threshold_alert_packetloss. Alert threshold for packet loss
            threshold-warning-jitter:
                type: int
                description: Deprecated, please rename it to threshold_warning_jitter. Warning threshold for jitter
            threshold-warning-latency:
                type: int
                description: Deprecated, please rename it to threshold_warning_latency. Warning threshold for latency
            threshold-warning-packetloss:
                type: int
                description: Deprecated, please rename it to threshold_warning_packetloss. Warning threshold for packet loss
            update-cascade-interface:
                type: str
                description: Deprecated, please rename it to update_cascade_interface. Enable/disable update cascade interface.
                choices:
                    - 'disable'
                    - 'enable'
            update-static-route:
                type: str
                description: Deprecated, please rename it to update_static_route. Enable/disable updating the static route.
                choices:
                    - 'disable'
                    - 'enable'
            user:
                type: str
                description: The user name to access probe server.
            detect-mode:
                type: str
                description: Deprecated, please rename it to detect_mode. The mode determining how to detect the server.
                choices:
                    - 'active'
                    - 'passive'
                    - 'prefer-passive'
                    - 'remote'
                    - 'agent-based'
            mos-codec:
                type: str
                description: Deprecated, please rename it to mos_codec. Codec to use for MOS calculation
                choices:
                    - 'g711'
                    - 'g722'
                    - 'g729'
            source:
                type: str
                description: Source IP address used in the health-check packet to the server.
            vrf:
                type: int
                description: Virtual Routing Forwarding ID.
            embed-measured-health:
                type: str
                description: Deprecated, please rename it to embed_measured_health. Enable/disable embedding measured health information.
                choices:
                    - 'disable'
                    - 'enable'
            sla-id-redistribute:
                type: int
                description: Deprecated, please rename it to sla_id_redistribute. Select the ID from the SLA sub-table.
            class-id:
                type: str
                description: Deprecated, please rename it to class_id. Traffic class ID.
            source6:
                type: str
                description: Source IPv6 addressused in the health-check packet to server.
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
    - name: SD-WAN status checking or health checking.
      fortinet.fortimanager.fmgr_wanprof_system_sdwan_healthcheck:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        adom: <your own value>
        wanprof: <your own value>
        state: present # <value in [present, absent]>
        wanprof_system_sdwan_healthcheck:
          _dynamic_server: <string>
          addr_mode: <value in [ipv4, ipv6]>
          diffservcode: <string>
          dns_match_ip: <string>
          dns_request_domain: <string>
          failtime: <integer>
          ftp_file: <string>
          ftp_mode: <value in [passive, port]>
          ha_priority: <integer>
          http_agent: <string>
          http_get: <string>
          http_match: <string>
          interval: <integer>
          members: <list or string>
          name: <string>
          packet_size: <integer>
          password: <list or string>
          port: <integer>
          probe_count: <integer>
          probe_packets: <value in [disable, enable]>
          probe_timeout: <integer>
          protocol: <value in [ping, tcp-echo, udp-echo, ...]>
          quality_measured_method: <value in [half-close, half-open]>
          recoverytime: <integer>
          security_mode: <value in [none, authentication]>
          server: <list or string>
          sla:
            -
              id: <integer>
              jitter_threshold: <integer>
              latency_threshold: <integer>
              link_cost_factor:
                - latency
                - jitter
                - packet-loss
                - mos
                - remote
              packetloss_threshold: <integer>
              mos_threshold: <string>
              priority_in_sla: <integer>
              priority_out_sla: <integer>
          sla_fail_log_period: <integer>
          sla_pass_log_period: <integer>
          system_dns: <value in [disable, enable]>
          threshold_alert_jitter: <integer>
          threshold_alert_latency: <integer>
          threshold_alert_packetloss: <integer>
          threshold_warning_jitter: <integer>
          threshold_warning_latency: <integer>
          threshold_warning_packetloss: <integer>
          update_cascade_interface: <value in [disable, enable]>
          update_static_route: <value in [disable, enable]>
          user: <string>
          detect_mode: <value in [active, passive, prefer-passive, ...]>
          mos_codec: <value in [g711, g722, g729]>
          source: <string>
          vrf: <integer>
          embed_measured_health: <value in [disable, enable]>
          sla_id_redistribute: <integer>
          class_id: <string>
          source6: <string>
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
        '/pm/config/adom/{adom}/wanprof/{wanprof}/system/sdwan/health-check'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/wanprof/{wanprof}/system/sdwan/health-check/{health-check}'
    ]

    url_params = ['adom', 'wanprof']
    module_primary_key = 'name'
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'wanprof': {'required': True, 'type': 'str'},
        'wanprof_system_sdwan_healthcheck': {
            'type': 'dict',
            'v_range': [['6.4.1', '']],
            'options': {
                '_dynamic-server': {'v_range': [['6.4.1', '6.4.14']], 'type': 'str'},
                'addr-mode': {'v_range': [['6.4.1', '']], 'choices': ['ipv4', 'ipv6'], 'type': 'str'},
                'diffservcode': {'v_range': [['6.4.1', '']], 'type': 'str'},
                'dns-match-ip': {'v_range': [['6.4.2', '']], 'type': 'str'},
                'dns-request-domain': {'v_range': [['6.4.1', '']], 'type': 'str'},
                'failtime': {'v_range': [['6.4.1', '']], 'type': 'int'},
                'ftp-file': {'v_range': [['6.4.2', '']], 'type': 'str'},
                'ftp-mode': {'v_range': [['6.4.2', '']], 'choices': ['passive', 'port'], 'type': 'str'},
                'ha-priority': {'v_range': [['6.4.1', '']], 'type': 'int'},
                'http-agent': {'v_range': [['6.4.1', '']], 'type': 'str'},
                'http-get': {'v_range': [['6.4.1', '']], 'type': 'str'},
                'http-match': {'v_range': [['6.4.1', '']], 'type': 'str'},
                'interval': {'v_range': [['6.4.1', '']], 'type': 'int'},
                'members': {'v_range': [['6.4.1', '']], 'type': 'raw'},
                'name': {'v_range': [['6.4.1', '']], 'required': True, 'type': 'str'},
                'packet-size': {'v_range': [['6.4.1', '']], 'type': 'int'},
                'password': {'v_range': [['6.4.1', '']], 'no_log': True, 'type': 'raw'},
                'port': {'v_range': [['6.4.1', '']], 'type': 'int'},
                'probe-count': {'v_range': [['6.4.1', '']], 'type': 'int'},
                'probe-packets': {'v_range': [['6.4.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'probe-timeout': {'v_range': [['6.4.1', '']], 'type': 'int'},
                'protocol': {
                    'v_range': [['6.4.1', '']],
                    'choices': ['ping', 'tcp-echo', 'udp-echo', 'http', 'twamp', 'ping6', 'dns', 'tcp-connect', 'ftp', 'https'],
                    'type': 'str'
                },
                'quality-measured-method': {'v_range': [['6.4.2', '']], 'choices': ['half-close', 'half-open'], 'type': 'str'},
                'recoverytime': {'v_range': [['6.4.1', '']], 'type': 'int'},
                'security-mode': {'v_range': [['6.4.1', '']], 'choices': ['none', 'authentication'], 'type': 'str'},
                'server': {'v_range': [['6.4.1', '']], 'type': 'raw'},
                'sla': {
                    'v_range': [['6.4.1', '']],
                    'type': 'list',
                    'options': {
                        'id': {'v_range': [['6.4.1', '']], 'type': 'int'},
                        'jitter-threshold': {'v_range': [['6.4.1', '']], 'type': 'int'},
                        'latency-threshold': {'v_range': [['6.4.1', '']], 'type': 'int'},
                        'link-cost-factor': {
                            'v_range': [['6.4.1', '']],
                            'type': 'list',
                            'choices': ['latency', 'jitter', 'packet-loss', 'mos', 'remote'],
                            'elements': 'str'
                        },
                        'packetloss-threshold': {'v_range': [['6.4.1', '']], 'type': 'int'},
                        'mos-threshold': {'v_range': [['7.2.0', '']], 'type': 'str'},
                        'priority-in-sla': {'v_range': [['7.2.1', '']], 'type': 'int'},
                        'priority-out-sla': {'v_range': [['7.2.1', '']], 'type': 'int'}
                    },
                    'elements': 'dict'
                },
                'sla-fail-log-period': {'v_range': [['6.4.1', '']], 'type': 'int'},
                'sla-pass-log-period': {'v_range': [['6.4.1', '']], 'no_log': True, 'type': 'int'},
                'system-dns': {'v_range': [['6.4.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'threshold-alert-jitter': {'v_range': [['6.4.1', '']], 'type': 'int'},
                'threshold-alert-latency': {'v_range': [['6.4.1', '']], 'type': 'int'},
                'threshold-alert-packetloss': {'v_range': [['6.4.1', '']], 'type': 'int'},
                'threshold-warning-jitter': {'v_range': [['6.4.1', '']], 'type': 'int'},
                'threshold-warning-latency': {'v_range': [['6.4.1', '']], 'type': 'int'},
                'threshold-warning-packetloss': {'v_range': [['6.4.1', '']], 'type': 'int'},
                'update-cascade-interface': {'v_range': [['6.4.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'update-static-route': {'v_range': [['6.4.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'user': {'v_range': [['6.4.2', '']], 'type': 'str'},
                'detect-mode': {'v_range': [['7.0.0', '']], 'choices': ['active', 'passive', 'prefer-passive', 'remote', 'agent-based'], 'type': 'str'},
                'mos-codec': {'v_range': [['7.2.0', '']], 'choices': ['g711', 'g722', 'g729'], 'type': 'str'},
                'source': {'v_range': [['7.2.0', '']], 'type': 'str'},
                'vrf': {'v_range': [['7.2.0', '']], 'type': 'int'},
                'embed-measured-health': {'v_range': [['7.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'sla-id-redistribute': {'v_range': [['7.2.1', '']], 'type': 'int'},
                'class-id': {'v_range': [['7.4.0', '']], 'type': 'str'},
                'source6': {'v_range': [['7.4.0', '']], 'type': 'str'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('full crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'wanprof_system_sdwan_healthcheck'),
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
