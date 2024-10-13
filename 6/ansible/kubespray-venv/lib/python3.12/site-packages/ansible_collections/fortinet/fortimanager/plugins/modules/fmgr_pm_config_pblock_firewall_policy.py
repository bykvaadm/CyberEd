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
module: fmgr_pm_config_pblock_firewall_policy
short_description: Configure IPv4/IPv6 policies.
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
    pblock:
        description: The parameter (pblock) in requested url.
        type: str
        required: true
    pm_config_pblock_firewall_policy:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            _policy_block:
                type: int
                description: Assigned policy block.
            action:
                type: str
                description: Policy action
                choices:
                    - 'deny'
                    - 'accept'
                    - 'ipsec'
                    - 'ssl-vpn'
                    - 'redirect'
                    - 'isolate'
            anti-replay:
                type: str
                description: Deprecated, please rename it to anti_replay. Enable/disable anti-replay check.
                choices:
                    - 'disable'
                    - 'enable'
            application-list:
                type: str
                description: Deprecated, please rename it to application_list. Name of an existing Application list.
            auth-cert:
                type: str
                description: Deprecated, please rename it to auth_cert. HTTPS server certificate for policy authentication.
            auth-path:
                type: str
                description: Deprecated, please rename it to auth_path. Enable/disable authentication-based routing.
                choices:
                    - 'disable'
                    - 'enable'
            auth-redirect-addr:
                type: str
                description: Deprecated, please rename it to auth_redirect_addr. HTTP-to-HTTPS redirect address for firewall authentication.
            auto-asic-offload:
                type: str
                description: Deprecated, please rename it to auto_asic_offload. Enable/disable policy traffic ASIC offloading.
                choices:
                    - 'disable'
                    - 'enable'
            av-profile:
                type: str
                description: Deprecated, please rename it to av_profile. Name of an existing Antivirus profile.
            block-notification:
                type: str
                description: Deprecated, please rename it to block_notification. Enable/disable block notification.
                choices:
                    - 'disable'
                    - 'enable'
            captive-portal-exempt:
                type: str
                description: Deprecated, please rename it to captive_portal_exempt. Enable to exempt some users from the captive portal.
                choices:
                    - 'disable'
                    - 'enable'
            capture-packet:
                type: str
                description: Deprecated, please rename it to capture_packet. Enable/disable capture packets.
                choices:
                    - 'disable'
                    - 'enable'
            cifs-profile:
                type: str
                description: Deprecated, please rename it to cifs_profile. Name of an existing CIFS profile.
            comments:
                type: str
                description: Comment.
            custom-log-fields:
                type: raw
                description: (list) Deprecated, please rename it to custom_log_fields. Custom fields to append to log messages for this policy.
            decrypted-traffic-mirror:
                type: str
                description: Deprecated, please rename it to decrypted_traffic_mirror. Decrypted traffic mirror.
            delay-tcp-npu-session:
                type: str
                description: Deprecated, please rename it to delay_tcp_npu_session. Enable TCP NPU session delay to guarantee packet order of 3-way han...
                choices:
                    - 'disable'
                    - 'enable'
            diffserv-forward:
                type: str
                description: Deprecated, please rename it to diffserv_forward. Enable to change packets DiffServ values to the specified diffservcode-f...
                choices:
                    - 'disable'
                    - 'enable'
            diffserv-reverse:
                type: str
                description: Deprecated, please rename it to diffserv_reverse. Enable to change packets reverse
                choices:
                    - 'disable'
                    - 'enable'
            diffservcode-forward:
                type: str
                description: Deprecated, please rename it to diffservcode_forward. Change packets DiffServ to this value.
            diffservcode-rev:
                type: str
                description: Deprecated, please rename it to diffservcode_rev. Change packets reverse
            disclaimer:
                type: str
                description: Enable/disable user authentication disclaimer.
                choices:
                    - 'disable'
                    - 'enable'
                    - 'user'
                    - 'domain'
                    - 'policy'
            dlp-profile:
                type: str
                description: Deprecated, please rename it to dlp_profile. Name of an existing DLP profile.
            dnsfilter-profile:
                type: str
                description: Deprecated, please rename it to dnsfilter_profile. Name of an existing DNS filter profile.
            dsri:
                type: str
                description: Enable DSRI to ignore HTTP server responses.
                choices:
                    - 'disable'
                    - 'enable'
            dstaddr:
                type: raw
                description: (list) Destination IPv4 address and address group names.
            dstaddr-negate:
                type: str
                description: Deprecated, please rename it to dstaddr_negate. When enabled dstaddr/dstaddr6 specifies what the destination address must ...
                choices:
                    - 'disable'
                    - 'enable'
            dstaddr6:
                type: raw
                description: (list) Destination IPv6 address name and address group names.
            dstintf:
                type: raw
                description: (list) Outgoing
            dynamic-shaping:
                type: str
                description: Deprecated, please rename it to dynamic_shaping. Enable/disable dynamic RADIUS defined traffic shaping.
                choices:
                    - 'disable'
                    - 'enable'
            email-collect:
                type: str
                description: Deprecated, please rename it to email_collect. Enable/disable email collection.
                choices:
                    - 'disable'
                    - 'enable'
            emailfilter-profile:
                type: str
                description: Deprecated, please rename it to emailfilter_profile. Name of an existing email filter profile.
            fec:
                type: str
                description: Enable/disable Forward Error Correction on traffic matching this policy on a FEC device.
                choices:
                    - 'disable'
                    - 'enable'
            file-filter-profile:
                type: str
                description: Deprecated, please rename it to file_filter_profile. Name of an existing file-filter profile.
            firewall-session-dirty:
                type: str
                description: Deprecated, please rename it to firewall_session_dirty. How to handle sessions if the configuration of this firewall polic...
                choices:
                    - 'check-all'
                    - 'check-new'
            fixedport:
                type: str
                description: Enable to prevent source NAT from changing a sessions source port.
                choices:
                    - 'disable'
                    - 'enable'
            fsso-agent-for-ntlm:
                type: str
                description: Deprecated, please rename it to fsso_agent_for_ntlm. FSSO agent to use for NTLM authentication.
            fsso-groups:
                type: raw
                description: (list) Deprecated, please rename it to fsso_groups. Names of FSSO groups.
            geoip-anycast:
                type: str
                description: Deprecated, please rename it to geoip_anycast. Enable/disable recognition of anycast IP addresses using the geography IP d...
                choices:
                    - 'disable'
                    - 'enable'
            geoip-match:
                type: str
                description: Deprecated, please rename it to geoip_match. Match geography address based either on its physical location or registered l...
                choices:
                    - 'physical-location'
                    - 'registered-location'
            global-label:
                type: str
                description: Deprecated, please rename it to global_label. Label for the policy that appears when the GUI is in Global View mode.
            groups:
                type: raw
                description: (list) Names of user groups that can authenticate with this policy.
            gtp-profile:
                type: str
                description: Deprecated, please rename it to gtp_profile. GTP profile.
            http-policy-redirect:
                type: str
                description: Deprecated, please rename it to http_policy_redirect. Redirect HTTP
                choices:
                    - 'disable'
                    - 'enable'
            icap-profile:
                type: str
                description: Deprecated, please rename it to icap_profile. Name of an existing ICAP profile.
            identity-based-route:
                type: str
                description: Deprecated, please rename it to identity_based_route. Name of identity-based routing rule.
            inbound:
                type: str
                description: Policy-based IPsec VPN
                choices:
                    - 'disable'
                    - 'enable'
            inspection-mode:
                type: str
                description: Deprecated, please rename it to inspection_mode. Policy inspection mode
                choices:
                    - 'proxy'
                    - 'flow'
            internet-service:
                type: str
                description: Deprecated, please rename it to internet_service. Enable/disable use of Internet Services for this policy.
                choices:
                    - 'disable'
                    - 'enable'
            internet-service-custom:
                type: raw
                description: (list) Deprecated, please rename it to internet_service_custom. Custom Internet Service name.
            internet-service-custom-group:
                type: raw
                description: (list) Deprecated, please rename it to internet_service_custom_group. Custom Internet Service group name.
            internet-service-group:
                type: raw
                description: (list) Deprecated, please rename it to internet_service_group. Internet Service group name.
            internet-service-name:
                type: raw
                description: (list) Deprecated, please rename it to internet_service_name. Internet Service name.
            internet-service-negate:
                type: str
                description: Deprecated, please rename it to internet_service_negate. When enabled internet-service specifies what the service must NOT be.
                choices:
                    - 'disable'
                    - 'enable'
            internet-service-src:
                type: str
                description: Deprecated, please rename it to internet_service_src. Enable/disable use of Internet Services in source for this policy.
                choices:
                    - 'disable'
                    - 'enable'
            internet-service-src-custom:
                type: raw
                description: (list) Deprecated, please rename it to internet_service_src_custom. Custom Internet Service source name.
            internet-service-src-custom-group:
                type: raw
                description: (list) Deprecated, please rename it to internet_service_src_custom_group. Custom Internet Service source group name.
            internet-service-src-group:
                type: raw
                description: (list) Deprecated, please rename it to internet_service_src_group. Internet Service source group name.
            internet-service-src-name:
                type: raw
                description: (list) Deprecated, please rename it to internet_service_src_name. Internet Service source name.
            internet-service-src-negate:
                type: str
                description: Deprecated, please rename it to internet_service_src_negate. When enabled internet-service-src specifies what the service ...
                choices:
                    - 'disable'
                    - 'enable'
            ippool:
                type: str
                description: Enable to use IP Pools for source NAT.
                choices:
                    - 'disable'
                    - 'enable'
            ips-sensor:
                type: str
                description: Deprecated, please rename it to ips_sensor. Name of an existing IPS sensor.
            label:
                type: str
                description: Label for the policy that appears when the GUI is in Section View mode.
            logtraffic:
                type: str
                description: Enable or disable logging.
                choices:
                    - 'disable'
                    - 'enable'
                    - 'all'
                    - 'utm'
            logtraffic-start:
                type: str
                description: Deprecated, please rename it to logtraffic_start. Record logs when a session starts.
                choices:
                    - 'disable'
                    - 'enable'
            match-vip:
                type: str
                description: Deprecated, please rename it to match_vip. Enable to match packets that have had their destination addresses changed by a VIP.
                choices:
                    - 'disable'
                    - 'enable'
            match-vip-only:
                type: str
                description: Deprecated, please rename it to match_vip_only. Enable/disable matching of only those packets that have had their destinat...
                choices:
                    - 'disable'
                    - 'enable'
            name:
                type: str
                description: Policy name.
            nat:
                type: str
                description: Enable/disable source NAT.
                choices:
                    - 'disable'
                    - 'enable'
            nat46:
                type: str
                description: Enable/disable NAT46.
                choices:
                    - 'disable'
                    - 'enable'
            nat64:
                type: str
                description: Enable/disable NAT64.
                choices:
                    - 'disable'
                    - 'enable'
            natinbound:
                type: str
                description: Policy-based IPsec VPN
                choices:
                    - 'disable'
                    - 'enable'
            natip:
                type: str
                description: Policy-based IPsec VPN
            natoutbound:
                type: str
                description: Policy-based IPsec VPN
                choices:
                    - 'disable'
                    - 'enable'
            np-acceleration:
                type: str
                description: Deprecated, please rename it to np_acceleration. Enable/disable UTM Network Processor acceleration.
                choices:
                    - 'disable'
                    - 'enable'
            ntlm:
                type: str
                description: Enable/disable NTLM authentication.
                choices:
                    - 'disable'
                    - 'enable'
            ntlm-enabled-browsers:
                type: raw
                description: (list) Deprecated, please rename it to ntlm_enabled_browsers. HTTP-User-Agent value of supported browsers.
            ntlm-guest:
                type: str
                description: Deprecated, please rename it to ntlm_guest. Enable/disable NTLM guest user access.
                choices:
                    - 'disable'
                    - 'enable'
            outbound:
                type: str
                description: Policy-based IPsec VPN
                choices:
                    - 'disable'
                    - 'enable'
            passive-wan-health-measurement:
                type: str
                description: Deprecated, please rename it to passive_wan_health_measurement. Enable/disable passive WAN health measurement.
                choices:
                    - 'disable'
                    - 'enable'
            per-ip-shaper:
                type: str
                description: Deprecated, please rename it to per_ip_shaper. Per-IP traffic shaper.
            permit-any-host:
                type: str
                description: Deprecated, please rename it to permit_any_host. Accept UDP packets from any host.
                choices:
                    - 'disable'
                    - 'enable'
            permit-stun-host:
                type: str
                description: Deprecated, please rename it to permit_stun_host. Accept UDP packets from any Session Traversal Utilities for NAT
                choices:
                    - 'disable'
                    - 'enable'
            pfcp-profile:
                type: str
                description: Deprecated, please rename it to pfcp_profile. PFCP profile.
            policy-expiry:
                type: str
                description: Deprecated, please rename it to policy_expiry. Enable/disable policy expiry.
                choices:
                    - 'disable'
                    - 'enable'
            policy-expiry-date:
                type: str
                description: Deprecated, please rename it to policy_expiry_date. Policy expiry date
            policyid:
                type: int
                description: Policy ID
                required: true
            poolname:
                type: raw
                description: (list) IP Pool names.
            poolname6:
                type: raw
                description: (list) IPv6 pool names.
            profile-group:
                type: str
                description: Deprecated, please rename it to profile_group. Name of profile group.
            profile-protocol-options:
                type: str
                description: Deprecated, please rename it to profile_protocol_options. Name of an existing Protocol options profile.
            profile-type:
                type: str
                description: Deprecated, please rename it to profile_type. Determine whether the firewall policy allows security profile groups or sing...
                choices:
                    - 'single'
                    - 'group'
            radius-mac-auth-bypass:
                type: str
                description: Deprecated, please rename it to radius_mac_auth_bypass. Enable MAC authentication bypass.
                choices:
                    - 'disable'
                    - 'enable'
            redirect-url:
                type: str
                description: Deprecated, please rename it to redirect_url. URL users are directed to after seeing and accepting the disclaimer or authe...
            replacemsg-override-group:
                type: str
                description: Deprecated, please rename it to replacemsg_override_group. Override the default replacement message group for this policy.
            reputation-direction:
                type: str
                description: Deprecated, please rename it to reputation_direction. Direction of the initial traffic for reputation to take effect.
                choices:
                    - 'source'
                    - 'destination'
            reputation-minimum:
                type: int
                description: Deprecated, please rename it to reputation_minimum. Minimum Reputation to take action.
            rtp-addr:
                type: raw
                description: (list) Deprecated, please rename it to rtp_addr. Address names if this is an RTP NAT policy.
            rtp-nat:
                type: str
                description: Deprecated, please rename it to rtp_nat. Enable Real Time Protocol
                choices:
                    - 'disable'
                    - 'enable'
            schedule:
                type: str
                description: Schedule name.
            schedule-timeout:
                type: str
                description: Deprecated, please rename it to schedule_timeout. Enable to force current sessions to end when the schedule object times out.
                choices:
                    - 'disable'
                    - 'enable'
            sctp-filter-profile:
                type: str
                description: Deprecated, please rename it to sctp_filter_profile. Name of an existing SCTP filter profile.
            send-deny-packet:
                type: str
                description: Deprecated, please rename it to send_deny_packet. Enable to send a reply when a session is denied or blocked by a firewall...
                choices:
                    - 'disable'
                    - 'enable'
            service:
                type: raw
                description: (list) Service and service group names.
            service-negate:
                type: str
                description: Deprecated, please rename it to service_negate. When enabled service specifies what the service must NOT be.
                choices:
                    - 'disable'
                    - 'enable'
            session-ttl:
                type: raw
                description: (int or str) Deprecated, please rename it to session_ttl. TTL in seconds for sessions accepted by this policy
            sgt:
                type: raw
                description: (list) Security group tags.
            sgt-check:
                type: str
                description: Deprecated, please rename it to sgt_check. Enable/disable security group tags
                choices:
                    - 'disable'
                    - 'enable'
            src-vendor-mac:
                type: raw
                description: (list) Deprecated, please rename it to src_vendor_mac. Vendor MAC source ID.
            srcaddr:
                type: raw
                description: (list) Source IPv4 address and address group names.
            srcaddr-negate:
                type: str
                description: Deprecated, please rename it to srcaddr_negate. When enabled srcaddr/srcaddr6 specifies what the source address must NOT be.
                choices:
                    - 'disable'
                    - 'enable'
            srcaddr6:
                type: raw
                description: (list) Source IPv6 address name and address group names.
            srcintf:
                type: raw
                description: (list) Incoming
            ssh-filter-profile:
                type: str
                description: Deprecated, please rename it to ssh_filter_profile. Name of an existing SSH filter profile.
            ssh-policy-redirect:
                type: str
                description: Deprecated, please rename it to ssh_policy_redirect. Redirect SSH traffic to matching transparent proxy policy.
                choices:
                    - 'disable'
                    - 'enable'
            ssl-ssh-profile:
                type: str
                description: Deprecated, please rename it to ssl_ssh_profile. Name of an existing SSL SSH profile.
            status:
                type: str
                description: Enable or disable this policy.
                choices:
                    - 'disable'
                    - 'enable'
            tcp-mss-receiver:
                type: int
                description: Deprecated, please rename it to tcp_mss_receiver. Receiver TCP maximum segment size
            tcp-mss-sender:
                type: int
                description: Deprecated, please rename it to tcp_mss_sender. Sender TCP maximum segment size
            tcp-session-without-syn:
                type: str
                description: Deprecated, please rename it to tcp_session_without_syn. Enable/disable creation of TCP session without SYN flag.
                choices:
                    - 'all'
                    - 'data-only'
                    - 'disable'
            timeout-send-rst:
                type: str
                description: Deprecated, please rename it to timeout_send_rst. Enable/disable sending RST packets when TCP sessions expire.
                choices:
                    - 'disable'
                    - 'enable'
            tos:
                type: str
                description: ToS
            tos-mask:
                type: str
                description: Deprecated, please rename it to tos_mask. Non-zero bit positions are used for comparison while zero bit positions are ignored.
            tos-negate:
                type: str
                description: Deprecated, please rename it to tos_negate. Enable negated TOS match.
                choices:
                    - 'disable'
                    - 'enable'
            traffic-shaper:
                type: str
                description: Deprecated, please rename it to traffic_shaper. Traffic shaper.
            traffic-shaper-reverse:
                type: str
                description: Deprecated, please rename it to traffic_shaper_reverse. Reverse traffic shaper.
            users:
                type: raw
                description: (list) Names of individual users that can authenticate with this policy.
            utm-status:
                type: str
                description: Deprecated, please rename it to utm_status. Enable to add one or more security profiles
                choices:
                    - 'disable'
                    - 'enable'
            uuid:
                type: str
                description: Universally Unique Identifier
            videofilter-profile:
                type: str
                description: Deprecated, please rename it to videofilter_profile. Name of an existing VideoFilter profile.
            vlan-cos-fwd:
                type: int
                description: Deprecated, please rename it to vlan_cos_fwd. VLAN forward direction user priority
            vlan-cos-rev:
                type: int
                description: Deprecated, please rename it to vlan_cos_rev. VLAN reverse direction user priority
            vlan-filter:
                type: str
                description: Deprecated, please rename it to vlan_filter. Set VLAN filters.
            voip-profile:
                type: str
                description: Deprecated, please rename it to voip_profile. Name of an existing VoIP profile.
            vpntunnel:
                type: str
                description: Policy-based IPsec VPN
            waf-profile:
                type: str
                description: Deprecated, please rename it to waf_profile. Name of an existing Web application firewall profile.
            wanopt:
                type: str
                description: Enable/disable WAN optimization.
                choices:
                    - 'disable'
                    - 'enable'
            wanopt-detection:
                type: str
                description: Deprecated, please rename it to wanopt_detection. WAN optimization auto-detection mode.
                choices:
                    - 'active'
                    - 'passive'
                    - 'off'
            wanopt-passive-opt:
                type: str
                description: Deprecated, please rename it to wanopt_passive_opt. WAN optimization passive mode options.
                choices:
                    - 'default'
                    - 'transparent'
                    - 'non-transparent'
            wanopt-peer:
                type: str
                description: Deprecated, please rename it to wanopt_peer. WAN optimization peer.
            wanopt-profile:
                type: str
                description: Deprecated, please rename it to wanopt_profile. WAN optimization profile.
            wccp:
                type: str
                description: Enable/disable forwarding traffic matching this policy to a configured WCCP server.
                choices:
                    - 'disable'
                    - 'enable'
            webcache:
                type: str
                description: Enable/disable web cache.
                choices:
                    - 'disable'
                    - 'enable'
            webcache-https:
                type: str
                description: Deprecated, please rename it to webcache_https. Enable/disable web cache for HTTPS.
                choices:
                    - 'disable'
                    - 'ssl-server'
                    - 'any'
                    - 'enable'
            webfilter-profile:
                type: str
                description: Deprecated, please rename it to webfilter_profile. Name of an existing Web filter profile.
            webproxy-forward-server:
                type: str
                description: Deprecated, please rename it to webproxy_forward_server. Webproxy forward server name.
            webproxy-profile:
                type: str
                description: Deprecated, please rename it to webproxy_profile. Webproxy profile name.
            ztna-ems-tag:
                type: raw
                description: (list) Deprecated, please rename it to ztna_ems_tag. Source ztna-ems-tag names.
            ztna-geo-tag:
                type: raw
                description: (list) Deprecated, please rename it to ztna_geo_tag. Source ztna-geo-tag names.
            ztna-status:
                type: str
                description: Deprecated, please rename it to ztna_status. Enable/disable zero trust access.
                choices:
                    - 'disable'
                    - 'enable'
            policy-offload:
                type: str
                description: Deprecated, please rename it to policy_offload. Enable/Disable hardware session setup for CGNAT.
                choices:
                    - 'disable'
                    - 'enable'
            cgn-session-quota:
                type: int
                description: Deprecated, please rename it to cgn_session_quota. Session quota
            tcp-timeout-pid:
                type: str
                description: Deprecated, please rename it to tcp_timeout_pid. TCP timeout profile ID
            udp-timeout-pid:
                type: str
                description: Deprecated, please rename it to udp_timeout_pid. UDP timeout profile ID
            dlp-sensor:
                type: str
                description: Deprecated, please rename it to dlp_sensor. Name of an existing DLP sensor.
            cgn-eif:
                type: str
                description: Deprecated, please rename it to cgn_eif. Enable/Disable CGN endpoint independent filtering.
                choices:
                    - 'disable'
                    - 'enable'
            cgn-log-server-grp:
                type: str
                description: Deprecated, please rename it to cgn_log_server_grp. NP log server group name
            cgn-resource-quota:
                type: int
                description: Deprecated, please rename it to cgn_resource_quota. Resource quota
            cgn-eim:
                type: str
                description: Deprecated, please rename it to cgn_eim. Enable/Disable CGN endpoint independent mapping
                choices:
                    - 'disable'
                    - 'enable'
            mms-profile:
                type: str
                description: Deprecated, please rename it to mms_profile. Name of an existing MMS profile.
            app-category:
                type: raw
                description: (list) Deprecated, please rename it to app_category. Application category ID list.
            internet-service-src-id:
                type: raw
                description: (list) Deprecated, please rename it to internet_service_src_id. Internet Service source ID.
            rsso:
                type: str
                description: Enable/disable RADIUS single sign-on
                choices:
                    - 'disable'
                    - 'enable'
            internet-service-id:
                type: raw
                description: (list) Deprecated, please rename it to internet_service_id. Internet Service ID.
            best-route:
                type: str
                description: Deprecated, please rename it to best_route. Best route.
                choices:
                    - 'disable'
                    - 'enable'
            fsso:
                type: str
                description: Enable/disable Fortinet Single Sign-On.
                choices:
                    - 'disable'
                    - 'enable'
            url-category:
                type: raw
                description: (list) Deprecated, please rename it to url_category. URL category ID list.
            app-group:
                type: raw
                description: (list) Deprecated, please rename it to app_group. Application group names.
            ssl-mirror-intf:
                type: raw
                description: (list) Deprecated, please rename it to ssl_mirror_intf. SSL mirror interface name.
            wsso:
                type: str
                description: Enable/disable WiFi Single Sign On
                choices:
                    - 'disable'
                    - 'enable'
            ssl-mirror:
                type: str
                description: Deprecated, please rename it to ssl_mirror. Enable to copy decrypted SSL traffic to a FortiGate interface
                choices:
                    - 'disable'
                    - 'enable'
            application:
                type: raw
                description: (list) Application ID list.
            dscp-negate:
                type: str
                description: Deprecated, please rename it to dscp_negate. Enable negated DSCP match.
                choices:
                    - 'disable'
                    - 'enable'
            learning-mode:
                type: str
                description: Deprecated, please rename it to learning_mode. Enable to allow everything, but log all of the meaningful data for security...
                choices:
                    - 'disable'
                    - 'enable'
            devices:
                type: raw
                description: (list) Names of devices or device groups that can be matched by the policy.
            dscp-value:
                type: str
                description: Deprecated, please rename it to dscp_value. DSCP value.
            spamfilter-profile:
                type: str
                description: Deprecated, please rename it to spamfilter_profile. Name of an existing Spam filter profile.
            scan-botnet-connections:
                type: str
                description: Deprecated, please rename it to scan_botnet_connections. Block or monitor connections to Botnet servers or disable Botnet ...
                choices:
                    - 'disable'
                    - 'block'
                    - 'monitor'
            dscp-match:
                type: str
                description: Deprecated, please rename it to dscp_match. Enable DSCP check.
                choices:
                    - 'disable'
                    - 'enable'
            diffserv-copy:
                type: str
                description: Deprecated, please rename it to diffserv_copy. Enable to copy packets DiffServ values from sessions original direction to ...
                choices:
                    - 'disable'
                    - 'enable'
            dstaddr6-negate:
                type: str
                description: Deprecated, please rename it to dstaddr6_negate. When enabled dstaddr6 specifies what the destination address must NOT be.
                choices:
                    - 'disable'
                    - 'enable'
            internet-service6:
                type: str
                description: Deprecated, please rename it to internet_service6. Enable/disable use of IPv6 Internet Services for this policy.
                choices:
                    - 'disable'
                    - 'enable'
            internet-service6-custom:
                type: raw
                description: (list) Deprecated, please rename it to internet_service6_custom. Custom IPv6 Internet Service name.
            internet-service6-custom-group:
                type: raw
                description: (list) Deprecated, please rename it to internet_service6_custom_group. Custom Internet Service6 group name.
            internet-service6-group:
                type: raw
                description: (list) Deprecated, please rename it to internet_service6_group. Internet Service group name.
            internet-service6-name:
                type: raw
                description: (list) Deprecated, please rename it to internet_service6_name. IPv6 Internet Service name.
            internet-service6-negate:
                type: str
                description: Deprecated, please rename it to internet_service6_negate. When enabled internet-service6 specifies what the service must N...
                choices:
                    - 'disable'
                    - 'enable'
            internet-service6-src:
                type: str
                description: Deprecated, please rename it to internet_service6_src. Enable/disable use of IPv6 Internet Services in source for this policy.
                choices:
                    - 'disable'
                    - 'enable'
            internet-service6-src-custom:
                type: raw
                description: (list) Deprecated, please rename it to internet_service6_src_custom. Custom IPv6 Internet Service source name.
            internet-service6-src-custom-group:
                type: raw
                description: (list) Deprecated, please rename it to internet_service6_src_custom_group. Custom Internet Service6 source group name.
            internet-service6-src-group:
                type: raw
                description: (list) Deprecated, please rename it to internet_service6_src_group. Internet Service6 source group name.
            internet-service6-src-name:
                type: raw
                description: (list) Deprecated, please rename it to internet_service6_src_name. IPv6 Internet Service source name.
            internet-service6-src-negate:
                type: str
                description: Deprecated, please rename it to internet_service6_src_negate. When enabled internet-service6-src specifies what the servic...
                choices:
                    - 'disable'
                    - 'enable'
            network-service-dynamic:
                type: raw
                description: (list) Deprecated, please rename it to network_service_dynamic. Dynamic Network Service name.
            network-service-src-dynamic:
                type: raw
                description: (list) Deprecated, please rename it to network_service_src_dynamic. Dynamic Network Service source name.
            reputation-direction6:
                type: str
                description: Deprecated, please rename it to reputation_direction6. Direction of the initial traffic for IPv6 reputation to take effect.
                choices:
                    - 'source'
                    - 'destination'
            reputation-minimum6:
                type: int
                description: Deprecated, please rename it to reputation_minimum6. IPv6 Minimum Reputation to take action.
            srcaddr6-negate:
                type: str
                description: Deprecated, please rename it to srcaddr6_negate. When enabled srcaddr6 specifies what the source address must NOT be.
                choices:
                    - 'disable'
                    - 'enable'
            ip-version-type:
                type: str
                description: Deprecated, please rename it to ip_version_type. IP version of the policy.
            ips-voip-filter:
                type: str
                description: Deprecated, please rename it to ips_voip_filter. Name of an existing VoIP
            pcp-inbound:
                type: str
                description: Deprecated, please rename it to pcp_inbound. Enable/disable PCP inbound DNAT.
                choices:
                    - 'disable'
                    - 'enable'
            pcp-outbound:
                type: str
                description: Deprecated, please rename it to pcp_outbound. Enable/disable PCP outbound SNAT.
                choices:
                    - 'disable'
                    - 'enable'
            pcp-poolname:
                type: raw
                description: (list) Deprecated, please rename it to pcp_poolname. PCP pool names.
            policy-behaviour-type:
                type: str
                description: Deprecated, please rename it to policy_behaviour_type. Behaviour of the policy.
            policy-expiry-date-utc:
                type: str
                description: Deprecated, please rename it to policy_expiry_date_utc. Policy expiry date and time, in epoch format.
            ztna-device-ownership:
                type: str
                description: Deprecated, please rename it to ztna_device_ownership. Enable/disable zero trust device ownership.
                choices:
                    - 'disable'
                    - 'enable'
            ztna-ems-tag-secondary:
                type: raw
                description: (list) Deprecated, please rename it to ztna_ems_tag_secondary. Source ztna-ems-tag-secondary names.
            ztna-policy-redirect:
                type: str
                description: Deprecated, please rename it to ztna_policy_redirect. Redirect ZTNA traffic to matching Access-Proxy proxy-policy.
                choices:
                    - 'disable'
                    - 'enable'
            ztna-tags-match-logic:
                type: str
                description: Deprecated, please rename it to ztna_tags_match_logic. ZTNA tag matching logic.
                choices:
                    - 'or'
                    - 'and'
            casb-profile:
                type: str
                description: Deprecated, please rename it to casb_profile. Name of an existing CASB profile.
            virtual-patch-profile:
                type: str
                description: Deprecated, please rename it to virtual_patch_profile. Name of an existing virtual-patch profile.
            diameter-filter-profile:
                type: str
                description: Deprecated, please rename it to diameter_filter_profile. Name of an existing Diameter filter profile.
            port-preserve:
                type: str
                description: Deprecated, please rename it to port_preserve. Enable/disable preservation of the original source port from source NAT if ...
                choices:
                    - 'disable'
                    - 'enable'
            cgn-sw-eif-ctrl:
                type: str
                description: Deprecated, please rename it to cgn_sw_eif_ctrl. Enable/disable software endpoint independent filtering control.
                choices:
                    - 'disable'
                    - 'enable'
            eif-check:
                type: str
                description: Deprecated, please rename it to eif_check. Enable/Disable check endpoint-independent-filtering pinhole.
                choices:
                    - 'disable'
                    - 'enable'
            eif-learn:
                type: str
                description: Deprecated, please rename it to eif_learn. Enable/Disable learning of end-point-independent filtering pinhole.
                choices:
                    - 'disable'
                    - 'enable'
            log-http-transaction:
                type: str
                description: Deprecated, please rename it to log_http_transaction. Enable/disable HTTP transaction log.
                choices:
                    - 'disable'
                    - 'enable'
                    - 'all'
                    - 'utm'
            radius-ip-auth-bypass:
                type: str
                description: Deprecated, please rename it to radius_ip_auth_bypass. Enable IP authentication bypass.
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
    - name: Configure IPv4/IPv6 policies.
      fortinet.fortimanager.fmgr_pm_config_pblock_firewall_policy:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        adom: <your own value>
        pblock: <your own value>
        state: present # <value in [present, absent]>
        pm_config_pblock_firewall_policy:
          _policy_block: <integer>
          action: <value in [deny, accept, ipsec, ...]>
          anti_replay: <value in [disable, enable]>
          application_list: <string>
          auth_cert: <string>
          auth_path: <value in [disable, enable]>
          auth_redirect_addr: <string>
          auto_asic_offload: <value in [disable, enable]>
          av_profile: <string>
          block_notification: <value in [disable, enable]>
          captive_portal_exempt: <value in [disable, enable]>
          capture_packet: <value in [disable, enable]>
          cifs_profile: <string>
          comments: <string>
          custom_log_fields: <list or string>
          decrypted_traffic_mirror: <string>
          delay_tcp_npu_session: <value in [disable, enable]>
          diffserv_forward: <value in [disable, enable]>
          diffserv_reverse: <value in [disable, enable]>
          diffservcode_forward: <string>
          diffservcode_rev: <string>
          disclaimer: <value in [disable, enable, user, ...]>
          dlp_profile: <string>
          dnsfilter_profile: <string>
          dsri: <value in [disable, enable]>
          dstaddr: <list or string>
          dstaddr_negate: <value in [disable, enable]>
          dstaddr6: <list or string>
          dstintf: <list or string>
          dynamic_shaping: <value in [disable, enable]>
          email_collect: <value in [disable, enable]>
          emailfilter_profile: <string>
          fec: <value in [disable, enable]>
          file_filter_profile: <string>
          firewall_session_dirty: <value in [check-all, check-new]>
          fixedport: <value in [disable, enable]>
          fsso_agent_for_ntlm: <string>
          fsso_groups: <list or string>
          geoip_anycast: <value in [disable, enable]>
          geoip_match: <value in [physical-location, registered-location]>
          global_label: <string>
          groups: <list or string>
          gtp_profile: <string>
          http_policy_redirect: <value in [disable, enable]>
          icap_profile: <string>
          identity_based_route: <string>
          inbound: <value in [disable, enable]>
          inspection_mode: <value in [proxy, flow]>
          internet_service: <value in [disable, enable]>
          internet_service_custom: <list or string>
          internet_service_custom_group: <list or string>
          internet_service_group: <list or string>
          internet_service_name: <list or string>
          internet_service_negate: <value in [disable, enable]>
          internet_service_src: <value in [disable, enable]>
          internet_service_src_custom: <list or string>
          internet_service_src_custom_group: <list or string>
          internet_service_src_group: <list or string>
          internet_service_src_name: <list or string>
          internet_service_src_negate: <value in [disable, enable]>
          ippool: <value in [disable, enable]>
          ips_sensor: <string>
          label: <string>
          logtraffic: <value in [disable, enable, all, ...]>
          logtraffic_start: <value in [disable, enable]>
          match_vip: <value in [disable, enable]>
          match_vip_only: <value in [disable, enable]>
          name: <string>
          nat: <value in [disable, enable]>
          nat46: <value in [disable, enable]>
          nat64: <value in [disable, enable]>
          natinbound: <value in [disable, enable]>
          natip: <string>
          natoutbound: <value in [disable, enable]>
          np_acceleration: <value in [disable, enable]>
          ntlm: <value in [disable, enable]>
          ntlm_enabled_browsers: <list or string>
          ntlm_guest: <value in [disable, enable]>
          outbound: <value in [disable, enable]>
          passive_wan_health_measurement: <value in [disable, enable]>
          per_ip_shaper: <string>
          permit_any_host: <value in [disable, enable]>
          permit_stun_host: <value in [disable, enable]>
          pfcp_profile: <string>
          policy_expiry: <value in [disable, enable]>
          policy_expiry_date: <string>
          policyid: <integer>
          poolname: <list or string>
          poolname6: <list or string>
          profile_group: <string>
          profile_protocol_options: <string>
          profile_type: <value in [single, group]>
          radius_mac_auth_bypass: <value in [disable, enable]>
          redirect_url: <string>
          replacemsg_override_group: <string>
          reputation_direction: <value in [source, destination]>
          reputation_minimum: <integer>
          rtp_addr: <list or string>
          rtp_nat: <value in [disable, enable]>
          schedule: <string>
          schedule_timeout: <value in [disable, enable]>
          sctp_filter_profile: <string>
          send_deny_packet: <value in [disable, enable]>
          service: <list or string>
          service_negate: <value in [disable, enable]>
          session_ttl: <integer or string>
          sgt: <list or integer>
          sgt_check: <value in [disable, enable]>
          src_vendor_mac: <list or string>
          srcaddr: <list or string>
          srcaddr_negate: <value in [disable, enable]>
          srcaddr6: <list or string>
          srcintf: <list or string>
          ssh_filter_profile: <string>
          ssh_policy_redirect: <value in [disable, enable]>
          ssl_ssh_profile: <string>
          status: <value in [disable, enable]>
          tcp_mss_receiver: <integer>
          tcp_mss_sender: <integer>
          tcp_session_without_syn: <value in [all, data-only, disable]>
          timeout_send_rst: <value in [disable, enable]>
          tos: <string>
          tos_mask: <string>
          tos_negate: <value in [disable, enable]>
          traffic_shaper: <string>
          traffic_shaper_reverse: <string>
          users: <list or string>
          utm_status: <value in [disable, enable]>
          uuid: <string>
          videofilter_profile: <string>
          vlan_cos_fwd: <integer>
          vlan_cos_rev: <integer>
          vlan_filter: <string>
          voip_profile: <string>
          vpntunnel: <string>
          waf_profile: <string>
          wanopt: <value in [disable, enable]>
          wanopt_detection: <value in [active, passive, off]>
          wanopt_passive_opt: <value in [default, transparent, non-transparent]>
          wanopt_peer: <string>
          wanopt_profile: <string>
          wccp: <value in [disable, enable]>
          webcache: <value in [disable, enable]>
          webcache_https: <value in [disable, ssl-server, any, ...]>
          webfilter_profile: <string>
          webproxy_forward_server: <string>
          webproxy_profile: <string>
          ztna_ems_tag: <list or string>
          ztna_geo_tag: <list or string>
          ztna_status: <value in [disable, enable]>
          policy_offload: <value in [disable, enable]>
          cgn_session_quota: <integer>
          tcp_timeout_pid: <string>
          udp_timeout_pid: <string>
          dlp_sensor: <string>
          cgn_eif: <value in [disable, enable]>
          cgn_log_server_grp: <string>
          cgn_resource_quota: <integer>
          cgn_eim: <value in [disable, enable]>
          mms_profile: <string>
          app_category: <list or string>
          internet_service_src_id: <list or string>
          rsso: <value in [disable, enable]>
          internet_service_id: <list or string>
          best_route: <value in [disable, enable]>
          fsso: <value in [disable, enable]>
          url_category: <list or string>
          app_group: <list or string>
          ssl_mirror_intf: <list or string>
          wsso: <value in [disable, enable]>
          ssl_mirror: <value in [disable, enable]>
          application: <list or integer>
          dscp_negate: <value in [disable, enable]>
          learning_mode: <value in [disable, enable]>
          devices: <list or string>
          dscp_value: <string>
          spamfilter_profile: <string>
          scan_botnet_connections: <value in [disable, block, monitor]>
          dscp_match: <value in [disable, enable]>
          diffserv_copy: <value in [disable, enable]>
          dstaddr6_negate: <value in [disable, enable]>
          internet_service6: <value in [disable, enable]>
          internet_service6_custom: <list or string>
          internet_service6_custom_group: <list or string>
          internet_service6_group: <list or string>
          internet_service6_name: <list or string>
          internet_service6_negate: <value in [disable, enable]>
          internet_service6_src: <value in [disable, enable]>
          internet_service6_src_custom: <list or string>
          internet_service6_src_custom_group: <list or string>
          internet_service6_src_group: <list or string>
          internet_service6_src_name: <list or string>
          internet_service6_src_negate: <value in [disable, enable]>
          network_service_dynamic: <list or string>
          network_service_src_dynamic: <list or string>
          reputation_direction6: <value in [source, destination]>
          reputation_minimum6: <integer>
          srcaddr6_negate: <value in [disable, enable]>
          ip_version_type: <string>
          ips_voip_filter: <string>
          pcp_inbound: <value in [disable, enable]>
          pcp_outbound: <value in [disable, enable]>
          pcp_poolname: <list or string>
          policy_behaviour_type: <string>
          policy_expiry_date_utc: <string>
          ztna_device_ownership: <value in [disable, enable]>
          ztna_ems_tag_secondary: <list or string>
          ztna_policy_redirect: <value in [disable, enable]>
          ztna_tags_match_logic: <value in [or, and]>
          casb_profile: <string>
          virtual_patch_profile: <string>
          diameter_filter_profile: <string>
          port_preserve: <value in [disable, enable]>
          cgn_sw_eif_ctrl: <value in [disable, enable]>
          eif_check: <value in [disable, enable]>
          eif_learn: <value in [disable, enable]>
          log_http_transaction: <value in [disable, enable, all, ...]>
          radius_ip_auth_bypass: <value in [disable, enable]>
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
        '/pm/config/adom/{adom}/pblock/{pblock}/firewall/policy'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/pblock/{pblock}/firewall/policy/{policy}'
    ]

    url_params = ['adom', 'pblock']
    module_primary_key = 'policyid'
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'pblock': {'required': True, 'type': 'str'},
        'pm_config_pblock_firewall_policy': {
            'type': 'dict',
            'v_range': [['7.0.3', '']],
            'options': {
                '_policy_block': {'v_range': [['7.0.3', '']], 'type': 'int'},
                'action': {'v_range': [['7.0.3', '']], 'choices': ['deny', 'accept', 'ipsec', 'ssl-vpn', 'redirect', 'isolate'], 'type': 'str'},
                'anti-replay': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'application-list': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'auth-cert': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'auth-path': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'auth-redirect-addr': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'auto-asic-offload': {'v_range': [['7.0.3', '7.2.0'], ['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'av-profile': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'block-notification': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'captive-portal-exempt': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'capture-packet': {'v_range': [['7.0.3', '7.2.0'], ['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'cifs-profile': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'comments': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'custom-log-fields': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'decrypted-traffic-mirror': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'delay-tcp-npu-session': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'diffserv-forward': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'diffserv-reverse': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'diffservcode-forward': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'diffservcode-rev': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'disclaimer': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable', 'user', 'domain', 'policy'], 'type': 'str'},
                'dlp-profile': {'v_range': [['7.2.0', '']], 'type': 'str'},
                'dnsfilter-profile': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'dsri': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'dstaddr': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'dstaddr-negate': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'dstaddr6': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'dstintf': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'dynamic-shaping': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'email-collect': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'emailfilter-profile': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'fec': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'file-filter-profile': {'v_range': [['7.0.3', '7.2.4'], ['7.4.0', '']], 'type': 'str'},
                'firewall-session-dirty': {'v_range': [['7.0.3', '']], 'choices': ['check-all', 'check-new'], 'type': 'str'},
                'fixedport': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'fsso-agent-for-ntlm': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'fsso-groups': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'geoip-anycast': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'geoip-match': {'v_range': [['7.0.3', '']], 'choices': ['physical-location', 'registered-location'], 'type': 'str'},
                'global-label': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'groups': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'gtp-profile': {'v_range': [['7.0.3', '7.2.0'], ['7.4.3', '']], 'type': 'str'},
                'http-policy-redirect': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'icap-profile': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'identity-based-route': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'inbound': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'inspection-mode': {'v_range': [['7.0.3', '']], 'choices': ['proxy', 'flow'], 'type': 'str'},
                'internet-service': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'internet-service-custom': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'internet-service-custom-group': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'internet-service-group': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'internet-service-name': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'internet-service-negate': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'internet-service-src': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'internet-service-src-custom': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'internet-service-src-custom-group': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'internet-service-src-group': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'internet-service-src-name': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'internet-service-src-negate': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ippool': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ips-sensor': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'label': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'logtraffic': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable', 'all', 'utm'], 'type': 'str'},
                'logtraffic-start': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'match-vip': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'match-vip-only': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'name': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'nat': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'nat46': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'nat64': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'natinbound': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'natip': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'natoutbound': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'np-acceleration': {'v_range': [['7.0.3', '7.2.0'], ['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ntlm': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ntlm-enabled-browsers': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'ntlm-guest': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'outbound': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'passive-wan-health-measurement': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'per-ip-shaper': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'permit-any-host': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'permit-stun-host': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'pfcp-profile': {'v_range': [['7.0.3', '7.2.0'], ['7.4.3', '']], 'type': 'str'},
                'policy-expiry': {'v_range': [['7.2.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'policy-expiry-date': {'v_range': [['7.2.0', '']], 'type': 'str'},
                'policyid': {'v_range': [['7.0.3', '']], 'required': True, 'type': 'int'},
                'poolname': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'poolname6': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'profile-group': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'profile-protocol-options': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'profile-type': {'v_range': [['7.0.3', '']], 'choices': ['single', 'group'], 'type': 'str'},
                'radius-mac-auth-bypass': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'redirect-url': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'replacemsg-override-group': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'reputation-direction': {'v_range': [['7.0.3', '']], 'choices': ['source', 'destination'], 'type': 'str'},
                'reputation-minimum': {'v_range': [['7.0.3', '']], 'type': 'int'},
                'rtp-addr': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'rtp-nat': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'schedule': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'schedule-timeout': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'sctp-filter-profile': {'v_range': [['7.0.3', '7.2.4'], ['7.4.0', '']], 'type': 'str'},
                'send-deny-packet': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'service': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'service-negate': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'session-ttl': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'sgt': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'sgt-check': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'src-vendor-mac': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'srcaddr': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'srcaddr-negate': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'srcaddr6': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'srcintf': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'ssh-filter-profile': {'v_range': [['7.0.3', '7.2.4'], ['7.4.0', '']], 'type': 'str'},
                'ssh-policy-redirect': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ssl-ssh-profile': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'status': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'tcp-mss-receiver': {'v_range': [['7.0.3', '']], 'type': 'int'},
                'tcp-mss-sender': {'v_range': [['7.0.3', '']], 'type': 'int'},
                'tcp-session-without-syn': {'v_range': [['7.0.3', '']], 'choices': ['all', 'data-only', 'disable'], 'type': 'str'},
                'timeout-send-rst': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'tos': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'tos-mask': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'tos-negate': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'traffic-shaper': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'traffic-shaper-reverse': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'users': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'utm-status': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'uuid': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'videofilter-profile': {'v_range': [['7.0.3', '7.2.4'], ['7.4.0', '']], 'type': 'str'},
                'vlan-cos-fwd': {'v_range': [['7.0.3', '']], 'type': 'int'},
                'vlan-cos-rev': {'v_range': [['7.0.3', '']], 'type': 'int'},
                'vlan-filter': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'voip-profile': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'vpntunnel': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'waf-profile': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'wanopt': {'v_range': [['7.0.3', '7.2.0'], ['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'wanopt-detection': {'v_range': [['7.0.3', '7.2.0'], ['7.4.3', '']], 'choices': ['active', 'passive', 'off'], 'type': 'str'},
                'wanopt-passive-opt': {
                    'v_range': [['7.0.3', '7.2.0'], ['7.4.3', '']],
                    'choices': ['default', 'transparent', 'non-transparent'],
                    'type': 'str'
                },
                'wanopt-peer': {'v_range': [['7.0.3', '7.2.0'], ['7.4.3', '']], 'type': 'str'},
                'wanopt-profile': {'v_range': [['7.0.3', '7.2.0'], ['7.4.3', '']], 'type': 'str'},
                'wccp': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'webcache': {'v_range': [['7.0.3', '7.2.0'], ['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'webcache-https': {'v_range': [['7.0.3', '7.2.0'], ['7.4.3', '']], 'choices': ['disable', 'ssl-server', 'any', 'enable'], 'type': 'str'},
                'webfilter-profile': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'webproxy-forward-server': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'webproxy-profile': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'ztna-ems-tag': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'ztna-geo-tag': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'ztna-status': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'policy-offload': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'cgn-session-quota': {'v_range': [['7.0.3', '']], 'type': 'int'},
                'tcp-timeout-pid': {'v_range': [['7.0.3', '7.2.0'], ['7.4.3', '']], 'type': 'str'},
                'udp-timeout-pid': {'v_range': [['7.0.3', '7.2.0'], ['7.4.3', '']], 'type': 'str'},
                'dlp-sensor': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'cgn-eif': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'cgn-log-server-grp': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'cgn-resource-quota': {'v_range': [['7.0.3', '']], 'type': 'int'},
                'cgn-eim': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'mms-profile': {'v_range': [['7.0.3', '7.2.0'], ['7.4.3', '']], 'type': 'str'},
                'app-category': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'internet-service-src-id': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'rsso': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'internet-service-id': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'best-route': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'fsso': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'url-category': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'app-group': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'ssl-mirror-intf': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'wsso': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ssl-mirror': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'application': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'dscp-negate': {'v_range': [['7.0.3', '7.2.1']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'learning-mode': {'v_range': [['7.0.3', '7.2.1']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'devices': {'v_range': [['7.0.3', '7.2.1']], 'type': 'raw'},
                'dscp-value': {'v_range': [['7.0.3', '7.2.1']], 'type': 'str'},
                'spamfilter-profile': {'v_range': [['7.0.3', '7.2.1']], 'type': 'str'},
                'scan-botnet-connections': {'v_range': [['7.0.3', '7.2.1']], 'choices': ['disable', 'block', 'monitor'], 'type': 'str'},
                'dscp-match': {'v_range': [['7.0.3', '7.2.1']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'diffserv-copy': {'v_range': [['7.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'dstaddr6-negate': {'v_range': [['7.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'internet-service6': {'v_range': [['7.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'internet-service6-custom': {'v_range': [['7.2.1', '']], 'type': 'raw'},
                'internet-service6-custom-group': {'v_range': [['7.2.1', '']], 'type': 'raw'},
                'internet-service6-group': {'v_range': [['7.2.1', '']], 'type': 'raw'},
                'internet-service6-name': {'v_range': [['7.2.1', '']], 'type': 'raw'},
                'internet-service6-negate': {'v_range': [['7.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'internet-service6-src': {'v_range': [['7.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'internet-service6-src-custom': {'v_range': [['7.2.1', '']], 'type': 'raw'},
                'internet-service6-src-custom-group': {'v_range': [['7.2.1', '']], 'type': 'raw'},
                'internet-service6-src-group': {'v_range': [['7.2.1', '']], 'type': 'raw'},
                'internet-service6-src-name': {'v_range': [['7.2.1', '']], 'type': 'raw'},
                'internet-service6-src-negate': {'v_range': [['7.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'network-service-dynamic': {'v_range': [['7.2.1', '']], 'type': 'raw'},
                'network-service-src-dynamic': {'v_range': [['7.2.1', '']], 'type': 'raw'},
                'reputation-direction6': {'v_range': [['7.2.1', '']], 'choices': ['source', 'destination'], 'type': 'str'},
                'reputation-minimum6': {'v_range': [['7.2.1', '']], 'type': 'int'},
                'srcaddr6-negate': {'v_range': [['7.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ip-version-type': {'v_range': [['7.4.0', '']], 'type': 'str'},
                'ips-voip-filter': {'v_range': [['7.4.0', '']], 'type': 'str'},
                'pcp-inbound': {'v_range': [['7.4.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'pcp-outbound': {'v_range': [['7.4.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'pcp-poolname': {'v_range': [['7.4.0', '']], 'type': 'raw'},
                'policy-behaviour-type': {'v_range': [['7.4.0', '']], 'type': 'str'},
                'policy-expiry-date-utc': {'v_range': [['7.4.0', '']], 'type': 'str'},
                'ztna-device-ownership': {'v_range': [['7.4.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ztna-ems-tag-secondary': {'v_range': [['7.4.0', '']], 'type': 'raw'},
                'ztna-policy-redirect': {'v_range': [['7.4.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ztna-tags-match-logic': {'v_range': [['7.4.0', '']], 'choices': ['or', 'and'], 'type': 'str'},
                'casb-profile': {'v_range': [['7.4.1', '']], 'type': 'str'},
                'virtual-patch-profile': {'v_range': [['7.4.1', '']], 'type': 'str'},
                'diameter-filter-profile': {'v_range': [['7.4.2', '']], 'type': 'str'},
                'port-preserve': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'cgn-sw-eif-ctrl': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'eif-check': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'eif-learn': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'log-http-transaction': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable', 'all', 'utm'], 'type': 'str'},
                'radius-ip-auth-bypass': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('full crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'pm_config_pblock_firewall_policy'),
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
