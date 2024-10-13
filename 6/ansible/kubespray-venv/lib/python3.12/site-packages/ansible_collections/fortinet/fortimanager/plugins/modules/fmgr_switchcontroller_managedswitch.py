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
module: fmgr_switchcontroller_managedswitch
short_description: Configure FortiSwitch devices that are managed by this FortiGate.
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
    switchcontroller_managedswitch:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            _platform:
                type: str
                description: Platform.
            description:
                type: str
                description: Description.
            name:
                type: str
                description: Managed-switch name.
            ports:
                type: list
                elements: dict
                description: Ports.
                suboptions:
                    allowed-vlans:
                        type: raw
                        description: (list or str) Deprecated, please rename it to allowed_vlans. Configure switch port tagged vlans
                    allowed-vlans-all:
                        type: str
                        description: Deprecated, please rename it to allowed_vlans_all. Enable/disable all defined vlans on this port.
                        choices:
                            - 'disable'
                            - 'enable'
                    arp-inspection-trust:
                        type: str
                        description: Deprecated, please rename it to arp_inspection_trust. Trusted or untrusted dynamic ARP inspection.
                        choices:
                            - 'untrusted'
                            - 'trusted'
                    bundle:
                        type: str
                        description: Enable/disable Link Aggregation Group
                        choices:
                            - 'disable'
                            - 'enable'
                    description:
                        type: str
                        description: Description for port.
                    dhcp-snoop-option82-trust:
                        type: str
                        description: Deprecated, please rename it to dhcp_snoop_option82_trust. Enable/disable allowance of DHCP with option-82 on untr...
                        choices:
                            - 'disable'
                            - 'enable'
                    dhcp-snooping:
                        type: str
                        description: Deprecated, please rename it to dhcp_snooping. Trusted or untrusted DHCP-snooping interface.
                        choices:
                            - 'trusted'
                            - 'untrusted'
                    discard-mode:
                        type: str
                        description: Deprecated, please rename it to discard_mode. Configure discard mode for port.
                        choices:
                            - 'none'
                            - 'all-untagged'
                            - 'all-tagged'
                    edge-port:
                        type: str
                        description: Deprecated, please rename it to edge_port. Enable/disable this interface as an edge port, bridging connections bet...
                        choices:
                            - 'disable'
                            - 'enable'
                    igmp-snooping:
                        type: str
                        description: Deprecated, please rename it to igmp_snooping. Set IGMP snooping mode for the physical port interface.
                        choices:
                            - 'disable'
                            - 'enable'
                    igmps-flood-reports:
                        type: str
                        description: Deprecated, please rename it to igmps_flood_reports. Enable/disable flooding of IGMP reports to this interface whe...
                        choices:
                            - 'disable'
                            - 'enable'
                    igmps-flood-traffic:
                        type: str
                        description: Deprecated, please rename it to igmps_flood_traffic. Enable/disable flooding of IGMP snooping traffic to this inte...
                        choices:
                            - 'disable'
                            - 'enable'
                    lacp-speed:
                        type: str
                        description: Deprecated, please rename it to lacp_speed. End Link Aggregation Control Protocol
                        choices:
                            - 'slow'
                            - 'fast'
                    learning-limit:
                        type: int
                        description: Deprecated, please rename it to learning_limit. Limit the number of dynamic MAC addresses on this Port
                    lldp-profile:
                        type: str
                        description: Deprecated, please rename it to lldp_profile. LLDP port TLV profile.
                    lldp-status:
                        type: str
                        description: Deprecated, please rename it to lldp_status. LLDP transmit and receive status.
                        choices:
                            - 'disable'
                            - 'rx-only'
                            - 'tx-only'
                            - 'tx-rx'
                    loop-guard:
                        type: str
                        description: Deprecated, please rename it to loop_guard. Enable/disable loop-guard on this interface, an STP optimization used ...
                        choices:
                            - 'disabled'
                            - 'enabled'
                    loop-guard-timeout:
                        type: int
                        description: Deprecated, please rename it to loop_guard_timeout. Loop-guard timeout
                    max-bundle:
                        type: int
                        description: Deprecated, please rename it to max_bundle. Maximum size of LAG bundle
                    mclag:
                        type: str
                        description: Enable/disable multi-chassis link aggregation
                        choices:
                            - 'disable'
                            - 'enable'
                    member-withdrawal-behavior:
                        type: str
                        description: Deprecated, please rename it to member_withdrawal_behavior. Port behavior after it withdraws because of loss of co...
                        choices:
                            - 'forward'
                            - 'block'
                    members:
                        type: raw
                        description: (list) Aggregated LAG bundle interfaces.
                    min-bundle:
                        type: int
                        description: Deprecated, please rename it to min_bundle. Minimum size of LAG bundle
                    mode:
                        type: str
                        description: LACP mode
                        choices:
                            - 'static'
                            - 'lacp-passive'
                            - 'lacp-active'
                    poe-pre-standard-detection:
                        type: str
                        description: Deprecated, please rename it to poe_pre_standard_detection. Enable/disable PoE pre-standard detection.
                        choices:
                            - 'disable'
                            - 'enable'
                    poe-status:
                        type: str
                        description: Deprecated, please rename it to poe_status. Enable/disable PoE status.
                        choices:
                            - 'disable'
                            - 'enable'
                    port-name:
                        type: str
                        description: Deprecated, please rename it to port_name. Switch port name.
                    port-owner:
                        type: str
                        description: Deprecated, please rename it to port_owner. Switch port name.
                    port-security-policy:
                        type: str
                        description: Deprecated, please rename it to port_security_policy. Switch controller authentication policy to apply to this man...
                    port-selection-criteria:
                        type: str
                        description: Deprecated, please rename it to port_selection_criteria. Algorithm for aggregate port selection.
                        choices:
                            - 'src-mac'
                            - 'dst-mac'
                            - 'src-dst-mac'
                            - 'src-ip'
                            - 'dst-ip'
                            - 'src-dst-ip'
                    qos-policy:
                        type: str
                        description: Deprecated, please rename it to qos_policy. Switch controller QoS policy from available options.
                    sample-direction:
                        type: str
                        description: Deprecated, please rename it to sample_direction. SFlow sample direction.
                        choices:
                            - 'rx'
                            - 'tx'
                            - 'both'
                    sflow-counter-interval:
                        type: int
                        description: Deprecated, please rename it to sflow_counter_interval. SFlow sampler counter polling interval
                    sflow-sample-rate:
                        type: int
                        description: Deprecated, please rename it to sflow_sample_rate. SFlow sampler sample rate
                    sflow-sampler:
                        type: str
                        description: Deprecated, please rename it to sflow_sampler. Enable/disable sFlow protocol on this interface.
                        choices:
                            - 'disabled'
                            - 'enabled'
                    stp-bpdu-guard:
                        type: str
                        description: Deprecated, please rename it to stp_bpdu_guard. Enable/disable STP BPDU guard on this interface.
                        choices:
                            - 'disabled'
                            - 'enabled'
                    stp-bpdu-guard-timeout:
                        type: int
                        description: Deprecated, please rename it to stp_bpdu_guard_timeout. BPDU Guard disabling protection
                    stp-root-guard:
                        type: str
                        description: Deprecated, please rename it to stp_root_guard. Enable/disable STP root guard on this interface.
                        choices:
                            - 'disabled'
                            - 'enabled'
                    stp-state:
                        type: str
                        description: Deprecated, please rename it to stp_state. Enable/disable Spanning Tree Protocol
                        choices:
                            - 'disabled'
                            - 'enabled'
                    type:
                        type: str
                        description: Interface type
                        choices:
                            - 'physical'
                            - 'trunk'
                    untagged-vlans:
                        type: raw
                        description: (list or str) Deprecated, please rename it to untagged_vlans. Configure switch port untagged vlans
                    vlan:
                        type: str
                        description: Assign switch ports to a VLAN.
                    export-to-pool-flag:
                        type: int
                        description: Deprecated, please rename it to export_to_pool_flag. Switch controller export port to pool-list.
                    mac-addr:
                        type: str
                        description: Deprecated, please rename it to mac_addr. Port/Trunk MAC.
                    packet-sample-rate:
                        type: int
                        description: Deprecated, please rename it to packet_sample_rate. Packet sampling rate
                    packet-sampler:
                        type: str
                        description: Deprecated, please rename it to packet_sampler. Enable/disable packet sampling on this interface.
                        choices:
                            - 'disabled'
                            - 'enabled'
                    sticky-mac:
                        type: str
                        description: Deprecated, please rename it to sticky_mac. Enable or disable sticky-mac on the interface.
                        choices:
                            - 'disable'
                            - 'enable'
                    storm-control-policy:
                        type: str
                        description: Deprecated, please rename it to storm_control_policy. Switch controller storm control policy from available options.
                    dot1x-enable:
                        type: str
                        description: Deprecated, please rename it to dot1x_enable. Dot1x enable.
                        choices:
                            - 'disable'
                            - 'enable'
                    max-miss-heartbeats:
                        type: int
                        description: Deprecated, please rename it to max_miss_heartbeats. Maximum tolerant missed heartbeats.
                    access-mode:
                        type: str
                        description: Deprecated, please rename it to access_mode. Access mode of the port.
                        choices:
                            - 'normal'
                            - 'nac'
                            - 'dynamic'
                            - 'static'
                    ip-source-guard:
                        type: str
                        description: Deprecated, please rename it to ip_source_guard. Enable/disable IP source guard.
                        choices:
                            - 'disable'
                            - 'enable'
                    mclag-icl-port:
                        type: int
                        description: Deprecated, please rename it to mclag_icl_port. Mclag icl port.
                    p2p-port:
                        type: int
                        description: Deprecated, please rename it to p2p_port. P2p port.
                    aggregator-mode:
                        type: str
                        description: Deprecated, please rename it to aggregator_mode. LACP member select mode.
                        choices:
                            - 'bandwidth'
                            - 'count'
                    rpvst-port:
                        type: str
                        description: Deprecated, please rename it to rpvst_port. Enable/disable inter-operability with rapid PVST on this interface.
                        choices:
                            - 'disabled'
                            - 'enabled'
                    flow-control:
                        type: str
                        description: Deprecated, please rename it to flow_control. Flow control direction.
                        choices:
                            - 'disable'
                            - 'tx'
                            - 'rx'
                            - 'both'
                    media-type:
                        type: str
                        description: Deprecated, please rename it to media_type. Media type.
                    pause-meter:
                        type: int
                        description: Deprecated, please rename it to pause_meter. Configure ingress pause metering rate, in kbps
                    pause-meter-resume:
                        type: str
                        description: Deprecated, please rename it to pause_meter_resume. Resume threshold for resuming traffic on ingress port.
                        choices:
                            - '25%'
                            - '50%'
                            - '75%'
                    trunk-member:
                        type: int
                        description: Deprecated, please rename it to trunk_member. Trunk member.
                    fec-capable:
                        type: int
                        description: Deprecated, please rename it to fec_capable. FEC capable.
                    fec-state:
                        type: str
                        description: Deprecated, please rename it to fec_state. State of forward error correction.
                        choices:
                            - 'disabled'
                            - 'cl74'
                            - 'cl91'
                            - 'detect-by-module'
                    matched-dpp-intf-tags:
                        type: str
                        description: Deprecated, please rename it to matched_dpp_intf_tags. Matched interface tags in the dynamic port policy.
                    matched-dpp-policy:
                        type: str
                        description: Deprecated, please rename it to matched_dpp_policy. Matched child policy in the dynamic port policy.
                    port-policy:
                        type: str
                        description: Deprecated, please rename it to port_policy. Switch controller dynamic port policy from available options.
                    status:
                        type: str
                        description: Switch port admin status
                        choices:
                            - 'down'
                            - 'up'
                    dsl-profile:
                        type: str
                        description: Deprecated, please rename it to dsl_profile. DSL policy configuration.
                    flap-duration:
                        type: int
                        description: Deprecated, please rename it to flap_duration. Period over which flap events are calculated
                    flap-rate:
                        type: int
                        description: Deprecated, please rename it to flap_rate. Number of stage change events needed within flap-duration.
                    flap-timeout:
                        type: int
                        description: Deprecated, please rename it to flap_timeout. Flap guard disabling protection
                    flapguard:
                        type: str
                        description: Enable/disable flap guard.
                        choices:
                            - 'disable'
                            - 'enable'
                    interface-tags:
                        type: raw
                        description: (list or str) Deprecated, please rename it to interface_tags. Tag
                    poe-max-power:
                        type: str
                        description: Deprecated, please rename it to poe_max_power. Poe max power.
                    poe-standard:
                        type: str
                        description: Deprecated, please rename it to poe_standard. Poe standard.
                    igmp-snooping-flood-reports:
                        type: str
                        description: Deprecated, please rename it to igmp_snooping_flood_reports. Enable/disable flooding of IGMP reports to this inter...
                        choices:
                            - 'disable'
                            - 'enable'
                    mcast-snooping-flood-traffic:
                        type: str
                        description: Deprecated, please rename it to mcast_snooping_flood_traffic. Enable/disable flooding of IGMP snooping traffic to ...
                        choices:
                            - 'disable'
                            - 'enable'
                    link-status:
                        type: str
                        description: Deprecated, please rename it to link_status. Link status.
                        choices:
                            - 'down'
                            - 'up'
                    poe-mode-bt-cabable:
                        type: int
                        description: Deprecated, please rename it to poe_mode_bt_cabable. PoE mode IEEE 802.
                    poe-port-mode:
                        type: str
                        description: Deprecated, please rename it to poe_port_mode. Configure PoE port mode.
                        choices:
                            - 'ieee802-3af'
                            - 'ieee802-3at'
                            - 'ieee802-3bt'
                    poe-port-power:
                        type: str
                        description: Deprecated, please rename it to poe_port_power. Configure PoE port power.
                        choices:
                            - 'normal'
                            - 'perpetual'
                            - 'perpetual-fast'
                    poe-port-priority:
                        type: str
                        description: Deprecated, please rename it to poe_port_priority. Configure PoE port priority.
                        choices:
                            - 'critical-priority'
                            - 'high-priority'
                            - 'low-priority'
                            - 'medium-priority'
                    acl-group:
                        type: raw
                        description: (list) Deprecated, please rename it to acl_group. ACL groups on this port.
                    dhcp-snoop-option82-override:
                        type: list
                        elements: dict
                        description: Deprecated, please rename it to dhcp_snoop_option82_override. Dhcp snoop option82 override.
                        suboptions:
                            circuit-id:
                                type: str
                                description: Deprecated, please rename it to circuit_id. Circuit ID string.
                            remote-id:
                                type: str
                                description: Deprecated, please rename it to remote_id. Remote ID string.
                            vlan-name:
                                type: str
                                description: Deprecated, please rename it to vlan_name. DHCP snooping option 82 VLAN.
                    fortiswitch-acls:
                        type: raw
                        description: (list) Deprecated, please rename it to fortiswitch_acls. ACLs on this port.
                    isl-peer-device-sn:
                        type: str
                        description: Deprecated, please rename it to isl_peer_device_sn. Isl peer device sn.
                    authenticated-port:
                        type: int
                        description: Deprecated, please rename it to authenticated_port. Authenticated port.
                    encrypted-port:
                        type: int
                        description: Deprecated, please rename it to encrypted_port. Encrypted port.
                    ptp-status:
                        type: str
                        description: Deprecated, please rename it to ptp_status. Enable/disable PTP policy on this FortiSwitch port.
                        choices:
                            - 'disable'
                            - 'enable'
                    restricted-auth-port:
                        type: int
                        description: Deprecated, please rename it to restricted_auth_port. Restricted auth port.
                    allow-arp-monitor:
                        type: str
                        description: Deprecated, please rename it to allow_arp_monitor. Enable/Disable allow ARP monitor.
                        choices:
                            - 'disable'
                            - 'enable'
                    export-to:
                        type: raw
                        description: (list) Deprecated, please rename it to export_to. Export managed-switch port to a tenant VDOM.
                    export-to-pool:
                        type: raw
                        description: (list) Deprecated, please rename it to export_to_pool. Switch controller export port to pool-list.
                    fallback-port:
                        type: str
                        description: Deprecated, please rename it to fallback_port. LACP fallback port.
                    fgt-peer-device-name:
                        type: str
                        description: Deprecated, please rename it to fgt_peer_device_name. Fgt peer device name.
                    fgt-peer-port-name:
                        type: str
                        description: Deprecated, please rename it to fgt_peer_port_name. Fgt peer port name.
                    fiber-port:
                        type: int
                        description: Deprecated, please rename it to fiber_port. Fiber port.
                    flags:
                        type: int
                        description: Flags.
                    fortilink-port:
                        type: int
                        description: Deprecated, please rename it to fortilink_port. Fortilink port.
                    isl-local-trunk-name:
                        type: str
                        description: Deprecated, please rename it to isl_local_trunk_name. Isl local trunk name.
                    isl-peer-device-name:
                        type: str
                        description: Deprecated, please rename it to isl_peer_device_name. Isl peer device name.
                    isl-peer-port-name:
                        type: str
                        description: Deprecated, please rename it to isl_peer_port_name. Isl peer port name.
                    poe-capable:
                        type: int
                        description: Deprecated, please rename it to poe_capable. PoE capable.
                    port-number:
                        type: int
                        description: Deprecated, please rename it to port_number. Port number.
                    port-prefix-type:
                        type: int
                        description: Deprecated, please rename it to port_prefix_type. Port prefix type.
                    ptp-policy:
                        type: raw
                        description: (list) Deprecated, please rename it to ptp_policy. PTP policy configuration.
                    speed:
                        type: str
                        description: Switch port speed; default and available settings depend on hardware.
                        choices:
                            - 'auto'
                            - '10full'
                            - '10half'
                            - '100full'
                            - '100half'
                            - '1000full'
                            - '10000full'
                            - '1000auto'
                            - '40000full'
                            - '1000fiber'
                            - '10000'
                            - '40000'
                            - 'auto-module'
                            - '100FX-half'
                            - '100FX-full'
                            - '100000full'
                            - '2500full'
                            - '25000full'
                            - '50000full'
                            - '40000auto'
                            - '10000cr'
                            - '10000sr'
                            - '100000sr4'
                            - '100000cr4'
                            - '25000cr4'
                            - '25000sr4'
                            - '5000full'
                            - '2500auto'
                            - '5000auto'
                            - '1000full-fiber'
                            - '40000sr4'
                            - '40000cr4'
                            - '25000cr'
                            - '25000sr'
                            - '50000cr'
                            - '50000sr'
                    speed-mask:
                        type: int
                        description: Deprecated, please rename it to speed_mask. Switch port speed mask.
                    stacking-port:
                        type: int
                        description: Deprecated, please rename it to stacking_port. Stacking port.
                    switch-id:
                        type: str
                        description: Deprecated, please rename it to switch_id. Switch id.
                    virtual-port:
                        type: int
                        description: Deprecated, please rename it to virtual_port. Virtualized switch port.
                    export-tags:
                        type: raw
                        description: (list) Deprecated, please rename it to export_tags. Configure export tag
                    log-mac-event:
                        type: str
                        description: Deprecated, please rename it to log_mac_event. Enable/disable logging for dynamic MAC address events.
                        choices:
                            - 'disable'
                            - 'enable'
                    pd-capable:
                        type: int
                        description: Deprecated, please rename it to pd_capable. Powered device capable.
                    qnq:
                        type: raw
                        description: (list) '802.'
            switch-id:
                type: str
                description: Deprecated, please rename it to switch_id. Managed-switch id.
                required: true
            override-snmp-community:
                type: str
                description: Deprecated, please rename it to override_snmp_community. Enable/disable overriding the global SNMP communities.
                choices:
                    - 'disable'
                    - 'enable'
            override-snmp-sysinfo:
                type: str
                description: Deprecated, please rename it to override_snmp_sysinfo. Enable/disable overriding the global SNMP system information.
                choices:
                    - 'disable'
                    - 'enable'
            override-snmp-trap-threshold:
                type: str
                description: Deprecated, please rename it to override_snmp_trap_threshold. Enable/disable overriding the global SNMP trap threshold values.
                choices:
                    - 'disable'
                    - 'enable'
            override-snmp-user:
                type: str
                description: Deprecated, please rename it to override_snmp_user. Enable/disable overriding the global SNMP users.
                choices:
                    - 'disable'
                    - 'enable'
            poe-detection-type:
                type: int
                description: Deprecated, please rename it to poe_detection_type. Poe detection type.
            remote-log:
                type: list
                elements: dict
                description: Deprecated, please rename it to remote_log. Remote log.
                suboptions:
                    csv:
                        type: str
                        description: Enable/disable comma-separated value
                        choices:
                            - 'disable'
                            - 'enable'
                    facility:
                        type: str
                        description: Facility to log to remote syslog server.
                        choices:
                            - 'kernel'
                            - 'user'
                            - 'mail'
                            - 'daemon'
                            - 'auth'
                            - 'syslog'
                            - 'lpr'
                            - 'news'
                            - 'uucp'
                            - 'cron'
                            - 'authpriv'
                            - 'ftp'
                            - 'ntp'
                            - 'audit'
                            - 'alert'
                            - 'clock'
                            - 'local0'
                            - 'local1'
                            - 'local2'
                            - 'local3'
                            - 'local4'
                            - 'local5'
                            - 'local6'
                            - 'local7'
                    name:
                        type: str
                        description: Remote log name.
                    port:
                        type: int
                        description: Remote syslog server listening port.
                    server:
                        type: str
                        description: IPv4 address of the remote syslog server.
                    severity:
                        type: str
                        description: Severity of logs to be transferred to remote log server.
                        choices:
                            - 'emergency'
                            - 'alert'
                            - 'critical'
                            - 'error'
                            - 'warning'
                            - 'notification'
                            - 'information'
                            - 'debug'
                    status:
                        type: str
                        description: Enable/disable logging by FortiSwitch device to a remote syslog server.
                        choices:
                            - 'disable'
                            - 'enable'
            snmp-community:
                type: list
                elements: dict
                description: Deprecated, please rename it to snmp_community. Snmp community.
                suboptions:
                    events:
                        type: list
                        elements: str
                        description: SNMP notifications
                        choices:
                            - 'cpu-high'
                            - 'mem-low'
                            - 'log-full'
                            - 'intf-ip'
                            - 'ent-conf-change'
                            - 'l2mac'
                    hosts:
                        type: list
                        elements: dict
                        description: Hosts.
                        suboptions:
                            id:
                                type: int
                                description: Host entry ID.
                            ip:
                                type: str
                                description: IPv4 address of the SNMP manager
                    id:
                        type: int
                        description: SNMP community ID.
                    name:
                        type: str
                        description: SNMP community name.
                    query-v1-port:
                        type: int
                        description: Deprecated, please rename it to query_v1_port. SNMP v1 query port
                    query-v1-status:
                        type: str
                        description: Deprecated, please rename it to query_v1_status. Enable/disable SNMP v1 queries.
                        choices:
                            - 'disable'
                            - 'enable'
                    query-v2c-port:
                        type: int
                        description: Deprecated, please rename it to query_v2c_port. SNMP v2c query port
                    query-v2c-status:
                        type: str
                        description: Deprecated, please rename it to query_v2c_status. Enable/disable SNMP v2c queries.
                        choices:
                            - 'disable'
                            - 'enable'
                    status:
                        type: str
                        description: Enable/disable this SNMP community.
                        choices:
                            - 'disable'
                            - 'enable'
                    trap-v1-lport:
                        type: int
                        description: Deprecated, please rename it to trap_v1_lport. SNMP v2c trap local port
                    trap-v1-rport:
                        type: int
                        description: Deprecated, please rename it to trap_v1_rport. SNMP v2c trap remote port
                    trap-v1-status:
                        type: str
                        description: Deprecated, please rename it to trap_v1_status. Enable/disable SNMP v1 traps.
                        choices:
                            - 'disable'
                            - 'enable'
                    trap-v2c-lport:
                        type: int
                        description: Deprecated, please rename it to trap_v2c_lport. SNMP v2c trap local port
                    trap-v2c-rport:
                        type: int
                        description: Deprecated, please rename it to trap_v2c_rport. SNMP v2c trap remote port
                    trap-v2c-status:
                        type: str
                        description: Deprecated, please rename it to trap_v2c_status. Enable/disable SNMP v2c traps.
                        choices:
                            - 'disable'
                            - 'enable'
            snmp-user:
                type: list
                elements: dict
                description: Deprecated, please rename it to snmp_user. Snmp user.
                suboptions:
                    auth-proto:
                        type: str
                        description: Deprecated, please rename it to auth_proto. Authentication protocol.
                        choices:
                            - 'md5'
                            - 'sha'
                            - 'sha1'
                            - 'sha256'
                            - 'sha384'
                            - 'sha512'
                            - 'sha224'
                    auth-pwd:
                        type: raw
                        description: (list) Deprecated, please rename it to auth_pwd. Password for authentication protocol.
                    name:
                        type: str
                        description: SNMP user name.
                    priv-proto:
                        type: str
                        description: Deprecated, please rename it to priv_proto. Privacy
                        choices:
                            - 'des'
                            - 'aes'
                            - 'aes128'
                            - 'aes192'
                            - 'aes256'
                            - 'aes192c'
                            - 'aes256c'
                    priv-pwd:
                        type: raw
                        description: (list) Deprecated, please rename it to priv_pwd. Password for privacy
                    queries:
                        type: str
                        description: Enable/disable SNMP queries for this user.
                        choices:
                            - 'disable'
                            - 'enable'
                    query-port:
                        type: int
                        description: Deprecated, please rename it to query_port. SNMPv3 query port
                    security-level:
                        type: str
                        description: Deprecated, please rename it to security_level. Security level for message authentication and encryption.
                        choices:
                            - 'no-auth-no-priv'
                            - 'auth-no-priv'
                            - 'auth-priv'
            mclag-igmp-snooping-aware:
                type: str
                description: Deprecated, please rename it to mclag_igmp_snooping_aware. Enable/disable MCLAG IGMP-snooping awareness.
                choices:
                    - 'disable'
                    - 'enable'
            ip-source-guard:
                type: list
                elements: dict
                description: Deprecated, please rename it to ip_source_guard. Ip source guard.
                suboptions:
                    binding-entry:
                        type: list
                        elements: dict
                        description: Deprecated, please rename it to binding_entry. Binding entry.
                        suboptions:
                            entry-name:
                                type: str
                                description: Deprecated, please rename it to entry_name. Configure binding pair.
                            ip:
                                type: str
                                description: Source IP for this rule.
                            mac:
                                type: str
                                description: MAC address for this rule.
                    description:
                        type: str
                        description: Description.
                    port:
                        type: str
                        description: Ingress interface to which source guard is bound.
            l3-discovered:
                type: int
                description: Deprecated, please rename it to l3_discovered. L3 discovered.
            qos-drop-policy:
                type: str
                description: Deprecated, please rename it to qos_drop_policy. Set QoS drop-policy.
                choices:
                    - 'taildrop'
                    - 'random-early-detection'
            qos-red-probability:
                type: int
                description: Deprecated, please rename it to qos_red_probability. Set QoS RED/WRED drop probability.
            switch-dhcp_opt43_key:
                type: str
                description: Deprecated, please rename it to switch_dhcp_opt43_key. DHCP option43 key.
            tdr-supported:
                type: str
                description: Deprecated, please rename it to tdr_supported. Tdr supported.
            custom-command:
                type: list
                elements: dict
                description: Deprecated, please rename it to custom_command. Custom command.
                suboptions:
                    command-entry:
                        type: str
                        description: Deprecated, please rename it to command_entry. List of FortiSwitch commands.
                    command-name:
                        type: str
                        description: Deprecated, please rename it to command_name. Names of commands to be pushed to this FortiSwitch device, as config...
            firmware-provision:
                type: str
                description: Deprecated, please rename it to firmware_provision. Enable/disable provisioning of firmware to FortiSwitches on join conne...
                choices:
                    - 'disable'
                    - 'enable'
            firmware-provision-version:
                type: str
                description: Deprecated, please rename it to firmware_provision_version. Firmware version to provision to this FortiSwitch on bootup
            dhcp-server-access-list:
                type: str
                description: Deprecated, please rename it to dhcp_server_access_list. DHCP snooping server access list.
                choices:
                    - 'disable'
                    - 'enable'
                    - 'global'
            firmware-provision-latest:
                type: str
                description: Deprecated, please rename it to firmware_provision_latest. Enable/disable one-time automatic provisioning of the latest fi...
                choices:
                    - 'disable'
                    - 'once'
            dhcp-snooping-static-client:
                type: list
                elements: dict
                description: Deprecated, please rename it to dhcp_snooping_static_client. Dhcp snooping static client.
                suboptions:
                    ip:
                        type: str
                        description: Client static IP address.
                    mac:
                        type: str
                        description: Client MAC address.
                    name:
                        type: str
                        description: Client name.
                    port:
                        type: str
                        description: Interface name.
                    vlan:
                        type: str
                        description: VLAN name.
            ptp-profile:
                type: str
                description: Deprecated, please rename it to ptp_profile. PTP profile configuration.
            ptp-status:
                type: str
                description: Deprecated, please rename it to ptp_status. Enable/disable PTP profile on this FortiSwitch.
                choices:
                    - 'disable'
                    - 'enable'
            route-offload:
                type: str
                description: Deprecated, please rename it to route_offload. Enable/disable route offload on this FortiSwitch.
                choices:
                    - 'disable'
                    - 'enable'
            route-offload-mclag:
                type: str
                description: Deprecated, please rename it to route_offload_mclag. Enable/disable route offload MCLAG on this FortiSwitch.
                choices:
                    - 'disable'
                    - 'enable'
            route-offload-router:
                type: list
                elements: dict
                description: Deprecated, please rename it to route_offload_router. Route offload router.
                suboptions:
                    router-ip:
                        type: str
                        description: Deprecated, please rename it to router_ip. Router IP address.
                    vlan-name:
                        type: str
                        description: Deprecated, please rename it to vlan_name. VLAN name.
            mgmt-mode:
                type: int
                description: Deprecated, please rename it to mgmt_mode. FortiLink management mode.
            purdue-level:
                type: str
                description: Deprecated, please rename it to purdue_level. Purdue Level of this FortiSwitch.
                choices:
                    - '1'
                    - '2'
                    - '3'
                    - '4'
                    - '5'
                    - '1.5'
                    - '2.5'
                    - '3.5'
                    - '5.5'
            radius-nas-ip:
                type: str
                description: Deprecated, please rename it to radius_nas_ip. NAS-IP address.
            radius-nas-ip-override:
                type: str
                description: Deprecated, please rename it to radius_nas_ip_override. Use locally defined NAS-IP.
                choices:
                    - 'disable'
                    - 'enable'
            tunnel-discovered:
                type: int
                description: Deprecated, please rename it to tunnel_discovered. Tunnel discovered.
            vlan:
                type: list
                elements: dict
                description: Vlan.
                suboptions:
                    assignment-priority:
                        type: int
                        description: Deprecated, please rename it to assignment_priority. '802.'
                    vlan-name:
                        type: str
                        description: Deprecated, please rename it to vlan_name. VLAN name.
            802-1X-settings:
                type: dict
                description: Deprecated, please rename it to 802_1X_settings. 802 1X settings.
                suboptions:
                    link-down-auth:
                        type: str
                        description: Deprecated, please rename it to link_down_auth. Authentication state to set if a link is down.
                        choices:
                            - 'set-unauth'
                            - 'no-action'
                    local-override:
                        type: str
                        description: Deprecated, please rename it to local_override. Enable to override global 802.
                        choices:
                            - 'disable'
                            - 'enable'
                    mab-reauth:
                        type: str
                        description: Deprecated, please rename it to mab_reauth. Enable or disable MAB reauthentication settings.
                        choices:
                            - 'disable'
                            - 'enable'
                    mac-called-station-delimiter:
                        type: str
                        description: Deprecated, please rename it to mac_called_station_delimiter. MAC called station delimiter
                        choices:
                            - 'hyphen'
                            - 'single-hyphen'
                            - 'colon'
                            - 'none'
                    mac-calling-station-delimiter:
                        type: str
                        description: Deprecated, please rename it to mac_calling_station_delimiter. MAC calling station delimiter
                        choices:
                            - 'hyphen'
                            - 'single-hyphen'
                            - 'colon'
                            - 'none'
                    mac-case:
                        type: str
                        description: Deprecated, please rename it to mac_case. MAC case
                        choices:
                            - 'uppercase'
                            - 'lowercase'
                    mac-password-delimiter:
                        type: str
                        description: Deprecated, please rename it to mac_password_delimiter. MAC authentication password delimiter
                        choices:
                            - 'hyphen'
                            - 'single-hyphen'
                            - 'colon'
                            - 'none'
                    mac-username-delimiter:
                        type: str
                        description: Deprecated, please rename it to mac_username_delimiter. MAC authentication username delimiter
                        choices:
                            - 'hyphen'
                            - 'single-hyphen'
                            - 'colon'
                            - 'none'
                    max-reauth-attempt:
                        type: int
                        description: Deprecated, please rename it to max_reauth_attempt. Maximum number of authentication attempts
                    reauth-period:
                        type: int
                        description: Deprecated, please rename it to reauth_period. Reauthentication time interval
                    tx-period:
                        type: int
                        description: Deprecated, please rename it to tx_period. '802.'
            access-profile:
                type: raw
                description: (list) Deprecated, please rename it to access_profile. FortiSwitch access profile.
            delayed-restart-trigger:
                type: int
                description: Deprecated, please rename it to delayed_restart_trigger. Delayed restart triggered for this FortiSwitch.
            directly-connected:
                type: int
                description: Deprecated, please rename it to directly_connected. Directly connected.
            dynamic-capability:
                type: str
                description: Deprecated, please rename it to dynamic_capability. List of features this FortiSwitch supports
            dynamically-discovered:
                type: int
                description: Deprecated, please rename it to dynamically_discovered. Dynamically discovered.
            flow-identity:
                type: str
                description: Deprecated, please rename it to flow_identity. Flow-tracking netflow ipfix switch identity in hex format
            fsw-wan1-admin:
                type: str
                description: Deprecated, please rename it to fsw_wan1_admin. FortiSwitch WAN1 admin status; enable to authorize the FortiSwitch as a ma...
                choices:
                    - 'disable'
                    - 'enable'
                    - 'discovered'
            fsw-wan1-peer:
                type: raw
                description: (list) Deprecated, please rename it to fsw_wan1_peer. FortiSwitch WAN1 peer port.
            fsw-wan2-admin:
                type: str
                description: Deprecated, please rename it to fsw_wan2_admin. FortiSwitch WAN2 admin status; enable to authorize the FortiSwitch as a ma...
                choices:
                    - 'disable'
                    - 'enable'
                    - 'discovered'
            fsw-wan2-peer:
                type: str
                description: Deprecated, please rename it to fsw_wan2_peer. FortiSwitch WAN2 peer port.
            igmp-snooping:
                type: dict
                description: Deprecated, please rename it to igmp_snooping. Igmp snooping.
                suboptions:
                    aging-time:
                        type: int
                        description: Deprecated, please rename it to aging_time. Maximum time to retain a multicast snooping entry for which no packets...
                    flood-unknown-multicast:
                        type: str
                        description: Deprecated, please rename it to flood_unknown_multicast. Enable/disable unknown multicast flooding.
                        choices:
                            - 'disable'
                            - 'enable'
                    local-override:
                        type: str
                        description: Deprecated, please rename it to local_override. Enable/disable overriding the global IGMP snooping configuration.
                        choices:
                            - 'disable'
                            - 'enable'
                    vlans:
                        type: list
                        elements: dict
                        description: Vlans.
                        suboptions:
                            proxy:
                                type: str
                                description: IGMP snooping proxy for the VLAN interface.
                                choices:
                                    - 'disable'
                                    - 'enable'
                                    - 'global'
                            querier:
                                type: str
                                description: Enable/disable IGMP snooping querier for the VLAN interface.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            querier-addr:
                                type: str
                                description: Deprecated, please rename it to querier_addr. IGMP snooping querier address.
                            version:
                                type: int
                                description: IGMP snooping querying version.
                            vlan-name:
                                type: raw
                                description: (list) Deprecated, please rename it to vlan_name. List of FortiSwitch VLANs.
            max-allowed-trunk-members:
                type: int
                description: Deprecated, please rename it to max_allowed_trunk_members. FortiSwitch maximum allowed trunk members.
            mirror:
                type: list
                elements: dict
                description: Mirror.
                suboptions:
                    dst:
                        type: str
                        description: Destination port.
                    name:
                        type: str
                        description: Mirror name.
                    src-egress:
                        type: raw
                        description: (list) Deprecated, please rename it to src_egress. Source egress interfaces.
                    src-ingress:
                        type: raw
                        description: (list) Deprecated, please rename it to src_ingress. Source ingress interfaces.
                    status:
                        type: str
                        description: Active/inactive mirror configuration.
                        choices:
                            - 'inactive'
                            - 'active'
                    switching-packet:
                        type: str
                        description: Deprecated, please rename it to switching_packet. Enable/disable switching functionality when mirroring.
                        choices:
                            - 'disable'
                            - 'enable'
            owner-vdom:
                type: str
                description: Deprecated, please rename it to owner_vdom. VDOM which owner of port belongs to.
            poe-pre-standard-detection:
                type: str
                description: Deprecated, please rename it to poe_pre_standard_detection. Enable/disable PoE pre-standard detection.
                choices:
                    - 'disable'
                    - 'enable'
            pre-provisioned:
                type: int
                description: Deprecated, please rename it to pre_provisioned. Pre-provisioned managed switch.
            sn:
                type: str
                description: Managed-switch serial number.
            snmp-sysinfo:
                type: dict
                description: Deprecated, please rename it to snmp_sysinfo. Snmp sysinfo.
                suboptions:
                    contact-info:
                        type: str
                        description: Deprecated, please rename it to contact_info. Contact information.
                    description:
                        type: str
                        description: System description.
                    engine-id:
                        type: str
                        description: Deprecated, please rename it to engine_id. Local SNMP engine ID string
                    location:
                        type: str
                        description: System location.
                    status:
                        type: str
                        description: Enable/disable SNMP.
                        choices:
                            - 'disable'
                            - 'enable'
            snmp-trap-threshold:
                type: dict
                description: Deprecated, please rename it to snmp_trap_threshold. Snmp trap threshold.
                suboptions:
                    trap-high-cpu-threshold:
                        type: int
                        description: Deprecated, please rename it to trap_high_cpu_threshold. CPU usage when trap is sent.
                    trap-log-full-threshold:
                        type: int
                        description: Deprecated, please rename it to trap_log_full_threshold. Log disk usage when trap is sent.
                    trap-low-memory-threshold:
                        type: int
                        description: Deprecated, please rename it to trap_low_memory_threshold. Memory usage when trap is sent.
            staged-image-version:
                type: str
                description: Deprecated, please rename it to staged_image_version. Staged image version for FortiSwitch.
            static-mac:
                type: list
                elements: dict
                description: Deprecated, please rename it to static_mac. Static mac.
                suboptions:
                    description:
                        type: str
                        description: Description.
                    id:
                        type: int
                        description: ID.
                    interface:
                        type: str
                        description: Interface name.
                    mac:
                        type: str
                        description: MAC address.
                    type:
                        type: str
                        description: Type.
                        choices:
                            - 'static'
                            - 'sticky'
                    vlan:
                        type: raw
                        description: (list) Vlan.
            storm-control:
                type: dict
                description: Deprecated, please rename it to storm_control. Storm control.
                suboptions:
                    broadcast:
                        type: str
                        description: Enable/disable storm control to drop broadcast traffic.
                        choices:
                            - 'disable'
                            - 'enable'
                    local-override:
                        type: str
                        description: Deprecated, please rename it to local_override. Enable to override global FortiSwitch storm control settings for t...
                        choices:
                            - 'disable'
                            - 'enable'
                    rate:
                        type: int
                        description: Rate in packets per second at which storm control drops excess traffic
                    unknown-multicast:
                        type: str
                        description: Deprecated, please rename it to unknown_multicast. Enable/disable storm control to drop unknown multicast traffic.
                        choices:
                            - 'disable'
                            - 'enable'
                    unknown-unicast:
                        type: str
                        description: Deprecated, please rename it to unknown_unicast. Enable/disable storm control to drop unknown unicast traffic.
                        choices:
                            - 'disable'
                            - 'enable'
            stp-instance:
                type: list
                elements: dict
                description: Deprecated, please rename it to stp_instance. Stp instance.
                suboptions:
                    id:
                        type: str
                        description: Instance ID.
                    priority:
                        type: str
                        description: Priority.
                        choices:
                            - '0'
                            - '4096'
                            - '8192'
                            - '12288'
                            - '12328'
                            - '16384'
                            - '20480'
                            - '24576'
                            - '28672'
                            - '32768'
                            - '36864'
                            - '40960'
                            - '45056'
                            - '49152'
                            - '53248'
                            - '57344'
                            - '61440'
            stp-settings:
                type: dict
                description: Deprecated, please rename it to stp_settings. Stp settings.
                suboptions:
                    forward-time:
                        type: int
                        description: Deprecated, please rename it to forward_time. Period of time a port is in listening and learning state
                    hello-time:
                        type: int
                        description: Deprecated, please rename it to hello_time. Period of time between successive STP frame Bridge Protocol Data Units
                    local-override:
                        type: str
                        description: Deprecated, please rename it to local_override. Enable to configure local STP settings that override global STP se...
                        choices:
                            - 'disable'
                            - 'enable'
                    max-age:
                        type: int
                        description: Deprecated, please rename it to max_age. Maximum time before a bridge port saves its configuration BPDU information
                    max-hops:
                        type: int
                        description: Deprecated, please rename it to max_hops. Maximum number of hops between the root bridge and the furthest bridge
                    name:
                        type: str
                        description: Name of local STP settings configuration.
                    pending-timer:
                        type: int
                        description: Deprecated, please rename it to pending_timer. Pending time
                    revision:
                        type: int
                        description: STP revision number
                    status:
                        type: str
                        description: Enable/disable STP.
                        choices:
                            - 'disable'
                            - 'enable'
            switch-device-tag:
                type: str
                description: Deprecated, please rename it to switch_device_tag. User definable label/tag.
            switch-log:
                type: dict
                description: Deprecated, please rename it to switch_log. Switch log.
                suboptions:
                    local-override:
                        type: str
                        description: Deprecated, please rename it to local_override. Enable to configure local logging settings that override global lo...
                        choices:
                            - 'disable'
                            - 'enable'
                    severity:
                        type: str
                        description: Severity of FortiSwitch logs that are added to the FortiGate event log.
                        choices:
                            - 'emergency'
                            - 'alert'
                            - 'critical'
                            - 'error'
                            - 'warning'
                            - 'notification'
                            - 'information'
                            - 'debug'
                    status:
                        type: str
                        description: Enable/disable adding FortiSwitch logs to the FortiGate event log.
                        choices:
                            - 'disable'
                            - 'enable'
            switch-profile:
                type: raw
                description: (list) Deprecated, please rename it to switch_profile. FortiSwitch profile.
            type:
                type: str
                description: Indication of switch type, physical or virtual.
                choices:
                    - 'physical'
                    - 'virtual'
            version:
                type: int
                description: FortiSwitch version.
            poe-lldp-detection:
                type: str
                description: Deprecated, please rename it to poe_lldp_detection. Enable/disable PoE LLDP detection.
                choices:
                    - 'disable'
                    - 'enable'
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
    - name: Configure FortiSwitch devices that are managed by this FortiGate.
      fortinet.fortimanager.fmgr_switchcontroller_managedswitch:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: present # <value in [present, absent]>
        switchcontroller_managedswitch:
          _platform: <string>
          description: <string>
          name: <string>
          ports:
            -
              allowed_vlans: <list or string>
              allowed_vlans_all: <value in [disable, enable]>
              arp_inspection_trust: <value in [untrusted, trusted]>
              bundle: <value in [disable, enable]>
              description: <string>
              dhcp_snoop_option82_trust: <value in [disable, enable]>
              dhcp_snooping: <value in [trusted, untrusted]>
              discard_mode: <value in [none, all-untagged, all-tagged]>
              edge_port: <value in [disable, enable]>
              igmp_snooping: <value in [disable, enable]>
              igmps_flood_reports: <value in [disable, enable]>
              igmps_flood_traffic: <value in [disable, enable]>
              lacp_speed: <value in [slow, fast]>
              learning_limit: <integer>
              lldp_profile: <string>
              lldp_status: <value in [disable, rx-only, tx-only, ...]>
              loop_guard: <value in [disabled, enabled]>
              loop_guard_timeout: <integer>
              max_bundle: <integer>
              mclag: <value in [disable, enable]>
              member_withdrawal_behavior: <value in [forward, block]>
              members: <list or string>
              min_bundle: <integer>
              mode: <value in [static, lacp-passive, lacp-active]>
              poe_pre_standard_detection: <value in [disable, enable]>
              poe_status: <value in [disable, enable]>
              port_name: <string>
              port_owner: <string>
              port_security_policy: <string>
              port_selection_criteria: <value in [src-mac, dst-mac, src-dst-mac, ...]>
              qos_policy: <string>
              sample_direction: <value in [rx, tx, both]>
              sflow_counter_interval: <integer>
              sflow_sample_rate: <integer>
              sflow_sampler: <value in [disabled, enabled]>
              stp_bpdu_guard: <value in [disabled, enabled]>
              stp_bpdu_guard_timeout: <integer>
              stp_root_guard: <value in [disabled, enabled]>
              stp_state: <value in [disabled, enabled]>
              type: <value in [physical, trunk]>
              untagged_vlans: <list or string>
              vlan: <string>
              export_to_pool_flag: <integer>
              mac_addr: <string>
              packet_sample_rate: <integer>
              packet_sampler: <value in [disabled, enabled]>
              sticky_mac: <value in [disable, enable]>
              storm_control_policy: <string>
              dot1x_enable: <value in [disable, enable]>
              max_miss_heartbeats: <integer>
              access_mode: <value in [normal, nac, dynamic, ...]>
              ip_source_guard: <value in [disable, enable]>
              mclag_icl_port: <integer>
              p2p_port: <integer>
              aggregator_mode: <value in [bandwidth, count]>
              rpvst_port: <value in [disabled, enabled]>
              flow_control: <value in [disable, tx, rx, ...]>
              media_type: <string>
              pause_meter: <integer>
              pause_meter_resume: <value in [25%, 50%, 75%]>
              trunk_member: <integer>
              fec_capable: <integer>
              fec_state: <value in [disabled, cl74, cl91, ...]>
              matched_dpp_intf_tags: <string>
              matched_dpp_policy: <string>
              port_policy: <string>
              status: <value in [down, up]>
              dsl_profile: <string>
              flap_duration: <integer>
              flap_rate: <integer>
              flap_timeout: <integer>
              flapguard: <value in [disable, enable]>
              interface_tags: <list or string>
              poe_max_power: <string>
              poe_standard: <string>
              igmp_snooping_flood_reports: <value in [disable, enable]>
              mcast_snooping_flood_traffic: <value in [disable, enable]>
              link_status: <value in [down, up]>
              poe_mode_bt_cabable: <integer>
              poe_port_mode: <value in [ieee802-3af, ieee802-3at, ieee802-3bt]>
              poe_port_power: <value in [normal, perpetual, perpetual-fast]>
              poe_port_priority: <value in [critical-priority, high-priority, low-priority, ...]>
              acl_group: <list or string>
              dhcp_snoop_option82_override:
                -
                  circuit_id: <string>
                  remote_id: <string>
                  vlan_name: <string>
              fortiswitch_acls: <list or integer>
              isl_peer_device_sn: <string>
              authenticated_port: <integer>
              encrypted_port: <integer>
              ptp_status: <value in [disable, enable]>
              restricted_auth_port: <integer>
              allow_arp_monitor: <value in [disable, enable]>
              export_to: <list or string>
              export_to_pool: <list or string>
              fallback_port: <string>
              fgt_peer_device_name: <string>
              fgt_peer_port_name: <string>
              fiber_port: <integer>
              flags: <integer>
              fortilink_port: <integer>
              isl_local_trunk_name: <string>
              isl_peer_device_name: <string>
              isl_peer_port_name: <string>
              poe_capable: <integer>
              port_number: <integer>
              port_prefix_type: <integer>
              ptp_policy: <list or string>
              speed: <value in [auto, 10full, 10half, ...]>
              speed_mask: <integer>
              stacking_port: <integer>
              switch_id: <string>
              virtual_port: <integer>
              export_tags: <list or string>
              log_mac_event: <value in [disable, enable]>
              pd_capable: <integer>
              qnq: <list or string>
          switch_id: <string>
          override_snmp_community: <value in [disable, enable]>
          override_snmp_sysinfo: <value in [disable, enable]>
          override_snmp_trap_threshold: <value in [disable, enable]>
          override_snmp_user: <value in [disable, enable]>
          poe_detection_type: <integer>
          remote_log:
            -
              csv: <value in [disable, enable]>
              facility: <value in [kernel, user, mail, ...]>
              name: <string>
              port: <integer>
              server: <string>
              severity: <value in [emergency, alert, critical, ...]>
              status: <value in [disable, enable]>
          snmp_community:
            -
              events:
                - cpu-high
                - mem-low
                - log-full
                - intf-ip
                - ent-conf-change
                - l2mac
              hosts:
                -
                  id: <integer>
                  ip: <string>
              id: <integer>
              name: <string>
              query_v1_port: <integer>
              query_v1_status: <value in [disable, enable]>
              query_v2c_port: <integer>
              query_v2c_status: <value in [disable, enable]>
              status: <value in [disable, enable]>
              trap_v1_lport: <integer>
              trap_v1_rport: <integer>
              trap_v1_status: <value in [disable, enable]>
              trap_v2c_lport: <integer>
              trap_v2c_rport: <integer>
              trap_v2c_status: <value in [disable, enable]>
          snmp_user:
            -
              auth_proto: <value in [md5, sha, sha1, ...]>
              auth_pwd: <list or string>
              name: <string>
              priv_proto: <value in [des, aes, aes128, ...]>
              priv_pwd: <list or string>
              queries: <value in [disable, enable]>
              query_port: <integer>
              security_level: <value in [no-auth-no-priv, auth-no-priv, auth-priv]>
          mclag_igmp_snooping_aware: <value in [disable, enable]>
          ip_source_guard:
            -
              binding_entry:
                -
                  entry_name: <string>
                  ip: <string>
                  mac: <string>
              description: <string>
              port: <string>
          l3_discovered: <integer>
          qos_drop_policy: <value in [taildrop, random-early-detection]>
          qos_red_probability: <integer>
          switch_dhcp_opt43_key: <string>
          tdr_supported: <string>
          custom_command:
            -
              command_entry: <string>
              command_name: <string>
          firmware_provision: <value in [disable, enable]>
          firmware_provision_version: <string>
          dhcp_server_access_list: <value in [disable, enable, global]>
          firmware_provision_latest: <value in [disable, once]>
          dhcp_snooping_static_client:
            -
              ip: <string>
              mac: <string>
              name: <string>
              port: <string>
              vlan: <string>
          ptp_profile: <string>
          ptp_status: <value in [disable, enable]>
          route_offload: <value in [disable, enable]>
          route_offload_mclag: <value in [disable, enable]>
          route_offload_router:
            -
              router_ip: <string>
              vlan_name: <string>
          mgmt_mode: <integer>
          purdue_level: <value in [1, 2, 3, ...]>
          radius_nas_ip: <string>
          radius_nas_ip_override: <value in [disable, enable]>
          tunnel_discovered: <integer>
          vlan:
            -
              assignment_priority: <integer>
              vlan_name: <string>
          802_1X_settings:
            link_down_auth: <value in [set-unauth, no-action]>
            local_override: <value in [disable, enable]>
            mab_reauth: <value in [disable, enable]>
            mac_called_station_delimiter: <value in [hyphen, single-hyphen, colon, ...]>
            mac_calling_station_delimiter: <value in [hyphen, single-hyphen, colon, ...]>
            mac_case: <value in [uppercase, lowercase]>
            mac_password_delimiter: <value in [hyphen, single-hyphen, colon, ...]>
            mac_username_delimiter: <value in [hyphen, single-hyphen, colon, ...]>
            max_reauth_attempt: <integer>
            reauth_period: <integer>
            tx_period: <integer>
          access_profile: <list or string>
          delayed_restart_trigger: <integer>
          directly_connected: <integer>
          dynamic_capability: <string>
          dynamically_discovered: <integer>
          flow_identity: <string>
          fsw_wan1_admin: <value in [disable, enable, discovered]>
          fsw_wan1_peer: <list or string>
          fsw_wan2_admin: <value in [disable, enable, discovered]>
          fsw_wan2_peer: <string>
          igmp_snooping:
            aging_time: <integer>
            flood_unknown_multicast: <value in [disable, enable]>
            local_override: <value in [disable, enable]>
            vlans:
              -
                proxy: <value in [disable, enable, global]>
                querier: <value in [disable, enable]>
                querier_addr: <string>
                version: <integer>
                vlan_name: <list or string>
          max_allowed_trunk_members: <integer>
          mirror:
            -
              dst: <string>
              name: <string>
              src_egress: <list or string>
              src_ingress: <list or string>
              status: <value in [inactive, active]>
              switching_packet: <value in [disable, enable]>
          owner_vdom: <string>
          poe_pre_standard_detection: <value in [disable, enable]>
          pre_provisioned: <integer>
          sn: <string>
          snmp_sysinfo:
            contact_info: <string>
            description: <string>
            engine_id: <string>
            location: <string>
            status: <value in [disable, enable]>
          snmp_trap_threshold:
            trap_high_cpu_threshold: <integer>
            trap_log_full_threshold: <integer>
            trap_low_memory_threshold: <integer>
          staged_image_version: <string>
          static_mac:
            -
              description: <string>
              id: <integer>
              interface: <string>
              mac: <string>
              type: <value in [static, sticky]>
              vlan: <list or string>
          storm_control:
            broadcast: <value in [disable, enable]>
            local_override: <value in [disable, enable]>
            rate: <integer>
            unknown_multicast: <value in [disable, enable]>
            unknown_unicast: <value in [disable, enable]>
          stp_instance:
            -
              id: <string>
              priority: <value in [0, 4096, 8192, ...]>
          stp_settings:
            forward_time: <integer>
            hello_time: <integer>
            local_override: <value in [disable, enable]>
            max_age: <integer>
            max_hops: <integer>
            name: <string>
            pending_timer: <integer>
            revision: <integer>
            status: <value in [disable, enable]>
          switch_device_tag: <string>
          switch_log:
            local_override: <value in [disable, enable]>
            severity: <value in [emergency, alert, critical, ...]>
            status: <value in [disable, enable]>
          switch_profile: <list or string>
          type: <value in [physical, virtual]>
          version: <integer>
          poe_lldp_detection: <value in [disable, enable]>
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
        '/pm/config/adom/{adom}/obj/switch-controller/managed-switch',
        '/pm/config/global/obj/switch-controller/managed-switch'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/switch-controller/managed-switch/{managed-switch}',
        '/pm/config/global/obj/switch-controller/managed-switch/{managed-switch}'
    ]

    url_params = ['adom']
    module_primary_key = 'switch-id'
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'switchcontroller_managedswitch': {
            'type': 'dict',
            'v_range': [['6.0.0', '']],
            'options': {
                '_platform': {'type': 'str'},
                'description': {'type': 'str'},
                'name': {'type': 'str'},
                'ports': {
                    'type': 'list',
                    'options': {
                        'allowed-vlans': {'type': 'raw'},
                        'allowed-vlans-all': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'arp-inspection-trust': {'choices': ['untrusted', 'trusted'], 'type': 'str'},
                        'bundle': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'description': {'type': 'str'},
                        'dhcp-snoop-option82-trust': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'dhcp-snooping': {'choices': ['trusted', 'untrusted'], 'type': 'str'},
                        'discard-mode': {'choices': ['none', 'all-untagged', 'all-tagged'], 'type': 'str'},
                        'edge-port': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'igmp-snooping': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'igmps-flood-reports': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'igmps-flood-traffic': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'lacp-speed': {'choices': ['slow', 'fast'], 'type': 'str'},
                        'learning-limit': {'type': 'int'},
                        'lldp-profile': {'type': 'str'},
                        'lldp-status': {'choices': ['disable', 'rx-only', 'tx-only', 'tx-rx'], 'type': 'str'},
                        'loop-guard': {'choices': ['disabled', 'enabled'], 'type': 'str'},
                        'loop-guard-timeout': {'type': 'int'},
                        'max-bundle': {'type': 'int'},
                        'mclag': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'member-withdrawal-behavior': {'choices': ['forward', 'block'], 'type': 'str'},
                        'members': {'type': 'raw'},
                        'min-bundle': {'type': 'int'},
                        'mode': {'choices': ['static', 'lacp-passive', 'lacp-active'], 'type': 'str'},
                        'poe-pre-standard-detection': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'poe-status': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'port-name': {'type': 'str'},
                        'port-owner': {'type': 'str'},
                        'port-security-policy': {'type': 'str'},
                        'port-selection-criteria': {'choices': ['src-mac', 'dst-mac', 'src-dst-mac', 'src-ip', 'dst-ip', 'src-dst-ip'], 'type': 'str'},
                        'qos-policy': {'type': 'str'},
                        'sample-direction': {'choices': ['rx', 'tx', 'both'], 'type': 'str'},
                        'sflow-counter-interval': {'type': 'int'},
                        'sflow-sample-rate': {'v_range': [['6.0.0', '7.2.1']], 'type': 'int'},
                        'sflow-sampler': {'v_range': [['6.0.0', '7.2.1']], 'choices': ['disabled', 'enabled'], 'type': 'str'},
                        'stp-bpdu-guard': {'choices': ['disabled', 'enabled'], 'type': 'str'},
                        'stp-bpdu-guard-timeout': {'type': 'int'},
                        'stp-root-guard': {'choices': ['disabled', 'enabled'], 'type': 'str'},
                        'stp-state': {'choices': ['disabled', 'enabled'], 'type': 'str'},
                        'type': {'choices': ['physical', 'trunk'], 'type': 'str'},
                        'untagged-vlans': {'type': 'raw'},
                        'vlan': {'type': 'str'},
                        'export-to-pool-flag': {'v_range': [['6.2.1', '6.2.3'], ['7.4.3', '']], 'type': 'int'},
                        'mac-addr': {'v_range': [['6.2.1', '6.2.1'], ['7.4.3', '']], 'type': 'str'},
                        'packet-sample-rate': {'v_range': [['6.2.0', '']], 'type': 'int'},
                        'packet-sampler': {'v_range': [['6.2.0', '']], 'choices': ['disabled', 'enabled'], 'type': 'str'},
                        'sticky-mac': {'v_range': [['6.2.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'storm-control-policy': {'v_range': [['6.2.0', '6.2.3'], ['7.4.3', '']], 'type': 'str'},
                        'dot1x-enable': {'v_range': [['6.2.0', '6.2.12']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'max-miss-heartbeats': {'v_range': [['6.2.0', '6.2.12']], 'type': 'int'},
                        'access-mode': {'v_range': [['6.4.0', '']], 'choices': ['normal', 'nac', 'dynamic', 'static'], 'type': 'str'},
                        'ip-source-guard': {'v_range': [['6.4.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'mclag-icl-port': {'v_range': [['6.4.0', '']], 'type': 'int'},
                        'p2p-port': {'v_range': [['6.4.0', '']], 'type': 'int'},
                        'aggregator-mode': {'v_range': [['6.4.2', '']], 'choices': ['bandwidth', 'count'], 'type': 'str'},
                        'rpvst-port': {'v_range': [['6.4.2', '']], 'choices': ['disabled', 'enabled'], 'type': 'str'},
                        'flow-control': {'v_range': [['6.4.3', '']], 'choices': ['disable', 'tx', 'rx', 'both'], 'type': 'str'},
                        'media-type': {'v_range': [['6.4.3', '']], 'type': 'str'},
                        'pause-meter': {'v_range': [['6.4.3', '']], 'type': 'int'},
                        'pause-meter-resume': {'v_range': [['6.4.3', '']], 'choices': ['25%', '50%', '75%'], 'type': 'str'},
                        'trunk-member': {'v_range': [['6.2.7', '6.2.12'], ['6.4.3', '']], 'type': 'int'},
                        'fec-capable': {'v_range': [['7.0.0', '']], 'type': 'int'},
                        'fec-state': {'v_range': [['7.0.0', '']], 'choices': ['disabled', 'cl74', 'cl91', 'detect-by-module'], 'type': 'str'},
                        'matched-dpp-intf-tags': {'v_range': [['7.0.0', '']], 'type': 'str'},
                        'matched-dpp-policy': {'v_range': [['7.0.0', '']], 'type': 'str'},
                        'port-policy': {'v_range': [['7.0.0', '7.0.4'], ['7.2.0', '']], 'type': 'str'},
                        'status': {'v_range': [['6.4.6', '']], 'choices': ['down', 'up'], 'type': 'str'},
                        'dsl-profile': {'v_range': [['7.0.2', '']], 'type': 'str'},
                        'flap-duration': {'v_range': [['7.2.0', '']], 'type': 'int'},
                        'flap-rate': {'v_range': [['7.2.0', '']], 'type': 'int'},
                        'flap-timeout': {'v_range': [['7.2.0', '']], 'type': 'int'},
                        'flapguard': {'v_range': [['7.2.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'interface-tags': {'v_range': [['7.0.2', '']], 'type': 'raw'},
                        'poe-max-power': {'v_range': [['7.0.1', '']], 'type': 'str'},
                        'poe-standard': {'v_range': [['7.0.1', '']], 'type': 'str'},
                        'igmp-snooping-flood-reports': {'v_range': [['7.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'mcast-snooping-flood-traffic': {'v_range': [['7.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'link-status': {'v_range': [['7.2.2', '']], 'choices': ['down', 'up'], 'type': 'str'},
                        'poe-mode-bt-cabable': {'v_range': [['7.2.2', '']], 'type': 'int'},
                        'poe-port-mode': {'v_range': [['7.2.2', '']], 'choices': ['ieee802-3af', 'ieee802-3at', 'ieee802-3bt'], 'type': 'str'},
                        'poe-port-power': {'v_range': [['7.2.2', '']], 'choices': ['normal', 'perpetual', 'perpetual-fast'], 'type': 'str'},
                        'poe-port-priority': {
                            'v_range': [['7.2.2', '']],
                            'choices': ['critical-priority', 'high-priority', 'low-priority', 'medium-priority'],
                            'type': 'str'
                        },
                        'acl-group': {'v_range': [['7.4.0', '']], 'type': 'raw'},
                        'dhcp-snoop-option82-override': {
                            'v_range': [['7.4.0', '']],
                            'type': 'list',
                            'options': {
                                'circuit-id': {'v_range': [['7.4.0', '']], 'type': 'str'},
                                'remote-id': {'v_range': [['7.4.0', '']], 'type': 'str'},
                                'vlan-name': {'v_range': [['7.4.0', '']], 'type': 'str'}
                            },
                            'elements': 'dict'
                        },
                        'fortiswitch-acls': {'v_range': [['7.4.0', '']], 'type': 'raw'},
                        'isl-peer-device-sn': {'v_range': [['7.4.0', '']], 'type': 'str'},
                        'authenticated-port': {'v_range': [['7.4.1', '']], 'type': 'int'},
                        'encrypted-port': {'v_range': [['7.4.1', '']], 'type': 'int'},
                        'ptp-status': {'v_range': [['7.4.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'restricted-auth-port': {'v_range': [['7.4.1', '']], 'type': 'int'},
                        'allow-arp-monitor': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'export-to': {'v_range': [['7.4.3', '']], 'type': 'raw'},
                        'export-to-pool': {'v_range': [['7.4.3', '']], 'type': 'raw'},
                        'fallback-port': {'v_range': [['7.4.3', '']], 'type': 'str'},
                        'fgt-peer-device-name': {'v_range': [['7.4.3', '']], 'type': 'str'},
                        'fgt-peer-port-name': {'v_range': [['7.4.3', '']], 'type': 'str'},
                        'fiber-port': {'v_range': [['7.4.3', '']], 'type': 'int'},
                        'flags': {'v_range': [['7.4.3', '']], 'type': 'int'},
                        'fortilink-port': {'v_range': [['7.4.3', '']], 'type': 'int'},
                        'isl-local-trunk-name': {'v_range': [['7.4.3', '']], 'type': 'str'},
                        'isl-peer-device-name': {'v_range': [['7.4.3', '']], 'type': 'str'},
                        'isl-peer-port-name': {'v_range': [['7.4.3', '']], 'type': 'str'},
                        'poe-capable': {'v_range': [['7.4.3', '']], 'type': 'int'},
                        'port-number': {'v_range': [['7.4.3', '']], 'type': 'int'},
                        'port-prefix-type': {'v_range': [['7.4.3', '']], 'type': 'int'},
                        'ptp-policy': {'v_range': [['7.4.3', '']], 'type': 'raw'},
                        'speed': {
                            'v_range': [['7.4.3', '']],
                            'choices': [
                                'auto', '10full', '10half', '100full', '100half', '1000full', '10000full', '1000auto', '40000full', '1000fiber', '10000',
                                '40000', 'auto-module', '100FX-half', '100FX-full', '100000full', '2500full', '25000full', '50000full', '40000auto',
                                '10000cr', '10000sr', '100000sr4', '100000cr4', '25000cr4', '25000sr4', '5000full', '2500auto', '5000auto',
                                '1000full-fiber', '40000sr4', '40000cr4', '25000cr', '25000sr', '50000cr', '50000sr'
                            ],
                            'type': 'str'
                        },
                        'speed-mask': {'v_range': [['7.4.3', '']], 'type': 'int'},
                        'stacking-port': {'v_range': [['7.4.3', '']], 'type': 'int'},
                        'switch-id': {'v_range': [['7.4.3', '']], 'type': 'str'},
                        'virtual-port': {'v_range': [['7.4.3', '']], 'type': 'int'},
                        'export-tags': {'v_range': [['7.4.3', '']], 'type': 'raw'},
                        'log-mac-event': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'pd-capable': {'v_range': [['7.6.0', '']], 'type': 'int'},
                        'qnq': {'v_range': [['7.6.0', '']], 'type': 'raw'}
                    },
                    'elements': 'dict'
                },
                'switch-id': {'required': True, 'type': 'str'},
                'override-snmp-community': {'v_range': [['6.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'override-snmp-sysinfo': {'v_range': [['6.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'override-snmp-trap-threshold': {'v_range': [['6.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'override-snmp-user': {'v_range': [['6.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'poe-detection-type': {'v_range': [['6.2.0', '']], 'type': 'int'},
                'remote-log': {
                    'v_range': [['6.2.1', '6.2.3'], ['7.4.3', '']],
                    'type': 'list',
                    'options': {
                        'csv': {'v_range': [['6.2.1', '6.2.3'], ['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'facility': {
                            'v_range': [['6.2.1', '6.2.3'], ['7.4.3', '']],
                            'choices': [
                                'kernel', 'user', 'mail', 'daemon', 'auth', 'syslog', 'lpr', 'news', 'uucp', 'cron', 'authpriv', 'ftp', 'ntp', 'audit',
                                'alert', 'clock', 'local0', 'local1', 'local2', 'local3', 'local4', 'local5', 'local6', 'local7'
                            ],
                            'type': 'str'
                        },
                        'name': {'v_range': [['6.2.1', '6.2.3'], ['7.4.3', '']], 'type': 'str'},
                        'port': {'v_range': [['6.2.1', '6.2.3'], ['7.4.3', '']], 'type': 'int'},
                        'server': {'v_range': [['6.2.1', '6.2.3'], ['7.4.3', '']], 'type': 'str'},
                        'severity': {
                            'v_range': [['6.2.1', '6.2.3'], ['7.4.3', '']],
                            'choices': ['emergency', 'alert', 'critical', 'error', 'warning', 'notification', 'information', 'debug'],
                            'type': 'str'
                        },
                        'status': {'v_range': [['6.2.1', '6.2.3'], ['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'}
                    },
                    'elements': 'dict'
                },
                'snmp-community': {
                    'v_range': [['6.2.1', '6.2.3'], ['7.4.3', '']],
                    'type': 'list',
                    'options': {
                        'events': {
                            'v_range': [['6.2.1', '6.2.3'], ['7.4.3', '']],
                            'type': 'list',
                            'choices': ['cpu-high', 'mem-low', 'log-full', 'intf-ip', 'ent-conf-change', 'l2mac'],
                            'elements': 'str'
                        },
                        'hosts': {
                            'v_range': [['6.2.1', '6.2.3'], ['7.4.3', '']],
                            'type': 'list',
                            'options': {
                                'id': {'v_range': [['6.2.1', '6.2.3'], ['7.4.3', '']], 'type': 'int'},
                                'ip': {'v_range': [['6.2.1', '6.2.3'], ['7.4.3', '']], 'type': 'str'}
                            },
                            'elements': 'dict'
                        },
                        'id': {'v_range': [['6.2.1', '6.2.3'], ['7.4.3', '']], 'type': 'int'},
                        'name': {'v_range': [['6.2.1', '6.2.3'], ['7.4.3', '']], 'type': 'str'},
                        'query-v1-port': {'v_range': [['6.2.1', '6.2.3'], ['7.4.3', '']], 'type': 'int'},
                        'query-v1-status': {'v_range': [['6.2.1', '6.2.3'], ['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'query-v2c-port': {'v_range': [['6.2.1', '6.2.3'], ['7.4.3', '']], 'type': 'int'},
                        'query-v2c-status': {'v_range': [['6.2.1', '6.2.3'], ['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'status': {'v_range': [['6.2.1', '6.2.3'], ['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'trap-v1-lport': {'v_range': [['6.2.1', '6.2.3'], ['7.4.3', '']], 'type': 'int'},
                        'trap-v1-rport': {'v_range': [['6.2.1', '6.2.3'], ['7.4.3', '']], 'type': 'int'},
                        'trap-v1-status': {'v_range': [['6.2.1', '6.2.3'], ['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'trap-v2c-lport': {'v_range': [['6.2.1', '6.2.3'], ['7.4.3', '']], 'type': 'int'},
                        'trap-v2c-rport': {'v_range': [['6.2.1', '6.2.3'], ['7.4.3', '']], 'type': 'int'},
                        'trap-v2c-status': {'v_range': [['6.2.1', '6.2.3'], ['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'}
                    },
                    'elements': 'dict'
                },
                'snmp-user': {
                    'v_range': [['6.2.1', '6.2.3'], ['7.4.3', '']],
                    'type': 'list',
                    'options': {
                        'auth-proto': {
                            'v_range': [['6.2.1', '6.2.3'], ['7.4.3', '']],
                            'choices': ['md5', 'sha', 'sha1', 'sha256', 'sha384', 'sha512', 'sha224'],
                            'type': 'str'
                        },
                        'auth-pwd': {'v_range': [['6.2.1', '6.2.3'], ['7.4.3', '']], 'type': 'raw'},
                        'name': {'v_range': [['6.2.1', '6.2.3'], ['7.4.3', '']], 'type': 'str'},
                        'priv-proto': {
                            'v_range': [['6.2.1', '6.2.3'], ['7.4.3', '']],
                            'choices': ['des', 'aes', 'aes128', 'aes192', 'aes256', 'aes192c', 'aes256c'],
                            'type': 'str'
                        },
                        'priv-pwd': {'v_range': [['6.2.1', '6.2.3'], ['7.4.3', '']], 'type': 'raw'},
                        'queries': {'v_range': [['6.2.1', '6.2.3'], ['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'query-port': {'v_range': [['6.2.1', '6.2.3'], ['7.4.3', '']], 'type': 'int'},
                        'security-level': {
                            'v_range': [['6.2.1', '6.2.3'], ['7.4.3', '']],
                            'choices': ['no-auth-no-priv', 'auth-no-priv', 'auth-priv'],
                            'type': 'str'
                        }
                    },
                    'elements': 'dict'
                },
                'mclag-igmp-snooping-aware': {'v_range': [['6.2.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ip-source-guard': {
                    'v_range': [['6.4.0', '6.4.1'], ['7.4.3', '']],
                    'type': 'list',
                    'options': {
                        'binding-entry': {
                            'v_range': [['6.4.0', '6.4.1'], ['7.4.3', '']],
                            'type': 'list',
                            'options': {
                                'entry-name': {'v_range': [['6.4.0', '6.4.1'], ['7.4.3', '']], 'type': 'str'},
                                'ip': {'v_range': [['6.4.0', '6.4.1'], ['7.4.3', '']], 'type': 'str'},
                                'mac': {'v_range': [['6.4.0', '6.4.1'], ['7.4.3', '']], 'type': 'str'}
                            },
                            'elements': 'dict'
                        },
                        'description': {'v_range': [['6.4.0', '6.4.1'], ['7.4.3', '']], 'type': 'str'},
                        'port': {'v_range': [['6.4.0', '6.4.1'], ['7.4.3', '']], 'type': 'str'}
                    },
                    'elements': 'dict'
                },
                'l3-discovered': {'v_range': [['6.4.0', '']], 'type': 'int'},
                'qos-drop-policy': {'v_range': [['6.4.0', '']], 'choices': ['taildrop', 'random-early-detection'], 'type': 'str'},
                'qos-red-probability': {'v_range': [['6.4.0', '']], 'type': 'int'},
                'switch-dhcp_opt43_key': {'v_range': [['6.4.0', '']], 'no_log': True, 'type': 'str'},
                'tdr-supported': {'v_range': [['6.4.3', '']], 'type': 'str'},
                'custom-command': {
                    'v_range': [['7.0.0', '']],
                    'type': 'list',
                    'options': {'command-entry': {'v_range': [['7.0.0', '']], 'type': 'str'}, 'command-name': {'v_range': [['7.0.0', '']], 'type': 'str'}},
                    'elements': 'dict'
                },
                'firmware-provision': {'v_range': [['7.0.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'firmware-provision-version': {'v_range': [['7.0.0', '']], 'type': 'str'},
                'dhcp-server-access-list': {'v_range': [['7.0.1', '']], 'choices': ['disable', 'enable', 'global'], 'type': 'str'},
                'firmware-provision-latest': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'once'], 'type': 'str'},
                'dhcp-snooping-static-client': {
                    'v_range': [['7.2.2', '']],
                    'type': 'list',
                    'options': {
                        'ip': {'v_range': [['7.2.2', '']], 'type': 'str'},
                        'mac': {'v_range': [['7.2.2', '']], 'type': 'str'},
                        'name': {'v_range': [['7.2.2', '']], 'type': 'str'},
                        'port': {'v_range': [['7.2.2', '']], 'type': 'str'},
                        'vlan': {'v_range': [['7.2.2', '']], 'type': 'str'}
                    },
                    'elements': 'dict'
                },
                'ptp-profile': {'v_range': [['7.4.1', '']], 'type': 'str'},
                'ptp-status': {'v_range': [['7.4.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'route-offload': {'v_range': [['7.4.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'route-offload-mclag': {'v_range': [['7.4.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'route-offload-router': {
                    'v_range': [['7.4.1', '']],
                    'type': 'list',
                    'options': {'router-ip': {'v_range': [['7.4.1', '']], 'type': 'str'}, 'vlan-name': {'v_range': [['7.4.1', '']], 'type': 'str'}},
                    'elements': 'dict'
                },
                'mgmt-mode': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'purdue-level': {'v_range': [['7.4.2', '']], 'choices': ['1', '2', '3', '4', '5', '1.5', '2.5', '3.5', '5.5'], 'type': 'str'},
                'radius-nas-ip': {'v_range': [['7.4.2', '']], 'type': 'str'},
                'radius-nas-ip-override': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'tunnel-discovered': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'vlan': {
                    'v_range': [['7.4.2', '']],
                    'type': 'list',
                    'options': {
                        'assignment-priority': {'v_range': [['7.4.2', '']], 'type': 'int'},
                        'vlan-name': {'v_range': [['7.4.2', '']], 'type': 'str'}
                    },
                    'elements': 'dict'
                },
                '802-1X-settings': {
                    'v_range': [['7.4.3', '']],
                    'type': 'dict',
                    'options': {
                        'link-down-auth': {'v_range': [['7.4.3', '']], 'choices': ['set-unauth', 'no-action'], 'type': 'str'},
                        'local-override': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'mab-reauth': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'mac-called-station-delimiter': {
                            'v_range': [['7.4.3', '']],
                            'choices': ['hyphen', 'single-hyphen', 'colon', 'none'],
                            'type': 'str'
                        },
                        'mac-calling-station-delimiter': {
                            'v_range': [['7.4.3', '']],
                            'choices': ['hyphen', 'single-hyphen', 'colon', 'none'],
                            'type': 'str'
                        },
                        'mac-case': {'v_range': [['7.4.3', '']], 'choices': ['uppercase', 'lowercase'], 'type': 'str'},
                        'mac-password-delimiter': {'v_range': [['7.4.3', '']], 'choices': ['hyphen', 'single-hyphen', 'colon', 'none'], 'type': 'str'},
                        'mac-username-delimiter': {'v_range': [['7.4.3', '']], 'choices': ['hyphen', 'single-hyphen', 'colon', 'none'], 'type': 'str'},
                        'max-reauth-attempt': {'v_range': [['7.4.3', '']], 'type': 'int'},
                        'reauth-period': {'v_range': [['7.4.3', '']], 'type': 'int'},
                        'tx-period': {'v_range': [['7.4.3', '']], 'type': 'int'}
                    }
                },
                'access-profile': {'v_range': [['7.4.3', '']], 'type': 'raw'},
                'delayed-restart-trigger': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'directly-connected': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'dynamic-capability': {'v_range': [['7.4.3', '']], 'type': 'str'},
                'dynamically-discovered': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'flow-identity': {'v_range': [['7.4.3', '']], 'type': 'str'},
                'fsw-wan1-admin': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable', 'discovered'], 'type': 'str'},
                'fsw-wan1-peer': {'v_range': [['7.4.3', '']], 'type': 'raw'},
                'fsw-wan2-admin': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable', 'discovered'], 'type': 'str'},
                'fsw-wan2-peer': {'v_range': [['7.4.3', '']], 'type': 'str'},
                'igmp-snooping': {
                    'v_range': [['7.4.3', '']],
                    'type': 'dict',
                    'options': {
                        'aging-time': {'v_range': [['7.4.3', '']], 'type': 'int'},
                        'flood-unknown-multicast': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'local-override': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'vlans': {
                            'v_range': [['7.4.3', '']],
                            'type': 'list',
                            'options': {
                                'proxy': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable', 'global'], 'type': 'str'},
                                'querier': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'querier-addr': {'v_range': [['7.4.3', '']], 'type': 'str'},
                                'version': {'v_range': [['7.4.3', '']], 'type': 'int'},
                                'vlan-name': {'v_range': [['7.4.3', '']], 'type': 'raw'}
                            },
                            'elements': 'dict'
                        }
                    }
                },
                'max-allowed-trunk-members': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'mirror': {
                    'v_range': [['7.4.3', '']],
                    'type': 'list',
                    'options': {
                        'dst': {'v_range': [['7.4.3', '']], 'type': 'str'},
                        'name': {'v_range': [['7.4.3', '']], 'type': 'str'},
                        'src-egress': {'v_range': [['7.4.3', '']], 'type': 'raw'},
                        'src-ingress': {'v_range': [['7.4.3', '']], 'type': 'raw'},
                        'status': {'v_range': [['7.4.3', '']], 'choices': ['inactive', 'active'], 'type': 'str'},
                        'switching-packet': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'}
                    },
                    'elements': 'dict'
                },
                'owner-vdom': {'v_range': [['7.4.3', '']], 'type': 'str'},
                'poe-pre-standard-detection': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'pre-provisioned': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'sn': {'v_range': [['7.4.3', '']], 'type': 'str'},
                'snmp-sysinfo': {
                    'v_range': [['7.4.3', '']],
                    'type': 'dict',
                    'options': {
                        'contact-info': {'v_range': [['7.4.3', '']], 'type': 'str'},
                        'description': {'v_range': [['7.4.3', '']], 'type': 'str'},
                        'engine-id': {'v_range': [['7.4.3', '']], 'type': 'str'},
                        'location': {'v_range': [['7.4.3', '']], 'type': 'str'},
                        'status': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'}
                    }
                },
                'snmp-trap-threshold': {
                    'v_range': [['7.4.3', '']],
                    'type': 'dict',
                    'options': {
                        'trap-high-cpu-threshold': {'v_range': [['7.4.3', '']], 'type': 'int'},
                        'trap-log-full-threshold': {'v_range': [['7.4.3', '']], 'type': 'int'},
                        'trap-low-memory-threshold': {'v_range': [['7.4.3', '']], 'type': 'int'}
                    }
                },
                'staged-image-version': {'v_range': [['7.4.3', '']], 'type': 'str'},
                'static-mac': {
                    'v_range': [['7.4.3', '']],
                    'type': 'list',
                    'options': {
                        'description': {'v_range': [['7.4.3', '']], 'type': 'str'},
                        'id': {'v_range': [['7.4.3', '']], 'type': 'int'},
                        'interface': {'v_range': [['7.4.3', '']], 'type': 'str'},
                        'mac': {'v_range': [['7.4.3', '']], 'type': 'str'},
                        'type': {'v_range': [['7.4.3', '']], 'choices': ['static', 'sticky'], 'type': 'str'},
                        'vlan': {'v_range': [['7.4.3', '']], 'type': 'raw'}
                    },
                    'elements': 'dict'
                },
                'storm-control': {
                    'v_range': [['7.4.3', '']],
                    'type': 'dict',
                    'options': {
                        'broadcast': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'local-override': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'rate': {'v_range': [['7.4.3', '']], 'type': 'int'},
                        'unknown-multicast': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'unknown-unicast': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'}
                    }
                },
                'stp-instance': {
                    'v_range': [['7.4.3', '']],
                    'type': 'list',
                    'options': {
                        'id': {'v_range': [['7.4.3', '']], 'type': 'str'},
                        'priority': {
                            'v_range': [['7.4.3', '']],
                            'choices': [
                                '0', '4096', '8192', '12288', '12328', '16384', '20480', '24576', '28672', '32768', '36864', '40960', '45056', '49152',
                                '53248', '57344', '61440'
                            ],
                            'type': 'str'
                        }
                    },
                    'elements': 'dict'
                },
                'stp-settings': {
                    'v_range': [['7.4.3', '']],
                    'type': 'dict',
                    'options': {
                        'forward-time': {'v_range': [['7.4.3', '']], 'type': 'int'},
                        'hello-time': {'v_range': [['7.4.3', '']], 'type': 'int'},
                        'local-override': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'max-age': {'v_range': [['7.4.3', '']], 'type': 'int'},
                        'max-hops': {'v_range': [['7.4.3', '']], 'type': 'int'},
                        'name': {'v_range': [['7.4.3', '']], 'type': 'str'},
                        'pending-timer': {'v_range': [['7.4.3', '']], 'type': 'int'},
                        'revision': {'v_range': [['7.4.3', '']], 'type': 'int'},
                        'status': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'}
                    }
                },
                'switch-device-tag': {'v_range': [['7.4.3', '']], 'type': 'str'},
                'switch-log': {
                    'v_range': [['7.4.3', '']],
                    'type': 'dict',
                    'options': {
                        'local-override': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'severity': {
                            'v_range': [['7.4.3', '']],
                            'choices': ['emergency', 'alert', 'critical', 'error', 'warning', 'notification', 'information', 'debug'],
                            'type': 'str'
                        },
                        'status': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'}
                    }
                },
                'switch-profile': {'v_range': [['7.4.3', '']], 'type': 'raw'},
                'type': {'v_range': [['7.4.3', '']], 'choices': ['physical', 'virtual'], 'type': 'str'},
                'version': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'poe-lldp-detection': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('full crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'switchcontroller_managedswitch'),
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
