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
module: fmgr_firewall_sslsshprofile
short_description: Configure SSL/SSH protocol options.
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
    firewall_sslsshprofile:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            caname:
                type: str
                description: CA certificate used by SSL Inspection.
            comment:
                type: str
                description: Optional comments.
            mapi-over-https:
                type: str
                description: Deprecated, please rename it to mapi_over_https. Enable/disable inspection of MAPI over HTTPS.
                choices:
                    - 'disable'
                    - 'enable'
            name:
                type: str
                description: Name.
                required: true
            rpc-over-https:
                type: str
                description: Deprecated, please rename it to rpc_over_https. Enable/disable inspection of RPC over HTTPS.
                choices:
                    - 'disable'
                    - 'enable'
            server-cert:
                type: raw
                description: (list or str) Deprecated, please rename it to server_cert. Certificate used by SSL Inspection to replace server certificate.
            server-cert-mode:
                type: str
                description: Deprecated, please rename it to server_cert_mode. Re-sign or replace the servers certificate.
                choices:
                    - 're-sign'
                    - 'replace'
            ssl-anomalies-log:
                type: str
                description: Deprecated, please rename it to ssl_anomalies_log. Enable/disable logging SSL anomalies.
                choices:
                    - 'disable'
                    - 'enable'
            ssl-exempt:
                type: list
                elements: dict
                description: Deprecated, please rename it to ssl_exempt. Ssl exempt.
                suboptions:
                    address:
                        type: str
                        description: IPv4 address object.
                    address6:
                        type: str
                        description: IPv6 address object.
                    fortiguard-category:
                        type: str
                        description: Deprecated, please rename it to fortiguard_category. FortiGuard category ID.
                    id:
                        type: int
                        description: ID number.
                    regex:
                        type: str
                        description: Exempt servers by regular expression.
                    type:
                        type: str
                        description: Type of address object
                        choices:
                            - 'fortiguard-category'
                            - 'address'
                            - 'address6'
                            - 'wildcard-fqdn'
                            - 'regex'
                            - 'finger-print'
                    wildcard-fqdn:
                        type: str
                        description: Deprecated, please rename it to wildcard_fqdn. Exempt servers by wildcard FQDN.
            ssl-exemptions-log:
                type: str
                description: Deprecated, please rename it to ssl_exemptions_log. Enable/disable logging SSL exemptions.
                choices:
                    - 'disable'
                    - 'enable'
            ssl-server:
                type: list
                elements: dict
                description: Deprecated, please rename it to ssl_server. Ssl server.
                suboptions:
                    ftps-client-cert-request:
                        type: str
                        description: Deprecated, please rename it to ftps_client_cert_request. Action based on client certificate request during the FT...
                        choices:
                            - 'bypass'
                            - 'inspect'
                            - 'block'
                    https-client-cert-request:
                        type: str
                        description: Deprecated, please rename it to https_client_cert_request. Action based on client certificate request during the H...
                        choices:
                            - 'bypass'
                            - 'inspect'
                            - 'block'
                    id:
                        type: int
                        description: SSL server ID.
                    imaps-client-cert-request:
                        type: str
                        description: Deprecated, please rename it to imaps_client_cert_request. Action based on client certificate request during the I...
                        choices:
                            - 'bypass'
                            - 'inspect'
                            - 'block'
                    ip:
                        type: str
                        description: IPv4 address of the SSL server.
                    pop3s-client-cert-request:
                        type: str
                        description: Deprecated, please rename it to pop3s_client_cert_request. Action based on client certificate request during the P...
                        choices:
                            - 'bypass'
                            - 'inspect'
                            - 'block'
                    smtps-client-cert-request:
                        type: str
                        description: Deprecated, please rename it to smtps_client_cert_request. Action based on client certificate request during the S...
                        choices:
                            - 'bypass'
                            - 'inspect'
                            - 'block'
                    ssl-other-client-cert-request:
                        type: str
                        description: Deprecated, please rename it to ssl_other_client_cert_request. Action based on client certificate request during a...
                        choices:
                            - 'bypass'
                            - 'inspect'
                            - 'block'
                    ftps-client-certificate:
                        type: str
                        description: Deprecated, please rename it to ftps_client_certificate. Action based on received client certificate during the FT...
                        choices:
                            - 'bypass'
                            - 'inspect'
                            - 'block'
                    https-client-certificate:
                        type: str
                        description: Deprecated, please rename it to https_client_certificate. Action based on received client certificate during the H...
                        choices:
                            - 'bypass'
                            - 'inspect'
                            - 'block'
                    imaps-client-certificate:
                        type: str
                        description: Deprecated, please rename it to imaps_client_certificate. Action based on received client certificate during the I...
                        choices:
                            - 'bypass'
                            - 'inspect'
                            - 'block'
                    pop3s-client-certificate:
                        type: str
                        description: Deprecated, please rename it to pop3s_client_certificate. Action based on received client certificate during the P...
                        choices:
                            - 'bypass'
                            - 'inspect'
                            - 'block'
                    smtps-client-certificate:
                        type: str
                        description: Deprecated, please rename it to smtps_client_certificate. Action based on received client certificate during the S...
                        choices:
                            - 'bypass'
                            - 'inspect'
                            - 'block'
                    ssl-other-client-certificate:
                        type: str
                        description: Deprecated, please rename it to ssl_other_client_certificate. Action based on received client certificate during a...
                        choices:
                            - 'bypass'
                            - 'inspect'
                            - 'block'
            untrusted-caname:
                type: str
                description: Deprecated, please rename it to untrusted_caname. Untrusted CA certificate used by SSL Inspection.
            use-ssl-server:
                type: str
                description: Deprecated, please rename it to use_ssl_server. Enable/disable the use of SSL server table for SSL offloading.
                choices:
                    - 'disable'
                    - 'enable'
            whitelist:
                type: str
                description: Enable/disable exempting servers by FortiGuard whitelist.
                choices:
                    - 'disable'
                    - 'enable'
            block-blacklisted-certificates:
                type: str
                description: Deprecated, please rename it to block_blacklisted_certificates. Enable/disable blocking SSL-based botnet communication by ...
                choices:
                    - 'disable'
                    - 'enable'
            certname:
                type: str
                description: Certificate containing the key to use when re-signing server certificates for SSL inspection.
            ssl-invalid-server-cert-log:
                type: str
                description: Deprecated, please rename it to ssl_invalid_server_cert_log. Enable/disable SSL server certificate validation logging.
                choices:
                    - 'disable'
                    - 'enable'
            ssl-negotiation-log:
                type: str
                description: Deprecated, please rename it to ssl_negotiation_log. Enable/disable logging SSL negotiation.
                choices:
                    - 'disable'
                    - 'enable'
            ftps:
                type: dict
                description: Ftps.
                suboptions:
                    cert-validation-failure:
                        type: str
                        description: Deprecated, please rename it to cert_validation_failure. Action based on certificate validation failure.
                        choices:
                            - 'allow'
                            - 'block'
                            - 'ignore'
                    cert-validation-timeout:
                        type: str
                        description: Deprecated, please rename it to cert_validation_timeout. Action based on certificate validation timeout.
                        choices:
                            - 'allow'
                            - 'block'
                            - 'ignore'
                    client-certificate:
                        type: str
                        description: Deprecated, please rename it to client_certificate. Action based on received client certificate.
                        choices:
                            - 'bypass'
                            - 'inspect'
                            - 'block'
                    expired-server-cert:
                        type: str
                        description: Deprecated, please rename it to expired_server_cert. Action based on server certificate is expired.
                        choices:
                            - 'allow'
                            - 'block'
                            - 'ignore'
                    ports:
                        type: raw
                        description: (list) Ports to use for scanning
                    revoked-server-cert:
                        type: str
                        description: Deprecated, please rename it to revoked_server_cert. Action based on server certificate is revoked.
                        choices:
                            - 'allow'
                            - 'block'
                            - 'ignore'
                    sni-server-cert-check:
                        type: str
                        description: Deprecated, please rename it to sni_server_cert_check. Check the SNI in the client hello message with the CN or SA...
                        choices:
                            - 'disable'
                            - 'enable'
                            - 'strict'
                    status:
                        type: str
                        description: Configure protocol inspection status.
                        choices:
                            - 'disable'
                            - 'deep-inspection'
                    unsupported-ssl-cipher:
                        type: str
                        description: Deprecated, please rename it to unsupported_ssl_cipher. Action based on the SSL cipher used being unsupported.
                        choices:
                            - 'allow'
                            - 'block'
                    unsupported-ssl-negotiation:
                        type: str
                        description: Deprecated, please rename it to unsupported_ssl_negotiation. Action based on the SSL negotiation used being unsupp...
                        choices:
                            - 'allow'
                            - 'block'
                    untrusted-server-cert:
                        type: str
                        description: Deprecated, please rename it to untrusted_server_cert. Action based on server certificate is not issued by a trust...
                        choices:
                            - 'allow'
                            - 'block'
                            - 'ignore'
                    unsupported-ssl:
                        type: str
                        description: Deprecated, please rename it to unsupported_ssl. Action based on the SSL encryption used being unsupported.
                        choices:
                            - 'bypass'
                            - 'inspect'
                            - 'block'
                    client-cert-request:
                        type: str
                        description: Deprecated, please rename it to client_cert_request. Action based on client certificate request.
                        choices:
                            - 'bypass'
                            - 'inspect'
                            - 'block'
                    invalid-server-cert:
                        type: str
                        description: Deprecated, please rename it to invalid_server_cert. Allow or block the invalid SSL session server certificate.
                        choices:
                            - 'allow'
                            - 'block'
                    allow-invalid-server-cert:
                        type: str
                        description: Deprecated, please rename it to allow_invalid_server_cert. When enabled, allows SSL sessions whose server certific...
                        choices:
                            - 'disable'
                            - 'enable'
                    untrusted-cert:
                        type: str
                        description: Deprecated, please rename it to untrusted_cert. Allow, ignore, or block the untrusted SSL session server certificate.
                        choices:
                            - 'allow'
                            - 'block'
                            - 'ignore'
                    min-allowed-ssl-version:
                        type: str
                        description: Deprecated, please rename it to min_allowed_ssl_version. Minimum SSL version to be allowed.
                        choices:
                            - 'ssl-3.0'
                            - 'tls-1.0'
                            - 'tls-1.1'
                            - 'tls-1.2'
                            - 'tls-1.3'
                    unsupported-ssl-version:
                        type: str
                        description: Deprecated, please rename it to unsupported_ssl_version. Action based on the SSL version used being unsupported.
                        choices:
                            - 'block'
                            - 'allow'
                            - 'inspect'
            https:
                type: dict
                description: Https.
                suboptions:
                    cert-validation-failure:
                        type: str
                        description: Deprecated, please rename it to cert_validation_failure. Action based on certificate validation failure.
                        choices:
                            - 'allow'
                            - 'block'
                            - 'ignore'
                    cert-validation-timeout:
                        type: str
                        description: Deprecated, please rename it to cert_validation_timeout. Action based on certificate validation timeout.
                        choices:
                            - 'allow'
                            - 'block'
                            - 'ignore'
                    client-certificate:
                        type: str
                        description: Deprecated, please rename it to client_certificate. Action based on received client certificate.
                        choices:
                            - 'bypass'
                            - 'inspect'
                            - 'block'
                    expired-server-cert:
                        type: str
                        description: Deprecated, please rename it to expired_server_cert. Action based on server certificate is expired.
                        choices:
                            - 'allow'
                            - 'block'
                            - 'ignore'
                    ports:
                        type: raw
                        description: (list) Ports to use for scanning
                    proxy-after-tcp-handshake:
                        type: str
                        description: Deprecated, please rename it to proxy_after_tcp_handshake. Proxy traffic after the TCP 3-way handshake has been es...
                        choices:
                            - 'disable'
                            - 'enable'
                    revoked-server-cert:
                        type: str
                        description: Deprecated, please rename it to revoked_server_cert. Action based on server certificate is revoked.
                        choices:
                            - 'allow'
                            - 'block'
                            - 'ignore'
                    sni-server-cert-check:
                        type: str
                        description: Deprecated, please rename it to sni_server_cert_check. Check the SNI in the client hello message with the CN or SA...
                        choices:
                            - 'disable'
                            - 'enable'
                            - 'strict'
                    status:
                        type: str
                        description: Configure protocol inspection status.
                        choices:
                            - 'disable'
                            - 'certificate-inspection'
                            - 'deep-inspection'
                    unsupported-ssl-cipher:
                        type: str
                        description: Deprecated, please rename it to unsupported_ssl_cipher. Action based on the SSL cipher used being unsupported.
                        choices:
                            - 'allow'
                            - 'block'
                    unsupported-ssl-negotiation:
                        type: str
                        description: Deprecated, please rename it to unsupported_ssl_negotiation. Action based on the SSL negotiation used being unsupp...
                        choices:
                            - 'allow'
                            - 'block'
                    untrusted-server-cert:
                        type: str
                        description: Deprecated, please rename it to untrusted_server_cert. Action based on server certificate is not issued by a trust...
                        choices:
                            - 'allow'
                            - 'block'
                            - 'ignore'
                    unsupported-ssl:
                        type: str
                        description: Deprecated, please rename it to unsupported_ssl. Action based on the SSL encryption used being unsupported.
                        choices:
                            - 'bypass'
                            - 'inspect'
                            - 'block'
                    client-cert-request:
                        type: str
                        description: Deprecated, please rename it to client_cert_request. Action based on client certificate request.
                        choices:
                            - 'bypass'
                            - 'inspect'
                            - 'block'
                    invalid-server-cert:
                        type: str
                        description: Deprecated, please rename it to invalid_server_cert. Allow or block the invalid SSL session server certificate.
                        choices:
                            - 'allow'
                            - 'block'
                    allow-invalid-server-cert:
                        type: str
                        description: Deprecated, please rename it to allow_invalid_server_cert. When enabled, allows SSL sessions whose server certific...
                        choices:
                            - 'disable'
                            - 'enable'
                    untrusted-cert:
                        type: str
                        description: Deprecated, please rename it to untrusted_cert. Allow, ignore, or block the untrusted SSL session server certificate.
                        choices:
                            - 'allow'
                            - 'block'
                            - 'ignore'
                    cert-probe-failure:
                        type: str
                        description: Deprecated, please rename it to cert_probe_failure. Action based on certificate probe failure.
                        choices:
                            - 'block'
                            - 'allow'
                    min-allowed-ssl-version:
                        type: str
                        description: Deprecated, please rename it to min_allowed_ssl_version. Minimum SSL version to be allowed.
                        choices:
                            - 'ssl-3.0'
                            - 'tls-1.0'
                            - 'tls-1.1'
                            - 'tls-1.2'
                            - 'tls-1.3'
                    unsupported-ssl-version:
                        type: str
                        description: Deprecated, please rename it to unsupported_ssl_version. Action based on the SSL version used being unsupported.
                        choices:
                            - 'block'
                            - 'allow'
                            - 'inspect'
                    quic:
                        type: str
                        description: Enable/disable QUIC inspection
                        choices:
                            - 'disable'
                            - 'enable'
                            - 'bypass'
                            - 'block'
                            - 'inspect'
                    encrypted-client-hello:
                        type: str
                        description: Deprecated, please rename it to encrypted_client_hello. Block/allow session based on existence of encrypted-client...
                        choices:
                            - 'block'
                            - 'allow'
            imaps:
                type: dict
                description: Imaps.
                suboptions:
                    cert-validation-failure:
                        type: str
                        description: Deprecated, please rename it to cert_validation_failure. Action based on certificate validation failure.
                        choices:
                            - 'allow'
                            - 'block'
                            - 'ignore'
                    cert-validation-timeout:
                        type: str
                        description: Deprecated, please rename it to cert_validation_timeout. Action based on certificate validation timeout.
                        choices:
                            - 'allow'
                            - 'block'
                            - 'ignore'
                    client-certificate:
                        type: str
                        description: Deprecated, please rename it to client_certificate. Action based on received client certificate.
                        choices:
                            - 'bypass'
                            - 'inspect'
                            - 'block'
                    expired-server-cert:
                        type: str
                        description: Deprecated, please rename it to expired_server_cert. Action based on server certificate is expired.
                        choices:
                            - 'allow'
                            - 'block'
                            - 'ignore'
                    ports:
                        type: raw
                        description: (list) Ports to use for scanning
                    proxy-after-tcp-handshake:
                        type: str
                        description: Deprecated, please rename it to proxy_after_tcp_handshake. Proxy traffic after the TCP 3-way handshake has been es...
                        choices:
                            - 'disable'
                            - 'enable'
                    revoked-server-cert:
                        type: str
                        description: Deprecated, please rename it to revoked_server_cert. Action based on server certificate is revoked.
                        choices:
                            - 'allow'
                            - 'block'
                            - 'ignore'
                    sni-server-cert-check:
                        type: str
                        description: Deprecated, please rename it to sni_server_cert_check. Check the SNI in the client hello message with the CN or SA...
                        choices:
                            - 'disable'
                            - 'enable'
                            - 'strict'
                    status:
                        type: str
                        description: Configure protocol inspection status.
                        choices:
                            - 'disable'
                            - 'deep-inspection'
                    unsupported-ssl-cipher:
                        type: str
                        description: Deprecated, please rename it to unsupported_ssl_cipher. Action based on the SSL cipher used being unsupported.
                        choices:
                            - 'allow'
                            - 'block'
                    unsupported-ssl-negotiation:
                        type: str
                        description: Deprecated, please rename it to unsupported_ssl_negotiation. Action based on the SSL negotiation used being unsupp...
                        choices:
                            - 'allow'
                            - 'block'
                    untrusted-server-cert:
                        type: str
                        description: Deprecated, please rename it to untrusted_server_cert. Action based on server certificate is not issued by a trust...
                        choices:
                            - 'allow'
                            - 'block'
                            - 'ignore'
                    unsupported-ssl:
                        type: str
                        description: Deprecated, please rename it to unsupported_ssl. Action based on the SSL encryption used being unsupported.
                        choices:
                            - 'bypass'
                            - 'inspect'
                            - 'block'
                    client-cert-request:
                        type: str
                        description: Deprecated, please rename it to client_cert_request. Action based on client certificate request.
                        choices:
                            - 'bypass'
                            - 'inspect'
                            - 'block'
                    invalid-server-cert:
                        type: str
                        description: Deprecated, please rename it to invalid_server_cert. Allow or block the invalid SSL session server certificate.
                        choices:
                            - 'allow'
                            - 'block'
                    allow-invalid-server-cert:
                        type: str
                        description: Deprecated, please rename it to allow_invalid_server_cert. When enabled, allows SSL sessions whose server certific...
                        choices:
                            - 'disable'
                            - 'enable'
                    untrusted-cert:
                        type: str
                        description: Deprecated, please rename it to untrusted_cert. Allow, ignore, or block the untrusted SSL session server certificate.
                        choices:
                            - 'allow'
                            - 'block'
                            - 'ignore'
                    unsupported-ssl-version:
                        type: str
                        description: Deprecated, please rename it to unsupported_ssl_version. Action based on the SSL version used being unsupported.
                        choices:
                            - 'block'
                            - 'allow'
                            - 'inspect'
                    min-allowed-ssl-version:
                        type: str
                        description: Deprecated, please rename it to min_allowed_ssl_version. Min allowed ssl version.
                        choices:
                            - 'ssl-3.0'
                            - 'tls-1.0'
                            - 'tls-1.1'
                            - 'tls-1.2'
                            - 'tls-1.3'
            pop3s:
                type: dict
                description: Pop3s.
                suboptions:
                    cert-validation-failure:
                        type: str
                        description: Deprecated, please rename it to cert_validation_failure. Action based on certificate validation failure.
                        choices:
                            - 'allow'
                            - 'block'
                            - 'ignore'
                    cert-validation-timeout:
                        type: str
                        description: Deprecated, please rename it to cert_validation_timeout. Action based on certificate validation timeout.
                        choices:
                            - 'allow'
                            - 'block'
                            - 'ignore'
                    client-certificate:
                        type: str
                        description: Deprecated, please rename it to client_certificate. Action based on received client certificate.
                        choices:
                            - 'bypass'
                            - 'inspect'
                            - 'block'
                    expired-server-cert:
                        type: str
                        description: Deprecated, please rename it to expired_server_cert. Action based on server certificate is expired.
                        choices:
                            - 'allow'
                            - 'block'
                            - 'ignore'
                    ports:
                        type: raw
                        description: (list) Ports to use for scanning
                    proxy-after-tcp-handshake:
                        type: str
                        description: Deprecated, please rename it to proxy_after_tcp_handshake. Proxy traffic after the TCP 3-way handshake has been es...
                        choices:
                            - 'disable'
                            - 'enable'
                    revoked-server-cert:
                        type: str
                        description: Deprecated, please rename it to revoked_server_cert. Action based on server certificate is revoked.
                        choices:
                            - 'allow'
                            - 'block'
                            - 'ignore'
                    sni-server-cert-check:
                        type: str
                        description: Deprecated, please rename it to sni_server_cert_check. Check the SNI in the client hello message with the CN or SA...
                        choices:
                            - 'disable'
                            - 'enable'
                            - 'strict'
                    status:
                        type: str
                        description: Configure protocol inspection status.
                        choices:
                            - 'disable'
                            - 'deep-inspection'
                    unsupported-ssl-cipher:
                        type: str
                        description: Deprecated, please rename it to unsupported_ssl_cipher. Action based on the SSL cipher used being unsupported.
                        choices:
                            - 'allow'
                            - 'block'
                    unsupported-ssl-negotiation:
                        type: str
                        description: Deprecated, please rename it to unsupported_ssl_negotiation. Action based on the SSL negotiation used being unsupp...
                        choices:
                            - 'allow'
                            - 'block'
                    untrusted-server-cert:
                        type: str
                        description: Deprecated, please rename it to untrusted_server_cert. Action based on server certificate is not issued by a trust...
                        choices:
                            - 'allow'
                            - 'block'
                            - 'ignore'
                    unsupported-ssl:
                        type: str
                        description: Deprecated, please rename it to unsupported_ssl. Action based on the SSL encryption used being unsupported.
                        choices:
                            - 'bypass'
                            - 'inspect'
                            - 'block'
                    client-cert-request:
                        type: str
                        description: Deprecated, please rename it to client_cert_request. Action based on client certificate request.
                        choices:
                            - 'bypass'
                            - 'inspect'
                            - 'block'
                    invalid-server-cert:
                        type: str
                        description: Deprecated, please rename it to invalid_server_cert. Allow or block the invalid SSL session server certificate.
                        choices:
                            - 'allow'
                            - 'block'
                    allow-invalid-server-cert:
                        type: str
                        description: Deprecated, please rename it to allow_invalid_server_cert. When enabled, allows SSL sessions whose server certific...
                        choices:
                            - 'disable'
                            - 'enable'
                    untrusted-cert:
                        type: str
                        description: Deprecated, please rename it to untrusted_cert. Allow, ignore, or block the untrusted SSL session server certificate.
                        choices:
                            - 'allow'
                            - 'block'
                            - 'ignore'
                    unsupported-ssl-version:
                        type: str
                        description: Deprecated, please rename it to unsupported_ssl_version. Action based on the SSL version used being unsupported.
                        choices:
                            - 'block'
                            - 'allow'
                            - 'inspect'
                    min-allowed-ssl-version:
                        type: str
                        description: Deprecated, please rename it to min_allowed_ssl_version. Min allowed ssl version.
                        choices:
                            - 'ssl-3.0'
                            - 'tls-1.0'
                            - 'tls-1.1'
                            - 'tls-1.2'
                            - 'tls-1.3'
            smtps:
                type: dict
                description: Smtps.
                suboptions:
                    cert-validation-failure:
                        type: str
                        description: Deprecated, please rename it to cert_validation_failure. Action based on certificate validation failure.
                        choices:
                            - 'allow'
                            - 'block'
                            - 'ignore'
                    cert-validation-timeout:
                        type: str
                        description: Deprecated, please rename it to cert_validation_timeout. Action based on certificate validation timeout.
                        choices:
                            - 'allow'
                            - 'block'
                            - 'ignore'
                    client-certificate:
                        type: str
                        description: Deprecated, please rename it to client_certificate. Action based on received client certificate.
                        choices:
                            - 'bypass'
                            - 'inspect'
                            - 'block'
                    expired-server-cert:
                        type: str
                        description: Deprecated, please rename it to expired_server_cert. Action based on server certificate is expired.
                        choices:
                            - 'allow'
                            - 'block'
                            - 'ignore'
                    ports:
                        type: raw
                        description: (list) Ports to use for scanning
                    proxy-after-tcp-handshake:
                        type: str
                        description: Deprecated, please rename it to proxy_after_tcp_handshake. Proxy traffic after the TCP 3-way handshake has been es...
                        choices:
                            - 'disable'
                            - 'enable'
                    revoked-server-cert:
                        type: str
                        description: Deprecated, please rename it to revoked_server_cert. Action based on server certificate is revoked.
                        choices:
                            - 'allow'
                            - 'block'
                            - 'ignore'
                    sni-server-cert-check:
                        type: str
                        description: Deprecated, please rename it to sni_server_cert_check. Check the SNI in the client hello message with the CN or SA...
                        choices:
                            - 'disable'
                            - 'enable'
                            - 'strict'
                    status:
                        type: str
                        description: Configure protocol inspection status.
                        choices:
                            - 'disable'
                            - 'deep-inspection'
                    unsupported-ssl-cipher:
                        type: str
                        description: Deprecated, please rename it to unsupported_ssl_cipher. Action based on the SSL cipher used being unsupported.
                        choices:
                            - 'allow'
                            - 'block'
                    unsupported-ssl-negotiation:
                        type: str
                        description: Deprecated, please rename it to unsupported_ssl_negotiation. Action based on the SSL negotiation used being unsupp...
                        choices:
                            - 'allow'
                            - 'block'
                    untrusted-server-cert:
                        type: str
                        description: Deprecated, please rename it to untrusted_server_cert. Action based on server certificate is not issued by a trust...
                        choices:
                            - 'allow'
                            - 'block'
                            - 'ignore'
                    unsupported-ssl:
                        type: str
                        description: Deprecated, please rename it to unsupported_ssl. Action based on the SSL encryption used being unsupported.
                        choices:
                            - 'bypass'
                            - 'inspect'
                            - 'block'
                    client-cert-request:
                        type: str
                        description: Deprecated, please rename it to client_cert_request. Action based on client certificate request.
                        choices:
                            - 'bypass'
                            - 'inspect'
                            - 'block'
                    invalid-server-cert:
                        type: str
                        description: Deprecated, please rename it to invalid_server_cert. Allow or block the invalid SSL session server certificate.
                        choices:
                            - 'allow'
                            - 'block'
                    allow-invalid-server-cert:
                        type: str
                        description: Deprecated, please rename it to allow_invalid_server_cert. When enabled, allows SSL sessions whose server certific...
                        choices:
                            - 'disable'
                            - 'enable'
                    untrusted-cert:
                        type: str
                        description: Deprecated, please rename it to untrusted_cert. Allow, ignore, or block the untrusted SSL session server certificate.
                        choices:
                            - 'allow'
                            - 'block'
                            - 'ignore'
                    unsupported-ssl-version:
                        type: str
                        description: Deprecated, please rename it to unsupported_ssl_version. Action based on the SSL version used being unsupported.
                        choices:
                            - 'block'
                            - 'allow'
                            - 'inspect'
                    min-allowed-ssl-version:
                        type: str
                        description: Deprecated, please rename it to min_allowed_ssl_version. Min allowed ssl version.
                        choices:
                            - 'ssl-3.0'
                            - 'tls-1.0'
                            - 'tls-1.1'
                            - 'tls-1.2'
                            - 'tls-1.3'
            ssh:
                type: dict
                description: Ssh.
                suboptions:
                    inspect-all:
                        type: str
                        description: Deprecated, please rename it to inspect_all. Level of SSL inspection.
                        choices:
                            - 'disable'
                            - 'deep-inspection'
                    ports:
                        type: raw
                        description: (list) Ports to use for scanning
                    proxy-after-tcp-handshake:
                        type: str
                        description: Deprecated, please rename it to proxy_after_tcp_handshake. Proxy traffic after the TCP 3-way handshake has been es...
                        choices:
                            - 'disable'
                            - 'enable'
                    ssh-algorithm:
                        type: str
                        description: Deprecated, please rename it to ssh_algorithm. Relative strength of encryption algorithms accepted during negotiation.
                        choices:
                            - 'compatible'
                            - 'high-encryption'
                    ssh-tun-policy-check:
                        type: str
                        description: Deprecated, please rename it to ssh_tun_policy_check. Enable/disable SSH tunnel policy check.
                        choices:
                            - 'disable'
                            - 'enable'
                    status:
                        type: str
                        description: Configure protocol inspection status.
                        choices:
                            - 'disable'
                            - 'deep-inspection'
                    unsupported-version:
                        type: str
                        description: Deprecated, please rename it to unsupported_version. Action based on SSH version being unsupported.
                        choices:
                            - 'block'
                            - 'bypass'
                    ssh-policy-check:
                        type: str
                        description: Deprecated, please rename it to ssh_policy_check. Enable/disable SSH policy check.
                        choices:
                            - 'disable'
                            - 'enable'
                    block:
                        type: list
                        elements: str
                        description: SSH blocking options.
                        choices:
                            - 'x11-filter'
                            - 'ssh-shell'
                            - 'exec'
                            - 'port-forward'
                    log:
                        type: list
                        elements: str
                        description: SSH logging options.
                        choices:
                            - 'x11-filter'
                            - 'ssh-shell'
                            - 'exec'
                            - 'port-forward'
            ssl:
                type: dict
                description: Ssl.
                suboptions:
                    cert-validation-failure:
                        type: str
                        description: Deprecated, please rename it to cert_validation_failure. Action based on certificate validation failure.
                        choices:
                            - 'allow'
                            - 'block'
                            - 'ignore'
                    cert-validation-timeout:
                        type: str
                        description: Deprecated, please rename it to cert_validation_timeout. Action based on certificate validation timeout.
                        choices:
                            - 'allow'
                            - 'block'
                            - 'ignore'
                    client-certificate:
                        type: str
                        description: Deprecated, please rename it to client_certificate. Action based on received client certificate.
                        choices:
                            - 'bypass'
                            - 'inspect'
                            - 'block'
                    expired-server-cert:
                        type: str
                        description: Deprecated, please rename it to expired_server_cert. Action based on server certificate is expired.
                        choices:
                            - 'allow'
                            - 'block'
                            - 'ignore'
                    inspect-all:
                        type: str
                        description: Deprecated, please rename it to inspect_all. Level of SSL inspection.
                        choices:
                            - 'disable'
                            - 'certificate-inspection'
                            - 'deep-inspection'
                    revoked-server-cert:
                        type: str
                        description: Deprecated, please rename it to revoked_server_cert. Action based on server certificate is revoked.
                        choices:
                            - 'allow'
                            - 'block'
                            - 'ignore'
                    sni-server-cert-check:
                        type: str
                        description: Deprecated, please rename it to sni_server_cert_check. Check the SNI in the client hello message with the CN or SA...
                        choices:
                            - 'disable'
                            - 'enable'
                            - 'strict'
                    unsupported-ssl-cipher:
                        type: str
                        description: Deprecated, please rename it to unsupported_ssl_cipher. Action based on the SSL cipher used being unsupported.
                        choices:
                            - 'allow'
                            - 'block'
                    unsupported-ssl-negotiation:
                        type: str
                        description: Deprecated, please rename it to unsupported_ssl_negotiation. Action based on the SSL negotiation used being unsupp...
                        choices:
                            - 'allow'
                            - 'block'
                    untrusted-server-cert:
                        type: str
                        description: Deprecated, please rename it to untrusted_server_cert. Action based on server certificate is not issued by a trust...
                        choices:
                            - 'allow'
                            - 'block'
                            - 'ignore'
                    unsupported-ssl:
                        type: str
                        description: Deprecated, please rename it to unsupported_ssl. Action based on the SSL encryption used being unsupported.
                        choices:
                            - 'bypass'
                            - 'inspect'
                            - 'block'
                    client-cert-request:
                        type: str
                        description: Deprecated, please rename it to client_cert_request. Action based on client certificate request.
                        choices:
                            - 'bypass'
                            - 'inspect'
                            - 'block'
                    invalid-server-cert:
                        type: str
                        description: Deprecated, please rename it to invalid_server_cert. Allow or block the invalid SSL session server certificate.
                        choices:
                            - 'allow'
                            - 'block'
                    allow-invalid-server-cert:
                        type: str
                        description: Deprecated, please rename it to allow_invalid_server_cert. When enabled, allows SSL sessions whose server certific...
                        choices:
                            - 'disable'
                            - 'enable'
                    untrusted-cert:
                        type: str
                        description: Deprecated, please rename it to untrusted_cert. Allow, ignore, or block the untrusted SSL session server certificate.
                        choices:
                            - 'allow'
                            - 'block'
                            - 'ignore'
                    cert-probe-failure:
                        type: str
                        description: Deprecated, please rename it to cert_probe_failure. Action based on certificate probe failure.
                        choices:
                            - 'block'
                            - 'allow'
                    min-allowed-ssl-version:
                        type: str
                        description: Deprecated, please rename it to min_allowed_ssl_version. Minimum SSL version to be allowed.
                        choices:
                            - 'ssl-3.0'
                            - 'tls-1.0'
                            - 'tls-1.1'
                            - 'tls-1.2'
                            - 'tls-1.3'
                    unsupported-ssl-version:
                        type: str
                        description: Deprecated, please rename it to unsupported_ssl_version. Action based on the SSL version used being unsupported.
                        choices:
                            - 'block'
                            - 'allow'
                            - 'inspect'
                    encrypted-client-hello:
                        type: str
                        description: Deprecated, please rename it to encrypted_client_hello. Block/allow session based on existence of encrypted-client...
                        choices:
                            - 'block'
                            - 'allow'
            allowlist:
                type: str
                description: Enable/disable exempting servers by FortiGuard allowlist.
                choices:
                    - 'disable'
                    - 'enable'
            block-blocklisted-certificates:
                type: str
                description: Deprecated, please rename it to block_blocklisted_certificates. Enable/disable blocking SSL-based botnet communication by ...
                choices:
                    - 'disable'
                    - 'enable'
            dot:
                type: dict
                description: Dot.
                suboptions:
                    cert-validation-failure:
                        type: str
                        description: Deprecated, please rename it to cert_validation_failure. Action based on certificate validation failure.
                        choices:
                            - 'allow'
                            - 'block'
                            - 'ignore'
                    cert-validation-timeout:
                        type: str
                        description: Deprecated, please rename it to cert_validation_timeout. Action based on certificate validation timeout.
                        choices:
                            - 'allow'
                            - 'block'
                            - 'ignore'
                    client-certificate:
                        type: str
                        description: Deprecated, please rename it to client_certificate. Action based on received client certificate.
                        choices:
                            - 'bypass'
                            - 'inspect'
                            - 'block'
                    expired-server-cert:
                        type: str
                        description: Deprecated, please rename it to expired_server_cert. Action based on server certificate is expired.
                        choices:
                            - 'allow'
                            - 'block'
                            - 'ignore'
                    proxy-after-tcp-handshake:
                        type: str
                        description: Deprecated, please rename it to proxy_after_tcp_handshake. Proxy traffic after the TCP 3-way handshake has been es...
                        choices:
                            - 'disable'
                            - 'enable'
                    revoked-server-cert:
                        type: str
                        description: Deprecated, please rename it to revoked_server_cert. Action based on server certificate is revoked.
                        choices:
                            - 'allow'
                            - 'block'
                            - 'ignore'
                    sni-server-cert-check:
                        type: str
                        description: Deprecated, please rename it to sni_server_cert_check. Check the SNI in the client hello message with the CN or SA...
                        choices:
                            - 'enable'
                            - 'strict'
                            - 'disable'
                    status:
                        type: str
                        description: Configure protocol inspection status.
                        choices:
                            - 'disable'
                            - 'deep-inspection'
                    unsupported-ssl-cipher:
                        type: str
                        description: Deprecated, please rename it to unsupported_ssl_cipher. Action based on the SSL cipher used being unsupported.
                        choices:
                            - 'block'
                            - 'allow'
                    unsupported-ssl-negotiation:
                        type: str
                        description: Deprecated, please rename it to unsupported_ssl_negotiation. Action based on the SSL negotiation used being unsupp...
                        choices:
                            - 'block'
                            - 'allow'
                    untrusted-server-cert:
                        type: str
                        description: Deprecated, please rename it to untrusted_server_cert. Action based on server certificate is not issued by a trust...
                        choices:
                            - 'allow'
                            - 'block'
                            - 'ignore'
                    unsupported-ssl-version:
                        type: str
                        description: Deprecated, please rename it to unsupported_ssl_version. Action based on the SSL version used being unsupported.
                        choices:
                            - 'block'
                            - 'allow'
                            - 'inspect'
                    min-allowed-ssl-version:
                        type: str
                        description: Deprecated, please rename it to min_allowed_ssl_version. Min allowed ssl version.
                        choices:
                            - 'ssl-3.0'
                            - 'tls-1.0'
                            - 'tls-1.1'
                            - 'tls-1.2'
                            - 'tls-1.3'
                    quic:
                        type: str
                        description: Enable/disable QUIC inspection
                        choices:
                            - 'disable'
                            - 'enable'
                            - 'bypass'
                            - 'block'
                            - 'inspect'
            supported-alpn:
                type: str
                description: Deprecated, please rename it to supported_alpn. Configure ALPN option.
                choices:
                    - 'none'
                    - 'http1-1'
                    - 'http2'
                    - 'all'
            ssl-anomaly-log:
                type: str
                description: Deprecated, please rename it to ssl_anomaly_log. Enable/disable logging of SSL anomalies.
                choices:
                    - 'disable'
                    - 'enable'
            ssl-exemption-ip-rating:
                type: str
                description: Deprecated, please rename it to ssl_exemption_ip_rating. Enable/disable IP based URL rating.
                choices:
                    - 'disable'
                    - 'enable'
            ssl-exemption-log:
                type: str
                description: Deprecated, please rename it to ssl_exemption_log. Enable/disable logging SSL exemptions.
                choices:
                    - 'disable'
                    - 'enable'
            ssl-handshake-log:
                type: str
                description: Deprecated, please rename it to ssl_handshake_log. Enable/disable logging of TLS handshakes.
                choices:
                    - 'disable'
                    - 'enable'
            ssl-server-cert-log:
                type: str
                description: Deprecated, please rename it to ssl_server_cert_log. Enable/disable logging of server certificate information.
                choices:
                    - 'disable'
                    - 'enable'
            ech-outer-sni:
                type: list
                elements: dict
                description: Deprecated, please rename it to ech_outer_sni. Ech outer sni.
                suboptions:
                    name:
                        type: str
                        description: ClientHelloOuter SNI name.
                    sni:
                        type: str
                        description: ClientHelloOuter SNI to be blocked.
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
    - name: Configure SSL/SSH protocol options.
      fortinet.fortimanager.fmgr_firewall_sslsshprofile:
        bypass_validation: false
        adom: ansible
        state: present
        firewall_sslsshprofile:
          comment: "ansible-comment1"
          mapi-over-https: disable # <value in [disable, enable]>
          name: "ansible-test"
          use-ssl-server: disable # <value in [disable, enable]>
          whitelist: enable # <value in [disable, enable]>

