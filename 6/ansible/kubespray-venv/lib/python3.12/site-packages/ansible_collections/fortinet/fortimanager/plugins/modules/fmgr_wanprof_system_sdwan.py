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
module: fmgr_wanprof_system_sdwan
short_description: Configure redundant internet connections using SD-WAN
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
    wanprof_system_sdwan:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            duplication:
                type: list
                elements: dict
                description: Duplication.
                suboptions:
                    dstaddr:
                        type: raw
                        description: (list or str) Destination address or address group names.
                    dstaddr6:
                        type: raw
                        description: (list or str) Destination address6 or address6 group names.
                    dstintf:
                        type: raw
                        description: (list or str) Outgoing
                    id:
                        type: int
                        description: Duplication rule ID
                    packet-de-duplication:
                        type: str
                        description: Deprecated, please rename it to packet_de_duplication. Enable/disable discarding of packets that have been duplicated.
                        choices:
                            - 'disable'
                            - 'enable'
                    packet-duplication:
                        type: str
                        description: Deprecated, please rename it to packet_duplication. Configure packet duplication method.
                        choices:
                            - 'disable'
                            - 'force'
                            - 'on-demand'
                    service:
                        type: raw
                        description: (list or str) Service and service group name.
                    srcaddr:
                        type: raw
                        description: (list or str) Source address or address group names.
                    srcaddr6:
                        type: raw
                        description: (list or str) Source address6 or address6 group names.
                    srcintf:
                        type: raw
                        description: (list or str) Incoming
                    service-id:
                        type: raw
                        description: (list or str) Deprecated, please rename it to service_id. SD-WAN service rule ID list.
                    sla-match-service:
                        type: str
                        description: Deprecated, please rename it to sla_match_service. Enable/disable packet duplication matching health-check SLAs in...
                        choices:
                            - 'disable'
                            - 'enable'
            duplication-max-num:
                type: int
                description: Deprecated, please rename it to duplication_max_num. Maximum number of interface members a packet is duplicated in the SD-...
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
                        description: Deprecated, please rename it to ftp_file. Full path and file name on the FTP server to download for FTP health-che...
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
                        description: Deprecated, please rename it to http_get. URL used to communicate with the server if the protocol if the protocol ...
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
                        description: Deprecated, please rename it to probe_count. Number of most recent probes that should be used to calculate latency...
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
                        description: Deprecated, please rename it to sla_fail_log_period. Time interval in seconds that SLA fail log messages will be g...
                    sla-pass-log-period:
                        type: int
                        description: Deprecated, please rename it to sla_pass_log_period. Time interval in seconds that SLA pass log messages will be g...
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
                    cost:
                        type: int
                        description: Cost of this interface for services in SLA mode
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
                    zone:
                        type: str
                        description: Zone name.
                    priority6:
                        type: int
                        description: Priority of the interface for IPv6
                    preferred-source:
                        type: str
                        description: Deprecated, please rename it to preferred_source. Preferred source of route for this member.
                    transport-group:
                        type: int
                        description: Deprecated, please rename it to transport_group. Measured transport group
                    priority-in-sla:
                        type: int
                        description: Deprecated, please rename it to priority_in_sla. Preferred priority of routes to this member when this member is i...
                    priority-out-sla:
                        type: int
                        description: Deprecated, please rename it to priority_out_sla. Preferred priority of routes to this member when this member is ...
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
                        description: IP/IPv6 address of neighbor.
                    member:
                        type: raw
                        description: (list or str) Member sequence number.
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
                    minimum-sla-meet-members:
                        type: int
                        description: Deprecated, please rename it to minimum_sla_meet_members. Minimum number of members which meet SLA when the neighb...
                    mode:
                        type: str
                        description: What metric to select the neighbor.
                        choices:
                            - 'sla'
                            - 'speedtest'
                    service-id:
                        type: str
                        description: Deprecated, please rename it to service_id. SD-WAN service ID to work with the neighbor.
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
                        description: Deprecated, please rename it to hold_down_time. Waiting period in seconds when switching from the back-up member t...
                    id:
                        type: int
                        description: SD-WAN rule ID
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
                        description: Deprecated, please rename it to internet_service. Enable/disable use of Internet service for application-based loa...
                        choices:
                            - 'disable'
                            - 'enable'
                    internet-service-app-ctrl:
                        type: raw
                        description: (list) Deprecated, please rename it to internet_service_app_ctrl. Application control based Internet Service ID list.
                    internet-service-app-ctrl-group:
                        type: raw
                        description: (list or str) Deprecated, please rename it to internet_service_app_ctrl_group. Application control based Internet ...
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
                        description: Deprecated, please rename it to link_cost_threshold. Percentage threshold change of link cost values that will res...
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
                        description: Deprecated, please rename it to standalone_action. Enable/disable service when selected neighbor role is standalon...
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
                        description: (list) Deprecated, please rename it to internet_service_app_ctrl_category. IDs of one or more application control ...
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
            status:
                type: str
                description: Enable/disable SD-WAN.
                choices:
                    - 'disable'
                    - 'enable'
            zone:
                type: list
                elements: dict
                description: Zone.
                suboptions:
                    name:
                        type: str
                        description: Zone name.
                    service-sla-tie-break:
                        type: str
                        description: Deprecated, please rename it to service_sla_tie_break. Method of selecting member if more than one meets the SLA.
                        choices:
                            - 'cfg-order'
                            - 'fib-best-match'
                            - 'input-device'
                    minimum-sla-meet-members:
                        type: int
                        description: Deprecated, please rename it to minimum_sla_meet_members. Minimum number of members which meet SLA when the neighb...
                    advpn-health-check:
                        type: str
                        description: Deprecated, please rename it to advpn_health_check. Health check for ADVPN local overlay link quality.
                    advpn-select:
                        type: str
                        description: Deprecated, please rename it to advpn_select. Enable/disable selection of ADVPN based on SDWAN information.
                        choices:
                            - 'disable'
                            - 'enable'
            speedtest-bypass-routing:
                type: str
                description: Deprecated, please rename it to speedtest_bypass_routing. Enable/disable bypass routing when speedtest on a SD-WAN member.
                choices:
                    - 'disable'
                    - 'enable'
            fail-alert-interfaces:
                type: raw
                description: (list) Deprecated, please rename it to fail_alert_interfaces. Physical interfaces that will be alerted.
            app-perf-log-period:
                type: int
                description: Deprecated, please rename it to app_perf_log_period. Time interval in seconds that applicationperformance logs are generated
            health-check-fortiguard:
                type: list
                elements: dict
                description: Deprecated, please rename it to health_check_fortiguard. Health check fortiguard.
                suboptions:
                    addr-mode:
                        type: str
                        description: Deprecated, please rename it to addr_mode. Address mode
                        choices:
                            - 'ipv4'
                            - 'ipv6'
                    class-id:
                        type: raw
                        description: (list) Deprecated, please rename it to class_id. Traffic class ID.
                    detect-mode:
                        type: str
                        description: Deprecated, please rename it to detect_mode. The mode determining how to detect the server.
                        choices:
                            - 'active'
                            - 'passive'
                            - 'prefer-passive'
                            - 'remote'
                            - 'agent-based'
                    diffservcode:
                        type: str
                        description: Differentiated services code point
                    dns-match-ip:
                        type: str
                        description: Deprecated, please rename it to dns_match_ip. Response IP expected from DNS server if the protocol is DNS.
                    dns-request-domain:
                        type: str
                        description: Deprecated, please rename it to dns_request_domain. Fully qualified domain name to resolve for the DNS probe.
                    embed-measured-health:
                        type: str
                        description: Deprecated, please rename it to embed_measured_health. Enable/disable embedding measured health information.
                        choices:
                            - 'disable'
                            - 'enable'
                    failtime:
                        type: int
                        description: Number of failures before server is considered lost
                    ftp-file:
                        type: str
                        description: Deprecated, please rename it to ftp_file. Full path and file name on the FTP server to download for FTP health-che...
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
                        description: Deprecated, please rename it to http_get. URL used to communicate with the server if the protocol if the protocol ...
                    http-match:
                        type: str
                        description: Deprecated, please rename it to http_match. Response string expected from the server if the protocol is HTTP.
                    interval:
                        type: int
                        description: Status check interval in milliseconds, or the time between attempting to connect to the server
                    members:
                        type: raw
                        description: (list) Member sequence number list.
                    mos-codec:
                        type: str
                        description: Deprecated, please rename it to mos_codec. Codec to use for MOS calculation
                        choices:
                            - 'g711'
                            - 'g722'
                            - 'g729'
                    packet-size:
                        type: int
                        description: Deprecated, please rename it to packet_size. Packet size of a TWAMP test session.
                    password:
                        type: raw
                        description: (list) TWAMP controller password in authentication mode.
                    port:
                        type: int
                        description: Port number used to communicate with the server over the selected protocol
                    probe-count:
                        type: int
                        description: Deprecated, please rename it to probe_count. Number of most recent probes that should be used to calculate latency...
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
                        description: (list) Predefined IP address or FQDN name from FortiGuard.
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
                            mos-threshold:
                                type: str
                                description: Deprecated, please rename it to mos_threshold. Minimum Mean Opinion Score for SLA to be marked as pass.
                            packetloss-threshold:
                                type: int
                                description: Deprecated, please rename it to packetloss_threshold. Packet loss for SLA to make decision in percentage.
                            priority-in-sla:
                                type: int
                                description: Deprecated, please rename it to priority_in_sla. Value to be distributed into routing table when in-sla
                            priority-out-sla:
                                type: int
                                description: Deprecated, please rename it to priority_out_sla. Value to be distributed into routing table when out-sla
                    sla-fail-log-period:
                        type: int
                        description: Deprecated, please rename it to sla_fail_log_period. Time interval in seconds that SLA fail log messages will be g...
                    sla-id-redistribute:
                        type: int
                        description: Deprecated, please rename it to sla_id_redistribute. Select the ID from the SLA sub-table.
                    sla-pass-log-period:
                        type: int
                        description: Deprecated, please rename it to sla_pass_log_period. Time interval in seconds that SLA pass log messages will be g...
                    source:
                        type: str
                        description: Source IP address used in the health-check packet to the server.
                    source6:
                        type: str
                        description: Source IPv6 address used in the health-check packet to server.
                    system-dns:
                        type: str
                        description: Deprecated, please rename it to system_dns. Enable/disable system DNS as the probe server.
                        choices:
                            - 'disable'
                            - 'enable'
                    target-name:
                        type: str
                        description: Deprecated, please rename it to target_name. Status check or predefined health-check targets name.
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
                    vrf:
                        type: int
                        description: Virtual Routing Forwarding ID.
            option:
                type: list
                elements: str
                description: Option.
                choices:
                    - 'sdwan-overlay'
                    - 'sdwan-manager'
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
      fortinet.fortimanager.fmgr_wanprof_system_sdwan:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        adom: <your own value>
        wanprof: <your own value>
        wanprof_system_sdwan:
          duplication:
            -
              dstaddr: <list or string>
              dstaddr6: <list or string>
              dstintf: <list or string>
              id: <integer>
              packet_de_duplication: <value in [disable, enable]>
              packet_duplication: <value in [disable, force, on-demand]>
              service: <list or string>
              srcaddr: <list or string>
              srcaddr6: <list or string>
              srcintf: <list or string>
              service_id: <list or string>
              sla_match_service: <value in [disable, enable]>
          duplication_max_num: <integer>
          fail_detect: <value in [disable, enable]>
          health_check:
            -
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
          load_balance_mode: <value in [source-ip-based, weight-based, usage-based, ...]>
          members:
            -
              _dynamic_member: <string>
              comment: <string>
              cost: <integer>
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
              zone: <string>
              priority6: <integer>
              preferred_source: <string>
              transport_group: <integer>
              priority_in_sla: <integer>
              priority_out_sla: <integer>
          neighbor:
            -
              health_check: <string>
              ip: <string>
              member: <list or string>
              role: <value in [primary, secondary, standalone]>
              sla_id: <integer>
              minimum_sla_meet_members: <integer>
              mode: <value in [sla, speedtest]>
              service_id: <string>
          neighbor_hold_boot_time: <integer>
          neighbor_hold_down: <value in [disable, enable]>
          neighbor_hold_down_time: <integer>
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
          status: <value in [disable, enable]>
          zone:
            -
              name: <string>
              service_sla_tie_break: <value in [cfg-order, fib-best-match, input-device]>
              minimum_sla_meet_members: <integer>
              advpn_health_check: <string>
              advpn_select: <value in [disable, enable]>
          speedtest_bypass_routing: <value in [disable, enable]>
          fail_alert_interfaces: <list or string>
          app_perf_log_period: <integer>
          health_check_fortiguard:
            -
              addr_mode: <value in [ipv4, ipv6]>
              class_id: <list or string>
              detect_mode: <value in [active, passive, prefer-passive, ...]>
              diffservcode: <string>
              dns_match_ip: <string>
              dns_request_domain: <string>
              embed_measured_health: <value in [disable, enable]>
              failtime: <integer>
              ftp_file: <string>
              ftp_mode: <value in [passive, port]>
              ha_priority: <integer>
              http_agent: <string>
              http_get: <string>
              http_match: <string>
              interval: <integer>
              members: <list or string>
              mos_codec: <value in [g711, g722, g729]>
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
                  mos_threshold: <string>
                  packetloss_threshold: <integer>
                  priority_in_sla: <integer>
                  priority_out_sla: <integer>
              sla_fail_log_period: <integer>
              sla_id_redistribute: <integer>
              sla_pass_log_period: <integer>
              source: <string>
              source6: <string>
              system_dns: <value in [disable, enable]>
              target_name: <string>
              threshold_alert_jitter: <integer>
              threshold_alert_latency: <integer>
              threshold_alert_packetloss: <integer>
              threshold_warning_jitter: <integer>
              threshold_warning_latency: <integer>
              threshold_warning_packetloss: <integer>
              update_cascade_interface: <value in [disable, enable]>
              update_static_route: <value in [disable, enable]>
              user: <string>
              vrf: <integer>
          option:
            - sdwan-overlay
            - sdwan-manager
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
        '/pm/config/adom/{adom}/wanprof/{wanprof}/system/sdwan'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/wanprof/{wanprof}/system/sdwan/{sdwan}'
    ]

    url_params = ['adom', 'wanprof']
    module_primary_key = None
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'wanprof': {'required': True, 'type': 'str'},
        'wanprof_system_sdwan': {
            'type': 'dict',
            'v_range': [['6.4.1', '']],
            'options': {
                'duplication': {
                    'v_range': [['6.4.2', '']],
                    'type': 'list',
                    'options': {
                        'dstaddr': {'v_range': [['6.4.2', '']], 'type': 'raw'},
                        'dstaddr6': {'v_range': [['6.4.2', '']], 'type': 'raw'},
                        'dstintf': {'v_range': [['6.4.2', '']], 'type': 'raw'},
                        'id': {'v_range': [['6.4.2', '']], 'type': 'int'},
                        'packet-de-duplication': {'v_range': [['6.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'packet-duplication': {'v_range': [['6.4.2', '']], 'choices': ['disable', 'force', 'on-demand'], 'type': 'str'},
                        'service': {'v_range': [['6.4.2', '']], 'type': 'raw'},
                        'srcaddr': {'v_range': [['6.4.2', '']], 'type': 'raw'},
                        'srcaddr6': {'v_range': [['6.4.2', '']], 'type': 'raw'},
                        'srcintf': {'v_range': [['6.4.2', '']], 'type': 'raw'},
                        'service-id': {'v_range': [['6.4.3', '']], 'type': 'raw'},
                        'sla-match-service': {'v_range': [['7.2.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'}
                    },
                    'elements': 'dict'
                },
                'duplication-max-num': {'v_range': [['6.4.2', '']], 'type': 'int'},
                'fail-detect': {'v_range': [['6.4.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'health-check': {
                    'v_range': [['6.4.1', '']],
                    'type': 'list',
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
                        'name': {'v_range': [['6.4.1', '']], 'type': 'str'},
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
                        'detect-mode': {
                            'v_range': [['7.0.0', '']],
                            'choices': ['active', 'passive', 'prefer-passive', 'remote', 'agent-based'],
                            'type': 'str'
                        },
                        'mos-codec': {'v_range': [['7.2.0', '']], 'choices': ['g711', 'g722', 'g729'], 'type': 'str'},
                        'source': {'v_range': [['7.2.0', '']], 'type': 'str'},
                        'vrf': {'v_range': [['7.2.0', '']], 'type': 'int'},
                        'embed-measured-health': {'v_range': [['7.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'sla-id-redistribute': {'v_range': [['7.2.1', '']], 'type': 'int'},
                        'class-id': {'v_range': [['7.4.0', '']], 'type': 'str'},
                        'source6': {'v_range': [['7.4.0', '']], 'type': 'str'}
                    },
                    'elements': 'dict'
                },
                'load-balance-mode': {
                    'v_range': [['6.4.1', '']],
                    'choices': ['source-ip-based', 'weight-based', 'usage-based', 'source-dest-ip-based', 'measured-volume-based'],
                    'type': 'str'
                },
                'members': {
                    'v_range': [['6.4.1', '']],
                    'type': 'list',
                    'options': {
                        '_dynamic-member': {'v_range': [['6.4.1', '6.4.14']], 'type': 'str'},
                        'comment': {'v_range': [['6.4.1', '']], 'type': 'str'},
                        'cost': {'v_range': [['6.4.1', '']], 'type': 'int'},
                        'gateway': {'v_range': [['6.4.1', '']], 'type': 'str'},
                        'gateway6': {'v_range': [['6.4.1', '']], 'type': 'str'},
                        'ingress-spillover-threshold': {'v_range': [['6.4.1', '']], 'type': 'int'},
                        'interface': {'v_range': [['6.4.1', '']], 'type': 'str'},
                        'priority': {'v_range': [['6.4.1', '']], 'type': 'int'},
                        'seq-num': {'v_range': [['6.4.1', '']], 'type': 'int'},
                        'source': {'v_range': [['6.4.1', '']], 'type': 'str'},
                        'source6': {'v_range': [['6.4.1', '']], 'type': 'str'},
                        'spillover-threshold': {'v_range': [['6.4.1', '']], 'type': 'int'},
                        'status': {'v_range': [['6.4.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'volume-ratio': {'v_range': [['6.4.1', '']], 'type': 'int'},
                        'weight': {'v_range': [['6.4.1', '']], 'type': 'int'},
                        'zone': {'v_range': [['6.4.1', '']], 'type': 'str'},
                        'priority6': {'v_range': [['7.0.0', '']], 'type': 'int'},
                        'preferred-source': {'v_range': [['7.4.0', '']], 'type': 'str'},
                        'transport-group': {'v_range': [['7.4.2', '']], 'type': 'int'},
                        'priority-in-sla': {'v_range': [['7.6.0', '']], 'type': 'int'},
                        'priority-out-sla': {'v_range': [['7.6.0', '']], 'type': 'int'}
                    },
                    'elements': 'dict'
                },
                'neighbor': {
                    'v_range': [['6.4.1', '']],
                    'type': 'list',
                    'options': {
                        'health-check': {'v_range': [['6.4.1', '']], 'type': 'str'},
                        'ip': {'v_range': [['6.4.1', '']], 'type': 'str'},
                        'member': {'v_range': [['6.4.1', '']], 'type': 'raw'},
                        'role': {'v_range': [['6.4.1', '']], 'choices': ['primary', 'secondary', 'standalone'], 'type': 'str'},
                        'sla-id': {'v_range': [['6.4.1', '']], 'type': 'int'},
                        'minimum-sla-meet-members': {'v_range': [['7.2.0', '']], 'type': 'int'},
                        'mode': {'v_range': [['7.0.1', '']], 'choices': ['sla', 'speedtest'], 'type': 'str'},
                        'service-id': {'v_range': [['7.4.1', '']], 'type': 'str'}
                    },
                    'elements': 'dict'
                },
                'neighbor-hold-boot-time': {'v_range': [['6.4.1', '']], 'type': 'int'},
                'neighbor-hold-down': {'v_range': [['6.4.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'neighbor-hold-down-time': {'v_range': [['6.4.1', '']], 'type': 'int'},
                'service': {
                    'v_range': [['6.4.1', '']],
                    'type': 'list',
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
                        'id': {'v_range': [['6.4.1', '']], 'type': 'int'},
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
                    },
                    'elements': 'dict'
                },
                'status': {'v_range': [['6.4.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'zone': {
                    'v_range': [['6.4.1', '']],
                    'type': 'list',
                    'options': {
                        'name': {'v_range': [['6.4.1', '']], 'type': 'str'},
                        'service-sla-tie-break': {'v_range': [['6.4.3', '']], 'choices': ['cfg-order', 'fib-best-match', 'input-device'], 'type': 'str'},
                        'minimum-sla-meet-members': {'v_range': [['7.4.1', '']], 'type': 'int'},
                        'advpn-health-check': {'v_range': [['7.4.2', '']], 'type': 'str'},
                        'advpn-select': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'}
                    },
                    'elements': 'dict'
                },
                'speedtest-bypass-routing': {'v_range': [['7.0.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'fail-alert-interfaces': {'v_range': [['7.2.3', '']], 'type': 'raw'},
                'app-perf-log-period': {'v_range': [['7.4.0', '']], 'type': 'int'},
                'health-check-fortiguard': {
                    'v_range': [['7.6.0', '']],
                    'type': 'list',
                    'options': {
                        'addr-mode': {'v_range': [['7.6.0', '']], 'choices': ['ipv4', 'ipv6'], 'type': 'str'},
                        'class-id': {'v_range': [['7.6.0', '']], 'type': 'raw'},
                        'detect-mode': {
                            'v_range': [['7.6.0', '']],
                            'choices': ['active', 'passive', 'prefer-passive', 'remote', 'agent-based'],
                            'type': 'str'
                        },
                        'diffservcode': {'v_range': [['7.6.0', '']], 'type': 'str'},
                        'dns-match-ip': {'v_range': [['7.6.0', '']], 'type': 'str'},
                        'dns-request-domain': {'v_range': [['7.6.0', '']], 'type': 'str'},
                        'embed-measured-health': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'failtime': {'v_range': [['7.6.0', '']], 'type': 'int'},
                        'ftp-file': {'v_range': [['7.6.0', '']], 'type': 'str'},
                        'ftp-mode': {'v_range': [['7.6.0', '']], 'choices': ['passive', 'port'], 'type': 'str'},
                        'ha-priority': {'v_range': [['7.6.0', '']], 'type': 'int'},
                        'http-agent': {'v_range': [['7.6.0', '']], 'type': 'str'},
                        'http-get': {'v_range': [['7.6.0', '']], 'type': 'str'},
                        'http-match': {'v_range': [['7.6.0', '']], 'type': 'str'},
                        'interval': {'v_range': [['7.6.0', '']], 'type': 'int'},
                        'members': {'v_range': [['7.6.0', '']], 'type': 'raw'},
                        'mos-codec': {'v_range': [['7.6.0', '']], 'choices': ['g711', 'g722', 'g729'], 'type': 'str'},
                        'packet-size': {'v_range': [['7.6.0', '']], 'type': 'int'},
                        'password': {'v_range': [['7.6.0', '']], 'no_log': True, 'type': 'raw'},
                        'port': {'v_range': [['7.6.0', '']], 'type': 'int'},
                        'probe-count': {'v_range': [['7.6.0', '']], 'type': 'int'},
                        'probe-packets': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'probe-timeout': {'v_range': [['7.6.0', '']], 'type': 'int'},
                        'protocol': {
                            'v_range': [['7.6.0', '']],
                            'choices': ['ping', 'tcp-echo', 'udp-echo', 'http', 'twamp', 'dns', 'tcp-connect', 'ftp', 'https'],
                            'type': 'str'
                        },
                        'quality-measured-method': {'v_range': [['7.6.0', '']], 'choices': ['half-close', 'half-open'], 'type': 'str'},
                        'recoverytime': {'v_range': [['7.6.0', '']], 'type': 'int'},
                        'security-mode': {'v_range': [['7.6.0', '']], 'choices': ['none', 'authentication'], 'type': 'str'},
                        'server': {'v_range': [['7.6.0', '']], 'type': 'raw'},
                        'sla': {
                            'v_range': [['7.6.0', '']],
                            'type': 'list',
                            'options': {
                                'id': {'v_range': [['7.6.0', '']], 'type': 'int'},
                                'jitter-threshold': {'v_range': [['7.6.0', '']], 'type': 'int'},
                                'latency-threshold': {'v_range': [['7.6.0', '']], 'type': 'int'},
                                'link-cost-factor': {
                                    'v_range': [['7.6.0', '']],
                                    'type': 'list',
                                    'choices': ['latency', 'jitter', 'packet-loss', 'mos', 'remote'],
                                    'elements': 'str'
                                },
                                'mos-threshold': {'v_range': [['7.6.0', '']], 'type': 'str'},
                                'packetloss-threshold': {'v_range': [['7.6.0', '']], 'type': 'int'},
                                'priority-in-sla': {'v_range': [['7.6.0', '']], 'type': 'int'},
                                'priority-out-sla': {'v_range': [['7.6.0', '']], 'type': 'int'}
                            },
                            'elements': 'dict'
                        },
                        'sla-fail-log-period': {'v_range': [['7.6.0', '']], 'type': 'int'},
                        'sla-id-redistribute': {'v_range': [['7.6.0', '']], 'type': 'int'},
                        'sla-pass-log-period': {'v_range': [['7.6.0', '']], 'no_log': True, 'type': 'int'},
                        'source': {'v_range': [['7.6.0', '']], 'type': 'str'},
                        'source6': {'v_range': [['7.6.0', '']], 'type': 'str'},
                        'system-dns': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'target-name': {'v_range': [['7.6.0', '']], 'type': 'str'},
                        'threshold-alert-jitter': {'v_range': [['7.6.0', '']], 'type': 'int'},
                        'threshold-alert-latency': {'v_range': [['7.6.0', '']], 'type': 'int'},
                        'threshold-alert-packetloss': {'v_range': [['7.6.0', '']], 'type': 'int'},
                        'threshold-warning-jitter': {'v_range': [['7.6.0', '']], 'type': 'int'},
                        'threshold-warning-latency': {'v_range': [['7.6.0', '']], 'type': 'int'},
                        'threshold-warning-packetloss': {'v_range': [['7.6.0', '']], 'type': 'int'},
                        'update-cascade-interface': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'update-static-route': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'user': {'v_range': [['7.6.0', '']], 'type': 'str'},
                        'vrf': {'v_range': [['7.6.0', '']], 'type': 'int'}
                    },
                    'elements': 'dict'
                },
                'option': {'v_range': [['7.6.0', '']], 'type': 'list', 'choices': ['sdwan-overlay', 'sdwan-manager'], 'elements': 'str'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('partial crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'wanprof_system_sdwan'),
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
