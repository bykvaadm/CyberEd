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
module: fmgr_fsp_vlan_interface
short_description: Configure interfaces.
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
    vlan:
        description: The parameter (vlan) in requested url.
        type: str
        required: true
    fsp_vlan_interface:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            ac-name:
                type: str
                description: Deprecated, please rename it to ac_name. Ac name.
            aggregate:
                type: str
                description: Aggregate.
            algorithm:
                type: str
                description: Algorithm.
                choices:
                    - 'L2'
                    - 'L3'
                    - 'L4'
                    - 'LB'
                    - 'Source-MAC'
            alias:
                type: str
                description: Alias.
            allowaccess:
                type: list
                elements: str
                description: Allowaccess.
                choices:
                    - 'https'
                    - 'ping'
                    - 'ssh'
                    - 'snmp'
                    - 'http'
                    - 'telnet'
                    - 'fgfm'
                    - 'auto-ipsec'
                    - 'radius-acct'
                    - 'probe-response'
                    - 'capwap'
                    - 'dnp'
                    - 'ftm'
                    - 'fabric'
                    - 'speed-test'
            ap-discover:
                type: str
                description: Deprecated, please rename it to ap_discover. Ap discover.
                choices:
                    - 'disable'
                    - 'enable'
            arpforward:
                type: str
                description: Arpforward.
                choices:
                    - 'disable'
                    - 'enable'
            atm-protocol:
                type: str
                description: Deprecated, please rename it to atm_protocol. Atm protocol.
                choices:
                    - 'none'
                    - 'ipoa'
            auth-type:
                type: str
                description: Deprecated, please rename it to auth_type. Auth type.
                choices:
                    - 'auto'
                    - 'pap'
                    - 'chap'
                    - 'mschapv1'
                    - 'mschapv2'
            auto-auth-extension-device:
                type: str
                description: Deprecated, please rename it to auto_auth_extension_device. Auto auth extension device.
                choices:
                    - 'disable'
                    - 'enable'
            bfd:
                type: str
                description: Bfd.
                choices:
                    - 'global'
                    - 'enable'
                    - 'disable'
            bfd-desired-min-tx:
                type: int
                description: Deprecated, please rename it to bfd_desired_min_tx. Bfd desired min tx.
            bfd-detect-mult:
                type: int
                description: Deprecated, please rename it to bfd_detect_mult. Bfd detect mult.
            bfd-required-min-rx:
                type: int
                description: Deprecated, please rename it to bfd_required_min_rx. Bfd required min rx.
            broadcast-forticlient-discovery:
                type: str
                description: Deprecated, please rename it to broadcast_forticlient_discovery. Broadcast forticlient discovery.
                choices:
                    - 'disable'
                    - 'enable'
            broadcast-forward:
                type: str
                description: Deprecated, please rename it to broadcast_forward. Broadcast forward.
                choices:
                    - 'disable'
                    - 'enable'
            captive-portal:
                type: int
                description: Deprecated, please rename it to captive_portal. Captive portal.
            cli-conn-status:
                type: int
                description: Deprecated, please rename it to cli_conn_status. Cli conn status.
            color:
                type: int
                description: Color.
            ddns:
                type: str
                description: Ddns.
                choices:
                    - 'disable'
                    - 'enable'
            ddns-auth:
                type: str
                description: Deprecated, please rename it to ddns_auth. Ddns auth.
                choices:
                    - 'disable'
                    - 'tsig'
            ddns-domain:
                type: str
                description: Deprecated, please rename it to ddns_domain. Ddns domain.
            ddns-key:
                type: raw
                description: (list or str) Deprecated, please rename it to ddns_key. Ddns key.
            ddns-keyname:
                type: str
                description: Deprecated, please rename it to ddns_keyname. Ddns keyname.
            ddns-password:
                type: raw
                description: (list) Deprecated, please rename it to ddns_password. Ddns password.
            ddns-server:
                type: str
                description: Deprecated, please rename it to ddns_server. Ddns server.
                choices:
                    - 'dhs.org'
                    - 'dyndns.org'
                    - 'dyns.net'
                    - 'tzo.com'
                    - 'ods.org'
                    - 'vavic.com'
                    - 'now.net.cn'
                    - 'dipdns.net'
                    - 'easydns.com'
                    - 'genericDDNS'
            ddns-server-ip:
                type: str
                description: Deprecated, please rename it to ddns_server_ip. Ddns server ip.
            ddns-sn:
                type: str
                description: Deprecated, please rename it to ddns_sn. Ddns sn.
            ddns-ttl:
                type: int
                description: Deprecated, please rename it to ddns_ttl. Ddns ttl.
            ddns-username:
                type: str
                description: Deprecated, please rename it to ddns_username. Ddns username.
            ddns-zone:
                type: str
                description: Deprecated, please rename it to ddns_zone. Ddns zone.
            dedicated-to:
                type: str
                description: Deprecated, please rename it to dedicated_to. Dedicated to.
                choices:
                    - 'none'
                    - 'management'
            defaultgw:
                type: str
                description: Defaultgw.
                choices:
                    - 'disable'
                    - 'enable'
            description:
                type: str
                description: Description.
            detected-peer-mtu:
                type: int
                description: Deprecated, please rename it to detected_peer_mtu. Detected peer mtu.
            detectprotocol:
                type: list
                elements: str
                description: Detectprotocol.
                choices:
                    - 'ping'
                    - 'tcp-echo'
                    - 'udp-echo'
            detectserver:
                type: str
                description: Detectserver.
            device-access-list:
                type: raw
                description: (list or str) Deprecated, please rename it to device_access_list. Device access list.
            device-identification:
                type: str
                description: Deprecated, please rename it to device_identification. Device identification.
                choices:
                    - 'disable'
                    - 'enable'
            device-identification-active-scan:
                type: str
                description: Deprecated, please rename it to device_identification_active_scan. Device identification active scan.
                choices:
                    - 'disable'
                    - 'enable'
            device-netscan:
                type: str
                description: Deprecated, please rename it to device_netscan. Device netscan.
                choices:
                    - 'disable'
                    - 'enable'
            device-user-identification:
                type: str
                description: Deprecated, please rename it to device_user_identification. Device user identification.
                choices:
                    - 'disable'
                    - 'enable'
            devindex:
                type: int
                description: Devindex.
            dhcp-client-identifier:
                type: str
                description: Deprecated, please rename it to dhcp_client_identifier. Dhcp client identifier.
            dhcp-relay-agent-option:
                type: str
                description: Deprecated, please rename it to dhcp_relay_agent_option. Dhcp relay agent option.
                choices:
                    - 'disable'
                    - 'enable'
            dhcp-relay-ip:
                type: raw
                description: (list) Deprecated, please rename it to dhcp_relay_ip. Dhcp relay ip.
            dhcp-relay-service:
                type: str
                description: Deprecated, please rename it to dhcp_relay_service. Dhcp relay service.
                choices:
                    - 'disable'
                    - 'enable'
            dhcp-relay-type:
                type: str
                description: Deprecated, please rename it to dhcp_relay_type. Dhcp relay type.
                choices:
                    - 'regular'
                    - 'ipsec'
            dhcp-renew-time:
                type: int
                description: Deprecated, please rename it to dhcp_renew_time. Dhcp renew time.
            disc-retry-timeout:
                type: int
                description: Deprecated, please rename it to disc_retry_timeout. Disc retry timeout.
            disconnect-threshold:
                type: int
                description: Deprecated, please rename it to disconnect_threshold. Disconnect threshold.
            distance:
                type: int
                description: Distance.
            dns-query:
                type: str
                description: Deprecated, please rename it to dns_query. Dns query.
                choices:
                    - 'disable'
                    - 'recursive'
                    - 'non-recursive'
            dns-server-override:
                type: str
                description: Deprecated, please rename it to dns_server_override. Dns server override.
                choices:
                    - 'disable'
                    - 'enable'
            drop-fragment:
                type: str
                description: Deprecated, please rename it to drop_fragment. Drop fragment.
                choices:
                    - 'disable'
                    - 'enable'
            drop-overlapped-fragment:
                type: str
                description: Deprecated, please rename it to drop_overlapped_fragment. Drop overlapped fragment.
                choices:
                    - 'disable'
                    - 'enable'
            egress-cos:
                type: str
                description: Deprecated, please rename it to egress_cos. Egress cos.
                choices:
                    - 'disable'
                    - 'cos0'
                    - 'cos1'
                    - 'cos2'
                    - 'cos3'
                    - 'cos4'
                    - 'cos5'
                    - 'cos6'
                    - 'cos7'
            egress-shaping-profile:
                type: str
                description: Deprecated, please rename it to egress_shaping_profile. Egress shaping profile.
            endpoint-compliance:
                type: str
                description: Deprecated, please rename it to endpoint_compliance. Endpoint compliance.
                choices:
                    - 'disable'
                    - 'enable'
            estimated-downstream-bandwidth:
                type: int
                description: Deprecated, please rename it to estimated_downstream_bandwidth. Estimated downstream bandwidth.
            estimated-upstream-bandwidth:
                type: int
                description: Deprecated, please rename it to estimated_upstream_bandwidth. Estimated upstream bandwidth.
            explicit-ftp-proxy:
                type: str
                description: Deprecated, please rename it to explicit_ftp_proxy. Explicit ftp proxy.
                choices:
                    - 'disable'
                    - 'enable'
            explicit-web-proxy:
                type: str
                description: Deprecated, please rename it to explicit_web_proxy. Explicit web proxy.
                choices:
                    - 'disable'
                    - 'enable'
            external:
                type: str
                description: External.
                choices:
                    - 'disable'
                    - 'enable'
            fail-action-on-extender:
                type: str
                description: Deprecated, please rename it to fail_action_on_extender. Fail action on extender.
                choices:
                    - 'soft-restart'
                    - 'hard-restart'
                    - 'reboot'
            fail-alert-interfaces:
                type: raw
                description: (list or str) Deprecated, please rename it to fail_alert_interfaces. Fail alert interfaces.
            fail-alert-method:
                type: str
                description: Deprecated, please rename it to fail_alert_method. Fail alert method.
                choices:
                    - 'link-failed-signal'
                    - 'link-down'
            fail-detect:
                type: str
                description: Deprecated, please rename it to fail_detect. Fail detect.
                choices:
                    - 'disable'
                    - 'enable'
            fail-detect-option:
                type: list
                elements: str
                description: Deprecated, please rename it to fail_detect_option. Fail detect option.
                choices:
                    - 'detectserver'
                    - 'link-down'
            fdp:
                type: str
                description: Fdp.
                choices:
                    - 'disable'
                    - 'enable'
            fortiheartbeat:
                type: str
                description: Fortiheartbeat.
                choices:
                    - 'disable'
                    - 'enable'
            fortilink:
                type: str
                description: Fortilink.
                choices:
                    - 'disable'
                    - 'enable'
            fortilink-backup-link:
                type: int
                description: Deprecated, please rename it to fortilink_backup_link. Fortilink backup link.
            fortilink-split-interface:
                type: str
                description: Deprecated, please rename it to fortilink_split_interface. Fortilink split interface.
                choices:
                    - 'disable'
                    - 'enable'
            fortilink-stacking:
                type: str
                description: Deprecated, please rename it to fortilink_stacking. Fortilink stacking.
                choices:
                    - 'disable'
                    - 'enable'
            forward-domain:
                type: int
                description: Deprecated, please rename it to forward_domain. Forward domain.
            forward-error-correction:
                type: str
                description: Deprecated, please rename it to forward_error_correction. Forward error correction.
                choices:
                    - 'disable'
                    - 'enable'
                    - 'rs-fec'
                    - 'base-r-fec'
                    - 'fec-cl91'
                    - 'fec-cl74'
                    - 'rs-544'
                    - 'none'
                    - 'cl91-rs-fec'
                    - 'cl74-fc-fec'
                    - 'auto'
            fp-anomaly:
                type: list
                elements: str
                description: Deprecated, please rename it to fp_anomaly. Fp anomaly.
                choices:
                    - 'drop_tcp_fin_noack'
                    - 'pass_winnuke'
                    - 'pass_tcpland'
                    - 'pass_udpland'
                    - 'pass_icmpland'
                    - 'pass_ipland'
                    - 'pass_iprr'
                    - 'pass_ipssrr'
                    - 'pass_iplsrr'
                    - 'pass_ipstream'
                    - 'pass_ipsecurity'
                    - 'pass_iptimestamp'
                    - 'pass_ipunknown_option'
                    - 'pass_ipunknown_prot'
                    - 'pass_icmp_frag'
                    - 'pass_tcp_no_flag'
                    - 'pass_tcp_fin_noack'
                    - 'drop_winnuke'
                    - 'drop_tcpland'
                    - 'drop_udpland'
                    - 'drop_icmpland'
                    - 'drop_ipland'
                    - 'drop_iprr'
                    - 'drop_ipssrr'
                    - 'drop_iplsrr'
                    - 'drop_ipstream'
                    - 'drop_ipsecurity'
                    - 'drop_iptimestamp'
                    - 'drop_ipunknown_option'
                    - 'drop_ipunknown_prot'
                    - 'drop_icmp_frag'
                    - 'drop_tcp_no_flag'
            fp-disable:
                type: list
                elements: str
                description: Deprecated, please rename it to fp_disable. Fp disable.
                choices:
                    - 'all'
                    - 'ipsec'
                    - 'none'
            gateway-address:
                type: str
                description: Deprecated, please rename it to gateway_address. Gateway address.
            gi-gk:
                type: str
                description: Deprecated, please rename it to gi_gk. Gi gk.
                choices:
                    - 'disable'
                    - 'enable'
            gwaddr:
                type: str
                description: Gwaddr.
            gwdetect:
                type: str
                description: Gwdetect.
                choices:
                    - 'disable'
                    - 'enable'
            ha-priority:
                type: int
                description: Deprecated, please rename it to ha_priority. Ha priority.
            icmp-accept-redirect:
                type: str
                description: Deprecated, please rename it to icmp_accept_redirect. Icmp accept redirect.
                choices:
                    - 'disable'
                    - 'enable'
            icmp-redirect:
                type: str
                description: Deprecated, please rename it to icmp_redirect. Icmp redirect.
                choices:
                    - 'disable'
                    - 'enable'
            icmp-send-redirect:
                type: str
                description: Deprecated, please rename it to icmp_send_redirect. Icmp send redirect.
                choices:
                    - 'disable'
                    - 'enable'
            ident-accept:
                type: str
                description: Deprecated, please rename it to ident_accept. Ident accept.
                choices:
                    - 'disable'
                    - 'enable'
            idle-timeout:
                type: int
                description: Deprecated, please rename it to idle_timeout. Idle timeout.
            if-mdix:
                type: str
                description: Deprecated, please rename it to if_mdix. If mdix.
                choices:
                    - 'auto'
                    - 'normal'
                    - 'crossover'
            if-media:
                type: str
                description: Deprecated, please rename it to if_media. If media.
                choices:
                    - 'auto'
                    - 'copper'
                    - 'fiber'
            in-force-vlan-cos:
                type: int
                description: Deprecated, please rename it to in_force_vlan_cos. In force vlan cos.
            inbandwidth:
                type: int
                description: Inbandwidth.
            ingress-cos:
                type: str
                description: Deprecated, please rename it to ingress_cos. Ingress cos.
                choices:
                    - 'disable'
                    - 'cos0'
                    - 'cos1'
                    - 'cos2'
                    - 'cos3'
                    - 'cos4'
                    - 'cos5'
                    - 'cos6'
                    - 'cos7'
            ingress-spillover-threshold:
                type: int
                description: Deprecated, please rename it to ingress_spillover_threshold. Ingress spillover threshold.
            internal:
                type: int
                description: Internal.
            ip:
                type: str
                description: Ip.
            ipmac:
                type: str
                description: Ipmac.
                choices:
                    - 'disable'
                    - 'enable'
            ips-sniffer-mode:
                type: str
                description: Deprecated, please rename it to ips_sniffer_mode. Ips sniffer mode.
                choices:
                    - 'disable'
                    - 'enable'
            ipunnumbered:
                type: str
                description: Ipunnumbered.
            ipv6:
                type: dict
                description: Ipv6.
                suboptions:
                    autoconf:
                        type: str
                        description: Autoconf.
                        choices:
                            - 'disable'
                            - 'enable'
                    dhcp6-client-options:
                        type: list
                        elements: str
                        description: Deprecated, please rename it to dhcp6_client_options. Dhcp6 client options.
                        choices:
                            - 'rapid'
                            - 'iapd'
                            - 'iana'
                            - 'dns'
                            - 'dnsname'
                    dhcp6-information-request:
                        type: str
                        description: Deprecated, please rename it to dhcp6_information_request. Dhcp6 information request.
                        choices:
                            - 'disable'
                            - 'enable'
                    dhcp6-prefix-delegation:
                        type: str
                        description: Deprecated, please rename it to dhcp6_prefix_delegation. Dhcp6 prefix delegation.
                        choices:
                            - 'disable'
                            - 'enable'
                    dhcp6-prefix-hint:
                        type: str
                        description: Deprecated, please rename it to dhcp6_prefix_hint. Dhcp6 prefix hint.
                    dhcp6-prefix-hint-plt:
                        type: int
                        description: Deprecated, please rename it to dhcp6_prefix_hint_plt. Dhcp6 prefix hint plt.
                    dhcp6-prefix-hint-vlt:
                        type: int
                        description: Deprecated, please rename it to dhcp6_prefix_hint_vlt. Dhcp6 prefix hint vlt.
                    dhcp6-relay-ip:
                        type: str
                        description: Deprecated, please rename it to dhcp6_relay_ip. Dhcp6 relay ip.
                    dhcp6-relay-service:
                        type: str
                        description: Deprecated, please rename it to dhcp6_relay_service. Dhcp6 relay service.
                        choices:
                            - 'disable'
                            - 'enable'
                    dhcp6-relay-type:
                        type: str
                        description: Deprecated, please rename it to dhcp6_relay_type. Dhcp6 relay type.
                        choices:
                            - 'regular'
                    ip6-address:
                        type: str
                        description: Deprecated, please rename it to ip6_address. Ip6 address.
                    ip6-allowaccess:
                        type: list
                        elements: str
                        description: Deprecated, please rename it to ip6_allowaccess. Ip6 allowaccess.
                        choices:
                            - 'https'
                            - 'ping'
                            - 'ssh'
                            - 'snmp'
                            - 'http'
                            - 'telnet'
                            - 'fgfm'
                            - 'capwap'
                            - 'fabric'
                    ip6-default-life:
                        type: int
                        description: Deprecated, please rename it to ip6_default_life. Ip6 default life.
                    ip6-dns-server-override:
                        type: str
                        description: Deprecated, please rename it to ip6_dns_server_override. Ip6 dns server override.
                        choices:
                            - 'disable'
                            - 'enable'
                    ip6-hop-limit:
                        type: int
                        description: Deprecated, please rename it to ip6_hop_limit. Ip6 hop limit.
                    ip6-link-mtu:
                        type: int
                        description: Deprecated, please rename it to ip6_link_mtu. Ip6 link mtu.
                    ip6-manage-flag:
                        type: str
                        description: Deprecated, please rename it to ip6_manage_flag. Ip6 manage flag.
                        choices:
                            - 'disable'
                            - 'enable'
                    ip6-max-interval:
                        type: int
                        description: Deprecated, please rename it to ip6_max_interval. Ip6 max interval.
                    ip6-min-interval:
                        type: int
                        description: Deprecated, please rename it to ip6_min_interval. Ip6 min interval.
                    ip6-mode:
                        type: str
                        description: Deprecated, please rename it to ip6_mode. Ip6 mode.
                        choices:
                            - 'static'
                            - 'dhcp'
                            - 'pppoe'
                            - 'delegated'
                    ip6-other-flag:
                        type: str
                        description: Deprecated, please rename it to ip6_other_flag. Ip6 other flag.
                        choices:
                            - 'disable'
                            - 'enable'
                    ip6-reachable-time:
                        type: int
                        description: Deprecated, please rename it to ip6_reachable_time. Ip6 reachable time.
                    ip6-retrans-time:
                        type: int
                        description: Deprecated, please rename it to ip6_retrans_time. Ip6 retrans time.
                    ip6-send-adv:
                        type: str
                        description: Deprecated, please rename it to ip6_send_adv. Ip6 send adv.
                        choices:
                            - 'disable'
                            - 'enable'
                    ip6-subnet:
                        type: str
                        description: Deprecated, please rename it to ip6_subnet. Ip6 subnet.
                    ip6-upstream-interface:
                        type: str
                        description: Deprecated, please rename it to ip6_upstream_interface. Ip6 upstream interface.
                    nd-cert:
                        type: str
                        description: Deprecated, please rename it to nd_cert. Nd cert.
                    nd-cga-modifier:
                        type: str
                        description: Deprecated, please rename it to nd_cga_modifier. Nd cga modifier.
                    nd-mode:
                        type: str
                        description: Deprecated, please rename it to nd_mode. Nd mode.
                        choices:
                            - 'basic'
                            - 'SEND-compatible'
                    nd-security-level:
                        type: int
                        description: Deprecated, please rename it to nd_security_level. Nd security level.
                    nd-timestamp-delta:
                        type: int
                        description: Deprecated, please rename it to nd_timestamp_delta. Nd timestamp delta.
                    nd-timestamp-fuzz:
                        type: int
                        description: Deprecated, please rename it to nd_timestamp_fuzz. Nd timestamp fuzz.
                    vrip6_link_local:
                        type: str
                        description: Vrip6 link local.
                    vrrp-virtual-mac6:
                        type: str
                        description: Deprecated, please rename it to vrrp_virtual_mac6. Vrrp virtual mac6.
                        choices:
                            - 'disable'
                            - 'enable'
                    ip6-delegated-prefix-list:
                        type: list
                        elements: dict
                        description: Deprecated, please rename it to ip6_delegated_prefix_list. Ip6 delegated prefix list.
                        suboptions:
                            autonomous-flag:
                                type: str
                                description: Deprecated, please rename it to autonomous_flag. Autonomous flag.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            onlink-flag:
                                type: str
                                description: Deprecated, please rename it to onlink_flag. Onlink flag.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            prefix-id:
                                type: int
                                description: Deprecated, please rename it to prefix_id. Prefix id.
                            rdnss:
                                type: raw
                                description: (list) Rdnss.
                            rdnss-service:
                                type: str
                                description: Deprecated, please rename it to rdnss_service. Rdnss service.
                                choices:
                                    - 'delegated'
                                    - 'default'
                                    - 'specify'
                            subnet:
                                type: str
                                description: Subnet.
                            upstream-interface:
                                type: str
                                description: Deprecated, please rename it to upstream_interface. Upstream interface.
                            delegated-prefix-iaid:
                                type: int
                                description: Deprecated, please rename it to delegated_prefix_iaid. IAID of obtained delegated-prefix from the upstream...
                    ip6-extra-addr:
                        type: list
                        elements: dict
                        description: Deprecated, please rename it to ip6_extra_addr. Ip6 extra addr.
                        suboptions:
                            prefix:
                                type: str
                                description: Prefix.
                    ip6-prefix-list:
                        type: list
                        elements: dict
                        description: Deprecated, please rename it to ip6_prefix_list. Ip6 prefix list.
                        suboptions:
                            autonomous-flag:
                                type: str
                                description: Deprecated, please rename it to autonomous_flag. Autonomous flag.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            dnssl:
                                type: raw
                                description: (list) Dnssl.
                            onlink-flag:
                                type: str
                                description: Deprecated, please rename it to onlink_flag. Onlink flag.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            preferred-life-time:
                                type: int
                                description: Deprecated, please rename it to preferred_life_time. Preferred life time.
                            prefix:
                                type: str
                                description: Prefix.
                            rdnss:
                                type: raw
                                description: (list) Rdnss.
                            valid-life-time:
                                type: int
                                description: Deprecated, please rename it to valid_life_time. Valid life time.
                    vrrp6:
                        type: list
                        elements: dict
                        description: Vrrp6.
                        suboptions:
                            accept-mode:
                                type: str
                                description: Deprecated, please rename it to accept_mode. Accept mode.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            adv-interval:
                                type: int
                                description: Deprecated, please rename it to adv_interval. Adv interval.
                            preempt:
                                type: str
                                description: Preempt.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            priority:
                                type: int
                                description: Priority.
                            start-time:
                                type: int
                                description: Deprecated, please rename it to start_time. Start time.
                            status:
                                type: str
                                description: Status.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            vrdst6:
                                type: str
                                description: Vrdst6.
                            vrgrp:
                                type: int
                                description: Vrgrp.
                            vrid:
                                type: int
                                description: Vrid.
                            vrip6:
                                type: str
                                description: Vrip6.
                            ignore-default-route:
                                type: str
                                description: Deprecated, please rename it to ignore_default_route. Enable/disable ignoring of default route when checki...
                                choices:
                                    - 'disable'
                                    - 'enable'
                            vrdst-priority:
                                type: int
                                description: Deprecated, please rename it to vrdst_priority. Priority of the virtual router when the virtual router des...
                    interface-identifier:
                        type: str
                        description: Deprecated, please rename it to interface_identifier. Interface identifier.
                    unique-autoconf-addr:
                        type: str
                        description: Deprecated, please rename it to unique_autoconf_addr. Unique autoconf addr.
                        choices:
                            - 'disable'
                            - 'enable'
                    icmp6-send-redirect:
                        type: str
                        description: Deprecated, please rename it to icmp6_send_redirect. Enable/disable sending of ICMPv6 redirects.
                        choices:
                            - 'disable'
                            - 'enable'
                    cli-conn6-status:
                        type: int
                        description: Deprecated, please rename it to cli_conn6_status. Cli conn6 status.
                    ip6-prefix-mode:
                        type: str
                        description: Deprecated, please rename it to ip6_prefix_mode. Assigning a prefix from DHCP or RA.
                        choices:
                            - 'dhcp6'
                            - 'ra'
                    ra-send-mtu:
                        type: str
                        description: Deprecated, please rename it to ra_send_mtu. Enable/disable sending link MTU in RA packet.
                        choices:
                            - 'disable'
                            - 'enable'
                    ip6-delegated-prefix-iaid:
                        type: int
                        description: Deprecated, please rename it to ip6_delegated_prefix_iaid. IAID of obtained delegated-prefix from the upstream int...
                    dhcp6-relay-source-interface:
                        type: str
                        description: Deprecated, please rename it to dhcp6_relay_source_interface. Enable/disable use of address on this interface as t...
                        choices:
                            - 'disable'
                            - 'enable'
                    dhcp6-relay-interface-id:
                        type: str
                        description: Deprecated, please rename it to dhcp6_relay_interface_id. DHCP6 relay interface ID.
                    dhcp6-relay-source-ip:
                        type: str
                        description: Deprecated, please rename it to dhcp6_relay_source_ip. IPv6 address used by the DHCP6 relay as its source IP.
            l2forward:
                type: str
                description: L2forward.
                choices:
                    - 'disable'
                    - 'enable'
            l2tp-client:
                type: str
                description: Deprecated, please rename it to l2tp_client. L2tp client.
                choices:
                    - 'disable'
                    - 'enable'
            lacp-ha-slave:
                type: str
                description: Deprecated, please rename it to lacp_ha_slave. Lacp ha slave.
                choices:
                    - 'disable'
                    - 'enable'
            lacp-mode:
                type: str
                description: Deprecated, please rename it to lacp_mode. Lacp mode.
                choices:
                    - 'static'
                    - 'passive'
                    - 'active'
            lacp-speed:
                type: str
                description: Deprecated, please rename it to lacp_speed. Lacp speed.
                choices:
                    - 'slow'
                    - 'fast'
            lcp-echo-interval:
                type: int
                description: Deprecated, please rename it to lcp_echo_interval. Lcp echo interval.
            lcp-max-echo-fails:
                type: int
                description: Deprecated, please rename it to lcp_max_echo_fails. Lcp max echo fails.
            link-up-delay:
                type: int
                description: Deprecated, please rename it to link_up_delay. Link up delay.
            listen-forticlient-connection:
                type: str
                description: Deprecated, please rename it to listen_forticlient_connection. Listen forticlient connection.
                choices:
                    - 'disable'
                    - 'enable'
            lldp-network-policy:
                type: str
                description: Deprecated, please rename it to lldp_network_policy. Lldp network policy.
            lldp-reception:
                type: str
                description: Deprecated, please rename it to lldp_reception. Lldp reception.
                choices:
                    - 'disable'
                    - 'enable'
                    - 'vdom'
            lldp-transmission:
                type: str
                description: Deprecated, please rename it to lldp_transmission. Lldp transmission.
                choices:
                    - 'enable'
                    - 'disable'
                    - 'vdom'
            log:
                type: str
                description: Log.
                choices:
                    - 'disable'
                    - 'enable'
            macaddr:
                type: str
                description: Macaddr.
            management-ip:
                type: str
                description: Deprecated, please rename it to management_ip. Management ip.
            max-egress-burst-rate:
                type: int
                description: Deprecated, please rename it to max_egress_burst_rate. Max egress burst rate.
            max-egress-rate:
                type: int
                description: Deprecated, please rename it to max_egress_rate. Max egress rate.
            mediatype:
                type: str
                description: Mediatype.
                choices:
                    - 'serdes-sfp'
                    - 'sgmii-sfp'
                    - 'cfp2-sr10'
                    - 'cfp2-lr4'
                    - 'serdes-copper-sfp'
                    - 'sr'
                    - 'cr'
                    - 'lr'
                    - 'qsfp28-sr4'
                    - 'qsfp28-lr4'
                    - 'qsfp28-cr4'
                    - 'sr4'
                    - 'cr4'
                    - 'lr4'
                    - 'none'
                    - 'gmii'
                    - 'sgmii'
                    - 'sr2'
                    - 'lr2'
                    - 'cr2'
                    - 'sr8'
                    - 'lr8'
                    - 'cr8'
            member:
                type: raw
                description: (list or str) Member.
            min-links:
                type: int
                description: Deprecated, please rename it to min_links. Min links.
            min-links-down:
                type: str
                description: Deprecated, please rename it to min_links_down. Min links down.
                choices:
                    - 'operational'
                    - 'administrative'
            mode:
                type: str
                description: Mode.
                choices:
                    - 'static'
                    - 'dhcp'
                    - 'pppoe'
                    - 'pppoa'
                    - 'ipoa'
                    - 'eoa'
            mtu:
                type: int
                description: Mtu.
            mtu-override:
                type: str
                description: Deprecated, please rename it to mtu_override. Mtu override.
                choices:
                    - 'disable'
                    - 'enable'
            mux-type:
                type: str
                description: Deprecated, please rename it to mux_type. Mux type.
                choices:
                    - 'llc-encaps'
                    - 'vc-encaps'
            name:
                type: str
                description: Name.
            ndiscforward:
                type: str
                description: Ndiscforward.
                choices:
                    - 'disable'
                    - 'enable'
            netbios-forward:
                type: str
                description: Deprecated, please rename it to netbios_forward. Netbios forward.
                choices:
                    - 'disable'
                    - 'enable'
            netflow-sampler:
                type: str
                description: Deprecated, please rename it to netflow_sampler. Netflow sampler.
                choices:
                    - 'disable'
                    - 'tx'
                    - 'rx'
                    - 'both'
            npu-fastpath:
                type: str
                description: Deprecated, please rename it to npu_fastpath. Npu fastpath.
                choices:
                    - 'disable'
                    - 'enable'
            nst:
                type: str
                description: Nst.
                choices:
                    - 'disable'
                    - 'enable'
            out-force-vlan-cos:
                type: int
                description: Deprecated, please rename it to out_force_vlan_cos. Out force vlan cos.
            outbandwidth:
                type: int
                description: Outbandwidth.
            padt-retry-timeout:
                type: int
                description: Deprecated, please rename it to padt_retry_timeout. Padt retry timeout.
            password:
                type: raw
                description: (list) Password.
            peer-interface:
                type: raw
                description: (list or str) Deprecated, please rename it to peer_interface. Peer interface.
            phy-mode:
                type: str
                description: Deprecated, please rename it to phy_mode. Phy mode.
                choices:
                    - 'auto'
                    - 'adsl'
                    - 'vdsl'
                    - 'adsl-auto'
                    - 'vdsl2'
                    - 'adsl2+'
                    - 'adsl2'
                    - 'g.dmt'
                    - 't1.413'
                    - 'g.lite'
                    - 'g-dmt'
                    - 't1-413'
                    - 'g-lite'
            ping-serv-status:
                type: int
                description: Deprecated, please rename it to ping_serv_status. Ping serv status.
            poe:
                type: str
                description: Poe.
                choices:
                    - 'disable'
                    - 'enable'
            polling-interval:
                type: int
                description: Deprecated, please rename it to polling_interval. Polling interval.
            pppoe-unnumbered-negotiate:
                type: str
                description: Deprecated, please rename it to pppoe_unnumbered_negotiate. Pppoe unnumbered negotiate.
                choices:
                    - 'disable'
                    - 'enable'
            pptp-auth-type:
                type: str
                description: Deprecated, please rename it to pptp_auth_type. Pptp auth type.
                choices:
                    - 'auto'
                    - 'pap'
                    - 'chap'
                    - 'mschapv1'
                    - 'mschapv2'
            pptp-client:
                type: str
                description: Deprecated, please rename it to pptp_client. Pptp client.
                choices:
                    - 'disable'
                    - 'enable'
            pptp-password:
                type: raw
                description: (list) Deprecated, please rename it to pptp_password. Pptp password.
            pptp-server-ip:
                type: str
                description: Deprecated, please rename it to pptp_server_ip. Pptp server ip.
            pptp-timeout:
                type: int
                description: Deprecated, please rename it to pptp_timeout. Pptp timeout.
            pptp-user:
                type: str
                description: Deprecated, please rename it to pptp_user. Pptp user.
            preserve-session-route:
                type: str
                description: Deprecated, please rename it to preserve_session_route. Preserve session route.
                choices:
                    - 'disable'
                    - 'enable'
            priority:
                type: int
                description: Priority.
            priority-override:
                type: str
                description: Deprecated, please rename it to priority_override. Priority override.
                choices:
                    - 'disable'
                    - 'enable'
            proxy-captive-portal:
                type: str
                description: Deprecated, please rename it to proxy_captive_portal. Proxy captive portal.
                choices:
                    - 'disable'
                    - 'enable'
            redundant-interface:
                type: str
                description: Deprecated, please rename it to redundant_interface. Redundant interface.
            remote-ip:
                type: str
                description: Deprecated, please rename it to remote_ip. Remote ip.
            replacemsg-override-group:
                type: str
                description: Deprecated, please rename it to replacemsg_override_group. Replacemsg override group.
            retransmission:
                type: str
                description: Retransmission.
                choices:
                    - 'disable'
                    - 'enable'
            role:
                type: str
                description: Role.
                choices:
                    - 'lan'
                    - 'wan'
                    - 'dmz'
                    - 'undefined'
            sample-direction:
                type: str
                description: Deprecated, please rename it to sample_direction. Sample direction.
                choices:
                    - 'rx'
                    - 'tx'
                    - 'both'
            sample-rate:
                type: int
                description: Deprecated, please rename it to sample_rate. Sample rate.
            scan-botnet-connections:
                type: str
                description: Deprecated, please rename it to scan_botnet_connections. Scan botnet connections.
                choices:
                    - 'disable'
                    - 'block'
                    - 'monitor'
            secondary-IP:
                type: str
                description: Deprecated, please rename it to secondary_IP. Secondary IP.
                choices:
                    - 'disable'
                    - 'enable'
            secondaryip:
                type: list
                elements: dict
                description: Secondaryip.
                suboptions:
                    allowaccess:
                        type: list
                        elements: str
                        description: Allowaccess.
                        choices:
                            - 'https'
                            - 'ping'
                            - 'ssh'
                            - 'snmp'
                            - 'http'
                            - 'telnet'
                            - 'fgfm'
                            - 'auto-ipsec'
                            - 'radius-acct'
                            - 'probe-response'
                            - 'capwap'
                            - 'dnp'
                            - 'ftm'
                            - 'fabric'
                            - 'speed-test'
                            - 'icond'
                            - 'scim'
                    detectprotocol:
                        type: list
                        elements: str
                        description: Detectprotocol.
                        choices:
                            - 'ping'
                            - 'tcp-echo'
                            - 'udp-echo'
                    detectserver:
                        type: str
                        description: Detectserver.
                    gwdetect:
                        type: str
                        description: Gwdetect.
                        choices:
                            - 'disable'
                            - 'enable'
                    ha-priority:
                        type: int
                        description: Deprecated, please rename it to ha_priority. Ha priority.
                    id:
                        type: int
                        description: Id.
                    ip:
                        type: str
                        description: Ip.
                    ping-serv-status:
                        type: int
                        description: Deprecated, please rename it to ping_serv_status. Ping serv status.
                    seq:
                        type: int
                        description: Seq.
                    secip-relay-ip:
                        type: str
                        description: Deprecated, please rename it to secip_relay_ip. DHCP relay IP address.
            security-8021x-dynamic-vlan-id:
                type: int
                description: Deprecated, please rename it to security_8021x_dynamic_vlan_id. Security 8021x dynamic vlan id.
            security-8021x-master:
                type: str
                description: Deprecated, please rename it to security_8021x_master. Security 8021x master.
            security-8021x-mode:
                type: str
                description: Deprecated, please rename it to security_8021x_mode. Security 8021x mode.
                choices:
                    - 'default'
                    - 'dynamic-vlan'
                    - 'fallback'
                    - 'slave'
            security-exempt-list:
                type: str
                description: Deprecated, please rename it to security_exempt_list. Security exempt list.
            security-external-logout:
                type: str
                description: Deprecated, please rename it to security_external_logout. Security external logout.
            security-external-web:
                type: str
                description: Deprecated, please rename it to security_external_web. Security external web.
            security-groups:
                type: raw
                description: (list or str) Deprecated, please rename it to security_groups. Security groups.
            security-mac-auth-bypass:
                type: str
                description: Deprecated, please rename it to security_mac_auth_bypass. Security mac auth bypass.
                choices:
                    - 'disable'
                    - 'enable'
                    - 'mac-auth-only'
            security-mode:
                type: str
                description: Deprecated, please rename it to security_mode. Security mode.
                choices:
                    - 'none'
                    - 'captive-portal'
                    - '802.1X'
            security-redirect-url:
                type: str
                description: Deprecated, please rename it to security_redirect_url. Security redirect url.
            service-name:
                type: str
                description: Deprecated, please rename it to service_name. Service name.
            sflow-sampler:
                type: str
                description: Deprecated, please rename it to sflow_sampler. Sflow sampler.
                choices:
                    - 'disable'
                    - 'enable'
            speed:
                type: str
                description: Speed.
                choices:
                    - 'auto'
                    - '10full'
                    - '10half'
                    - '100full'
                    - '100half'
                    - '1000full'
                    - '1000half'
                    - '10000full'
                    - '1000auto'
                    - '10000auto'
                    - '40000full'
                    - '100Gfull'
                    - '25000full'
                    - '40000auto'
                    - '25000auto'
                    - '100Gauto'
                    - '400Gfull'
                    - '400Gauto'
                    - '50000full'
                    - '2500auto'
                    - '5000auto'
                    - '50000auto'
                    - '200Gfull'
                    - '200Gauto'
                    - '100auto'
            spillover-threshold:
                type: int
                description: Deprecated, please rename it to spillover_threshold. Spillover threshold.
            src-check:
                type: str
                description: Deprecated, please rename it to src_check. Src check.
                choices:
                    - 'disable'
                    - 'enable'
            status:
                type: str
                description: Status.
                choices:
                    - 'down'
                    - 'up'
            stp:
                type: str
                description: Stp.
                choices:
                    - 'disable'
                    - 'enable'
            stp-ha-slave:
                type: str
                description: Deprecated, please rename it to stp_ha_slave. Stp ha slave.
                choices:
                    - 'disable'
                    - 'enable'
                    - 'priority-adjust'
            stpforward:
                type: str
                description: Stpforward.
                choices:
                    - 'disable'
                    - 'enable'
            stpforward-mode:
                type: str
                description: Deprecated, please rename it to stpforward_mode. Stpforward mode.
                choices:
                    - 'rpl-all-ext-id'
                    - 'rpl-bridge-ext-id'
                    - 'rpl-nothing'
            strip-priority-vlan-tag:
                type: str
                description: Deprecated, please rename it to strip_priority_vlan_tag. Strip priority vlan tag.
                choices:
                    - 'disable'
                    - 'enable'
            subst:
                type: str
                description: Subst.
                choices:
                    - 'disable'
                    - 'enable'
            substitute-dst-mac:
                type: str
                description: Deprecated, please rename it to substitute_dst_mac. Substitute dst mac.
            switch:
                type: str
                description: Switch.
            switch-controller-access-vlan:
                type: str
                description: Deprecated, please rename it to switch_controller_access_vlan. Switch controller access vlan.
                choices:
                    - 'disable'
                    - 'enable'
            switch-controller-arp-inspection:
                type: str
                description: Deprecated, please rename it to switch_controller_arp_inspection. Switch controller arp inspection.
                choices:
                    - 'disable'
                    - 'enable'
                    - 'monitor'
            switch-controller-auth:
                type: str
                description: Deprecated, please rename it to switch_controller_auth. Switch controller auth.
                choices:
                    - 'radius'
                    - 'usergroup'
            switch-controller-dhcp-snooping:
                type: str
                description: Deprecated, please rename it to switch_controller_dhcp_snooping. Switch controller dhcp snooping.
                choices:
                    - 'disable'
                    - 'enable'
            switch-controller-dhcp-snooping-option82:
                type: str
                description: Deprecated, please rename it to switch_controller_dhcp_snooping_option82. Switch controller dhcp snooping option82.
                choices:
                    - 'disable'
                    - 'enable'
            switch-controller-dhcp-snooping-verify-mac:
                type: str
                description: Deprecated, please rename it to switch_controller_dhcp_snooping_verify_mac. Switch controller dhcp snooping verify mac.
                choices:
                    - 'disable'
                    - 'enable'
            switch-controller-igmp-snooping:
                type: str
                description: Deprecated, please rename it to switch_controller_igmp_snooping. Switch controller igmp snooping.
                choices:
                    - 'disable'
                    - 'enable'
            switch-controller-learning-limit:
                type: int
                description: Deprecated, please rename it to switch_controller_learning_limit. Switch controller learning limit.
            switch-controller-radius-server:
                type: str
                description: Deprecated, please rename it to switch_controller_radius_server. Switch controller radius server.
            switch-controller-traffic-policy:
                type: str
                description: Deprecated, please rename it to switch_controller_traffic_policy. Switch controller traffic policy.
            tc-mode:
                type: str
                description: Deprecated, please rename it to tc_mode. Tc mode.
                choices:
                    - 'ptm'
                    - 'atm'
            tcp-mss:
                type: int
                description: Deprecated, please rename it to tcp_mss. Tcp mss.
            trunk:
                type: str
                description: Trunk.
                choices:
                    - 'disable'
                    - 'enable'
            trust-ip-1:
                type: str
                description: Deprecated, please rename it to trust_ip_1. Trust ip 1.
            trust-ip-2:
                type: str
                description: Deprecated, please rename it to trust_ip_2. Trust ip 2.
            trust-ip-3:
                type: str
                description: Deprecated, please rename it to trust_ip_3. Trust ip 3.
            trust-ip6-1:
                type: str
                description: Deprecated, please rename it to trust_ip6_1. Trust ip6 1.
            trust-ip6-2:
                type: str
                description: Deprecated, please rename it to trust_ip6_2. Trust ip6 2.
            trust-ip6-3:
                type: str
                description: Deprecated, please rename it to trust_ip6_3. Trust ip6 3.
            type:
                type: str
                description: Type.
                choices:
                    - 'physical'
                    - 'vlan'
                    - 'aggregate'
                    - 'redundant'
                    - 'tunnel'
                    - 'wireless'
                    - 'vdom-link'
                    - 'loopback'
                    - 'switch'
                    - 'hard-switch'
                    - 'hdlc'
                    - 'vap-switch'
                    - 'wl-mesh'
                    - 'fortilink'
                    - 'switch-vlan'
                    - 'fctrl-trunk'
                    - 'tdm'
                    - 'fext-wan'
                    - 'vxlan'
                    - 'emac-vlan'
                    - 'geneve'
                    - 'ssl'
                    - 'lan-extension'
            username:
                type: str
                description: Username.
            vci:
                type: int
                description: Vci.
            vectoring:
                type: str
                description: Vectoring.
                choices:
                    - 'disable'
                    - 'enable'
            vindex:
                type: int
                description: Vindex.
            vlanforward:
                type: str
                description: Vlanforward.
                choices:
                    - 'disable'
                    - 'enable'
            vlanid:
                type: int
                description: Vlanid.
            vpi:
                type: int
                description: Vpi.
            vrf:
                type: int
                description: Vrf.
            vrrp:
                type: list
                elements: dict
                description: Vrrp.
                suboptions:
                    accept-mode:
                        type: str
                        description: Deprecated, please rename it to accept_mode. Accept mode.
                        choices:
                            - 'disable'
                            - 'enable'
                    adv-interval:
                        type: int
                        description: Deprecated, please rename it to adv_interval. Adv interval.
                    ignore-default-route:
                        type: str
                        description: Deprecated, please rename it to ignore_default_route. Ignore default route.
                        choices:
                            - 'disable'
                            - 'enable'
                    preempt:
                        type: str
                        description: Preempt.
                        choices:
                            - 'disable'
                            - 'enable'
                    priority:
                        type: int
                        description: Priority.
                    start-time:
                        type: int
                        description: Deprecated, please rename it to start_time. Start time.
                    status:
                        type: str
                        description: Status.
                        choices:
                            - 'disable'
                            - 'enable'
                    version:
                        type: str
                        description: Version.
                        choices:
                            - '2'
                            - '3'
                    vrdst:
                        type: raw
                        description: (list) Vrdst.
                    vrdst-priority:
                        type: int
                        description: Deprecated, please rename it to vrdst_priority. Vrdst priority.
                    vrgrp:
                        type: int
                        description: Vrgrp.
                    vrid:
                        type: int
                        description: Vrid.
                    vrip:
                        type: str
                        description: Vrip.
                    proxy-arp:
                        type: list
                        elements: dict
                        description: Deprecated, please rename it to proxy_arp. Proxy arp.
                        suboptions:
                            id:
                                type: int
                                description: ID.
                            ip:
                                type: str
                                description: Set IP addresses of proxy ARP.
            vrrp-virtual-mac:
                type: str
                description: Deprecated, please rename it to vrrp_virtual_mac. Vrrp virtual mac.
                choices:
                    - 'disable'
                    - 'enable'
            wccp:
                type: str
                description: Wccp.
                choices:
                    - 'disable'
                    - 'enable'
            weight:
                type: int
                description: Weight.
            wifi-5g-threshold:
                type: str
                description: Deprecated, please rename it to wifi_5g_threshold. Wifi 5g threshold.
            wifi-acl:
                type: str
                description: Deprecated, please rename it to wifi_acl. Wifi acl.
                choices:
                    - 'deny'
                    - 'allow'
            wifi-ap-band:
                type: str
                description: Deprecated, please rename it to wifi_ap_band. Wifi ap band.
                choices:
                    - 'any'
                    - '5g-preferred'
                    - '5g-only'
            wifi-auth:
                type: str
                description: Deprecated, please rename it to wifi_auth. Wifi auth.
                choices:
                    - 'PSK'
                    - 'RADIUS'
                    - 'radius'
                    - 'usergroup'
            wifi-auto-connect:
                type: str
                description: Deprecated, please rename it to wifi_auto_connect. Wifi auto connect.
                choices:
                    - 'disable'
                    - 'enable'
            wifi-auto-save:
                type: str
                description: Deprecated, please rename it to wifi_auto_save. Wifi auto save.
                choices:
                    - 'disable'
                    - 'enable'
            wifi-broadcast-ssid:
                type: str
                description: Deprecated, please rename it to wifi_broadcast_ssid. Wifi broadcast ssid.
                choices:
                    - 'disable'
                    - 'enable'
            wifi-encrypt:
                type: str
                description: Deprecated, please rename it to wifi_encrypt. Wifi encrypt.
                choices:
                    - 'TKIP'
                    - 'AES'
            wifi-fragment-threshold:
                type: int
                description: Deprecated, please rename it to wifi_fragment_threshold. Wifi fragment threshold.
            wifi-key:
                type: raw
                description: (list) Deprecated, please rename it to wifi_key. Wifi key.
            wifi-keyindex:
                type: int
                description: Deprecated, please rename it to wifi_keyindex. Wifi keyindex.
            wifi-mac-filter:
                type: str
                description: Deprecated, please rename it to wifi_mac_filter. Wifi mac filter.
                choices:
                    - 'disable'
                    - 'enable'
            wifi-passphrase:
                type: raw
                description: (list) Deprecated, please rename it to wifi_passphrase. Wifi passphrase.
            wifi-radius-server:
                type: str
                description: Deprecated, please rename it to wifi_radius_server. Wifi radius server.
            wifi-rts-threshold:
                type: int
                description: Deprecated, please rename it to wifi_rts_threshold. Wifi rts threshold.
            wifi-security:
                type: str
                description: Deprecated, please rename it to wifi_security. Wifi security.
                choices:
                    - 'None'
                    - 'WEP64'
                    - 'wep64'
                    - 'WEP128'
                    - 'wep128'
                    - 'WPA_PSK'
                    - 'WPA_RADIUS'
                    - 'WPA'
                    - 'WPA2'
                    - 'WPA2_AUTO'
                    - 'open'
                    - 'wpa-personal'
                    - 'wpa-enterprise'
                    - 'wpa-only-personal'
                    - 'wpa-only-enterprise'
                    - 'wpa2-only-personal'
                    - 'wpa2-only-enterprise'
            wifi-ssid:
                type: str
                description: Deprecated, please rename it to wifi_ssid. Wifi ssid.
            wifi-usergroup:
                type: str
                description: Deprecated, please rename it to wifi_usergroup. Wifi usergroup.
            wins-ip:
                type: str
                description: Deprecated, please rename it to wins_ip. Wins ip.
            eip:
                type: str
                description: Eip.
            fortilink-neighbor-detect:
                type: str
                description: Deprecated, please rename it to fortilink_neighbor_detect. Fortilink neighbor detect.
                choices:
                    - 'lldp'
                    - 'fortilink'
            ingress-shaping-profile:
                type: str
                description: Deprecated, please rename it to ingress_shaping_profile. Ingress shaping profile.
            ring-rx:
                type: int
                description: Deprecated, please rename it to ring_rx. Ring rx.
            ring-tx:
                type: int
                description: Deprecated, please rename it to ring_tx. Ring tx.
            switch-controller-igmp-snooping-fast-leave:
                type: str
                description: Deprecated, please rename it to switch_controller_igmp_snooping_fast_leave. Switch controller igmp snooping fast leave.
                choices:
                    - 'disable'
                    - 'enable'
            switch-controller-igmp-snooping-proxy:
                type: str
                description: Deprecated, please rename it to switch_controller_igmp_snooping_proxy. Switch controller igmp snooping proxy.
                choices:
                    - 'disable'
                    - 'enable'
            switch-controller-rspan-mode:
                type: str
                description: Deprecated, please rename it to switch_controller_rspan_mode. Switch controller rspan mode.
                choices:
                    - 'disable'
                    - 'enable'
            bandwidth-measure-time:
                type: int
                description: Deprecated, please rename it to bandwidth_measure_time. Bandwidth measure time.
            ip-managed-by-fortiipam:
                type: str
                description: Deprecated, please rename it to ip_managed_by_fortiipam. Ip managed by fortiipam.
                choices:
                    - 'disable'
                    - 'enable'
                    - 'inherit-global'
            managed-subnetwork-size:
                type: str
                description: Deprecated, please rename it to managed_subnetwork_size. Managed subnetwork size.
                choices:
                    - '256'
                    - '512'
                    - '1024'
                    - '2048'
                    - '4096'
                    - '8192'
                    - '16384'
                    - '32768'
                    - '65536'
                    - '32'
                    - '64'
                    - '128'
            measured-downstream-bandwidth:
                type: int
                description: Deprecated, please rename it to measured_downstream_bandwidth. Measured downstream bandwidth.
            measured-upstream-bandwidth:
                type: int
                description: Deprecated, please rename it to measured_upstream_bandwidth. Measured upstream bandwidth.
            monitor-bandwidth:
                type: str
                description: Deprecated, please rename it to monitor_bandwidth. Monitor bandwidth.
                choices:
                    - 'disable'
                    - 'enable'
            swc-vlan:
                type: int
                description: Deprecated, please rename it to swc_vlan. Swc vlan.
            switch-controller-feature:
                type: str
                description: Deprecated, please rename it to switch_controller_feature. Switch controller feature.
                choices:
                    - 'none'
                    - 'default-vlan'
                    - 'quarantine'
                    - 'sniffer'
                    - 'voice'
                    - 'camera'
                    - 'rspan'
                    - 'video'
                    - 'nac'
                    - 'nac-segment'
            switch-controller-mgmt-vlan:
                type: int
                description: Deprecated, please rename it to switch_controller_mgmt_vlan. Switch controller mgmt vlan.
            switch-controller-nac:
                type: str
                description: Deprecated, please rename it to switch_controller_nac. Switch controller nac.
            vlan-protocol:
                type: str
                description: Deprecated, please rename it to vlan_protocol. Vlan protocol.
                choices:
                    - '8021q'
                    - '8021ad'
            dhcp-relay-interface:
                type: str
                description: Deprecated, please rename it to dhcp_relay_interface. Dhcp relay interface.
            dhcp-relay-interface-select-method:
                type: str
                description: Deprecated, please rename it to dhcp_relay_interface_select_method. Dhcp relay interface select method.
                choices:
                    - 'auto'
                    - 'sdwan'
                    - 'specify'
            np-qos-profile:
                type: int
                description: Deprecated, please rename it to np_qos_profile. NP QoS profile ID.
            swc-first-create:
                type: int
                description: Deprecated, please rename it to swc_first_create. Initial create for switch-controller VLANs.
            switch-controller-iot-scanning:
                type: str
                description: Deprecated, please rename it to switch_controller_iot_scanning. Enable/disable managed FortiSwitch IoT scanning.
                choices:
                    - 'disable'
                    - 'enable'
            switch-controller-source-ip:
                type: str
                description: Deprecated, please rename it to switch_controller_source_ip. Source IP address used in FortiLink over L3 connections.
                choices:
                    - 'outbound'
                    - 'fixed'
            dhcp-relay-request-all-server:
                type: str
                description: Deprecated, please rename it to dhcp_relay_request_all_server. Enable/disable sending of DHCP requests to all servers.
                choices:
                    - 'disable'
                    - 'enable'
            stp-ha-secondary:
                type: str
                description: Deprecated, please rename it to stp_ha_secondary. Control STP behaviour on HA secondary.
                choices:
                    - 'disable'
                    - 'enable'
                    - 'priority-adjust'
            switch-controller-dynamic:
                type: str
                description: Deprecated, please rename it to switch_controller_dynamic. Integrated FortiLink settings for managed FortiSwitch.
            auth-cert:
                type: str
                description: Deprecated, please rename it to auth_cert. HTTPS server certificate.
            auth-portal-addr:
                type: str
                description: Deprecated, please rename it to auth_portal_addr. Address of captive portal.
            dhcp-classless-route-addition:
                type: str
                description: Deprecated, please rename it to dhcp_classless_route_addition. Enable/disable addition of classless static routes retrieve...
                choices:
                    - 'disable'
                    - 'enable'
            dhcp-relay-link-selection:
                type: str
                description: Deprecated, please rename it to dhcp_relay_link_selection. DHCP relay link selection.
            dns-server-protocol:
                type: list
                elements: str
                description: Deprecated, please rename it to dns_server_protocol. DNS transport protocols.
                choices:
                    - 'cleartext'
                    - 'dot'
                    - 'doh'
            eap-ca-cert:
                type: str
                description: Deprecated, please rename it to eap_ca_cert. EAP CA certificate name.
            eap-identity:
                type: str
                description: Deprecated, please rename it to eap_identity. EAP identity.
            eap-method:
                type: str
                description: Deprecated, please rename it to eap_method. EAP method.
                choices:
                    - 'tls'
                    - 'peap'
            eap-password:
                type: raw
                description: (list) Deprecated, please rename it to eap_password. EAP password.
            eap-supplicant:
                type: str
                description: Deprecated, please rename it to eap_supplicant. Enable/disable EAP-Supplicant.
                choices:
                    - 'disable'
                    - 'enable'
            eap-user-cert:
                type: str
                description: Deprecated, please rename it to eap_user_cert. EAP user certificate name.
            ike-saml-server:
                type: str
                description: Deprecated, please rename it to ike_saml_server. Configure IKE authentication SAML server.
            lacp-ha-secondary:
                type: str
                description: Deprecated, please rename it to lacp_ha_secondary. Lacp ha secondary.
                choices:
                    - 'disable'
                    - 'enable'
            pvc-atm-qos:
                type: str
                description: Deprecated, please rename it to pvc_atm_qos. SFP-DSL ADSL Fallback PVC ATM QoS.
                choices:
                    - 'cbr'
                    - 'rt-vbr'
                    - 'nrt-vbr'
                    - 'ubr'
            pvc-chan:
                type: int
                description: Deprecated, please rename it to pvc_chan. SFP-DSL ADSL Fallback PVC Channel.
            pvc-crc:
                type: int
                description: Deprecated, please rename it to pvc_crc. SFP-DSL ADSL Fallback PVC CRC Option
            pvc-pcr:
                type: int
                description: Deprecated, please rename it to pvc_pcr. SFP-DSL ADSL Fallback PVC Packet Cell Rate in cells
            pvc-scr:
                type: int
                description: Deprecated, please rename it to pvc_scr. SFP-DSL ADSL Fallback PVC Sustainable Cell Rate in cells
            pvc-vlan-id:
                type: int
                description: Deprecated, please rename it to pvc_vlan_id. SFP-DSL ADSL Fallback PVC VLAN ID.
            pvc-vlan-rx-id:
                type: int
                description: Deprecated, please rename it to pvc_vlan_rx_id. SFP-DSL ADSL Fallback PVC VLANID RX.
            pvc-vlan-rx-op:
                type: str
                description: Deprecated, please rename it to pvc_vlan_rx_op. SFP-DSL ADSL Fallback PVC VLAN RX op.
                choices:
                    - 'pass-through'
                    - 'replace'
                    - 'remove'
            pvc-vlan-tx-id:
                type: int
                description: Deprecated, please rename it to pvc_vlan_tx_id. SFP-DSL ADSL Fallback PVC VLAN ID TX.
            pvc-vlan-tx-op:
                type: str
                description: Deprecated, please rename it to pvc_vlan_tx_op. SFP-DSL ADSL Fallback PVC VLAN TX op.
                choices:
                    - 'pass-through'
                    - 'replace'
                    - 'remove'
            reachable-time:
                type: int
                description: Deprecated, please rename it to reachable_time. IPv4 reachable time in milliseconds
            select-profile-30a-35b:
                type: str
                description: Deprecated, please rename it to select_profile_30a_35b. Select VDSL Profile 30a or 35b.
                choices:
                    - '30A'
                    - '35B'
            sfp-dsl:
                type: str
                description: Deprecated, please rename it to sfp_dsl. Enable/disable SFP DSL.
                choices:
                    - 'disable'
                    - 'enable'
            sfp-dsl-adsl-fallback:
                type: str
                description: Deprecated, please rename it to sfp_dsl_adsl_fallback. Enable/disable SFP DSL ADSL fallback.
                choices:
                    - 'disable'
                    - 'enable'
            sfp-dsl-autodetect:
                type: str
                description: Deprecated, please rename it to sfp_dsl_autodetect. Enable/disable SFP DSL MAC address autodetect.
                choices:
                    - 'disable'
                    - 'enable'
            sfp-dsl-mac:
                type: str
                description: Deprecated, please rename it to sfp_dsl_mac. SFP DSL MAC address.
            sw-algorithm:
                type: str
                description: Deprecated, please rename it to sw_algorithm. Frame distribution algorithm for switch.
                choices:
                    - 'l2'
                    - 'l3'
                    - 'eh'
                    - 'default'
            system-id:
                type: str
                description: Deprecated, please rename it to system_id. Define a system ID for the aggregate interface.
            system-id-type:
                type: str
                description: Deprecated, please rename it to system_id_type. Method in which system ID is generated.
                choices:
                    - 'auto'
                    - 'user'
            vlan-id:
                type: int
                description: Deprecated, please rename it to vlan_id. Vlan ID
            vlan-op-mode:
                type: str
                description: Deprecated, please rename it to vlan_op_mode. Configure DSL 802.
                choices:
                    - 'tag'
                    - 'untag'
                    - 'passthrough'
            generic-receive-offload:
                type: str
                description: Deprecated, please rename it to generic_receive_offload. Generic receive offload.
                choices:
                    - 'disable'
                    - 'enable'
            interconnect-profile:
                type: str
                description: Deprecated, please rename it to interconnect_profile. Set interconnect profile.
                choices:
                    - 'default'
                    - 'profile1'
                    - 'profile2'
            large-receive-offload:
                type: str
                description: Deprecated, please rename it to large_receive_offload. Large receive offload.
                choices:
                    - 'disable'
                    - 'enable'
            annex:
                type: str
                description: Set xDSL annex type.
                choices:
                    - 'a'
                    - 'b'
                    - 'j'
                    - 'bjm'
                    - 'i'
                    - 'al'
                    - 'm'
                    - 'aijlm'
                    - 'bj'
            aggregate-type:
                type: str
                description: Deprecated, please rename it to aggregate_type. Type of aggregation.
                choices:
                    - 'physical'
                    - 'vxlan'
            switch-controller-netflow-collect:
                type: str
                description: Deprecated, please rename it to switch_controller_netflow_collect. NetFlow collection and processing.
                choices:
                    - 'disable'
                    - 'enable'
            wifi-dns-server1:
                type: str
                description: Deprecated, please rename it to wifi_dns_server1. DNS server 1.
            wifi-dns-server2:
                type: str
                description: Deprecated, please rename it to wifi_dns_server2. DNS server 2.
            wifi-gateway:
                type: str
                description: Deprecated, please rename it to wifi_gateway. IPv4 default gateway IP address.
            default-purdue-level:
                type: str
                description: Deprecated, please rename it to default_purdue_level. Default purdue level of device detected on this interface.
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
            dhcp-broadcast-flag:
                type: str
                description: Deprecated, please rename it to dhcp_broadcast_flag. Enable/disable setting of the broadcast flag in messages sent by the ...
                choices:
                    - 'disable'
                    - 'enable'
            dhcp-smart-relay:
                type: str
                description: Deprecated, please rename it to dhcp_smart_relay. Enable/disable DHCP smart relay.
                choices:
                    - 'disable'
                    - 'enable'
            switch-controller-offloading:
                type: str
                description: Deprecated, please rename it to switch_controller_offloading. Switch controller offloading.
                choices:
                    - 'disable'
                    - 'enable'
            switch-controller-offloading-gw:
                type: str
                description: Deprecated, please rename it to switch_controller_offloading_gw. Switch controller offloading gw.
                choices:
                    - 'disable'
                    - 'enable'
            switch-controller-offloading-ip:
                type: str
                description: Deprecated, please rename it to switch_controller_offloading_ip. Switch controller offloading ip.
            dhcp-relay-circuit-id:
                type: str
                description: Deprecated, please rename it to dhcp_relay_circuit_id. DHCP relay circuit ID.
            dhcp-relay-source-ip:
                type: str
                description: Deprecated, please rename it to dhcp_relay_source_ip. IP address used by the DHCP relay as its source IP.
            switch-controller-offload:
                type: str
                description: Deprecated, please rename it to switch_controller_offload. Enable/disable managed FortiSwitch routing offload.
                choices:
                    - 'disable'
                    - 'enable'
            switch-controller-offload-gw:
                type: str
                description: Deprecated, please rename it to switch_controller_offload_gw. Enable/disable managed FortiSwitch routing offload gateway.
                choices:
                    - 'disable'
                    - 'enable'
            switch-controller-offload-ip:
                type: str
                description: Deprecated, please rename it to switch_controller_offload_ip. IP for routing offload on FortiSwitch.
            mirroring-direction:
                type: str
                description: Deprecated, please rename it to mirroring_direction. Port mirroring direction.
                choices:
                    - 'rx'
                    - 'tx'
                    - 'both'
            mirroring-port:
                type: str
                description: Deprecated, please rename it to mirroring_port. Mirroring port.
            port-mirroring:
                type: str
                description: Deprecated, please rename it to port_mirroring. Enable/disable NP port mirroring.
                choices:
                    - 'disable'
                    - 'enable'
            security-8021x-member-mode:
                type: str
                description: Deprecated, please rename it to security_8021x_member_mode. '802.'
                choices:
                    - 'disable'
                    - 'switch'
            stp-edge:
                type: str
                description: Deprecated, please rename it to stp_edge. Enable/disable as STP edge port.
                choices:
                    - 'disable'
                    - 'enable'
            dhcp-relay-allow-no-end-option:
                type: str
                description: Deprecated, please rename it to dhcp_relay_allow_no_end_option. Enable/disable relaying DHCP messages with no end option.
                choices:
                    - 'disable'
                    - 'enable'
            netflow-sample-rate:
                type: int
                description: Deprecated, please rename it to netflow_sample_rate. NetFlow sample rate.
            netflow-sampler-id:
                type: int
                description: Deprecated, please rename it to netflow_sampler_id. Netflow sampler ID.
            pppoe-egress-cos:
                type: str
                description: Deprecated, please rename it to pppoe_egress_cos. CoS in VLAN tag for outgoing PPPoE/PPP packets.
                choices:
                    - 'cos0'
                    - 'cos1'
                    - 'cos2'
                    - 'cos3'
                    - 'cos4'
                    - 'cos5'
                    - 'cos6'
                    - 'cos7'
            security-ip-auth-bypass:
                type: str
                description: Deprecated, please rename it to security_ip_auth_bypass. Enable/disable IP authentication bypass.
                choices:
                    - 'disable'
                    - 'enable'
            virtual-mac:
                type: str
                description: Deprecated, please rename it to virtual_mac. Change the interfaces virtual MAC address.
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
    - name: Configure interfaces.
      fortinet.fortimanager.fmgr_fsp_vlan_interface:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        adom: <your own value>
        vlan: <your own value>
        fsp_vlan_interface:
          ac_name: <string>
          aggregate: <string>
          algorithm: <value in [L2, L3, L4, ...]>
          alias: <string>
          allowaccess:
            - https
            - ping
            - ssh
            - snmp
            - http
            - telnet
            - fgfm
            - auto-ipsec
            - radius-acct
            - probe-response
            - capwap
            - dnp
            - ftm
            - fabric
            - speed-test
          ap_discover: <value in [disable, enable]>
          arpforward: <value in [disable, enable]>
          atm_protocol: <value in [none, ipoa]>
          auth_type: <value in [auto, pap, chap, ...]>
          auto_auth_extension_device: <value in [disable, enable]>
          bfd: <value in [global, enable, disable]>
          bfd_desired_min_tx: <integer>
          bfd_detect_mult: <integer>
          bfd_required_min_rx: <integer>
          broadcast_forticlient_discovery: <value in [disable, enable]>
          broadcast_forward: <value in [disable, enable]>
          captive_portal: <integer>
          cli_conn_status: <integer>
          color: <integer>
          ddns: <value in [disable, enable]>
          ddns_auth: <value in [disable, tsig]>
          ddns_domain: <string>
          ddns_key: <list or string>
          ddns_keyname: <string>
          ddns_password: <list or string>
          ddns_server: <value in [dhs.org, dyndns.org, dyns.net, ...]>
          ddns_server_ip: <string>
          ddns_sn: <string>
          ddns_ttl: <integer>
          ddns_username: <string>
          ddns_zone: <string>
          dedicated_to: <value in [none, management]>
          defaultgw: <value in [disable, enable]>
          description: <string>
          detected_peer_mtu: <integer>
          detectprotocol:
            - ping
            - tcp-echo
            - udp-echo
          detectserver: <string>
          device_access_list: <list or string>
          device_identification: <value in [disable, enable]>
          device_identification_active_scan: <value in [disable, enable]>
          device_netscan: <value in [disable, enable]>
          device_user_identification: <value in [disable, enable]>
          devindex: <integer>
          dhcp_client_identifier: <string>
          dhcp_relay_agent_option: <value in [disable, enable]>
          dhcp_relay_ip: <list or string>
          dhcp_relay_service: <value in [disable, enable]>
          dhcp_relay_type: <value in [regular, ipsec]>
          dhcp_renew_time: <integer>
          disc_retry_timeout: <integer>
          disconnect_threshold: <integer>
          distance: <integer>
          dns_query: <value in [disable, recursive, non-recursive]>
          dns_server_override: <value in [disable, enable]>
          drop_fragment: <value in [disable, enable]>
          drop_overlapped_fragment: <value in [disable, enable]>
          egress_cos: <value in [disable, cos0, cos1, ...]>
          egress_shaping_profile: <string>
          endpoint_compliance: <value in [disable, enable]>
          estimated_downstream_bandwidth: <integer>
          estimated_upstream_bandwidth: <integer>
          explicit_ftp_proxy: <value in [disable, enable]>
          explicit_web_proxy: <value in [disable, enable]>
          external: <value in [disable, enable]>
          fail_action_on_extender: <value in [soft-restart, hard-restart, reboot]>
          fail_alert_interfaces: <list or string>
          fail_alert_method: <value in [link-failed-signal, link-down]>
          fail_detect: <value in [disable, enable]>
          fail_detect_option:
            - detectserver
            - link-down
          fdp: <value in [disable, enable]>
          fortiheartbeat: <value in [disable, enable]>
          fortilink: <value in [disable, enable]>
          fortilink_backup_link: <integer>
          fortilink_split_interface: <value in [disable, enable]>
          fortilink_stacking: <value in [disable, enable]>
          forward_domain: <integer>
          forward_error_correction: <value in [disable, enable, rs-fec, ...]>
          fp_anomaly:
            - drop_tcp_fin_noack
            - pass_winnuke
            - pass_tcpland
            - pass_udpland
            - pass_icmpland
            - pass_ipland
            - pass_iprr
            - pass_ipssrr
            - pass_iplsrr
            - pass_ipstream
            - pass_ipsecurity
            - pass_iptimestamp
            - pass_ipunknown_option
            - pass_ipunknown_prot
            - pass_icmp_frag
            - pass_tcp_no_flag
            - pass_tcp_fin_noack
            - drop_winnuke
            - drop_tcpland
            - drop_udpland
            - drop_icmpland
            - drop_ipland
            - drop_iprr
            - drop_ipssrr
            - drop_iplsrr
            - drop_ipstream
            - drop_ipsecurity
            - drop_iptimestamp
            - drop_ipunknown_option
            - drop_ipunknown_prot
            - drop_icmp_frag
            - drop_tcp_no_flag
          fp_disable:
            - all
            - ipsec
            - none
          gateway_address: <string>
          gi_gk: <value in [disable, enable]>
          gwaddr: <string>
          gwdetect: <value in [disable, enable]>
          ha_priority: <integer>
          icmp_accept_redirect: <value in [disable, enable]>
          icmp_redirect: <value in [disable, enable]>
          icmp_send_redirect: <value in [disable, enable]>
          ident_accept: <value in [disable, enable]>
          idle_timeout: <integer>
          if_mdix: <value in [auto, normal, crossover]>
          if_media: <value in [auto, copper, fiber]>
          in_force_vlan_cos: <integer>
          inbandwidth: <integer>
          ingress_cos: <value in [disable, cos0, cos1, ...]>
          ingress_spillover_threshold: <integer>
          internal: <integer>
          ip: <string>
          ipmac: <value in [disable, enable]>
          ips_sniffer_mode: <value in [disable, enable]>
          ipunnumbered: <string>
          ipv6:
            autoconf: <value in [disable, enable]>
            dhcp6_client_options:
              - rapid
              - iapd
              - iana
              - dns
              - dnsname
            dhcp6_information_request: <value in [disable, enable]>
            dhcp6_prefix_delegation: <value in [disable, enable]>
            dhcp6_prefix_hint: <string>
            dhcp6_prefix_hint_plt: <integer>
            dhcp6_prefix_hint_vlt: <integer>
            dhcp6_relay_ip: <string>
            dhcp6_relay_service: <value in [disable, enable]>
            dhcp6_relay_type: <value in [regular]>
            ip6_address: <string>
            ip6_allowaccess:
              - https
              - ping
              - ssh
              - snmp
              - http
              - telnet
              - fgfm
              - capwap
              - fabric
            ip6_default_life: <integer>
            ip6_dns_server_override: <value in [disable, enable]>
            ip6_hop_limit: <integer>
            ip6_link_mtu: <integer>
            ip6_manage_flag: <value in [disable, enable]>
            ip6_max_interval: <integer>
            ip6_min_interval: <integer>
            ip6_mode: <value in [static, dhcp, pppoe, ...]>
            ip6_other_flag: <value in [disable, enable]>
            ip6_reachable_time: <integer>
            ip6_retrans_time: <integer>
            ip6_send_adv: <value in [disable, enable]>
            ip6_subnet: <string>
            ip6_upstream_interface: <string>
            nd_cert: <string>
            nd_cga_modifier: <string>
            nd_mode: <value in [basic, SEND-compatible]>
            nd_security_level: <integer>
            nd_timestamp_delta: <integer>
            nd_timestamp_fuzz: <integer>
            vrip6_link_local: <string>
            vrrp_virtual_mac6: <value in [disable, enable]>
            ip6_delegated_prefix_list:
              -
                autonomous_flag: <value in [disable, enable]>
                onlink_flag: <value in [disable, enable]>
                prefix_id: <integer>
                rdnss: <list or string>
                rdnss_service: <value in [delegated, default, specify]>
                subnet: <string>
                upstream_interface: <string>
                delegated_prefix_iaid: <integer>
            ip6_extra_addr:
              -
                prefix: <string>
            ip6_prefix_list:
              -
                autonomous_flag: <value in [disable, enable]>
                dnssl: <list or string>
                onlink_flag: <value in [disable, enable]>
                preferred_life_time: <integer>
                prefix: <string>
                rdnss: <list or string>
                valid_life_time: <integer>
            vrrp6:
              -
                accept_mode: <value in [disable, enable]>
                adv_interval: <integer>
                preempt: <value in [disable, enable]>
                priority: <integer>
                start_time: <integer>
                status: <value in [disable, enable]>
                vrdst6: <string>
                vrgrp: <integer>
                vrid: <integer>
                vrip6: <string>
                ignore_default_route: <value in [disable, enable]>
                vrdst_priority: <integer>
            interface_identifier: <string>
            unique_autoconf_addr: <value in [disable, enable]>
            icmp6_send_redirect: <value in [disable, enable]>
            cli_conn6_status: <integer>
            ip6_prefix_mode: <value in [dhcp6, ra]>
            ra_send_mtu: <value in [disable, enable]>
            ip6_delegated_prefix_iaid: <integer>
            dhcp6_relay_source_interface: <value in [disable, enable]>
            dhcp6_relay_interface_id: <string>
            dhcp6_relay_source_ip: <string>
          l2forward: <value in [disable, enable]>
          l2tp_client: <value in [disable, enable]>
          lacp_ha_slave: <value in [disable, enable]>
          lacp_mode: <value in [static, passive, active]>
          lacp_speed: <value in [slow, fast]>
          lcp_echo_interval: <integer>
          lcp_max_echo_fails: <integer>
          link_up_delay: <integer>
          listen_forticlient_connection: <value in [disable, enable]>
          lldp_network_policy: <string>
          lldp_reception: <value in [disable, enable, vdom]>
          lldp_transmission: <value in [enable, disable, vdom]>
          log: <value in [disable, enable]>
          macaddr: <string>
          management_ip: <string>
          max_egress_burst_rate: <integer>
          max_egress_rate: <integer>
          mediatype: <value in [serdes-sfp, sgmii-sfp, cfp2-sr10, ...]>
          member: <list or string>
          min_links: <integer>
          min_links_down: <value in [operational, administrative]>
          mode: <value in [static, dhcp, pppoe, ...]>
          mtu: <integer>
          mtu_override: <value in [disable, enable]>
          mux_type: <value in [llc-encaps, vc-encaps]>
          name: <string>
          ndiscforward: <value in [disable, enable]>
          netbios_forward: <value in [disable, enable]>
          netflow_sampler: <value in [disable, tx, rx, ...]>
          npu_fastpath: <value in [disable, enable]>
          nst: <value in [disable, enable]>
          out_force_vlan_cos: <integer>
          outbandwidth: <integer>
          padt_retry_timeout: <integer>
          password: <list or string>
          peer_interface: <list or string>
          phy_mode: <value in [auto, adsl, vdsl, ...]>
          ping_serv_status: <integer>
          poe: <value in [disable, enable]>
          polling_interval: <integer>
          pppoe_unnumbered_negotiate: <value in [disable, enable]>
          pptp_auth_type: <value in [auto, pap, chap, ...]>
          pptp_client: <value in [disable, enable]>
          pptp_password: <list or string>
          pptp_server_ip: <string>
          pptp_timeout: <integer>
          pptp_user: <string>
          preserve_session_route: <value in [disable, enable]>
          priority: <integer>
          priority_override: <value in [disable, enable]>
          proxy_captive_portal: <value in [disable, enable]>
          redundant_interface: <string>
          remote_ip: <string>
          replacemsg_override_group: <string>
          retransmission: <value in [disable, enable]>
          role: <value in [lan, wan, dmz, ...]>
          sample_direction: <value in [rx, tx, both]>
          sample_rate: <integer>
          scan_botnet_connections: <value in [disable, block, monitor]>
          secondary_IP: <value in [disable, enable]>
          secondaryip:
            -
              allowaccess:
                - https
                - ping
                - ssh
                - snmp
                - http
                - telnet
                - fgfm
                - auto-ipsec
                - radius-acct
                - probe-response
                - capwap
                - dnp
                - ftm
                - fabric
                - speed-test
                - icond
                - scim
              detectprotocol:
                - ping
                - tcp-echo
                - udp-echo
              detectserver: <string>
              gwdetect: <value in [disable, enable]>
              ha_priority: <integer>
              id: <integer>
              ip: <string>
              ping_serv_status: <integer>
              seq: <integer>
              secip_relay_ip: <string>
          security_8021x_dynamic_vlan_id: <integer>
          security_8021x_master: <string>
          security_8021x_mode: <value in [default, dynamic-vlan, fallback, ...]>
          security_exempt_list: <string>
          security_external_logout: <string>
          security_external_web: <string>
          security_groups: <list or string>
          security_mac_auth_bypass: <value in [disable, enable, mac-auth-only]>
          security_mode: <value in [none, captive-portal, 802.1X]>
          security_redirect_url: <string>
          service_name: <string>
          sflow_sampler: <value in [disable, enable]>
          speed: <value in [auto, 10full, 10half, ...]>
          spillover_threshold: <integer>
          src_check: <value in [disable, enable]>
          status: <value in [down, up]>
          stp: <value in [disable, enable]>
          stp_ha_slave: <value in [disable, enable, priority-adjust]>
          stpforward: <value in [disable, enable]>
          stpforward_mode: <value in [rpl-all-ext-id, rpl-bridge-ext-id, rpl-nothing]>
          strip_priority_vlan_tag: <value in [disable, enable]>
          subst: <value in [disable, enable]>
          substitute_dst_mac: <string>
          switch: <string>
          switch_controller_access_vlan: <value in [disable, enable]>
          switch_controller_arp_inspection: <value in [disable, enable, monitor]>
          switch_controller_auth: <value in [radius, usergroup]>
          switch_controller_dhcp_snooping: <value in [disable, enable]>
          switch_controller_dhcp_snooping_option82: <value in [disable, enable]>
          switch_controller_dhcp_snooping_verify_mac: <value in [disable, enable]>
          switch_controller_igmp_snooping: <value in [disable, enable]>
          switch_controller_learning_limit: <integer>
          switch_controller_radius_server: <string>
          switch_controller_traffic_policy: <string>
          tc_mode: <value in [ptm, atm]>
          tcp_mss: <integer>
          trunk: <value in [disable, enable]>
          trust_ip_1: <string>
          trust_ip_2: <string>
          trust_ip_3: <string>
          trust_ip6_1: <string>
          trust_ip6_2: <string>
          trust_ip6_3: <string>
          type: <value in [physical, vlan, aggregate, ...]>
          username: <string>
          vci: <integer>
          vectoring: <value in [disable, enable]>
          vindex: <integer>
          vlanforward: <value in [disable, enable]>
          vlanid: <integer>
          vpi: <integer>
          vrf: <integer>
          vrrp:
            -
              accept_mode: <value in [disable, enable]>
              adv_interval: <integer>
              ignore_default_route: <value in [disable, enable]>
              preempt: <value in [disable, enable]>
              priority: <integer>
              start_time: <integer>
              status: <value in [disable, enable]>
              version: <value in [2, 3]>
              vrdst: <list or string>
              vrdst_priority: <integer>
              vrgrp: <integer>
              vrid: <integer>
              vrip: <string>
              proxy_arp:
                -
                  id: <integer>
                  ip: <string>
          vrrp_virtual_mac: <value in [disable, enable]>
          wccp: <value in [disable, enable]>
          weight: <integer>
          wifi_5g_threshold: <string>
          wifi_acl: <value in [deny, allow]>
          wifi_ap_band: <value in [any, 5g-preferred, 5g-only]>
          wifi_auth: <value in [PSK, RADIUS, radius, ...]>
          wifi_auto_connect: <value in [disable, enable]>
          wifi_auto_save: <value in [disable, enable]>
          wifi_broadcast_ssid: <value in [disable, enable]>
          wifi_encrypt: <value in [TKIP, AES]>
          wifi_fragment_threshold: <integer>
          wifi_key: <list or string>
          wifi_keyindex: <integer>
          wifi_mac_filter: <value in [disable, enable]>
          wifi_passphrase: <list or string>
          wifi_radius_server: <string>
          wifi_rts_threshold: <integer>
          wifi_security: <value in [None, WEP64, wep64, ...]>
          wifi_ssid: <string>
          wifi_usergroup: <string>
          wins_ip: <string>
          eip: <string>
          fortilink_neighbor_detect: <value in [lldp, fortilink]>
          ingress_shaping_profile: <string>
          ring_rx: <integer>
          ring_tx: <integer>
          switch_controller_igmp_snooping_fast_leave: <value in [disable, enable]>
          switch_controller_igmp_snooping_proxy: <value in [disable, enable]>
          switch_controller_rspan_mode: <value in [disable, enable]>
          bandwidth_measure_time: <integer>
          ip_managed_by_fortiipam: <value in [disable, enable, inherit-global]>
          managed_subnetwork_size: <value in [256, 512, 1024, ...]>
          measured_downstream_bandwidth: <integer>
          measured_upstream_bandwidth: <integer>
          monitor_bandwidth: <value in [disable, enable]>
          swc_vlan: <integer>
          switch_controller_feature: <value in [none, default-vlan, quarantine, ...]>
          switch_controller_mgmt_vlan: <integer>
          switch_controller_nac: <string>
          vlan_protocol: <value in [8021q, 8021ad]>
          dhcp_relay_interface: <string>
          dhcp_relay_interface_select_method: <value in [auto, sdwan, specify]>
          np_qos_profile: <integer>
          swc_first_create: <integer>
          switch_controller_iot_scanning: <value in [disable, enable]>
          switch_controller_source_ip: <value in [outbound, fixed]>
          dhcp_relay_request_all_server: <value in [disable, enable]>
          stp_ha_secondary: <value in [disable, enable, priority-adjust]>
          switch_controller_dynamic: <string>
          auth_cert: <string>
          auth_portal_addr: <string>
          dhcp_classless_route_addition: <value in [disable, enable]>
          dhcp_relay_link_selection: <string>
          dns_server_protocol:
            - cleartext
            - dot
            - doh
          eap_ca_cert: <string>
          eap_identity: <string>
          eap_method: <value in [tls, peap]>
          eap_password: <list or string>
          eap_supplicant: <value in [disable, enable]>
          eap_user_cert: <string>
          ike_saml_server: <string>
          lacp_ha_secondary: <value in [disable, enable]>
          pvc_atm_qos: <value in [cbr, rt-vbr, nrt-vbr, ...]>
          pvc_chan: <integer>
          pvc_crc: <integer>
          pvc_pcr: <integer>
          pvc_scr: <integer>
          pvc_vlan_id: <integer>
          pvc_vlan_rx_id: <integer>
          pvc_vlan_rx_op: <value in [pass-through, replace, remove]>
          pvc_vlan_tx_id: <integer>
          pvc_vlan_tx_op: <value in [pass-through, replace, remove]>
          reachable_time: <integer>
          select_profile_30a_35b: <value in [30A, 35B]>
          sfp_dsl: <value in [disable, enable]>
          sfp_dsl_adsl_fallback: <value in [disable, enable]>
          sfp_dsl_autodetect: <value in [disable, enable]>
          sfp_dsl_mac: <string>
          sw_algorithm: <value in [l2, l3, eh, ...]>
          system_id: <string>
          system_id_type: <value in [auto, user]>
          vlan_id: <integer>
          vlan_op_mode: <value in [tag, untag, passthrough]>
          generic_receive_offload: <value in [disable, enable]>
          interconnect_profile: <value in [default, profile1, profile2]>
          large_receive_offload: <value in [disable, enable]>
          annex: <value in [a, b, j, ...]>
          aggregate_type: <value in [physical, vxlan]>
          switch_controller_netflow_collect: <value in [disable, enable]>
          wifi_dns_server1: <string>
          wifi_dns_server2: <string>
          wifi_gateway: <string>
          default_purdue_level: <value in [1, 2, 3, ...]>
          dhcp_broadcast_flag: <value in [disable, enable]>
          dhcp_smart_relay: <value in [disable, enable]>
          switch_controller_offloading: <value in [disable, enable]>
          switch_controller_offloading_gw: <value in [disable, enable]>
          switch_controller_offloading_ip: <string>
          dhcp_relay_circuit_id: <string>
          dhcp_relay_source_ip: <string>
          switch_controller_offload: <value in [disable, enable]>
          switch_controller_offload_gw: <value in [disable, enable]>
          switch_controller_offload_ip: <string>
          mirroring_direction: <value in [rx, tx, both]>
          mirroring_port: <string>
          port_mirroring: <value in [disable, enable]>
          security_8021x_member_mode: <value in [disable, switch]>
          stp_edge: <value in [disable, enable]>
          dhcp_relay_allow_no_end_option: <value in [disable, enable]>
          netflow_sample_rate: <integer>
          netflow_sampler_id: <integer>
          pppoe_egress_cos: <value in [cos0, cos1, cos2, ...]>
          security_ip_auth_bypass: <value in [disable, enable]>
          virtual_mac: <string>
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
        '/pm/config/adom/{adom}/obj/fsp/vlan/{vlan}/interface',
        '/pm/config/global/obj/fsp/vlan/{vlan}/interface'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/fsp/vlan/{vlan}/interface/{interface}',
        '/pm/config/global/obj/fsp/vlan/{vlan}/interface/{interface}'
    ]

    url_params = ['adom', 'vlan']
    module_primary_key = None
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'vlan': {'required': True, 'type': 'str'},
        'fsp_vlan_interface': {
            'type': 'dict',
            'v_range': [['6.0.0', '']],
            'options': {
                'ac-name': {'type': 'str'},
                'aggregate': {'type': 'str'},
                'algorithm': {'choices': ['L2', 'L3', 'L4', 'LB', 'Source-MAC'], 'type': 'str'},
                'alias': {'type': 'str'},
                'allowaccess': {
                    'type': 'list',
                    'choices': [
                        'https', 'ping', 'ssh', 'snmp', 'http', 'telnet', 'fgfm', 'auto-ipsec', 'radius-acct', 'probe-response', 'capwap', 'dnp', 'ftm',
                        'fabric', 'speed-test'
                    ],
                    'elements': 'str'
                },
                'ap-discover': {'choices': ['disable', 'enable'], 'type': 'str'},
                'arpforward': {'choices': ['disable', 'enable'], 'type': 'str'},
                'atm-protocol': {'choices': ['none', 'ipoa'], 'type': 'str'},
                'auth-type': {'choices': ['auto', 'pap', 'chap', 'mschapv1', 'mschapv2'], 'type': 'str'},
                'auto-auth-extension-device': {'choices': ['disable', 'enable'], 'type': 'str'},
                'bfd': {'choices': ['global', 'enable', 'disable'], 'type': 'str'},
                'bfd-desired-min-tx': {'type': 'int'},
                'bfd-detect-mult': {'type': 'int'},
                'bfd-required-min-rx': {'type': 'int'},
                'broadcast-forticlient-discovery': {'choices': ['disable', 'enable'], 'type': 'str'},
                'broadcast-forward': {'choices': ['disable', 'enable'], 'type': 'str'},
                'captive-portal': {'type': 'int'},
                'cli-conn-status': {'type': 'int'},
                'color': {'type': 'int'},
                'ddns': {'choices': ['disable', 'enable'], 'type': 'str'},
                'ddns-auth': {'choices': ['disable', 'tsig'], 'type': 'str'},
                'ddns-domain': {'type': 'str'},
                'ddns-key': {'no_log': True, 'type': 'raw'},
                'ddns-keyname': {'no_log': True, 'type': 'str'},
                'ddns-password': {'no_log': True, 'type': 'raw'},
                'ddns-server': {
                    'choices': [
                        'dhs.org', 'dyndns.org', 'dyns.net', 'tzo.com', 'ods.org', 'vavic.com', 'now.net.cn', 'dipdns.net', 'easydns.com', 'genericDDNS'
                    ],
                    'type': 'str'
                },
                'ddns-server-ip': {'type': 'str'},
                'ddns-sn': {'type': 'str'},
                'ddns-ttl': {'type': 'int'},
                'ddns-username': {'type': 'str'},
                'ddns-zone': {'type': 'str'},
                'dedicated-to': {'choices': ['none', 'management'], 'type': 'str'},
                'defaultgw': {'choices': ['disable', 'enable'], 'type': 'str'},
                'description': {'type': 'str'},
                'detected-peer-mtu': {'type': 'int'},
                'detectprotocol': {'type': 'list', 'choices': ['ping', 'tcp-echo', 'udp-echo'], 'elements': 'str'},
                'detectserver': {'type': 'str'},
                'device-access-list': {'type': 'raw'},
                'device-identification': {'choices': ['disable', 'enable'], 'type': 'str'},
                'device-identification-active-scan': {'choices': ['disable', 'enable'], 'type': 'str'},
                'device-netscan': {'choices': ['disable', 'enable'], 'type': 'str'},
                'device-user-identification': {'choices': ['disable', 'enable'], 'type': 'str'},
                'devindex': {'type': 'int'},
                'dhcp-client-identifier': {'type': 'str'},
                'dhcp-relay-agent-option': {'choices': ['disable', 'enable'], 'type': 'str'},
                'dhcp-relay-ip': {'type': 'raw'},
                'dhcp-relay-service': {'choices': ['disable', 'enable'], 'type': 'str'},
                'dhcp-relay-type': {'choices': ['regular', 'ipsec'], 'type': 'str'},
                'dhcp-renew-time': {'type': 'int'},
                'disc-retry-timeout': {'type': 'int'},
                'disconnect-threshold': {'type': 'int'},
                'distance': {'type': 'int'},
                'dns-query': {'choices': ['disable', 'recursive', 'non-recursive'], 'type': 'str'},
                'dns-server-override': {'choices': ['disable', 'enable'], 'type': 'str'},
                'drop-fragment': {'choices': ['disable', 'enable'], 'type': 'str'},
                'drop-overlapped-fragment': {'choices': ['disable', 'enable'], 'type': 'str'},
                'egress-cos': {'choices': ['disable', 'cos0', 'cos1', 'cos2', 'cos3', 'cos4', 'cos5', 'cos6', 'cos7'], 'type': 'str'},
                'egress-shaping-profile': {'type': 'str'},
                'endpoint-compliance': {'choices': ['disable', 'enable'], 'type': 'str'},
                'estimated-downstream-bandwidth': {'type': 'int'},
                'estimated-upstream-bandwidth': {'type': 'int'},
                'explicit-ftp-proxy': {'choices': ['disable', 'enable'], 'type': 'str'},
                'explicit-web-proxy': {'choices': ['disable', 'enable'], 'type': 'str'},
                'external': {'choices': ['disable', 'enable'], 'type': 'str'},
                'fail-action-on-extender': {'choices': ['soft-restart', 'hard-restart', 'reboot'], 'type': 'str'},
                'fail-alert-interfaces': {'type': 'raw'},
                'fail-alert-method': {'choices': ['link-failed-signal', 'link-down'], 'type': 'str'},
                'fail-detect': {'choices': ['disable', 'enable'], 'type': 'str'},
                'fail-detect-option': {'type': 'list', 'choices': ['detectserver', 'link-down'], 'elements': 'str'},
                'fdp': {'choices': ['disable', 'enable'], 'type': 'str'},
                'fortiheartbeat': {'choices': ['disable', 'enable'], 'type': 'str'},
                'fortilink': {'choices': ['disable', 'enable'], 'type': 'str'},
                'fortilink-backup-link': {'type': 'int'},
                'fortilink-split-interface': {'choices': ['disable', 'enable'], 'type': 'str'},
                'fortilink-stacking': {'choices': ['disable', 'enable'], 'type': 'str'},
                'forward-domain': {'type': 'int'},
                'forward-error-correction': {
                    'choices': [
                        'disable', 'enable', 'rs-fec', 'base-r-fec', 'fec-cl91', 'fec-cl74', 'rs-544', 'none', 'cl91-rs-fec', 'cl74-fc-fec', 'auto'
                    ],
                    'type': 'str'
                },
                'fp-anomaly': {
                    'type': 'list',
                    'choices': [
                        'drop_tcp_fin_noack', 'pass_winnuke', 'pass_tcpland', 'pass_udpland', 'pass_icmpland', 'pass_ipland', 'pass_iprr', 'pass_ipssrr',
                        'pass_iplsrr', 'pass_ipstream', 'pass_ipsecurity', 'pass_iptimestamp', 'pass_ipunknown_option', 'pass_ipunknown_prot',
                        'pass_icmp_frag', 'pass_tcp_no_flag', 'pass_tcp_fin_noack', 'drop_winnuke', 'drop_tcpland', 'drop_udpland', 'drop_icmpland',
                        'drop_ipland', 'drop_iprr', 'drop_ipssrr', 'drop_iplsrr', 'drop_ipstream', 'drop_ipsecurity', 'drop_iptimestamp',
                        'drop_ipunknown_option', 'drop_ipunknown_prot', 'drop_icmp_frag', 'drop_tcp_no_flag'
                    ],
                    'elements': 'str'
                },
                'fp-disable': {'type': 'list', 'choices': ['all', 'ipsec', 'none'], 'elements': 'str'},
                'gateway-address': {'type': 'str'},
                'gi-gk': {'choices': ['disable', 'enable'], 'type': 'str'},
                'gwaddr': {'v_range': [['6.0.0', '7.2.0']], 'type': 'str'},
                'gwdetect': {'choices': ['disable', 'enable'], 'type': 'str'},
                'ha-priority': {'type': 'int'},
                'icmp-accept-redirect': {'choices': ['disable', 'enable'], 'type': 'str'},
                'icmp-redirect': {'choices': ['disable', 'enable'], 'type': 'str'},
                'icmp-send-redirect': {'choices': ['disable', 'enable'], 'type': 'str'},
                'ident-accept': {'choices': ['disable', 'enable'], 'type': 'str'},
                'idle-timeout': {'type': 'int'},
                'if-mdix': {'choices': ['auto', 'normal', 'crossover'], 'type': 'str'},
                'if-media': {'choices': ['auto', 'copper', 'fiber'], 'type': 'str'},
                'in-force-vlan-cos': {'type': 'int'},
                'inbandwidth': {'type': 'int'},
                'ingress-cos': {'choices': ['disable', 'cos0', 'cos1', 'cos2', 'cos3', 'cos4', 'cos5', 'cos6', 'cos7'], 'type': 'str'},
                'ingress-spillover-threshold': {'type': 'int'},
                'internal': {'type': 'int'},
                'ip': {'type': 'str'},
                'ipmac': {'choices': ['disable', 'enable'], 'type': 'str'},
                'ips-sniffer-mode': {'choices': ['disable', 'enable'], 'type': 'str'},
                'ipunnumbered': {'type': 'str'},
                'ipv6': {
                    'type': 'dict',
                    'options': {
                        'autoconf': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'dhcp6-client-options': {'type': 'list', 'choices': ['rapid', 'iapd', 'iana', 'dns', 'dnsname'], 'elements': 'str'},
                        'dhcp6-information-request': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'dhcp6-prefix-delegation': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'dhcp6-prefix-hint': {'type': 'str'},
                        'dhcp6-prefix-hint-plt': {'type': 'int'},
                        'dhcp6-prefix-hint-vlt': {'type': 'int'},
                        'dhcp6-relay-ip': {'type': 'str'},
                        'dhcp6-relay-service': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'dhcp6-relay-type': {'choices': ['regular'], 'type': 'str'},
                        'ip6-address': {'type': 'str'},
                        'ip6-allowaccess': {
                            'type': 'list',
                            'choices': ['https', 'ping', 'ssh', 'snmp', 'http', 'telnet', 'fgfm', 'capwap', 'fabric'],
                            'elements': 'str'
                        },
                        'ip6-default-life': {'type': 'int'},
                        'ip6-dns-server-override': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'ip6-hop-limit': {'type': 'int'},
                        'ip6-link-mtu': {'type': 'int'},
                        'ip6-manage-flag': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'ip6-max-interval': {'type': 'int'},
                        'ip6-min-interval': {'type': 'int'},
                        'ip6-mode': {'choices': ['static', 'dhcp', 'pppoe', 'delegated'], 'type': 'str'},
                        'ip6-other-flag': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'ip6-reachable-time': {'type': 'int'},
                        'ip6-retrans-time': {'type': 'int'},
                        'ip6-send-adv': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'ip6-subnet': {'type': 'str'},
                        'ip6-upstream-interface': {'type': 'str'},
                        'nd-cert': {'type': 'str'},
                        'nd-cga-modifier': {'type': 'str'},
                        'nd-mode': {'choices': ['basic', 'SEND-compatible'], 'type': 'str'},
                        'nd-security-level': {'type': 'int'},
                        'nd-timestamp-delta': {'type': 'int'},
                        'nd-timestamp-fuzz': {'type': 'int'},
                        'vrip6_link_local': {'type': 'str'},
                        'vrrp-virtual-mac6': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'ip6-delegated-prefix-list': {
                            'v_range': [['6.2.2', '']],
                            'type': 'list',
                            'options': {
                                'autonomous-flag': {'v_range': [['6.2.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'onlink-flag': {'v_range': [['6.2.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'prefix-id': {'v_range': [['6.2.2', '']], 'type': 'int'},
                                'rdnss': {'v_range': [['6.2.2', '']], 'type': 'raw'},
                                'rdnss-service': {'v_range': [['6.2.2', '']], 'choices': ['delegated', 'default', 'specify'], 'type': 'str'},
                                'subnet': {'v_range': [['6.2.2', '']], 'type': 'str'},
                                'upstream-interface': {'v_range': [['6.2.2', '']], 'type': 'str'},
                                'delegated-prefix-iaid': {'v_range': [['7.0.2', '']], 'type': 'int'}
                            },
                            'elements': 'dict'
                        },
                        'ip6-extra-addr': {
                            'v_range': [['6.2.2', '']],
                            'type': 'list',
                            'options': {'prefix': {'v_range': [['6.2.2', '']], 'type': 'str'}},
                            'elements': 'dict'
                        },
                        'ip6-prefix-list': {
                            'v_range': [['6.2.2', '']],
                            'type': 'list',
                            'options': {
                                'autonomous-flag': {'v_range': [['6.2.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'dnssl': {'v_range': [['6.2.2', '']], 'type': 'raw'},
                                'onlink-flag': {'v_range': [['6.2.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'preferred-life-time': {'v_range': [['6.2.2', '']], 'type': 'int'},
                                'prefix': {'v_range': [['6.2.2', '']], 'type': 'str'},
                                'rdnss': {'v_range': [['6.2.2', '']], 'type': 'raw'},
                                'valid-life-time': {'v_range': [['6.2.2', '']], 'type': 'int'}
                            },
                            'elements': 'dict'
                        },
                        'vrrp6': {
                            'v_range': [['6.2.2', '']],
                            'type': 'list',
                            'options': {
                                'accept-mode': {'v_range': [['6.2.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'adv-interval': {'v_range': [['6.2.2', '']], 'type': 'int'},
                                'preempt': {'v_range': [['6.2.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'priority': {'v_range': [['6.2.2', '']], 'type': 'int'},
                                'start-time': {'v_range': [['6.2.2', '']], 'type': 'int'},
                                'status': {'v_range': [['6.2.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'vrdst6': {'v_range': [['6.2.2', '']], 'type': 'str'},
                                'vrgrp': {'v_range': [['6.2.2', '']], 'type': 'int'},
                                'vrid': {'v_range': [['6.2.2', '']], 'type': 'int'},
                                'vrip6': {'v_range': [['6.2.2', '']], 'type': 'str'},
                                'ignore-default-route': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'vrdst-priority': {'v_range': [['7.6.0', '']], 'type': 'int'}
                            },
                            'elements': 'dict'
                        },
                        'interface-identifier': {'v_range': [['6.4.1', '']], 'type': 'str'},
                        'unique-autoconf-addr': {'v_range': [['6.4.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'icmp6-send-redirect': {'v_range': [['6.4.4', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'cli-conn6-status': {'v_range': [['7.0.0', '']], 'type': 'int'},
                        'ip6-prefix-mode': {'v_range': [['7.0.0', '']], 'choices': ['dhcp6', 'ra'], 'type': 'str'},
                        'ra-send-mtu': {'v_range': [['6.4.6', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'ip6-delegated-prefix-iaid': {'v_range': [['7.0.2', '']], 'type': 'int'},
                        'dhcp6-relay-source-interface': {'v_range': [['7.2.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'dhcp6-relay-interface-id': {'v_range': [['7.4.1', '']], 'type': 'str'},
                        'dhcp6-relay-source-ip': {'v_range': [['7.4.1', '']], 'type': 'str'}
                    }
                },
                'l2forward': {'choices': ['disable', 'enable'], 'type': 'str'},
                'l2tp-client': {'choices': ['disable', 'enable'], 'type': 'str'},
                'lacp-ha-slave': {'choices': ['disable', 'enable'], 'type': 'str'},
                'lacp-mode': {'choices': ['static', 'passive', 'active'], 'type': 'str'},
                'lacp-speed': {'choices': ['slow', 'fast'], 'type': 'str'},
                'lcp-echo-interval': {'type': 'int'},
                'lcp-max-echo-fails': {'type': 'int'},
                'link-up-delay': {'type': 'int'},
                'listen-forticlient-connection': {'choices': ['disable', 'enable'], 'type': 'str'},
                'lldp-network-policy': {'type': 'str'},
                'lldp-reception': {'choices': ['disable', 'enable', 'vdom'], 'type': 'str'},
                'lldp-transmission': {'choices': ['enable', 'disable', 'vdom'], 'type': 'str'},
                'log': {'choices': ['disable', 'enable'], 'type': 'str'},
                'macaddr': {'type': 'str'},
                'management-ip': {'type': 'str'},
                'max-egress-burst-rate': {'type': 'int'},
                'max-egress-rate': {'type': 'int'},
                'mediatype': {
                    'choices': [
                        'serdes-sfp', 'sgmii-sfp', 'cfp2-sr10', 'cfp2-lr4', 'serdes-copper-sfp', 'sr', 'cr', 'lr', 'qsfp28-sr4', 'qsfp28-lr4',
                        'qsfp28-cr4', 'sr4', 'cr4', 'lr4', 'none', 'gmii', 'sgmii', 'sr2', 'lr2', 'cr2', 'sr8', 'lr8', 'cr8'
                    ],
                    'type': 'str'
                },
                'member': {'type': 'raw'},
                'min-links': {'type': 'int'},
                'min-links-down': {'choices': ['operational', 'administrative'], 'type': 'str'},
                'mode': {'choices': ['static', 'dhcp', 'pppoe', 'pppoa', 'ipoa', 'eoa'], 'type': 'str'},
                'mtu': {'type': 'int'},
                'mtu-override': {'choices': ['disable', 'enable'], 'type': 'str'},
                'mux-type': {'choices': ['llc-encaps', 'vc-encaps'], 'type': 'str'},
                'name': {'type': 'str'},
                'ndiscforward': {'choices': ['disable', 'enable'], 'type': 'str'},
                'netbios-forward': {'choices': ['disable', 'enable'], 'type': 'str'},
                'netflow-sampler': {'choices': ['disable', 'tx', 'rx', 'both'], 'type': 'str'},
                'npu-fastpath': {'choices': ['disable', 'enable'], 'type': 'str'},
                'nst': {'choices': ['disable', 'enable'], 'type': 'str'},
                'out-force-vlan-cos': {'type': 'int'},
                'outbandwidth': {'type': 'int'},
                'padt-retry-timeout': {'type': 'int'},
                'password': {'no_log': True, 'type': 'raw'},
                'peer-interface': {'type': 'raw'},
                'phy-mode': {
                    'choices': ['auto', 'adsl', 'vdsl', 'adsl-auto', 'vdsl2', 'adsl2+', 'adsl2', 'g.dmt', 't1.413', 'g.lite', 'g-dmt', 't1-413', 'g-lite'],
                    'type': 'str'
                },
                'ping-serv-status': {'v_range': [['6.0.0', '7.2.0']], 'type': 'int'},
                'poe': {'choices': ['disable', 'enable'], 'type': 'str'},
                'polling-interval': {'type': 'int'},
                'pppoe-unnumbered-negotiate': {'choices': ['disable', 'enable'], 'type': 'str'},
                'pptp-auth-type': {'choices': ['auto', 'pap', 'chap', 'mschapv1', 'mschapv2'], 'type': 'str'},
                'pptp-client': {'choices': ['disable', 'enable'], 'type': 'str'},
                'pptp-password': {'no_log': True, 'type': 'raw'},
                'pptp-server-ip': {'type': 'str'},
                'pptp-timeout': {'type': 'int'},
                'pptp-user': {'type': 'str'},
                'preserve-session-route': {'choices': ['disable', 'enable'], 'type': 'str'},
                'priority': {'type': 'int'},
                'priority-override': {'choices': ['disable', 'enable'], 'type': 'str'},
                'proxy-captive-portal': {'choices': ['disable', 'enable'], 'type': 'str'},
                'redundant-interface': {'type': 'str'},
                'remote-ip': {'type': 'str'},
                'replacemsg-override-group': {'type': 'str'},
                'retransmission': {'choices': ['disable', 'enable'], 'type': 'str'},
                'role': {'choices': ['lan', 'wan', 'dmz', 'undefined'], 'type': 'str'},
                'sample-direction': {'choices': ['rx', 'tx', 'both'], 'type': 'str'},
                'sample-rate': {'type': 'int'},
                'scan-botnet-connections': {'choices': ['disable', 'block', 'monitor'], 'type': 'str'},
                'secondary-IP': {'choices': ['disable', 'enable'], 'type': 'str'},
                'secondaryip': {
                    'type': 'list',
                    'options': {
                        'allowaccess': {
                            'type': 'list',
                            'choices': [
                                'https', 'ping', 'ssh', 'snmp', 'http', 'telnet', 'fgfm', 'auto-ipsec', 'radius-acct', 'probe-response', 'capwap', 'dnp',
                                'ftm', 'fabric', 'speed-test', 'icond', 'scim'
                            ],
                            'elements': 'str'
                        },
                        'detectprotocol': {
                            'v_range': [['6.0.0', '7.2.0']],
                            'type': 'list',
                            'choices': ['ping', 'tcp-echo', 'udp-echo'],
                            'elements': 'str'
                        },
                        'detectserver': {'v_range': [['6.0.0', '7.2.0']], 'type': 'str'},
                        'gwdetect': {'v_range': [['6.0.0', '7.2.0']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'ha-priority': {'v_range': [['6.0.0', '7.2.0']], 'type': 'int'},
                        'id': {'type': 'int'},
                        'ip': {'type': 'str'},
                        'ping-serv-status': {'v_range': [['6.0.0', '7.2.0']], 'type': 'int'},
                        'seq': {'type': 'int'},
                        'secip-relay-ip': {'v_range': [['7.4.0', '']], 'type': 'str'}
                    },
                    'elements': 'dict'
                },
                'security-8021x-dynamic-vlan-id': {'type': 'int'},
                'security-8021x-master': {'type': 'str'},
                'security-8021x-mode': {'choices': ['default', 'dynamic-vlan', 'fallback', 'slave'], 'type': 'str'},
                'security-exempt-list': {'type': 'str'},
                'security-external-logout': {'type': 'str'},
                'security-external-web': {'type': 'str'},
                'security-groups': {'type': 'raw'},
                'security-mac-auth-bypass': {'choices': ['disable', 'enable', 'mac-auth-only'], 'type': 'str'},
                'security-mode': {'choices': ['none', 'captive-portal', '802.1X'], 'type': 'str'},
                'security-redirect-url': {'type': 'str'},
                'service-name': {'type': 'str'},
                'sflow-sampler': {'choices': ['disable', 'enable'], 'type': 'str'},
                'speed': {
                    'choices': [
                        'auto', '10full', '10half', '100full', '100half', '1000full', '1000half', '10000full', '1000auto', '10000auto', '40000full',
                        '100Gfull', '25000full', '40000auto', '25000auto', '100Gauto', '400Gfull', '400Gauto', '50000full', '2500auto', '5000auto',
                        '50000auto', '200Gfull', '200Gauto', '100auto'
                    ],
                    'type': 'str'
                },
                'spillover-threshold': {'type': 'int'},
                'src-check': {'choices': ['disable', 'enable'], 'type': 'str'},
                'status': {'choices': ['down', 'up'], 'type': 'str'},
                'stp': {'choices': ['disable', 'enable'], 'type': 'str'},
                'stp-ha-slave': {'choices': ['disable', 'enable', 'priority-adjust'], 'type': 'str'},
                'stpforward': {'choices': ['disable', 'enable'], 'type': 'str'},
                'stpforward-mode': {'choices': ['rpl-all-ext-id', 'rpl-bridge-ext-id', 'rpl-nothing'], 'type': 'str'},
                'strip-priority-vlan-tag': {'choices': ['disable', 'enable'], 'type': 'str'},
                'subst': {'choices': ['disable', 'enable'], 'type': 'str'},
                'substitute-dst-mac': {'type': 'str'},
                'switch': {'type': 'str'},
                'switch-controller-access-vlan': {'choices': ['disable', 'enable'], 'type': 'str'},
                'switch-controller-arp-inspection': {'choices': ['disable', 'enable', 'monitor'], 'type': 'str'},
                'switch-controller-auth': {'choices': ['radius', 'usergroup'], 'type': 'str'},
                'switch-controller-dhcp-snooping': {'choices': ['disable', 'enable'], 'type': 'str'},
                'switch-controller-dhcp-snooping-option82': {'choices': ['disable', 'enable'], 'type': 'str'},
                'switch-controller-dhcp-snooping-verify-mac': {'choices': ['disable', 'enable'], 'type': 'str'},
                'switch-controller-igmp-snooping': {'choices': ['disable', 'enable'], 'type': 'str'},
                'switch-controller-learning-limit': {'type': 'int'},
                'switch-controller-radius-server': {'type': 'str'},
                'switch-controller-traffic-policy': {'type': 'str'},
                'tc-mode': {'choices': ['ptm', 'atm'], 'type': 'str'},
                'tcp-mss': {'type': 'int'},
                'trunk': {'choices': ['disable', 'enable'], 'type': 'str'},
                'trust-ip-1': {'type': 'str'},
                'trust-ip-2': {'type': 'str'},
                'trust-ip-3': {'type': 'str'},
                'trust-ip6-1': {'type': 'str'},
                'trust-ip6-2': {'type': 'str'},
                'trust-ip6-3': {'type': 'str'},
                'type': {
                    'choices': [
                        'physical', 'vlan', 'aggregate', 'redundant', 'tunnel', 'wireless', 'vdom-link', 'loopback', 'switch', 'hard-switch', 'hdlc',
                        'vap-switch', 'wl-mesh', 'fortilink', 'switch-vlan', 'fctrl-trunk', 'tdm', 'fext-wan', 'vxlan', 'emac-vlan', 'geneve', 'ssl',
                        'lan-extension'
                    ],
                    'type': 'str'
                },
                'username': {'type': 'str'},
                'vci': {'type': 'int'},
                'vectoring': {'choices': ['disable', 'enable'], 'type': 'str'},
                'vindex': {'type': 'int'},
                'vlanforward': {'choices': ['disable', 'enable'], 'type': 'str'},
                'vlanid': {'type': 'int'},
                'vpi': {'type': 'int'},
                'vrf': {'type': 'int'},
                'vrrp': {
                    'type': 'list',
                    'options': {
                        'accept-mode': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'adv-interval': {'type': 'int'},
                        'ignore-default-route': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'preempt': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'priority': {'type': 'int'},
                        'start-time': {'type': 'int'},
                        'status': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'version': {'choices': ['2', '3'], 'type': 'str'},
                        'vrdst': {'type': 'raw'},
                        'vrdst-priority': {'type': 'int'},
                        'vrgrp': {'type': 'int'},
                        'vrid': {'type': 'int'},
                        'vrip': {'type': 'str'},
                        'proxy-arp': {
                            'v_range': [['7.4.0', '']],
                            'type': 'list',
                            'options': {'id': {'v_range': [['7.4.0', '']], 'type': 'int'}, 'ip': {'v_range': [['7.4.0', '']], 'type': 'str'}},
                            'elements': 'dict'
                        }
                    },
                    'elements': 'dict'
                },
                'vrrp-virtual-mac': {'choices': ['disable', 'enable'], 'type': 'str'},
                'wccp': {'choices': ['disable', 'enable'], 'type': 'str'},
                'weight': {'type': 'int'},
                'wifi-5g-threshold': {'type': 'str'},
                'wifi-acl': {'choices': ['deny', 'allow'], 'type': 'str'},
                'wifi-ap-band': {'choices': ['any', '5g-preferred', '5g-only'], 'type': 'str'},
                'wifi-auth': {'choices': ['PSK', 'RADIUS', 'radius', 'usergroup'], 'type': 'str'},
                'wifi-auto-connect': {'choices': ['disable', 'enable'], 'type': 'str'},
                'wifi-auto-save': {'choices': ['disable', 'enable'], 'type': 'str'},
                'wifi-broadcast-ssid': {'choices': ['disable', 'enable'], 'type': 'str'},
                'wifi-encrypt': {'choices': ['TKIP', 'AES'], 'type': 'str'},
                'wifi-fragment-threshold': {'type': 'int'},
                'wifi-key': {'no_log': True, 'type': 'raw'},
                'wifi-keyindex': {'no_log': True, 'type': 'int'},
                'wifi-mac-filter': {'choices': ['disable', 'enable'], 'type': 'str'},
                'wifi-passphrase': {'no_log': True, 'type': 'raw'},
                'wifi-radius-server': {'type': 'str'},
                'wifi-rts-threshold': {'type': 'int'},
                'wifi-security': {
                    'choices': [
                        'None', 'WEP64', 'wep64', 'WEP128', 'wep128', 'WPA_PSK', 'WPA_RADIUS', 'WPA', 'WPA2', 'WPA2_AUTO', 'open', 'wpa-personal',
                        'wpa-enterprise', 'wpa-only-personal', 'wpa-only-enterprise', 'wpa2-only-personal', 'wpa2-only-enterprise'
                    ],
                    'type': 'str'
                },
                'wifi-ssid': {'type': 'str'},
                'wifi-usergroup': {'type': 'str'},
                'wins-ip': {'type': 'str'},
                'eip': {'v_range': [['6.2.1', '']], 'type': 'str'},
                'fortilink-neighbor-detect': {'v_range': [['6.2.1', '']], 'choices': ['lldp', 'fortilink'], 'type': 'str'},
                'ingress-shaping-profile': {'v_range': [['6.2.1', '']], 'type': 'str'},
                'ring-rx': {'v_range': [['6.2.1', '']], 'type': 'int'},
                'ring-tx': {'v_range': [['6.2.1', '']], 'type': 'int'},
                'switch-controller-igmp-snooping-fast-leave': {'v_range': [['6.2.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'switch-controller-igmp-snooping-proxy': {'v_range': [['6.2.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'switch-controller-rspan-mode': {'v_range': [['6.2.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'bandwidth-measure-time': {'v_range': [['6.4.0', '']], 'type': 'int'},
                'ip-managed-by-fortiipam': {'v_range': [['6.4.0', '']], 'choices': ['disable', 'enable', 'inherit-global'], 'type': 'str'},
                'managed-subnetwork-size': {
                    'v_range': [['6.4.0', '']],
                    'choices': ['256', '512', '1024', '2048', '4096', '8192', '16384', '32768', '65536', '32', '64', '128'],
                    'type': 'str'
                },
                'measured-downstream-bandwidth': {'v_range': [['6.4.0', '']], 'type': 'int'},
                'measured-upstream-bandwidth': {'v_range': [['6.4.0', '']], 'type': 'int'},
                'monitor-bandwidth': {'v_range': [['6.4.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'swc-vlan': {'v_range': [['6.4.0', '']], 'type': 'int'},
                'switch-controller-feature': {
                    'v_range': [['6.4.0', '']],
                    'choices': ['none', 'default-vlan', 'quarantine', 'sniffer', 'voice', 'camera', 'rspan', 'video', 'nac', 'nac-segment'],
                    'type': 'str'
                },
                'switch-controller-mgmt-vlan': {'v_range': [['6.4.0', '']], 'type': 'int'},
                'switch-controller-nac': {'v_range': [['6.4.0', '']], 'type': 'str'},
                'vlan-protocol': {'v_range': [['6.4.0', '']], 'choices': ['8021q', '8021ad'], 'type': 'str'},
                'dhcp-relay-interface': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'str'},
                'dhcp-relay-interface-select-method': {
                    'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']],
                    'choices': ['auto', 'sdwan', 'specify'],
                    'type': 'str'
                },
                'np-qos-profile': {'v_range': [['6.2.7', '6.2.12'], ['6.4.4', '']], 'type': 'int'},
                'swc-first-create': {'v_range': [['6.4.3', '']], 'type': 'int'},
                'switch-controller-iot-scanning': {'v_range': [['6.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'switch-controller-source-ip': {'v_range': [['6.4.3', '']], 'choices': ['outbound', 'fixed'], 'type': 'str'},
                'dhcp-relay-request-all-server': {'v_range': [['6.2.8', '6.2.12'], ['6.4.6', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'stp-ha-secondary': {'v_range': [['7.0.0', '']], 'choices': ['disable', 'enable', 'priority-adjust'], 'type': 'str'},
                'switch-controller-dynamic': {'v_range': [['7.0.0', '']], 'type': 'str'},
                'auth-cert': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'auth-portal-addr': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'dhcp-classless-route-addition': {'v_range': [['7.0.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'dhcp-relay-link-selection': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'dns-server-protocol': {'v_range': [['7.0.3', '']], 'type': 'list', 'choices': ['cleartext', 'dot', 'doh'], 'elements': 'str'},
                'eap-ca-cert': {'v_range': [['7.2.0', '']], 'type': 'str'},
                'eap-identity': {'v_range': [['7.2.0', '']], 'type': 'str'},
                'eap-method': {'v_range': [['7.2.0', '']], 'choices': ['tls', 'peap'], 'type': 'str'},
                'eap-password': {'v_range': [['7.2.0', '']], 'no_log': True, 'type': 'raw'},
                'eap-supplicant': {'v_range': [['7.2.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'eap-user-cert': {'v_range': [['7.2.0', '']], 'type': 'str'},
                'ike-saml-server': {'v_range': [['7.2.0', '']], 'type': 'str'},
                'lacp-ha-secondary': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'pvc-atm-qos': {'v_range': [['6.4.8', '6.4.14'], ['7.0.2', '']], 'choices': ['cbr', 'rt-vbr', 'nrt-vbr', 'ubr'], 'type': 'str'},
                'pvc-chan': {'v_range': [['6.4.8', '6.4.14'], ['7.0.2', '']], 'type': 'int'},
                'pvc-crc': {'v_range': [['6.4.8', '6.4.14'], ['7.0.2', '']], 'type': 'int'},
                'pvc-pcr': {'v_range': [['6.4.8', '6.4.14'], ['7.0.2', '']], 'type': 'int'},
                'pvc-scr': {'v_range': [['6.4.8', '6.4.14'], ['7.0.2', '']], 'type': 'int'},
                'pvc-vlan-id': {'v_range': [['6.4.8', '6.4.14'], ['7.0.2', '']], 'type': 'int'},
                'pvc-vlan-rx-id': {'v_range': [['6.4.8', '6.4.14'], ['7.0.2', '']], 'type': 'int'},
                'pvc-vlan-rx-op': {'v_range': [['6.4.8', '6.4.14'], ['7.0.2', '']], 'choices': ['pass-through', 'replace', 'remove'], 'type': 'str'},
                'pvc-vlan-tx-id': {'v_range': [['6.4.8', '6.4.14'], ['7.0.2', '']], 'type': 'int'},
                'pvc-vlan-tx-op': {'v_range': [['6.4.8', '6.4.14'], ['7.0.2', '']], 'choices': ['pass-through', 'replace', 'remove'], 'type': 'str'},
                'reachable-time': {'v_range': [['7.0.3', '']], 'type': 'int'},
                'select-profile-30a-35b': {'v_range': [['6.2.9', '6.2.12'], ['6.4.8', '6.4.14'], ['7.0.3', '']], 'choices': ['30A', '35B'], 'type': 'str'},
                'sfp-dsl': {'v_range': [['6.4.8', '6.4.14'], ['7.0.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'sfp-dsl-adsl-fallback': {'v_range': [['6.4.8', '6.4.14'], ['7.0.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'sfp-dsl-autodetect': {'v_range': [['6.4.8', '6.4.14'], ['7.0.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'sfp-dsl-mac': {'v_range': [['6.4.8', '6.4.14'], ['7.0.2', '']], 'type': 'str'},
                'sw-algorithm': {'v_range': [['7.0.1', '']], 'choices': ['l2', 'l3', 'eh', 'default'], 'type': 'str'},
                'system-id': {'v_range': [['6.4.7', '6.4.14'], ['7.0.2', '']], 'type': 'str'},
                'system-id-type': {'v_range': [['6.4.7', '6.4.14'], ['7.0.2', '']], 'choices': ['auto', 'user'], 'type': 'str'},
                'vlan-id': {'v_range': [['6.2.9', '6.2.12'], ['6.4.8', '6.4.14'], ['7.0.3', '']], 'type': 'int'},
                'vlan-op-mode': {
                    'v_range': [['6.2.9', '6.2.12'], ['6.4.8', '6.4.14'], ['7.0.3', '']],
                    'choices': ['tag', 'untag', 'passthrough'],
                    'type': 'str'
                },
                'generic-receive-offload': {'v_range': [['7.0.5', '7.0.12'], ['7.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'interconnect-profile': {'v_range': [['7.0.5', '7.0.12'], ['7.2.1', '']], 'choices': ['default', 'profile1', 'profile2'], 'type': 'str'},
                'large-receive-offload': {'v_range': [['7.0.5', '7.0.12'], ['7.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'annex': {
                    'v_range': [['7.0.10', '7.0.12'], ['7.2.5', '7.2.5'], ['7.4.2', '']],
                    'choices': ['a', 'b', 'j', 'bjm', 'i', 'al', 'm', 'aijlm', 'bj'],
                    'type': 'str'
                },
                'aggregate-type': {'v_range': [['7.2.1', '']], 'choices': ['physical', 'vxlan'], 'type': 'str'},
                'switch-controller-netflow-collect': {'v_range': [['7.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'wifi-dns-server1': {'v_range': [['7.2.2', '']], 'type': 'str'},
                'wifi-dns-server2': {'v_range': [['7.2.2', '']], 'type': 'str'},
                'wifi-gateway': {'v_range': [['7.2.2', '']], 'type': 'str'},
                'default-purdue-level': {'v_range': [['7.4.0', '']], 'choices': ['1', '2', '3', '4', '5', '1.5', '2.5', '3.5', '5.5'], 'type': 'str'},
                'dhcp-broadcast-flag': {'v_range': [['7.4.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'dhcp-smart-relay': {'v_range': [['7.4.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'switch-controller-offloading': {'v_range': [['7.4.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'switch-controller-offloading-gw': {'v_range': [['7.4.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'switch-controller-offloading-ip': {'v_range': [['7.4.0', '']], 'type': 'str'},
                'dhcp-relay-circuit-id': {'v_range': [['7.4.1', '']], 'type': 'str'},
                'dhcp-relay-source-ip': {'v_range': [['7.4.1', '']], 'type': 'str'},
                'switch-controller-offload': {'v_range': [['7.4.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'switch-controller-offload-gw': {'v_range': [['7.4.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'switch-controller-offload-ip': {'v_range': [['7.4.1', '']], 'type': 'str'},
                'mirroring-direction': {'v_range': [['7.4.2', '']], 'choices': ['rx', 'tx', 'both'], 'type': 'str'},
                'mirroring-port': {'v_range': [['7.4.2', '']], 'type': 'str'},
                'port-mirroring': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'security-8021x-member-mode': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'switch'], 'type': 'str'},
                'stp-edge': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'dhcp-relay-allow-no-end-option': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'netflow-sample-rate': {'v_range': [['7.6.0', '']], 'type': 'int'},
                'netflow-sampler-id': {'v_range': [['7.6.0', '']], 'type': 'int'},
                'pppoe-egress-cos': {
                    'v_range': [['7.6.0', '']],
                    'choices': ['cos0', 'cos1', 'cos2', 'cos3', 'cos4', 'cos5', 'cos6', 'cos7'],
                    'type': 'str'
                },
                'security-ip-auth-bypass': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'virtual-mac': {'v_range': [['7.6.0', '']], 'type': 'str'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('partial crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'fsp_vlan_interface'),
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
