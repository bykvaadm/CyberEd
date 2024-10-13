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
module: fmgr_firewall_profileprotocoloptions
short_description: Configure protocol options.
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
    firewall_profileprotocoloptions:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            comment:
                type: str
                description: Optional comments.
            name:
                type: str
                description: Name.
                required: true
            oversize-log:
                type: str
                description: Deprecated, please rename it to oversize_log. Enable/disable logging for antivirus oversize file blocking.
                choices:
                    - 'disable'
                    - 'enable'
            replacemsg-group:
                type: str
                description: Deprecated, please rename it to replacemsg_group. Name of the replacement message group to be used
            rpc-over-http:
                type: str
                description: Deprecated, please rename it to rpc_over_http. Enable/disable inspection of RPC over HTTP.
                choices:
                    - 'disable'
                    - 'enable'
            switching-protocols-log:
                type: str
                description: Deprecated, please rename it to switching_protocols_log. Enable/disable logging for HTTP/HTTPS switching protocols.
                choices:
                    - 'disable'
                    - 'enable'
            feature-set:
                type: str
                description: Deprecated, please rename it to feature_set. Flow/proxy feature set.
                choices:
                    - 'proxy'
                    - 'flow'
            cifs:
                type: dict
                description: Cifs.
                suboptions:
                    domain-controller:
                        type: str
                        description: Deprecated, please rename it to domain_controller. Domain for which to decrypt CIFS traffic.
                    file-filter:
                        type: dict
                        description: Deprecated, please rename it to file_filter. File filter.
                        suboptions:
                            entries:
                                type: list
                                elements: dict
                                description: Entries.
                                suboptions:
                                    action:
                                        type: str
                                        description: Action taken for matched file.
                                        choices:
                                            - 'log'
                                            - 'block'
                                    comment:
                                        type: str
                                        description: Comment.
                                    direction:
                                        type: str
                                        description: Match files transmitted in the sessions originating or reply direction.
                                        choices:
                                            - 'any'
                                            - 'incoming'
                                            - 'outgoing'
                                    file-type:
                                        type: raw
                                        description: (list) Deprecated, please rename it to file_type. Select file type.
                                    filter:
                                        type: str
                                        description: Add a file filter.
                                    protocol:
                                        type: list
                                        elements: str
                                        description: Protocols to apply with.
                                        choices:
                                            - 'cifs'
                            log:
                                type: str
                                description: Enable/disable file filter logging.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            status:
                                type: str
                                description: Enable/disable file filter.
                                choices:
                                    - 'disable'
                                    - 'enable'
                    options:
                        type: list
                        elements: str
                        description: One or more options that can be applied to the session.
                        choices:
                            - 'oversize'
                    oversize-limit:
                        type: int
                        description: Deprecated, please rename it to oversize_limit. Maximum in-memory file size that can be scanned
                    ports:
                        type: raw
                        description: (list) Ports to scan for content
                    scan-bzip2:
                        type: str
                        description: Deprecated, please rename it to scan_bzip2. Enable/disable scanning of BZip2 compressed files.
                        choices:
                            - 'disable'
                            - 'enable'
                    server-credential-type:
                        type: str
                        description: Deprecated, please rename it to server_credential_type. CIFS server credential type.
                        choices:
                            - 'none'
                            - 'credential-replication'
                            - 'credential-keytab'
                    server-keytab:
                        type: list
                        elements: dict
                        description: Deprecated, please rename it to server_keytab. Server keytab.
                        suboptions:
                            keytab:
                                type: str
                                description: Base64 encoded keytab file containing credential of the server.
                            password:
                                type: raw
                                description: (list) Password for keytab.
                            principal:
                                type: str
                                description: Service principal.
                    status:
                        type: str
                        description: Enable/disable the active status of scanning for this protocol.
                        choices:
                            - 'disable'
                            - 'enable'
                    tcp-window-maximum:
                        type: int
                        description: Deprecated, please rename it to tcp_window_maximum. Maximum dynamic TCP window size
                    tcp-window-minimum:
                        type: int
                        description: Deprecated, please rename it to tcp_window_minimum. Minimum dynamic TCP window size
                    tcp-window-size:
                        type: int
                        description: Deprecated, please rename it to tcp_window_size. Set TCP static window size
                    tcp-window-type:
                        type: str
                        description: Deprecated, please rename it to tcp_window_type. Specify type of TCP window to use for this protocol.
                        choices:
                            - 'system'
                            - 'static'
                            - 'dynamic'
                            - 'auto-tuning'
                    uncompressed-nest-limit:
                        type: int
                        description: Deprecated, please rename it to uncompressed_nest_limit. Maximum nested levels of compression that can be uncompre...
                    uncompressed-oversize-limit:
                        type: int
                        description: Deprecated, please rename it to uncompressed_oversize_limit. Maximum in-memory uncompressed file size that can be ...
            dns:
                type: dict
                description: Dns.
                suboptions:
                    ports:
                        type: raw
                        description: (list) Ports to scan for content
                    status:
                        type: str
                        description: Enable/disable the active status of scanning for this protocol.
                        choices:
                            - 'disable'
                            - 'enable'
            ftp:
                type: dict
                description: Ftp.
                suboptions:
                    comfort-amount:
                        type: int
                        description: Deprecated, please rename it to comfort_amount. Amount of data to send in a transmission for client comforting
                    comfort-interval:
                        type: int
                        description: Deprecated, please rename it to comfort_interval. Period of time between start, or last transmission, and the next...
                    inspect-all:
                        type: str
                        description: Deprecated, please rename it to inspect_all. Enable/disable the inspection of all ports for the protocol.
                        choices:
                            - 'disable'
                            - 'enable'
                    options:
                        type: list
                        elements: str
                        description: One or more options that can be applied to the session.
                        choices:
                            - 'clientcomfort'
                            - 'no-content-summary'
                            - 'oversize'
                            - 'splice'
                            - 'bypass-rest-command'
                            - 'bypass-mode-command'
                    oversize-limit:
                        type: int
                        description: Deprecated, please rename it to oversize_limit. Maximum in-memory file size that can be scanned
                    ports:
                        type: raw
                        description: (list) Ports to scan for content
                    scan-bzip2:
                        type: str
                        description: Deprecated, please rename it to scan_bzip2. Enable/disable scanning of BZip2 compressed files.
                        choices:
                            - 'disable'
                            - 'enable'
                    ssl-offloaded:
                        type: str
                        description: Deprecated, please rename it to ssl_offloaded. SSL decryption and encryption performed by an external device.
                        choices:
                            - 'no'
                            - 'yes'
                    status:
                        type: str
                        description: Enable/disable the active status of scanning for this protocol.
                        choices:
                            - 'disable'
                            - 'enable'
                    uncompressed-nest-limit:
                        type: int
                        description: Deprecated, please rename it to uncompressed_nest_limit. Maximum nested levels of compression that can be uncompre...
                    uncompressed-oversize-limit:
                        type: int
                        description: Deprecated, please rename it to uncompressed_oversize_limit. Maximum in-memory uncompressed file size that can be ...
                    stream-based-uncompressed-limit:
                        type: int
                        description: Deprecated, please rename it to stream_based_uncompressed_limit. Maximum stream-based uncompressed data size that ...
                    tcp-window-maximum:
                        type: int
                        description: Deprecated, please rename it to tcp_window_maximum. Maximum dynamic TCP window size.
                    tcp-window-minimum:
                        type: int
                        description: Deprecated, please rename it to tcp_window_minimum. Minimum dynamic TCP window size.
                    tcp-window-size:
                        type: int
                        description: Deprecated, please rename it to tcp_window_size. Set TCP static window size.
                    tcp-window-type:
                        type: str
                        description: Deprecated, please rename it to tcp_window_type. TCP window type to use for this protocol.
                        choices:
                            - 'system'
                            - 'static'
                            - 'dynamic'
                            - 'auto-tuning'
                    explicit-ftp-tls:
                        type: str
                        description: Deprecated, please rename it to explicit_ftp_tls. Enable/disable FTP redirection for explicit FTPS.
                        choices:
                            - 'disable'
                            - 'enable'
            http:
                type: dict
                description: Http.
                suboptions:
                    block-page-status-code:
                        type: int
                        description: Deprecated, please rename it to block_page_status_code. Code number returned for blocked HTTP pages
                    comfort-amount:
                        type: int
                        description: Deprecated, please rename it to comfort_amount. Amount of data to send in a transmission for client comforting
                    comfort-interval:
                        type: int
                        description: Deprecated, please rename it to comfort_interval. Period of time between start, or last transmission, and the next...
                    fortinet-bar:
                        type: str
                        description: Deprecated, please rename it to fortinet_bar. Enable/disable Fortinet bar on HTML content.
                        choices:
                            - 'disable'
                            - 'enable'
                    fortinet-bar-port:
                        type: int
                        description: Deprecated, please rename it to fortinet_bar_port. Port for use by Fortinet Bar
                    inspect-all:
                        type: str
                        description: Deprecated, please rename it to inspect_all. Enable/disable the inspection of all ports for the protocol.
                        choices:
                            - 'disable'
                            - 'enable'
                    options:
                        type: list
                        elements: str
                        description: One or more options that can be applied to the session.
                        choices:
                            - 'oversize'
                            - 'chunkedbypass'
                            - 'clientcomfort'
                            - 'no-content-summary'
                            - 'servercomfort'
                    oversize-limit:
                        type: int
                        description: Deprecated, please rename it to oversize_limit. Maximum in-memory file size that can be scanned
                    ports:
                        type: raw
                        description: (list) Ports to scan for content
                    post-lang:
                        type: list
                        elements: str
                        description: Deprecated, please rename it to post_lang. ID codes for character sets to be used to convert to UTF-8 for banned w...
                        choices:
                            - 'jisx0201'
                            - 'jisx0208'
                            - 'jisx0212'
                            - 'gb2312'
                            - 'ksc5601-ex'
                            - 'euc-jp'
                            - 'sjis'
                            - 'iso2022-jp'
                            - 'iso2022-jp-1'
                            - 'iso2022-jp-2'
                            - 'euc-cn'
                            - 'ces-gbk'
                            - 'hz'
                            - 'ces-big5'
                            - 'euc-kr'
                            - 'iso2022-jp-3'
                            - 'iso8859-1'
                            - 'tis620'
                            - 'cp874'
                            - 'cp1252'
                            - 'cp1251'
                    proxy-after-tcp-handshake:
                        type: str
                        description: Deprecated, please rename it to proxy_after_tcp_handshake. Proxy traffic after the TCP 3-way handshake has been es...
                        choices:
                            - 'disable'
                            - 'enable'
                    range-block:
                        type: str
                        description: Deprecated, please rename it to range_block. Enable/disable blocking of partial downloads.
                        choices:
                            - 'disable'
                            - 'enable'
                    retry-count:
                        type: int
                        description: Deprecated, please rename it to retry_count. Number of attempts to retry HTTP connection
                    scan-bzip2:
                        type: str
                        description: Deprecated, please rename it to scan_bzip2. Enable/disable scanning of BZip2 compressed files.
                        choices:
                            - 'disable'
                            - 'enable'
                    ssl-offloaded:
                        type: str
                        description: Deprecated, please rename it to ssl_offloaded. SSL decryption and encryption performed by an external device.
                        choices:
                            - 'no'
                            - 'yes'
                    status:
                        type: str
                        description: Enable/disable the active status of scanning for this protocol.
                        choices:
                            - 'disable'
                            - 'enable'
                    stream-based-uncompressed-limit:
                        type: int
                        description: Deprecated, please rename it to stream_based_uncompressed_limit. Maximum stream-based uncompressed data size that ...
                    streaming-content-bypass:
                        type: str
                        description: Deprecated, please rename it to streaming_content_bypass. Enable/disable bypassing of streaming content from buffe...
                        choices:
                            - 'disable'
                            - 'enable'
                    strip-x-forwarded-for:
                        type: str
                        description: Deprecated, please rename it to strip_x_forwarded_for. Enable/disable stripping of HTTP X-Forwarded-For header.
                        choices:
                            - 'disable'
                            - 'enable'
                    switching-protocols:
                        type: str
                        description: Deprecated, please rename it to switching_protocols. Bypass from scanning, or block a connection that attempts to ...
                        choices:
                            - 'bypass'
                            - 'block'
                    tcp-window-maximum:
                        type: int
                        description: Deprecated, please rename it to tcp_window_maximum. Maximum dynamic TCP window size
                    tcp-window-minimum:
                        type: int
                        description: Deprecated, please rename it to tcp_window_minimum. Minimum dynamic TCP window size
                    tcp-window-size:
                        type: int
                        description: Deprecated, please rename it to tcp_window_size. Set TCP static window size
                    tcp-window-type:
                        type: str
                        description: Deprecated, please rename it to tcp_window_type. Specify type of TCP window to use for this protocol.
                        choices:
                            - 'system'
                            - 'static'
                            - 'dynamic'
                            - 'auto-tuning'
                    tunnel-non-http:
                        type: str
                        description: Deprecated, please rename it to tunnel_non_http. Configure how to process non-HTTP traffic when a profile configur...
                        choices:
                            - 'disable'
                            - 'enable'
                    uncompressed-nest-limit:
                        type: int
                        description: Deprecated, please rename it to uncompressed_nest_limit. Maximum nested levels of compression that can be uncompre...
                    uncompressed-oversize-limit:
                        type: int
                        description: Deprecated, please rename it to uncompressed_oversize_limit. Maximum in-memory uncompressed file size that can be ...
                    unknown-http-version:
                        type: str
                        description: Deprecated, please rename it to unknown_http_version. How to handle HTTP sessions that do not comply with HTTP 0.
                        choices:
                            - 'best-effort'
                            - 'reject'
                            - 'tunnel'
                    http-policy:
                        type: str
                        description: Deprecated, please rename it to http_policy. Enable/disable HTTP policy check.
                        choices:
                            - 'disable'
                            - 'enable'
                    address-ip-rating:
                        type: str
                        description: Deprecated, please rename it to address_ip_rating. Enable/disable IP based URL rating.
                        choices:
                            - 'disable'
                            - 'enable'
                    h2c:
                        type: str
                        description: Enable/disable h2c HTTP connection upgrade.
                        choices:
                            - 'disable'
                            - 'enable'
                    verify-dns-for-policy-matching:
                        type: str
                        description: Deprecated, please rename it to verify_dns_for_policy_matching. Enable/disable verification of DNS for policy matc...
                        choices:
                            - 'disable'
                            - 'enable'
                    unknown-content-encoding:
                        type: str
                        description: Deprecated, please rename it to unknown_content_encoding. Configure the action the FortiGate unit will take on unk...
                        choices:
                            - 'block'
                            - 'inspect'
                            - 'bypass'
                    domain-fronting:
                        type: str
                        description: Deprecated, please rename it to domain_fronting. Configure HTTP domain fronting
                        choices:
                            - 'block'
                            - 'monitor'
                            - 'allow'
            imap:
                type: dict
                description: Imap.
                suboptions:
                    inspect-all:
                        type: str
                        description: Deprecated, please rename it to inspect_all. Enable/disable the inspection of all ports for the protocol.
                        choices:
                            - 'disable'
                            - 'enable'
                    options:
                        type: list
                        elements: str
                        description: One or more options that can be applied to the session.
                        choices:
                            - 'oversize'
                            - 'fragmail'
                            - 'no-content-summary'
                    oversize-limit:
                        type: int
                        description: Deprecated, please rename it to oversize_limit. Maximum in-memory file size that can be scanned
                    ports:
                        type: raw
                        description: (list) Ports to scan for content
                    proxy-after-tcp-handshake:
                        type: str
                        description: Deprecated, please rename it to proxy_after_tcp_handshake. Proxy traffic after the TCP 3-way handshake has been es...
                        choices:
                            - 'disable'
                            - 'enable'
                    scan-bzip2:
                        type: str
                        description: Deprecated, please rename it to scan_bzip2. Enable/disable scanning of BZip2 compressed files.
                        choices:
                            - 'disable'
                            - 'enable'
                    ssl-offloaded:
                        type: str
                        description: Deprecated, please rename it to ssl_offloaded. SSL decryption and encryption performed by an external device.
                        choices:
                            - 'no'
                            - 'yes'
                    status:
                        type: str
                        description: Enable/disable the active status of scanning for this protocol.
                        choices:
                            - 'disable'
                            - 'enable'
                    uncompressed-nest-limit:
                        type: int
                        description: Deprecated, please rename it to uncompressed_nest_limit. Maximum nested levels of compression that can be uncompre...
                    uncompressed-oversize-limit:
                        type: int
                        description: Deprecated, please rename it to uncompressed_oversize_limit. Maximum in-memory uncompressed file size that can be ...
            mail-signature:
                type: dict
                description: Deprecated, please rename it to mail_signature. Mail signature.
                suboptions:
                    signature:
                        type: str
                        description: Email signature to be added to outgoing email
                    status:
                        type: str
                        description: Enable/disable adding an email signature to SMTP email messages as they pass through the FortiGate.
                        choices:
                            - 'disable'
                            - 'enable'
            mapi:
                type: dict
                description: Mapi.
                suboptions:
                    options:
                        type: list
                        elements: str
                        description: One or more options that can be applied to the session.
                        choices:
                            - 'fragmail'
                            - 'oversize'
                            - 'no-content-summary'
                    oversize-limit:
                        type: int
                        description: Deprecated, please rename it to oversize_limit. Maximum in-memory file size that can be scanned
                    ports:
                        type: raw
                        description: (list) Ports to scan for content
                    scan-bzip2:
                        type: str
                        description: Deprecated, please rename it to scan_bzip2. Enable/disable scanning of BZip2 compressed files.
                        choices:
                            - 'disable'
                            - 'enable'
                    status:
                        type: str
                        description: Enable/disable the active status of scanning for this protocol.
                        choices:
                            - 'disable'
                            - 'enable'
                    uncompressed-nest-limit:
                        type: int
                        description: Deprecated, please rename it to uncompressed_nest_limit. Maximum nested levels of compression that can be uncompre...
                    uncompressed-oversize-limit:
                        type: int
                        description: Deprecated, please rename it to uncompressed_oversize_limit. Maximum in-memory uncompressed file size that can be ...
            nntp:
                type: dict
                description: Nntp.
                suboptions:
                    inspect-all:
                        type: str
                        description: Deprecated, please rename it to inspect_all. Enable/disable the inspection of all ports for the protocol.
                        choices:
                            - 'disable'
                            - 'enable'
                    options:
                        type: list
                        elements: str
                        description: One or more options that can be applied to the session.
                        choices:
                            - 'oversize'
                            - 'no-content-summary'
                            - 'splice'
                    oversize-limit:
                        type: int
                        description: Deprecated, please rename it to oversize_limit. Maximum in-memory file size that can be scanned
                    ports:
                        type: raw
                        description: (list) Ports to scan for content
                    proxy-after-tcp-handshake:
                        type: str
                        description: Deprecated, please rename it to proxy_after_tcp_handshake. Proxy traffic after the TCP 3-way handshake has been es...
                        choices:
                            - 'disable'
                            - 'enable'
                    scan-bzip2:
                        type: str
                        description: Deprecated, please rename it to scan_bzip2. Enable/disable scanning of BZip2 compressed files.
                        choices:
                            - 'disable'
                            - 'enable'
                    status:
                        type: str
                        description: Enable/disable the active status of scanning for this protocol.
                        choices:
                            - 'disable'
                            - 'enable'
                    uncompressed-nest-limit:
                        type: int
                        description: Deprecated, please rename it to uncompressed_nest_limit. Maximum nested levels of compression that can be uncompre...
                    uncompressed-oversize-limit:
                        type: int
                        description: Deprecated, please rename it to uncompressed_oversize_limit. Maximum in-memory uncompressed file size that can be ...
            pop3:
                type: dict
                description: Pop3.
                suboptions:
                    inspect-all:
                        type: str
                        description: Deprecated, please rename it to inspect_all. Enable/disable the inspection of all ports for the protocol.
                        choices:
                            - 'disable'
                            - 'enable'
                    options:
                        type: list
                        elements: str
                        description: One or more options that can be applied to the session.
                        choices:
                            - 'oversize'
                            - 'fragmail'
                            - 'no-content-summary'
                    oversize-limit:
                        type: int
                        description: Deprecated, please rename it to oversize_limit. Maximum in-memory file size that can be scanned
                    ports:
                        type: raw
                        description: (list) Ports to scan for content
                    proxy-after-tcp-handshake:
                        type: str
                        description: Deprecated, please rename it to proxy_after_tcp_handshake. Proxy traffic after the TCP 3-way handshake has been es...
                        choices:
                            - 'disable'
                            - 'enable'
                    scan-bzip2:
                        type: str
                        description: Deprecated, please rename it to scan_bzip2. Enable/disable scanning of BZip2 compressed files.
                        choices:
                            - 'disable'
                            - 'enable'
                    ssl-offloaded:
                        type: str
                        description: Deprecated, please rename it to ssl_offloaded. SSL decryption and encryption performed by an external device.
                        choices:
                            - 'no'
                            - 'yes'
                    status:
                        type: str
                        description: Enable/disable the active status of scanning for this protocol.
                        choices:
                            - 'disable'
                            - 'enable'
                    uncompressed-nest-limit:
                        type: int
                        description: Deprecated, please rename it to uncompressed_nest_limit. Maximum nested levels of compression that can be uncompre...
                    uncompressed-oversize-limit:
                        type: int
                        description: Deprecated, please rename it to uncompressed_oversize_limit. Maximum in-memory uncompressed file size that can be ...
            smtp:
                type: dict
                description: Smtp.
                suboptions:
                    inspect-all:
                        type: str
                        description: Deprecated, please rename it to inspect_all. Enable/disable the inspection of all ports for the protocol.
                        choices:
                            - 'disable'
                            - 'enable'
                    options:
                        type: list
                        elements: str
                        description: One or more options that can be applied to the session.
                        choices:
                            - 'oversize'
                            - 'fragmail'
                            - 'no-content-summary'
                            - 'splice'
                    oversize-limit:
                        type: int
                        description: Deprecated, please rename it to oversize_limit. Maximum in-memory file size that can be scanned
                    ports:
                        type: raw
                        description: (list) Ports to scan for content
                    proxy-after-tcp-handshake:
                        type: str
                        description: Deprecated, please rename it to proxy_after_tcp_handshake. Proxy traffic after the TCP 3-way handshake has been es...
                        choices:
                            - 'disable'
                            - 'enable'
                    scan-bzip2:
                        type: str
                        description: Deprecated, please rename it to scan_bzip2. Enable/disable scanning of BZip2 compressed files.
                        choices:
                            - 'disable'
                            - 'enable'
                    server-busy:
                        type: str
                        description: Deprecated, please rename it to server_busy. Enable/disable SMTP server busy when server not available.
                        choices:
                            - 'disable'
                            - 'enable'
                    ssl-offloaded:
                        type: str
                        description: Deprecated, please rename it to ssl_offloaded. SSL decryption and encryption performed by an external device.
                        choices:
                            - 'no'
                            - 'yes'
                    status:
                        type: str
                        description: Enable/disable the active status of scanning for this protocol.
                        choices:
                            - 'disable'
                            - 'enable'
                    uncompressed-nest-limit:
                        type: int
                        description: Deprecated, please rename it to uncompressed_nest_limit. Maximum nested levels of compression that can be uncompre...
                    uncompressed-oversize-limit:
                        type: int
                        description: Deprecated, please rename it to uncompressed_oversize_limit. Maximum in-memory uncompressed file size that can be ...
            ssh:
                type: dict
                description: Ssh.
                suboptions:
                    comfort-amount:
                        type: int
                        description: Deprecated, please rename it to comfort_amount. Amount of data to send in a transmission for client comforting
                    comfort-interval:
                        type: int
                        description: Deprecated, please rename it to comfort_interval. Period of time between start, or last transmission, and the next...
                    options:
                        type: list
                        elements: str
                        description: One or more options that can be applied to the session.
                        choices:
                            - 'oversize'
                            - 'clientcomfort'
                            - 'servercomfort'
                    oversize-limit:
                        type: int
                        description: Deprecated, please rename it to oversize_limit. Maximum in-memory file size that can be scanned
                    scan-bzip2:
                        type: str
                        description: Deprecated, please rename it to scan_bzip2. Enable/disable scanning of BZip2 compressed files.
                        choices:
                            - 'disable'
                            - 'enable'
                    uncompressed-nest-limit:
                        type: int
                        description: Deprecated, please rename it to uncompressed_nest_limit. Maximum nested levels of compression that can be uncompre...
                    uncompressed-oversize-limit:
                        type: int
                        description: Deprecated, please rename it to uncompressed_oversize_limit. Maximum in-memory uncompressed file size that can be ...
                    ssl-offloaded:
                        type: str
                        description: Deprecated, please rename it to ssl_offloaded. SSL decryption and encryption performed by an external device.
                        choices:
                            - 'no'
                            - 'yes'
                    stream-based-uncompressed-limit:
                        type: int
                        description: Deprecated, please rename it to stream_based_uncompressed_limit. Maximum stream-based uncompressed data size that ...
                    tcp-window-maximum:
                        type: int
                        description: Deprecated, please rename it to tcp_window_maximum. Maximum dynamic TCP window size.
                    tcp-window-minimum:
                        type: int
                        description: Deprecated, please rename it to tcp_window_minimum. Minimum dynamic TCP window size.
                    tcp-window-size:
                        type: int
                        description: Deprecated, please rename it to tcp_window_size. Set TCP static window size.
                    tcp-window-type:
                        type: str
                        description: Deprecated, please rename it to tcp_window_type. TCP window type to use for this protocol.
                        choices:
                            - 'system'
                            - 'static'
                            - 'dynamic'
                            - 'auto-tuning'
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
    - name: Configure protocol options.
      fortinet.fortimanager.fmgr_firewall_profileprotocoloptions:
        bypass_validation: false
        adom: ansible
        state: present
        firewall_profileprotocoloptions:
          comment: "ansible-comment"
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
    - name: Retrieve all the profile protocol options
      fortinet.fortimanager.fmgr_fact:
        facts:
          selector: "firewall_profileprotocoloptions"
          params:
            adom: "ansible"
            profile-protocol-options: "your_value"
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
        '/pm/config/adom/{adom}/obj/firewall/profile-protocol-options',
        '/pm/config/global/obj/firewall/profile-protocol-options'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/firewall/profile-protocol-options/{profile-protocol-options}',
        '/pm/config/global/obj/firewall/profile-protocol-options/{profile-protocol-options}'
    ]

    url_params = ['adom']
    module_primary_key = 'name'
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'firewall_profileprotocoloptions': {
            'type': 'dict',
            'v_range': [['6.0.0', '']],
            'options': {
                'comment': {'type': 'str'},
                'name': {'required': True, 'type': 'str'},
                'oversize-log': {'choices': ['disable', 'enable'], 'type': 'str'},
                'replacemsg-group': {'type': 'str'},
                'rpc-over-http': {'choices': ['disable', 'enable'], 'type': 'str'},
                'switching-protocols-log': {'choices': ['disable', 'enable'], 'type': 'str'},
                'feature-set': {'v_range': [['6.4.0', '']], 'choices': ['proxy', 'flow'], 'type': 'str'},
                'cifs': {
                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                    'type': 'dict',
                    'options': {
                        'domain-controller': {'v_range': [['6.4.5', '']], 'type': 'str'},
                        'file-filter': {
                            'v_range': [['6.4.5', '']],
                            'type': 'dict',
                            'options': {
                                'entries': {
                                    'v_range': [['6.4.5', '']],
                                    'type': 'list',
                                    'options': {
                                        'action': {'v_range': [['6.4.5', '']], 'choices': ['log', 'block'], 'type': 'str'},
                                        'comment': {'v_range': [['6.4.5', '']], 'type': 'str'},
                                        'direction': {'v_range': [['6.4.5', '']], 'choices': ['any', 'incoming', 'outgoing'], 'type': 'str'},
                                        'file-type': {'v_range': [['6.4.5', '']], 'type': 'raw'},
                                        'filter': {'v_range': [['6.4.5', '']], 'type': 'str'},
                                        'protocol': {'v_range': [['6.4.5', '']], 'type': 'list', 'choices': ['cifs'], 'elements': 'str'}
                                    },
                                    'elements': 'dict'
                                },
                                'log': {'v_range': [['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'status': {'v_range': [['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'}
                            }
                        },
                        'options': {'v_range': [['6.4.5', '']], 'type': 'list', 'choices': ['oversize'], 'elements': 'str'},
                        'oversize-limit': {'v_range': [['6.4.5', '']], 'type': 'int'},
                        'ports': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'raw'},
                        'scan-bzip2': {'v_range': [['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'server-credential-type': {
                            'v_range': [['6.4.5', '']],
                            'choices': ['none', 'credential-replication', 'credential-keytab'],
                            'type': 'str'
                        },
                        'server-keytab': {
                            'v_range': [['6.4.5', '']],
                            'no_log': True,
                            'type': 'list',
                            'options': {
                                'keytab': {'v_range': [['6.4.5', '']], 'no_log': True, 'type': 'str'},
                                'password': {'v_range': [['6.4.5', '']], 'no_log': True, 'type': 'raw'},
                                'principal': {'v_range': [['6.4.5', '']], 'type': 'str'}
                            },
                            'elements': 'dict'
                        },
                        'status': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'tcp-window-maximum': {'v_range': [['6.4.5', '']], 'type': 'int'},
                        'tcp-window-minimum': {'v_range': [['6.4.5', '']], 'type': 'int'},
                        'tcp-window-size': {'v_range': [['6.4.5', '']], 'type': 'int'},
                        'tcp-window-type': {'v_range': [['6.4.5', '']], 'choices': ['system', 'static', 'dynamic', 'auto-tuning'], 'type': 'str'},
                        'uncompressed-nest-limit': {'v_range': [['6.4.5', '']], 'type': 'int'},
                        'uncompressed-oversize-limit': {'v_range': [['6.4.5', '']], 'type': 'int'}
                    }
                },
                'dns': {
                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                    'type': 'dict',
                    'options': {
                        'ports': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'raw'},
                        'status': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'}
                    }
                },
                'ftp': {
                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                    'type': 'dict',
                    'options': {
                        'comfort-amount': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'comfort-interval': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'inspect-all': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'options': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'type': 'list',
                            'choices': ['clientcomfort', 'no-content-summary', 'oversize', 'splice', 'bypass-rest-command', 'bypass-mode-command'],
                            'elements': 'str'
                        },
                        'oversize-limit': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'ports': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'raw'},
                        'scan-bzip2': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'ssl-offloaded': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['no', 'yes'], 'type': 'str'},
                        'status': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'uncompressed-nest-limit': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'uncompressed-oversize-limit': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'stream-based-uncompressed-limit': {'v_range': [['7.0.0', '']], 'type': 'int'},
                        'tcp-window-maximum': {'v_range': [['7.0.0', '']], 'type': 'int'},
                        'tcp-window-minimum': {'v_range': [['7.0.0', '']], 'type': 'int'},
                        'tcp-window-size': {'v_range': [['7.0.0', '']], 'type': 'int'},
                        'tcp-window-type': {'v_range': [['7.0.0', '']], 'choices': ['system', 'static', 'dynamic', 'auto-tuning'], 'type': 'str'},
                        'explicit-ftp-tls': {'v_range': [['7.0.5', '7.0.12'], ['7.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'}
                    }
                },
                'http': {
                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                    'type': 'dict',
                    'options': {
                        'block-page-status-code': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'comfort-amount': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'comfort-interval': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'fortinet-bar': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'fortinet-bar-port': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'inspect-all': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'options': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'type': 'list',
                            'choices': ['oversize', 'chunkedbypass', 'clientcomfort', 'no-content-summary', 'servercomfort'],
                            'elements': 'str'
                        },
                        'oversize-limit': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'ports': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'raw'},
                        'post-lang': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'type': 'list',
                            'choices': [
                                'jisx0201', 'jisx0208', 'jisx0212', 'gb2312', 'ksc5601-ex', 'euc-jp', 'sjis', 'iso2022-jp', 'iso2022-jp-1',
                                'iso2022-jp-2', 'euc-cn', 'ces-gbk', 'hz', 'ces-big5', 'euc-kr', 'iso2022-jp-3', 'iso8859-1', 'tis620', 'cp874',
                                'cp1252', 'cp1251'
                            ],
                            'elements': 'str'
                        },
                        'proxy-after-tcp-handshake': {'v_range': [['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'range-block': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'retry-count': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'scan-bzip2': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'ssl-offloaded': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['no', 'yes'], 'type': 'str'},
                        'status': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'stream-based-uncompressed-limit': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'streaming-content-bypass': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'strip-x-forwarded-for': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'switching-protocols': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['bypass', 'block'], 'type': 'str'},
                        'tcp-window-maximum': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'tcp-window-minimum': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'tcp-window-size': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'tcp-window-type': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['system', 'static', 'dynamic', 'auto-tuning'],
                            'type': 'str'
                        },
                        'tunnel-non-http': {'v_range': [['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'uncompressed-nest-limit': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'uncompressed-oversize-limit': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'unknown-http-version': {'v_range': [['6.4.5', '']], 'choices': ['best-effort', 'reject', 'tunnel'], 'type': 'str'},
                        'http-policy': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '7.2.1']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'address-ip-rating': {'v_range': [['7.0.4', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'h2c': {'v_range': [['7.2.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'verify-dns-for-policy-matching': {'v_range': [['7.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'unknown-content-encoding': {'v_range': [['7.2.2', '']], 'choices': ['block', 'inspect', 'bypass'], 'type': 'str'},
                        'domain-fronting': {'v_range': [['7.6.0', '']], 'choices': ['block', 'monitor', 'allow'], 'type': 'str'}
                    }
                },
                'imap': {
                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                    'type': 'dict',
                    'options': {
                        'inspect-all': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'options': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'type': 'list',
                            'choices': ['oversize', 'fragmail', 'no-content-summary'],
                            'elements': 'str'
                        },
                        'oversize-limit': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'ports': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'raw'},
                        'proxy-after-tcp-handshake': {'v_range': [['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'scan-bzip2': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'ssl-offloaded': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['no', 'yes'], 'type': 'str'},
                        'status': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'uncompressed-nest-limit': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'uncompressed-oversize-limit': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'}
                    }
                },
                'mail-signature': {
                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                    'type': 'dict',
                    'options': {
                        'signature': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'status': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'}
                    }
                },
                'mapi': {
                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                    'type': 'dict',
                    'options': {
                        'options': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'type': 'list',
                            'choices': ['fragmail', 'oversize', 'no-content-summary'],
                            'elements': 'str'
                        },
                        'oversize-limit': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'ports': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'raw'},
                        'scan-bzip2': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'status': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'uncompressed-nest-limit': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'uncompressed-oversize-limit': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'}
                    }
                },
                'nntp': {
                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                    'type': 'dict',
                    'options': {
                        'inspect-all': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'options': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'type': 'list',
                            'choices': ['oversize', 'no-content-summary', 'splice'],
                            'elements': 'str'
                        },
                        'oversize-limit': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'ports': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'raw'},
                        'proxy-after-tcp-handshake': {'v_range': [['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'scan-bzip2': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'status': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'uncompressed-nest-limit': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'uncompressed-oversize-limit': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'}
                    }
                },
                'pop3': {
                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                    'type': 'dict',
                    'options': {
                        'inspect-all': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'options': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'type': 'list',
                            'choices': ['oversize', 'fragmail', 'no-content-summary'],
                            'elements': 'str'
                        },
                        'oversize-limit': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'ports': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'raw'},
                        'proxy-after-tcp-handshake': {'v_range': [['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'scan-bzip2': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'ssl-offloaded': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['no', 'yes'], 'type': 'str'},
                        'status': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'uncompressed-nest-limit': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'uncompressed-oversize-limit': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'}
                    }
                },
                'smtp': {
                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                    'type': 'dict',
                    'options': {
                        'inspect-all': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'options': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'type': 'list',
                            'choices': ['oversize', 'fragmail', 'no-content-summary', 'splice'],
                            'elements': 'str'
                        },
                        'oversize-limit': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'ports': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'raw'},
                        'proxy-after-tcp-handshake': {'v_range': [['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'scan-bzip2': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'server-busy': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'ssl-offloaded': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['no', 'yes'], 'type': 'str'},
                        'status': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'uncompressed-nest-limit': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'uncompressed-oversize-limit': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'}
                    }
                },
                'ssh': {
                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                    'type': 'dict',
                    'options': {
                        'comfort-amount': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'comfort-interval': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'options': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'type': 'list',
                            'choices': ['oversize', 'clientcomfort', 'servercomfort'],
                            'elements': 'str'
                        },
                        'oversize-limit': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'scan-bzip2': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'uncompressed-nest-limit': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'uncompressed-oversize-limit': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'ssl-offloaded': {'v_range': [['7.0.0', '']], 'choices': ['no', 'yes'], 'type': 'str'},
                        'stream-based-uncompressed-limit': {'v_range': [['7.0.0', '']], 'type': 'int'},
                        'tcp-window-maximum': {'v_range': [['7.0.0', '']], 'type': 'int'},
                        'tcp-window-minimum': {'v_range': [['7.0.0', '']], 'type': 'int'},
                        'tcp-window-size': {'v_range': [['7.0.0', '']], 'type': 'int'},
                        'tcp-window-type': {'v_range': [['7.0.0', '']], 'choices': ['system', 'static', 'dynamic', 'auto-tuning'], 'type': 'str'}
                    }
                }
            }

        }
    }

    module_option_spec = get_module_arg_spec('full crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'firewall_profileprotocoloptions'),
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