- name: Gathering fortimanager facts
  hosts: fortimanagers
  gather_facts: false
  connection: httpapi
  vars:
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_httpapi_port: 443
  tasks:
    - name: Retrieve all the SSL/SSH protocol options
      fortinet.fortimanager.fmgr_fact:
        facts:
          selector: "firewall_sslsshprofile"
          params:
            adom: "ansible"
            ssl-ssh-profile: "your_value"
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
        '/pm/config/adom/{adom}/obj/firewall/ssl-ssh-profile',
        '/pm/config/global/obj/firewall/ssl-ssh-profile'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/firewall/ssl-ssh-profile/{ssl-ssh-profile}',
        '/pm/config/global/obj/firewall/ssl-ssh-profile/{ssl-ssh-profile}'
    ]

    url_params = ['adom']
    module_primary_key = 'name'
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'firewall_sslsshprofile': {
            'type': 'dict',
            'v_range': [['6.0.0', '']],
            'options': {
                'caname': {'type': 'str'},
                'comment': {'type': 'str'},
                'mapi-over-https': {'choices': ['disable', 'enable'], 'type': 'str'},
                'name': {'required': True, 'type': 'str'},
                'rpc-over-https': {'choices': ['disable', 'enable'], 'type': 'str'},
                'server-cert': {'type': 'raw'},
                'server-cert-mode': {'choices': ['re-sign', 'replace'], 'type': 'str'},
                'ssl-anomalies-log': {'choices': ['disable', 'enable'], 'type': 'str'},
                'ssl-exempt': {
                    'type': 'list',
                    'options': {
                        'address': {'type': 'str'},
                        'address6': {'type': 'str'},
                        'fortiguard-category': {'type': 'str'},
                        'id': {'type': 'int'},
                        'regex': {'type': 'str'},
                        'type': {'choices': ['fortiguard-category', 'address', 'address6', 'wildcard-fqdn', 'regex', 'finger-print'], 'type': 'str'},
                        'wildcard-fqdn': {'type': 'str'}
                    },
                    'elements': 'dict'
                },
                'ssl-exemptions-log': {'choices': ['disable', 'enable'], 'type': 'str'},
                'ssl-server': {
                    'type': 'list',
                    'options': {
                        'ftps-client-cert-request': {'choices': ['bypass', 'inspect', 'block'], 'type': 'str'},
                        'https-client-cert-request': {'choices': ['bypass', 'inspect', 'block'], 'type': 'str'},
                        'id': {'type': 'int'},
                        'imaps-client-cert-request': {'choices': ['bypass', 'inspect', 'block'], 'type': 'str'},
                        'ip': {'type': 'str'},
                        'pop3s-client-cert-request': {'choices': ['bypass', 'inspect', 'block'], 'type': 'str'},
                        'smtps-client-cert-request': {'choices': ['bypass', 'inspect', 'block'], 'type': 'str'},
                        'ssl-other-client-cert-request': {'choices': ['bypass', 'inspect', 'block'], 'type': 'str'},
                        'ftps-client-certificate': {'v_range': [['6.4.0', '']], 'choices': ['bypass', 'inspect', 'block'], 'type': 'str'},
                        'https-client-certificate': {'v_range': [['6.4.0', '']], 'choices': ['bypass', 'inspect', 'block'], 'type': 'str'},
                        'imaps-client-certificate': {'v_range': [['6.4.0', '']], 'choices': ['bypass', 'inspect', 'block'], 'type': 'str'},
                        'pop3s-client-certificate': {'v_range': [['6.4.0', '']], 'choices': ['bypass', 'inspect', 'block'], 'type': 'str'},
                        'smtps-client-certificate': {'v_range': [['6.4.0', '']], 'choices': ['bypass', 'inspect', 'block'], 'type': 'str'},
                        'ssl-other-client-certificate': {'v_range': [['6.4.0', '']], 'choices': ['bypass', 'inspect', 'block'], 'type': 'str'}
                    },
                    'elements': 'dict'
                },
                'untrusted-caname': {'type': 'str'},
                'use-ssl-server': {'choices': ['disable', 'enable'], 'type': 'str'},
                'whitelist': {'choices': ['disable', 'enable'], 'type': 'str'},
                'block-blacklisted-certificates': {'v_range': [['6.2.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'certname': {'v_range': [['6.2.0', '6.2.12']], 'type': 'str'},
                'ssl-invalid-server-cert-log': {'v_range': [['6.2.0', '6.2.12']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ssl-negotiation-log': {'v_range': [['6.4.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ftps': {
                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                    'type': 'dict',
                    'options': {
                        'cert-validation-failure': {'v_range': [['6.4.5', '']], 'choices': ['allow', 'block', 'ignore'], 'type': 'str'},
                        'cert-validation-timeout': {'v_range': [['6.4.5', '']], 'choices': ['allow', 'block', 'ignore'], 'type': 'str'},
                        'client-certificate': {'v_range': [['6.4.5', '']], 'choices': ['bypass', 'inspect', 'block'], 'type': 'str'},
                        'expired-server-cert': {'v_range': [['6.4.5', '']], 'choices': ['allow', 'block', 'ignore'], 'type': 'str'},
                        'ports': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'raw'},
                        'revoked-server-cert': {'v_range': [['6.4.5', '']], 'choices': ['allow', 'block', 'ignore'], 'type': 'str'},
                        'sni-server-cert-check': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['disable', 'enable', 'strict'],
                            'type': 'str'
                        },
                        'status': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'deep-inspection'], 'type': 'str'},
                        'unsupported-ssl-cipher': {'v_range': [['6.4.5', '']], 'choices': ['allow', 'block'], 'type': 'str'},
                        'unsupported-ssl-negotiation': {'v_range': [['6.4.5', '']], 'choices': ['allow', 'block'], 'type': 'str'},
                        'untrusted-server-cert': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['allow', 'block', 'ignore'], 'type': 'str'},
                        'unsupported-ssl': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['bypass', 'inspect', 'block'], 'type': 'str'},
                        'client-cert-request': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['bypass', 'inspect', 'block'], 'type': 'str'},
                        'invalid-server-cert': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['allow', 'block'], 'type': 'str'},
                        'allow-invalid-server-cert': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '7.2.1']],
                            'choices': ['disable', 'enable'],
                            'type': 'str'
                        },
                        'untrusted-cert': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '7.2.1']], 'choices': ['allow', 'block', 'ignore'], 'type': 'str'},
                        'min-allowed-ssl-version': {
                            'v_range': [['7.0.3', '']],
                            'choices': ['ssl-3.0', 'tls-1.0', 'tls-1.1', 'tls-1.2', 'tls-1.3'],
                            'type': 'str'
                        },
                        'unsupported-ssl-version': {'v_range': [['7.0.1', '']], 'choices': ['block', 'allow', 'inspect'], 'type': 'str'}
                    }
                },
                'https': {
                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                    'type': 'dict',
                    'options': {
                        'cert-validation-failure': {'v_range': [['6.4.5', '']], 'choices': ['allow', 'block', 'ignore'], 'type': 'str'},
                        'cert-validation-timeout': {'v_range': [['6.4.5', '']], 'choices': ['allow', 'block', 'ignore'], 'type': 'str'},
                        'client-certificate': {'v_range': [['6.4.5', '']], 'choices': ['bypass', 'inspect', 'block'], 'type': 'str'},
                        'expired-server-cert': {'v_range': [['6.4.5', '']], 'choices': ['allow', 'block', 'ignore'], 'type': 'str'},
                        'ports': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'raw'},
                        'proxy-after-tcp-handshake': {'v_range': [['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'revoked-server-cert': {'v_range': [['6.4.5', '']], 'choices': ['allow', 'block', 'ignore'], 'type': 'str'},
                        'sni-server-cert-check': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['disable', 'enable', 'strict'],
                            'type': 'str'
                        },
                        'status': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['disable', 'certificate-inspection', 'deep-inspection'],
                            'type': 'str'
                        },
                        'unsupported-ssl-cipher': {'v_range': [['6.4.5', '']], 'choices': ['allow', 'block'], 'type': 'str'},
                        'unsupported-ssl-negotiation': {'v_range': [['6.4.5', '']], 'choices': ['allow', 'block'], 'type': 'str'},
                        'untrusted-server-cert': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['allow', 'block', 'ignore'], 'type': 'str'},
                        'unsupported-ssl': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['bypass', 'inspect', 'block'], 'type': 'str'},
                        'client-cert-request': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['bypass', 'inspect', 'block'], 'type': 'str'},
                        'invalid-server-cert': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['allow', 'block'], 'type': 'str'},
                        'allow-invalid-server-cert': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '7.2.1']],
                            'choices': ['disable', 'enable'],
                            'type': 'str'
                        },
                        'untrusted-cert': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '7.2.1']], 'choices': ['allow', 'block', 'ignore'], 'type': 'str'},
                        'cert-probe-failure': {'v_range': [['7.0.0', '']], 'choices': ['block', 'allow'], 'type': 'str'},
                        'min-allowed-ssl-version': {
                            'v_range': [['7.0.3', '']],
                            'choices': ['ssl-3.0', 'tls-1.0', 'tls-1.1', 'tls-1.2', 'tls-1.3'],
                            'type': 'str'
                        },
                        'unsupported-ssl-version': {'v_range': [['7.0.1', '']], 'choices': ['block', 'allow', 'inspect'], 'type': 'str'},
                        'quic': {'v_range': [['7.4.1', '']], 'choices': ['disable', 'enable', 'bypass', 'block', 'inspect'], 'type': 'str'},
                        'encrypted-client-hello': {'v_range': [['7.4.3', '']], 'choices': ['block', 'allow'], 'type': 'str'}
                    }
                },
                'imaps': {
                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                    'type': 'dict',
                    'options': {
                        'cert-validation-failure': {'v_range': [['6.4.5', '']], 'choices': ['allow', 'block', 'ignore'], 'type': 'str'},
                        'cert-validation-timeout': {'v_range': [['6.4.5', '']], 'choices': ['allow', 'block', 'ignore'], 'type': 'str'},
                        'client-certificate': {'v_range': [['6.4.5', '']], 'choices': ['bypass', 'inspect', 'block'], 'type': 'str'},
                        'expired-server-cert': {'v_range': [['6.4.5', '']], 'choices': ['allow', 'block', 'ignore'], 'type': 'str'},
                        'ports': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'raw'},
                        'proxy-after-tcp-handshake': {'v_range': [['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'revoked-server-cert': {'v_range': [['6.4.5', '']], 'choices': ['allow', 'block', 'ignore'], 'type': 'str'},
                        'sni-server-cert-check': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['disable', 'enable', 'strict'],
                            'type': 'str'
                        },
                        'status': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'deep-inspection'], 'type': 'str'},
                        'unsupported-ssl-cipher': {'v_range': [['6.4.5', '']], 'choices': ['allow', 'block'], 'type': 'str'},
                        'unsupported-ssl-negotiation': {'v_range': [['6.4.5', '']], 'choices': ['allow', 'block'], 'type': 'str'},
                        'untrusted-server-cert': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['allow', 'block', 'ignore'], 'type': 'str'},
                        'unsupported-ssl': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['bypass', 'inspect', 'block'], 'type': 'str'},
                        'client-cert-request': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['bypass', 'inspect', 'block'], 'type': 'str'},
                        'invalid-server-cert': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['allow', 'block'], 'type': 'str'},
                        'allow-invalid-server-cert': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '7.2.1']],
                            'choices': ['disable', 'enable'],
                            'type': 'str'
                        },
                        'untrusted-cert': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '7.2.1']], 'choices': ['allow', 'block', 'ignore'], 'type': 'str'},
                        'unsupported-ssl-version': {'v_range': [['7.0.1', '']], 'choices': ['block', 'allow', 'inspect'], 'type': 'str'},
                        'min-allowed-ssl-version': {
                            'v_range': [['7.0.3', '']],
                            'choices': ['ssl-3.0', 'tls-1.0', 'tls-1.1', 'tls-1.2', 'tls-1.3'],
                            'type': 'str'
                        }
                    }
                },
                'pop3s': {
                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                    'type': 'dict',
                    'options': {
                        'cert-validation-failure': {'v_range': [['6.4.5', '']], 'choices': ['allow', 'block', 'ignore'], 'type': 'str'},
                        'cert-validation-timeout': {'v_range': [['6.4.5', '']], 'choices': ['allow', 'block', 'ignore'], 'type': 'str'},
                        'client-certificate': {'v_range': [['6.4.5', '']], 'choices': ['bypass', 'inspect', 'block'], 'type': 'str'},
                        'expired-server-cert': {'v_range': [['6.4.5', '']], 'choices': ['allow', 'block', 'ignore'], 'type': 'str'},
                        'ports': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'raw'},
                        'proxy-after-tcp-handshake': {'v_range': [['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'revoked-server-cert': {'v_range': [['6.4.5', '']], 'choices': ['allow', 'block', 'ignore'], 'type': 'str'},
                        'sni-server-cert-check': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['disable', 'enable', 'strict'],
                            'type': 'str'
                        },
                        'status': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'deep-inspection'], 'type': 'str'},
                        'unsupported-ssl-cipher': {'v_range': [['6.4.5', '']], 'choices': ['allow', 'block'], 'type': 'str'},
                        'unsupported-ssl-negotiation': {'v_range': [['6.4.5', '']], 'choices': ['allow', 'block'], 'type': 'str'},
                        'untrusted-server-cert': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['allow', 'block', 'ignore'], 'type': 'str'},
                        'unsupported-ssl': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['bypass', 'inspect', 'block'], 'type': 'str'},
                        'client-cert-request': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['bypass', 'inspect', 'block'], 'type': 'str'},
                        'invalid-server-cert': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['allow', 'block'], 'type': 'str'},
                        'allow-invalid-server-cert': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '7.2.1']],
                            'choices': ['disable', 'enable'],
                            'type': 'str'
                        },
                        'untrusted-cert': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '7.2.1']], 'choices': ['allow', 'block', 'ignore'], 'type': 'str'},
                        'unsupported-ssl-version': {'v_range': [['7.0.1', '']], 'choices': ['block', 'allow', 'inspect'], 'type': 'str'},
                        'min-allowed-ssl-version': {
                            'v_range': [['7.0.3', '']],
                            'choices': ['ssl-3.0', 'tls-1.0', 'tls-1.1', 'tls-1.2', 'tls-1.3'],
                            'type': 'str'
                        }
                    }
                },
                'smtps': {
                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                    'type': 'dict',
                    'options': {
                        'cert-validation-failure': {'v_range': [['6.4.5', '']], 'choices': ['allow', 'block', 'ignore'], 'type': 'str'},
                        'cert-validation-timeout': {'v_range': [['6.4.5', '']], 'choices': ['allow', 'block', 'ignore'], 'type': 'str'},
                        'client-certificate': {'v_range': [['6.4.5', '']], 'choices': ['bypass', 'inspect', 'block'], 'type': 'str'},
                        'expired-server-cert': {'v_range': [['6.4.5', '']], 'choices': ['allow', 'block', 'ignore'], 'type': 'str'},
                        'ports': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'raw'},
                        'proxy-after-tcp-handshake': {'v_range': [['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'revoked-server-cert': {'v_range': [['6.4.5', '']], 'choices': ['allow', 'block', 'ignore'], 'type': 'str'},
                        'sni-server-cert-check': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['disable', 'enable', 'strict'],
                            'type': 'str'
                        },
                        'status': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'deep-inspection'], 'type': 'str'},
                        'unsupported-ssl-cipher': {'v_range': [['6.4.5', '']], 'choices': ['allow', 'block'], 'type': 'str'},
                        'unsupported-ssl-negotiation': {'v_range': [['6.4.5', '']], 'choices': ['allow', 'block'], 'type': 'str'},
                        'untrusted-server-cert': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['allow', 'block', 'ignore'], 'type': 'str'},
                        'unsupported-ssl': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['bypass', 'inspect', 'block'], 'type': 'str'},
                        'client-cert-request': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['bypass', 'inspect', 'block'], 'type': 'str'},
                        'invalid-server-cert': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['allow', 'block'], 'type': 'str'},
                        'allow-invalid-server-cert': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '7.2.1']],
                            'choices': ['disable', 'enable'],
                            'type': 'str'
                        },
                        'untrusted-cert': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '7.2.1']], 'choices': ['allow', 'block', 'ignore'], 'type': 'str'},
                        'unsupported-ssl-version': {'v_range': [['7.0.1', '']], 'choices': ['block', 'allow', 'inspect'], 'type': 'str'},
                        'min-allowed-ssl-version': {
                            'v_range': [['7.0.3', '']],
                            'choices': ['ssl-3.0', 'tls-1.0', 'tls-1.1', 'tls-1.2', 'tls-1.3'],
                            'type': 'str'
                        }
                    }
                },
                'ssh': {
                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                    'type': 'dict',
                    'options': {
                        'inspect-all': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'deep-inspection'], 'type': 'str'},
                        'ports': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'raw'},
                        'proxy-after-tcp-handshake': {'v_range': [['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'ssh-algorithm': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['compatible', 'high-encryption'], 'type': 'str'},
                        'ssh-tun-policy-check': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'status': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'deep-inspection'], 'type': 'str'},
                        'unsupported-version': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['block', 'bypass'], 'type': 'str'},
                        'ssh-policy-check': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '7.2.1']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'block': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '6.4.14']],
                            'type': 'list',
                            'choices': ['x11-filter', 'ssh-shell', 'exec', 'port-forward'],
                            'elements': 'str'
                        },
                        'log': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '6.4.14']],
                            'type': 'list',
                            'choices': ['x11-filter', 'ssh-shell', 'exec', 'port-forward'],
                            'elements': 'str'
                        }
                    }
                },
                'ssl': {
                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                    'type': 'dict',
                    'options': {
                        'cert-validation-failure': {'v_range': [['6.4.5', '']], 'choices': ['allow', 'block', 'ignore'], 'type': 'str'},
                        'cert-validation-timeout': {'v_range': [['6.4.5', '']], 'choices': ['allow', 'block', 'ignore'], 'type': 'str'},
                        'client-certificate': {'v_range': [['6.4.5', '']], 'choices': ['bypass', 'inspect', 'block'], 'type': 'str'},
                        'expired-server-cert': {'v_range': [['6.4.5', '']], 'choices': ['allow', 'block', 'ignore'], 'type': 'str'},
                        'inspect-all': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['disable', 'certificate-inspection', 'deep-inspection'],
                            'type': 'str'
                        },
                        'revoked-server-cert': {'v_range': [['6.4.5', '']], 'choices': ['allow', 'block', 'ignore'], 'type': 'str'},
                        'sni-server-cert-check': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['disable', 'enable', 'strict'],
                            'type': 'str'
                        },
                        'unsupported-ssl-cipher': {'v_range': [['6.4.5', '']], 'choices': ['allow', 'block'], 'type': 'str'},
                        'unsupported-ssl-negotiation': {'v_range': [['6.4.5', '']], 'choices': ['allow', 'block'], 'type': 'str'},
                        'untrusted-server-cert': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['allow', 'block', 'ignore'], 'type': 'str'},
                        'unsupported-ssl': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['bypass', 'inspect', 'block'], 'type': 'str'},
                        'client-cert-request': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['bypass', 'inspect', 'block'], 'type': 'str'},
                        'invalid-server-cert': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['allow', 'block'], 'type': 'str'},
                        'allow-invalid-server-cert': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '7.2.1']],
                            'choices': ['disable', 'enable'],
                            'type': 'str'
                        },
                        'untrusted-cert': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '7.2.1']], 'choices': ['allow', 'block', 'ignore'], 'type': 'str'},
                        'cert-probe-failure': {'v_range': [['7.0.1', '']], 'choices': ['block', 'allow'], 'type': 'str'},
                        'min-allowed-ssl-version': {
                            'v_range': [['7.0.3', '']],
                            'choices': ['ssl-3.0', 'tls-1.0', 'tls-1.1', 'tls-1.2', 'tls-1.3'],
                            'type': 'str'
                        },
                        'unsupported-ssl-version': {'v_range': [['7.0.1', '']], 'choices': ['block', 'allow', 'inspect'], 'type': 'str'},
                        'encrypted-client-hello': {'v_range': [['7.4.3', '']], 'choices': ['block', 'allow'], 'type': 'str'}
                    }
                },
                'allowlist': {'v_range': [['7.0.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'block-blocklisted-certificates': {'v_range': [['7.0.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'dot': {
                    'v_range': [['7.0.0', '']],
                    'type': 'dict',
                    'options': {
                        'cert-validation-failure': {'v_range': [['7.0.0', '']], 'choices': ['allow', 'block', 'ignore'], 'type': 'str'},
                        'cert-validation-timeout': {'v_range': [['7.0.0', '']], 'choices': ['allow', 'block', 'ignore'], 'type': 'str'},
                        'client-certificate': {'v_range': [['7.0.0', '']], 'choices': ['bypass', 'inspect', 'block'], 'type': 'str'},
                        'expired-server-cert': {'v_range': [['7.0.0', '']], 'choices': ['allow', 'block', 'ignore'], 'type': 'str'},
                        'proxy-after-tcp-handshake': {'v_range': [['7.0.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'revoked-server-cert': {'v_range': [['7.0.0', '']], 'choices': ['allow', 'block', 'ignore'], 'type': 'str'},
                        'sni-server-cert-check': {'v_range': [['7.0.0', '']], 'choices': ['enable', 'strict', 'disable'], 'type': 'str'},
                        'status': {'v_range': [['7.0.0', '']], 'choices': ['disable', 'deep-inspection'], 'type': 'str'},
                        'unsupported-ssl-cipher': {'v_range': [['7.0.0', '']], 'choices': ['block', 'allow'], 'type': 'str'},
                        'unsupported-ssl-negotiation': {'v_range': [['7.0.0', '']], 'choices': ['block', 'allow'], 'type': 'str'},
                        'untrusted-server-cert': {'v_range': [['7.0.0', '']], 'choices': ['allow', 'block', 'ignore'], 'type': 'str'},
                        'unsupported-ssl-version': {'v_range': [['7.0.1', '']], 'choices': ['block', 'allow', 'inspect'], 'type': 'str'},
                        'min-allowed-ssl-version': {
                            'v_range': [['7.0.3', '']],
                            'choices': ['ssl-3.0', 'tls-1.0', 'tls-1.1', 'tls-1.2', 'tls-1.3'],
                            'type': 'str'
                        },
                        'quic': {'v_range': [['7.4.1', '']], 'choices': ['disable', 'enable', 'bypass', 'block', 'inspect'], 'type': 'str'}
                    }
                },
                'supported-alpn': {'v_range': [['7.0.0', '']], 'choices': ['none', 'http1-1', 'http2', 'all'], 'type': 'str'},
                'ssl-anomaly-log': {'v_range': [['7.0.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ssl-exemption-ip-rating': {'v_range': [['7.0.4', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ssl-exemption-log': {'v_range': [['7.0.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ssl-handshake-log': {'v_range': [['7.0.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ssl-server-cert-log': {'v_range': [['7.0.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ech-outer-sni': {
                    'v_range': [['7.4.3', '']],
                    'type': 'list',
                    'options': {'name': {'v_range': [['7.4.3', '']], 'type': 'str'}, 'sni': {'v_range': [['7.4.3', '']], 'type': 'str'}},
                    'elements': 'dict'
                }
            }

        }
    }

    module_option_spec = get_module_arg_spec('full crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'firewall_sslsshprofile'),
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
