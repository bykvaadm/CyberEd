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
module: fmgr_vpn_ssl_settings
short_description: Configure SSL VPN.
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
    device:
        description: The parameter (device) in requested url.
        type: str
        required: true
    vdom:
        description: The parameter (vdom) in requested url.
        type: str
        required: true
    vpn_ssl_settings:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            algorithm:
                type: str
                description: Force the SSL VPN security level.
                choices:
                    - 'default'
                    - 'high'
                    - 'low'
                    - 'medium'
            auth-session-check-source-ip:
                type: str
                description: Deprecated, please rename it to auth_session_check_source_ip. Enable/disable checking of source IP for authentication session.
                choices:
                    - 'disable'
                    - 'enable'
            auth-timeout:
                type: int
                description: Deprecated, please rename it to auth_timeout. SSL VPN authentication timeout
            authentication-rule:
                type: list
                elements: dict
                description: Deprecated, please rename it to authentication_rule. Authentication rule.
                suboptions:
                    auth:
                        type: str
                        description: SSL VPN authentication method restriction.
                        choices:
                            - 'any'
                            - 'local'
                            - 'radius'
                            - 'ldap'
                            - 'tacacs+'
                            - 'peer'
                    cipher:
                        type: str
                        description: SSL VPN cipher strength.
                        choices:
                            - 'any'
                            - 'high'
                            - 'medium'
                    client-cert:
                        type: str
                        description: Deprecated, please rename it to client_cert. Enable/disable SSL VPN client certificate restrictive.
                        choices:
                            - 'disable'
                            - 'enable'
                    groups:
                        type: raw
                        description: (list or str) User groups.
                    id:
                        type: int
                        description: ID
                    portal:
                        type: str
                        description: SSL VPN portal.
                    realm:
                        type: str
                        description: SSL VPN realm.
                    source-address:
                        type: raw
                        description: (list or str) Deprecated, please rename it to source_address. Source address of incoming traffic.
                    source-address-negate:
                        type: str
                        description: Deprecated, please rename it to source_address_negate. Enable/disable negated source address match.
                        choices:
                            - 'disable'
                            - 'enable'
                    source-address6:
                        type: raw
                        description: (list or str) Deprecated, please rename it to source_address6. IPv6 source address of incoming traffic.
                    source-address6-negate:
                        type: str
                        description: Deprecated, please rename it to source_address6_negate. Enable/disable negated source IPv6 address match.
                        choices:
                            - 'disable'
                            - 'enable'
                    source-interface:
                        type: raw
                        description: (list or str) Deprecated, please rename it to source_interface. SSL VPN source interface of incoming traffic.
                    user-peer:
                        type: str
                        description: Deprecated, please rename it to user_peer. Name of user peer.
                    users:
                        type: raw
                        description: (list or str) User name.
            auto-tunnel-static-route:
                type: str
                description: Deprecated, please rename it to auto_tunnel_static_route. Enable/disable to auto-create static routes for the SSL VPN tunn...
                choices:
                    - 'disable'
                    - 'enable'
            banned-cipher:
                type: list
                elements: str
                description: Deprecated, please rename it to banned_cipher. Select one or more cipher technologies that cannot be used in SSL VPN negot...
                choices:
                    - 'RSA'
                    - 'DH'
                    - 'DHE'
                    - 'ECDH'
                    - 'ECDHE'
                    - 'DSS'
                    - 'ECDSA'
                    - 'AES'
                    - 'AESGCM'
                    - 'CAMELLIA'
                    - '3DES'
                    - 'SHA1'
                    - 'SHA256'
                    - 'SHA384'
                    - 'STATIC'
                    - 'CHACHA20'
                    - 'ARIA'
                    - 'AESCCM'
            check-referer:
                type: str
                description: Deprecated, please rename it to check_referer. Enable/disable verification of referer field in HTTP request header.
                choices:
                    - 'disable'
                    - 'enable'
            default-portal:
                type: str
                description: Deprecated, please rename it to default_portal. Default SSL VPN portal.
            deflate-compression-level:
                type: int
                description: Deprecated, please rename it to deflate_compression_level. Compression level
            deflate-min-data-size:
                type: int
                description: Deprecated, please rename it to deflate_min_data_size. Minimum amount of data that triggers compression
            dns-server1:
                type: str
                description: Deprecated, please rename it to dns_server1. DNS server 1.
            dns-server2:
                type: str
                description: Deprecated, please rename it to dns_server2. DNS server 2.
            dns-suffix:
                type: str
                description: Deprecated, please rename it to dns_suffix. DNS suffix used for SSL VPN clients.
            dtls-hello-timeout:
                type: int
                description: Deprecated, please rename it to dtls_hello_timeout. SSLVPN maximum DTLS hello timeout
            dtls-max-proto-ver:
                type: str
                description: Deprecated, please rename it to dtls_max_proto_ver. DTLS maximum protocol version.
                choices:
                    - 'dtls1-0'
                    - 'dtls1-2'
            dtls-min-proto-ver:
                type: str
                description: Deprecated, please rename it to dtls_min_proto_ver. DTLS minimum protocol version.
                choices:
                    - 'dtls1-0'
                    - 'dtls1-2'
            dtls-tunnel:
                type: str
                description: Deprecated, please rename it to dtls_tunnel. Enable/disable DTLS to prevent eavesdropping, tampering, or message forgery.
                choices:
                    - 'disable'
                    - 'enable'
            encode-2f-sequence:
                type: str
                description: Deprecated, please rename it to encode_2f_sequence. Encode 2F sequence to forward slash in URLs.
                choices:
                    - 'disable'
                    - 'enable'
            encrypt-and-store-password:
                type: str
                description: Deprecated, please rename it to encrypt_and_store_password. Encrypt and store user passwords for SSL VPN web sessions.
                choices:
                    - 'disable'
                    - 'enable'
            force-two-factor-auth:
                type: str
                description: Deprecated, please rename it to force_two_factor_auth. Enable/disable only PKI users with two-factor authentication for SS...
                choices:
                    - 'disable'
                    - 'enable'
            header-x-forwarded-for:
                type: str
                description: Deprecated, please rename it to header_x_forwarded_for. Forward the same, add, or remove HTTP header.
                choices:
                    - 'pass'
                    - 'add'
                    - 'remove'
            hsts-include-subdomains:
                type: str
                description: Deprecated, please rename it to hsts_include_subdomains. Add HSTS includeSubDomains response header.
                choices:
                    - 'disable'
                    - 'enable'
            http-compression:
                type: str
                description: Deprecated, please rename it to http_compression. Enable/disable to allow HTTP compression over SSL VPN tunnels.
                choices:
                    - 'disable'
                    - 'enable'
            http-only-cookie:
                type: str
                description: Deprecated, please rename it to http_only_cookie. Enable/disable SSL VPN support for HttpOnly cookies.
                choices:
                    - 'disable'
                    - 'enable'
            http-request-body-timeout:
                type: int
                description: Deprecated, please rename it to http_request_body_timeout. SSL VPN session is disconnected if an HTTP request body is not ...
            http-request-header-timeout:
                type: int
                description: Deprecated, please rename it to http_request_header_timeout. SSL VPN session is disconnected if an HTTP request header is ...
            https-redirect:
                type: str
                description: Deprecated, please rename it to https_redirect. Enable/disable redirect of port 80 to SSL VPN port.
                choices:
                    - 'disable'
                    - 'enable'
            idle-timeout:
                type: int
                description: Deprecated, please rename it to idle_timeout. SSL VPN disconnects if idle for specified time in seconds.
            ipv6-dns-server1:
                type: str
                description: Deprecated, please rename it to ipv6_dns_server1. IPv6 DNS server 1.
            ipv6-dns-server2:
                type: str
                description: Deprecated, please rename it to ipv6_dns_server2. IPv6 DNS server 2.
            ipv6-wins-server1:
                type: str
                description: Deprecated, please rename it to ipv6_wins_server1. IPv6 WINS server 1.
            ipv6-wins-server2:
                type: str
                description: Deprecated, please rename it to ipv6_wins_server2. IPv6 WINS server 2.
            login-attempt-limit:
                type: int
                description: Deprecated, please rename it to login_attempt_limit. SSL VPN maximum login attempt times before block
            login-block-time:
                type: int
                description: Deprecated, please rename it to login_block_time. Time for which a user is blocked from logging in after too many failed l...
            login-timeout:
                type: int
                description: Deprecated, please rename it to login_timeout. SSLVPN maximum login timeout
            port:
                type: int
                description: SSL VPN access port
            port-precedence:
                type: str
                description: Deprecated, please rename it to port_precedence. Enable/disable, Enable means that if SSL VPN connections are allowed on a...
                choices:
                    - 'disable'
                    - 'enable'
            reqclientcert:
                type: str
                description: Enable/disable to require client certificates for all SSL VPN users.
                choices:
                    - 'disable'
                    - 'enable'
            route-source-interface:
                type: str
                description: Deprecated, please rename it to route_source_interface. Enable/disable to allow SSL VPN sessions to bypass routing and bin...
                choices:
                    - 'disable'
                    - 'enable'
            servercert:
                type: str
                description: Name of the server certificate to be used for SSL VPNs.
            source-address:
                type: raw
                description: (list or str) Deprecated, please rename it to source_address. Source address of incoming traffic.
            source-address-negate:
                type: str
                description: Deprecated, please rename it to source_address_negate. Enable/disable negated source address match.
                choices:
                    - 'disable'
                    - 'enable'
            source-address6:
                type: raw
                description: (list or str) Deprecated, please rename it to source_address6. IPv6 source address of incoming traffic.
            source-address6-negate:
                type: str
                description: Deprecated, please rename it to source_address6_negate. Enable/disable negated source IPv6 address match.
                choices:
                    - 'disable'
                    - 'enable'
            source-interface:
                type: raw
                description: (list or str) Deprecated, please rename it to source_interface. SSL VPN source interface of incoming traffic.
            ssl-client-renegotiation:
                type: str
                description: Deprecated, please rename it to ssl_client_renegotiation. Enable/disable to allow client renegotiation by the server if th...
                choices:
                    - 'disable'
                    - 'enable'
            ssl-insert-empty-fragment:
                type: str
                description: Deprecated, please rename it to ssl_insert_empty_fragment. Enable/disable insertion of empty fragment.
                choices:
                    - 'disable'
                    - 'enable'
            ssl-max-proto-ver:
                type: str
                description: Deprecated, please rename it to ssl_max_proto_ver. SSL maximum protocol version.
                choices:
                    - 'tls1-0'
                    - 'tls1-1'
                    - 'tls1-2'
                    - 'tls1-3'
            ssl-min-proto-ver:
                type: str
                description: Deprecated, please rename it to ssl_min_proto_ver. SSL minimum protocol version.
                choices:
                    - 'tls1-0'
                    - 'tls1-1'
                    - 'tls1-2'
                    - 'tls1-3'
            tlsv1-0:
                type: str
                description: Deprecated, please rename it to tlsv1_0. Enable/disable TLSv1.
                choices:
                    - 'disable'
                    - 'enable'
            tlsv1-1:
                type: str
                description: Deprecated, please rename it to tlsv1_1. Enable/disable TLSv1.
                choices:
                    - 'disable'
                    - 'enable'
            tlsv1-2:
                type: str
                description: Deprecated, please rename it to tlsv1_2. Enable/disable TLSv1.
                choices:
                    - 'disable'
                    - 'enable'
            tlsv1-3:
                type: str
                description: Deprecated, please rename it to tlsv1_3. Tlsv1 3.
                choices:
                    - 'disable'
                    - 'enable'
            transform-backward-slashes:
                type: str
                description: Deprecated, please rename it to transform_backward_slashes. Transform backward slashes to forward slashes in URLs.
                choices:
                    - 'disable'
                    - 'enable'
            tunnel-connect-without-reauth:
                type: str
                description: Deprecated, please rename it to tunnel_connect_without_reauth. Enable/disable tunnel connection without re-authorization i...
                choices:
                    - 'disable'
                    - 'enable'
            tunnel-ip-pools:
                type: raw
                description: (list or str) Deprecated, please rename it to tunnel_ip_pools. Names of the IPv4 IP Pool firewall objects that define the ...
            tunnel-ipv6-pools:
                type: raw
                description: (list or str) Deprecated, please rename it to tunnel_ipv6_pools. Names of the IPv6 IP Pool firewall objects that define th...
            tunnel-user-session-timeout:
                type: int
                description: Deprecated, please rename it to tunnel_user_session_timeout. Time out value to clean up user session after tunnel connecti...
            unsafe-legacy-renegotiation:
                type: str
                description: Deprecated, please rename it to unsafe_legacy_renegotiation. Enable/disable unsafe legacy re-negotiation.
                choices:
                    - 'disable'
                    - 'enable'
            url-obscuration:
                type: str
                description: Deprecated, please rename it to url_obscuration. Enable/disable to obscure the host name of the URL of the web browser dis...
                choices:
                    - 'disable'
                    - 'enable'
            user-peer:
                type: str
                description: Deprecated, please rename it to user_peer. Name of user peer.
            wins-server1:
                type: str
                description: Deprecated, please rename it to wins_server1. WINS server 1.
            wins-server2:
                type: str
                description: Deprecated, please rename it to wins_server2. WINS server 2.
            x-content-type-options:
                type: str
                description: Deprecated, please rename it to x_content_type_options. Add HTTP X-Content-Type-Options header.
                choices:
                    - 'disable'
                    - 'enable'
            sslv3:
                type: str
                description: Sslv3.
                choices:
                    - 'disable'
                    - 'enable'
            ssl-big-buffer:
                type: str
                description: Deprecated, please rename it to ssl_big_buffer. Disable using the big SSLv3 buffer feature to save memory and force higher...
                choices:
                    - 'disable'
                    - 'enable'
            client-sigalgs:
                type: str
                description: Deprecated, please rename it to client_sigalgs. Set signature algorithms related to client authentication.
                choices:
                    - 'no-rsa-pss'
                    - 'all'
            ciphersuite:
                type: list
                elements: str
                description: Select one or more TLS 1.
                choices:
                    - 'TLS-AES-128-GCM-SHA256'
                    - 'TLS-AES-256-GCM-SHA384'
                    - 'TLS-CHACHA20-POLY1305-SHA256'
                    - 'TLS-AES-128-CCM-SHA256'
                    - 'TLS-AES-128-CCM-8-SHA256'
            dual-stack-mode:
                type: str
                description: Deprecated, please rename it to dual_stack_mode. Tunnel mode
                choices:
                    - 'disable'
                    - 'enable'
            tunnel-addr-assigned-method:
                type: str
                description: Deprecated, please rename it to tunnel_addr_assigned_method. Method used for assigning address for tunnel.
                choices:
                    - 'first-available'
                    - 'round-robin'
            browser-language-detection:
                type: str
                description: Deprecated, please rename it to browser_language_detection. Enable/disable overriding the configured system language based...
                choices:
                    - 'disable'
                    - 'enable'
            saml-redirect-port:
                type: int
                description: Deprecated, please rename it to saml_redirect_port. SAML local redirect port in the machine running FortiClient
            status:
                type: str
                description: Enable/disable SSL-VPN.
                choices:
                    - 'disable'
                    - 'enable'
            web-mode-snat:
                type: str
                description: Deprecated, please rename it to web_mode_snat. Enable/disable use of IP pools defined in firewall policy while using web-mode.
                choices:
                    - 'disable'
                    - 'enable'
            ztna-trusted-client:
                type: str
                description: Deprecated, please rename it to ztna_trusted_client. Enable/disable verification of device certificate for SSLVPN ZTNA ses...
                choices:
                    - 'disable'
                    - 'enable'
            dtls-heartbeat-fail-count:
                type: int
                description: Deprecated, please rename it to dtls_heartbeat_fail_count. Number of missing heartbeats before the connection is considere...
            dtls-heartbeat-idle-timeout:
                type: int
                description: Deprecated, please rename it to dtls_heartbeat_idle_timeout. Idle timeout before DTLS heartbeat is sent.
            dtls-heartbeat-interval:
                type: int
                description: Deprecated, please rename it to dtls_heartbeat_interval. Interval between DTLS heartbeat.
            server-hostname:
                type: str
                description: Deprecated, please rename it to server_hostname. Server hostname for HTTPS.
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
    - name: Configure SSL VPN.
      fortinet.fortimanager.fmgr_vpn_ssl_settings:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        device: <your own value>
        vdom: <your own value>
        vpn_ssl_settings:
          algorithm: <value in [default, high, low, ...]>
          auth_session_check_source_ip: <value in [disable, enable]>
          auth_timeout: <integer>
          authentication_rule:
            -
              auth: <value in [any, local, radius, ...]>
              cipher: <value in [any, high, medium]>
              client_cert: <value in [disable, enable]>
              groups: <list or string>
              id: <integer>
              portal: <string>
              realm: <string>
              source_address: <list or string>
              source_address_negate: <value in [disable, enable]>
              source_address6: <list or string>
              source_address6_negate: <value in [disable, enable]>
              source_interface: <list or string>
              user_peer: <string>
              users: <list or string>
          auto_tunnel_static_route: <value in [disable, enable]>
          banned_cipher:
            - RSA
            - DH
            - DHE
            - ECDH
            - ECDHE
            - DSS
            - ECDSA
            - AES
            - AESGCM
            - CAMELLIA
            - 3DES
            - SHA1
            - SHA256
            - SHA384
            - STATIC
            - CHACHA20
            - ARIA
            - AESCCM
          check_referer: <value in [disable, enable]>
          default_portal: <string>
          deflate_compression_level: <integer>
          deflate_min_data_size: <integer>
          dns_server1: <string>
          dns_server2: <string>
          dns_suffix: <string>
          dtls_hello_timeout: <integer>
          dtls_max_proto_ver: <value in [dtls1-0, dtls1-2]>
          dtls_min_proto_ver: <value in [dtls1-0, dtls1-2]>
          dtls_tunnel: <value in [disable, enable]>
          encode_2f_sequence: <value in [disable, enable]>
          encrypt_and_store_password: <value in [disable, enable]>
          force_two_factor_auth: <value in [disable, enable]>
          header_x_forwarded_for: <value in [pass, add, remove]>
          hsts_include_subdomains: <value in [disable, enable]>
          http_compression: <value in [disable, enable]>
          http_only_cookie: <value in [disable, enable]>
          http_request_body_timeout: <integer>
          http_request_header_timeout: <integer>
          https_redirect: <value in [disable, enable]>
          idle_timeout: <integer>
          ipv6_dns_server1: <string>
          ipv6_dns_server2: <string>
          ipv6_wins_server1: <string>
          ipv6_wins_server2: <string>
          login_attempt_limit: <integer>
          login_block_time: <integer>
          login_timeout: <integer>
          port: <integer>
          port_precedence: <value in [disable, enable]>
          reqclientcert: <value in [disable, enable]>
          route_source_interface: <value in [disable, enable]>
          servercert: <string>
          source_address: <list or string>
          source_address_negate: <value in [disable, enable]>
          source_address6: <list or string>
          source_address6_negate: <value in [disable, enable]>
          source_interface: <list or string>
          ssl_client_renegotiation: <value in [disable, enable]>
          ssl_insert_empty_fragment: <value in [disable, enable]>
          ssl_max_proto_ver: <value in [tls1-0, tls1-1, tls1-2, ...]>
          ssl_min_proto_ver: <value in [tls1-0, tls1-1, tls1-2, ...]>
          tlsv1_0: <value in [disable, enable]>
          tlsv1_1: <value in [disable, enable]>
          tlsv1_2: <value in [disable, enable]>
          tlsv1_3: <value in [disable, enable]>
          transform_backward_slashes: <value in [disable, enable]>
          tunnel_connect_without_reauth: <value in [disable, enable]>
          tunnel_ip_pools: <list or string>
          tunnel_ipv6_pools: <list or string>
          tunnel_user_session_timeout: <integer>
          unsafe_legacy_renegotiation: <value in [disable, enable]>
          url_obscuration: <value in [disable, enable]>
          user_peer: <string>
          wins_server1: <string>
          wins_server2: <string>
          x_content_type_options: <value in [disable, enable]>
          sslv3: <value in [disable, enable]>
          ssl_big_buffer: <value in [disable, enable]>
          client_sigalgs: <value in [no-rsa-pss, all]>
          ciphersuite:
            - TLS-AES-128-GCM-SHA256
            - TLS-AES-256-GCM-SHA384
            - TLS-CHACHA20-POLY1305-SHA256
            - TLS-AES-128-CCM-SHA256
            - TLS-AES-128-CCM-8-SHA256
          dual_stack_mode: <value in [disable, enable]>
          tunnel_addr_assigned_method: <value in [first-available, round-robin]>
          browser_language_detection: <value in [disable, enable]>
          saml_redirect_port: <integer>
          status: <value in [disable, enable]>
          web_mode_snat: <value in [disable, enable]>
          ztna_trusted_client: <value in [disable, enable]>
          dtls_heartbeat_fail_count: <integer>
          dtls_heartbeat_idle_timeout: <integer>
          dtls_heartbeat_interval: <integer>
          server_hostname: <string>
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
        '/pm/config/device/{device}/vdom/{vdom}/vpn/ssl/settings'
    ]

    perobject_jrpc_urls = [
        '/pm/config/device/{device}/vdom/{vdom}/vpn/ssl/settings/{settings}'
    ]

    url_params = ['device', 'vdom']
    module_primary_key = None
    module_arg_spec = {
        'device': {'required': True, 'type': 'str'},
        'vdom': {'required': True, 'type': 'str'},
        'vpn_ssl_settings': {
            'type': 'dict',
            'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']],
            'options': {
                'algorithm': {
                    'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '7.2.1'], ['7.4.3', '']],
                    'choices': ['default', 'high', 'low', 'medium'],
                    'type': 'str'
                },
                'auth-session-check-source-ip': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'auth-timeout': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'int'},
                'authentication-rule': {
                    'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']],
                    'type': 'list',
                    'options': {
                        'auth': {
                            'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']],
                            'choices': ['any', 'local', 'radius', 'ldap', 'tacacs+', 'peer'],
                            'type': 'str'
                        },
                        'cipher': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'choices': ['any', 'high', 'medium'], 'type': 'str'},
                        'client-cert': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'groups': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'raw'},
                        'id': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'int'},
                        'portal': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'str'},
                        'realm': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'str'},
                        'source-address': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'raw'},
                        'source-address-negate': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'source-address6': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'raw'},
                        'source-address6-negate': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'source-interface': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'raw'},
                        'user-peer': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'str'},
                        'users': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'raw'}
                    },
                    'elements': 'dict'
                },
                'auto-tunnel-static-route': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'banned-cipher': {
                    'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']],
                    'type': 'list',
                    'choices': [
                        'RSA', 'DH', 'DHE', 'ECDH', 'ECDHE', 'DSS', 'ECDSA', 'AES', 'AESGCM', 'CAMELLIA', '3DES', 'SHA1', 'SHA256', 'SHA384', 'STATIC',
                        'CHACHA20', 'ARIA', 'AESCCM'
                    ],
                    'elements': 'str'
                },
                'check-referer': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'default-portal': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'str'},
                'deflate-compression-level': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'int'},
                'deflate-min-data-size': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'int'},
                'dns-server1': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'str'},
                'dns-server2': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'str'},
                'dns-suffix': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'str'},
                'dtls-hello-timeout': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'int'},
                'dtls-max-proto-ver': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'choices': ['dtls1-0', 'dtls1-2'], 'type': 'str'},
                'dtls-min-proto-ver': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'choices': ['dtls1-0', 'dtls1-2'], 'type': 'str'},
                'dtls-tunnel': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'encode-2f-sequence': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'encrypt-and-store-password': {'v_range': [['6.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'force-two-factor-auth': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'header-x-forwarded-for': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'choices': ['pass', 'add', 'remove'], 'type': 'str'},
                'hsts-include-subdomains': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'http-compression': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'http-only-cookie': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'http-request-body-timeout': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'int'},
                'http-request-header-timeout': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'int'},
                'https-redirect': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'idle-timeout': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'int'},
                'ipv6-dns-server1': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'str'},
                'ipv6-dns-server2': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'str'},
                'ipv6-wins-server1': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'str'},
                'ipv6-wins-server2': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'str'},
                'login-attempt-limit': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'int'},
                'login-block-time': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'int'},
                'login-timeout': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'int'},
                'port': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'int'},
                'port-precedence': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'reqclientcert': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'route-source-interface': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '7.2.0']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'servercert': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'str'},
                'source-address': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'raw'},
                'source-address-negate': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'source-address6': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'raw'},
                'source-address6-negate': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'source-interface': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'raw'},
                'ssl-client-renegotiation': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ssl-insert-empty-fragment': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ssl-max-proto-ver': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'choices': ['tls1-0', 'tls1-1', 'tls1-2', 'tls1-3'], 'type': 'str'},
                'ssl-min-proto-ver': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'choices': ['tls1-0', 'tls1-1', 'tls1-2', 'tls1-3'], 'type': 'str'},
                'tlsv1-0': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '7.2.1']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'tlsv1-1': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '7.2.1']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'tlsv1-2': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '7.2.1']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'tlsv1-3': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '7.2.0']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'transform-backward-slashes': {'v_range': [['6.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'tunnel-connect-without-reauth': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'tunnel-ip-pools': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'raw'},
                'tunnel-ipv6-pools': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'raw'},
                'tunnel-user-session-timeout': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'int'},
                'unsafe-legacy-renegotiation': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'url-obscuration': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'user-peer': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'str'},
                'wins-server1': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'str'},
                'wins-server2': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'str'},
                'x-content-type-options': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'sslv3': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '6.4.14']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ssl-big-buffer': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '6.4.14']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'client-sigalgs': {'v_range': [['6.4.4', '']], 'choices': ['no-rsa-pss', 'all'], 'type': 'str'},
                'ciphersuite': {
                    'v_range': [['6.4.8', '']],
                    'type': 'list',
                    'choices': [
                        'TLS-AES-128-GCM-SHA256', 'TLS-AES-256-GCM-SHA384', 'TLS-CHACHA20-POLY1305-SHA256', 'TLS-AES-128-CCM-SHA256',
                        'TLS-AES-128-CCM-8-SHA256'
                    ],
                    'elements': 'str'
                },
                'dual-stack-mode': {'v_range': [['7.0.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'tunnel-addr-assigned-method': {'v_range': [['7.0.0', '']], 'choices': ['first-available', 'round-robin'], 'type': 'str'},
                'browser-language-detection': {'v_range': [['7.2.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'saml-redirect-port': {'v_range': [['7.0.1', '']], 'type': 'int'},
                'status': {'v_range': [['6.4.8', '6.4.14'], ['7.0.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'web-mode-snat': {'v_range': [['7.0.4', '7.2.3'], ['7.4.0', '7.4.1'], ['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ztna-trusted-client': {'v_range': [['7.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'dtls-heartbeat-fail-count': {'v_range': [['7.4.0', '']], 'type': 'int'},
                'dtls-heartbeat-idle-timeout': {'v_range': [['7.4.0', '']], 'type': 'int'},
                'dtls-heartbeat-interval': {'v_range': [['7.4.0', '']], 'type': 'int'},
                'server-hostname': {'v_range': [['7.4.0', '']], 'type': 'str'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('partial crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'vpn_ssl_settings'),
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
