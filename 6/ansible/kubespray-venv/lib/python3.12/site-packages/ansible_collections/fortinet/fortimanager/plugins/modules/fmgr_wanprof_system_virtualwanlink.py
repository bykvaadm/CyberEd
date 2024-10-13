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
module: fmgr_wanprof_system_virtualwanlink
short_description: Configure redundant internet connections using SD-WAN
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
    wanprof_system_virtualwanlink:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            fail-detect:
                type: str
                description: Deprecated, please rename it to fail_detect. Enable/disable SD-WAN Internet connection status checking
                choices:
                    - 'disable'
                    - 'enable'
            health-check:
                type: list
                elements: dict
                description: Deprecated, please rename it to health_check. Health check.
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
                    failtime:
                        type: int
                        description: Number of failures before server is considered lost
                    http-agent:
                        type: str
                        description: Deprecated, please rename it to http_agent. String in the http-agent field in the HTTP header.
                    http-get:
                        type: str
                        description: Deprecated, please rename it to http_get. URL used to communicate with the server if the protocol if the protocol ...
                    http-match:
                        type: str
                        description: Deprecated, please rename it to http_match. Response string expected from the server if the protocol is HTTP.
                    interval:
                        type: int
                        description: Status check interval, or the time between attempting to connect to the server
                    members:
                        type: raw
                        description: (list or str) Member sequence number list.
                    name:
                        type: str
                        description: Status check or health check name.
                    packet-size:
                        type: int
                        description: Deprecated, please rename it to packet_size. Packet size of a twamp test session,
                    password:
                        type: raw
                        description: (list) Twamp controller password in authentication mode
                    port:
                        type: int
                        description: Port number used to communicate with the server over the selected protocol.
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
                            packetloss-threshold:
                                type: int
                                description: Deprecated, please rename it to packetloss_threshold. Packet loss for SLA to make decision in percentage.
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
                    internet-service-id:
                        type: str
                        description: Deprecated, please rename it to internet_service_id. Internet service ID.
                    probe-packets:
                        type: str
                        description: Deprecated, please rename it to probe_packets. Enable/disable transmission of probe packets.
                        choices:
                            - 'disable'
                            - 'enable'
                    sla-fail-log-period:
                        type: int
                        description: Deprecated, please rename it to sla_fail_log_period. Time interval in seconds that SLA fail log messages will be g...
                    sla-pass-log-period:
                        type: int
                        description: Deprecated, please rename it to sla_pass_log_period. Time interval in seconds that SLA pass log messages will be g...
                    timeout:
                        type: int
                        description: How long to wait before not receiving a reply from the server to consider the connetion attempt a failure
                    ha-priority:
                        type: int
                        description: Deprecated, please rename it to ha_priority. HA election priority
                    diffservcode:
                        type: str
                        description: Differentiated services code point
                    probe-timeout:
                        type: int
                        description: Deprecated, please rename it to probe_timeout. Time to wait before a probe packet is considered lost
                    dns-request-domain:
                        type: str
                        description: Deprecated, please rename it to dns_request_domain. Fully qualified domain name to resolve for the DNS probe.
                    probe-count:
                        type: int
                        description: Deprecated, please rename it to probe_count. Number of most recent probes that should be used to calculate latency...
                    system-dns:
                        type: str
                        description: Deprecated, please rename it to system_dns. Enable/disable system DNS as the probe server.
                        choices:
                            - 'disable'
                            - 'enable'
            load-balance-mode:
                type: str
                description: Deprecated, please rename it to load_balance_mode. Algorithm or mode to use for load balancing Internet traffic to SD-WAN ...
                choices:
                    - 'source-ip-based'
                    - 'weight-based'
                    - 'usage-based'
                    - 'source-dest-ip-based'
                    - 'measured-volume-based'
            members:
                type: list
                elements: dict
                description: Members.
                suboptions:
                    _dynamic-member:
                        type: str
                        description: Deprecated, please rename it to _dynamic_member. Dynamic member.
                    comment:
                        type: str
                        description: Comments.
                    gateway:
                        type: str
                        description: The default gateway for this interface.
                    gateway6:
                        type: str
                        description: IPv6 gateway.
                    ingress-spillover-threshold:
                        type: int
                        description: Deprecated, please rename it to ingress_spillover_threshold. Ingress spillover threshold for this interface
                    interface:
                        type: str
                        description: Interface name.
                    priority:
                        type: int
                        description: Priority of the interface
                    seq-num:
                        type: int
                        description: Deprecated, please rename it to seq_num. Sequence number
                    source:
                        type: str
                        description: Source IP address used in the health-check packet to the server.
                    source6:
                        type: str
                        description: Source IPv6 address used in the health-check packet to the server.
                    spillover-threshold:
                        type: int
                        description: Deprecated, please rename it to spillover_threshold. Egress spillover threshold for this interface
                    status:
                        type: str
                        description: Enable/disable this interface in the SD-WAN.
                        choices:
                            - 'disable'
                            - 'enable'
                    volume-ratio:
                        type: int
                        description: Deprecated, please rename it to volume_ratio. Measured volume ratio
                    weight:
                        type: int
                        description: Weight of this interface for weighted load balancing.
                    cost:
                        type: int
                        description: Cost of this interface for services in SLA mode
            service:
                type: list
                elements: dict
                description: Service.
                suboptions:
                    addr-mode:
                        type: str
                        description: Deprecated, please rename it to addr_mode. Address mode
                        choices:
                            - 'ipv4'
                            - 'ipv6'
                    bandwidth-weight:
                        type: int
                        description: Deprecated, please rename it to bandwidth_weight. Coefficient of reciprocal of available bidirectional bandwidth i...
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
                    health-check:
                        type: str
                        description: Deprecated, please rename it to health_check. Health check.
                    hold-down-time:
                        type: int
                        description: Deprecated, please rename it to hold_down_time. Waiting period in seconds when switching from the back-up member t...
                    id:
                        type: int
                        description: Priority rule ID
                    internet-service:
                        type: str
                        description: Deprecated, please rename it to internet_service. Enable/disable use of Internet service for application-based loa...
                        choices:
                            - 'disable'
                            - 'enable'
                    internet-service-ctrl:
                        type: raw
                        description: (list) Deprecated, please rename it to internet_service_ctrl. Control-based Internet Service ID list.
                    internet-service-ctrl-group:
                        type: raw
                        description: (list or str) Deprecated, please rename it to internet_service_ctrl_group. Control-based Internet Service group list.
                    internet-service-custom:
                        type: raw
                        description: (list or str) Deprecated, please rename it to internet_service_custom. Custom Internet service name list.
                    internet-service-custom-group:
                        type: raw
                        description: (list or str) Deprecated, please rename it to internet_service_custom_group. Custom Internet Service group list.
                    internet-service-group:
                        type: raw
                        description: (list or str) Deprecated, please rename it to internet_service_group. Internet Service group list.
                    internet-service-id:
                        type: raw
                        description: (list or str) Deprecated, please rename it to internet_service_id. Internet service ID list.
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
                        description: Deprecated, please rename it to link_cost_threshold. Percentage threshold change of link cost values that will res...
                    member:
                        type: str
                        description: Member sequence number.
                    mode:
                        type: str
                        description: Control how the priority rule sets the priority of interfaces in the SD-WAN.
                        choices:
                            - 'auto'
                            - 'manual'
                            - 'priority'
                            - 'sla'
                            - 'load-balance'
                    name:
                        type: str
                        description: Priority rule name.
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
                                description: Deprecated, please rename it to health_check. Virtual WAN Link health-check.
                            id:
                                type: int
                                description: SLA ID.
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
                    internet-service-app-ctrl:
                        type: raw
                        description: (list) Deprecated, please rename it to internet_service_app_ctrl. Application control based Internet Service ID list.
                    internet-service-app-ctrl-group:
                        type: raw
                        description: (list or str) Deprecated, please rename it to internet_service_app_ctrl_group. Application control based Internet ...
                    role:
                        type: str
                        description: Service role to work with neighbor.
                        choices:
                            - 'primary'
                            - 'secondary'
                            - 'standalone'
                    sla-compare-method:
                        type: str
                        description: Deprecated, please rename it to sla_compare_method. Method to compare SLA value for sla and load balance mode.
                        choices:
                            - 'order'
                            - 'number'
                    standalone-action:
                        type: str
                        description: Deprecated, please rename it to standalone_action. Enable/disable service when selected neighbor role is standalon...
                        choices:
                            - 'disable'
                            - 'enable'
                    input-device:
                        type: raw
                        description: (list or str) Deprecated, please rename it to input_device. Source interface name.
                    internet-service-name:
                        type: str
                        description: Deprecated, please rename it to internet_service_name. Internet service name list.
                    input-device-negate:
                        type: str
                        description: Deprecated, please rename it to input_device_negate. Enable/disable negation of input device match.
                        choices:
                            - 'disable'
                            - 'enable'
            status:
                type: str
                description: Enable/disable SD-WAN.
                choices:
                    - 'disable'
                    - 'enable'
            neighbor:
                type: list
                elements: dict
                description: Neighbor.
                suboptions:
                    health-check:
                        type: str
                        description: Deprecated, please rename it to health_check. SD-WAN health-check name.
                    ip:
                        type: str
                        description: IP address of neighbor.
                    member:
                        type: str
                        description: Member sequence number.
                    role:
                        type: str
                        description: Role of neighbor.
                        choices:
                            - 'primary'
                            - 'secondary'
                            - 'standalone'
                    sla-id:
                        type: int
                        description: Deprecated, please rename it to sla_id. SLA ID.
            neighbor-hold-boot-time:
                type: int
                description: Deprecated, please rename it to neighbor_hold_boot_time. Waiting period in seconds when switching from the primary neighbo...
            neighbor-hold-down:
                type: str
                description: Deprecated, please rename it to neighbor_hold_down. Enable/disable hold switching from the secondary neighbor to the prima...
                choices:
                    - 'disable'
                    - 'enable'
            neighbor-hold-down-time:
                type: int
                description: Deprecated, please rename it to neighbor_hold_down_time. Waiting period in seconds when switching from the secondary neigh...
            fail-alert-interfaces:
                type: raw
                description: (list) Deprecated, please rename it to fail_alert_interfaces. Physical interfaces that will be alerted.
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
    - name: Configure redundant internet connections using SD-WAN
      fortinet.fortimanager.fmgr_wanprof_system_virtualwanlink:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        adom: <your own value>
        wanprof: <your own value>
        wanprof_system_virtualwanlink:
          fail_detect: <value in [disable, enable]>
          health_check:
            -
              _dynamic_server: <string>
              addr_mode: <value in [ipv4, ipv6]>
              failtime: <integer>
              http_agent: <string>
              http_get: <string>
              http_match: <string>
              interval: <integer>
              members: <list or string>
              name: <string>
              packet_size: <integer>
              password: <list or string>
              port: <integer>
              protocol: <value in [ping, tcp-echo, udp-echo, ...]>
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
                  packetloss_threshold: <integer>
              threshold_alert_jitter: <integer>
              threshold_alert_latency: <integer>
              threshold_alert_packetloss: <integer>
              threshold_warning_jitter: <integer>
              threshold_warning_latency: <integer>
              threshold_warning_packetloss: <integer>
              update_cascade_interface: <value in [disable, enable]>
              update_static_route: <value in [disable, enable]>
              internet_service_id: <string>
              probe_packets: <value in [disable, enable]>
              sla_fail_log_period: <integer>
              sla_pass_log_period: <integer>
              timeout: <integer>
              ha_priority: <integer>
              diffservcode: <string>
              probe_timeout: <integer>
              dns_request_domain: <string>
              probe_count: <integer>
              system_dns: <value in [disable, enable]>
          load_balance_mode: <value in [source-ip-based, weight-based, usage-based, ...]>
          members:
            -
              _dynamic_member: <string>
              comment: <string>
              gateway: <string>
              gateway6: <string>
              ingress_spillover_threshold: <integer>
              interface: <string>
              priority: <integer>
              seq_num: <integer>
              source: <string>
              source6: <string>
              spillover_threshold: <integer>
              status: <value in [disable, enable]>
              volume_ratio: <integer>
              weight: <integer>
              cost: <integer>
          service:
            -
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
              health_check: <string>
              hold_down_time: <integer>
              id: <integer>
              internet_service: <value in [disable, enable]>
              internet_service_ctrl: <list or integer>
              internet_service_ctrl_group: <list or string>
              internet_service_custom: <list or string>
              internet_service_custom_group: <list or string>
              internet_service_group: <list or string>
              internet_service_id: <list or string>
              jitter_weight: <integer>
              latency_weight: <integer>
              link_cost_factor: <value in [latency, jitter, packet-loss, ...]>
              link_cost_threshold: <integer>
              member: <string>
              mode: <value in [auto, manual, priority, ...]>
              name: <string>
              packet_loss_weight: <integer>
              priority_members: <list or string>
              protocol: <integer>
              quality_link: <integer>
              route_tag: <integer>
              sla:
                -
                  health_check: <string>
                  id: <integer>
              src: <list or string>
              src_negate: <value in [disable, enable]>
              src6: <list or string>
              start_port: <integer>
              status: <value in [disable, enable]>
              tos: <string>
              tos_mask: <string>
              users: <list or string>
              internet_service_app_ctrl: <list or integer>
              internet_service_app_ctrl_group: <list or string>
              role: <value in [primary, secondary, standalone]>
              sla_compare_method: <value in [order, number]>
              standalone_action: <value in [disable, enable]>
              input_device: <list or string>
              internet_service_name: <string>
              input_device_negate: <value in [disable, enable]>
          status: <value in [disable, enable]>
          neighbor:
            -
              health_check: <string>
              ip: <string>
              member: <string>
              role: <value in [primary, secondary, standalone]>
              sla_id: <integer>
          neighbor_hold_boot_time: <integer>
          neighbor_hold_down: <value in [disable, enable]>
          neighbor_hold_down_time: <integer>
          fail_alert_interfaces: <list or string>
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
        '/pm/config/adom/{adom}/wanprof/{wanprof}/system/virtual-wan-link'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/wanprof/{wanprof}/system/virtual-wan-link/{virtual-wan-link}'
    ]

    url_params = ['adom', 'wanprof']
    module_primary_key = None
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'wanprof': {'required': True, 'type': 'str'},
        'wanprof_system_virtualwanlink': {
            'type': 'dict',
            'v_range': [['6.0.0', '']],
            'options': {
                'fail-detect': {'choices': ['disable', 'enable'], 'type': 'str'},
                'health-check': {
                    'type': 'list',
                    'options': {
                        '_dynamic-server': {'v_range': [['6.0.0', '6.4.14']], 'type': 'str'},
                        'addr-mode': {'choices': ['ipv4', 'ipv6'], 'type': 'str'},
                        'failtime': {'type': 'int'},
                        'http-agent': {'type': 'str'},
                        'http-get': {'type': 'str'},
                        'http-match': {'type': 'str'},
                        'interval': {'type': 'int'},
                        'members': {'type': 'raw'},
                        'name': {'type': 'str'},
                        'packet-size': {'type': 'int'},
                        'password': {'no_log': True, 'type': 'raw'},
                        'port': {'type': 'int'},
                        'protocol': {'choices': ['ping', 'tcp-echo', 'udp-echo', 'http', 'twamp', 'ping6', 'dns'], 'type': 'str'},
                        'recoverytime': {'type': 'int'},
                        'security-mode': {'choices': ['none', 'authentication'], 'type': 'str'},
                        'server': {'type': 'raw'},
                        'sla': {
                            'type': 'list',
                            'options': {
                                'id': {'type': 'int'},
                                'jitter-threshold': {'type': 'int'},
                                'latency-threshold': {'type': 'int'},
                                'link-cost-factor': {'type': 'list', 'choices': ['latency', 'jitter', 'packet-loss'], 'elements': 'str'},
                                'packetloss-threshold': {'type': 'int'}
                            },
                            'elements': 'dict'
                        },
                        'threshold-alert-jitter': {'type': 'int'},
                        'threshold-alert-latency': {'type': 'int'},
                        'threshold-alert-packetloss': {'type': 'int'},
                        'threshold-warning-jitter': {'type': 'int'},
                        'threshold-warning-latency': {'type': 'int'},
                        'threshold-warning-packetloss': {'type': 'int'},
                        'update-cascade-interface': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'update-static-route': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'internet-service-id': {'v_range': [['6.2.0', '7.2.0']], 'type': 'str'},
                        'probe-packets': {'v_range': [['6.2.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'sla-fail-log-period': {'v_range': [['6.2.0', '']], 'type': 'int'},
                        'sla-pass-log-period': {'v_range': [['6.2.0', '']], 'no_log': True, 'type': 'int'},
                        'timeout': {'v_range': [['6.2.0', '6.4.14']], 'type': 'int'},
                        'ha-priority': {'v_range': [['6.2.2', '']], 'type': 'int'},
                        'diffservcode': {'v_range': [['6.2.5', '']], 'type': 'str'},
                        'probe-timeout': {'v_range': [['6.2.5', '']], 'type': 'int'},
                        'dns-request-domain': {'v_range': [['6.4.0', '6.4.0']], 'type': 'str'},
                        'probe-count': {'v_range': [['6.4.0', '6.4.0']], 'type': 'int'},
                        'system-dns': {'v_range': [['6.4.0', '6.4.0']], 'choices': ['disable', 'enable'], 'type': 'str'}
                    },
                    'elements': 'dict'
                },
                'load-balance-mode': {
                    'choices': ['source-ip-based', 'weight-based', 'usage-based', 'source-dest-ip-based', 'measured-volume-based'],
                    'type': 'str'
                },
                'members': {
                    'type': 'list',
                    'options': {
                        '_dynamic-member': {'v_range': [['6.0.0', '6.4.14']], 'type': 'str'},
                        'comment': {'type': 'str'},
                        'gateway': {'type': 'str'},
                        'gateway6': {'type': 'str'},
                        'ingress-spillover-threshold': {'type': 'int'},
                        'interface': {'type': 'str'},
                        'priority': {'type': 'int'},
                        'seq-num': {'type': 'int'},
                        'source': {'type': 'str'},
                        'source6': {'type': 'str'},
                        'spillover-threshold': {'type': 'int'},
                        'status': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'volume-ratio': {'type': 'int'},
                        'weight': {'type': 'int'},
                        'cost': {'v_range': [['6.2.0', '']], 'type': 'int'}
                    },
                    'elements': 'dict'
                },
                'service': {
                    'type': 'list',
                    'options': {
                        'addr-mode': {'choices': ['ipv4', 'ipv6'], 'type': 'str'},
                        'bandwidth-weight': {'type': 'int'},
                        'default': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'dscp-forward': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'dscp-forward-tag': {'type': 'str'},
                        'dscp-reverse': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'dscp-reverse-tag': {'type': 'str'},
                        'dst': {'type': 'raw'},
                        'dst-negate': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'dst6': {'type': 'raw'},
                        'end-port': {'type': 'int'},
                        'gateway': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'groups': {'type': 'raw'},
                        'health-check': {'type': 'str'},
                        'hold-down-time': {'type': 'int'},
                        'id': {'type': 'int'},
                        'internet-service': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'internet-service-ctrl': {'v_range': [['6.0.0', '7.2.1']], 'type': 'raw'},
                        'internet-service-ctrl-group': {'v_range': [['6.0.0', '7.2.1']], 'type': 'raw'},
                        'internet-service-custom': {'type': 'raw'},
                        'internet-service-custom-group': {'type': 'raw'},
                        'internet-service-group': {'type': 'raw'},
                        'internet-service-id': {'type': 'raw'},
                        'jitter-weight': {'type': 'int'},
                        'latency-weight': {'type': 'int'},
                        'link-cost-factor': {
                            'choices': ['latency', 'jitter', 'packet-loss', 'inbandwidth', 'outbandwidth', 'bibandwidth', 'custom-profile-1'],
                            'type': 'str'
                        },
                        'link-cost-threshold': {'type': 'int'},
                        'member': {'v_range': [['6.0.0', '7.2.1']], 'type': 'str'},
                        'mode': {'choices': ['auto', 'manual', 'priority', 'sla', 'load-balance'], 'type': 'str'},
                        'name': {'type': 'str'},
                        'packet-loss-weight': {'type': 'int'},
                        'priority-members': {'type': 'raw'},
                        'protocol': {'type': 'int'},
                        'quality-link': {'type': 'int'},
                        'route-tag': {'type': 'int'},
                        'sla': {'type': 'list', 'options': {'health-check': {'type': 'str'}, 'id': {'type': 'int'}}, 'elements': 'dict'},
                        'src': {'type': 'raw'},
                        'src-negate': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'src6': {'type': 'raw'},
                        'start-port': {'type': 'int'},
                        'status': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'tos': {'type': 'str'},
                        'tos-mask': {'type': 'str'},
                        'users': {'type': 'raw'},
                        'internet-service-app-ctrl': {'v_range': [['6.2.0', '']], 'type': 'raw'},
                        'internet-service-app-ctrl-group': {'v_range': [['6.2.0', '']], 'type': 'raw'},
                        'role': {'v_range': [['6.2.1', '']], 'choices': ['primary', 'secondary', 'standalone'], 'type': 'str'},
                        'sla-compare-method': {'v_range': [['6.2.1', '']], 'choices': ['order', 'number'], 'type': 'str'},
                        'standalone-action': {'v_range': [['6.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'input-device': {'v_range': [['6.2.2', '']], 'type': 'raw'},
                        'internet-service-name': {'v_range': [['6.4.0', '6.4.0']], 'type': 'str'},
                        'input-device-negate': {'v_range': [['6.4.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'}
                    },
                    'elements': 'dict'
                },
                'status': {'choices': ['disable', 'enable'], 'type': 'str'},
                'neighbor': {
                    'v_range': [['6.2.1', '']],
                    'type': 'list',
                    'options': {
                        'health-check': {'v_range': [['6.2.1', '']], 'type': 'str'},
                        'ip': {'v_range': [['6.2.1', '']], 'type': 'str'},
                        'member': {'v_range': [['6.2.1', '']], 'type': 'str'},
                        'role': {'v_range': [['6.2.1', '']], 'choices': ['primary', 'secondary', 'standalone'], 'type': 'str'},
                        'sla-id': {'v_range': [['6.2.1', '']], 'type': 'int'}
                    },
                    'elements': 'dict'
                },
                'neighbor-hold-boot-time': {'v_range': [['6.2.1', '']], 'type': 'int'},
                'neighbor-hold-down': {'v_range': [['6.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'neighbor-hold-down-time': {'v_range': [['6.2.1', '']], 'type': 'int'},
                'fail-alert-interfaces': {'v_range': [['7.2.3', '']], 'type': 'raw'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('partial crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'wanprof_system_virtualwanlink'),
                           supports_check_mode=True)

    if not module._socket_path:
        module.fail_json(msg='MUST RUN IN HTTPAPI MODE')
    connection = Connection(module._socket_path)
    fmgr = NAPIManager(jrpc_urls, perobject_jrpc_urls, module_primary_key, url_params, module, connection, top_level_schema_name='data')
    fmgr.validate_parameters(params_validation_blob)
    fmgr.process_partial_curd(argument_specs=module_arg_spec)

    module.exit_json(meta=module.params)


if __name__ == '__main__':
    main()
