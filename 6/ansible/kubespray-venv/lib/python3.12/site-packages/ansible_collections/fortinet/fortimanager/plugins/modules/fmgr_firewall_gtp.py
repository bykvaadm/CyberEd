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
module: fmgr_firewall_gtp
short_description: Configure GTP.
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
    firewall_gtp:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            addr-notify:
                type: str
                description: Deprecated, please rename it to addr_notify. Overbilling notify address
            apn:
                type: list
                elements: dict
                description: Apn.
                suboptions:
                    action:
                        type: str
                        description: Action.
                        choices:
                            - 'allow'
                            - 'deny'
                    apnmember:
                        type: raw
                        description: (list or str) APN member.
                    id:
                        type: int
                        description: ID.
                    selection-mode:
                        type: list
                        elements: str
                        description: Deprecated, please rename it to selection_mode. APN selection mode.
                        choices:
                            - 'ms'
                            - 'net'
                            - 'vrf'
            apn-filter:
                type: str
                description: Deprecated, please rename it to apn_filter. Apn filter
                choices:
                    - 'disable'
                    - 'enable'
            authorized-ggsns:
                type: str
                description: Deprecated, please rename it to authorized_ggsns. Authorized GGSN group
            authorized-sgsns:
                type: str
                description: Deprecated, please rename it to authorized_sgsns. Authorized SGSN group
            comment:
                type: str
                description: Comment.
            context-id:
                type: int
                description: Deprecated, please rename it to context_id. Overbilling context.
            control-plane-message-rate-limit:
                type: int
                description: Deprecated, please rename it to control_plane_message_rate_limit. Control plane message rate limit
            default-apn-action:
                type: str
                description: Deprecated, please rename it to default_apn_action. Default apn action
                choices:
                    - 'allow'
                    - 'deny'
            default-imsi-action:
                type: str
                description: Deprecated, please rename it to default_imsi_action. Default imsi action
                choices:
                    - 'allow'
                    - 'deny'
            default-ip-action:
                type: str
                description: Deprecated, please rename it to default_ip_action. Default action for encapsulated IP traffic
                choices:
                    - 'allow'
                    - 'deny'
            default-noip-action:
                type: str
                description: Deprecated, please rename it to default_noip_action. Default action for encapsulated non-IP traffic
                choices:
                    - 'allow'
                    - 'deny'
            default-policy-action:
                type: str
                description: Deprecated, please rename it to default_policy_action. Default advanced policy action
                choices:
                    - 'allow'
                    - 'deny'
            denied-log:
                type: str
                description: Deprecated, please rename it to denied_log. Log denied
                choices:
                    - 'disable'
                    - 'enable'
            echo-request-interval:
                type: int
                description: Deprecated, please rename it to echo_request_interval. Echo request interval
            extension-log:
                type: str
                description: Deprecated, please rename it to extension_log. Log in extension format
                choices:
                    - 'disable'
                    - 'enable'
            forwarded-log:
                type: str
                description: Deprecated, please rename it to forwarded_log. Log forwarded
                choices:
                    - 'disable'
                    - 'enable'
            global-tunnel-limit:
                type: str
                description: Deprecated, please rename it to global_tunnel_limit. Global tunnel limit.
            gtp-in-gtp:
                type: str
                description: Deprecated, please rename it to gtp_in_gtp. Gtp in gtp
                choices:
                    - 'allow'
                    - 'deny'
            gtpu-denied-log:
                type: str
                description: Deprecated, please rename it to gtpu_denied_log. Enable/disable logging of denied GTP-U packets.
                choices:
                    - 'disable'
                    - 'enable'
            gtpu-forwarded-log:
                type: str
                description: Deprecated, please rename it to gtpu_forwarded_log. Enable/disable logging of forwarded GTP-U packets.
                choices:
                    - 'disable'
                    - 'enable'
            gtpu-log-freq:
                type: int
                description: Deprecated, please rename it to gtpu_log_freq. Logging of frequency of GTP-U packets.
            half-close-timeout:
                type: int
                description: Deprecated, please rename it to half_close_timeout. Half-close tunnel timeout
            half-open-timeout:
                type: int
                description: Deprecated, please rename it to half_open_timeout. Half-open tunnel timeout
            handover-group:
                type: str
                description: Deprecated, please rename it to handover_group. Handover SGSN group
            ie-remove-policy:
                type: list
                elements: dict
                description: Deprecated, please rename it to ie_remove_policy. Ie remove policy.
                suboptions:
                    id:
                        type: int
                        description: ID.
                    remove-ies:
                        type: list
                        elements: str
                        description: Deprecated, please rename it to remove_ies. GTP IEs to be removed.
                        choices:
                            - 'apn-restriction'
                            - 'rat-type'
                            - 'rai'
                            - 'uli'
                            - 'imei'
                    sgsn-addr:
                        type: str
                        description: Deprecated, please rename it to sgsn_addr. SGSN address name.
                    sgsn-addr6:
                        type: str
                        description: Deprecated, please rename it to sgsn_addr6. SGSN IPv6 address name.
            ie-remover:
                type: str
                description: Deprecated, please rename it to ie_remover. IE removal policy.
                choices:
                    - 'disable'
                    - 'enable'
            ie-white-list-v0v1:
                type: str
                description: Deprecated, please rename it to ie_white_list_v0v1. IE white list.
            ie-white-list-v2:
                type: str
                description: Deprecated, please rename it to ie_white_list_v2. IE white list.
            imsi:
                type: list
                elements: dict
                description: Imsi.
                suboptions:
                    action:
                        type: str
                        description: Action.
                        choices:
                            - 'allow'
                            - 'deny'
                    apnmember:
                        type: raw
                        description: (list or str) APN member.
                    id:
                        type: int
                        description: ID.
                    mcc-mnc:
                        type: str
                        description: Deprecated, please rename it to mcc_mnc. MCC MNC.
                    msisdn-prefix:
                        type: str
                        description: Deprecated, please rename it to msisdn_prefix. MSISDN prefix.
                    selection-mode:
                        type: list
                        elements: str
                        description: Deprecated, please rename it to selection_mode. APN selection mode.
                        choices:
                            - 'ms'
                            - 'net'
                            - 'vrf'
            imsi-filter:
                type: str
                description: Deprecated, please rename it to imsi_filter. Imsi filter
                choices:
                    - 'disable'
                    - 'enable'
            interface-notify:
                type: str
                description: Deprecated, please rename it to interface_notify. Overbilling interface
            invalid-reserved-field:
                type: str
                description: Deprecated, please rename it to invalid_reserved_field. Invalid reserved field in GTP header
                choices:
                    - 'allow'
                    - 'deny'
            invalid-sgsns-to-log:
                type: str
                description: Deprecated, please rename it to invalid_sgsns_to_log. Invalid SGSN group to be logged
            ip-filter:
                type: str
                description: Deprecated, please rename it to ip_filter. IP filter for encapsulted traffic
                choices:
                    - 'disable'
                    - 'enable'
            ip-policy:
                type: list
                elements: dict
                description: Deprecated, please rename it to ip_policy. Ip policy.
                suboptions:
                    action:
                        type: str
                        description: Action.
                        choices:
                            - 'allow'
                            - 'deny'
                    dstaddr:
                        type: str
                        description: Destination address name.
                    id:
                        type: int
                        description: ID.
                    srcaddr:
                        type: str
                        description: Source address name.
                    dstaddr6:
                        type: str
                        description: Destination IPv6 address name.
                    srcaddr6:
                        type: str
                        description: Source IPv6 address name.
            log-freq:
                type: int
                description: Deprecated, please rename it to log_freq. Logging of frequency of GTP-C packets.
            log-gtpu-limit:
                type: int
                description: Deprecated, please rename it to log_gtpu_limit. The user data log limit
            log-imsi-prefix:
                type: str
                description: Deprecated, please rename it to log_imsi_prefix. IMSI prefix for selective logging.
            log-msisdn-prefix:
                type: str
                description: Deprecated, please rename it to log_msisdn_prefix. The msisdn prefix for selective logging
            max-message-length:
                type: int
                description: Deprecated, please rename it to max_message_length. Max message length
            message-filter-v0v1:
                type: str
                description: Deprecated, please rename it to message_filter_v0v1. Message filter.
            message-filter-v2:
                type: str
                description: Deprecated, please rename it to message_filter_v2. Message filter.
            min-message-length:
                type: int
                description: Deprecated, please rename it to min_message_length. Min message length
            miss-must-ie:
                type: str
                description: Deprecated, please rename it to miss_must_ie. Missing mandatory information element
                choices:
                    - 'allow'
                    - 'deny'
            monitor-mode:
                type: str
                description: Deprecated, please rename it to monitor_mode. GTP monitor mode
                choices:
                    - 'disable'
                    - 'enable'
                    - 'vdom'
            name:
                type: str
                description: Profile name.
                required: true
            noip-filter:
                type: str
                description: Deprecated, please rename it to noip_filter. Non-IP filter for encapsulted traffic
                choices:
                    - 'disable'
                    - 'enable'
            noip-policy:
                type: list
                elements: dict
                description: Deprecated, please rename it to noip_policy. Noip policy.
                suboptions:
                    action:
                        type: str
                        description: Action.
                        choices:
                            - 'allow'
                            - 'deny'
                    end:
                        type: int
                        description: End of protocol range
                    id:
                        type: int
                        description: ID.
                    start:
                        type: int
                        description: Start of protocol range
                    type:
                        type: str
                        description: Protocol field type.
                        choices:
                            - 'etsi'
                            - 'ietf'
            out-of-state-ie:
                type: str
                description: Deprecated, please rename it to out_of_state_ie. Out of state information element.
                choices:
                    - 'allow'
                    - 'deny'
            out-of-state-message:
                type: str
                description: Deprecated, please rename it to out_of_state_message. Out of state GTP message
                choices:
                    - 'allow'
                    - 'deny'
            per-apn-shaper:
                type: list
                elements: dict
                description: Deprecated, please rename it to per_apn_shaper. Per apn shaper.
                suboptions:
                    apn:
                        type: str
                        description: APN name.
                    id:
                        type: int
                        description: ID.
                    rate-limit:
                        type: int
                        description: Deprecated, please rename it to rate_limit. Rate limit
                    version:
                        type: int
                        description: GTP version number
            policy:
                type: list
                elements: dict
                description: Policy.
                suboptions:
                    action:
                        type: str
                        description: Action.
                        choices:
                            - 'allow'
                            - 'deny'
                    apn-sel-mode:
                        type: list
                        elements: str
                        description: Deprecated, please rename it to apn_sel_mode. APN selection mode.
                        choices:
                            - 'ms'
                            - 'net'
                            - 'vrf'
                    apnmember:
                        type: raw
                        description: (list or str) APN member.
                    id:
                        type: int
                        description: ID.
                    imei:
                        type: str
                        description: IMEI
                    imsi:
                        type: str
                        description: IMSI prefix.
                    max-apn-restriction:
                        type: str
                        description: Deprecated, please rename it to max_apn_restriction. Maximum APN restriction value.
                        choices:
                            - 'all'
                            - 'public-1'
                            - 'public-2'
                            - 'private-1'
                            - 'private-2'
                    messages:
                        type: list
                        elements: str
                        description: GTP messages.
                        choices:
                            - 'create-req'
                            - 'create-res'
                            - 'update-req'
                            - 'update-res'
                    msisdn:
                        type: str
                        description: MSISDN prefix.
                    rai:
                        type: str
                        description: RAI pattern.
                    rat-type:
                        type: list
                        elements: str
                        description: Deprecated, please rename it to rat_type. RAT Type.
                        choices:
                            - 'any'
                            - 'utran'
                            - 'geran'
                            - 'wlan'
                            - 'gan'
                            - 'hspa'
                            - 'eutran'
                            - 'virtual'
                            - 'nbiot'
                    uli:
                        type: str
                        description: ULI pattern.
                    imsi-prefix:
                        type: str
                        description: Deprecated, please rename it to imsi_prefix. IMSI prefix.
                    msisdn-prefix:
                        type: str
                        description: Deprecated, please rename it to msisdn_prefix. MSISDN prefix.
                    apn:
                        type: str
                        description: APN subfix.
            policy-filter:
                type: str
                description: Deprecated, please rename it to policy_filter. Advanced policy filter
                choices:
                    - 'disable'
                    - 'enable'
            port-notify:
                type: int
                description: Deprecated, please rename it to port_notify. Overbilling notify port
            rate-limit-mode:
                type: str
                description: Deprecated, please rename it to rate_limit_mode. GTP rate limit mode.
                choices:
                    - 'per-profile'
                    - 'per-stream'
                    - 'per-apn'
            rate-limited-log:
                type: str
                description: Deprecated, please rename it to rate_limited_log. Log rate limited
                choices:
                    - 'disable'
                    - 'enable'
            rate-sampling-interval:
                type: int
                description: Deprecated, please rename it to rate_sampling_interval. Rate sampling interval
            remove-if-echo-expires:
                type: str
                description: Deprecated, please rename it to remove_if_echo_expires. Remove if echo response expires
                choices:
                    - 'disable'
                    - 'enable'
            remove-if-recovery-differ:
                type: str
                description: Deprecated, please rename it to remove_if_recovery_differ. Remove upon different Recovery IE
                choices:
                    - 'disable'
                    - 'enable'
            reserved-ie:
                type: str
                description: Deprecated, please rename it to reserved_ie. Reserved information element
                choices:
                    - 'allow'
                    - 'deny'
            send-delete-when-timeout:
                type: str
                description: Deprecated, please rename it to send_delete_when_timeout. Send DELETE request to path endpoints when GTPv0/v1 tunnel timeout.
                choices:
                    - 'disable'
                    - 'enable'
            send-delete-when-timeout-v2:
                type: str
                description: Deprecated, please rename it to send_delete_when_timeout_v2. Send DELETE request to path endpoints when GTPv2 tunnel timeout.
                choices:
                    - 'disable'
                    - 'enable'
            spoof-src-addr:
                type: str
                description: Deprecated, please rename it to spoof_src_addr. Spoofed source address for Mobile Station.
                choices:
                    - 'allow'
                    - 'deny'
            state-invalid-log:
                type: str
                description: Deprecated, please rename it to state_invalid_log. Log state invalid
                choices:
                    - 'disable'
                    - 'enable'
            traffic-count-log:
                type: str
                description: Deprecated, please rename it to traffic_count_log. Log tunnel traffic counter
                choices:
                    - 'disable'
                    - 'enable'
            tunnel-limit:
                type: int
                description: Deprecated, please rename it to tunnel_limit. Tunnel limit
            tunnel-limit-log:
                type: str
                description: Deprecated, please rename it to tunnel_limit_log. Tunnel limit
                choices:
                    - 'disable'
                    - 'enable'
            tunnel-timeout:
                type: int
                description: Deprecated, please rename it to tunnel_timeout. Established tunnel timeout
            unknown-version-action:
                type: str
                description: Deprecated, please rename it to unknown_version_action. Action for unknown gtp version
                choices:
                    - 'allow'
                    - 'deny'
            user-plane-message-rate-limit:
                type: int
                description: Deprecated, please rename it to user_plane_message_rate_limit. User plane message rate limit
            warning-threshold:
                type: int
                description: Deprecated, please rename it to warning_threshold. Warning threshold for rate limiting
            policy-v2:
                type: list
                elements: dict
                description: Deprecated, please rename it to policy_v2. Policy v2.
                suboptions:
                    action:
                        type: str
                        description: Action.
                        choices:
                            - 'deny'
                            - 'allow'
                    apn-sel-mode:
                        type: list
                        elements: str
                        description: Deprecated, please rename it to apn_sel_mode. APN selection mode.
                        choices:
                            - 'ms'
                            - 'net'
                            - 'vrf'
                    apnmember:
                        type: raw
                        description: (list or str) APN member.
                    id:
                        type: int
                        description: ID.
                    imsi-prefix:
                        type: str
                        description: Deprecated, please rename it to imsi_prefix. IMSI prefix.
                    max-apn-restriction:
                        type: str
                        description: Deprecated, please rename it to max_apn_restriction. Maximum APN restriction value.
                        choices:
                            - 'all'
                            - 'public-1'
                            - 'public-2'
                            - 'private-1'
                            - 'private-2'
                    mei:
                        type: str
                        description: MEI pattern.
                    messages:
                        type: list
                        elements: str
                        description: GTP messages.
                        choices:
                            - 'create-ses-req'
                            - 'create-ses-res'
                            - 'modify-bearer-req'
                            - 'modify-bearer-res'
                    msisdn-prefix:
                        type: str
                        description: Deprecated, please rename it to msisdn_prefix. MSISDN prefix.
                    rat-type:
                        type: list
                        elements: str
                        description: Deprecated, please rename it to rat_type. RAT Type.
                        choices:
                            - 'any'
                            - 'utran'
                            - 'geran'
                            - 'wlan'
                            - 'gan'
                            - 'hspa'
                            - 'eutran'
                            - 'virtual'
                            - 'nbiot'
                            - 'ltem'
                            - 'nr'
                    uli:
                        type: raw
                        description: (list) GTPv2 ULI patterns
            sub-second-interval:
                type: str
                description: Deprecated, please rename it to sub_second_interval. Sub-second interval
                choices:
                    - '0.1'
                    - '0.25'
                    - '0.5'
            sub-second-sampling:
                type: str
                description: Deprecated, please rename it to sub_second_sampling. Enable/disable sub-second sampling.
                choices:
                    - 'disable'
                    - 'enable'
            authorized-ggsns6:
                type: str
                description: Deprecated, please rename it to authorized_ggsns6. Authorized GGSN/PGW IPv6 group.
            authorized-sgsns6:
                type: str
                description: Deprecated, please rename it to authorized_sgsns6. Authorized SGSN/SGW IPv6 group.
            handover-group6:
                type: str
                description: Deprecated, please rename it to handover_group6. Handover SGSN/SGW IPv6 group.
            invalid-sgsns6-to-log:
                type: str
                description: Deprecated, please rename it to invalid_sgsns6_to_log. Invalid SGSN IPv6 group to be logged.
            ie-validation:
                type: dict
                description: Deprecated, please rename it to ie_validation. Ie validation.
                suboptions:
                    apn-restriction:
                        type: str
                        description: Deprecated, please rename it to apn_restriction. Validate APN restriction.
                        choices:
                            - 'disable'
                            - 'enable'
                    charging-ID:
                        type: str
                        description: Deprecated, please rename it to charging_ID. Validate charging ID.
                        choices:
                            - 'disable'
                            - 'enable'
                    charging-gateway-addr:
                        type: str
                        description: Deprecated, please rename it to charging_gateway_addr. Validate charging gateway address.
                        choices:
                            - 'disable'
                            - 'enable'
                    end-user-addr:
                        type: str
                        description: Deprecated, please rename it to end_user_addr. Validate end user address.
                        choices:
                            - 'disable'
                            - 'enable'
                    gsn-addr:
                        type: str
                        description: Deprecated, please rename it to gsn_addr. Validate GSN address.
                        choices:
                            - 'disable'
                            - 'enable'
                    imei:
                        type: str
                        description: Validate IMEI
                        choices:
                            - 'disable'
                            - 'enable'
                    imsi:
                        type: str
                        description: Validate IMSI.
                        choices:
                            - 'disable'
                            - 'enable'
                    mm-context:
                        type: str
                        description: Deprecated, please rename it to mm_context. Validate MM context.
                        choices:
                            - 'disable'
                            - 'enable'
                    ms-tzone:
                        type: str
                        description: Deprecated, please rename it to ms_tzone. Validate MS time zone.
                        choices:
                            - 'disable'
                            - 'enable'
                    ms-validated:
                        type: str
                        description: Deprecated, please rename it to ms_validated. Validate MS validated.
                        choices:
                            - 'disable'
                            - 'enable'
                    msisdn:
                        type: str
                        description: Validate MSISDN.
                        choices:
                            - 'disable'
                            - 'enable'
                    nsapi:
                        type: str
                        description: Validate NSAPI.
                        choices:
                            - 'disable'
                            - 'enable'
                    pdp-context:
                        type: str
                        description: Deprecated, please rename it to pdp_context. Validate PDP context.
                        choices:
                            - 'disable'
                            - 'enable'
                    qos-profile:
                        type: str
                        description: Deprecated, please rename it to qos_profile. Validate Quality of Service
                        choices:
                            - 'disable'
                            - 'enable'
                    rai:
                        type: str
                        description: Validate RAI.
                        choices:
                            - 'disable'
                            - 'enable'
                    rat-type:
                        type: str
                        description: Deprecated, please rename it to rat_type. Validate RAT type.
                        choices:
                            - 'disable'
                            - 'enable'
                    reordering-required:
                        type: str
                        description: Deprecated, please rename it to reordering_required. Validate re-ordering required.
                        choices:
                            - 'disable'
                            - 'enable'
                    selection-mode:
                        type: str
                        description: Deprecated, please rename it to selection_mode. Validate selection mode.
                        choices:
                            - 'disable'
                            - 'enable'
                    uli:
                        type: str
                        description: Validate user location information.
                        choices:
                            - 'disable'
                            - 'enable'
            message-rate-limit:
                type: dict
                description: Deprecated, please rename it to message_rate_limit. Message rate limit.
                suboptions:
                    create-aa-pdp-request:
                        type: int
                        description: Deprecated, please rename it to create_aa_pdp_request. Rate limit for create AA PDP context request
                    create-aa-pdp-response:
                        type: int
                        description: Deprecated, please rename it to create_aa_pdp_response. Rate limit for create AA PDP context response
                    create-mbms-request:
                        type: int
                        description: Deprecated, please rename it to create_mbms_request. Rate limit for create MBMS context request
                    create-mbms-response:
                        type: int
                        description: Deprecated, please rename it to create_mbms_response. Rate limit for create MBMS context response
                    create-pdp-request:
                        type: int
                        description: Deprecated, please rename it to create_pdp_request. Rate limit for create PDP context request
                    create-pdp-response:
                        type: int
                        description: Deprecated, please rename it to create_pdp_response. Rate limit for create PDP context response
                    delete-aa-pdp-request:
                        type: int
                        description: Deprecated, please rename it to delete_aa_pdp_request. Rate limit for delete AA PDP context request
                    delete-aa-pdp-response:
                        type: int
                        description: Deprecated, please rename it to delete_aa_pdp_response. Rate limit for delete AA PDP context response
                    delete-mbms-request:
                        type: int
                        description: Deprecated, please rename it to delete_mbms_request. Rate limit for delete MBMS context request
                    delete-mbms-response:
                        type: int
                        description: Deprecated, please rename it to delete_mbms_response. Rate limit for delete MBMS context response
                    delete-pdp-request:
                        type: int
                        description: Deprecated, please rename it to delete_pdp_request. Rate limit for delete PDP context request
                    delete-pdp-response:
                        type: int
                        description: Deprecated, please rename it to delete_pdp_response. Rate limit for delete PDP context response
                    echo-reponse:
                        type: int
                        description: Deprecated, please rename it to echo_reponse. Rate limit for echo response
                    echo-request:
                        type: int
                        description: Deprecated, please rename it to echo_request. Rate limit for echo requests
                    error-indication:
                        type: int
                        description: Deprecated, please rename it to error_indication. Rate limit for error indication
                    failure-report-request:
                        type: int
                        description: Deprecated, please rename it to failure_report_request. Rate limit for failure report request
                    failure-report-response:
                        type: int
                        description: Deprecated, please rename it to failure_report_response. Rate limit for failure report response
                    fwd-reloc-complete-ack:
                        type: int
                        description: Deprecated, please rename it to fwd_reloc_complete_ack. Rate limit for forward relocation complete acknowledge
                    fwd-relocation-complete:
                        type: int
                        description: Deprecated, please rename it to fwd_relocation_complete. Rate limit for forward relocation complete
                    fwd-relocation-request:
                        type: int
                        description: Deprecated, please rename it to fwd_relocation_request. Rate limit for forward relocation request
                    fwd-relocation-response:
                        type: int
                        description: Deprecated, please rename it to fwd_relocation_response. Rate limit for forward relocation response
                    fwd-srns-context:
                        type: int
                        description: Deprecated, please rename it to fwd_srns_context. Rate limit for forward SRNS context
                    fwd-srns-context-ack:
                        type: int
                        description: Deprecated, please rename it to fwd_srns_context_ack. Rate limit for forward SRNS context acknowledge
                    g-pdu:
                        type: int
                        description: Deprecated, please rename it to g_pdu. Rate limit for G-PDU
                    identification-request:
                        type: int
                        description: Deprecated, please rename it to identification_request. Rate limit for identification request
                    identification-response:
                        type: int
                        description: Deprecated, please rename it to identification_response. Rate limit for identification response
                    mbms-de-reg-request:
                        type: int
                        description: Deprecated, please rename it to mbms_de_reg_request. Rate limit for MBMS de-registration request
                    mbms-de-reg-response:
                        type: int
                        description: Deprecated, please rename it to mbms_de_reg_response. Rate limit for MBMS de-registration response
                    mbms-notify-rej-request:
                        type: int
                        description: Deprecated, please rename it to mbms_notify_rej_request. Rate limit for MBMS notification reject request
                    mbms-notify-rej-response:
                        type: int
                        description: Deprecated, please rename it to mbms_notify_rej_response. Rate limit for MBMS notification reject response
                    mbms-notify-request:
                        type: int
                        description: Deprecated, please rename it to mbms_notify_request. Rate limit for MBMS notification request
                    mbms-notify-response:
                        type: int
                        description: Deprecated, please rename it to mbms_notify_response. Rate limit for MBMS notification response
                    mbms-reg-request:
                        type: int
                        description: Deprecated, please rename it to mbms_reg_request. Rate limit for MBMS registration request
                    mbms-reg-response:
                        type: int
                        description: Deprecated, please rename it to mbms_reg_response. Rate limit for MBMS registration response
                    mbms-ses-start-request:
                        type: int
                        description: Deprecated, please rename it to mbms_ses_start_request. Rate limit for MBMS session start request
                    mbms-ses-start-response:
                        type: int
                        description: Deprecated, please rename it to mbms_ses_start_response. Rate limit for MBMS session start response
                    mbms-ses-stop-request:
                        type: int
                        description: Deprecated, please rename it to mbms_ses_stop_request. Rate limit for MBMS session stop request
                    mbms-ses-stop-response:
                        type: int
                        description: Deprecated, please rename it to mbms_ses_stop_response. Rate limit for MBMS session stop response
                    note-ms-request:
                        type: int
                        description: Deprecated, please rename it to note_ms_request. Rate limit for note MS GPRS present request
                    note-ms-response:
                        type: int
                        description: Deprecated, please rename it to note_ms_response. Rate limit for note MS GPRS present response
                    pdu-notify-rej-request:
                        type: int
                        description: Deprecated, please rename it to pdu_notify_rej_request. Rate limit for PDU notify reject request
                    pdu-notify-rej-response:
                        type: int
                        description: Deprecated, please rename it to pdu_notify_rej_response. Rate limit for PDU notify reject response
                    pdu-notify-request:
                        type: int
                        description: Deprecated, please rename it to pdu_notify_request. Rate limit for PDU notify request
                    pdu-notify-response:
                        type: int
                        description: Deprecated, please rename it to pdu_notify_response. Rate limit for PDU notify response
                    ran-info:
                        type: int
                        description: Deprecated, please rename it to ran_info. Rate limit for RAN information relay
                    relocation-cancel-request:
                        type: int
                        description: Deprecated, please rename it to relocation_cancel_request. Rate limit for relocation cancel request
                    relocation-cancel-response:
                        type: int
                        description: Deprecated, please rename it to relocation_cancel_response. Rate limit for relocation cancel response
                    send-route-request:
                        type: int
                        description: Deprecated, please rename it to send_route_request. Rate limit for send routing information for GPRS request
                    send-route-response:
                        type: int
                        description: Deprecated, please rename it to send_route_response. Rate limit for send routing information for GPRS response
                    sgsn-context-ack:
                        type: int
                        description: Deprecated, please rename it to sgsn_context_ack. Rate limit for SGSN context acknowledgement
                    sgsn-context-request:
                        type: int
                        description: Deprecated, please rename it to sgsn_context_request. Rate limit for SGSN context request
                    sgsn-context-response:
                        type: int
                        description: Deprecated, please rename it to sgsn_context_response. Rate limit for SGSN context response
                    support-ext-hdr-notify:
                        type: int
                        description: Deprecated, please rename it to support_ext_hdr_notify. Rate limit for support extension headers notification
                    update-mbms-request:
                        type: int
                        description: Deprecated, please rename it to update_mbms_request. Rate limit for update MBMS context request
                    update-mbms-response:
                        type: int
                        description: Deprecated, please rename it to update_mbms_response. Rate limit for update MBMS context response
                    update-pdp-request:
                        type: int
                        description: Deprecated, please rename it to update_pdp_request. Rate limit for update PDP context request
                    update-pdp-response:
                        type: int
                        description: Deprecated, please rename it to update_pdp_response. Rate limit for update PDP context response
                    version-not-support:
                        type: int
                        description: Deprecated, please rename it to version_not_support. Rate limit for version not supported
                    echo-response:
                        type: int
                        description: Deprecated, please rename it to echo_response. Rate limit for echo response
            message-rate-limit-v0:
                type: dict
                description: Deprecated, please rename it to message_rate_limit_v0. Message rate limit v0.
                suboptions:
                    create-pdp-request:
                        type: int
                        description: Deprecated, please rename it to create_pdp_request. Rate limit
                    delete-pdp-request:
                        type: int
                        description: Deprecated, please rename it to delete_pdp_request. Rate limit
                    echo-request:
                        type: int
                        description: Deprecated, please rename it to echo_request. Rate limit
            message-rate-limit-v1:
                type: dict
                description: Deprecated, please rename it to message_rate_limit_v1. Message rate limit v1.
                suboptions:
                    create-pdp-request:
                        type: int
                        description: Deprecated, please rename it to create_pdp_request. Rate limit
                    delete-pdp-request:
                        type: int
                        description: Deprecated, please rename it to delete_pdp_request. Rate limit
                    echo-request:
                        type: int
                        description: Deprecated, please rename it to echo_request. Rate limit
            message-rate-limit-v2:
                type: dict
                description: Deprecated, please rename it to message_rate_limit_v2. Message rate limit v2.
                suboptions:
                    create-session-request:
                        type: int
                        description: Deprecated, please rename it to create_session_request. Rate limit
                    delete-session-request:
                        type: int
                        description: Deprecated, please rename it to delete_session_request. Rate limit
                    echo-request:
                        type: int
                        description: Deprecated, please rename it to echo_request. Rate limit
            ie-allow-list-v0v1:
                type: str
                description: Deprecated, please rename it to ie_allow_list_v0v1. IE allow list.
            ie-allow-list-v2:
                type: str
                description: Deprecated, please rename it to ie_allow_list_v2. IE allow list.
            rat-timeout-profile:
                type: str
                description: Deprecated, please rename it to rat_timeout_profile. RAT timeout profile.
            message-filter:
                type: dict
                description: Deprecated, please rename it to message_filter. Message filter.
                suboptions:
                    create-aa-pdp:
                        type: str
                        description: Deprecated, please rename it to create_aa_pdp. Create AA PDP.
                        choices:
                            - 'allow'
                            - 'deny'
                    create-mbms:
                        type: str
                        description: Deprecated, please rename it to create_mbms. Create MBMS.
                        choices:
                            - 'allow'
                            - 'deny'
                    create-pdp:
                        type: str
                        description: Deprecated, please rename it to create_pdp. Create PDP.
                        choices:
                            - 'allow'
                            - 'deny'
                    data-record:
                        type: str
                        description: Deprecated, please rename it to data_record. Data record.
                        choices:
                            - 'allow'
                            - 'deny'
                    delete-aa-pdp:
                        type: str
                        description: Deprecated, please rename it to delete_aa_pdp. Delete AA PDP.
                        choices:
                            - 'allow'
                            - 'deny'
                    delete-mbms:
                        type: str
                        description: Deprecated, please rename it to delete_mbms. Delete MBMS.
                        choices:
                            - 'allow'
                            - 'deny'
                    delete-pdp:
                        type: str
                        description: Deprecated, please rename it to delete_pdp. Delete PDP.
                        choices:
                            - 'allow'
                            - 'deny'
                    echo:
                        type: str
                        description: Echo.
                        choices:
                            - 'allow'
                            - 'deny'
                    error-indication:
                        type: str
                        description: Deprecated, please rename it to error_indication. Error indication.
                        choices:
                            - 'allow'
                            - 'deny'
                    failure-report:
                        type: str
                        description: Deprecated, please rename it to failure_report. Failure report.
                        choices:
                            - 'allow'
                            - 'deny'
                    fwd-relocation:
                        type: str
                        description: Deprecated, please rename it to fwd_relocation. Forward relocation.
                        choices:
                            - 'allow'
                            - 'deny'
                    fwd-srns-context:
                        type: str
                        description: Deprecated, please rename it to fwd_srns_context. Forward SRNS context.
                        choices:
                            - 'allow'
                            - 'deny'
                    gtp-pdu:
                        type: str
                        description: Deprecated, please rename it to gtp_pdu. GTP PDU.
                        choices:
                            - 'allow'
                            - 'deny'
                    identification:
                        type: str
                        description: Identification.
                        choices:
                            - 'allow'
                            - 'deny'
                    mbms-notification:
                        type: str
                        description: Deprecated, please rename it to mbms_notification. MBMS notification.
                        choices:
                            - 'allow'
                            - 'deny'
                    node-alive:
                        type: str
                        description: Deprecated, please rename it to node_alive. Node alive.
                        choices:
                            - 'allow'
                            - 'deny'
                    note-ms-present:
                        type: str
                        description: Deprecated, please rename it to note_ms_present. Note MS present.
                        choices:
                            - 'allow'
                            - 'deny'
                    pdu-notification:
                        type: str
                        description: Deprecated, please rename it to pdu_notification. PDU notification.
                        choices:
                            - 'allow'
                            - 'deny'
                    ran-info:
                        type: str
                        description: Deprecated, please rename it to ran_info. Ran info.
                        choices:
                            - 'allow'
                            - 'deny'
                    redirection:
                        type: str
                        description: Redirection.
                        choices:
                            - 'allow'
                            - 'deny'
                    relocation-cancel:
                        type: str
                        description: Deprecated, please rename it to relocation_cancel. Relocation cancel.
                        choices:
                            - 'allow'
                            - 'deny'
                    send-route:
                        type: str
                        description: Deprecated, please rename it to send_route. Send route.
                        choices:
                            - 'allow'
                            - 'deny'
                    sgsn-context:
                        type: str
                        description: Deprecated, please rename it to sgsn_context. SGSN context.
                        choices:
                            - 'allow'
                            - 'deny'
                    support-extension:
                        type: str
                        description: Deprecated, please rename it to support_extension. Support extension.
                        choices:
                            - 'allow'
                            - 'deny'
                    unknown-message-action:
                        type: str
                        description: Deprecated, please rename it to unknown_message_action. Unknown message action.
                        choices:
                            - 'allow'
                            - 'deny'
                    update-mbms:
                        type: str
                        description: Deprecated, please rename it to update_mbms. Update MBMS.
                        choices:
                            - 'allow'
                            - 'deny'
                    update-pdp:
                        type: str
                        description: Deprecated, please rename it to update_pdp. Update PDP.
                        choices:
                            - 'allow'
                            - 'deny'
                    version-not-support:
                        type: str
                        description: Deprecated, please rename it to version_not_support. Version not supported.
                        choices:
                            - 'allow'
                            - 'deny'
            gtpv0:
                type: str
                description: GTPv0 traffic.
                choices:
                    - 'allow'
                    - 'deny'
