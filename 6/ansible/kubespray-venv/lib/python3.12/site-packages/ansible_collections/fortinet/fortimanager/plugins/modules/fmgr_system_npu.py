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
module: fmgr_system_npu
short_description: Configure NPU attributes.
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
    system_npu:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            capwap-offload:
                type: str
                description: Deprecated, please rename it to capwap_offload. Enable/disable offloading managed FortiAP and FortiLink CAPWAP sessions.
                choices:
                    - 'disable'
                    - 'enable'
            dedicated-management-affinity:
                type: str
                description: Deprecated, please rename it to dedicated_management_affinity. Affinity setting for management deamons
            dedicated-management-cpu:
                type: str
                description: Deprecated, please rename it to dedicated_management_cpu. Enable to dedicate one CPU for GUI and CLI connections when NPs ...
                choices:
                    - 'disable'
                    - 'enable'
            fastpath:
                type: str
                description: Enable/disable NP6 offloading
                choices:
                    - 'disable'
                    - 'enable'
            fp-anomaly:
                type: dict
                description: Deprecated, please rename it to fp_anomaly. Fp anomaly.
                suboptions:
                    esp-minlen-err:
                        type: str
                        description: Deprecated, please rename it to esp_minlen_err. Invalid IPv4 ESP short packet anomalies.
                        choices:
                            - 'drop'
                            - 'trap-to-host'
                    icmp-csum-err:
                        type: str
                        description: Deprecated, please rename it to icmp_csum_err. Invalid IPv4 ICMP packet checksum anomalies.
                        choices:
                            - 'drop'
                            - 'trap-to-host'
                    icmp-minlen-err:
                        type: str
                        description: Deprecated, please rename it to icmp_minlen_err. Invalid IPv4 ICMP short packet anomalies.
                        choices:
                            - 'drop'
                            - 'trap-to-host'
                    ipv4-csum-err:
                        type: str
                        description: Deprecated, please rename it to ipv4_csum_err. Invalid IPv4 packet checksum anomalies.
                        choices:
                            - 'drop'
                            - 'trap-to-host'
                    ipv4-ihl-err:
                        type: str
                        description: Deprecated, please rename it to ipv4_ihl_err. Invalid IPv4 header length anomalies.
                        choices:
                            - 'drop'
                            - 'trap-to-host'
                    ipv4-len-err:
                        type: str
                        description: Deprecated, please rename it to ipv4_len_err. Invalid IPv4 packet length anomalies.
                        choices:
                            - 'drop'
                            - 'trap-to-host'
                    ipv4-opt-err:
                        type: str
                        description: Deprecated, please rename it to ipv4_opt_err. Invalid IPv4 option parsing anomalies.
                        choices:
                            - 'drop'
                            - 'trap-to-host'
                    ipv4-ttlzero-err:
                        type: str
                        description: Deprecated, please rename it to ipv4_ttlzero_err. Invalid IPv4 TTL field zero anomalies.
                        choices:
                            - 'drop'
                            - 'trap-to-host'
                    ipv4-ver-err:
                        type: str
                        description: Deprecated, please rename it to ipv4_ver_err. Invalid IPv4 header version anomalies.
                        choices:
                            - 'drop'
                            - 'trap-to-host'
                    ipv6-exthdr-len-err:
                        type: str
                        description: Deprecated, please rename it to ipv6_exthdr_len_err. Invalid IPv6 packet chain extension header total length anoma...
                        choices:
                            - 'drop'
                            - 'trap-to-host'
                    ipv6-exthdr-order-err:
                        type: str
                        description: Deprecated, please rename it to ipv6_exthdr_order_err. Invalid IPv6 packet extension header ordering anomalies.
                        choices:
                            - 'drop'
                            - 'trap-to-host'
                    ipv6-ihl-err:
                        type: str
                        description: Deprecated, please rename it to ipv6_ihl_err. Invalid IPv6 packet length anomalies.
                        choices:
                            - 'drop'
                            - 'trap-to-host'
                    ipv6-plen-zero:
                        type: str
                        description: Deprecated, please rename it to ipv6_plen_zero. Invalid IPv6 packet payload length zero anomalies.
                        choices:
                            - 'drop'
                            - 'trap-to-host'
                    ipv6-ver-err:
                        type: str
                        description: Deprecated, please rename it to ipv6_ver_err. Invalid IPv6 packet version anomalies.
                        choices:
                            - 'drop'
                            - 'trap-to-host'
                    tcp-csum-err:
                        type: str
                        description: Deprecated, please rename it to tcp_csum_err. Invalid IPv4 TCP packet checksum anomalies.
                        choices:
                            - 'drop'
                            - 'trap-to-host'
                    tcp-hlen-err:
                        type: str
                        description: Deprecated, please rename it to tcp_hlen_err. Invalid IPv4 TCP header length anomalies.
                        choices:
                            - 'drop'
                            - 'trap-to-host'
                    tcp-plen-err:
                        type: str
                        description: Deprecated, please rename it to tcp_plen_err. Invalid IPv4 TCP packet length anomalies.
                        choices:
                            - 'drop'
                            - 'trap-to-host'
                    udp-csum-err:
                        type: str
                        description: Deprecated, please rename it to udp_csum_err. Invalid IPv4 UDP packet checksum anomalies.
                        choices:
                            - 'drop'
                            - 'trap-to-host'
                    udp-hlen-err:
                        type: str
                        description: Deprecated, please rename it to udp_hlen_err. Invalid IPv4 UDP packet header length anomalies.
                        choices:
                            - 'drop'
                            - 'trap-to-host'
                    udp-len-err:
                        type: str
                        description: Deprecated, please rename it to udp_len_err. Invalid IPv4 UDP packet length anomalies.
                        choices:
                            - 'drop'
                            - 'trap-to-host'
                    udp-plen-err:
                        type: str
                        description: Deprecated, please rename it to udp_plen_err. Invalid IPv4 UDP packet minimum length anomalies.
                        choices:
                            - 'drop'
                            - 'trap-to-host'
                    udplite-cover-err:
                        type: str
                        description: Deprecated, please rename it to udplite_cover_err. Invalid IPv4 UDP-Lite packet coverage anomalies.
                        choices:
                            - 'drop'
                            - 'trap-to-host'
                    udplite-csum-err:
                        type: str
                        description: Deprecated, please rename it to udplite_csum_err. Invalid IPv4 UDP-Lite packet checksum anomalies.
                        choices:
                            - 'drop'
                            - 'trap-to-host'
                    unknproto-minlen-err:
                        type: str
                        description: Deprecated, please rename it to unknproto_minlen_err. Invalid IPv4 L4 unknown protocol short packet anomalies.
                        choices:
                            - 'drop'
                            - 'trap-to-host'
                    tcp-fin-only:
                        type: str
                        description: Deprecated, please rename it to tcp_fin_only. TCP SYN flood with only FIN flag set anomalies.
                        choices:
                            - 'allow'
                            - 'drop'
                            - 'trap-to-host'
                    ipv4-optsecurity:
                        type: str
                        description: Deprecated, please rename it to ipv4_optsecurity. Security option anomalies.
                        choices:
                            - 'allow'
                            - 'drop'
                            - 'trap-to-host'
                    ipv6-optralert:
                        type: str
                        description: Deprecated, please rename it to ipv6_optralert. Router alert option anomalies.
                        choices:
                            - 'allow'
                            - 'drop'
                            - 'trap-to-host'
                    tcp-syn-fin:
                        type: str
                        description: Deprecated, please rename it to tcp_syn_fin. TCP SYN flood SYN/FIN flag set anomalies.
                        choices:
                            - 'allow'
                            - 'drop'
                            - 'trap-to-host'
                    ipv4-proto-err:
                        type: str
                        description: Deprecated, please rename it to ipv4_proto_err. Invalid layer 4 protocol anomalies.
                        choices:
                            - 'allow'
                            - 'drop'
                            - 'trap-to-host'
                    ipv6-saddr-err:
                        type: str
                        description: Deprecated, please rename it to ipv6_saddr_err. Source address as multicast anomalies.
                        choices:
                            - 'allow'
                            - 'drop'
                            - 'trap-to-host'
                    icmp-frag:
                        type: str
                        description: Deprecated, please rename it to icmp_frag. Layer 3 fragmented packets that could be part of layer 4 ICMP anomalies.
                        choices:
                            - 'allow'
                            - 'drop'
                            - 'trap-to-host'
                    ipv4-optssrr:
                        type: str
                        description: Deprecated, please rename it to ipv4_optssrr. Strict source record route option anomalies.
                        choices:
                            - 'allow'
                            - 'drop'
                            - 'trap-to-host'
                    ipv6-opthomeaddr:
                        type: str
                        description: Deprecated, please rename it to ipv6_opthomeaddr. Home address option anomalies.
                        choices:
                            - 'allow'
                            - 'drop'
                            - 'trap-to-host'
                    udp-land:
                        type: str
                        description: Deprecated, please rename it to udp_land. UDP land anomalies.
                        choices:
                            - 'allow'
                            - 'drop'
                            - 'trap-to-host'
                    ipv6-optinvld:
                        type: str
                        description: Deprecated, please rename it to ipv6_optinvld. Invalid option anomalies.
                        choices:
                            - 'allow'
                            - 'drop'
                            - 'trap-to-host'
                    tcp-fin-noack:
                        type: str
                        description: Deprecated, please rename it to tcp_fin_noack. TCP SYN flood with FIN flag set without ACK setting anomalies.
                        choices:
                            - 'allow'
                            - 'drop'
                            - 'trap-to-host'
                    ipv6-proto-err:
                        type: str
                        description: Deprecated, please rename it to ipv6_proto_err. Layer 4 invalid protocol anomalies.
                        choices:
                            - 'allow'
                            - 'drop'
                            - 'trap-to-host'
                    tcp-land:
                        type: str
                        description: Deprecated, please rename it to tcp_land. TCP land anomalies.
                        choices:
                            - 'allow'
                            - 'drop'
                            - 'trap-to-host'
                    ipv4-unknopt:
                        type: str
                        description: Deprecated, please rename it to ipv4_unknopt. Unknown option anomalies.
                        choices:
                            - 'allow'
                            - 'drop'
                            - 'trap-to-host'
                    ipv4-optstream:
                        type: str
                        description: Deprecated, please rename it to ipv4_optstream. Stream option anomalies.
                        choices:
                            - 'allow'
                            - 'drop'
                            - 'trap-to-host'
                    ipv6-optjumbo:
                        type: str
                        description: Deprecated, please rename it to ipv6_optjumbo. Jumbo options anomalies.
                        choices:
                            - 'allow'
                            - 'drop'
                            - 'trap-to-host'
                    icmp-land:
                        type: str
                        description: Deprecated, please rename it to icmp_land. ICMP land anomalies.
                        choices:
                            - 'allow'
                            - 'drop'
                            - 'trap-to-host'
                    tcp-winnuke:
                        type: str
                        description: Deprecated, please rename it to tcp_winnuke. TCP WinNuke anomalies.
                        choices:
                            - 'allow'
                            - 'drop'
                            - 'trap-to-host'
                    ipv6-daddr-err:
                        type: str
                        description: Deprecated, please rename it to ipv6_daddr_err. Destination address as unspecified or loopback address anomalies.
                        choices:
                            - 'allow'
                            - 'drop'
                            - 'trap-to-host'
                    ipv4-land:
                        type: str
                        description: Deprecated, please rename it to ipv4_land. Land anomalies.
                        choices:
                            - 'allow'
                            - 'drop'
                            - 'trap-to-host'
                    ipv6-opttunnel:
                        type: str
                        description: Deprecated, please rename it to ipv6_opttunnel. Tunnel encapsulation limit option anomalies.
                        choices:
                            - 'allow'
                            - 'drop'
                            - 'trap-to-host'
                    tcp-no-flag:
                        type: str
                        description: Deprecated, please rename it to tcp_no_flag. TCP SYN flood with no flag set anomalies.
                        choices:
                            - 'allow'
                            - 'drop'
                            - 'trap-to-host'
                    ipv6-land:
                        type: str
                        description: Deprecated, please rename it to ipv6_land. Land anomalies.
                        choices:
                            - 'allow'
                            - 'drop'
                            - 'trap-to-host'
                    ipv4-optlsrr:
                        type: str
                        description: Deprecated, please rename it to ipv4_optlsrr. Loose source record route option anomalies.
                        choices:
                            - 'allow'
                            - 'drop'
                            - 'trap-to-host'
                    ipv4-opttimestamp:
                        type: str
                        description: Deprecated, please rename it to ipv4_opttimestamp. Timestamp option anomalies.
                        choices:
                            - 'allow'
                            - 'drop'
                            - 'trap-to-host'
                    ipv4-optrr:
                        type: str
                        description: Deprecated, please rename it to ipv4_optrr. Record route option anomalies.
                        choices:
                            - 'allow'
                            - 'drop'
                            - 'trap-to-host'
                    ipv6-optnsap:
                        type: str
                        description: Deprecated, please rename it to ipv6_optnsap. Network service access point address option anomalies.
                        choices:
                            - 'allow'
                            - 'drop'
                            - 'trap-to-host'
                    ipv6-unknopt:
                        type: str
                        description: Deprecated, please rename it to ipv6_unknopt. Unknown option anomalies.
                        choices:
                            - 'allow'
                            - 'drop'
                            - 'trap-to-host'
                    tcp-syn-data:
                        type: str
                        description: Deprecated, please rename it to tcp_syn_data. TCP SYN flood packets with data anomalies.
                        choices:
                            - 'allow'
                            - 'drop'
                            - 'trap-to-host'
                    ipv6-optendpid:
                        type: str
                        description: Deprecated, please rename it to ipv6_optendpid. End point identification anomalies.
                        choices:
                            - 'allow'
                            - 'drop'
                            - 'trap-to-host'
                    gtpu-plen-err:
                        type: str
                        description: Deprecated, please rename it to gtpu_plen_err. Gtpu plen err.
                        choices:
                            - 'drop'
                            - 'trap-to-host'
                    vxlan-minlen-err:
                        type: str
                        description: Deprecated, please rename it to vxlan_minlen_err. Vxlan minlen err.
                        choices:
                            - 'drop'
                            - 'trap-to-host'
                    capwap-minlen-err:
                        type: str
                        description: Deprecated, please rename it to capwap_minlen_err. Capwap minlen err.
                        choices:
                            - 'drop'
                            - 'trap-to-host'
                    gre-csum-err:
                        type: str
                        description: Deprecated, please rename it to gre_csum_err. Gre csum err.
                        choices:
                            - 'drop'
                            - 'trap-to-host'
                    nvgre-minlen-err:
                        type: str
                        description: Deprecated, please rename it to nvgre_minlen_err. Nvgre minlen err.
                        choices:
                            - 'drop'
                            - 'trap-to-host'
                    sctp-l4len-err:
                        type: str
                        description: Deprecated, please rename it to sctp_l4len_err. Sctp l4len err.
                        choices:
                            - 'drop'
                            - 'trap-to-host'
                    tcp-hlenvsl4len-err:
                        type: str
                        description: Deprecated, please rename it to tcp_hlenvsl4len_err. Tcp hlenvsl4len err.
                        choices:
                            - 'drop'
                            - 'trap-to-host'
                    sctp-crc-err:
                        type: str
                        description: Deprecated, please rename it to sctp_crc_err. Sctp crc err.
                        choices:
                            - 'drop'
                            - 'trap-to-host'
                    sctp-clen-err:
                        type: str
                        description: Deprecated, please rename it to sctp_clen_err. Sctp clen err.
                        choices:
                            - 'drop'
                            - 'trap-to-host'
                    uesp-minlen-err:
                        type: str
                        description: Deprecated, please rename it to uesp_minlen_err. Uesp minlen err.
                        choices:
                            - 'drop'
                            - 'trap-to-host'
                    sctp-csum-err:
                        type: str
                        description: Deprecated, please rename it to sctp_csum_err. Invalid IPv4 SCTP checksum anomalies.
                        choices:
                            - 'allow'
                            - 'drop'
                            - 'trap-to-host'
            gtp-enhanced-cpu-range:
                type: str
                description: Deprecated, please rename it to gtp_enhanced_cpu_range. GTP enhanced CPU range option.
                choices:
                    - '0'
                    - '1'
                    - '2'
            gtp-enhanced-mode:
                type: str
                description: Deprecated, please rename it to gtp_enhanced_mode. Enable/disable GTP enhanced mode.
                choices:
                    - 'disable'
                    - 'enable'
            host-shortcut-mode:
                type: str
                description: Deprecated, please rename it to host_shortcut_mode. Set np6 host shortcut mode.
                choices:
                    - 'bi-directional'
                    - 'host-shortcut'
            htx-gtse-quota:
                type: str
                description: Deprecated, please rename it to htx_gtse_quota. Configure HTX GTSE quota.
                choices:
                    - '100Mbps'
                    - '200Mbps'
                    - '300Mbps'
                    - '400Mbps'
                    - '500Mbps'
                    - '600Mbps'
                    - '700Mbps'
                    - '800Mbps'
                    - '900Mbps'
                    - '1Gbps'
                    - '2Gbps'
                    - '4Gbps'
                    - '8Gbps'
                    - '10Gbps'
            intf-shaping-offload:
                type: str
                description: Deprecated, please rename it to intf_shaping_offload. Enable/disable NPU offload when doing interface-based traffic shapin...
                choices:
                    - 'disable'
                    - 'enable'
            iph-rsvd-re-cksum:
                type: str
                description: Deprecated, please rename it to iph_rsvd_re_cksum. Enable/disable IP checksum re-calculation for packets with iph.
                choices:
                    - 'disable'
                    - 'enable'
            ipsec-dec-subengine-mask:
                type: str
                description: Deprecated, please rename it to ipsec_dec_subengine_mask. IPsec decryption subengine mask
            ipsec-enc-subengine-mask:
                type: str
                description: Deprecated, please rename it to ipsec_enc_subengine_mask. IPsec encryption subengine mask
            ipsec-inbound-cache:
                type: str
                description: Deprecated, please rename it to ipsec_inbound_cache. Enable/disable IPsec inbound cache for anti-replay.
                choices:
                    - 'disable'
                    - 'enable'
            ipsec-mtu-override:
                type: str
                description: Deprecated, please rename it to ipsec_mtu_override. Enable/disable NP6 IPsec MTU override.
                choices:
                    - 'disable'
                    - 'enable'
            ipsec-over-vlink:
                type: str
                description: Deprecated, please rename it to ipsec_over_vlink. Enable/disable IPSEC over vlink.
                choices:
                    - 'disable'
                    - 'enable'
            isf-np-queues:
                type: dict
                description: Deprecated, please rename it to isf_np_queues. Isf np queues.
                suboptions:
                    cos0:
                        type: str
                        description: CoS profile name for CoS 0.
                    cos1:
                        type: str
                        description: CoS profile name for CoS 1.
                    cos2:
                        type: str
                        description: CoS profile name for CoS 2.
                    cos3:
                        type: str
                        description: CoS profile name for CoS 3.
                    cos4:
                        type: str
                        description: CoS profile name for CoS 4.
                    cos5:
                        type: str
                        description: CoS profile name for CoS 5.
                    cos6:
                        type: str
                        description: CoS profile name for CoS 6.
                    cos7:
                        type: str
                        description: CoS profile name for CoS 7.
            lag-out-port-select:
                type: str
                description: Deprecated, please rename it to lag_out_port_select. Enable/disable LAG outgoing port selection based on incoming traffic ...
                choices:
                    - 'disable'
                    - 'enable'
            mcast-session-accounting:
                type: str
                description: Deprecated, please rename it to mcast_session_accounting. Enable/disable traffic accounting for each multicast session thr...
                choices:
                    - 'disable'
                    - 'session-based'
                    - 'tpe-based'
            np6-cps-optimization-mode:
                type: str
                description: Deprecated, please rename it to np6_cps_optimization_mode. Enable/disable NP6 connection per second
                choices:
                    - 'disable'
                    - 'enable'
            per-session-accounting:
                type: str
                description: Deprecated, please rename it to per_session_accounting. Enable/disable per-session accounting.
                choices:
                    - 'enable'
                    - 'disable'
                    - 'enable-by-log'
                    - 'all-enable'
                    - 'traffic-log-only'
            port-cpu-map:
                type: list
                elements: dict
                description: Deprecated, please rename it to port_cpu_map. Port cpu map.
                suboptions:
                    cpu-core:
                        type: str
                        description: Deprecated, please rename it to cpu_core. The CPU core to map to an interface.
                    interface:
                        type: str
                        description: The interface to map to a CPU core.
            port-npu-map:
                type: list
                elements: dict
                description: Deprecated, please rename it to port_npu_map. Port npu map.
                suboptions:
                    interface:
                        type: str
                        description: Set npu interface port to NPU group map.
                    npu-group-index:
                        type: int
                        description: Deprecated, please rename it to npu_group_index. Mapping NPU group index.
            priority-protocol:
                type: dict
                description: Deprecated, please rename it to priority_protocol. Priority protocol.
                suboptions:
                    bfd:
                        type: str
                        description: Enable/disable NPU BFD priority protocol.
                        choices:
                            - 'disable'
                            - 'enable'
                    bgp:
                        type: str
                        description: Enable/disable NPU BGP priority protocol.
                        choices:
                            - 'disable'
                            - 'enable'
                    slbc:
                        type: str
                        description: Enable/disable NPU SLBC priority protocol.
                        choices:
                            - 'disable'
                            - 'enable'
            qos-mode:
                type: str
                description: Deprecated, please rename it to qos_mode. QoS mode on switch and NP.
                choices:
                    - 'disable'
                    - 'priority'
                    - 'round-robin'
            rdp-offload:
                type: str
                description: Deprecated, please rename it to rdp_offload. Enable/disable rdp offload.
                choices:
                    - 'disable'
                    - 'enable'
            recover-np6-link:
                type: str
                description: Deprecated, please rename it to recover_np6_link. Enable/disable internal link failure check and recovery after boot up.
                choices:
                    - 'disable'
                    - 'enable'
            session-denied-offload:
                type: str
                description: Deprecated, please rename it to session_denied_offload. Enable/disable offloading of denied sessions.
                choices:
                    - 'disable'
                    - 'enable'
            sse-backpressure:
                type: str
                description: Deprecated, please rename it to sse_backpressure. Enable/disable sse backpressure.
                choices:
                    - 'disable'
                    - 'enable'
            strip-clear-text-padding:
                type: str
                description: Deprecated, please rename it to strip_clear_text_padding. Enable/disable stripping clear text padding.
                choices:
                    - 'disable'
                    - 'enable'
            strip-esp-padding:
                type: str
                description: Deprecated, please rename it to strip_esp_padding. Enable/disable stripping ESP padding.
                choices:
                    - 'disable'
                    - 'enable'
            sw-eh-hash:
                type: dict
                description: Deprecated, please rename it to sw_eh_hash. Sw eh hash.
                suboptions:
                    computation:
                        type: str
                        description: Set hashing computation.
                        choices:
                            - 'xor16'
                            - 'xor8'
                            - 'xor4'
                            - 'crc16'
                    destination-ip-lower-16:
                        type: str
                        description: Deprecated, please rename it to destination_ip_lower_16. Include/exclude destination IP address lower 16 bits.
                        choices:
                            - 'include'
                            - 'exclude'
                    destination-ip-upper-16:
                        type: str
                        description: Deprecated, please rename it to destination_ip_upper_16. Include/exclude destination IP address upper 16 bits.
                        choices:
                            - 'include'
                            - 'exclude'
                    destination-port:
                        type: str
                        description: Deprecated, please rename it to destination_port. Include/exclude destination port if TCP/UDP.
                        choices:
                            - 'include'
                            - 'exclude'
                    ip-protocol:
                        type: str
                        description: Deprecated, please rename it to ip_protocol. Include/exclude IP protocol.
                        choices:
                            - 'include'
                            - 'exclude'
                    netmask-length:
                        type: int
                        description: Deprecated, please rename it to netmask_length. Network mask length.
                    source-ip-lower-16:
                        type: str
                        description: Deprecated, please rename it to source_ip_lower_16. Include/exclude source IP address lower 16 bits.
                        choices:
                            - 'include'
                            - 'exclude'
                    source-ip-upper-16:
                        type: str
                        description: Deprecated, please rename it to source_ip_upper_16. Include/exclude source IP address upper 16 bits.
                        choices:
                            - 'include'
                            - 'exclude'
                    source-port:
                        type: str
                        description: Deprecated, please rename it to source_port. Include/exclude source port if TCP/UDP.
                        choices:
                            - 'include'
                            - 'exclude'
            sw-np-bandwidth:
                type: str
                description: Deprecated, please rename it to sw_np_bandwidth. Bandwidth from switch to NP.
                choices:
                    - '0G'
                    - '2G'
                    - '4G'
                    - '5G'
                    - '6G'
                    - '7G'
                    - '8G'
                    - '9G'
            switch-np-hash:
                type: str
                description: Deprecated, please rename it to switch_np_hash. Switch-NP trunk port selection Criteria.
                choices:
                    - 'src-ip'
                    - 'dst-ip'
                    - 'src-dst-ip'
            uesp-offload:
                type: str
                description: Deprecated, please rename it to uesp_offload. Enable/disable UDP-encapsulated ESP offload
                choices:
                    - 'disable'
                    - 'enable'
            np-queues:
                type: dict
                description: Deprecated, please rename it to np_queues. Np queues.
                suboptions:
                    ethernet-type:
                        type: list
                        elements: dict
                        description: Deprecated, please rename it to ethernet_type. Ethernet type.
                        suboptions:
                            name:
                                type: str
                                description: Ethernet Type Name.
                            queue:
                                type: int
                                description: Queue Number.
                            type:
                                type: int
                                description: Ethernet Type.
                            weight:
                                type: int
                                description: Class Weight.
                    ip-protocol:
                        type: list
                        elements: dict
                        description: Deprecated, please rename it to ip_protocol. Ip protocol.
                        suboptions:
                            name:
                                type: str
                                description: IP Protocol Name.
                            protocol:
                                type: int
                                description: IP Protocol.
                            queue:
                                type: int
                                description: Queue Number.
                            weight:
                                type: int
                                description: Class Weight.
                    ip-service:
                        type: list
                        elements: dict
                        description: Deprecated, please rename it to ip_service. Ip service.
                        suboptions:
                            dport:
                                type: int
                                description: Destination port.
                            name:
                                type: str
                                description: IP service name.
                            protocol:
                                type: int
                                description: IP protocol.
                            queue:
                                type: int
                                description: Queue number.
                            sport:
                                type: int
                                description: Source port.
                            weight:
                                type: int
                                description: Class weight.
                    profile:
                        type: list
                        elements: dict
                        description: Profile.
                        suboptions:
                            cos0:
                                type: str
                                description: Queue number of CoS 0.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            cos1:
                                type: str
                                description: Queue number of CoS 1.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            cos2:
                                type: str
                                description: Queue number of CoS 2.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            cos3:
                                type: str
                                description: Queue number of CoS 3.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            cos4:
                                type: str
                                description: Queue number of CoS 4.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            cos5:
                                type: str
                                description: Queue number of CoS 5.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            cos6:
                                type: str
                                description: Queue number of CoS 6.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            cos7:
                                type: str
                                description: Queue number of CoS 7.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp0:
                                type: str
                                description: Queue number of DSCP 0.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp1:
                                type: str
                                description: Queue number of DSCP 1.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp10:
                                type: str
                                description: Queue number of DSCP 10.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp11:
                                type: str
                                description: Queue number of DSCP 11.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp12:
                                type: str
                                description: Queue number of DSCP 12.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp13:
                                type: str
                                description: Queue number of DSCP 13.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp14:
                                type: str
                                description: Queue number of DSCP 14.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp15:
                                type: str
                                description: Queue number of DSCP 15.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp16:
                                type: str
                                description: Queue number of DSCP 16.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp17:
                                type: str
                                description: Queue number of DSCP 17.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp18:
                                type: str
                                description: Queue number of DSCP 18.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp19:
                                type: str
                                description: Queue number of DSCP 19.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp2:
                                type: str
                                description: Queue number of DSCP 2.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp20:
                                type: str
                                description: Queue number of DSCP 20.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp21:
                                type: str
                                description: Queue number of DSCP 21.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp22:
                                type: str
                                description: Queue number of DSCP 22.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp23:
                                type: str
                                description: Queue number of DSCP 23.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp24:
                                type: str
                                description: Queue number of DSCP 24.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp25:
                                type: str
                                description: Queue number of DSCP 25.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp26:
                                type: str
                                description: Queue number of DSCP 26.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp27:
                                type: str
                                description: Queue number of DSCP 27.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp28:
                                type: str
                                description: Queue number of DSCP 28.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp29:
                                type: str
                                description: Queue number of DSCP 29.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp3:
                                type: str
                                description: Queue number of DSCP 3.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp30:
                                type: str
                                description: Queue number of DSCP 30.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp31:
                                type: str
                                description: Queue number of DSCP 31.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp32:
                                type: str
                                description: Queue number of DSCP 32.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp33:
                                type: str
                                description: Queue number of DSCP 33.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp34:
                                type: str
                                description: Queue number of DSCP 34.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp35:
                                type: str
                                description: Queue number of DSCP 35.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp36:
                                type: str
                                description: Queue number of DSCP 36.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp37:
                                type: str
                                description: Queue number of DSCP 37.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp38:
                                type: str
                                description: Queue number of DSCP 38.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp39:
                                type: str
                                description: Queue number of DSCP 39.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp4:
                                type: str
                                description: Queue number of DSCP 4.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp40:
                                type: str
                                description: Queue number of DSCP 40.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp41:
                                type: str
                                description: Queue number of DSCP 41.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp42:
                                type: str
                                description: Queue number of DSCP 42.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp43:
                                type: str
                                description: Queue number of DSCP 43.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp44:
                                type: str
                                description: Queue number of DSCP 44.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp45:
                                type: str
                                description: Queue number of DSCP 45.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp46:
                                type: str
                                description: Queue number of DSCP 46.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp47:
                                type: str
                                description: Queue number of DSCP 47.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp48:
                                type: str
                                description: Queue number of DSCP 48.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp49:
                                type: str
                                description: Queue number of DSCP 49.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp5:
                                type: str
                                description: Queue number of DSCP 5.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp50:
                                type: str
                                description: Queue number of DSCP 50.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp51:
                                type: str
                                description: Queue number of DSCP 51.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp52:
                                type: str
                                description: Queue number of DSCP 52.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp53:
                                type: str
                                description: Queue number of DSCP 53.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp54:
                                type: str
                                description: Queue number of DSCP 54.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp55:
                                type: str
                                description: Queue number of DSCP 55.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp56:
                                type: str
                                description: Queue number of DSCP 56.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp57:
                                type: str
                                description: Queue number of DSCP 57.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp58:
                                type: str
                                description: Queue number of DSCP 58.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp59:
                                type: str
                                description: Queue number of DSCP 59.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp6:
                                type: str
                                description: Queue number of DSCP 6.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp60:
                                type: str
                                description: Queue number of DSCP 60.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp61:
                                type: str
                                description: Queue number of DSCP 61.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp62:
                                type: str
                                description: Queue number of DSCP 62.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp63:
                                type: str
                                description: Queue number of DSCP 63.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp7:
                                type: str
                                description: Queue number of DSCP 7.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp8:
                                type: str
                                description: Queue number of DSCP 8.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            dscp9:
                                type: str
                                description: Queue number of DSCP 9.
                                choices:
                                    - 'queue0'
                                    - 'queue1'
                                    - 'queue2'
                                    - 'queue3'
                                    - 'queue4'
                                    - 'queue5'
                                    - 'queue6'
                                    - 'queue7'
                            id:
                                type: int
                                description: Profile ID.
                            type:
                                type: str
                                description: Profile type.
                                choices:
                                    - 'cos'
                                    - 'dscp'
                            weight:
                                type: int
                                description: Class weight.
                    scheduler:
                        type: list
                        elements: dict
                        description: Scheduler.
                        suboptions:
                            mode:
                                type: str
                                description: Scheduler mode.
                                choices:
                                    - 'none'
                                    - 'priority'
                                    - 'round-robin'
                            name:
                                type: str
                                description: Scheduler name.
            udp-timeout-profile:
                type: list
                elements: dict
                description: Deprecated, please rename it to udp_timeout_profile. Udp timeout profile.
                suboptions:
                    id:
                        type: int
                        description: Timeout profile ID
                    udp-idle:
                        type: int
                        description: Deprecated, please rename it to udp_idle. Set UDP idle timeout
            qtm-buf-mode:
                type: str
                description: Deprecated, please rename it to qtm_buf_mode. QTM channel configuration for packet buffer.
                choices:
                    - '6ch'
                    - '4ch'
            default-qos-type:
                type: str
                description: Deprecated, please rename it to default_qos_type. Set default QoS type.
                choices:
                    - 'policing'
                    - 'shaping'
                    - 'policing-enhanced'
            tcp-rst-timeout:
                type: int
                description: Deprecated, please rename it to tcp_rst_timeout. TCP RST timeout in seconds
            ipsec-local-uesp-port:
                type: int
                description: Deprecated, please rename it to ipsec_local_uesp_port. Ipsec local uesp port.
            htab-dedi-queue-nr:
                type: int
                description: Deprecated, please rename it to htab_dedi_queue_nr. Set the number of dedicate queue for hash table messages.
            double-level-mcast-offload:
                type: str
                description: Deprecated, please rename it to double_level_mcast_offload. Enable double level mcast offload.
                choices:
                    - 'disable'
                    - 'enable'
            dse-timeout:
                type: int
                description: Deprecated, please rename it to dse_timeout. DSE timeout in seconds
            ippool-overload-low:
                type: int
                description: Deprecated, please rename it to ippool_overload_low. Low threshold for overload ippool port reuse
            pba-eim:
                type: str
                description: Deprecated, please rename it to pba_eim. Configure option for PBA
                choices:
                    - 'disallow'
                    - 'allow'
            policy-offload-level:
                type: str
                description: Deprecated, please rename it to policy_offload_level. Configure firewall policy offload level
                choices:
                    - 'disable'
                    - 'dos-offload'
                    - 'full-offload'
            max-session-timeout:
                type: int
                description: Deprecated, please rename it to max_session_timeout. Maximum time interval for refreshing NPU-offloaded sessions
            port-path-option:
                type: dict
                description: Deprecated, please rename it to port_path_option. Port path option.
                suboptions:
                    ports-using-npu:
                        type: raw
                        description: (list) Deprecated, please rename it to ports_using_npu. Set ha/aux ports to handle traffic with NPU
            vlan-lookup-cache:
                type: str
                description: Deprecated, please rename it to vlan_lookup_cache. Enable/disable vlan lookup cache
                choices:
                    - 'disable'
                    - 'enable'
            dos-options:
                type: dict
                description: Deprecated, please rename it to dos_options. Dos options.
                suboptions:
                    npu-dos-meter-mode:
                        type: str
                        description: Deprecated, please rename it to npu_dos_meter_mode. Set DoS meter NPU offloading mode.
                        choices:
                            - 'local'
                            - 'global'
                    npu-dos-synproxy-mode:
                        type: str
                        description: Deprecated, please rename it to npu_dos_synproxy_mode. Set NPU DoS SYNPROXY mode.
                        choices:
                            - 'synack2ack'
                            - 'pass-synack'
                    npu-dos-tpe-mode:
                        type: str
                        description: Deprecated, please rename it to npu_dos_tpe_mode. Enable/disable insertion of DoS meter ID to session table.
                        choices:
                            - 'disable'
                            - 'enable'
            hash-tbl-spread:
                type: str
                description: Deprecated, please rename it to hash_tbl_spread. Enable/disable hash table entry spread
                choices:
                    - 'disable'
                    - 'enable'
            tcp-timeout-profile:
                type: list
                elements: dict
                description: Deprecated, please rename it to tcp_timeout_profile. Tcp timeout profile.
                suboptions:
                    close-wait:
                        type: int
                        description: Deprecated, please rename it to close_wait. Set close-wait timeout
                    fin-wait:
                        type: int
                        description: Deprecated, please rename it to fin_wait. Set fin-wait timeout
                    id:
                        type: int
                        description: Timeout profile ID
                    syn-sent:
                        type: int
                        description: Deprecated, please rename it to syn_sent. Set syn-sent timeout
                    syn-wait:
                        type: int
                        description: Deprecated, please rename it to syn_wait. Set syn-wait timeout
                    tcp-idle:
                        type: int
                        description: Deprecated, please rename it to tcp_idle. Set TCP establish timeout
                    time-wait:
                        type: int
                        description: Deprecated, please rename it to time_wait. Set time-wait timeout
            ip-reassembly:
                type: dict
                description: Deprecated, please rename it to ip_reassembly. Ip reassembly.
                suboptions:
                    max-timeout:
                        type: int
                        description: Deprecated, please rename it to max_timeout. Maximum timeout value for IP reassembly
                    min-timeout:
                        type: int
                        description: Deprecated, please rename it to min_timeout. Minimum timeout value for IP reassembly
                    status:
                        type: str
                        description: Set IP reassembly processing status.
                        choices:
                            - 'disable'
                            - 'enable'
            gtp-support:
                type: str
                description: Deprecated, please rename it to gtp_support. Enable/Disable NP7 GTP support
                choices:
                    - 'disable'
                    - 'enable'
            htx-icmp-csum-chk:
                type: str
                description: Deprecated, please rename it to htx_icmp_csum_chk. Set HTX icmp csum checking mode.
                choices:
                    - 'pass'
                    - 'drop'
            hpe:
                type: dict
                description: Hpe.
                suboptions:
                    all-protocol:
                        type: int
                        description: Deprecated, please rename it to all_protocol. Maximum packet rate of each host queue except high priority traffic
                    arp-max:
                        type: int
                        description: Deprecated, please rename it to arp_max. Maximum ARP packet rate
                    enable-shaper:
                        type: str
                        description: Deprecated, please rename it to enable_shaper. Enable/Disable NPU Host Protection Engine
                        choices:
                            - 'disable'
                            - 'enable'
                    esp-max:
                        type: int
                        description: Deprecated, please rename it to esp_max. Maximum ESP packet rate
                    high-priority:
                        type: int
                        description: Deprecated, please rename it to high_priority. Maximum packet rate for high priority traffic packets
                    icmp-max:
                        type: int
                        description: Deprecated, please rename it to icmp_max. Maximum ICMP packet rate
                    ip-frag-max:
                        type: int
                        description: Deprecated, please rename it to ip_frag_max. Maximum fragmented IP packet rate
                    ip-others-max:
                        type: int
                        description: Deprecated, please rename it to ip_others_max. Maximum IP packet rate for other packets
                    l2-others-max:
                        type: int
                        description: Deprecated, please rename it to l2_others_max. Maximum L2 packet rate for L2 packets that are not ARP packets
                    pri-type-max:
                        type: int
                        description: Deprecated, please rename it to pri_type_max. Maximum overflow rate of priority type traffic
                    sctp-max:
                        type: int
                        description: Deprecated, please rename it to sctp_max. Maximum SCTP packet rate
                    tcp-max:
                        type: int
                        description: Deprecated, please rename it to tcp_max. Maximum TCP packet rate
                    tcpfin-rst-max:
                        type: int
                        description: Deprecated, please rename it to tcpfin_rst_max. Maximum TCP carries FIN or RST flags packet rate
                    tcpsyn-ack-max:
                        type: int
                        description: Deprecated, please rename it to tcpsyn_ack_max. Maximum TCP carries SYN and ACK flags packet rate
                    tcpsyn-max:
                        type: int
                        description: Deprecated, please rename it to tcpsyn_max. Maximum TCP SYN packet rate
                    udp-max:
                        type: int
                        description: Deprecated, please rename it to udp_max. Maximum UDP packet rate
                    enable-queue-shaper:
                        type: str
                        description: Deprecated, please rename it to enable_queue_shaper. Enable/Disable NPU host protection engine
                        choices:
                            - 'disable'
                            - 'enable'
                    exception-code:
                        type: int
                        description: Deprecated, please rename it to exception_code. Maximum exception code rate of traffic
                    fragment-with-sess:
                        type: int
                        description: Deprecated, please rename it to fragment_with_sess. Maximum fragment with session rate of traffic
                    fragment-without-session:
                        type: int
                        description: Deprecated, please rename it to fragment_without_session. Maximum fragment without session rate of traffic
                    queue-shaper-max:
                        type: int
                        description: Deprecated, please rename it to queue_shaper_max. Maximum per queue byte rate of traffic
            dsw-dts-profile:
                type: list
                elements: dict
                description: Deprecated, please rename it to dsw_dts_profile. Dsw dts profile.
                suboptions:
                    action:
                        type: str
                        description: Set NPU DSW DTS profile action.
                        choices:
                            - 'wait'
                            - 'drop'
                            - 'drop_tmr_0'
                            - 'drop_tmr_1'
                            - 'enque'
                            - 'enque_0'
                            - 'enque_1'
                    min-limit:
                        type: int
                        description: Deprecated, please rename it to min_limit. Set NPU DSW DTS profile min-limt.
                    profile-id:
                        type: int
                        description: Deprecated, please rename it to profile_id. Set NPU DSW DTS profile profile id.
                    step:
                        type: int
                        description: Set NPU DSW DTS profile step.
            hash-config:
                type: str
                description: Deprecated, please rename it to hash_config. Configure NPU trunk hash.
                choices:
                    - '5-tuple'
                    - 'src-ip'
                    - 'src-dst-ip'
            ipsec-ob-np-sel:
                type: str
                description: Deprecated, please rename it to ipsec_ob_np_sel. IPsec NP selection for OB SA offloading.
                choices:
                    - 'RR'
                    - 'rr'
                    - 'Packet'
                    - 'Hash'
            napi-break-interval:
                type: int
                description: Deprecated, please rename it to napi_break_interval. NAPI break interval
            background-sse-scan:
                type: dict
                description: Deprecated, please rename it to background_sse_scan. Background sse scan.
                suboptions:
                    scan:
                        type: str
                        description: Enable/disable background SSE scan by driver thread
                        choices:
                            - 'disable'
                            - 'enable'
                    stats-update-interval:
                        type: int
                        description: Deprecated, please rename it to stats_update_interval. Stats update interval
                    udp-keepalive-interval:
                        type: int
                        description: Deprecated, please rename it to udp_keepalive_interval. UDP keepalive interval
                    scan-stale:
                        type: int
                        description: Deprecated, please rename it to scan_stale. Configure scanning of active or stale sessions
                    scan-vt:
                        type: int
                        description: Deprecated, please rename it to scan_vt. Select version/type to scan
                    stats-qual-access:
                        type: int
                        description: Deprecated, please rename it to stats_qual_access. Statistics update access qualification in seconds
                    stats-qual-duration:
                        type: int
                        description: Deprecated, please rename it to stats_qual_duration. Statistics update duration qualification in seconds
                    udp-qual-access:
                        type: int
                        description: Deprecated, please rename it to udp_qual_access. UDP keepalive access qualification in seconds
                    udp-qual-duration:
                        type: int
                        description: Deprecated, please rename it to udp_qual_duration. UDP keepalive duration qualification in seconds
            inbound-dscp-copy-port:
                type: raw
                description: (list) Deprecated, please rename it to inbound_dscp_copy_port. Physical interfaces that support inbound-dscp-copy.
            session-acct-interval:
                type: int
                description: Deprecated, please rename it to session_acct_interval. Session accounting update interval
            htab-msg-queue:
                type: str
                description: Deprecated, please rename it to htab_msg_queue. Set hash table message queue mode.
                choices:
                    - 'idle'
                    - 'data'
                    - 'dedicated'
            dsw-queue-dts-profile:
                type: list
                elements: dict
                description: Deprecated, please rename it to dsw_queue_dts_profile. Dsw queue dts profile.
                suboptions:
                    iport:
                        type: str
                        description: Set NPU DSW DTS in port.
                        choices:
                            - 'EIF0'
                            - 'eif0'
                            - 'EIF1'
                            - 'eif1'
                            - 'EIF2'
                            - 'eif2'
                            - 'EIF3'
                            - 'eif3'
                            - 'EIF4'
                            - 'eif4'
                            - 'EIF5'
                            - 'eif5'
                            - 'EIF6'
                            - 'eif6'
                            - 'EIF7'
                            - 'eif7'
                            - 'HTX0'
                            - 'htx0'
                            - 'HTX1'
                            - 'htx1'
                            - 'SSE0'
                            - 'sse0'
                            - 'SSE1'
                            - 'sse1'
                            - 'SSE2'
                            - 'sse2'
                            - 'SSE3'
                            - 'sse3'
                            - 'RLT'
                            - 'rlt'
                            - 'DFR'
                            - 'dfr'
                            - 'IPSECI'
                            - 'ipseci'
                            - 'IPSECO'
                            - 'ipseco'
                            - 'IPTI'
                            - 'ipti'
                            - 'IPTO'
                            - 'ipto'
                            - 'VEP0'
                            - 'vep0'
                            - 'VEP2'
                            - 'vep2'
                            - 'VEP4'
                            - 'vep4'
                            - 'VEP6'
                            - 'vep6'
                            - 'IVS'
                            - 'ivs'
                            - 'L2TI1'
                            - 'l2ti1'
                            - 'L2TO'
                            - 'l2to'
                            - 'L2TI0'
                            - 'l2ti0'
                            - 'PLE'
                            - 'ple'
                            - 'SPATH'
                            - 'spath'
                            - 'QTM'
                            - 'qtm'
                    name:
                        type: str
                        description: Name.
                    oport:
                        type: str
                        description: Set NPU DSW DTS out port.
                        choices:
                            - 'EIF0'
                            - 'eif0'
                            - 'EIF1'
                            - 'eif1'
                            - 'EIF2'
                            - 'eif2'
                            - 'EIF3'
                            - 'eif3'
                            - 'EIF4'
                            - 'eif4'
                            - 'EIF5'
                            - 'eif5'
                            - 'EIF6'
                            - 'eif6'
                            - 'EIF7'
                            - 'eif7'
                            - 'HRX'
                            - 'hrx'
                            - 'SSE0'
                            - 'sse0'
                            - 'SSE1'
                            - 'sse1'
                            - 'SSE2'
                            - 'sse2'
                            - 'SSE3'
                            - 'sse3'
                            - 'RLT'
                            - 'rlt'
                            - 'DFR'
                            - 'dfr'
                            - 'IPSECI'
                            - 'ipseci'
                            - 'IPSECO'
                            - 'ipseco'
                            - 'IPTI'
                            - 'ipti'
                            - 'IPTO'
                            - 'ipto'
                            - 'VEP0'
                            - 'vep0'
                            - 'VEP2'
                            - 'vep2'
                            - 'VEP4'
                            - 'vep4'
                            - 'VEP6'
                            - 'vep6'
                            - 'IVS'
                            - 'ivs'
                            - 'L2TI1'
                            - 'l2ti1'
                            - 'L2TO'
                            - 'l2to'
                            - 'L2TI0'
                            - 'l2ti0'
                            - 'PLE'
                            - 'ple'
                            - 'SYNK'
                            - 'sync'
                            - 'NSS'
                            - 'nss'
                            - 'TSK'
                            - 'tsk'
                            - 'QTM'
                            - 'qtm'
                            - 'l2tO'
                    profile-id:
                        type: int
                        description: Deprecated, please rename it to profile_id. Set NPU DSW DTS profile ID.
                    queue-select:
                        type: int
                        description: Deprecated, please rename it to queue_select. Set NPU DSW DTS queue ID select
            hw-ha-scan-interval:
                type: int
                description: Deprecated, please rename it to hw_ha_scan_interval. HW HA periodical scan interval in seconds
            ippool-overload-high:
                type: int
                description: Deprecated, please rename it to ippool_overload_high. High threshold for overload ippool port reuse
            nat46-force-ipv4-packet-forwarding:
                type: str
                description: Deprecated, please rename it to nat46_force_ipv4_packet_forwarding. Enable/disable mandatory IPv4 packet forwarding in nat46.
                choices:
                    - 'disable'
                    - 'enable'
            prp-port-out:
                type: raw
                description: (list or str) Deprecated, please rename it to prp_port_out. Egress port configured to allow the PRP trailer not be strippe...
            isf-np-rx-tr-distr:
                type: str
                description: Deprecated, please rename it to isf_np_rx_tr_distr. Select ISF NP Rx trunk distribution
                choices:
                    - 'port-flow'
                    - 'round-robin'
                    - 'randomized'
            mcast-session-counting6:
                type: str
                description: Deprecated, please rename it to mcast_session_counting6. Enable/disable traffic accounting for each multicast session6 thr...
                choices:
                    - 'disable'
                    - 'enable'
                    - 'session-based'
                    - 'tpe-based'
            prp-port-in:
                type: raw
                description: (list or str) Deprecated, please rename it to prp_port_in. Ingress port configured to allow the PRP trailer not be strippe...
            rps-mode:
                type: str
                description: Deprecated, please rename it to rps_mode. Enable/disable receive packet steering
                choices:
                    - 'disable'
                    - 'enable'
            per-policy-accounting:
                type: str
                description: Deprecated, please rename it to per_policy_accounting. Set per-policy accounting.
                choices:
                    - 'disable'
                    - 'enable'
            mcast-session-counting:
                type: str
                description: Deprecated, please rename it to mcast_session_counting. Mcast session counting.
                choices:
                    - 'disable'
                    - 'enable'
                    - 'session-based'
                    - 'tpe-based'
            inbound-dscp-copy:
                type: str
                description: Deprecated, please rename it to inbound_dscp_copy. Enable/disable copying the DSCP field from outer IP header to inner IP ...
                choices:
                    - 'disable'
                    - 'enable'
            ipsec-host-dfclr:
                type: str
                description: Deprecated, please rename it to ipsec_host_dfclr. Enable/disable DF clearing of NP4lite host IPsec offload.
                choices:
                    - 'disable'
                    - 'enable'
            process-icmp-by-host:
                type: str
                description: Deprecated, please rename it to process_icmp_by_host. Enable/disable process ICMP by host when received from IPsec tunnel ...
                choices:
                    - 'disable'
                    - 'enable'
            dedicated-tx-npu:
                type: str
                description: Deprecated, please rename it to dedicated_tx_npu. Enable/disable dedication of 3rd NPU for slow path TX.
                choices:
                    - 'disable'
                    - 'enable'
            ull-port-mode:
                type: str
                description: Deprecated, please rename it to ull_port_mode. Set ULL ports speed to 10G/25G
                choices:
                    - '10G'
                    - '25G'
            sse-ha-scan:
                type: dict
                description: Deprecated, please rename it to sse_ha_scan. Sse ha scan.
                suboptions:
                    gap:
                        type: int
                        description: Scanning message gap
                    max-session-cnt:
                        type: int
                        description: Deprecated, please rename it to max_session_cnt. If the session count
                    min-duration:
                        type: int
                        description: Deprecated, please rename it to min_duration. Scanning filter for minimum duration of the session.
            hash-ipv6-sel:
                type: int
                description: Deprecated, please rename it to hash_ipv6_sel. Select which 4bytes of the IPv6 address are used for traffic hash
            ip-fragment-offload:
                type: str
                description: Deprecated, please rename it to ip_fragment_offload. Enable/disable NP7 NPU IP fragment offload.
                choices:
                    - 'disable'
                    - 'enable'
            ple-non-syn-tcp-action:
                type: str
                description: Deprecated, please rename it to ple_non_syn_tcp_action. Configure action for the PLE to take on TCP packets that have the ...
                choices:
                    - 'forward'
                    - 'drop'
            npu-group-effective-scope:
                type: int
                description: Deprecated, please rename it to npu_group_effective_scope. Npu-group-effective-scope defines under which npu-group cmds su...
            ipsec-STS-timeout:
                type: str
                description: Deprecated, please rename it to ipsec_STS_timeout. Set NP7Lite IPsec STS msg timeout.
                choices:
                    - '1'
                    - '2'
                    - '3'
                    - '4'
                    - '5'
                    - '6'
                    - '7'
                    - '8'
                    - '9'
                    - '10'
            ipsec-throughput-msg-frequency:
                type: str
                description: Deprecated, please rename it to ipsec_throughput_msg_frequency. Set NP7Lite IPsec throughput msg frequency
                choices:
                    - 'disable'
                    - '32KB'
                    - '64KB'
                    - '128KB'
                    - '256KB'
                    - '512KB'
                    - '1MB'
                    - '2MB'
                    - '4MB'
                    - '8MB'
                    - '16MB'
                    - '32MB'
                    - '64MB'
                    - '128MB'
                    - '256MB'
                    - '512MB'
                    - '1GB'
            ipt-STS-timeout:
                type: str
                description: Deprecated, please rename it to ipt_STS_timeout. Set NP7Lite IPT STS msg timeout.
                choices:
                    - '1'
                    - '2'
                    - '3'
                    - '4'
                    - '5'
                    - '6'
                    - '7'
                    - '8'
                    - '9'
                    - '10'
            ipt-throughput-msg-frequency:
                type: str
                description: Deprecated, please rename it to ipt_throughput_msg_frequency. Set NP7Lite IPT throughput msg frequency
                choices:
                    - 'disable'
                    - '32KB'
                    - '64KB'
                    - '128KB'
                    - '256KB'
                    - '512KB'
                    - '1MB'
                    - '2MB'
                    - '4MB'
                    - '8MB'
                    - '16MB'
                    - '32MB'
                    - '64MB'
                    - '128MB'
                    - '256MB'
                    - '512MB'
                    - '1GB'
            default-tcp-refresh-dir:
                type: str
                description: Deprecated, please rename it to default_tcp_refresh_dir. Default SSE timeout TCP refresh direction.
                choices:
                    - 'both'
                    - 'outgoing'
                    - 'incoming'
            default-udp-refresh-dir:
                type: str
                description: Deprecated, please rename it to default_udp_refresh_dir. Default SSE timeout UDP refresh direction.
                choices:
                    - 'both'
                    - 'outgoing'
                    - 'incoming'
            nss-threads-option:
                type: str
                description: Deprecated, please rename it to nss_threads_option. Configure thread options for the NP7s NSS module.
                choices:
                    - '4t-eif'
                    - '4t-noeif'
                    - '2t'
            prp-session-clear-mode:
                type: str
                description: Deprecated, please rename it to prp_session_clear_mode. PRP session clear mode for excluded ip sessions.
                choices:
                    - 'blocking'
                    - 'non-blocking'
                    - 'do-not-clear'
            shaping-stats:
                type: str
                description: Deprecated, please rename it to shaping_stats. Enable/disable NP7 traffic shaping statistics
                choices:
                    - 'disable'
                    - 'enable'
            sw-tr-hash:
                type: dict
                description: Deprecated, please rename it to sw_tr_hash. Sw tr hash.
                suboptions:
                    draco15:
                        type: str
                        description: Enable/disable DRACO15 hashing.
                        choices:
                            - 'disable'
                            - 'enable'
                    tcp-udp-port:
                        type: str
                        description: Deprecated, please rename it to tcp_udp_port. Include/exclude TCP/UDP source and destination port for unicast trun...
                        choices:
                            - 'include'
                            - 'exclude'
            pba-port-select-mode:
                type: str
                description: Deprecated, please rename it to pba_port_select_mode. Port selection mode for PBA IP pool.
                choices:
                    - 'random'
                    - 'direct'
            spa-port-select-mode:
                type: str
                description: Deprecated, please rename it to spa_port_select_mode. Port selection mode for SPA IP pool.
                choices:
                    - 'random'
                    - 'direct'
            split-ipsec-engines:
                type: str
                description: Deprecated, please rename it to split_ipsec_engines. Enable/disable Split IPsec Engines.
                choices:
                    - 'disable'
                    - 'enable'
            tunnel-over-vlink:
                type: str
                description: Deprecated, please rename it to tunnel_over_vlink. Enable/disable selection of which NP6 chip the tunnel uses
                choices:
                    - 'disable'
                    - 'enable'
            max-receive-unit:
                type: int
                description: Deprecated, please rename it to max_receive_unit. Set the maximum packet size for receive, larger packets will be silently...
            npu-tcam:
                type: list
                elements: dict
                description: Deprecated, please rename it to npu_tcam. Npu tcam.
                suboptions:
                    data:
                        type: dict
                        description: Data.
                        suboptions:
                            df:
                                type: str
                                description: Tcam data ip flag df.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            dstip:
                                type: str
                                description: Tcam data dst ipv4 address.
                            dstipv6:
                                type: str
                                description: Tcam data dst ipv6 address.
                            dstmac:
                                type: str
                                description: Tcam data dst macaddr.
                            dstport:
                                type: int
                                description: Tcam data L4 dst port.
                            ethertype:
                                type: str
                                description: Tcam data ethertype.
                            ext-tag:
                                type: str
                                description: Deprecated, please rename it to ext_tag. Tcam data extension tag.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            frag-off:
                                type: int
                                description: Deprecated, please rename it to frag_off. Tcam data ip flag fragment offset.
                            gen-buf-cnt:
                                type: int
                                description: Deprecated, please rename it to gen_buf_cnt. Tcam data gen info buffer count.
                            gen-iv:
                                type: str
                                description: Deprecated, please rename it to gen_iv. Tcam data gen info iv.
                                choices:
                                    - 'invalid'
                                    - 'valid'
                            gen-l3-flags:
                                type: int
                                description: Deprecated, please rename it to gen_l3_flags. Tcam data gen info L3 flags.
                            gen-l4-flags:
                                type: int
                                description: Deprecated, please rename it to gen_l4_flags. Tcam data gen info L4 flags.
                            gen-pkt-ctrl:
                                type: int
                                description: Deprecated, please rename it to gen_pkt_ctrl. Tcam data gen info packet control.
                            gen-pri:
                                type: int
                                description: Deprecated, please rename it to gen_pri. Tcam data gen info priority.
                            gen-pri-v:
                                type: str
                                description: Deprecated, please rename it to gen_pri_v. Tcam data gen info priority valid.
                                choices:
                                    - 'invalid'
                                    - 'valid'
                            gen-tv:
                                type: str
                                description: Deprecated, please rename it to gen_tv. Tcam data gen info tv.
                                choices:
                                    - 'invalid'
                                    - 'valid'
                            ihl:
                                type: int
                                description: Tcam data ipv4 IHL.
                            ip4-id:
                                type: int
                                description: Deprecated, please rename it to ip4_id. Tcam data ipv4 id.
                            ip6-fl:
                                type: int
                                description: Deprecated, please rename it to ip6_fl. Tcam data ipv6 flow label.
                            ipver:
                                type: int
                                description: Tcam data ip header version.
                            l4-wd10:
                                type: int
                                description: Deprecated, please rename it to l4_wd10. Tcam data L4 word10.
                            l4-wd11:
                                type: int
                                description: Deprecated, please rename it to l4_wd11. Tcam data L4 word11.
                            l4-wd8:
                                type: int
                                description: Deprecated, please rename it to l4_wd8. Tcam data L4 word8.
                            l4-wd9:
                                type: int
                                description: Deprecated, please rename it to l4_wd9. Tcam data L4 word9.
                            mf:
                                type: str
                                description: Tcam data ip flag mf.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            protocol:
                                type: int
                                description: Tcam data ip protocol.
                            slink:
                                type: int
                                description: Tcam data sublink.
                            smac-change:
                                type: str
                                description: Deprecated, please rename it to smac_change. Tcam data source MAC change.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            sp:
                                type: int
                                description: Tcam data source port.
                            src-cfi:
                                type: str
                                description: Deprecated, please rename it to src_cfi. Tcam data source cfi.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            src-prio:
                                type: int
                                description: Deprecated, please rename it to src_prio. Tcam data source priority.
                            src-updt:
                                type: str
                                description: Deprecated, please rename it to src_updt. Tcam data source update.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            srcip:
                                type: str
                                description: Tcam data src ipv4 address.
                            srcipv6:
                                type: str
                                description: Tcam data src ipv6 address.
                            srcmac:
                                type: str
                                description: Tcam data src macaddr.
                            srcport:
                                type: int
                                description: Tcam data L4 src port.
                            svid:
                                type: int
                                description: Tcam data source vid.
                            tcp-ack:
                                type: str
                                description: Deprecated, please rename it to tcp_ack. Tcam data tcp flag ack.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            tcp-cwr:
                                type: str
                                description: Deprecated, please rename it to tcp_cwr. Tcam data tcp flag cwr.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            tcp-ece:
                                type: str
                                description: Deprecated, please rename it to tcp_ece. Tcam data tcp flag ece.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            tcp-fin:
                                type: str
                                description: Deprecated, please rename it to tcp_fin. Tcam data tcp flag fin.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            tcp-push:
                                type: str
                                description: Deprecated, please rename it to tcp_push. Tcam data tcp flag push.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            tcp-rst:
                                type: str
                                description: Deprecated, please rename it to tcp_rst. Tcam data tcp flag rst.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            tcp-syn:
                                type: str
                                description: Deprecated, please rename it to tcp_syn. Tcam data tcp flag syn.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            tcp-urg:
                                type: str
                                description: Deprecated, please rename it to tcp_urg. Tcam data tcp flag urg.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            tgt-cfi:
                                type: str
                                description: Deprecated, please rename it to tgt_cfi. Tcam data target cfi.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            tgt-prio:
                                type: int
                                description: Deprecated, please rename it to tgt_prio. Tcam data target priority.
                            tgt-updt:
                                type: str
                                description: Deprecated, please rename it to tgt_updt. Tcam data target port update.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            tgt-v:
                                type: str
                                description: Deprecated, please rename it to tgt_v. Tcam data target valid.
                                choices:
                                    - 'invalid'
                                    - 'valid'
                            tos:
                                type: int
                                description: Tcam data ip tos.
                            tp:
                                type: int
                                description: Tcam data target port.
                            ttl:
                                type: int
                                description: Tcam data ip ttl.
                            tvid:
                                type: int
                                description: Tcam data target vid.
                            vdid:
                                type: int
                                description: Tcam data vdom id.
                    dbg-dump:
                        type: int
                        description: Deprecated, please rename it to dbg_dump. Debug driver dump data/mask pdq.
                    mask:
                        type: dict
                        description: Mask.
                        suboptions:
                            df:
                                type: str
                                description: Tcam mask ip flag df.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            dstip:
                                type: str
                                description: Tcam mask dst ipv4 address.
                            dstipv6:
                                type: str
                                description: Tcam mask dst ipv6 address.
                            dstmac:
                                type: str
                                description: Tcam mask dst macaddr.
                            dstport:
                                type: int
                                description: Tcam mask L4 dst port.
                            ethertype:
                                type: str
                                description: Tcam mask ethertype.
                            ext-tag:
                                type: str
                                description: Deprecated, please rename it to ext_tag. Tcam mask extension tag.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            frag-off:
                                type: int
                                description: Deprecated, please rename it to frag_off. Tcam data ip flag fragment offset.
                            gen-buf-cnt:
                                type: int
                                description: Deprecated, please rename it to gen_buf_cnt. Tcam mask gen info buffer count.
                            gen-iv:
                                type: str
                                description: Deprecated, please rename it to gen_iv. Tcam mask gen info iv.
                                choices:
                                    - 'invalid'
                                    - 'valid'
                            gen-l3-flags:
                                type: int
                                description: Deprecated, please rename it to gen_l3_flags. Tcam mask gen info L3 flags.
                            gen-l4-flags:
                                type: int
                                description: Deprecated, please rename it to gen_l4_flags. Tcam mask gen info L4 flags.
                            gen-pkt-ctrl:
                                type: int
                                description: Deprecated, please rename it to gen_pkt_ctrl. Tcam mask gen info packet control.
                            gen-pri:
                                type: int
                                description: Deprecated, please rename it to gen_pri. Tcam mask gen info priority.
                            gen-pri-v:
                                type: str
                                description: Deprecated, please rename it to gen_pri_v. Tcam mask gen info priority valid.
                                choices:
                                    - 'invalid'
                                    - 'valid'
                            gen-tv:
                                type: str
                                description: Deprecated, please rename it to gen_tv. Tcam mask gen info tv.
                                choices:
                                    - 'invalid'
                                    - 'valid'
                            ihl:
                                type: int
                                description: Tcam mask ipv4 IHL.
                            ip4-id:
                                type: int
                                description: Deprecated, please rename it to ip4_id. Tcam mask ipv4 id.
                            ip6-fl:
                                type: int
                                description: Deprecated, please rename it to ip6_fl. Tcam mask ipv6 flow label.
                            ipver:
                                type: int
                                description: Tcam mask ip header version.
                            l4-wd10:
                                type: int
                                description: Deprecated, please rename it to l4_wd10. Tcam mask L4 word10.
                            l4-wd11:
                                type: int
                                description: Deprecated, please rename it to l4_wd11. Tcam mask L4 word11.
                            l4-wd8:
                                type: int
                                description: Deprecated, please rename it to l4_wd8. Tcam mask L4 word8.
                            l4-wd9:
                                type: int
                                description: Deprecated, please rename it to l4_wd9. Tcam mask L4 word9.
                            mf:
                                type: str
                                description: Tcam mask ip flag mf.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            protocol:
                                type: int
                                description: Tcam mask ip protocol.
                            slink:
                                type: int
                                description: Tcam mask sublink.
                            smac-change:
                                type: str
                                description: Deprecated, please rename it to smac_change. Tcam mask source MAC change.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            sp:
                                type: int
                                description: Tcam mask source port.
                            src-cfi:
                                type: str
                                description: Deprecated, please rename it to src_cfi. Tcam mask source cfi.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            src-prio:
                                type: int
                                description: Deprecated, please rename it to src_prio. Tcam mask source priority.
                            src-updt:
                                type: str
                                description: Deprecated, please rename it to src_updt. Tcam mask source update.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            srcip:
                                type: str
                                description: Tcam mask src ipv4 address.
                            srcipv6:
                                type: str
                                description: Tcam mask src ipv6 address.
                            srcmac:
                                type: str
                                description: Tcam mask src macaddr.
                            srcport:
                                type: int
                                description: Tcam mask L4 src port.
                            svid:
                                type: int
                                description: Tcam mask source vid.
                            tcp-ack:
                                type: str
                                description: Deprecated, please rename it to tcp_ack. Tcam mask tcp flag ack.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            tcp-cwr:
                                type: str
                                description: Deprecated, please rename it to tcp_cwr. Tcam mask tcp flag cwr.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            tcp-ece:
                                type: str
                                description: Deprecated, please rename it to tcp_ece. Tcam mask tcp flag ece.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            tcp-fin:
                                type: str
                                description: Deprecated, please rename it to tcp_fin. Tcam mask tcp flag fin.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            tcp-push:
                                type: str
                                description: Deprecated, please rename it to tcp_push. Tcam mask tcp flag push.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            tcp-rst:
                                type: str
                                description: Deprecated, please rename it to tcp_rst. Tcam mask tcp flag rst.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            tcp-syn:
                                type: str
                                description: Deprecated, please rename it to tcp_syn. Tcam mask tcp flag syn.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            tcp-urg:
                                type: str
                                description: Deprecated, please rename it to tcp_urg. Tcam mask tcp flag urg.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            tgt-cfi:
                                type: str
                                description: Deprecated, please rename it to tgt_cfi. Tcam mask target cfi.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            tgt-prio:
                                type: int
                                description: Deprecated, please rename it to tgt_prio. Tcam mask target priority.
                            tgt-updt:
                                type: str
                                description: Deprecated, please rename it to tgt_updt. Tcam mask target port update.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            tgt-v:
                                type: str
                                description: Deprecated, please rename it to tgt_v. Tcam mask target valid.
                                choices:
                                    - 'invalid'
                                    - 'valid'
                            tos:
                                type: int
                                description: Tcam mask ip tos.
                            tp:
                                type: int
                                description: Tcam mask target port.
                            ttl:
                                type: int
                                description: Tcam mask ip ttl.
                            tvid:
                                type: int
                                description: Tcam mask target vid.
                            vdid:
                                type: int
                                description: Tcam mask vdom id.
                    mir-act:
                        type: dict
                        description: Deprecated, please rename it to mir_act. Mir act.
                        suboptions:
                            vlif:
                                type: int
                                description: Tcam mirror action vlif.
                    name:
                        type: str
                        description: NPU TCAM policies name.
                    oid:
                        type: int
                        description: NPU TCAM OID.
                    pri-act:
                        type: dict
                        description: Deprecated, please rename it to pri_act. Pri act.
                        suboptions:
                            priority:
                                type: int
                                description: Tcam priority action priority.
                            weight:
                                type: int
                                description: Tcam priority action weight.
                    sact:
                        type: dict
                        description: Sact.
                        suboptions:
                            act:
                                type: int
                                description: Tcam sact act.
                            act-v:
                                type: str
                                description: Deprecated, please rename it to act_v. Enable to set sact act.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            bmproc:
                                type: int
                                description: Tcam sact bmproc.
                            bmproc-v:
                                type: str
                                description: Deprecated, please rename it to bmproc_v. Enable to set sact bmproc.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            df-lif:
                                type: int
                                description: Deprecated, please rename it to df_lif. Tcam sact df-lif.
                            df-lif-v:
                                type: str
                                description: Deprecated, please rename it to df_lif_v. Enable to set sact df-lif.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            dfr:
                                type: int
                                description: Tcam sact dfr.
                            dfr-v:
                                type: str
                                description: Deprecated, please rename it to dfr_v. Enable to set sact dfr.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            dmac-skip:
                                type: int
                                description: Deprecated, please rename it to dmac_skip. Tcam sact dmac-skip.
                            dmac-skip-v:
                                type: str
                                description: Deprecated, please rename it to dmac_skip_v. Enable to set sact dmac-skip.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            dosen:
                                type: int
                                description: Tcam sact dosen.
                            dosen-v:
                                type: str
                                description: Deprecated, please rename it to dosen_v. Enable to set sact dosen.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            espff-proc:
                                type: int
                                description: Deprecated, please rename it to espff_proc. Tcam sact espff-proc.
                            espff-proc-v:
                                type: str
                                description: Deprecated, please rename it to espff_proc_v. Enable to set sact espff-proc.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            etype-pid:
                                type: int
                                description: Deprecated, please rename it to etype_pid. Tcam sact etype-pid.
                            etype-pid-v:
                                type: str
                                description: Deprecated, please rename it to etype_pid_v. Enable to set sact etype-pid.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            frag-proc:
                                type: int
                                description: Deprecated, please rename it to frag_proc. Tcam sact frag-proc.
                            frag-proc-v:
                                type: str
                                description: Deprecated, please rename it to frag_proc_v. Enable to set sact frag-proc.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            fwd:
                                type: int
                                description: Tcam sact fwd.
                            fwd-lif:
                                type: int
                                description: Deprecated, please rename it to fwd_lif. Tcam sact fwd-lif.
                            fwd-lif-v:
                                type: str
                                description: Deprecated, please rename it to fwd_lif_v. Enable to set sact fwd-lif.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            fwd-tvid:
                                type: int
                                description: Deprecated, please rename it to fwd_tvid. Tcam sact fwd-tvid.
                            fwd-tvid-v:
                                type: str
                                description: Deprecated, please rename it to fwd_tvid_v. Enable to set sact fwd-vid.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            fwd-v:
                                type: str
                                description: Deprecated, please rename it to fwd_v. Enable to set sact fwd.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            icpen:
                                type: int
                                description: Tcam sact icpen.
                            icpen-v:
                                type: str
                                description: Deprecated, please rename it to icpen_v. Enable to set sact icpen.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            igmp-mld-snp:
                                type: int
                                description: Deprecated, please rename it to igmp_mld_snp. Tcam sact igmp-mld-snp.
                            igmp-mld-snp-v:
                                type: str
                                description: Deprecated, please rename it to igmp_mld_snp_v. Enable to set sact igmp-mld-snp.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            learn:
                                type: int
                                description: Tcam sact learn.
                            learn-v:
                                type: str
                                description: Deprecated, please rename it to learn_v. Enable to set sact learn.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            m-srh-ctrl:
                                type: int
                                description: Deprecated, please rename it to m_srh_ctrl. Tcam sact m-srh-ctrl.
                            m-srh-ctrl-v:
                                type: str
                                description: Deprecated, please rename it to m_srh_ctrl_v. Enable to set sact m-srh-ctrl.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            mac-id:
                                type: int
                                description: Deprecated, please rename it to mac_id. Tcam sact mac-id.
                            mac-id-v:
                                type: str
                                description: Deprecated, please rename it to mac_id_v. Enable to set sact mac-id.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            mss:
                                type: int
                                description: Tcam sact mss.
                            mss-v:
                                type: str
                                description: Deprecated, please rename it to mss_v. Enable to set sact mss.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            pleen:
                                type: int
                                description: Tcam sact pleen.
                            pleen-v:
                                type: str
                                description: Deprecated, please rename it to pleen_v. Enable to set sact pleen.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            prio-pid:
                                type: int
                                description: Deprecated, please rename it to prio_pid. Tcam sact prio-pid.
                            prio-pid-v:
                                type: str
                                description: Deprecated, please rename it to prio_pid_v. Enable to set sact prio-pid.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            promis:
                                type: int
                                description: Tcam sact promis.
                            promis-v:
                                type: str
                                description: Deprecated, please rename it to promis_v. Enable to set sact promis.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            rfsh:
                                type: int
                                description: Tcam sact rfsh.
                            rfsh-v:
                                type: str
                                description: Deprecated, please rename it to rfsh_v. Enable to set sact rfsh.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            smac-skip:
                                type: int
                                description: Deprecated, please rename it to smac_skip. Tcam sact smac-skip.
                            smac-skip-v:
                                type: str
                                description: Deprecated, please rename it to smac_skip_v. Enable to set sact smac-skip.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            tp-smchk-v:
                                type: str
                                description: Deprecated, please rename it to tp_smchk_v. Enable to set sact tp mode.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            tp_smchk:
                                type: int
                                description: Tcam sact tp mode.
                            tpe-id:
                                type: int
                                description: Deprecated, please rename it to tpe_id. Tcam sact tpe-id.
                            tpe-id-v:
                                type: str
                                description: Deprecated, please rename it to tpe_id_v. Enable to set sact tpe-id.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            vdm:
                                type: int
                                description: Tcam sact vdm.
                            vdm-v:
                                type: str
                                description: Deprecated, please rename it to vdm_v. Enable to set sact vdm.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            vdom-id:
                                type: int
                                description: Deprecated, please rename it to vdom_id. Tcam sact vdom-id.
                            vdom-id-v:
                                type: str
                                description: Deprecated, please rename it to vdom_id_v. Enable to set sact vdom-id.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            x-mode:
                                type: int
                                description: Deprecated, please rename it to x_mode. Tcam sact x-mode.
                            x-mode-v:
                                type: str
                                description: Deprecated, please rename it to x_mode_v. Enable to set sact x-mode.
                                choices:
                                    - 'disable'
                                    - 'enable'
                    tact:
                        type: dict
                        description: Tact.
                        suboptions:
                            act:
                                type: int
                                description: Tcam tact act.
                            act-v:
                                type: str
                                description: Deprecated, please rename it to act_v. Enable to set tact act.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            fmtuv4-s:
                                type: int
                                description: Deprecated, please rename it to fmtuv4_s. Tcam tact fmtuv4-s.
                            fmtuv4-s-v:
                                type: str
                                description: Deprecated, please rename it to fmtuv4_s_v. Enable to set tact fmtuv4-s.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            fmtuv6-s:
                                type: int
                                description: Deprecated, please rename it to fmtuv6_s. Tcam tact fmtuv6-s.
                            fmtuv6-s-v:
                                type: str
                                description: Deprecated, please rename it to fmtuv6_s_v. Enable to set tact fmtuv6-s.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            lnkid:
                                type: int
                                description: Tcam tact lnkid.
                            lnkid-v:
                                type: str
                                description: Deprecated, please rename it to lnkid_v. Enable to set tact lnkid.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            mac-id:
                                type: int
                                description: Deprecated, please rename it to mac_id. Tcam tact mac-id.
                            mac-id-v:
                                type: str
                                description: Deprecated, please rename it to mac_id_v. Enable to set tact mac-id.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            mss-t:
                                type: int
                                description: Deprecated, please rename it to mss_t. Tcam tact mss.
                            mss-t-v:
                                type: str
                                description: Deprecated, please rename it to mss_t_v. Enable to set tact mss.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            mtuv4:
                                type: int
                                description: Tcam tact mtuv4.
                            mtuv4-v:
                                type: str
                                description: Deprecated, please rename it to mtuv4_v. Enable to set tact mtuv4.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            mtuv6:
                                type: int
                                description: Tcam tact mtuv6.
                            mtuv6-v:
                                type: str
                                description: Deprecated, please rename it to mtuv6_v. Enable to set tact mtuv6.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            slif-act:
                                type: int
                                description: Deprecated, please rename it to slif_act. Tcam tact slif-act.
                            slif-act-v:
                                type: str
                                description: Deprecated, please rename it to slif_act_v. Enable to set tact slif-act.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            sublnkid:
                                type: int
                                description: Tcam tact sublnkid.
                            sublnkid-v:
                                type: str
                                description: Deprecated, please rename it to sublnkid_v. Enable to set tact sublnkid.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            tgtv-act:
                                type: int
                                description: Deprecated, please rename it to tgtv_act. Tcam tact tgtv-act.
                            tgtv-act-v:
                                type: str
                                description: Deprecated, please rename it to tgtv_act_v. Enable to set tact tgtv-act.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            tlif-act:
                                type: int
                                description: Deprecated, please rename it to tlif_act. Tcam tact tlif-act.
                            tlif-act-v:
                                type: str
                                description: Deprecated, please rename it to tlif_act_v. Enable to set tact tlif-act.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            tpeid:
                                type: int
                                description: Tcam tact tpeid.
                            tpeid-v:
                                type: str
                                description: Deprecated, please rename it to tpeid_v. Enable to set tact tpeid.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            v6fe:
                                type: int
                                description: Tcam tact v6fe.
                            v6fe-v:
                                type: str
                                description: Deprecated, please rename it to v6fe_v. Enable to set tact v6fe.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            vep-en-v:
                                type: str
                                description: Deprecated, please rename it to vep_en_v. Enable to set tact vep-en.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            vep-slid:
                                type: int
                                description: Deprecated, please rename it to vep_slid. Tcam tact vep_slid.
                            vep-slid-v:
                                type: str
                                description: Deprecated, please rename it to vep_slid_v. Enable to set tact vep-slid.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            vep_en:
                                type: int
                                description: Tcam tact vep_en.
                            xlt-lif:
                                type: int
                                description: Deprecated, please rename it to xlt_lif. Tcam tact xlt-lif.
                            xlt-lif-v:
                                type: str
                                description: Deprecated, please rename it to xlt_lif_v. Enable to set tact xlt-lif.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            xlt-vid:
                                type: int
                                description: Deprecated, please rename it to xlt_vid. Tcam tact xlt-vid.
                            xlt-vid-v:
                                type: str
                                description: Deprecated, please rename it to xlt_vid_v. Enable to set tact xlt-vid.
                                choices:
                                    - 'disable'
                                    - 'enable'
                    type:
                        type: str
                        description: TCAM policy type.
                        choices:
                            - 'L2_src_tc'
                            - 'L2_tgt_tc'
                            - 'L2_src_mir'
                            - 'L2_tgt_mir'
                            - 'L2_src_act'
                            - 'L2_tgt_act'
                            - 'IPv4_src_tc'
                            - 'IPv4_tgt_tc'
                            - 'IPv4_src_mir'
                            - 'IPv4_tgt_mir'
                            - 'IPv4_src_act'
                            - 'IPv4_tgt_act'
                            - 'IPv6_src_tc'
                            - 'IPv6_tgt_tc'
                            - 'IPv6_src_mir'
                            - 'IPv6_tgt_mir'
                            - 'IPv6_src_act'
                            - 'IPv6_tgt_act'
                    vid:
                        type: int
                        description: NPU TCAM VID.
            icmp-rate-ctrl:
                type: dict
                description: Deprecated, please rename it to icmp_rate_ctrl. Icmp rate ctrl.
                suboptions:
                    icmp-v4-bucket-size:
                        type: int
                        description: Deprecated, please rename it to icmp_v4_bucket_size. Bucket size used in the token bucket algorithm for controllin...
                    icmp-v4-rate:
                        type: int
                        description: Deprecated, please rename it to icmp_v4_rate. Average rate of ICMPv4 packets that allowed to be generated per second
                    icmp-v6-bucket-size:
                        type: int
                        description: Deprecated, please rename it to icmp_v6_bucket_size. Bucket size used in the token bucket algorithm for controllin...
                    icmp-v6-rate:
                        type: int
                        description: Deprecated, please rename it to icmp_v6_rate. Average rate of ICMPv6 packets that allowed to be generated per second
            vxlan-offload:
                type: str
                description: Deprecated, please rename it to vxlan_offload. Enable/disable offloading vxlan.
                choices:
                    - 'disable'
                    - 'enable'
            icmp-error-rate-ctrl:
                type: dict
                description: Deprecated, please rename it to icmp_error_rate_ctrl. Icmp error rate ctrl.
                suboptions:
                    icmpv4-error-bucket-size:
                        type: int
                        description: Deprecated, please rename it to icmpv4_error_bucket_size. Bucket size used in the token bucket algorithm for contr...
                    icmpv4-error-rate:
                        type: int
                        description: Deprecated, please rename it to icmpv4_error_rate. Average rate of ICMPv4 error packets that allowed to be generat...
                    icmpv4-error-rate-limit:
                        type: str
                        description: Deprecated, please rename it to icmpv4_error_rate_limit. Enable to limit the ICMPv4 error packets generated by thi...
                        choices:
                            - 'disable'
                            - 'enable'
                    icmpv6-error-bucket-size:
                        type: int
                        description: Deprecated, please rename it to icmpv6_error_bucket_size. Bucket size used in the token bucket algorithm for contr...
                    icmpv6-error-rate:
                        type: int
                        description: Deprecated, please rename it to icmpv6_error_rate. Average rate of ICMPv6 error packets that allowed to be generat...
                    icmpv6-error-rate-limit:
                        type: str
                        description: Deprecated, please rename it to icmpv6_error_rate_limit. Enable to limit the ICMPv6 error packets generated by thi...
                        choices:
                            - 'disable'
                            - 'enable'
            ipv4-session-quota:
                type: str
                description: Deprecated, please rename it to ipv4_session_quota. Enable/Disable NoNAT IPv4 session quota for hyperscale VDOMs.
                choices:
                    - 'disable'
                    - 'enable'
            ipv4-session-quota-high:
                type: int
                description: Deprecated, please rename it to ipv4_session_quota_high. Configure NoNAT IPv4 session quota high threshold.
            ipv4-session-quota-low:
                type: int
                description: Deprecated, please rename it to ipv4_session_quota_low. Configure NoNAT IPv4 session quota low threshold.
            ipv6-prefix-session-quota:
                type: str
                description: Deprecated, please rename it to ipv6_prefix_session_quota. Enable/Disable hardware IPv6 /64 prefix session quota for hyper...
                choices:
                    - 'disable'
                    - 'enable'
            ipv6-prefix-session-quota-high:
                type: int
                description: Deprecated, please rename it to ipv6_prefix_session_quota_high. Configure IPv6 prefix session quota high threshold.
            ipv6-prefix-session-quota-low:
                type: int
                description: Deprecated, please rename it to ipv6_prefix_session_quota_low. Configure IPv6 prefix session quota low threshold.
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
    - name: Configure NPU attributes.
      fortinet.fortimanager.fmgr_system_npu:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        adom: <your own value>
        system_npu:
          capwap_offload: <value in [disable, enable]>
          dedicated_management_affinity: <string>
          dedicated_management_cpu: <value in [disable, enable]>
          fastpath: <value in [disable, enable]>
          fp_anomaly:
            esp_minlen_err: <value in [drop, trap-to-host]>
            icmp_csum_err: <value in [drop, trap-to-host]>
            icmp_minlen_err: <value in [drop, trap-to-host]>
            ipv4_csum_err: <value in [drop, trap-to-host]>
            ipv4_ihl_err: <value in [drop, trap-to-host]>
            ipv4_len_err: <value in [drop, trap-to-host]>
            ipv4_opt_err: <value in [drop, trap-to-host]>
            ipv4_ttlzero_err: <value in [drop, trap-to-host]>
            ipv4_ver_err: <value in [drop, trap-to-host]>
            ipv6_exthdr_len_err: <value in [drop, trap-to-host]>
            ipv6_exthdr_order_err: <value in [drop, trap-to-host]>
            ipv6_ihl_err: <value in [drop, trap-to-host]>
            ipv6_plen_zero: <value in [drop, trap-to-host]>
            ipv6_ver_err: <value in [drop, trap-to-host]>
            tcp_csum_err: <value in [drop, trap-to-host]>
            tcp_hlen_err: <value in [drop, trap-to-host]>
            tcp_plen_err: <value in [drop, trap-to-host]>
            udp_csum_err: <value in [drop, trap-to-host]>
            udp_hlen_err: <value in [drop, trap-to-host]>
            udp_len_err: <value in [drop, trap-to-host]>
            udp_plen_err: <value in [drop, trap-to-host]>
            udplite_cover_err: <value in [drop, trap-to-host]>
            udplite_csum_err: <value in [drop, trap-to-host]>
            unknproto_minlen_err: <value in [drop, trap-to-host]>
            tcp_fin_only: <value in [allow, drop, trap-to-host]>
            ipv4_optsecurity: <value in [allow, drop, trap-to-host]>
            ipv6_optralert: <value in [allow, drop, trap-to-host]>
            tcp_syn_fin: <value in [allow, drop, trap-to-host]>
            ipv4_proto_err: <value in [allow, drop, trap-to-host]>
            ipv6_saddr_err: <value in [allow, drop, trap-to-host]>
            icmp_frag: <value in [allow, drop, trap-to-host]>
            ipv4_optssrr: <value in [allow, drop, trap-to-host]>
            ipv6_opthomeaddr: <value in [allow, drop, trap-to-host]>
            udp_land: <value in [allow, drop, trap-to-host]>
            ipv6_optinvld: <value in [allow, drop, trap-to-host]>
            tcp_fin_noack: <value in [allow, drop, trap-to-host]>
            ipv6_proto_err: <value in [allow, drop, trap-to-host]>
            tcp_land: <value in [allow, drop, trap-to-host]>
            ipv4_unknopt: <value in [allow, drop, trap-to-host]>
            ipv4_optstream: <value in [allow, drop, trap-to-host]>
            ipv6_optjumbo: <value in [allow, drop, trap-to-host]>
            icmp_land: <value in [allow, drop, trap-to-host]>
            tcp_winnuke: <value in [allow, drop, trap-to-host]>
            ipv6_daddr_err: <value in [allow, drop, trap-to-host]>
            ipv4_land: <value in [allow, drop, trap-to-host]>
            ipv6_opttunnel: <value in [allow, drop, trap-to-host]>
            tcp_no_flag: <value in [allow, drop, trap-to-host]>
            ipv6_land: <value in [allow, drop, trap-to-host]>
            ipv4_optlsrr: <value in [allow, drop, trap-to-host]>
            ipv4_opttimestamp: <value in [allow, drop, trap-to-host]>
            ipv4_optrr: <value in [allow, drop, trap-to-host]>
            ipv6_optnsap: <value in [allow, drop, trap-to-host]>
            ipv6_unknopt: <value in [allow, drop, trap-to-host]>
            tcp_syn_data: <value in [allow, drop, trap-to-host]>
            ipv6_optendpid: <value in [allow, drop, trap-to-host]>
            gtpu_plen_err: <value in [drop, trap-to-host]>
            vxlan_minlen_err: <value in [drop, trap-to-host]>
            capwap_minlen_err: <value in [drop, trap-to-host]>
            gre_csum_err: <value in [drop, trap-to-host]>
            nvgre_minlen_err: <value in [drop, trap-to-host]>
            sctp_l4len_err: <value in [drop, trap-to-host]>
            tcp_hlenvsl4len_err: <value in [drop, trap-to-host]>
            sctp_crc_err: <value in [drop, trap-to-host]>
            sctp_clen_err: <value in [drop, trap-to-host]>
            uesp_minlen_err: <value in [drop, trap-to-host]>
            sctp_csum_err: <value in [allow, drop, trap-to-host]>
          gtp_enhanced_cpu_range: <value in [0, 1, 2]>
          gtp_enhanced_mode: <value in [disable, enable]>
          host_shortcut_mode: <value in [bi-directional, host-shortcut]>
          htx_gtse_quota: <value in [100Mbps, 200Mbps, 300Mbps, ...]>
          intf_shaping_offload: <value in [disable, enable]>
          iph_rsvd_re_cksum: <value in [disable, enable]>
          ipsec_dec_subengine_mask: <string>
          ipsec_enc_subengine_mask: <string>
          ipsec_inbound_cache: <value in [disable, enable]>
          ipsec_mtu_override: <value in [disable, enable]>
          ipsec_over_vlink: <value in [disable, enable]>
          isf_np_queues:
            cos0: <string>
            cos1: <string>
            cos2: <string>
            cos3: <string>
            cos4: <string>
            cos5: <string>
            cos6: <string>
            cos7: <string>
          lag_out_port_select: <value in [disable, enable]>
          mcast_session_accounting: <value in [disable, session-based, tpe-based]>
          np6_cps_optimization_mode: <value in [disable, enable]>
          per_session_accounting: <value in [enable, disable, enable-by-log, ...]>
          port_cpu_map:
            -
              cpu_core: <string>
              interface: <string>
          port_npu_map:
            -
              interface: <string>
              npu_group_index: <integer>
          priority_protocol:
            bfd: <value in [disable, enable]>
            bgp: <value in [disable, enable]>
            slbc: <value in [disable, enable]>
          qos_mode: <value in [disable, priority, round-robin]>
          rdp_offload: <value in [disable, enable]>
          recover_np6_link: <value in [disable, enable]>
          session_denied_offload: <value in [disable, enable]>
          sse_backpressure: <value in [disable, enable]>
          strip_clear_text_padding: <value in [disable, enable]>
          strip_esp_padding: <value in [disable, enable]>
          sw_eh_hash:
            computation: <value in [xor16, xor8, xor4, ...]>
            destination_ip_lower_16: <value in [include, exclude]>
            destination_ip_upper_16: <value in [include, exclude]>
            destination_port: <value in [include, exclude]>
            ip_protocol: <value in [include, exclude]>
            netmask_length: <integer>
            source_ip_lower_16: <value in [include, exclude]>
            source_ip_upper_16: <value in [include, exclude]>
            source_port: <value in [include, exclude]>
          sw_np_bandwidth: <value in [0G, 2G, 4G, ...]>
          switch_np_hash: <value in [src-ip, dst-ip, src-dst-ip]>
          uesp_offload: <value in [disable, enable]>
          np_queues:
            ethernet_type:
              -
                name: <string>
                queue: <integer>
                type: <integer>
                weight: <integer>
            ip_protocol:
              -
                name: <string>
                protocol: <integer>
                queue: <integer>
                weight: <integer>
            ip_service:
              -
                dport: <integer>
                name: <string>
                protocol: <integer>
                queue: <integer>
                sport: <integer>
                weight: <integer>
            profile:
              -
                cos0: <value in [queue0, queue1, queue2, ...]>
                cos1: <value in [queue0, queue1, queue2, ...]>
                cos2: <value in [queue0, queue1, queue2, ...]>
                cos3: <value in [queue0, queue1, queue2, ...]>
                cos4: <value in [queue0, queue1, queue2, ...]>
                cos5: <value in [queue0, queue1, queue2, ...]>
                cos6: <value in [queue0, queue1, queue2, ...]>
                cos7: <value in [queue0, queue1, queue2, ...]>
                dscp0: <value in [queue0, queue1, queue2, ...]>
                dscp1: <value in [queue0, queue1, queue2, ...]>
                dscp10: <value in [queue0, queue1, queue2, ...]>
                dscp11: <value in [queue0, queue1, queue2, ...]>
                dscp12: <value in [queue0, queue1, queue2, ...]>
                dscp13: <value in [queue0, queue1, queue2, ...]>
                dscp14: <value in [queue0, queue1, queue2, ...]>
                dscp15: <value in [queue0, queue1, queue2, ...]>
                dscp16: <value in [queue0, queue1, queue2, ...]>
                dscp17: <value in [queue0, queue1, queue2, ...]>
                dscp18: <value in [queue0, queue1, queue2, ...]>
                dscp19: <value in [queue0, queue1, queue2, ...]>
                dscp2: <value in [queue0, queue1, queue2, ...]>
                dscp20: <value in [queue0, queue1, queue2, ...]>
                dscp21: <value in [queue0, queue1, queue2, ...]>
                dscp22: <value in [queue0, queue1, queue2, ...]>
                dscp23: <value in [queue0, queue1, queue2, ...]>
                dscp24: <value in [queue0, queue1, queue2, ...]>
                dscp25: <value in [queue0, queue1, queue2, ...]>
                dscp26: <value in [queue0, queue1, queue2, ...]>
                dscp27: <value in [queue0, queue1, queue2, ...]>
                dscp28: <value in [queue0, queue1, queue2, ...]>
                dscp29: <value in [queue0, queue1, queue2, ...]>
                dscp3: <value in [queue0, queue1, queue2, ...]>
                dscp30: <value in [queue0, queue1, queue2, ...]>
                dscp31: <value in [queue0, queue1, queue2, ...]>
                dscp32: <value in [queue0, queue1, queue2, ...]>
                dscp33: <value in [queue0, queue1, queue2, ...]>
                dscp34: <value in [queue0, queue1, queue2, ...]>
                dscp35: <value in [queue0, queue1, queue2, ...]>
                dscp36: <value in [queue0, queue1, queue2, ...]>
                dscp37: <value in [queue0, queue1, queue2, ...]>
                dscp38: <value in [queue0, queue1, queue2, ...]>
                dscp39: <value in [queue0, queue1, queue2, ...]>
                dscp4: <value in [queue0, queue1, queue2, ...]>
                dscp40: <value in [queue0, queue1, queue2, ...]>
                dscp41: <value in [queue0, queue1, queue2, ...]>
                dscp42: <value in [queue0, queue1, queue2, ...]>
                dscp43: <value in [queue0, queue1, queue2, ...]>
                dscp44: <value in [queue0, queue1, queue2, ...]>
                dscp45: <value in [queue0, queue1, queue2, ...]>
                dscp46: <value in [queue0, queue1, queue2, ...]>
                dscp47: <value in [queue0, queue1, queue2, ...]>
                dscp48: <value in [queue0, queue1, queue2, ...]>
                dscp49: <value in [queue0, queue1, queue2, ...]>
                dscp5: <value in [queue0, queue1, queue2, ...]>
                dscp50: <value in [queue0, queue1, queue2, ...]>
                dscp51: <value in [queue0, queue1, queue2, ...]>
                dscp52: <value in [queue0, queue1, queue2, ...]>
                dscp53: <value in [queue0, queue1, queue2, ...]>
                dscp54: <value in [queue0, queue1, queue2, ...]>
                dscp55: <value in [queue0, queue1, queue2, ...]>
                dscp56: <value in [queue0, queue1, queue2, ...]>
                dscp57: <value in [queue0, queue1, queue2, ...]>
                dscp58: <value in [queue0, queue1, queue2, ...]>
                dscp59: <value in [queue0, queue1, queue2, ...]>
                dscp6: <value in [queue0, queue1, queue2, ...]>
                dscp60: <value in [queue0, queue1, queue2, ...]>
                dscp61: <value in [queue0, queue1, queue2, ...]>
                dscp62: <value in [queue0, queue1, queue2, ...]>
                dscp63: <value in [queue0, queue1, queue2, ...]>
                dscp7: <value in [queue0, queue1, queue2, ...]>
                dscp8: <value in [queue0, queue1, queue2, ...]>
                dscp9: <value in [queue0, queue1, queue2, ...]>
                id: <integer>
                type: <value in [cos, dscp]>
                weight: <integer>
            scheduler:
              -
                mode: <value in [none, priority, round-robin]>
                name: <string>
          udp_timeout_profile:
            -
              id: <integer>
              udp_idle: <integer>
          qtm_buf_mode: <value in [6ch, 4ch]>
          default_qos_type: <value in [policing, shaping, policing-enhanced]>
          tcp_rst_timeout: <integer>
          ipsec_local_uesp_port: <integer>
          htab_dedi_queue_nr: <integer>
          double_level_mcast_offload: <value in [disable, enable]>
          dse_timeout: <integer>
          ippool_overload_low: <integer>
          pba_eim: <value in [disallow, allow]>
          policy_offload_level: <value in [disable, dos-offload, full-offload]>
          max_session_timeout: <integer>
          port_path_option:
            ports_using_npu: <list or string>
          vlan_lookup_cache: <value in [disable, enable]>
          dos_options:
            npu_dos_meter_mode: <value in [local, global]>
            npu_dos_synproxy_mode: <value in [synack2ack, pass-synack]>
            npu_dos_tpe_mode: <value in [disable, enable]>
          hash_tbl_spread: <value in [disable, enable]>
          tcp_timeout_profile:
            -
              close_wait: <integer>
              fin_wait: <integer>
              id: <integer>
              syn_sent: <integer>
              syn_wait: <integer>
              tcp_idle: <integer>
              time_wait: <integer>
          ip_reassembly:
            max_timeout: <integer>
            min_timeout: <integer>
            status: <value in [disable, enable]>
          gtp_support: <value in [disable, enable]>
          htx_icmp_csum_chk: <value in [pass, drop]>
          hpe:
            all_protocol: <integer>
            arp_max: <integer>
            enable_shaper: <value in [disable, enable]>
            esp_max: <integer>
            high_priority: <integer>
            icmp_max: <integer>
            ip_frag_max: <integer>
            ip_others_max: <integer>
            l2_others_max: <integer>
            pri_type_max: <integer>
            sctp_max: <integer>
            tcp_max: <integer>
            tcpfin_rst_max: <integer>
            tcpsyn_ack_max: <integer>
            tcpsyn_max: <integer>
            udp_max: <integer>
            enable_queue_shaper: <value in [disable, enable]>
            exception_code: <integer>
            fragment_with_sess: <integer>
            fragment_without_session: <integer>
            queue_shaper_max: <integer>
          dsw_dts_profile:
            -
              action: <value in [wait, drop, drop_tmr_0, ...]>
              min_limit: <integer>
              profile_id: <integer>
              step: <integer>
          hash_config: <value in [5-tuple, src-ip, src-dst-ip]>
          ipsec_ob_np_sel: <value in [RR, rr, Packet, ...]>
          napi_break_interval: <integer>
          background_sse_scan:
            scan: <value in [disable, enable]>
            stats_update_interval: <integer>
            udp_keepalive_interval: <integer>
            scan_stale: <integer>
            scan_vt: <integer>
            stats_qual_access: <integer>
            stats_qual_duration: <integer>
            udp_qual_access: <integer>
            udp_qual_duration: <integer>
          inbound_dscp_copy_port: <list or string>
          session_acct_interval: <integer>
          htab_msg_queue: <value in [idle, data, dedicated]>
          dsw_queue_dts_profile:
            -
              iport: <value in [EIF0, eif0, EIF1, ...]>
              name: <string>
              oport: <value in [EIF0, eif0, EIF1, ...]>
              profile_id: <integer>
              queue_select: <integer>
          hw_ha_scan_interval: <integer>
          ippool_overload_high: <integer>
          nat46_force_ipv4_packet_forwarding: <value in [disable, enable]>
          prp_port_out: <list or string>
          isf_np_rx_tr_distr: <value in [port-flow, round-robin, randomized]>
          mcast_session_counting6: <value in [disable, enable, session-based, ...]>
          prp_port_in: <list or string>
          rps_mode: <value in [disable, enable]>
          per_policy_accounting: <value in [disable, enable]>
          mcast_session_counting: <value in [disable, enable, session-based, ...]>
          inbound_dscp_copy: <value in [disable, enable]>
          ipsec_host_dfclr: <value in [disable, enable]>
          process_icmp_by_host: <value in [disable, enable]>
          dedicated_tx_npu: <value in [disable, enable]>
          ull_port_mode: <value in [10G, 25G]>
          sse_ha_scan:
            gap: <integer>
            max_session_cnt: <integer>
            min_duration: <integer>
          hash_ipv6_sel: <integer>
          ip_fragment_offload: <value in [disable, enable]>
          ple_non_syn_tcp_action: <value in [forward, drop]>
          npu_group_effective_scope: <integer>
          ipsec_STS_timeout: <value in [1, 2, 3, ...]>
          ipsec_throughput_msg_frequency: <value in [disable, 32KB, 64KB, ...]>
          ipt_STS_timeout: <value in [1, 2, 3, ...]>
          ipt_throughput_msg_frequency: <value in [disable, 32KB, 64KB, ...]>
          default_tcp_refresh_dir: <value in [both, outgoing, incoming]>
          default_udp_refresh_dir: <value in [both, outgoing, incoming]>
          nss_threads_option: <value in [4t-eif, 4t-noeif, 2t]>
          prp_session_clear_mode: <value in [blocking, non-blocking, do-not-clear]>
          shaping_stats: <value in [disable, enable]>
          sw_tr_hash:
            draco15: <value in [disable, enable]>
            tcp_udp_port: <value in [include, exclude]>
          pba_port_select_mode: <value in [random, direct]>
          spa_port_select_mode: <value in [random, direct]>
          split_ipsec_engines: <value in [disable, enable]>
          tunnel_over_vlink: <value in [disable, enable]>
          max_receive_unit: <integer>
          npu_tcam:
            -
              data:
                df: <value in [disable, enable]>
                dstip: <string>
                dstipv6: <string>
                dstmac: <string>
                dstport: <integer>
                ethertype: <string>
                ext_tag: <value in [disable, enable]>
                frag_off: <integer>
                gen_buf_cnt: <integer>
                gen_iv: <value in [invalid, valid]>
                gen_l3_flags: <integer>
                gen_l4_flags: <integer>
                gen_pkt_ctrl: <integer>
                gen_pri: <integer>
                gen_pri_v: <value in [invalid, valid]>
                gen_tv: <value in [invalid, valid]>
                ihl: <integer>
                ip4_id: <integer>
                ip6_fl: <integer>
                ipver: <integer>
                l4_wd10: <integer>
                l4_wd11: <integer>
                l4_wd8: <integer>
                l4_wd9: <integer>
                mf: <value in [disable, enable]>
                protocol: <integer>
                slink: <integer>
                smac_change: <value in [disable, enable]>
                sp: <integer>
                src_cfi: <value in [disable, enable]>
                src_prio: <integer>
                src_updt: <value in [disable, enable]>
                srcip: <string>
                srcipv6: <string>
                srcmac: <string>
                srcport: <integer>
                svid: <integer>
                tcp_ack: <value in [disable, enable]>
                tcp_cwr: <value in [disable, enable]>
                tcp_ece: <value in [disable, enable]>
                tcp_fin: <value in [disable, enable]>
                tcp_push: <value in [disable, enable]>
                tcp_rst: <value in [disable, enable]>
                tcp_syn: <value in [disable, enable]>
                tcp_urg: <value in [disable, enable]>
                tgt_cfi: <value in [disable, enable]>
                tgt_prio: <integer>
                tgt_updt: <value in [disable, enable]>
                tgt_v: <value in [invalid, valid]>
                tos: <integer>
                tp: <integer>
                ttl: <integer>
                tvid: <integer>
                vdid: <integer>
              dbg_dump: <integer>
              mask:
                df: <value in [disable, enable]>
                dstip: <string>
                dstipv6: <string>
                dstmac: <string>
                dstport: <integer>
                ethertype: <string>
                ext_tag: <value in [disable, enable]>
                frag_off: <integer>
                gen_buf_cnt: <integer>
                gen_iv: <value in [invalid, valid]>
                gen_l3_flags: <integer>
                gen_l4_flags: <integer>
                gen_pkt_ctrl: <integer>
                gen_pri: <integer>
                gen_pri_v: <value in [invalid, valid]>
                gen_tv: <value in [invalid, valid]>
                ihl: <integer>
                ip4_id: <integer>
                ip6_fl: <integer>
                ipver: <integer>
                l4_wd10: <integer>
                l4_wd11: <integer>
                l4_wd8: <integer>
                l4_wd9: <integer>
                mf: <value in [disable, enable]>
                protocol: <integer>
                slink: <integer>
                smac_change: <value in [disable, enable]>
                sp: <integer>
                src_cfi: <value in [disable, enable]>
                src_prio: <integer>
                src_updt: <value in [disable, enable]>
                srcip: <string>
                srcipv6: <string>
                srcmac: <string>
                srcport: <integer>
                svid: <integer>
                tcp_ack: <value in [disable, enable]>
                tcp_cwr: <value in [disable, enable]>
                tcp_ece: <value in [disable, enable]>
                tcp_fin: <value in [disable, enable]>
                tcp_push: <value in [disable, enable]>
                tcp_rst: <value in [disable, enable]>
                tcp_syn: <value in [disable, enable]>
                tcp_urg: <value in [disable, enable]>
                tgt_cfi: <value in [disable, enable]>
                tgt_prio: <integer>
                tgt_updt: <value in [disable, enable]>
                tgt_v: <value in [invalid, valid]>
                tos: <integer>
                tp: <integer>
                ttl: <integer>
                tvid: <integer>
                vdid: <integer>
              mir_act:
                vlif: <integer>
              name: <string>
              oid: <integer>
              pri_act:
                priority: <integer>
                weight: <integer>
              sact:
                act: <integer>
                act_v: <value in [disable, enable]>
                bmproc: <integer>
                bmproc_v: <value in [disable, enable]>
                df_lif: <integer>
                df_lif_v: <value in [disable, enable]>
                dfr: <integer>
                dfr_v: <value in [disable, enable]>
                dmac_skip: <integer>
                dmac_skip_v: <value in [disable, enable]>
                dosen: <integer>
                dosen_v: <value in [disable, enable]>
                espff_proc: <integer>
                espff_proc_v: <value in [disable, enable]>
                etype_pid: <integer>
                etype_pid_v: <value in [disable, enable]>
                frag_proc: <integer>
                frag_proc_v: <value in [disable, enable]>
                fwd: <integer>
                fwd_lif: <integer>
                fwd_lif_v: <value in [disable, enable]>
                fwd_tvid: <integer>
                fwd_tvid_v: <value in [disable, enable]>
                fwd_v: <value in [disable, enable]>
                icpen: <integer>
                icpen_v: <value in [disable, enable]>
                igmp_mld_snp: <integer>
                igmp_mld_snp_v: <value in [disable, enable]>
                learn: <integer>
                learn_v: <value in [disable, enable]>
                m_srh_ctrl: <integer>
                m_srh_ctrl_v: <value in [disable, enable]>
                mac_id: <integer>
                mac_id_v: <value in [disable, enable]>
                mss: <integer>
                mss_v: <value in [disable, enable]>
                pleen: <integer>
                pleen_v: <value in [disable, enable]>
                prio_pid: <integer>
                prio_pid_v: <value in [disable, enable]>
                promis: <integer>
                promis_v: <value in [disable, enable]>
                rfsh: <integer>
                rfsh_v: <value in [disable, enable]>
                smac_skip: <integer>
                smac_skip_v: <value in [disable, enable]>
                tp_smchk_v: <value in [disable, enable]>
                tp_smchk: <integer>
                tpe_id: <integer>
                tpe_id_v: <value in [disable, enable]>
                vdm: <integer>
                vdm_v: <value in [disable, enable]>
                vdom_id: <integer>
                vdom_id_v: <value in [disable, enable]>
                x_mode: <integer>
                x_mode_v: <value in [disable, enable]>
              tact:
                act: <integer>
                act_v: <value in [disable, enable]>
                fmtuv4_s: <integer>
                fmtuv4_s_v: <value in [disable, enable]>
                fmtuv6_s: <integer>
                fmtuv6_s_v: <value in [disable, enable]>
                lnkid: <integer>
                lnkid_v: <value in [disable, enable]>
                mac_id: <integer>
                mac_id_v: <value in [disable, enable]>
                mss_t: <integer>
                mss_t_v: <value in [disable, enable]>
                mtuv4: <integer>
                mtuv4_v: <value in [disable, enable]>
                mtuv6: <integer>
                mtuv6_v: <value in [disable, enable]>
                slif_act: <integer>
                slif_act_v: <value in [disable, enable]>
                sublnkid: <integer>
                sublnkid_v: <value in [disable, enable]>
                tgtv_act: <integer>
                tgtv_act_v: <value in [disable, enable]>
                tlif_act: <integer>
                tlif_act_v: <value in [disable, enable]>
                tpeid: <integer>
                tpeid_v: <value in [disable, enable]>
                v6fe: <integer>
                v6fe_v: <value in [disable, enable]>
                vep_en_v: <value in [disable, enable]>
                vep_slid: <integer>
                vep_slid_v: <value in [disable, enable]>
                vep_en: <integer>
                xlt_lif: <integer>
                xlt_lif_v: <value in [disable, enable]>
                xlt_vid: <integer>
                xlt_vid_v: <value in [disable, enable]>
              type: <value in [L2_src_tc, L2_tgt_tc, L2_src_mir, ...]>
              vid: <integer>
          icmp_rate_ctrl:
            icmp_v4_bucket_size: <integer>
            icmp_v4_rate: <integer>
            icmp_v6_bucket_size: <integer>
            icmp_v6_rate: <integer>
          vxlan_offload: <value in [disable, enable]>
          icmp_error_rate_ctrl:
            icmpv4_error_bucket_size: <integer>
            icmpv4_error_rate: <integer>
            icmpv4_error_rate_limit: <value in [disable, enable]>
            icmpv6_error_bucket_size: <integer>
            icmpv6_error_rate: <integer>
            icmpv6_error_rate_limit: <value in [disable, enable]>
          ipv4_session_quota: <value in [disable, enable]>
          ipv4_session_quota_high: <integer>
          ipv4_session_quota_low: <integer>
          ipv6_prefix_session_quota: <value in [disable, enable]>
          ipv6_prefix_session_quota_high: <integer>
          ipv6_prefix_session_quota_low: <integer>
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
        '/pm/config/adom/{adom}/obj/system/npu',
        '/pm/config/global/obj/system/npu'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/system/npu/{npu}',
        '/pm/config/global/obj/system/npu/{npu}'
    ]

    url_params = ['adom']
    module_primary_key = None
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'system_npu': {
            'type': 'dict',
            'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
            'options': {
                'capwap-offload': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'dedicated-management-affinity': {'v_range': [['7.0.1', '']], 'type': 'str'},
                'dedicated-management-cpu': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'fastpath': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'fp-anomaly': {
                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                    'type': 'dict',
                    'options': {
                        'esp-minlen-err': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['drop', 'trap-to-host'], 'type': 'str'},
                        'icmp-csum-err': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['drop', 'trap-to-host'], 'type': 'str'},
                        'icmp-minlen-err': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['drop', 'trap-to-host'], 'type': 'str'},
                        'ipv4-csum-err': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['drop', 'trap-to-host'], 'type': 'str'},
                        'ipv4-ihl-err': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['drop', 'trap-to-host'], 'type': 'str'},
                        'ipv4-len-err': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['drop', 'trap-to-host'], 'type': 'str'},
                        'ipv4-opt-err': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['drop', 'trap-to-host'], 'type': 'str'},
                        'ipv4-ttlzero-err': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['drop', 'trap-to-host'], 'type': 'str'},
                        'ipv4-ver-err': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['drop', 'trap-to-host'], 'type': 'str'},
                        'ipv6-exthdr-len-err': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['drop', 'trap-to-host'], 'type': 'str'},
                        'ipv6-exthdr-order-err': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['drop', 'trap-to-host'], 'type': 'str'},
                        'ipv6-ihl-err': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['drop', 'trap-to-host'], 'type': 'str'},
                        'ipv6-plen-zero': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['drop', 'trap-to-host'], 'type': 'str'},
                        'ipv6-ver-err': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['drop', 'trap-to-host'], 'type': 'str'},
                        'tcp-csum-err': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['drop', 'trap-to-host'], 'type': 'str'},
                        'tcp-hlen-err': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['drop', 'trap-to-host'], 'type': 'str'},
                        'tcp-plen-err': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['drop', 'trap-to-host'], 'type': 'str'},
                        'udp-csum-err': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['drop', 'trap-to-host'], 'type': 'str'},
                        'udp-hlen-err': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['drop', 'trap-to-host'], 'type': 'str'},
                        'udp-len-err': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['drop', 'trap-to-host'], 'type': 'str'},
                        'udp-plen-err': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['drop', 'trap-to-host'], 'type': 'str'},
                        'udplite-cover-err': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['drop', 'trap-to-host'], 'type': 'str'},
                        'udplite-csum-err': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['drop', 'trap-to-host'], 'type': 'str'},
                        'unknproto-minlen-err': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['drop', 'trap-to-host'], 'type': 'str'},
                        'tcp-fin-only': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['allow', 'drop', 'trap-to-host'], 'type': 'str'},
                        'ipv4-optsecurity': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['allow', 'drop', 'trap-to-host'], 'type': 'str'},
                        'ipv6-optralert': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['allow', 'drop', 'trap-to-host'], 'type': 'str'},
                        'tcp-syn-fin': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['allow', 'drop', 'trap-to-host'], 'type': 'str'},
                        'ipv4-proto-err': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['allow', 'drop', 'trap-to-host'], 'type': 'str'},
                        'ipv6-saddr-err': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['allow', 'drop', 'trap-to-host'], 'type': 'str'},
                        'icmp-frag': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['allow', 'drop', 'trap-to-host'], 'type': 'str'},
                        'ipv4-optssrr': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['allow', 'drop', 'trap-to-host'], 'type': 'str'},
                        'ipv6-opthomeaddr': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['allow', 'drop', 'trap-to-host'], 'type': 'str'},
                        'udp-land': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['allow', 'drop', 'trap-to-host'], 'type': 'str'},
                        'ipv6-optinvld': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['allow', 'drop', 'trap-to-host'], 'type': 'str'},
                        'tcp-fin-noack': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['allow', 'drop', 'trap-to-host'], 'type': 'str'},
                        'ipv6-proto-err': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['allow', 'drop', 'trap-to-host'], 'type': 'str'},
                        'tcp-land': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['allow', 'drop', 'trap-to-host'], 'type': 'str'},
                        'ipv4-unknopt': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['allow', 'drop', 'trap-to-host'], 'type': 'str'},
                        'ipv4-optstream': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['allow', 'drop', 'trap-to-host'], 'type': 'str'},
                        'ipv6-optjumbo': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['allow', 'drop', 'trap-to-host'], 'type': 'str'},
                        'icmp-land': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['allow', 'drop', 'trap-to-host'], 'type': 'str'},
                        'tcp-winnuke': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['allow', 'drop', 'trap-to-host'], 'type': 'str'},
                        'ipv6-daddr-err': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['allow', 'drop', 'trap-to-host'], 'type': 'str'},
                        'ipv4-land': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['allow', 'drop', 'trap-to-host'], 'type': 'str'},
                        'ipv6-opttunnel': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['allow', 'drop', 'trap-to-host'], 'type': 'str'},
                        'tcp-no-flag': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['allow', 'drop', 'trap-to-host'], 'type': 'str'},
                        'ipv6-land': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['allow', 'drop', 'trap-to-host'], 'type': 'str'},
                        'ipv4-optlsrr': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['allow', 'drop', 'trap-to-host'], 'type': 'str'},
                        'ipv4-opttimestamp': {
                            'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                            'choices': ['allow', 'drop', 'trap-to-host'],
                            'type': 'str'
                        },
                        'ipv4-optrr': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['allow', 'drop', 'trap-to-host'], 'type': 'str'},
                        'ipv6-optnsap': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['allow', 'drop', 'trap-to-host'], 'type': 'str'},
                        'ipv6-unknopt': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['allow', 'drop', 'trap-to-host'], 'type': 'str'},
                        'tcp-syn-data': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['allow', 'drop', 'trap-to-host'], 'type': 'str'},
                        'ipv6-optendpid': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['allow', 'drop', 'trap-to-host'], 'type': 'str'},
                        'gtpu-plen-err': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['drop', 'trap-to-host'], 'type': 'str'},
                        'vxlan-minlen-err': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['drop', 'trap-to-host'], 'type': 'str'},
                        'capwap-minlen-err': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['drop', 'trap-to-host'], 'type': 'str'},
                        'gre-csum-err': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['drop', 'trap-to-host'], 'type': 'str'},
                        'nvgre-minlen-err': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['drop', 'trap-to-host'], 'type': 'str'},
                        'sctp-l4len-err': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['drop', 'trap-to-host'], 'type': 'str'},
                        'tcp-hlenvsl4len-err': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['drop', 'trap-to-host'], 'type': 'str'},
                        'sctp-crc-err': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['drop', 'trap-to-host'], 'type': 'str'},
                        'sctp-clen-err': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['drop', 'trap-to-host'], 'type': 'str'},
                        'uesp-minlen-err': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['drop', 'trap-to-host'], 'type': 'str'},
                        'sctp-csum-err': {'v_range': [['7.2.5', '7.2.5'], ['7.4.3', '']], 'choices': ['allow', 'drop', 'trap-to-host'], 'type': 'str'}
                    }
                },
                'gtp-enhanced-cpu-range': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['0', '1', '2'], 'type': 'str'},
                'gtp-enhanced-mode': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'host-shortcut-mode': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['bi-directional', 'host-shortcut'], 'type': 'str'},
                'htx-gtse-quota': {
                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                    'choices': [
                        '100Mbps', '200Mbps', '300Mbps', '400Mbps', '500Mbps', '600Mbps', '700Mbps', '800Mbps', '900Mbps', '1Gbps', '2Gbps', '4Gbps',
                        '8Gbps', '10Gbps'
                    ],
                    'type': 'str'
                },
                'intf-shaping-offload': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'iph-rsvd-re-cksum': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ipsec-dec-subengine-mask': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'str'},
                'ipsec-enc-subengine-mask': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'str'},
                'ipsec-inbound-cache': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ipsec-mtu-override': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ipsec-over-vlink': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'isf-np-queues': {
                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                    'type': 'dict',
                    'options': {
                        'cos0': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'str'},
                        'cos1': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'str'},
                        'cos2': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'str'},
                        'cos3': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'str'},
                        'cos4': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'str'},
                        'cos5': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'str'},
                        'cos6': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'str'},
                        'cos7': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'str'}
                    }
                },
                'lag-out-port-select': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'mcast-session-accounting': {
                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                    'choices': ['disable', 'session-based', 'tpe-based'],
                    'type': 'str'
                },
                'np6-cps-optimization-mode': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'per-session-accounting': {
                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                    'choices': ['enable', 'disable', 'enable-by-log', 'all-enable', 'traffic-log-only'],
                    'type': 'str'
                },
                'port-cpu-map': {
                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                    'type': 'list',
                    'options': {
                        'cpu-core': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'str'},
                        'interface': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'str'}
                    },
                    'elements': 'dict'
                },
                'port-npu-map': {
                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                    'type': 'list',
                    'options': {
                        'interface': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'str'},
                        'npu-group-index': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'}
                    },
                    'elements': 'dict'
                },
                'priority-protocol': {
                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                    'type': 'dict',
                    'options': {
                        'bfd': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'bgp': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'slbc': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'}
                    }
                },
                'qos-mode': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['disable', 'priority', 'round-robin'], 'type': 'str'},
                'rdp-offload': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'recover-np6-link': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'session-denied-offload': {'v_range': [['7.0.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'sse-backpressure': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'strip-clear-text-padding': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'strip-esp-padding': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'sw-eh-hash': {
                    'v_range': [['7.0.1', '']],
                    'type': 'dict',
                    'options': {
                        'computation': {'v_range': [['7.0.1', '']], 'choices': ['xor16', 'xor8', 'xor4', 'crc16'], 'type': 'str'},
                        'destination-ip-lower-16': {'v_range': [['7.0.1', '']], 'choices': ['include', 'exclude'], 'type': 'str'},
                        'destination-ip-upper-16': {'v_range': [['7.0.1', '']], 'choices': ['include', 'exclude'], 'type': 'str'},
                        'destination-port': {'v_range': [['7.0.1', '']], 'choices': ['include', 'exclude'], 'type': 'str'},
                        'ip-protocol': {'v_range': [['7.0.1', '']], 'choices': ['include', 'exclude'], 'type': 'str'},
                        'netmask-length': {'v_range': [['7.0.1', '']], 'type': 'int'},
                        'source-ip-lower-16': {'v_range': [['7.0.1', '']], 'choices': ['include', 'exclude'], 'type': 'str'},
                        'source-ip-upper-16': {'v_range': [['7.0.1', '']], 'choices': ['include', 'exclude'], 'type': 'str'},
                        'source-port': {'v_range': [['7.0.1', '']], 'choices': ['include', 'exclude'], 'type': 'str'}
                    }
                },
                'sw-np-bandwidth': {
                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                    'choices': ['0G', '2G', '4G', '5G', '6G', '7G', '8G', '9G'],
                    'type': 'str'
                },
                'switch-np-hash': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['src-ip', 'dst-ip', 'src-dst-ip'], 'type': 'str'},
                'uesp-offload': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'np-queues': {
                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                    'type': 'dict',
                    'options': {
                        'ethernet-type': {
                            'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                            'type': 'list',
                            'options': {
                                'name': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'str'},
                                'queue': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                                'type': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                                'weight': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'}
                            },
                            'elements': 'dict'
                        },
                        'ip-protocol': {
                            'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                            'type': 'list',
                            'options': {
                                'name': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'str'},
                                'protocol': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                                'queue': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                                'weight': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'}
                            },
                            'elements': 'dict'
                        },
                        'ip-service': {
                            'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                            'type': 'list',
                            'options': {
                                'dport': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                                'name': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'str'},
                                'protocol': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                                'queue': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                                'sport': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                                'weight': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'}
                            },
                            'elements': 'dict'
                        },
                        'profile': {
                            'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                            'type': 'list',
                            'options': {
                                'cos0': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'cos1': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'cos2': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'cos3': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'cos4': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'cos5': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'cos6': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'cos7': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp0': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp1': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp10': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp11': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp12': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp13': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp14': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp15': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp16': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp17': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp18': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp19': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp2': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp20': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp21': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp22': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp23': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp24': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp25': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp26': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp27': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp28': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp29': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp3': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp30': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp31': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp32': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp33': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp34': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp35': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp36': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp37': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp38': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp39': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp4': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp40': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp41': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp42': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp43': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp44': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp45': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp46': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp47': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp48': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp49': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp5': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp50': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp51': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp52': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp53': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp54': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp55': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp56': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp57': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp58': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp59': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp6': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp60': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp61': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp62': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp63': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp7': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp8': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'dscp9': {
                                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                                    'choices': ['queue0', 'queue1', 'queue2', 'queue3', 'queue4', 'queue5', 'queue6', 'queue7'],
                                    'type': 'str'
                                },
                                'id': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                                'type': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['cos', 'dscp'], 'type': 'str'},
                                'weight': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'}
                            },
                            'elements': 'dict'
                        },
                        'scheduler': {
                            'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                            'type': 'list',
                            'options': {
                                'mode': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['none', 'priority', 'round-robin'], 'type': 'str'},
                                'name': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'str'}
                            },
                            'elements': 'dict'
                        }
                    }
                },
                'udp-timeout-profile': {
                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                    'type': 'list',
                    'options': {
                        'id': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                        'udp-idle': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'}
                    },
                    'elements': 'dict'
                },
                'qtm-buf-mode': {'v_range': [['6.4.8', '6.4.14'], ['7.0.3', '']], 'choices': ['6ch', '4ch'], 'type': 'str'},
                'default-qos-type': {
                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                    'choices': ['policing', 'shaping', 'policing-enhanced'],
                    'type': 'str'
                },
                'tcp-rst-timeout': {'v_range': [['6.4.7', '6.4.14'], ['7.0.2', '']], 'type': 'int'},
                'ipsec-local-uesp-port': {'v_range': [['7.0.3', '']], 'type': 'int'},
                'htab-dedi-queue-nr': {'v_range': [['6.4.7', '6.4.14'], ['7.0.2', '']], 'type': 'int'},
                'double-level-mcast-offload': {'v_range': [['6.4.7', '6.4.14'], ['7.0.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'dse-timeout': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                'ippool-overload-low': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                'pba-eim': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['disallow', 'allow'], 'type': 'str'},
                'policy-offload-level': {
                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                    'choices': ['disable', 'dos-offload', 'full-offload'],
                    'type': 'str'
                },
                'max-session-timeout': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                'port-path-option': {
                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                    'type': 'dict',
                    'options': {'ports-using-npu': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'raw'}}
                },
                'vlan-lookup-cache': {'v_range': [['6.4.7', '6.4.14'], ['7.0.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'dos-options': {
                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                    'type': 'dict',
                    'options': {
                        'npu-dos-meter-mode': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['local', 'global'], 'type': 'str'},
                        'npu-dos-synproxy-mode': {
                            'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                            'choices': ['synack2ack', 'pass-synack'],
                            'type': 'str'
                        },
                        'npu-dos-tpe-mode': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'}
                    }
                },
                'hash-tbl-spread': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'tcp-timeout-profile': {
                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                    'type': 'list',
                    'options': {
                        'close-wait': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                        'fin-wait': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                        'id': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                        'syn-sent': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                        'syn-wait': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                        'tcp-idle': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                        'time-wait': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'}
                    },
                    'elements': 'dict'
                },
                'ip-reassembly': {
                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                    'type': 'dict',
                    'options': {
                        'max-timeout': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                        'min-timeout': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                        'status': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'}
                    }
                },
                'gtp-support': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'htx-icmp-csum-chk': {'v_range': [['6.4.8', '6.4.14'], ['7.0.3', '']], 'choices': ['pass', 'drop'], 'type': 'str'},
                'hpe': {
                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                    'type': 'dict',
                    'options': {
                        'all-protocol': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                        'arp-max': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                        'enable-shaper': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'esp-max': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                        'high-priority': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                        'icmp-max': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                        'ip-frag-max': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                        'ip-others-max': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                        'l2-others-max': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                        'pri-type-max': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                        'sctp-max': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                        'tcp-max': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                        'tcpfin-rst-max': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                        'tcpsyn-ack-max': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                        'tcpsyn-max': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                        'udp-max': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                        'enable-queue-shaper': {
                            'v_range': [['7.0.9', '7.0.12'], ['7.2.4', '7.2.5'], ['7.4.2', '']],
                            'choices': ['disable', 'enable'],
                            'type': 'str'
                        },
                        'exception-code': {'v_range': [['7.0.9', '7.0.12'], ['7.2.4', '7.2.5'], ['7.4.2', '']], 'type': 'int'},
                        'fragment-with-sess': {'v_range': [['7.0.9', '7.0.12'], ['7.2.4', '7.2.5'], ['7.4.2', '']], 'type': 'int'},
                        'fragment-without-session': {'v_range': [['7.0.9', '7.0.12'], ['7.2.4', '7.2.5'], ['7.4.2', '']], 'type': 'int'},
                        'queue-shaper-max': {'v_range': [['7.0.9', '7.0.12'], ['7.2.4', '7.2.5'], ['7.4.2', '']], 'type': 'int'}
                    }
                },
                'dsw-dts-profile': {
                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                    'type': 'list',
                    'options': {
                        'action': {
                            'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                            'choices': ['wait', 'drop', 'drop_tmr_0', 'drop_tmr_1', 'enque', 'enque_0', 'enque_1'],
                            'type': 'str'
                        },
                        'min-limit': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                        'profile-id': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                        'step': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'}
                    },
                    'elements': 'dict'
                },
                'hash-config': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['5-tuple', 'src-ip', 'src-dst-ip'], 'type': 'str'},
                'ipsec-ob-np-sel': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['RR', 'rr', 'Packet', 'Hash'], 'type': 'str'},
                'napi-break-interval': {'v_range': [['6.4.7', '6.4.14'], ['7.0.2', '']], 'type': 'int'},
                'background-sse-scan': {
                    'v_range': [['6.4.8', '6.4.14'], ['7.0.3', '']],
                    'type': 'dict',
                    'options': {
                        'scan': {'v_range': [['6.4.8', '6.4.14'], ['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'stats-update-interval': {'v_range': [['6.4.8', '6.4.14'], ['7.0.3', '']], 'type': 'int'},
                        'udp-keepalive-interval': {'v_range': [['6.4.8', '6.4.14'], ['7.0.3', '']], 'type': 'int'},
                        'scan-stale': {'v_range': [['7.0.12', '7.0.12'], ['7.4.1', '']], 'type': 'int'},
                        'scan-vt': {'v_range': [['7.0.12', '7.0.12'], ['7.4.1', '']], 'type': 'int'},
                        'stats-qual-access': {'v_range': [['7.0.12', '7.0.12'], ['7.4.1', '']], 'type': 'int'},
                        'stats-qual-duration': {'v_range': [['7.0.12', '7.0.12'], ['7.4.1', '']], 'type': 'int'},
                        'udp-qual-access': {'v_range': [['7.0.12', '7.0.12'], ['7.4.1', '']], 'type': 'int'},
                        'udp-qual-duration': {'v_range': [['7.0.12', '7.0.12'], ['7.4.1', '']], 'type': 'int'}
                    }
                },
                'inbound-dscp-copy-port': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'raw'},
                'session-acct-interval': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                'htab-msg-queue': {'v_range': [['6.4.7', '6.4.14'], ['7.0.2', '']], 'choices': ['idle', 'data', 'dedicated'], 'type': 'str'},
                'dsw-queue-dts-profile': {
                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                    'type': 'list',
                    'options': {
                        'iport': {
                            'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                            'choices': [
                                'EIF0', 'eif0', 'EIF1', 'eif1', 'EIF2', 'eif2', 'EIF3', 'eif3', 'EIF4', 'eif4', 'EIF5', 'eif5', 'EIF6', 'eif6', 'EIF7',
                                'eif7', 'HTX0', 'htx0', 'HTX1', 'htx1', 'SSE0', 'sse0', 'SSE1', 'sse1', 'SSE2', 'sse2', 'SSE3', 'sse3', 'RLT', 'rlt',
                                'DFR', 'dfr', 'IPSECI', 'ipseci', 'IPSECO', 'ipseco', 'IPTI', 'ipti', 'IPTO', 'ipto', 'VEP0', 'vep0', 'VEP2', 'vep2',
                                'VEP4', 'vep4', 'VEP6', 'vep6', 'IVS', 'ivs', 'L2TI1', 'l2ti1', 'L2TO', 'l2to', 'L2TI0', 'l2ti0', 'PLE', 'ple', 'SPATH',
                                'spath', 'QTM', 'qtm'
                            ],
                            'type': 'str'
                        },
                        'name': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'str'},
                        'oport': {
                            'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                            'choices': [
                                'EIF0', 'eif0', 'EIF1', 'eif1', 'EIF2', 'eif2', 'EIF3', 'eif3', 'EIF4', 'eif4', 'EIF5', 'eif5', 'EIF6', 'eif6', 'EIF7',
                                'eif7', 'HRX', 'hrx', 'SSE0', 'sse0', 'SSE1', 'sse1', 'SSE2', 'sse2', 'SSE3', 'sse3', 'RLT', 'rlt', 'DFR', 'dfr',
                                'IPSECI', 'ipseci', 'IPSECO', 'ipseco', 'IPTI', 'ipti', 'IPTO', 'ipto', 'VEP0', 'vep0', 'VEP2', 'vep2', 'VEP4', 'vep4',
                                'VEP6', 'vep6', 'IVS', 'ivs', 'L2TI1', 'l2ti1', 'L2TO', 'l2to', 'L2TI0', 'l2ti0', 'PLE', 'ple', 'SYNK', 'sync', 'NSS',
                                'nss', 'TSK', 'tsk', 'QTM', 'qtm', 'l2tO'
                            ],
                            'type': 'str'
                        },
                        'profile-id': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                        'queue-select': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'}
                    },
                    'elements': 'dict'
                },
                'hw-ha-scan-interval': {'v_range': [['6.4.8', '6.4.14'], ['7.0.3', '']], 'type': 'int'},
                'ippool-overload-high': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                'nat46-force-ipv4-packet-forwarding': {'v_range': [['6.4.8', '6.4.14'], ['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'prp-port-out': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'raw'},
                'isf-np-rx-tr-distr': {
                    'v_range': [['6.4.8', '6.4.14'], ['7.0.4', '']],
                    'choices': ['port-flow', 'round-robin', 'randomized'],
                    'type': 'str'
                },
                'mcast-session-counting6': {
                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                    'choices': ['disable', 'enable', 'session-based', 'tpe-based'],
                    'type': 'str'
                },
                'prp-port-in': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'type': 'raw'},
                'rps-mode': {'v_range': [['6.4.8', '6.4.14'], ['7.0.4', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'per-policy-accounting': {'v_range': [['6.4.8', '6.4.14'], ['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'mcast-session-counting': {
                    'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']],
                    'choices': ['disable', 'enable', 'session-based', 'tpe-based'],
                    'type': 'str'
                },
                'inbound-dscp-copy': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ipsec-host-dfclr': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '7.2.1']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'process-icmp-by-host': {'v_range': [['6.4.7', '6.4.14'], ['7.0.1', '7.2.1']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'dedicated-tx-npu': {'v_range': [['6.4.7', '6.4.14']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ull-port-mode': {'v_range': [['6.4.9', '6.4.14'], ['7.0.4', '7.0.12'], ['7.2.1', '']], 'choices': ['10G', '25G'], 'type': 'str'},
                'sse-ha-scan': {
                    'v_range': [['6.4.10', '6.4.14'], ['7.0.4', '7.0.12'], ['7.2.1', '']],
                    'type': 'dict',
                    'options': {
                        'gap': {'v_range': [['6.4.10', '6.4.14'], ['7.0.4', '7.0.12'], ['7.2.1', '']], 'type': 'int'},
                        'max-session-cnt': {'v_range': [['6.4.10', '6.4.14'], ['7.0.4', '7.0.12'], ['7.2.1', '']], 'type': 'int'},
                        'min-duration': {'v_range': [['6.4.10', '6.4.14'], ['7.0.4', '7.0.12'], ['7.2.1', '']], 'type': 'int'}
                    }
                },
                'hash-ipv6-sel': {'v_range': [['7.0.4', '7.0.12'], ['7.2.1', '']], 'type': 'int'},
                'ip-fragment-offload': {'v_range': [['7.0.4', '7.0.12'], ['7.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ple-non-syn-tcp-action': {'v_range': [['7.0.5', '7.0.12'], ['7.2.2', '']], 'choices': ['forward', 'drop'], 'type': 'str'},
                'npu-group-effective-scope': {'v_range': [['7.0.6', '7.0.12'], ['7.2.2', '']], 'type': 'int'},
                'ipsec-STS-timeout': {
                    'v_range': [['7.0.9', '7.0.12'], ['7.2.4', '7.2.5'], ['7.4.2', '']],
                    'choices': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
                    'type': 'str'
                },
                'ipsec-throughput-msg-frequency': {
                    'v_range': [['7.0.9', '7.0.12'], ['7.2.4', '7.2.5'], ['7.4.2', '']],
                    'choices': [
                        'disable', '32KB', '64KB', '128KB', '256KB', '512KB', '1MB', '2MB', '4MB', '8MB', '16MB', '32MB', '64MB', '128MB', '256MB',
                        '512MB', '1GB'
                    ],
                    'type': 'str'
                },
                'ipt-STS-timeout': {
                    'v_range': [['7.0.9', '7.0.12'], ['7.2.4', '7.2.5'], ['7.4.2', '']],
                    'choices': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
                    'type': 'str'
                },
                'ipt-throughput-msg-frequency': {
                    'v_range': [['7.0.9', '7.0.12'], ['7.2.4', '7.2.5'], ['7.4.2', '']],
                    'choices': [
                        'disable', '32KB', '64KB', '128KB', '256KB', '512KB', '1MB', '2MB', '4MB', '8MB', '16MB', '32MB', '64MB', '128MB', '256MB',
                        '512MB', '1GB'
                    ],
                    'type': 'str'
                },
                'default-tcp-refresh-dir': {'v_range': [['7.0.12', '7.0.12'], ['7.4.1', '']], 'choices': ['both', 'outgoing', 'incoming'], 'type': 'str'},
                'default-udp-refresh-dir': {'v_range': [['7.0.12', '7.0.12'], ['7.4.1', '']], 'choices': ['both', 'outgoing', 'incoming'], 'type': 'str'},
                'nss-threads-option': {'v_range': [['7.0.12', '7.0.12'], ['7.4.2', '']], 'choices': ['4t-eif', '4t-noeif', '2t'], 'type': 'str'},
                'prp-session-clear-mode': {'v_range': [['7.2.2', '']], 'choices': ['blocking', 'non-blocking', 'do-not-clear'], 'type': 'str'},
                'shaping-stats': {'v_range': [['7.2.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'sw-tr-hash': {
                    'v_range': [['7.2.4', '']],
                    'type': 'dict',
                    'options': {
                        'draco15': {'v_range': [['7.2.4', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'tcp-udp-port': {'v_range': [['7.2.4', '']], 'choices': ['include', 'exclude'], 'type': 'str'}
                    }
                },
                'pba-port-select-mode': {'v_range': [['7.2.5', '7.2.5'], ['7.4.2', '']], 'choices': ['random', 'direct'], 'type': 'str'},
                'spa-port-select-mode': {'v_range': [['7.2.5', '7.2.5'], ['7.4.2', '']], 'choices': ['random', 'direct'], 'type': 'str'},
                'split-ipsec-engines': {'v_range': [['7.2.5', '7.2.5'], ['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'tunnel-over-vlink': {'v_range': [['7.2.5', '7.2.5'], ['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'max-receive-unit': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'npu-tcam': {
                    'v_range': [['7.4.2', '']],
                    'type': 'list',
                    'options': {
                        'data': {
                            'v_range': [['7.4.2', '']],
                            'type': 'dict',
                            'options': {
                                'df': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'dstip': {'v_range': [['7.4.2', '']], 'type': 'str'},
                                'dstipv6': {'v_range': [['7.4.2', '']], 'type': 'str'},
                                'dstmac': {'v_range': [['7.4.2', '']], 'type': 'str'},
                                'dstport': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'ethertype': {'v_range': [['7.4.2', '']], 'type': 'str'},
                                'ext-tag': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'frag-off': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'gen-buf-cnt': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'gen-iv': {'v_range': [['7.4.2', '']], 'choices': ['invalid', 'valid'], 'type': 'str'},
                                'gen-l3-flags': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'gen-l4-flags': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'gen-pkt-ctrl': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'gen-pri': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'gen-pri-v': {'v_range': [['7.4.2', '']], 'choices': ['invalid', 'valid'], 'type': 'str'},
                                'gen-tv': {'v_range': [['7.4.2', '']], 'choices': ['invalid', 'valid'], 'type': 'str'},
                                'ihl': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'ip4-id': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'ip6-fl': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'ipver': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'l4-wd10': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'l4-wd11': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'l4-wd8': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'l4-wd9': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'mf': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'protocol': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'slink': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'smac-change': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'sp': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'src-cfi': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'src-prio': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'src-updt': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'srcip': {'v_range': [['7.4.2', '']], 'type': 'str'},
                                'srcipv6': {'v_range': [['7.4.2', '']], 'type': 'str'},
                                'srcmac': {'v_range': [['7.4.2', '']], 'type': 'str'},
                                'srcport': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'svid': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'tcp-ack': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'tcp-cwr': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'tcp-ece': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'tcp-fin': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'tcp-push': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'tcp-rst': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'tcp-syn': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'tcp-urg': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'tgt-cfi': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'tgt-prio': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'tgt-updt': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'tgt-v': {'v_range': [['7.4.2', '']], 'choices': ['invalid', 'valid'], 'type': 'str'},
                                'tos': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'tp': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'ttl': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'tvid': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'vdid': {'v_range': [['7.4.2', '']], 'type': 'int'}
                            }
                        },
                        'dbg-dump': {'v_range': [['7.4.2', '']], 'type': 'int'},
                        'mask': {
                            'v_range': [['7.4.2', '']],
                            'type': 'dict',
                            'options': {
                                'df': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'dstip': {'v_range': [['7.4.2', '']], 'type': 'str'},
                                'dstipv6': {'v_range': [['7.4.2', '']], 'type': 'str'},
                                'dstmac': {'v_range': [['7.4.2', '']], 'type': 'str'},
                                'dstport': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'ethertype': {'v_range': [['7.4.2', '']], 'type': 'str'},
                                'ext-tag': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'frag-off': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'gen-buf-cnt': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'gen-iv': {'v_range': [['7.4.2', '']], 'choices': ['invalid', 'valid'], 'type': 'str'},
                                'gen-l3-flags': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'gen-l4-flags': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'gen-pkt-ctrl': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'gen-pri': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'gen-pri-v': {'v_range': [['7.4.2', '']], 'choices': ['invalid', 'valid'], 'type': 'str'},
                                'gen-tv': {'v_range': [['7.4.2', '']], 'choices': ['invalid', 'valid'], 'type': 'str'},
                                'ihl': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'ip4-id': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'ip6-fl': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'ipver': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'l4-wd10': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'l4-wd11': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'l4-wd8': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'l4-wd9': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'mf': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'protocol': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'slink': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'smac-change': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'sp': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'src-cfi': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'src-prio': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'src-updt': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'srcip': {'v_range': [['7.4.2', '']], 'type': 'str'},
                                'srcipv6': {'v_range': [['7.4.2', '']], 'type': 'str'},
                                'srcmac': {'v_range': [['7.4.2', '']], 'type': 'str'},
                                'srcport': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'svid': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'tcp-ack': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'tcp-cwr': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'tcp-ece': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'tcp-fin': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'tcp-push': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'tcp-rst': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'tcp-syn': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'tcp-urg': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'tgt-cfi': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'tgt-prio': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'tgt-updt': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'tgt-v': {'v_range': [['7.4.2', '']], 'choices': ['invalid', 'valid'], 'type': 'str'},
                                'tos': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'tp': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'ttl': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'tvid': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'vdid': {'v_range': [['7.4.2', '']], 'type': 'int'}
                            }
                        },
                        'mir-act': {'v_range': [['7.4.2', '']], 'type': 'dict', 'options': {'vlif': {'v_range': [['7.4.2', '']], 'type': 'int'}}},
                        'name': {'v_range': [['7.4.2', '']], 'type': 'str'},
                        'oid': {'v_range': [['7.4.2', '']], 'type': 'int'},
                        'pri-act': {
                            'v_range': [['7.4.2', '']],
                            'type': 'dict',
                            'options': {'priority': {'v_range': [['7.4.2', '']], 'type': 'int'}, 'weight': {'v_range': [['7.4.2', '']], 'type': 'int'}}
                        },
                        'sact': {
                            'v_range': [['7.4.2', '']],
                            'type': 'dict',
                            'options': {
                                'act': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'act-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'bmproc': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'bmproc-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'df-lif': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'df-lif-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'dfr': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'dfr-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'dmac-skip': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'dmac-skip-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'dosen': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'dosen-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'espff-proc': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'espff-proc-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'etype-pid': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'etype-pid-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'frag-proc': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'frag-proc-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'fwd': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'fwd-lif': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'fwd-lif-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'fwd-tvid': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'fwd-tvid-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'fwd-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'icpen': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'icpen-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'igmp-mld-snp': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'igmp-mld-snp-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'learn': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'learn-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'm-srh-ctrl': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'm-srh-ctrl-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'mac-id': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'mac-id-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'mss': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'mss-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'pleen': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'pleen-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'prio-pid': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'prio-pid-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'promis': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'promis-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'rfsh': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'rfsh-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'smac-skip': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'smac-skip-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'tp-smchk-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'tp_smchk': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'tpe-id': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'tpe-id-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'vdm': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'vdm-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'vdom-id': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'vdom-id-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'x-mode': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'x-mode-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'}
                            }
                        },
                        'tact': {
                            'v_range': [['7.4.2', '']],
                            'type': 'dict',
                            'options': {
                                'act': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'act-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'fmtuv4-s': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'fmtuv4-s-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'fmtuv6-s': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'fmtuv6-s-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'lnkid': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'lnkid-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'mac-id': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'mac-id-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'mss-t': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'mss-t-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'mtuv4': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'mtuv4-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'mtuv6': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'mtuv6-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'slif-act': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'slif-act-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'sublnkid': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'sublnkid-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'tgtv-act': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'tgtv-act-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'tlif-act': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'tlif-act-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'tpeid': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'tpeid-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'v6fe': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'v6fe-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'vep-en-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'vep-slid': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'vep-slid-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'vep_en': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'xlt-lif': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'xlt-lif-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'xlt-vid': {'v_range': [['7.4.2', '']], 'type': 'int'},
                                'xlt-vid-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'}
                            }
                        },
                        'type': {
                            'v_range': [['7.4.2', '']],
                            'choices': [
                                'L2_src_tc', 'L2_tgt_tc', 'L2_src_mir', 'L2_tgt_mir', 'L2_src_act', 'L2_tgt_act', 'IPv4_src_tc', 'IPv4_tgt_tc',
                                'IPv4_src_mir', 'IPv4_tgt_mir', 'IPv4_src_act', 'IPv4_tgt_act', 'IPv6_src_tc', 'IPv6_tgt_tc', 'IPv6_src_mir',
                                'IPv6_tgt_mir', 'IPv6_src_act', 'IPv6_tgt_act'
                            ],
                            'type': 'str'
                        },
                        'vid': {'v_range': [['7.4.2', '']], 'type': 'int'}
                    },
                    'elements': 'dict'
                },
                'icmp-rate-ctrl': {
                    'v_range': [['7.4.3', '']],
                    'type': 'dict',
                    'options': {
                        'icmp-v4-bucket-size': {'v_range': [['7.4.3', '']], 'type': 'int'},
                        'icmp-v4-rate': {'v_range': [['7.4.3', '']], 'type': 'int'},
                        'icmp-v6-bucket-size': {'v_range': [['7.4.3', '']], 'type': 'int'},
                        'icmp-v6-rate': {'v_range': [['7.4.3', '']], 'type': 'int'}
                    }
                },
                'vxlan-offload': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'icmp-error-rate-ctrl': {
                    'v_range': [['7.6.0', '']],
                    'type': 'dict',
                    'options': {
                        'icmpv4-error-bucket-size': {'v_range': [['7.6.0', '']], 'type': 'int'},
                        'icmpv4-error-rate': {'v_range': [['7.6.0', '']], 'type': 'int'},
                        'icmpv4-error-rate-limit': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'icmpv6-error-bucket-size': {'v_range': [['7.6.0', '']], 'type': 'int'},
                        'icmpv6-error-rate': {'v_range': [['7.6.0', '']], 'type': 'int'},
                        'icmpv6-error-rate-limit': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'}
                    }
                },
                'ipv4-session-quota': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ipv4-session-quota-high': {'v_range': [['7.6.0', '']], 'type': 'int'},
                'ipv4-session-quota-low': {'v_range': [['7.6.0', '']], 'type': 'int'},
                'ipv6-prefix-session-quota': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ipv6-prefix-session-quota-high': {'v_range': [['7.6.0', '']], 'type': 'int'},
                'ipv6-prefix-session-quota-low': {'v_range': [['7.6.0', '']], 'type': 'int'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('partial crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'system_npu'),
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
