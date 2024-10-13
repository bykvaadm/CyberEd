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
module: fmgr_switchcontroller_managedswitch_ports
short_description: Managed-switch port list.
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
    managed-switch:
        description: Deprecated, please use "managed_switch"
        type: str
    managed_switch:
        description: The parameter (managed-switch) in requested url.
        type: str
    switchcontroller_managedswitch_ports:
        description: The top level parameters set.
        required: false
        type: dict
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
                description: Deprecated, please rename it to dhcp_snoop_option82_trust. Enable/disable allowance of DHCP with option-82 on untrusted in...
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
                description: Deprecated, please rename it to edge_port. Enable/disable this interface as an edge port, bridging connections between wor...
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
                description: Deprecated, please rename it to igmps_flood_reports. Enable/disable flooding of IGMP reports to this interface when igmp-s...
                choices:
                    - 'disable'
                    - 'enable'
            igmps-flood-traffic:
                type: str
                description: Deprecated, please rename it to igmps_flood_traffic. Enable/disable flooding of IGMP snooping traffic to this interface.
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
                description: Deprecated, please rename it to loop_guard. Enable/disable loop-guard on this interface, an STP optimization used to preve...
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
                description: Deprecated, please rename it to member_withdrawal_behavior. Port behavior after it withdraws because of loss of control pa...
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
                required: true
            port-owner:
                type: str
                description: Deprecated, please rename it to port_owner. Switch port name.
            port-security-policy:
                type: str
                description: Deprecated, please rename it to port_security_policy. Switch controller authentication policy to apply to this managed swi...
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
                description: Deprecated, please rename it to igmp_snooping_flood_reports. Enable/disable flooding of IGMP reports to this interface whe...
                choices:
                    - 'disable'
                    - 'enable'
            mcast-snooping-flood-traffic:
                type: str
                description: Deprecated, please rename it to mcast_snooping_flood_traffic. Enable/disable flooding of IGMP snooping traffic to this int...
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
    - name: Managed-switch port list.
      fortinet.fortimanager.fmgr_switchcontroller_managedswitch_ports:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        adom: <your own value>
        managed_switch: <your own value>
        state: present # <value in [present, absent]>
        switchcontroller_managedswitch_ports:
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
        '/pm/config/adom/{adom}/obj/switch-controller/managed-switch/{managed-switch}/ports',
        '/pm/config/global/obj/switch-controller/managed-switch/{managed-switch}/ports'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/switch-controller/managed-switch/{managed-switch}/ports/{ports}',
        '/pm/config/global/obj/switch-controller/managed-switch/{managed-switch}/ports/{ports}'
    ]

    url_params = ['adom', 'managed-switch']
    module_primary_key = 'port-name'
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'managed-switch': {'type': 'str', 'api_name': 'managed_switch'},
        'managed_switch': {'type': 'str'},
        'switchcontroller_managedswitch_ports': {
            'type': 'dict',
            'v_range': [['6.0.0', '']],
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
                'port-name': {'required': True, 'type': 'str'},
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
                        '40000', 'auto-module', '100FX-half', '100FX-full', '100000full', '2500full', '25000full', '50000full', '40000auto', '10000cr',
                        '10000sr', '100000sr4', '100000cr4', '25000cr4', '25000sr4', '5000full', '2500auto', '5000auto', '1000full-fiber', '40000sr4',
                        '40000cr4', '25000cr', '25000sr', '50000cr', '50000sr'
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
            }

        }
    }

    module_option_spec = get_module_arg_spec('full crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'switchcontroller_managedswitch_ports'),
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