'''

EXAMPLES = '''
- name: Example playbook
  hosts: fortimanagers
  connection: httpapi
  vars:
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_httpapi_port: 443
  tasks:
    - name: Configure GTP.
      fortinet.fortimanager.fmgr_firewall_gtp:
        bypass_validation: false
        adom: FortiCarrier # This is FOC-only object, need a FortiCarrier adom
        state: present
        firewall_gtp:
          monitor-mode: disable # <value in [disable, enable, vdom]>
          name: "ansible-test"

- name: Gathering fortimanager facts
  hosts: fortimanagers
  gather_facts: false
  connection: httpapi
  vars:
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_httpapi_port: 443
  tasks:
    - name: Retrieve all the GTPs
      fortinet.fortimanager.fmgr_fact:
        facts:
          selector: "firewall_gtp"
          params:
            adom: "FortiCarrier" # This is FOC-only object, need a FortiCarrier adom
            gtp: "your_value"
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
        '/pm/config/adom/{adom}/obj/firewall/gtp',
        '/pm/config/global/obj/firewall/gtp'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/firewall/gtp/{gtp}',
        '/pm/config/global/obj/firewall/gtp/{gtp}'
    ]

    url_params = ['adom']
    module_primary_key = 'name'
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'firewall_gtp': {
            'type': 'dict',
            'v_range': [['6.0.0', '']],
            'options': {
                'addr-notify': {'type': 'str'},
                'apn': {
                    'type': 'list',
                    'options': {
                        'action': {'choices': ['allow', 'deny'], 'type': 'str'},
                        'apnmember': {'type': 'raw'},
                        'id': {'type': 'int'},
                        'selection-mode': {'type': 'list', 'choices': ['ms', 'net', 'vrf'], 'elements': 'str'}
                    },
                    'elements': 'dict'
                },
                'apn-filter': {'choices': ['disable', 'enable'], 'type': 'str'},
                'authorized-ggsns': {'type': 'str'},
                'authorized-sgsns': {'type': 'str'},
                'comment': {'type': 'str'},
                'context-id': {'type': 'int'},
                'control-plane-message-rate-limit': {'type': 'int'},
                'default-apn-action': {'choices': ['allow', 'deny'], 'type': 'str'},
                'default-imsi-action': {'choices': ['allow', 'deny'], 'type': 'str'},
                'default-ip-action': {'choices': ['allow', 'deny'], 'type': 'str'},
                'default-noip-action': {'choices': ['allow', 'deny'], 'type': 'str'},
                'default-policy-action': {'choices': ['allow', 'deny'], 'type': 'str'},
                'denied-log': {'choices': ['disable', 'enable'], 'type': 'str'},
                'echo-request-interval': {'type': 'int'},
                'extension-log': {'choices': ['disable', 'enable'], 'type': 'str'},
                'forwarded-log': {'choices': ['disable', 'enable'], 'type': 'str'},
                'global-tunnel-limit': {'type': 'str'},
                'gtp-in-gtp': {'choices': ['allow', 'deny'], 'type': 'str'},
                'gtpu-denied-log': {'choices': ['disable', 'enable'], 'type': 'str'},
                'gtpu-forwarded-log': {'choices': ['disable', 'enable'], 'type': 'str'},
                'gtpu-log-freq': {'type': 'int'},
                'half-close-timeout': {'type': 'int'},
                'half-open-timeout': {'type': 'int'},
                'handover-group': {'type': 'str'},
                'ie-remove-policy': {
                    'type': 'list',
                    'options': {
                        'id': {'type': 'int'},
                        'remove-ies': {'type': 'list', 'choices': ['apn-restriction', 'rat-type', 'rai', 'uli', 'imei'], 'elements': 'str'},
                        'sgsn-addr': {'type': 'str'},
                        'sgsn-addr6': {'v_range': [['6.4.2', '']], 'type': 'str'}
                    },
                    'elements': 'dict'
                },
                'ie-remover': {'choices': ['disable', 'enable'], 'type': 'str'},
                'ie-white-list-v0v1': {'type': 'str'},
                'ie-white-list-v2': {'type': 'str'},
                'imsi': {
                    'type': 'list',
                    'options': {
                        'action': {'choices': ['allow', 'deny'], 'type': 'str'},
                        'apnmember': {'type': 'raw'},
                        'id': {'type': 'int'},
                        'mcc-mnc': {'type': 'str'},
                        'msisdn-prefix': {'type': 'str'},
                        'selection-mode': {'type': 'list', 'choices': ['ms', 'net', 'vrf'], 'elements': 'str'}
                    },
                    'elements': 'dict'
                },
                'imsi-filter': {'choices': ['disable', 'enable'], 'type': 'str'},
                'interface-notify': {'type': 'str'},
                'invalid-reserved-field': {'choices': ['allow', 'deny'], 'type': 'str'},
                'invalid-sgsns-to-log': {'type': 'str'},
                'ip-filter': {'choices': ['disable', 'enable'], 'type': 'str'},
                'ip-policy': {
                    'type': 'list',
                    'options': {
                        'action': {'choices': ['allow', 'deny'], 'type': 'str'},
                        'dstaddr': {'type': 'str'},
                        'id': {'type': 'int'},
                        'srcaddr': {'type': 'str'},
                        'dstaddr6': {'v_range': [['6.4.2', '']], 'type': 'str'},
                        'srcaddr6': {'v_range': [['6.4.2', '']], 'type': 'str'}
                    },
                    'elements': 'dict'
                },
                'log-freq': {'type': 'int'},
                'log-gtpu-limit': {'type': 'int'},
                'log-imsi-prefix': {'type': 'str'},
                'log-msisdn-prefix': {'type': 'str'},
                'max-message-length': {'type': 'int'},
                'message-filter-v0v1': {'type': 'str'},
                'message-filter-v2': {'type': 'str'},
                'min-message-length': {'type': 'int'},
                'miss-must-ie': {'choices': ['allow', 'deny'], 'type': 'str'},
                'monitor-mode': {'choices': ['disable', 'enable', 'vdom'], 'type': 'str'},
                'name': {'required': True, 'type': 'str'},
                'noip-filter': {'choices': ['disable', 'enable'], 'type': 'str'},
                'noip-policy': {
                    'type': 'list',
                    'options': {
                        'action': {'choices': ['allow', 'deny'], 'type': 'str'},
                        'end': {'type': 'int'},
                        'id': {'type': 'int'},
                        'start': {'type': 'int'},
                        'type': {'choices': ['etsi', 'ietf'], 'type': 'str'}
                    },
                    'elements': 'dict'
                },
                'out-of-state-ie': {'choices': ['allow', 'deny'], 'type': 'str'},
                'out-of-state-message': {'choices': ['allow', 'deny'], 'type': 'str'},
                'per-apn-shaper': {
                    'type': 'list',
                    'options': {'apn': {'type': 'str'}, 'id': {'type': 'int'}, 'rate-limit': {'type': 'int'}, 'version': {'type': 'int'}},
                    'elements': 'dict'
                },
                'policy': {
                    'type': 'list',
                    'options': {
                        'action': {'choices': ['allow', 'deny'], 'type': 'str'},
                        'apn-sel-mode': {'type': 'list', 'choices': ['ms', 'net', 'vrf'], 'elements': 'str'},
                        'apnmember': {'type': 'raw'},
                        'id': {'type': 'int'},
                        'imei': {'type': 'str'},
                        'imsi': {'v_range': [['6.0.0', '7.2.1']], 'type': 'str'},
                        'max-apn-restriction': {'choices': ['all', 'public-1', 'public-2', 'private-1', 'private-2'], 'type': 'str'},
                        'messages': {'type': 'list', 'choices': ['create-req', 'create-res', 'update-req', 'update-res'], 'elements': 'str'},
                        'msisdn': {'v_range': [['6.0.0', '7.2.1']], 'type': 'str'},
                        'rai': {'type': 'str'},
                        'rat-type': {
                            'type': 'list',
                            'choices': ['any', 'utran', 'geran', 'wlan', 'gan', 'hspa', 'eutran', 'virtual', 'nbiot'],
                            'elements': 'str'
                        },
                        'uli': {'type': 'str'},
                        'imsi-prefix': {'v_range': [['6.2.0', '']], 'type': 'str'},
                        'msisdn-prefix': {'v_range': [['6.2.0', '']], 'type': 'str'},
                        'apn': {'v_range': [['6.2.0', '6.2.12']], 'type': 'str'}
                    },
                    'elements': 'dict'
                },
                'policy-filter': {'choices': ['disable', 'enable'], 'type': 'str'},
                'port-notify': {'type': 'int'},
                'rate-limit-mode': {'choices': ['per-profile', 'per-stream', 'per-apn'], 'type': 'str'},
                'rate-limited-log': {'choices': ['disable', 'enable'], 'type': 'str'},
                'rate-sampling-interval': {'type': 'int'},
                'remove-if-echo-expires': {'choices': ['disable', 'enable'], 'type': 'str'},
                'remove-if-recovery-differ': {'choices': ['disable', 'enable'], 'type': 'str'},
                'reserved-ie': {'choices': ['allow', 'deny'], 'type': 'str'},
                'send-delete-when-timeout': {'choices': ['disable', 'enable'], 'type': 'str'},
                'send-delete-when-timeout-v2': {'choices': ['disable', 'enable'], 'type': 'str'},
                'spoof-src-addr': {'choices': ['allow', 'deny'], 'type': 'str'},
                'state-invalid-log': {'choices': ['disable', 'enable'], 'type': 'str'},
                'traffic-count-log': {'choices': ['disable', 'enable'], 'type': 'str'},
                'tunnel-limit': {'type': 'int'},
                'tunnel-limit-log': {'choices': ['disable', 'enable'], 'type': 'str'},
                'tunnel-timeout': {'type': 'int'},
                'unknown-version-action': {'choices': ['allow', 'deny'], 'type': 'str'},
                'user-plane-message-rate-limit': {'type': 'int'},
                'warning-threshold': {'type': 'int'},
                'policy-v2': {
                    'v_range': [['6.2.1', '']],
                    'type': 'list',
                    'options': {
                        'action': {'v_range': [['6.2.1', '']], 'choices': ['deny', 'allow'], 'type': 'str'},
                        'apn-sel-mode': {'v_range': [['6.2.1', '']], 'type': 'list', 'choices': ['ms', 'net', 'vrf'], 'elements': 'str'},
                        'apnmember': {'v_range': [['6.2.1', '']], 'type': 'raw'},
                        'id': {'v_range': [['6.2.1', '']], 'type': 'int'},
                        'imsi-prefix': {'v_range': [['6.2.1', '']], 'type': 'str'},
                        'max-apn-restriction': {
                            'v_range': [['6.2.1', '']],
                            'choices': ['all', 'public-1', 'public-2', 'private-1', 'private-2'],
                            'type': 'str'
                        },
                        'mei': {'v_range': [['6.2.1', '']], 'type': 'str'},
                        'messages': {
                            'v_range': [['6.2.1', '']],
                            'type': 'list',
                            'choices': ['create-ses-req', 'create-ses-res', 'modify-bearer-req', 'modify-bearer-res'],
                            'elements': 'str'
                        },
                        'msisdn-prefix': {'v_range': [['6.2.1', '']], 'type': 'str'},
                        'rat-type': {
                            'v_range': [['6.2.1', '']],
                            'type': 'list',
                            'choices': ['any', 'utran', 'geran', 'wlan', 'gan', 'hspa', 'eutran', 'virtual', 'nbiot', 'ltem', 'nr'],
                            'elements': 'str'
                        },
                        'uli': {'v_range': [['6.2.1', '']], 'type': 'raw'}
                    },
                    'elements': 'dict'
                },
                'sub-second-interval': {'v_range': [['6.2.2', '']], 'choices': ['0.1', '0.25', '0.5'], 'type': 'str'},
                'sub-second-sampling': {'v_range': [['6.2.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'authorized-ggsns6': {'v_range': [['6.4.2', '']], 'type': 'str'},
                'authorized-sgsns6': {'v_range': [['6.4.2', '']], 'type': 'str'},
                'handover-group6': {'v_range': [['6.4.2', '']], 'type': 'str'},
                'invalid-sgsns6-to-log': {'v_range': [['6.4.2', '']], 'type': 'str'},
                'ie-validation': {
                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                    'type': 'dict',
                    'options': {
                        'apn-restriction': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'charging-ID': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'charging-gateway-addr': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'end-user-addr': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'gsn-addr': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'imei': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'imsi': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'mm-context': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'ms-tzone': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'ms-validated': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'msisdn': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'nsapi': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'pdp-context': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'qos-profile': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'rai': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'rat-type': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'reordering-required': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'selection-mode': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'uli': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'}
                    }
                },
                'message-rate-limit': {
                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                    'type': 'dict',
                    'options': {
                        'create-aa-pdp-request': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'create-aa-pdp-response': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'create-mbms-request': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'create-mbms-response': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'create-pdp-request': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'create-pdp-response': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'delete-aa-pdp-request': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'delete-aa-pdp-response': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'delete-mbms-request': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'delete-mbms-response': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'delete-pdp-request': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'delete-pdp-response': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'echo-reponse': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'echo-request': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'error-indication': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'failure-report-request': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'failure-report-response': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'fwd-reloc-complete-ack': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'fwd-relocation-complete': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'fwd-relocation-request': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'fwd-relocation-response': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'fwd-srns-context': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'fwd-srns-context-ack': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'g-pdu': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'identification-request': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'identification-response': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'mbms-de-reg-request': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'mbms-de-reg-response': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'mbms-notify-rej-request': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'mbms-notify-rej-response': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'mbms-notify-request': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'mbms-notify-response': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'mbms-reg-request': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'mbms-reg-response': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'mbms-ses-start-request': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'mbms-ses-start-response': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'mbms-ses-stop-request': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'mbms-ses-stop-response': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'note-ms-request': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'note-ms-response': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'pdu-notify-rej-request': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'pdu-notify-rej-response': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'pdu-notify-request': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'pdu-notify-response': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'ran-info': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'relocation-cancel-request': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'relocation-cancel-response': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'send-route-request': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'send-route-response': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'sgsn-context-ack': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'sgsn-context-request': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'sgsn-context-response': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'support-ext-hdr-notify': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'update-mbms-request': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'update-mbms-response': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'update-pdp-request': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'update-pdp-response': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'version-not-support': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'echo-response': {'v_range': [['7.4.3', '']], 'type': 'int'}
                    }
                },
                'message-rate-limit-v0': {
                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                    'type': 'dict',
                    'options': {
                        'create-pdp-request': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'delete-pdp-request': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'echo-request': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'}
                    }
                },
                'message-rate-limit-v1': {
                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                    'type': 'dict',
                    'options': {
                        'create-pdp-request': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'delete-pdp-request': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'echo-request': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'}
                    }
                },
                'message-rate-limit-v2': {
                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                    'type': 'dict',
                    'options': {
                        'create-session-request': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'delete-session-request': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'echo-request': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'}
                    }
                },
                'ie-allow-list-v0v1': {'v_range': [['7.0.0', '']], 'type': 'str'},
                'ie-allow-list-v2': {'v_range': [['7.0.0', '']], 'type': 'str'},
                'rat-timeout-profile': {'v_range': [['7.0.1', '']], 'type': 'str'},
                'message-filter': {
                    'v_range': [['6.2.8', '6.2.12']],
                    'type': 'dict',
                    'options': {
                        'create-aa-pdp': {'v_range': [['6.2.8', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                        'create-mbms': {'v_range': [['6.2.8', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                        'create-pdp': {'v_range': [['6.2.8', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                        'data-record': {'v_range': [['6.2.8', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                        'delete-aa-pdp': {'v_range': [['6.2.8', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                        'delete-mbms': {'v_range': [['6.2.8', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                        'delete-pdp': {'v_range': [['6.2.8', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                        'echo': {'v_range': [['6.2.8', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                        'error-indication': {'v_range': [['6.2.8', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                        'failure-report': {'v_range': [['6.2.8', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                        'fwd-relocation': {'v_range': [['6.2.8', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                        'fwd-srns-context': {'v_range': [['6.2.8', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                        'gtp-pdu': {'v_range': [['6.2.8', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                        'identification': {'v_range': [['6.2.8', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                        'mbms-notification': {'v_range': [['6.2.8', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                        'node-alive': {'v_range': [['6.2.8', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                        'note-ms-present': {'v_range': [['6.2.8', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                        'pdu-notification': {'v_range': [['6.2.8', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                        'ran-info': {'v_range': [['6.2.8', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                        'redirection': {'v_range': [['6.2.8', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                        'relocation-cancel': {'v_range': [['6.2.8', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                        'send-route': {'v_range': [['6.2.8', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                        'sgsn-context': {'v_range': [['6.2.8', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                        'support-extension': {'v_range': [['6.2.8', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                        'unknown-message-action': {'v_range': [['6.2.8', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                        'update-mbms': {'v_range': [['6.2.8', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                        'update-pdp': {'v_range': [['6.2.8', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'},
                        'version-not-support': {'v_range': [['6.2.8', '6.2.12']], 'choices': ['allow', 'deny'], 'type': 'str'}
                    }
                },
                'gtpv0': {'v_range': [['7.6.0', '']], 'choices': ['allow', 'deny'], 'type': 'str'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('full crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'firewall_gtp'),
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
