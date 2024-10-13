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
module: fmgr_voip_profile
short_description: Configure VoIP profiles.
description:
    - This module is able to configure a FortiManager device.
    - Examples include all parameters and values which need to be adjusted to data sources before usage.

version_added: "1.0.0"
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
    voip_profile:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            comment:
                type: str
                description: Comment.
            name:
                type: str
                description: Profile name.
                required: true
            sccp:
                type: dict
                description: Sccp.
                suboptions:
                    block-mcast:
                        type: str
                        description: Deprecated, please rename it to block_mcast. Enable/disable block multicast RTP connections.
                        choices:
                            - 'disable'
                            - 'enable'
                    log-call-summary:
                        type: str
                        description: Deprecated, please rename it to log_call_summary. Enable/disable log summary of SCCP calls.
                        choices:
                            - 'disable'
                            - 'enable'
                    log-violations:
                        type: str
                        description: Deprecated, please rename it to log_violations. Enable/disable logging of SCCP violations.
                        choices:
                            - 'disable'
                            - 'enable'
                    max-calls:
                        type: int
                        description: Deprecated, please rename it to max_calls. Maximum calls per minute per SCCP client
                    status:
                        type: str
                        description: Enable/disable SCCP.
                        choices:
                            - 'disable'
                            - 'enable'
                    verify-header:
                        type: str
                        description: Deprecated, please rename it to verify_header. Enable/disable verify SCCP header content.
                        choices:
                            - 'disable'
                            - 'enable'
            sip:
                type: dict
                description: Sip.
                suboptions:
                    ack-rate:
                        type: int
                        description: Deprecated, please rename it to ack_rate. ACK request rate limit
                    block-ack:
                        type: str
                        description: Deprecated, please rename it to block_ack. Enable/disable block ACK requests.
                        choices:
                            - 'disable'
                            - 'enable'
                    block-bye:
                        type: str
                        description: Deprecated, please rename it to block_bye. Enable/disable block BYE requests.
                        choices:
                            - 'disable'
                            - 'enable'
                    block-cancel:
                        type: str
                        description: Deprecated, please rename it to block_cancel. Enable/disable block CANCEL requests.
                        choices:
                            - 'disable'
                            - 'enable'
                    block-geo-red-options:
                        type: str
                        description: Deprecated, please rename it to block_geo_red_options. Enable/disable block OPTIONS requests, but OPTIONS requests...
                        choices:
                            - 'disable'
                            - 'enable'
                    block-info:
                        type: str
                        description: Deprecated, please rename it to block_info. Enable/disable block INFO requests.
                        choices:
                            - 'disable'
                            - 'enable'
                    block-invite:
                        type: str
                        description: Deprecated, please rename it to block_invite. Enable/disable block INVITE requests.
                        choices:
                            - 'disable'
                            - 'enable'
                    block-long-lines:
                        type: str
                        description: Deprecated, please rename it to block_long_lines. Enable/disable block requests with headers exceeding max-line-le...
                        choices:
                            - 'disable'
                            - 'enable'
                    block-message:
                        type: str
                        description: Deprecated, please rename it to block_message. Enable/disable block MESSAGE requests.
                        choices:
                            - 'disable'
                            - 'enable'
                    block-notify:
                        type: str
                        description: Deprecated, please rename it to block_notify. Enable/disable block NOTIFY requests.
                        choices:
                            - 'disable'
                            - 'enable'
                    block-options:
                        type: str
                        description: Deprecated, please rename it to block_options. Enable/disable block OPTIONS requests and no OPTIONS as notifying m...
                        choices:
                            - 'disable'
                            - 'enable'
                    block-prack:
                        type: str
                        description: Deprecated, please rename it to block_prack. Enable/disable block prack requests.
                        choices:
                            - 'disable'
                            - 'enable'
                    block-publish:
                        type: str
                        description: Deprecated, please rename it to block_publish. Enable/disable block PUBLISH requests.
                        choices:
                            - 'disable'
                            - 'enable'
                    block-refer:
                        type: str
                        description: Deprecated, please rename it to block_refer. Enable/disable block REFER requests.
                        choices:
                            - 'disable'
                            - 'enable'
                    block-register:
                        type: str
                        description: Deprecated, please rename it to block_register. Enable/disable block REGISTER requests.
                        choices:
                            - 'disable'
                            - 'enable'
                    block-subscribe:
                        type: str
                        description: Deprecated, please rename it to block_subscribe. Enable/disable block SUBSCRIBE requests.
                        choices:
                            - 'disable'
                            - 'enable'
                    block-unknown:
                        type: str
                        description: Deprecated, please rename it to block_unknown. Block unrecognized SIP requests
                        choices:
                            - 'disable'
                            - 'enable'
                    block-update:
                        type: str
                        description: Deprecated, please rename it to block_update. Enable/disable block UPDATE requests.
                        choices:
                            - 'disable'
                            - 'enable'
                    bye-rate:
                        type: int
                        description: Deprecated, please rename it to bye_rate. BYE request rate limit
                    call-keepalive:
                        type: int
                        description: Deprecated, please rename it to call_keepalive. Continue tracking calls with no RTP for this many minutes.
                    cancel-rate:
                        type: int
                        description: Deprecated, please rename it to cancel_rate. CANCEL request rate limit
                    contact-fixup:
                        type: str
                        description: Deprecated, please rename it to contact_fixup. Fixup contact anyway even if contacts IP
                        choices:
                            - 'disable'
                            - 'enable'
                    hnt-restrict-source-ip:
                        type: str
                        description: Deprecated, please rename it to hnt_restrict_source_ip. Enable/disable restrict RTP source IP to be the same as SI...
                        choices:
                            - 'disable'
                            - 'enable'
                    hosted-nat-traversal:
                        type: str
                        description: Deprecated, please rename it to hosted_nat_traversal. Hosted NAT Traversal
                        choices:
                            - 'disable'
                            - 'enable'
                    info-rate:
                        type: int
                        description: Deprecated, please rename it to info_rate. INFO request rate limit
                    invite-rate:
                        type: int
                        description: Deprecated, please rename it to invite_rate. INVITE request rate limit
                    ips-rtp:
                        type: str
                        description: Deprecated, please rename it to ips_rtp. Enable/disable allow IPS on RTP.
                        choices:
                            - 'disable'
                            - 'enable'
                    log-call-summary:
                        type: str
                        description: Deprecated, please rename it to log_call_summary. Enable/disable logging of SIP call summary.
                        choices:
                            - 'disable'
                            - 'enable'
                    log-violations:
                        type: str
                        description: Deprecated, please rename it to log_violations. Enable/disable logging of SIP violations.
                        choices:
                            - 'disable'
                            - 'enable'
                    malformed-header-allow:
                        type: str
                        description: Deprecated, please rename it to malformed_header_allow. Action for malformed Allow header.
                        choices:
                            - 'pass'
                            - 'discard'
                            - 'respond'
                    malformed-header-call-id:
                        type: str
                        description: Deprecated, please rename it to malformed_header_call_id. Action for malformed Call-ID header.
                        choices:
                            - 'pass'
                            - 'discard'
                            - 'respond'
                    malformed-header-contact:
                        type: str
                        description: Deprecated, please rename it to malformed_header_contact. Action for malformed Contact header.
                        choices:
                            - 'pass'
                            - 'discard'
                            - 'respond'
                    malformed-header-content-length:
                        type: str
                        description: Deprecated, please rename it to malformed_header_content_length. Action for malformed Content-Length header.
                        choices:
                            - 'pass'
                            - 'discard'
                            - 'respond'
                    malformed-header-content-type:
                        type: str
                        description: Deprecated, please rename it to malformed_header_content_type. Action for malformed Content-Type header.
                        choices:
                            - 'pass'
                            - 'discard'
                            - 'respond'
                    malformed-header-cseq:
                        type: str
                        description: Deprecated, please rename it to malformed_header_cseq. Action for malformed CSeq header.
                        choices:
                            - 'pass'
                            - 'discard'
                            - 'respond'
                    malformed-header-expires:
                        type: str
                        description: Deprecated, please rename it to malformed_header_expires. Action for malformed Expires header.
                        choices:
                            - 'pass'
                            - 'discard'
                            - 'respond'
                    malformed-header-from:
                        type: str
                        description: Deprecated, please rename it to malformed_header_from. Action for malformed From header.
                        choices:
                            - 'pass'
                            - 'discard'
                            - 'respond'
                    malformed-header-max-forwards:
                        type: str
                        description: Deprecated, please rename it to malformed_header_max_forwards. Action for malformed Max-Forwards header.
                        choices:
                            - 'pass'
                            - 'discard'
                            - 'respond'
                    malformed-header-p-asserted-identity:
                        type: str
                        description: Deprecated, please rename it to malformed_header_p_asserted_identity. Action for malformed P-Asserted-Identity header.
                        choices:
                            - 'pass'
                            - 'discard'
                            - 'respond'
                    malformed-header-rack:
                        type: str
                        description: Deprecated, please rename it to malformed_header_rack. Action for malformed RAck header.
                        choices:
                            - 'pass'
                            - 'discard'
                            - 'respond'
                    malformed-header-record-route:
                        type: str
                        description: Deprecated, please rename it to malformed_header_record_route. Action for malformed Record-Route header.
                        choices:
                            - 'pass'
                            - 'discard'
                            - 'respond'
                    malformed-header-route:
                        type: str
                        description: Deprecated, please rename it to malformed_header_route. Action for malformed Route header.
                        choices:
                            - 'pass'
                            - 'discard'
                            - 'respond'
                    malformed-header-rseq:
                        type: str
                        description: Deprecated, please rename it to malformed_header_rseq. Action for malformed RSeq header.
                        choices:
                            - 'pass'
                            - 'discard'
                            - 'respond'
                    malformed-header-sdp-a:
                        type: str
                        description: Deprecated, please rename it to malformed_header_sdp_a. Action for malformed SDP a line.
                        choices:
                            - 'pass'
                            - 'discard'
                            - 'respond'
                    malformed-header-sdp-b:
                        type: str
                        description: Deprecated, please rename it to malformed_header_sdp_b. Action for malformed SDP b line.
                        choices:
                            - 'pass'
                            - 'discard'
                            - 'respond'
                    malformed-header-sdp-c:
                        type: str
                        description: Deprecated, please rename it to malformed_header_sdp_c. Action for malformed SDP c line.
                        choices:
                            - 'pass'
                            - 'discard'
                            - 'respond'
                    malformed-header-sdp-i:
                        type: str
                        description: Deprecated, please rename it to malformed_header_sdp_i. Action for malformed SDP i line.
                        choices:
                            - 'pass'
                            - 'discard'
                            - 'respond'
                    malformed-header-sdp-k:
                        type: str
                        description: Deprecated, please rename it to malformed_header_sdp_k. Action for malformed SDP k line.
                        choices:
                            - 'pass'
                            - 'discard'
                            - 'respond'
                    malformed-header-sdp-m:
                        type: str
                        description: Deprecated, please rename it to malformed_header_sdp_m. Action for malformed SDP m line.
                        choices:
                            - 'pass'
                            - 'discard'
                            - 'respond'
                    malformed-header-sdp-o:
                        type: str
                        description: Deprecated, please rename it to malformed_header_sdp_o. Action for malformed SDP o line.
                        choices:
                            - 'pass'
                            - 'discard'
                            - 'respond'
                    malformed-header-sdp-r:
                        type: str
                        description: Deprecated, please rename it to malformed_header_sdp_r. Action for malformed SDP r line.
                        choices:
                            - 'pass'
                            - 'discard'
                            - 'respond'
                    malformed-header-sdp-s:
                        type: str
                        description: Deprecated, please rename it to malformed_header_sdp_s. Action for malformed SDP s line.
                        choices:
                            - 'pass'
                            - 'discard'
                            - 'respond'
                    malformed-header-sdp-t:
                        type: str
                        description: Deprecated, please rename it to malformed_header_sdp_t. Action for malformed SDP t line.
                        choices:
                            - 'pass'
                            - 'discard'
                            - 'respond'
                    malformed-header-sdp-v:
                        type: str
                        description: Deprecated, please rename it to malformed_header_sdp_v. Action for malformed SDP v line.
                        choices:
                            - 'pass'
                            - 'discard'
                            - 'respond'
                    malformed-header-sdp-z:
                        type: str
                        description: Deprecated, please rename it to malformed_header_sdp_z. Action for malformed SDP z line.
                        choices:
                            - 'pass'
                            - 'discard'
                            - 'respond'
                    malformed-header-to:
                        type: str
                        description: Deprecated, please rename it to malformed_header_to. Action for malformed To header.
                        choices:
                            - 'pass'
                            - 'discard'
                            - 'respond'
                    malformed-header-via:
                        type: str
                        description: Deprecated, please rename it to malformed_header_via. Action for malformed VIA header.
                        choices:
                            - 'pass'
                            - 'discard'
                            - 'respond'
                    malformed-request-line:
                        type: str
                        description: Deprecated, please rename it to malformed_request_line. Action for malformed request line.
                        choices:
                            - 'pass'
                            - 'discard'
                            - 'respond'
                    max-body-length:
                        type: int
                        description: Deprecated, please rename it to max_body_length. Maximum SIP message body length
                    max-dialogs:
                        type: int
                        description: Deprecated, please rename it to max_dialogs. Maximum number of concurrent calls/dialogs
                    max-idle-dialogs:
                        type: int
                        description: Deprecated, please rename it to max_idle_dialogs. Maximum number established but idle dialogs to retain
                    max-line-length:
                        type: int
                        description: Deprecated, please rename it to max_line_length. Maximum SIP header line length
                    message-rate:
                        type: int
                        description: Deprecated, please rename it to message_rate. MESSAGE request rate limit
                    nat-port-range:
                        type: str
                        description: Deprecated, please rename it to nat_port_range. RTP NAT port range.
                    nat-trace:
                        type: str
                        description: Deprecated, please rename it to nat_trace. Enable/disable preservation of original IP in SDP i line.
                        choices:
                            - 'disable'
                            - 'enable'
                    no-sdp-fixup:
                        type: str
                        description: Deprecated, please rename it to no_sdp_fixup. Enable/disable no SDP fix-up.
                        choices:
                            - 'disable'
                            - 'enable'
                    notify-rate:
                        type: int
                        description: Deprecated, please rename it to notify_rate. NOTIFY request rate limit
                    open-contact-pinhole:
                        type: str
                        description: Deprecated, please rename it to open_contact_pinhole. Enable/disable open pinhole for non-REGISTER Contact port.
                        choices:
                            - 'disable'
                            - 'enable'
                    open-record-route-pinhole:
                        type: str
                        description: Deprecated, please rename it to open_record_route_pinhole. Enable/disable open pinhole for Record-Route port.
                        choices:
                            - 'disable'
                            - 'enable'
                    open-register-pinhole:
                        type: str
                        description: Deprecated, please rename it to open_register_pinhole. Enable/disable open pinhole for REGISTER Contact port.
                        choices:
                            - 'disable'
                            - 'enable'
                    open-via-pinhole:
                        type: str
                        description: Deprecated, please rename it to open_via_pinhole. Enable/disable open pinhole for Via port.
                        choices:
                            - 'disable'
                            - 'enable'
                    options-rate:
                        type: int
                        description: Deprecated, please rename it to options_rate. OPTIONS request rate limit
                    prack-rate:
                        type: int
                        description: Deprecated, please rename it to prack_rate. PRACK request rate limit
                    preserve-override:
                        type: str
                        description: Deprecated, please rename it to preserve_override. Override i line to preserve original IPS
                        choices:
                            - 'disable'
                            - 'enable'
                    provisional-invite-expiry-time:
                        type: int
                        description: Deprecated, please rename it to provisional_invite_expiry_time. Expiry time for provisional INVITE
                    publish-rate:
                        type: int
                        description: Deprecated, please rename it to publish_rate. PUBLISH request rate limit
                    refer-rate:
                        type: int
                        description: Deprecated, please rename it to refer_rate. REFER request rate limit
                    register-contact-trace:
                        type: str
                        description: Deprecated, please rename it to register_contact_trace. Enable/disable trace original IP/port within the contact h...
                        choices:
                            - 'disable'
                            - 'enable'
                    register-rate:
                        type: int
                        description: Deprecated, please rename it to register_rate. REGISTER request rate limit
                    rfc2543-branch:
                        type: str
                        description: Deprecated, please rename it to rfc2543_branch. Enable/disable support via branch compliant with RFC 2543.
                        choices:
                            - 'disable'
                            - 'enable'
                    rtp:
                        type: str
                        description: Enable/disable create pinholes for RTP traffic to traverse firewall.
                        choices:
                            - 'disable'
                            - 'enable'
                    ssl-algorithm:
                        type: str
                        description: Deprecated, please rename it to ssl_algorithm. Relative strength of encryption algorithms accepted in negotiation.
                        choices:
                            - 'high'
                            - 'medium'
                            - 'low'
                    ssl-auth-client:
                        type: str
                        description: Deprecated, please rename it to ssl_auth_client. Require a client certificate and authenticate it with the peer/pe...
                    ssl-auth-server:
                        type: str
                        description: Deprecated, please rename it to ssl_auth_server. Authenticate the servers certificate with the peer/peergrp.
                    ssl-client-certificate:
                        type: str
                        description: Deprecated, please rename it to ssl_client_certificate. Name of Certificate to offer to server if requested.
                    ssl-client-renegotiation:
                        type: str
                        description: Deprecated, please rename it to ssl_client_renegotiation. Allow/block client renegotiation by server.
                        choices:
                            - 'allow'
                            - 'deny'
                            - 'secure'
                    ssl-max-version:
                        type: str
                        description: Deprecated, please rename it to ssl_max_version. Highest SSL/TLS version to negotiate.
                        choices:
                            - 'ssl-3.0'
                            - 'tls-1.0'
                            - 'tls-1.1'
                            - 'tls-1.2'
                            - 'tls-1.3'
                    ssl-min-version:
                        type: str
                        description: Deprecated, please rename it to ssl_min_version. Lowest SSL/TLS version to negotiate.
                        choices:
                            - 'ssl-3.0'
                            - 'tls-1.0'
                            - 'tls-1.1'
                            - 'tls-1.2'
                            - 'tls-1.3'
                    ssl-mode:
                        type: str
                        description: Deprecated, please rename it to ssl_mode. SSL/TLS mode for encryption & decryption of traffic.
                        choices:
                            - 'off'
                            - 'full'
                    ssl-pfs:
                        type: str
                        description: Deprecated, please rename it to ssl_pfs. SSL Perfect Forward Secrecy.
                        choices:
                            - 'require'
                            - 'deny'
                            - 'allow'
                    ssl-send-empty-frags:
                        type: str
                        description: Deprecated, please rename it to ssl_send_empty_frags. Send empty fragments to avoid attack on CBC IV
                        choices:
                            - 'disable'
                            - 'enable'
                    ssl-server-certificate:
                        type: str
                        description: Deprecated, please rename it to ssl_server_certificate. Name of Certificate return to the client in every SSL conn...
                    status:
                        type: str
                        description: Enable/disable SIP.
                        choices:
                            - 'disable'
                            - 'enable'
                    strict-register:
                        type: str
                        description: Deprecated, please rename it to strict_register. Enable/disable only allow the registrar to connect.
                        choices:
                            - 'disable'
                            - 'enable'
                    subscribe-rate:
                        type: int
                        description: Deprecated, please rename it to subscribe_rate. SUBSCRIBE request rate limit
                    unknown-header:
                        type: str
                        description: Deprecated, please rename it to unknown_header. Action for unknown SIP header.
                        choices:
                            - 'pass'
                            - 'discard'
                            - 'respond'
                    update-rate:
                        type: int
                        description: Deprecated, please rename it to update_rate. UPDATE request rate limit
                    ack-rate-track:
                        type: str
                        description: Deprecated, please rename it to ack_rate_track. Track the packet protocol field.
                        choices:
                            - 'none'
                            - 'src-ip'
                            - 'dest-ip'
                    bye-rate-track:
                        type: str
                        description: Deprecated, please rename it to bye_rate_track. Track the packet protocol field.
                        choices:
                            - 'none'
                            - 'src-ip'
                            - 'dest-ip'
                    cancel-rate-track:
                        type: str
                        description: Deprecated, please rename it to cancel_rate_track. Track the packet protocol field.
                        choices:
                            - 'none'
                            - 'src-ip'
                            - 'dest-ip'
                    info-rate-track:
                        type: str
                        description: Deprecated, please rename it to info_rate_track. Track the packet protocol field.
                        choices:
                            - 'none'
                            - 'src-ip'
                            - 'dest-ip'
                    invite-rate-track:
                        type: str
                        description: Deprecated, please rename it to invite_rate_track. Track the packet protocol field.
                        choices:
                            - 'none'
                            - 'src-ip'
                            - 'dest-ip'
                    malformed-header-no-proxy-require:
                        type: str
                        description: Deprecated, please rename it to malformed_header_no_proxy_require. Action for malformed SIP messages without Proxy...
                        choices:
                            - 'pass'
                            - 'discard'
                            - 'respond'
                    malformed-header-no-require:
                        type: str
                        description: Deprecated, please rename it to malformed_header_no_require. Action for malformed SIP messages without Require header.
                        choices:
                            - 'pass'
                            - 'discard'
                            - 'respond'
                    message-rate-track:
                        type: str
                        description: Deprecated, please rename it to message_rate_track. Track the packet protocol field.
                        choices:
                            - 'none'
                            - 'src-ip'
                            - 'dest-ip'
                    notify-rate-track:
                        type: str
                        description: Deprecated, please rename it to notify_rate_track. Track the packet protocol field.
                        choices:
                            - 'none'
                            - 'src-ip'
                            - 'dest-ip'
                    options-rate-track:
                        type: str
                        description: Deprecated, please rename it to options_rate_track. Track the packet protocol field.
                        choices:
                            - 'none'
                            - 'src-ip'
                            - 'dest-ip'
                    prack-rate-track:
                        type: str
                        description: Deprecated, please rename it to prack_rate_track. Track the packet protocol field.
                        choices:
                            - 'none'
                            - 'src-ip'
                            - 'dest-ip'
                    publish-rate-track:
                        type: str
                        description: Deprecated, please rename it to publish_rate_track. Track the packet protocol field.
                        choices:
                            - 'none'
                            - 'src-ip'
                            - 'dest-ip'
                    refer-rate-track:
                        type: str
                        description: Deprecated, please rename it to refer_rate_track. Track the packet protocol field.
                        choices:
                            - 'none'
                            - 'src-ip'
                            - 'dest-ip'
                    register-rate-track:
                        type: str
                        description: Deprecated, please rename it to register_rate_track. Track the packet protocol field.
                        choices:
                            - 'none'
                            - 'src-ip'
                            - 'dest-ip'
                    subscribe-rate-track:
                        type: str
                        description: Deprecated, please rename it to subscribe_rate_track. Track the packet protocol field.
                        choices:
                            - 'none'
                            - 'src-ip'
                            - 'dest-ip'
                    update-rate-track:
                        type: str
                        description: Deprecated, please rename it to update_rate_track. Track the packet protocol field.
                        choices:
                            - 'none'
                            - 'src-ip'
                            - 'dest-ip'
                    call-id-regex:
                        type: str
                        description: Deprecated, please rename it to call_id_regex. Validate PCRE regular expression for Call-Id header value.
                    content-type-regex:
                        type: str
                        description: Deprecated, please rename it to content_type_regex. Validate PCRE regular expression for Content-Type header value.
            feature-set:
                type: str
                description: Deprecated, please rename it to feature_set. Flow or proxy inspection feature set.
                choices:
                    - 'flow'
                    - 'proxy'
                    - 'ips'
                    - 'voipd'
            msrp:
                type: dict
                description: Msrp.
                suboptions:
                    log-violations:
                        type: str
                        description: Deprecated, please rename it to log_violations. Enable/disable logging of MSRP violations.
                        choices:
                            - 'disable'
                            - 'enable'
                    max-msg-size:
                        type: int
                        description: Deprecated, please rename it to max_msg_size. Maximum allowable MSRP message size
                    max-msg-size-action:
                        type: str
                        description: Deprecated, please rename it to max_msg_size_action. Action for violation of max-msg-size.
                        choices:
                            - 'pass'
                            - 'block'
                            - 'reset'
                            - 'monitor'
                    status:
                        type: str
                        description: Enable/disable MSRP.
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
    - name: Configure VoIP profiles.
      fortinet.fortimanager.fmgr_voip_profile:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: present # <value in [present, absent]>
        voip_profile:
          comment: <string>
          name: <string>
          sccp:
            block_mcast: <value in [disable, enable]>
            log_call_summary: <value in [disable, enable]>
            log_violations: <value in [disable, enable]>
            max_calls: <integer>
            status: <value in [disable, enable]>
            verify_header: <value in [disable, enable]>
          sip:
            ack_rate: <integer>
            block_ack: <value in [disable, enable]>
            block_bye: <value in [disable, enable]>
            block_cancel: <value in [disable, enable]>
            block_geo_red_options: <value in [disable, enable]>
            block_info: <value in [disable, enable]>
            block_invite: <value in [disable, enable]>
            block_long_lines: <value in [disable, enable]>
            block_message: <value in [disable, enable]>
            block_notify: <value in [disable, enable]>
            block_options: <value in [disable, enable]>
            block_prack: <value in [disable, enable]>
            block_publish: <value in [disable, enable]>
            block_refer: <value in [disable, enable]>
            block_register: <value in [disable, enable]>
            block_subscribe: <value in [disable, enable]>
            block_unknown: <value in [disable, enable]>
            block_update: <value in [disable, enable]>
            bye_rate: <integer>
            call_keepalive: <integer>
            cancel_rate: <integer>
            contact_fixup: <value in [disable, enable]>
            hnt_restrict_source_ip: <value in [disable, enable]>
            hosted_nat_traversal: <value in [disable, enable]>
            info_rate: <integer>
            invite_rate: <integer>
            ips_rtp: <value in [disable, enable]>
            log_call_summary: <value in [disable, enable]>
            log_violations: <value in [disable, enable]>
            malformed_header_allow: <value in [pass, discard, respond]>
            malformed_header_call_id: <value in [pass, discard, respond]>
            malformed_header_contact: <value in [pass, discard, respond]>
            malformed_header_content_length: <value in [pass, discard, respond]>
            malformed_header_content_type: <value in [pass, discard, respond]>
            malformed_header_cseq: <value in [pass, discard, respond]>
            malformed_header_expires: <value in [pass, discard, respond]>
            malformed_header_from: <value in [pass, discard, respond]>
            malformed_header_max_forwards: <value in [pass, discard, respond]>
            malformed_header_p_asserted_identity: <value in [pass, discard, respond]>
            malformed_header_rack: <value in [pass, discard, respond]>
            malformed_header_record_route: <value in [pass, discard, respond]>
            malformed_header_route: <value in [pass, discard, respond]>
            malformed_header_rseq: <value in [pass, discard, respond]>
            malformed_header_sdp_a: <value in [pass, discard, respond]>
            malformed_header_sdp_b: <value in [pass, discard, respond]>
            malformed_header_sdp_c: <value in [pass, discard, respond]>
            malformed_header_sdp_i: <value in [pass, discard, respond]>
            malformed_header_sdp_k: <value in [pass, discard, respond]>
            malformed_header_sdp_m: <value in [pass, discard, respond]>
            malformed_header_sdp_o: <value in [pass, discard, respond]>
            malformed_header_sdp_r: <value in [pass, discard, respond]>
            malformed_header_sdp_s: <value in [pass, discard, respond]>
            malformed_header_sdp_t: <value in [pass, discard, respond]>
            malformed_header_sdp_v: <value in [pass, discard, respond]>
            malformed_header_sdp_z: <value in [pass, discard, respond]>
            malformed_header_to: <value in [pass, discard, respond]>
            malformed_header_via: <value in [pass, discard, respond]>
            malformed_request_line: <value in [pass, discard, respond]>
            max_body_length: <integer>
            max_dialogs: <integer>
            max_idle_dialogs: <integer>
            max_line_length: <integer>
            message_rate: <integer>
            nat_port_range: <string>
            nat_trace: <value in [disable, enable]>
            no_sdp_fixup: <value in [disable, enable]>
            notify_rate: <integer>
            open_contact_pinhole: <value in [disable, enable]>
            open_record_route_pinhole: <value in [disable, enable]>
            open_register_pinhole: <value in [disable, enable]>
            open_via_pinhole: <value in [disable, enable]>
            options_rate: <integer>
            prack_rate: <integer>
            preserve_override: <value in [disable, enable]>
            provisional_invite_expiry_time: <integer>
            publish_rate: <integer>
            refer_rate: <integer>
            register_contact_trace: <value in [disable, enable]>
            register_rate: <integer>
            rfc2543_branch: <value in [disable, enable]>
            rtp: <value in [disable, enable]>
            ssl_algorithm: <value in [high, medium, low]>
            ssl_auth_client: <string>
            ssl_auth_server: <string>
            ssl_client_certificate: <string>
            ssl_client_renegotiation: <value in [allow, deny, secure]>
            ssl_max_version: <value in [ssl-3.0, tls-1.0, tls-1.1, ...]>
            ssl_min_version: <value in [ssl-3.0, tls-1.0, tls-1.1, ...]>
            ssl_mode: <value in [off, full]>
            ssl_pfs: <value in [require, deny, allow]>
            ssl_send_empty_frags: <value in [disable, enable]>
            ssl_server_certificate: <string>
            status: <value in [disable, enable]>
            strict_register: <value in [disable, enable]>
            subscribe_rate: <integer>
            unknown_header: <value in [pass, discard, respond]>
            update_rate: <integer>
            ack_rate_track: <value in [none, src-ip, dest-ip]>
            bye_rate_track: <value in [none, src-ip, dest-ip]>
            cancel_rate_track: <value in [none, src-ip, dest-ip]>
            info_rate_track: <value in [none, src-ip, dest-ip]>
            invite_rate_track: <value in [none, src-ip, dest-ip]>
            malformed_header_no_proxy_require: <value in [pass, discard, respond]>
            malformed_header_no_require: <value in [pass, discard, respond]>
            message_rate_track: <value in [none, src-ip, dest-ip]>
            notify_rate_track: <value in [none, src-ip, dest-ip]>
            options_rate_track: <value in [none, src-ip, dest-ip]>
            prack_rate_track: <value in [none, src-ip, dest-ip]>
            publish_rate_track: <value in [none, src-ip, dest-ip]>
            refer_rate_track: <value in [none, src-ip, dest-ip]>
            register_rate_track: <value in [none, src-ip, dest-ip]>
            subscribe_rate_track: <value in [none, src-ip, dest-ip]>
            update_rate_track: <value in [none, src-ip, dest-ip]>
            call_id_regex: <string>
            content_type_regex: <string>
          feature_set: <value in [flow, proxy, ips, ...]>
          msrp:
            log_violations: <value in [disable, enable]>
            max_msg_size: <integer>
            max_msg_size_action: <value in [pass, block, reset, ...]>
            status: <value in [disable, enable]>
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
        '/pm/config/adom/{adom}/obj/voip/profile',
        '/pm/config/global/obj/voip/profile'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/voip/profile/{profile}',
        '/pm/config/global/obj/voip/profile/{profile}'
    ]

    url_params = ['adom']
    module_primary_key = 'name'
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'voip_profile': {
            'type': 'dict',
            'v_range': [['6.0.0', '']],
            'options': {
                'comment': {'type': 'str'},
                'name': {'required': True, 'type': 'str'},
                'sccp': {
                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                    'type': 'dict',
                    'options': {
                        'block-mcast': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'log-call-summary': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'log-violations': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'max-calls': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'status': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'verify-header': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'}
                    }
                },
                'sip': {
                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                    'type': 'dict',
                    'options': {
                        'ack-rate': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'block-ack': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'block-bye': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'block-cancel': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'block-geo-red-options': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'block-info': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'block-invite': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'block-long-lines': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'block-message': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'block-notify': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'block-options': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'block-prack': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'block-publish': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'block-refer': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'block-register': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'block-subscribe': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'block-unknown': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'block-update': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'bye-rate': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'call-keepalive': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'cancel-rate': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'contact-fixup': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'hnt-restrict-source-ip': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'hosted-nat-traversal': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'info-rate': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'invite-rate': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'ips-rtp': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'log-call-summary': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'log-violations': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'malformed-header-allow': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['pass', 'discard', 'respond'],
                            'type': 'str'
                        },
                        'malformed-header-call-id': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['pass', 'discard', 'respond'],
                            'type': 'str'
                        },
                        'malformed-header-contact': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['pass', 'discard', 'respond'],
                            'type': 'str'
                        },
                        'malformed-header-content-length': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['pass', 'discard', 'respond'],
                            'type': 'str'
                        },
                        'malformed-header-content-type': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['pass', 'discard', 'respond'],
                            'type': 'str'
                        },
                        'malformed-header-cseq': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['pass', 'discard', 'respond'],
                            'type': 'str'
                        },
                        'malformed-header-expires': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['pass', 'discard', 'respond'],
                            'type': 'str'
                        },
                        'malformed-header-from': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['pass', 'discard', 'respond'],
                            'type': 'str'
                        },
                        'malformed-header-max-forwards': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['pass', 'discard', 'respond'],
                            'type': 'str'
                        },
                        'malformed-header-p-asserted-identity': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['pass', 'discard', 'respond'],
                            'type': 'str'
                        },
                        'malformed-header-rack': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['pass', 'discard', 'respond'],
                            'type': 'str'
                        },
                        'malformed-header-record-route': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['pass', 'discard', 'respond'],
                            'type': 'str'
                        },
                        'malformed-header-route': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['pass', 'discard', 'respond'],
                            'type': 'str'
                        },
                        'malformed-header-rseq': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['pass', 'discard', 'respond'],
                            'type': 'str'
                        },
                        'malformed-header-sdp-a': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['pass', 'discard', 'respond'],
                            'type': 'str'
                        },
                        'malformed-header-sdp-b': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['pass', 'discard', 'respond'],
                            'type': 'str'
                        },
                        'malformed-header-sdp-c': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['pass', 'discard', 'respond'],
                            'type': 'str'
                        },
                        'malformed-header-sdp-i': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['pass', 'discard', 'respond'],
                            'type': 'str'
                        },
                        'malformed-header-sdp-k': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['pass', 'discard', 'respond'],
                            'type': 'str'
                        },
                        'malformed-header-sdp-m': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['pass', 'discard', 'respond'],
                            'type': 'str'
                        },
                        'malformed-header-sdp-o': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['pass', 'discard', 'respond'],
                            'type': 'str'
                        },
                        'malformed-header-sdp-r': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['pass', 'discard', 'respond'],
                            'type': 'str'
                        },
                        'malformed-header-sdp-s': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['pass', 'discard', 'respond'],
                            'type': 'str'
                        },
                        'malformed-header-sdp-t': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['pass', 'discard', 'respond'],
                            'type': 'str'
                        },
                        'malformed-header-sdp-v': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['pass', 'discard', 'respond'],
                            'type': 'str'
                        },
                        'malformed-header-sdp-z': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['pass', 'discard', 'respond'],
                            'type': 'str'
                        },
                        'malformed-header-to': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['pass', 'discard', 'respond'], 'type': 'str'},
                        'malformed-header-via': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['pass', 'discard', 'respond'],
                            'type': 'str'
                        },
                        'malformed-request-line': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['pass', 'discard', 'respond'],
                            'type': 'str'
                        },
                        'max-body-length': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'max-dialogs': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'max-idle-dialogs': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'max-line-length': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'message-rate': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'nat-port-range': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'nat-trace': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'no-sdp-fixup': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'notify-rate': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'open-contact-pinhole': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'open-record-route-pinhole': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'open-register-pinhole': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'open-via-pinhole': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'options-rate': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'prack-rate': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'preserve-override': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'provisional-invite-expiry-time': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'publish-rate': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'refer-rate': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'register-contact-trace': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'register-rate': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'rfc2543-branch': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'rtp': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'ssl-algorithm': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['high', 'medium', 'low'], 'type': 'str'},
                        'ssl-auth-client': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'ssl-auth-server': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'ssl-client-certificate': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'ssl-client-renegotiation': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['allow', 'deny', 'secure'],
                            'type': 'str'
                        },
                        'ssl-max-version': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['ssl-3.0', 'tls-1.0', 'tls-1.1', 'tls-1.2', 'tls-1.3'],
                            'type': 'str'
                        },
                        'ssl-min-version': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['ssl-3.0', 'tls-1.0', 'tls-1.1', 'tls-1.2', 'tls-1.3'],
                            'type': 'str'
                        },
                        'ssl-mode': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['off', 'full'], 'type': 'str'},
                        'ssl-pfs': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['require', 'deny', 'allow'], 'type': 'str'},
                        'ssl-send-empty-frags': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'ssl-server-certificate': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'status': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'strict-register': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'subscribe-rate': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'unknown-header': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['pass', 'discard', 'respond'], 'type': 'str'},
                        'update-rate': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'ack-rate-track': {'v_range': [['7.0.0', '']], 'choices': ['none', 'src-ip', 'dest-ip'], 'type': 'str'},
                        'bye-rate-track': {'v_range': [['7.0.0', '']], 'choices': ['none', 'src-ip', 'dest-ip'], 'type': 'str'},
                        'cancel-rate-track': {'v_range': [['7.0.0', '']], 'choices': ['none', 'src-ip', 'dest-ip'], 'type': 'str'},
                        'info-rate-track': {'v_range': [['7.0.0', '']], 'choices': ['none', 'src-ip', 'dest-ip'], 'type': 'str'},
                        'invite-rate-track': {'v_range': [['7.0.0', '']], 'choices': ['none', 'src-ip', 'dest-ip'], 'type': 'str'},
                        'malformed-header-no-proxy-require': {'v_range': [['7.0.0', '']], 'choices': ['pass', 'discard', 'respond'], 'type': 'str'},
                        'malformed-header-no-require': {'v_range': [['7.0.0', '']], 'choices': ['pass', 'discard', 'respond'], 'type': 'str'},
                        'message-rate-track': {'v_range': [['7.0.0', '']], 'choices': ['none', 'src-ip', 'dest-ip'], 'type': 'str'},
                        'notify-rate-track': {'v_range': [['7.0.0', '']], 'choices': ['none', 'src-ip', 'dest-ip'], 'type': 'str'},
                        'options-rate-track': {'v_range': [['7.0.0', '']], 'choices': ['none', 'src-ip', 'dest-ip'], 'type': 'str'},
                        'prack-rate-track': {'v_range': [['7.0.0', '']], 'choices': ['none', 'src-ip', 'dest-ip'], 'type': 'str'},
                        'publish-rate-track': {'v_range': [['7.0.0', '']], 'choices': ['none', 'src-ip', 'dest-ip'], 'type': 'str'},
                        'refer-rate-track': {'v_range': [['7.0.0', '']], 'choices': ['none', 'src-ip', 'dest-ip'], 'type': 'str'},
                        'register-rate-track': {'v_range': [['7.0.0', '']], 'choices': ['none', 'src-ip', 'dest-ip'], 'type': 'str'},
                        'subscribe-rate-track': {'v_range': [['7.0.0', '']], 'choices': ['none', 'src-ip', 'dest-ip'], 'type': 'str'},
                        'update-rate-track': {'v_range': [['7.0.0', '']], 'choices': ['none', 'src-ip', 'dest-ip'], 'type': 'str'},
                        'call-id-regex': {'v_range': [['7.2.3', '']], 'type': 'str'},
                        'content-type-regex': {'v_range': [['7.2.3', '']], 'type': 'str'}
                    }
                },
                'feature-set': {'v_range': [['7.0.0', '']], 'choices': ['flow', 'proxy', 'ips', 'voipd'], 'type': 'str'},
                'msrp': {
                    'v_range': [['7.0.2', '']],
                    'type': 'dict',
                    'options': {
                        'log-violations': {'v_range': [['7.0.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'max-msg-size': {'v_range': [['7.0.2', '']], 'type': 'int'},
                        'max-msg-size-action': {'v_range': [['7.0.2', '']], 'choices': ['pass', 'block', 'reset', 'monitor'], 'type': 'str'},
                        'status': {'v_range': [['7.0.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'}
                    }
                }
            }

        }
    }

    module_option_spec = get_module_arg_spec('full crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'voip_profile'),
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
