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
module: fmgr_user_radius
short_description: Configure RADIUS server entries.
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
    user_radius:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            accounting-server:
                type: list
                elements: dict
                description: Deprecated, please rename it to accounting_server. Accounting server.
                suboptions:
                    id:
                        type: int
                        description: ID
                    port:
                        type: int
                        description: RADIUS accounting port number.
                    secret:
                        type: raw
                        description: (list) Secret key.
                    server:
                        type: str
                        description: No description
                    source-ip:
                        type: str
                        description: Deprecated, please rename it to source_ip. Source IP address for communications to the RADIUS server.
                    status:
                        type: str
                        description: Status.
                        choices:
                            - 'disable'
                            - 'enable'
                    interface:
                        type: str
                        description: Specify outgoing interface to reach server.
                    interface-select-method:
                        type: str
                        description: Deprecated, please rename it to interface_select_method. Specify how to select outgoing interface to reach server.
                        choices:
                            - 'auto'
                            - 'sdwan'
                            - 'specify'
            acct-all-servers:
                type: str
                description: Deprecated, please rename it to acct_all_servers. Enable/disable sending of accounting messages to all configured servers
                choices:
                    - 'disable'
                    - 'enable'
            acct-interim-interval:
                type: int
                description: Deprecated, please rename it to acct_interim_interval. Time in seconds between each accounting interim update message.
            all-usergroup:
                type: str
                description: Deprecated, please rename it to all_usergroup. Enable/disable automatically including this RADIUS server in all user groups.
                choices:
                    - 'disable'
                    - 'enable'
            auth-type:
                type: str
                description: Deprecated, please rename it to auth_type. Authentication methods/protocols permitted for this RADIUS server.
                choices:
                    - 'pap'
                    - 'chap'
                    - 'ms_chap'
                    - 'ms_chap_v2'
                    - 'auto'
            class:
                type: raw
                description: (list) Class attribute name
            dynamic_mapping:
                type: list
                elements: dict
                description: Dynamic mapping.
                suboptions:
                    _scope:
                        type: list
                        elements: dict
                        description: Scope.
                        suboptions:
                            name:
                                type: str
                                description: Name.
                            vdom:
                                type: str
                                description: Vdom.
                    acct-all-servers:
                        type: str
                        description: Deprecated, please rename it to acct_all_servers. Acct all servers.
                        choices:
                            - 'disable'
                            - 'enable'
                    acct-interim-interval:
                        type: int
                        description: Deprecated, please rename it to acct_interim_interval. Acct interim interval.
                    all-usergroup:
                        type: str
                        description: Deprecated, please rename it to all_usergroup. All usergroup.
                        choices:
                            - 'disable'
                            - 'enable'
                    auth-type:
                        type: str
                        description: Deprecated, please rename it to auth_type. Auth type.
                        choices:
                            - 'pap'
                            - 'chap'
                            - 'ms_chap'
                            - 'ms_chap_v2'
                            - 'auto'
                    class:
                        type: raw
                        description: (list) Class.
                    dp-carrier-endpoint-attribute:
                        type: str
                        description: Deprecated, please rename it to dp_carrier_endpoint_attribute. Dp carrier endpoint attribute.
                        choices:
                            - 'User-Name'
                            - 'User-Password'
                            - 'CHAP-Password'
                            - 'NAS-IP-Address'
                            - 'NAS-Port'
                            - 'Service-Type'
                            - 'Framed-Protocol'
                            - 'Framed-IP-Address'
                            - 'Framed-IP-Netmask'
                            - 'Framed-Routing'
                            - 'Filter-Id'
                            - 'Framed-MTU'
                            - 'Framed-Compression'
                            - 'Login-IP-Host'
                            - 'Login-Service'
                            - 'Login-TCP-Port'
                            - 'Reply-Message'
                            - 'Callback-Number'
                            - 'Callback-Id'
                            - 'Framed-Route'
                            - 'Framed-IPX-Network'
                            - 'State'
                            - 'Class'
                            - 'Vendor-Specific'
                            - 'Session-Timeout'
                            - 'Idle-Timeout'
                            - 'Termination-Action'
                            - 'Called-Station-Id'
                            - 'Calling-Station-Id'
                            - 'NAS-Identifier'
                            - 'Proxy-State'
                            - 'Login-LAT-Service'
                            - 'Login-LAT-Node'
                            - 'Login-LAT-Group'
                            - 'Framed-AppleTalk-Link'
                            - 'Framed-AppleTalk-Network'
                            - 'Framed-AppleTalk-Zone'
                            - 'Acct-Status-Type'
                            - 'Acct-Delay-Time'
                            - 'Acct-Input-Octets'
                            - 'Acct-Output-Octets'
                            - 'Acct-Session-Id'
                            - 'Acct-Authentic'
                            - 'Acct-Session-Time'
                            - 'Acct-Input-Packets'
                            - 'Acct-Output-Packets'
                            - 'Acct-Terminate-Cause'
                            - 'Acct-Multi-Session-Id'
                            - 'Acct-Link-Count'
                            - 'CHAP-Challenge'
                            - 'NAS-Port-Type'
                            - 'Port-Limit'
                            - 'Login-LAT-Port'
                    dp-carrier-endpoint-block-attribute:
                        type: str
                        description: Deprecated, please rename it to dp_carrier_endpoint_block_attribute. Dp carrier endpoint block attribute.
                        choices:
                            - 'User-Name'
                            - 'User-Password'
                            - 'CHAP-Password'
                            - 'NAS-IP-Address'
                            - 'NAS-Port'
                            - 'Service-Type'
                            - 'Framed-Protocol'
                            - 'Framed-IP-Address'
                            - 'Framed-IP-Netmask'
                            - 'Framed-Routing'
                            - 'Filter-Id'
                            - 'Framed-MTU'
                            - 'Framed-Compression'
                            - 'Login-IP-Host'
                            - 'Login-Service'
                            - 'Login-TCP-Port'
                            - 'Reply-Message'
                            - 'Callback-Number'
                            - 'Callback-Id'
                            - 'Framed-Route'
                            - 'Framed-IPX-Network'
                            - 'State'
                            - 'Class'
                            - 'Vendor-Specific'
                            - 'Session-Timeout'
                            - 'Idle-Timeout'
                            - 'Termination-Action'
                            - 'Called-Station-Id'
                            - 'Calling-Station-Id'
                            - 'NAS-Identifier'
                            - 'Proxy-State'
                            - 'Login-LAT-Service'
                            - 'Login-LAT-Node'
                            - 'Login-LAT-Group'
                            - 'Framed-AppleTalk-Link'
                            - 'Framed-AppleTalk-Network'
                            - 'Framed-AppleTalk-Zone'
                            - 'Acct-Status-Type'
                            - 'Acct-Delay-Time'
                            - 'Acct-Input-Octets'
                            - 'Acct-Output-Octets'
                            - 'Acct-Session-Id'
                            - 'Acct-Authentic'
                            - 'Acct-Session-Time'
                            - 'Acct-Input-Packets'
                            - 'Acct-Output-Packets'
                            - 'Acct-Terminate-Cause'
                            - 'Acct-Multi-Session-Id'
                            - 'Acct-Link-Count'
                            - 'CHAP-Challenge'
                            - 'NAS-Port-Type'
                            - 'Port-Limit'
                            - 'Login-LAT-Port'
                    dp-context-timeout:
                        type: int
                        description: Deprecated, please rename it to dp_context_timeout. Dp context timeout.
                    dp-flush-ip-session:
                        type: str
                        description: Deprecated, please rename it to dp_flush_ip_session. Dp flush ip session.
                        choices:
                            - 'disable'
                            - 'enable'
                    dp-hold-time:
                        type: int
                        description: Deprecated, please rename it to dp_hold_time. Dp hold time.
                    dp-http-header:
                        type: str
                        description: Deprecated, please rename it to dp_http_header. Dp http header.
                    dp-http-header-fallback:
                        type: str
                        description: Deprecated, please rename it to dp_http_header_fallback. Dp http header fallback.
                        choices:
                            - 'ip-header-address'
                            - 'default-profile'
                    dp-http-header-status:
                        type: str
                        description: Deprecated, please rename it to dp_http_header_status. Dp http header status.
                        choices:
                            - 'disable'
                            - 'enable'
                    dp-http-header-suppress:
                        type: str
                        description: Deprecated, please rename it to dp_http_header_suppress. Dp http header suppress.
                        choices:
                            - 'disable'
                            - 'enable'
                    dp-log-dyn_flags:
                        type: list
                        elements: str
                        description: Deprecated, please rename it to dp_log_dyn_flags. Dp log dyn flags.
                        choices:
                            - 'none'
                            - 'protocol-error'
                            - 'profile-missing'
                            - 'context-missing'
                            - 'accounting-stop-missed'
                            - 'accounting-event'
                            - 'radiusd-other'
                            - 'endpoint-block'
                    dp-log-period:
                        type: int
                        description: Deprecated, please rename it to dp_log_period. Dp log period.
                    dp-mem-percent:
                        type: int
                        description: Deprecated, please rename it to dp_mem_percent. Dp mem percent.
                    dp-profile-attribute:
                        type: str
                        description: Deprecated, please rename it to dp_profile_attribute. Dp profile attribute.
                        choices:
                            - 'User-Name'
                            - 'User-Password'
                            - 'CHAP-Password'
                            - 'NAS-IP-Address'
                            - 'NAS-Port'
                            - 'Service-Type'
                            - 'Framed-Protocol'
                            - 'Framed-IP-Address'
                            - 'Framed-IP-Netmask'
                            - 'Framed-Routing'
                            - 'Filter-Id'
                            - 'Framed-MTU'
                            - 'Framed-Compression'
                            - 'Login-IP-Host'
                            - 'Login-Service'
                            - 'Login-TCP-Port'
                            - 'Reply-Message'
                            - 'Callback-Number'
                            - 'Callback-Id'
                            - 'Framed-Route'
                            - 'Framed-IPX-Network'
                            - 'State'
                            - 'Class'
                            - 'Vendor-Specific'
                            - 'Session-Timeout'
                            - 'Idle-Timeout'
                            - 'Termination-Action'
                            - 'Called-Station-Id'
                            - 'Calling-Station-Id'
                            - 'NAS-Identifier'
                            - 'Proxy-State'
                            - 'Login-LAT-Service'
                            - 'Login-LAT-Node'
                            - 'Login-LAT-Group'
                            - 'Framed-AppleTalk-Link'
                            - 'Framed-AppleTalk-Network'
                            - 'Framed-AppleTalk-Zone'
                            - 'Acct-Status-Type'
                            - 'Acct-Delay-Time'
                            - 'Acct-Input-Octets'
                            - 'Acct-Output-Octets'
                            - 'Acct-Session-Id'
                            - 'Acct-Authentic'
                            - 'Acct-Session-Time'
                            - 'Acct-Input-Packets'
                            - 'Acct-Output-Packets'
                            - 'Acct-Terminate-Cause'
                            - 'Acct-Multi-Session-Id'
                            - 'Acct-Link-Count'
                            - 'CHAP-Challenge'
                            - 'NAS-Port-Type'
                            - 'Port-Limit'
                            - 'Login-LAT-Port'
                    dp-profile-attribute-key:
                        type: str
                        description: Deprecated, please rename it to dp_profile_attribute_key. Dp profile attribute key.
                    dp-radius-response:
                        type: str
                        description: Deprecated, please rename it to dp_radius_response. Dp radius response.
                        choices:
                            - 'disable'
                            - 'enable'
                    dp-radius-server-port:
                        type: int
                        description: Deprecated, please rename it to dp_radius_server_port. Dp radius server port.
                    dp-secret:
                        type: raw
                        description: (list) Deprecated, please rename it to dp_secret. Dp secret.
                    dp-validate-request-secret:
                        type: str
                        description: Deprecated, please rename it to dp_validate_request_secret. Dp validate request secret.
                        choices:
                            - 'disable'
                            - 'enable'
                    dynamic-profile:
                        type: str
                        description: Deprecated, please rename it to dynamic_profile. Dynamic profile.
                        choices:
                            - 'disable'
                            - 'enable'
                    endpoint-translation:
                        type: str
                        description: Deprecated, please rename it to endpoint_translation. Endpoint translation.
                        choices:
                            - 'disable'
                            - 'enable'
                    ep-carrier-endpoint-convert-hex:
                        type: str
                        description: Deprecated, please rename it to ep_carrier_endpoint_convert_hex. Ep carrier endpoint convert hex.
                        choices:
                            - 'disable'
                            - 'enable'
                    ep-carrier-endpoint-header:
                        type: str
                        description: Deprecated, please rename it to ep_carrier_endpoint_header. Ep carrier endpoint header.
                    ep-carrier-endpoint-header-suppress:
                        type: str
                        description: Deprecated, please rename it to ep_carrier_endpoint_header_suppress. Ep carrier endpoint header suppress.
                        choices:
                            - 'disable'
                            - 'enable'
                    ep-carrier-endpoint-prefix:
                        type: str
                        description: Deprecated, please rename it to ep_carrier_endpoint_prefix. Ep carrier endpoint prefix.
                        choices:
                            - 'disable'
                            - 'enable'
                    ep-carrier-endpoint-prefix-range-max:
                        type: int
                        description: Deprecated, please rename it to ep_carrier_endpoint_prefix_range_max. Ep carrier endpoint prefix range max.
                    ep-carrier-endpoint-prefix-range-min:
                        type: int
                        description: Deprecated, please rename it to ep_carrier_endpoint_prefix_range_min. Ep carrier endpoint prefix range min.
                    ep-carrier-endpoint-prefix-string:
                        type: str
                        description: Deprecated, please rename it to ep_carrier_endpoint_prefix_string. Ep carrier endpoint prefix string.
                    ep-carrier-endpoint-source:
                        type: str
                        description: Deprecated, please rename it to ep_carrier_endpoint_source. Ep carrier endpoint source.
                        choices:
                            - 'http-header'
                            - 'cookie'
                    ep-ip-header:
                        type: str
                        description: Deprecated, please rename it to ep_ip_header. Ep ip header.
                    ep-ip-header-suppress:
                        type: str
                        description: Deprecated, please rename it to ep_ip_header_suppress. Ep ip header suppress.
                        choices:
                            - 'disable'
                            - 'enable'
                    ep-missing-header-fallback:
                        type: str
                        description: Deprecated, please rename it to ep_missing_header_fallback. Ep missing header fallback.
                        choices:
                            - 'session-ip'
                            - 'policy-profile'
                    ep-profile-query-type:
                        type: str
                        description: Deprecated, please rename it to ep_profile_query_type. Ep profile query type.
                        choices:
                            - 'session-ip'
                            - 'extract-ip'
                            - 'extract-carrier-endpoint'
                    h3c-compatibility:
                        type: str
                        description: Deprecated, please rename it to h3c_compatibility. H3c compatibility.
                        choices:
                            - 'disable'
                            - 'enable'
                    nas-ip:
                        type: str
                        description: Deprecated, please rename it to nas_ip. Nas ip.
                    password-encoding:
                        type: str
                        description: Deprecated, please rename it to password_encoding. Password encoding.
                        choices:
                            - 'ISO-8859-1'
                            - 'auto'
                    password-renewal:
                        type: str
                        description: Deprecated, please rename it to password_renewal. Password renewal.
                        choices:
                            - 'disable'
                            - 'enable'
                    radius-coa:
                        type: str
                        description: Deprecated, please rename it to radius_coa. Radius coa.
                        choices:
                            - 'disable'
                            - 'enable'
                    radius-port:
                        type: int
                        description: Deprecated, please rename it to radius_port. Radius port.
                    rsso:
                        type: str
                        description: Rsso.
                        choices:
                            - 'disable'
                            - 'enable'
                    rsso-context-timeout:
                        type: int
                        description: Deprecated, please rename it to rsso_context_timeout. Rsso context timeout.
                    rsso-endpoint-attribute:
                        type: str
                        description: Deprecated, please rename it to rsso_endpoint_attribute. Rsso endpoint attribute.
                        choices:
                            - 'User-Name'
                            - 'User-Password'
                            - 'CHAP-Password'
                            - 'NAS-IP-Address'
                            - 'NAS-Port'
                            - 'Service-Type'
                            - 'Framed-Protocol'
                            - 'Framed-IP-Address'
                            - 'Framed-IP-Netmask'
                            - 'Framed-Routing'
                            - 'Filter-Id'
                            - 'Framed-MTU'
                            - 'Framed-Compression'
                            - 'Login-IP-Host'
                            - 'Login-Service'
                            - 'Login-TCP-Port'
                            - 'Reply-Message'
                            - 'Callback-Number'
                            - 'Callback-Id'
                            - 'Framed-Route'
                            - 'Framed-IPX-Network'
                            - 'State'
                            - 'Class'
                            - 'Session-Timeout'
                            - 'Idle-Timeout'
                            - 'Termination-Action'
                            - 'Called-Station-Id'
                            - 'Calling-Station-Id'
                            - 'NAS-Identifier'
                            - 'Proxy-State'
                            - 'Login-LAT-Service'
                            - 'Login-LAT-Node'
                            - 'Login-LAT-Group'
                            - 'Framed-AppleTalk-Link'
                            - 'Framed-AppleTalk-Network'
                            - 'Framed-AppleTalk-Zone'
                            - 'Acct-Status-Type'
                            - 'Acct-Delay-Time'
                            - 'Acct-Input-Octets'
                            - 'Acct-Output-Octets'
                            - 'Acct-Session-Id'
                            - 'Acct-Authentic'
                            - 'Acct-Session-Time'
                            - 'Acct-Input-Packets'
                            - 'Acct-Output-Packets'
                            - 'Acct-Terminate-Cause'
                            - 'Acct-Multi-Session-Id'
                            - 'Acct-Link-Count'
                            - 'CHAP-Challenge'
                            - 'NAS-Port-Type'
                            - 'Port-Limit'
                            - 'Login-LAT-Port'
                    rsso-endpoint-block-attribute:
                        type: str
                        description: Deprecated, please rename it to rsso_endpoint_block_attribute. Rsso endpoint block attribute.
                        choices:
                            - 'User-Name'
                            - 'User-Password'
                            - 'CHAP-Password'
                            - 'NAS-IP-Address'
                            - 'NAS-Port'
                            - 'Service-Type'
                            - 'Framed-Protocol'
                            - 'Framed-IP-Address'
                            - 'Framed-IP-Netmask'
                            - 'Framed-Routing'
                            - 'Filter-Id'
                            - 'Framed-MTU'
                            - 'Framed-Compression'
                            - 'Login-IP-Host'
                            - 'Login-Service'
                            - 'Login-TCP-Port'
                            - 'Reply-Message'
                            - 'Callback-Number'
                            - 'Callback-Id'
                            - 'Framed-Route'
                            - 'Framed-IPX-Network'
                            - 'State'
                            - 'Class'
                            - 'Session-Timeout'
                            - 'Idle-Timeout'
                            - 'Termination-Action'
                            - 'Called-Station-Id'
                            - 'Calling-Station-Id'
                            - 'NAS-Identifier'
                            - 'Proxy-State'
                            - 'Login-LAT-Service'
                            - 'Login-LAT-Node'
                            - 'Login-LAT-Group'
                            - 'Framed-AppleTalk-Link'
                            - 'Framed-AppleTalk-Network'
                            - 'Framed-AppleTalk-Zone'
                            - 'Acct-Status-Type'
                            - 'Acct-Delay-Time'
                            - 'Acct-Input-Octets'
                            - 'Acct-Output-Octets'
                            - 'Acct-Session-Id'
                            - 'Acct-Authentic'
                            - 'Acct-Session-Time'
                            - 'Acct-Input-Packets'
                            - 'Acct-Output-Packets'
                            - 'Acct-Terminate-Cause'
                            - 'Acct-Multi-Session-Id'
                            - 'Acct-Link-Count'
                            - 'CHAP-Challenge'
                            - 'NAS-Port-Type'
                            - 'Port-Limit'
                            - 'Login-LAT-Port'
                    rsso-ep-one-ip-only:
                        type: str
                        description: Deprecated, please rename it to rsso_ep_one_ip_only. Rsso ep one ip only.
                        choices:
                            - 'disable'
                            - 'enable'
                    rsso-flush-ip-session:
                        type: str
                        description: Deprecated, please rename it to rsso_flush_ip_session. Rsso flush ip session.
                        choices:
                            - 'disable'
                            - 'enable'
                    rsso-log-flags:
                        type: list
                        elements: str
                        description: Deprecated, please rename it to rsso_log_flags. Rsso log flags.
                        choices:
                            - 'none'
                            - 'protocol-error'
                            - 'profile-missing'
                            - 'context-missing'
                            - 'accounting-stop-missed'
                            - 'accounting-event'
                            - 'radiusd-other'
                            - 'endpoint-block'
                    rsso-log-period:
                        type: int
                        description: Deprecated, please rename it to rsso_log_period. Rsso log period.
                    rsso-radius-response:
                        type: str
                        description: Deprecated, please rename it to rsso_radius_response. Rsso radius response.
                        choices:
                            - 'disable'
                            - 'enable'
                    rsso-radius-server-port:
                        type: int
                        description: Deprecated, please rename it to rsso_radius_server_port. Rsso radius server port.
                    rsso-secret:
                        type: raw
                        description: (list) Deprecated, please rename it to rsso_secret. Rsso secret.
                    rsso-validate-request-secret:
                        type: str
                        description: Deprecated, please rename it to rsso_validate_request_secret. Rsso validate request secret.
                        choices:
                            - 'disable'
                            - 'enable'
                    secondary-secret:
                        type: raw
                        description: (list) Deprecated, please rename it to secondary_secret. Secondary secret.
                    secondary-server:
                        type: str
                        description: Deprecated, please rename it to secondary_server. Secondary server.
                    secret:
                        type: raw
                        description: (list) Secret.
                    server:
                        type: str
                        description: Server.
                    source-ip:
                        type: str
                        description: Deprecated, please rename it to source_ip. Source ip.
                    sso-attribute:
                        type: str
                        description: Deprecated, please rename it to sso_attribute. Sso attribute.
                        choices:
                            - 'User-Name'
                            - 'User-Password'
                            - 'CHAP-Password'
                            - 'NAS-IP-Address'
                            - 'NAS-Port'
                            - 'Service-Type'
                            - 'Framed-Protocol'
                            - 'Framed-IP-Address'
                            - 'Framed-IP-Netmask'
                            - 'Framed-Routing'
                            - 'Filter-Id'
                            - 'Framed-MTU'
                            - 'Framed-Compression'
                            - 'Login-IP-Host'
                            - 'Login-Service'
                            - 'Login-TCP-Port'
                            - 'Reply-Message'
                            - 'Callback-Number'
                            - 'Callback-Id'
                            - 'Framed-Route'
                            - 'Framed-IPX-Network'
                            - 'State'
                            - 'Class'
                            - 'Session-Timeout'
                            - 'Idle-Timeout'
                            - 'Termination-Action'
                            - 'Called-Station-Id'
                            - 'Calling-Station-Id'
                            - 'NAS-Identifier'
                            - 'Proxy-State'
                            - 'Login-LAT-Service'
                            - 'Login-LAT-Node'
                            - 'Login-LAT-Group'
                            - 'Framed-AppleTalk-Link'
                            - 'Framed-AppleTalk-Network'
                            - 'Framed-AppleTalk-Zone'
                            - 'Acct-Status-Type'
                            - 'Acct-Delay-Time'
                            - 'Acct-Input-Octets'
                            - 'Acct-Output-Octets'
                            - 'Acct-Session-Id'
                            - 'Acct-Authentic'
                            - 'Acct-Session-Time'
                            - 'Acct-Input-Packets'
                            - 'Acct-Output-Packets'
                            - 'Acct-Terminate-Cause'
                            - 'Acct-Multi-Session-Id'
                            - 'Acct-Link-Count'
                            - 'CHAP-Challenge'
                            - 'NAS-Port-Type'
                            - 'Port-Limit'
                            - 'Login-LAT-Port'
                    sso-attribute-key:
                        type: str
                        description: Deprecated, please rename it to sso_attribute_key. Sso attribute key.
                    sso-attribute-value-override:
                        type: str
                        description: Deprecated, please rename it to sso_attribute_value_override. Sso attribute value override.
                        choices:
                            - 'disable'
                            - 'enable'
                    tertiary-secret:
                        type: raw
                        description: (list) Deprecated, please rename it to tertiary_secret. Tertiary secret.
                    tertiary-server:
                        type: str
                        description: Deprecated, please rename it to tertiary_server. Tertiary server.
                    timeout:
                        type: int
                        description: Timeout.
                    use-group-for-profile:
                        type: str
                        description: Deprecated, please rename it to use_group_for_profile. Use group for profile.
                        choices:
                            - 'disable'
                            - 'enable'
                    use-management-vdom:
                        type: str
                        description: Deprecated, please rename it to use_management_vdom. Use management vdom.
                        choices:
                            - 'disable'
                            - 'enable'
                    username-case-sensitive:
                        type: str
                        description: Deprecated, please rename it to username_case_sensitive. Username case sensitive.
                        choices:
                            - 'disable'
                            - 'enable'
                    interface:
                        type: str
                        description: Interface.
                    interface-select-method:
                        type: str
                        description: Deprecated, please rename it to interface_select_method. Interface select method.
                        choices:
                            - 'auto'
                            - 'sdwan'
                            - 'specify'
                    group-override-attr-type:
                        type: str
                        description: Deprecated, please rename it to group_override_attr_type. Group override attr type.
                        choices:
                            - 'filter-Id'
                            - 'class'
                    switch-controller-acct-fast-framedip-detect:
                        type: int
                        description: Deprecated, please rename it to switch_controller_acct_fast_framedip_detect. Switch controller acct fast framedip ...
                    accounting-server:
                        type: list
                        elements: dict
                        description: Deprecated, please rename it to accounting_server. Accounting server.
                        suboptions:
                            id:
                                type: int
                                description: Id.
                            interface:
                                type: str
                                description: Interface.
                            interface-select-method:
                                type: str
                                description: Deprecated, please rename it to interface_select_method. Interface select method.
                                choices:
                                    - 'auto'
                                    - 'sdwan'
                                    - 'specify'
                            port:
                                type: int
                                description: Port.
                            secret:
                                type: raw
                                description: (list) Secret.
                            server:
                                type: str
                                description: Server.
                            source-ip:
                                type: str
                                description: Deprecated, please rename it to source_ip. Source ip.
                            status:
                                type: str
                                description: Status.
                                choices:
                                    - 'disable'
                                    - 'enable'
                    switch-controller-service-type:
                        type: list
                        elements: str
                        description: Deprecated, please rename it to switch_controller_service_type. Switch controller service type.
                        choices:
                            - 'login'
                            - 'framed'
                            - 'callback-login'
                            - 'callback-framed'
                            - 'outbound'
                            - 'administrative'
                            - 'nas-prompt'
                            - 'authenticate-only'
                            - 'callback-nas-prompt'
                            - 'call-check'
                            - 'callback-administrative'
                    delimiter:
                        type: str
                        description: Configure delimiter to be used for separating profile group names in the SSO attribute
                        choices:
                            - 'plus'
                            - 'comma'
                    mac-case:
                        type: str
                        description: Deprecated, please rename it to mac_case. MAC authentication case
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
                    nas-id:
                        type: str
                        description: Deprecated, please rename it to nas_id. Custom NAS identifier.
                    nas-id-type:
                        type: str
                        description: Deprecated, please rename it to nas_id_type. NAS identifier type configuration
                        choices:
                            - 'legacy'
                            - 'custom'
                            - 'hostname'
                    ca-cert:
                        type: str
                        description: Deprecated, please rename it to ca_cert. CA of server to trust under TLS.
                    client-cert:
                        type: str
                        description: Deprecated, please rename it to client_cert. Client certificate to use under TLS.
                    server-identity-check:
                        type: str
                        description: Deprecated, please rename it to server_identity_check. Enable/disable RADIUS server identity check
                        choices:
                            - 'disable'
                            - 'enable'
                    status-ttl:
                        type: int
                        description: Deprecated, please rename it to status_ttl. Time for which server reachability is cached so that when a server is ...
                    tls-min-proto-version:
                        type: str
                        description: Deprecated, please rename it to tls_min_proto_version. Minimum supported protocol version for TLS connections
                        choices:
                            - 'default'
                            - 'TLSv1'
                            - 'TLSv1-1'
                            - 'TLSv1-2'
                            - 'SSLv3'
                            - 'TLSv1-3'
                    transport-protocol:
                        type: str
                        description: Deprecated, please rename it to transport_protocol. Transport protocol to be used
                        choices:
                            - 'udp'
                            - 'tcp'
                            - 'tls'
                    account-key-cert-field:
                        type: str
                        description: Deprecated, please rename it to account_key_cert_field. Define subject identity field in certificate for user acce...
                        choices:
                            - 'othername'
                            - 'rfc822name'
                            - 'dnsname'
                            - 'cn'
                    account-key-processing:
                        type: str
                        description: Deprecated, please rename it to account_key_processing. Account key processing operation.
                        choices:
                            - 'same'
                            - 'strip'
                    call-station-id-type:
                        type: str
                        description: Deprecated, please rename it to call_station_id_type. Calling & Called station identifier type configuration
                        choices:
                            - 'legacy'
                            - 'IP'
                            - 'MAC'
                    switch-controller-nas-ip-dynamic:
                        type: str
                        description: Deprecated, please rename it to switch_controller_nas_ip_dynamic. Enable/Disable switch-controller nas-ip dynamic ...
                        choices:
                            - 'disable'
                            - 'enable'
                    source-ip-interface:
                        type: raw
                        description: (list) Deprecated, please rename it to source_ip_interface. Source interface for communication with the RADIUS server.
            h3c-compatibility:
                type: str
                description: Deprecated, please rename it to h3c_compatibility. Enable/disable compatibility with the H3C, a mechanism that performs se...
                choices:
                    - 'disable'
                    - 'enable'
            name:
                type: str
                description: RADIUS server entry name.
                required: true
            nas-ip:
                type: str
                description: Deprecated, please rename it to nas_ip. IP address used to communicate with the RADIUS server and used as NAS-IP-Address a...
            password-encoding:
                type: str
                description: Deprecated, please rename it to password_encoding. Password encoding.
                choices:
                    - 'ISO-8859-1'
                    - 'auto'
            password-renewal:
                type: str
                description: Deprecated, please rename it to password_renewal. Enable/disable password renewal.
                choices:
                    - 'disable'
                    - 'enable'
            radius-coa:
                type: str
                description: Deprecated, please rename it to radius_coa. Enable to allow a mechanism to change the attributes of an authentication, aut...
                choices:
                    - 'disable'
                    - 'enable'
            radius-port:
                type: int
                description: Deprecated, please rename it to radius_port. RADIUS service port number.
            rsso:
                type: str
                description: Enable/disable RADIUS based single sign on feature.
                choices:
                    - 'disable'
                    - 'enable'
            rsso-context-timeout:
                type: int
                description: Deprecated, please rename it to rsso_context_timeout. Time in seconds before the logged out user is removed from the user ...
            rsso-endpoint-attribute:
                type: str
                description: Deprecated, please rename it to rsso_endpoint_attribute. RADIUS attributes used to extract the user end point identifer fr...
                choices:
                    - 'User-Name'
                    - 'User-Password'
                    - 'CHAP-Password'
                    - 'NAS-IP-Address'
                    - 'NAS-Port'
                    - 'Service-Type'
                    - 'Framed-Protocol'
                    - 'Framed-IP-Address'
                    - 'Framed-IP-Netmask'
                    - 'Framed-Routing'
                    - 'Filter-Id'
                    - 'Framed-MTU'
                    - 'Framed-Compression'
                    - 'Login-IP-Host'
                    - 'Login-Service'
                    - 'Login-TCP-Port'
                    - 'Reply-Message'
                    - 'Callback-Number'
                    - 'Callback-Id'
                    - 'Framed-Route'
                    - 'Framed-IPX-Network'
                    - 'State'
                    - 'Class'
                    - 'Session-Timeout'
                    - 'Idle-Timeout'
                    - 'Termination-Action'
                    - 'Called-Station-Id'
                    - 'Calling-Station-Id'
                    - 'NAS-Identifier'
                    - 'Proxy-State'
                    - 'Login-LAT-Service'
                    - 'Login-LAT-Node'
                    - 'Login-LAT-Group'
                    - 'Framed-AppleTalk-Link'
                    - 'Framed-AppleTalk-Network'
                    - 'Framed-AppleTalk-Zone'
                    - 'Acct-Status-Type'
                    - 'Acct-Delay-Time'
                    - 'Acct-Input-Octets'
                    - 'Acct-Output-Octets'
                    - 'Acct-Session-Id'
                    - 'Acct-Authentic'
                    - 'Acct-Session-Time'
                    - 'Acct-Input-Packets'
                    - 'Acct-Output-Packets'
                    - 'Acct-Terminate-Cause'
                    - 'Acct-Multi-Session-Id'
                    - 'Acct-Link-Count'
                    - 'CHAP-Challenge'
                    - 'NAS-Port-Type'
                    - 'Port-Limit'
                    - 'Login-LAT-Port'
            rsso-endpoint-block-attribute:
                type: str
                description: Deprecated, please rename it to rsso_endpoint_block_attribute. RADIUS attributes used to block a user.
                choices:
                    - 'User-Name'
                    - 'User-Password'
                    - 'CHAP-Password'
                    - 'NAS-IP-Address'
                    - 'NAS-Port'
                    - 'Service-Type'
                    - 'Framed-Protocol'
                    - 'Framed-IP-Address'
                    - 'Framed-IP-Netmask'
                    - 'Framed-Routing'
                    - 'Filter-Id'
                    - 'Framed-MTU'
                    - 'Framed-Compression'
                    - 'Login-IP-Host'
                    - 'Login-Service'
                    - 'Login-TCP-Port'
                    - 'Reply-Message'
                    - 'Callback-Number'
                    - 'Callback-Id'
                    - 'Framed-Route'
                    - 'Framed-IPX-Network'
                    - 'State'
                    - 'Class'
                    - 'Session-Timeout'
                    - 'Idle-Timeout'
                    - 'Termination-Action'
                    - 'Called-Station-Id'
                    - 'Calling-Station-Id'
                    - 'NAS-Identifier'
                    - 'Proxy-State'
                    - 'Login-LAT-Service'
                    - 'Login-LAT-Node'
                    - 'Login-LAT-Group'
                    - 'Framed-AppleTalk-Link'
                    - 'Framed-AppleTalk-Network'
                    - 'Framed-AppleTalk-Zone'
                    - 'Acct-Status-Type'
                    - 'Acct-Delay-Time'
                    - 'Acct-Input-Octets'
                    - 'Acct-Output-Octets'
                    - 'Acct-Session-Id'
                    - 'Acct-Authentic'
                    - 'Acct-Session-Time'
                    - 'Acct-Input-Packets'
                    - 'Acct-Output-Packets'
                    - 'Acct-Terminate-Cause'
                    - 'Acct-Multi-Session-Id'
                    - 'Acct-Link-Count'
                    - 'CHAP-Challenge'
                    - 'NAS-Port-Type'
                    - 'Port-Limit'
                    - 'Login-LAT-Port'
            rsso-ep-one-ip-only:
                type: str
                description: Deprecated, please rename it to rsso_ep_one_ip_only. Enable/disable the replacement of old IP addresses with new ones for ...
                choices:
                    - 'disable'
                    - 'enable'
            rsso-flush-ip-session:
                type: str
                description: Deprecated, please rename it to rsso_flush_ip_session. Enable/disable flushing user IP sessions on RADIUS accounting Stop ...
                choices:
                    - 'disable'
                    - 'enable'
            rsso-log-flags:
                type: list
                elements: str
                description: Deprecated, please rename it to rsso_log_flags. Events to log.
                choices:
                    - 'none'
                    - 'protocol-error'
                    - 'profile-missing'
                    - 'context-missing'
                    - 'accounting-stop-missed'
                    - 'accounting-event'
                    - 'radiusd-other'
                    - 'endpoint-block'
            rsso-log-period:
                type: int
                description: Deprecated, please rename it to rsso_log_period. Time interval in seconds that group event log messages will be generated ...
            rsso-radius-response:
                type: str
                description: Deprecated, please rename it to rsso_radius_response. Enable/disable sending RADIUS response packets after receiving Start...
                choices:
                    - 'disable'
                    - 'enable'
            rsso-radius-server-port:
                type: int
                description: Deprecated, please rename it to rsso_radius_server_port. UDP port to listen on for RADIUS Start and Stop records.
            rsso-secret:
                type: raw
                description: (list) Deprecated, please rename it to rsso_secret. RADIUS secret used by the RADIUS accounting server.
            rsso-validate-request-secret:
                type: str
                description: Deprecated, please rename it to rsso_validate_request_secret. Enable/disable validating the RADIUS request shared secret i...
                choices:
                    - 'disable'
                    - 'enable'
            secondary-secret:
                type: raw
                description: (list) Deprecated, please rename it to secondary_secret. Secret key to access the secondary server.
            secondary-server:
                type: str
                description: Deprecated, please rename it to secondary_server. No description
            secret:
                type: raw
                description: (list) Pre-shared secret key used to access the primary RADIUS server.
            server:
                type: str
                description: Primary RADIUS server CN domain name or IP address.
            source-ip:
                type: str
                description: Deprecated, please rename it to source_ip. Source IP address for communications to the RADIUS server.
            sso-attribute:
                type: str
                description: Deprecated, please rename it to sso_attribute. RADIUS attribute that contains the profile group name to be extracted from ...
                choices:
                    - 'User-Name'
                    - 'User-Password'
                    - 'CHAP-Password'
                    - 'NAS-IP-Address'
                    - 'NAS-Port'
                    - 'Service-Type'
                    - 'Framed-Protocol'
                    - 'Framed-IP-Address'
                    - 'Framed-IP-Netmask'
                    - 'Framed-Routing'
                    - 'Filter-Id'
                    - 'Framed-MTU'
                    - 'Framed-Compression'
                    - 'Login-IP-Host'
                    - 'Login-Service'
                    - 'Login-TCP-Port'
                    - 'Reply-Message'
                    - 'Callback-Number'
                    - 'Callback-Id'
                    - 'Framed-Route'
                    - 'Framed-IPX-Network'
                    - 'State'
                    - 'Class'
                    - 'Session-Timeout'
                    - 'Idle-Timeout'
                    - 'Termination-Action'
                    - 'Called-Station-Id'
                    - 'Calling-Station-Id'
                    - 'NAS-Identifier'
                    - 'Proxy-State'
                    - 'Login-LAT-Service'
                    - 'Login-LAT-Node'
                    - 'Login-LAT-Group'
                    - 'Framed-AppleTalk-Link'
                    - 'Framed-AppleTalk-Network'
                    - 'Framed-AppleTalk-Zone'
                    - 'Acct-Status-Type'
                    - 'Acct-Delay-Time'
                    - 'Acct-Input-Octets'
                    - 'Acct-Output-Octets'
                    - 'Acct-Session-Id'
                    - 'Acct-Authentic'
                    - 'Acct-Session-Time'
                    - 'Acct-Input-Packets'
                    - 'Acct-Output-Packets'
                    - 'Acct-Terminate-Cause'
                    - 'Acct-Multi-Session-Id'
                    - 'Acct-Link-Count'
                    - 'CHAP-Challenge'
                    - 'NAS-Port-Type'
                    - 'Port-Limit'
                    - 'Login-LAT-Port'
            sso-attribute-key:
                type: str
                description: Deprecated, please rename it to sso_attribute_key. Key prefix for SSO group value in the SSO attribute.
            sso-attribute-value-override:
                type: str
                description: Deprecated, please rename it to sso_attribute_value_override. Enable/disable override old attribute value with new value f...
                choices:
                    - 'disable'
                    - 'enable'
            tertiary-secret:
                type: raw
                description: (list) Deprecated, please rename it to tertiary_secret. Secret key to access the tertiary server.
            tertiary-server:
                type: str
                description: Deprecated, please rename it to tertiary_server. No description
            timeout:
                type: int
                description: Time in seconds between re-sending authentication requests.
            use-management-vdom:
                type: str
                description: Deprecated, please rename it to use_management_vdom. Enable/disable using management VDOM to send requests.
                choices:
                    - 'disable'
                    - 'enable'
            username-case-sensitive:
                type: str
                description: Deprecated, please rename it to username_case_sensitive. Enable/disable case sensitive user names.
                choices:
                    - 'disable'
                    - 'enable'
            interface:
                type: str
                description: Specify outgoing interface to reach server.
            interface-select-method:
                type: str
                description: Deprecated, please rename it to interface_select_method. Specify how to select outgoing interface to reach server.
                choices:
                    - 'auto'
                    - 'sdwan'
                    - 'specify'
            group-override-attr-type:
                type: str
                description: Deprecated, please rename it to group_override_attr_type. RADIUS attribute type to override user group information.
                choices:
                    - 'filter-Id'
                    - 'class'
            switch-controller-acct-fast-framedip-detect:
                type: int
                description: Deprecated, please rename it to switch_controller_acct_fast_framedip_detect. Switch controller accounting message Framed-I...
            switch-controller-service-type:
                type: list
                elements: str
                description: Deprecated, please rename it to switch_controller_service_type. RADIUS service type.
                choices:
                    - 'login'
                    - 'framed'
                    - 'callback-login'
                    - 'callback-framed'
                    - 'outbound'
                    - 'administrative'
                    - 'nas-prompt'
                    - 'authenticate-only'
                    - 'callback-nas-prompt'
                    - 'call-check'
                    - 'callback-administrative'
            delimiter:
                type: str
                description: Configure delimiter to be used for separating profile group names in the SSO attribute
                choices:
                    - 'plus'
                    - 'comma'
            mac-case:
                type: str
                description: Deprecated, please rename it to mac_case. MAC authentication case
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
            nas-id:
                type: str
                description: Deprecated, please rename it to nas_id. Custom NAS identifier.
            nas-id-type:
                type: str
                description: Deprecated, please rename it to nas_id_type. NAS identifier type configuration
                choices:
                    - 'legacy'
                    - 'custom'
                    - 'hostname'
            ca-cert:
                type: str
                description: Deprecated, please rename it to ca_cert. CA of server to trust under TLS.
            client-cert:
                type: str
                description: Deprecated, please rename it to client_cert. Client certificate to use under TLS.
            server-identity-check:
                type: str
                description: Deprecated, please rename it to server_identity_check. Enable/disable RADIUS server identity check
                choices:
                    - 'disable'
                    - 'enable'
            status-ttl:
                type: int
                description: Deprecated, please rename it to status_ttl. Time for which server reachability is cached so that when a server is unreacha...
            tls-min-proto-version:
                type: str
                description: Deprecated, please rename it to tls_min_proto_version. Minimum supported protocol version for TLS connections
                choices:
                    - 'default'
                    - 'TLSv1'
                    - 'TLSv1-1'
                    - 'TLSv1-2'
                    - 'SSLv3'
                    - 'TLSv1-3'
            transport-protocol:
                type: str
                description: Deprecated, please rename it to transport_protocol. Transport protocol to be used
                choices:
                    - 'udp'
                    - 'tcp'
                    - 'tls'
            account-key-cert-field:
                type: str
                description: Deprecated, please rename it to account_key_cert_field. Define subject identity field in certificate for user access right...
                choices:
                    - 'othername'
                    - 'rfc822name'
                    - 'dnsname'
                    - 'cn'
            account-key-processing:
                type: str
                description: Deprecated, please rename it to account_key_processing. Account key processing operation.
                choices:
                    - 'same'
                    - 'strip'
            call-station-id-type:
                type: str
                description: Deprecated, please rename it to call_station_id_type. Calling & Called station identifier type configuration
                choices:
                    - 'legacy'
                    - 'IP'
                    - 'MAC'
            switch-controller-nas-ip-dynamic:
                type: str
                description: Deprecated, please rename it to switch_controller_nas_ip_dynamic. Enable/Disable switch-controller nas-ip dynamic to dynam...
                choices:
                    - 'disable'
                    - 'enable'
            source-ip-interface:
                type: raw
                description: (list) Deprecated, please rename it to source_ip_interface. Source interface for communication with the RADIUS server.
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
    - name: Configure RADIUS server entries.
      fortinet.fortimanager.fmgr_user_radius:
        bypass_validation: false
        adom: ansible
        state: present
        user_radius:
          name: ansible-test-radius
          server: ansible
          timeout: 200

- name: Gathering fortimanager facts
  hosts: fortimanagers
  gather_facts: false
  connection: httpapi
  vars:
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_httpapi_port: 443
  tasks:
    - name: Retrieve all the RADIUS server entries
      fortinet.fortimanager.fmgr_fact:
        facts:
          selector: "user_radius"
          params:
            adom: "ansible"
            radius: "your_value"
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
        '/pm/config/adom/{adom}/obj/user/radius',
        '/pm/config/global/obj/user/radius'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/user/radius/{radius}',
        '/pm/config/global/obj/user/radius/{radius}'
    ]

    url_params = ['adom']
    module_primary_key = 'name'
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'user_radius': {
            'type': 'dict',
            'v_range': [['6.0.0', '']],
            'options': {
                'accounting-server': {
                    'type': 'list',
                    'options': {
                        'id': {'type': 'int'},
                        'port': {'type': 'int'},
                        'secret': {'no_log': True, 'type': 'raw'},
                        'server': {'type': 'str'},
                        'source-ip': {'type': 'str'},
                        'status': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'interface': {'v_range': [['6.2.5', '6.2.12'], ['6.4.1', '']], 'type': 'str'},
                        'interface-select-method': {
                            'v_range': [['6.2.5', '6.2.12'], ['6.4.1', '']],
                            'choices': ['auto', 'sdwan', 'specify'],
                            'type': 'str'
                        }
                    },
                    'elements': 'dict'
                },
                'acct-all-servers': {'choices': ['disable', 'enable'], 'type': 'str'},
                'acct-interim-interval': {'type': 'int'},
                'all-usergroup': {'choices': ['disable', 'enable'], 'type': 'str'},
                'auth-type': {'choices': ['pap', 'chap', 'ms_chap', 'ms_chap_v2', 'auto'], 'type': 'str'},
                'class': {'type': 'raw'},
                'dynamic_mapping': {
                    'type': 'list',
                    'options': {
                        '_scope': {'type': 'list', 'options': {'name': {'type': 'str'}, 'vdom': {'type': 'str'}}, 'elements': 'dict'},
                        'acct-all-servers': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'acct-interim-interval': {'type': 'int'},
                        'all-usergroup': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'auth-type': {'choices': ['pap', 'chap', 'ms_chap', 'ms_chap_v2', 'auto'], 'type': 'str'},
                        'class': {'type': 'raw'},
                        'dp-carrier-endpoint-attribute': {
                            'choices': [
                                'User-Name', 'User-Password', 'CHAP-Password', 'NAS-IP-Address', 'NAS-Port', 'Service-Type', 'Framed-Protocol',
                                'Framed-IP-Address', 'Framed-IP-Netmask', 'Framed-Routing', 'Filter-Id', 'Framed-MTU', 'Framed-Compression',
                                'Login-IP-Host', 'Login-Service', 'Login-TCP-Port', 'Reply-Message', 'Callback-Number', 'Callback-Id', 'Framed-Route',
                                'Framed-IPX-Network', 'State', 'Class', 'Vendor-Specific', 'Session-Timeout', 'Idle-Timeout', 'Termination-Action',
                                'Called-Station-Id', 'Calling-Station-Id', 'NAS-Identifier', 'Proxy-State', 'Login-LAT-Service', 'Login-LAT-Node',
                                'Login-LAT-Group', 'Framed-AppleTalk-Link', 'Framed-AppleTalk-Network', 'Framed-AppleTalk-Zone', 'Acct-Status-Type',
                                'Acct-Delay-Time', 'Acct-Input-Octets', 'Acct-Output-Octets', 'Acct-Session-Id', 'Acct-Authentic', 'Acct-Session-Time',
                                'Acct-Input-Packets', 'Acct-Output-Packets', 'Acct-Terminate-Cause', 'Acct-Multi-Session-Id', 'Acct-Link-Count',
                                'CHAP-Challenge', 'NAS-Port-Type', 'Port-Limit', 'Login-LAT-Port'
                            ],
                            'type': 'str'
                        },
                        'dp-carrier-endpoint-block-attribute': {
                            'choices': [
                                'User-Name', 'User-Password', 'CHAP-Password', 'NAS-IP-Address', 'NAS-Port', 'Service-Type', 'Framed-Protocol',
                                'Framed-IP-Address', 'Framed-IP-Netmask', 'Framed-Routing', 'Filter-Id', 'Framed-MTU', 'Framed-Compression',
                                'Login-IP-Host', 'Login-Service', 'Login-TCP-Port', 'Reply-Message', 'Callback-Number', 'Callback-Id', 'Framed-Route',
                                'Framed-IPX-Network', 'State', 'Class', 'Vendor-Specific', 'Session-Timeout', 'Idle-Timeout', 'Termination-Action',
                                'Called-Station-Id', 'Calling-Station-Id', 'NAS-Identifier', 'Proxy-State', 'Login-LAT-Service', 'Login-LAT-Node',
                                'Login-LAT-Group', 'Framed-AppleTalk-Link', 'Framed-AppleTalk-Network', 'Framed-AppleTalk-Zone', 'Acct-Status-Type',
                                'Acct-Delay-Time', 'Acct-Input-Octets', 'Acct-Output-Octets', 'Acct-Session-Id', 'Acct-Authentic', 'Acct-Session-Time',
                                'Acct-Input-Packets', 'Acct-Output-Packets', 'Acct-Terminate-Cause', 'Acct-Multi-Session-Id', 'Acct-Link-Count',
                                'CHAP-Challenge', 'NAS-Port-Type', 'Port-Limit', 'Login-LAT-Port'
                            ],
                            'type': 'str'
                        },
                        'dp-context-timeout': {'type': 'int'},
                        'dp-flush-ip-session': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'dp-hold-time': {'type': 'int'},
                        'dp-http-header': {'type': 'str'},
                        'dp-http-header-fallback': {'choices': ['ip-header-address', 'default-profile'], 'type': 'str'},
                        'dp-http-header-status': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'dp-http-header-suppress': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'dp-log-dyn_flags': {
                            'type': 'list',
                            'choices': [
                                'none', 'protocol-error', 'profile-missing', 'context-missing', 'accounting-stop-missed', 'accounting-event',
                                'radiusd-other', 'endpoint-block'
                            ],
                            'elements': 'str'
                        },
                        'dp-log-period': {'type': 'int'},
                        'dp-mem-percent': {'type': 'int'},
                        'dp-profile-attribute': {
                            'choices': [
                                'User-Name', 'User-Password', 'CHAP-Password', 'NAS-IP-Address', 'NAS-Port', 'Service-Type', 'Framed-Protocol',
                                'Framed-IP-Address', 'Framed-IP-Netmask', 'Framed-Routing', 'Filter-Id', 'Framed-MTU', 'Framed-Compression',
                                'Login-IP-Host', 'Login-Service', 'Login-TCP-Port', 'Reply-Message', 'Callback-Number', 'Callback-Id', 'Framed-Route',
                                'Framed-IPX-Network', 'State', 'Class', 'Vendor-Specific', 'Session-Timeout', 'Idle-Timeout', 'Termination-Action',
                                'Called-Station-Id', 'Calling-Station-Id', 'NAS-Identifier', 'Proxy-State', 'Login-LAT-Service', 'Login-LAT-Node',
                                'Login-LAT-Group', 'Framed-AppleTalk-Link', 'Framed-AppleTalk-Network', 'Framed-AppleTalk-Zone', 'Acct-Status-Type',
                                'Acct-Delay-Time', 'Acct-Input-Octets', 'Acct-Output-Octets', 'Acct-Session-Id', 'Acct-Authentic', 'Acct-Session-Time',
                                'Acct-Input-Packets', 'Acct-Output-Packets', 'Acct-Terminate-Cause', 'Acct-Multi-Session-Id', 'Acct-Link-Count',
                                'CHAP-Challenge', 'NAS-Port-Type', 'Port-Limit', 'Login-LAT-Port'
                            ],
                            'type': 'str'
                        },
                        'dp-profile-attribute-key': {'no_log': True, 'type': 'str'},
                        'dp-radius-response': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'dp-radius-server-port': {'type': 'int'},
                        'dp-secret': {'no_log': True, 'type': 'raw'},
                        'dp-validate-request-secret': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'dynamic-profile': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'endpoint-translation': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'ep-carrier-endpoint-convert-hex': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'ep-carrier-endpoint-header': {'type': 'str'},
                        'ep-carrier-endpoint-header-suppress': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'ep-carrier-endpoint-prefix': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'ep-carrier-endpoint-prefix-range-max': {'type': 'int'},
                        'ep-carrier-endpoint-prefix-range-min': {'type': 'int'},
                        'ep-carrier-endpoint-prefix-string': {'type': 'str'},
                        'ep-carrier-endpoint-source': {'choices': ['http-header', 'cookie'], 'type': 'str'},
                        'ep-ip-header': {'type': 'str'},
                        'ep-ip-header-suppress': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'ep-missing-header-fallback': {'choices': ['session-ip', 'policy-profile'], 'type': 'str'},
                        'ep-profile-query-type': {'choices': ['session-ip', 'extract-ip', 'extract-carrier-endpoint'], 'type': 'str'},
                        'h3c-compatibility': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'nas-ip': {'type': 'str'},
                        'password-encoding': {'choices': ['ISO-8859-1', 'auto'], 'type': 'str'},
                        'password-renewal': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'radius-coa': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'radius-port': {'type': 'int'},
                        'rsso': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'rsso-context-timeout': {'type': 'int'},
                        'rsso-endpoint-attribute': {
                            'choices': [
                                'User-Name', 'User-Password', 'CHAP-Password', 'NAS-IP-Address', 'NAS-Port', 'Service-Type', 'Framed-Protocol',
                                'Framed-IP-Address', 'Framed-IP-Netmask', 'Framed-Routing', 'Filter-Id', 'Framed-MTU', 'Framed-Compression',
                                'Login-IP-Host', 'Login-Service', 'Login-TCP-Port', 'Reply-Message', 'Callback-Number', 'Callback-Id', 'Framed-Route',
                                'Framed-IPX-Network', 'State', 'Class', 'Session-Timeout', 'Idle-Timeout', 'Termination-Action', 'Called-Station-Id',
                                'Calling-Station-Id', 'NAS-Identifier', 'Proxy-State', 'Login-LAT-Service', 'Login-LAT-Node', 'Login-LAT-Group',
                                'Framed-AppleTalk-Link', 'Framed-AppleTalk-Network', 'Framed-AppleTalk-Zone', 'Acct-Status-Type', 'Acct-Delay-Time',
                                'Acct-Input-Octets', 'Acct-Output-Octets', 'Acct-Session-Id', 'Acct-Authentic', 'Acct-Session-Time',
                                'Acct-Input-Packets', 'Acct-Output-Packets', 'Acct-Terminate-Cause', 'Acct-Multi-Session-Id', 'Acct-Link-Count',
                                'CHAP-Challenge', 'NAS-Port-Type', 'Port-Limit', 'Login-LAT-Port'
                            ],
                            'type': 'str'
                        },
                        'rsso-endpoint-block-attribute': {
                            'choices': [
                                'User-Name', 'User-Password', 'CHAP-Password', 'NAS-IP-Address', 'NAS-Port', 'Service-Type', 'Framed-Protocol',
                                'Framed-IP-Address', 'Framed-IP-Netmask', 'Framed-Routing', 'Filter-Id', 'Framed-MTU', 'Framed-Compression',
                                'Login-IP-Host', 'Login-Service', 'Login-TCP-Port', 'Reply-Message', 'Callback-Number', 'Callback-Id', 'Framed-Route',
                                'Framed-IPX-Network', 'State', 'Class', 'Session-Timeout', 'Idle-Timeout', 'Termination-Action', 'Called-Station-Id',
                                'Calling-Station-Id', 'NAS-Identifier', 'Proxy-State', 'Login-LAT-Service', 'Login-LAT-Node', 'Login-LAT-Group',
                                'Framed-AppleTalk-Link', 'Framed-AppleTalk-Network', 'Framed-AppleTalk-Zone', 'Acct-Status-Type', 'Acct-Delay-Time',
                                'Acct-Input-Octets', 'Acct-Output-Octets', 'Acct-Session-Id', 'Acct-Authentic', 'Acct-Session-Time',
                                'Acct-Input-Packets', 'Acct-Output-Packets', 'Acct-Terminate-Cause', 'Acct-Multi-Session-Id', 'Acct-Link-Count',
                                'CHAP-Challenge', 'NAS-Port-Type', 'Port-Limit', 'Login-LAT-Port'
                            ],
                            'type': 'str'
                        },
                        'rsso-ep-one-ip-only': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'rsso-flush-ip-session': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'rsso-log-flags': {
                            'type': 'list',
                            'choices': [
                                'none', 'protocol-error', 'profile-missing', 'context-missing', 'accounting-stop-missed', 'accounting-event',
                                'radiusd-other', 'endpoint-block'
                            ],
                            'elements': 'str'
                        },
                        'rsso-log-period': {'type': 'int'},
                        'rsso-radius-response': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'rsso-radius-server-port': {'type': 'int'},
                        'rsso-secret': {'no_log': True, 'type': 'raw'},
                        'rsso-validate-request-secret': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'secondary-secret': {'no_log': True, 'type': 'raw'},
                        'secondary-server': {'type': 'str'},
                        'secret': {'no_log': True, 'type': 'raw'},
                        'server': {'type': 'str'},
                        'source-ip': {'type': 'str'},
                        'sso-attribute': {
                            'choices': [
                                'User-Name', 'User-Password', 'CHAP-Password', 'NAS-IP-Address', 'NAS-Port', 'Service-Type', 'Framed-Protocol',
                                'Framed-IP-Address', 'Framed-IP-Netmask', 'Framed-Routing', 'Filter-Id', 'Framed-MTU', 'Framed-Compression',
                                'Login-IP-Host', 'Login-Service', 'Login-TCP-Port', 'Reply-Message', 'Callback-Number', 'Callback-Id', 'Framed-Route',
                                'Framed-IPX-Network', 'State', 'Class', 'Session-Timeout', 'Idle-Timeout', 'Termination-Action', 'Called-Station-Id',
                                'Calling-Station-Id', 'NAS-Identifier', 'Proxy-State', 'Login-LAT-Service', 'Login-LAT-Node', 'Login-LAT-Group',
                                'Framed-AppleTalk-Link', 'Framed-AppleTalk-Network', 'Framed-AppleTalk-Zone', 'Acct-Status-Type', 'Acct-Delay-Time',
                                'Acct-Input-Octets', 'Acct-Output-Octets', 'Acct-Session-Id', 'Acct-Authentic', 'Acct-Session-Time',
                                'Acct-Input-Packets', 'Acct-Output-Packets', 'Acct-Terminate-Cause', 'Acct-Multi-Session-Id', 'Acct-Link-Count',
                                'CHAP-Challenge', 'NAS-Port-Type', 'Port-Limit', 'Login-LAT-Port'
                            ],
                            'type': 'str'
                        },
                        'sso-attribute-key': {'no_log': True, 'type': 'str'},
                        'sso-attribute-value-override': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'tertiary-secret': {'no_log': True, 'type': 'raw'},
                        'tertiary-server': {'type': 'str'},
                        'timeout': {'type': 'int'},
                        'use-group-for-profile': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'use-management-vdom': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'username-case-sensitive': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'interface': {'v_range': [['6.2.5', '6.2.12'], ['6.4.1', '']], 'type': 'str'},
                        'interface-select-method': {
                            'v_range': [['6.2.5', '6.2.12'], ['6.4.1', '']],
                            'choices': ['auto', 'sdwan', 'specify'],
                            'type': 'str'
                        },
                        'group-override-attr-type': {'v_range': [['6.4.0', '']], 'choices': ['filter-Id', 'class'], 'type': 'str'},
                        'switch-controller-acct-fast-framedip-detect': {'v_range': [['6.4.0', '']], 'type': 'int'},
                        'accounting-server': {
                            'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']],
                            'type': 'list',
                            'options': {
                                'id': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'int'},
                                'interface': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'str'},
                                'interface-select-method': {
                                    'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']],
                                    'choices': ['auto', 'sdwan', 'specify'],
                                    'type': 'str'
                                },
                                'port': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'int'},
                                'secret': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'no_log': True, 'type': 'raw'},
                                'server': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'str'},
                                'source-ip': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'type': 'str'},
                                'status': {'v_range': [['6.2.6', '6.2.12'], ['6.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'}
                            },
                            'elements': 'dict'
                        },
                        'switch-controller-service-type': {
                            'v_range': [['6.4.2', '']],
                            'type': 'list',
                            'choices': [
                                'login', 'framed', 'callback-login', 'callback-framed', 'outbound', 'administrative', 'nas-prompt', 'authenticate-only',
                                'callback-nas-prompt', 'call-check', 'callback-administrative'
                            ],
                            'elements': 'str'
                        },
                        'delimiter': {'v_range': [['7.2.0', '']], 'choices': ['plus', 'comma'], 'type': 'str'},
                        'mac-case': {'v_range': [['7.2.1', '']], 'choices': ['uppercase', 'lowercase'], 'type': 'str'},
                        'mac-password-delimiter': {'v_range': [['7.2.1', '']], 'choices': ['hyphen', 'single-hyphen', 'colon', 'none'], 'type': 'str'},
                        'mac-username-delimiter': {'v_range': [['7.2.1', '']], 'choices': ['hyphen', 'single-hyphen', 'colon', 'none'], 'type': 'str'},
                        'nas-id': {'v_range': [['7.2.2', '']], 'type': 'str'},
                        'nas-id-type': {'v_range': [['7.2.2', '']], 'choices': ['legacy', 'custom', 'hostname'], 'type': 'str'},
                        'ca-cert': {'v_range': [['7.4.0', '']], 'type': 'str'},
                        'client-cert': {'v_range': [['7.4.0', '']], 'type': 'str'},
                        'server-identity-check': {'v_range': [['7.4.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'status-ttl': {'v_range': [['7.4.0', '']], 'type': 'int'},
                        'tls-min-proto-version': {
                            'v_range': [['7.4.0', '']],
                            'choices': ['default', 'TLSv1', 'TLSv1-1', 'TLSv1-2', 'SSLv3', 'TLSv1-3'],
                            'type': 'str'
                        },
                        'transport-protocol': {'v_range': [['7.4.0', '']], 'choices': ['udp', 'tcp', 'tls'], 'type': 'str'},
                        'account-key-cert-field': {'v_range': [['7.4.1', '']], 'choices': ['othername', 'rfc822name', 'dnsname', 'cn'], 'type': 'str'},
                        'account-key-processing': {'v_range': [['7.4.1', '']], 'choices': ['same', 'strip'], 'type': 'str'},
                        'call-station-id-type': {'v_range': [['7.4.1', '']], 'choices': ['legacy', 'IP', 'MAC'], 'type': 'str'},
                        'switch-controller-nas-ip-dynamic': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'source-ip-interface': {'v_range': [['7.6.0', '']], 'type': 'raw'}
                    },
                    'elements': 'dict'
                },
                'h3c-compatibility': {'choices': ['disable', 'enable'], 'type': 'str'},
                'name': {'required': True, 'type': 'str'},
                'nas-ip': {'type': 'str'},
                'password-encoding': {'choices': ['ISO-8859-1', 'auto'], 'type': 'str'},
                'password-renewal': {'choices': ['disable', 'enable'], 'type': 'str'},
                'radius-coa': {'choices': ['disable', 'enable'], 'type': 'str'},
                'radius-port': {'type': 'int'},
                'rsso': {'choices': ['disable', 'enable'], 'type': 'str'},
                'rsso-context-timeout': {'type': 'int'},
                'rsso-endpoint-attribute': {
                    'choices': [
                        'User-Name', 'User-Password', 'CHAP-Password', 'NAS-IP-Address', 'NAS-Port', 'Service-Type', 'Framed-Protocol',
                        'Framed-IP-Address', 'Framed-IP-Netmask', 'Framed-Routing', 'Filter-Id', 'Framed-MTU', 'Framed-Compression', 'Login-IP-Host',
                        'Login-Service', 'Login-TCP-Port', 'Reply-Message', 'Callback-Number', 'Callback-Id', 'Framed-Route', 'Framed-IPX-Network',
                        'State', 'Class', 'Session-Timeout', 'Idle-Timeout', 'Termination-Action', 'Called-Station-Id', 'Calling-Station-Id',
                        'NAS-Identifier', 'Proxy-State', 'Login-LAT-Service', 'Login-LAT-Node', 'Login-LAT-Group', 'Framed-AppleTalk-Link',
                        'Framed-AppleTalk-Network', 'Framed-AppleTalk-Zone', 'Acct-Status-Type', 'Acct-Delay-Time', 'Acct-Input-Octets',
                        'Acct-Output-Octets', 'Acct-Session-Id', 'Acct-Authentic', 'Acct-Session-Time', 'Acct-Input-Packets', 'Acct-Output-Packets',
                        'Acct-Terminate-Cause', 'Acct-Multi-Session-Id', 'Acct-Link-Count', 'CHAP-Challenge', 'NAS-Port-Type', 'Port-Limit',
                        'Login-LAT-Port'
                    ],
                    'type': 'str'
                },
                'rsso-endpoint-block-attribute': {
                    'choices': [
                        'User-Name', 'User-Password', 'CHAP-Password', 'NAS-IP-Address', 'NAS-Port', 'Service-Type', 'Framed-Protocol',
                        'Framed-IP-Address', 'Framed-IP-Netmask', 'Framed-Routing', 'Filter-Id', 'Framed-MTU', 'Framed-Compression', 'Login-IP-Host',
                        'Login-Service', 'Login-TCP-Port', 'Reply-Message', 'Callback-Number', 'Callback-Id', 'Framed-Route', 'Framed-IPX-Network',
                        'State', 'Class', 'Session-Timeout', 'Idle-Timeout', 'Termination-Action', 'Called-Station-Id', 'Calling-Station-Id',
                        'NAS-Identifier', 'Proxy-State', 'Login-LAT-Service', 'Login-LAT-Node', 'Login-LAT-Group', 'Framed-AppleTalk-Link',
                        'Framed-AppleTalk-Network', 'Framed-AppleTalk-Zone', 'Acct-Status-Type', 'Acct-Delay-Time', 'Acct-Input-Octets',
                        'Acct-Output-Octets', 'Acct-Session-Id', 'Acct-Authentic', 'Acct-Session-Time', 'Acct-Input-Packets', 'Acct-Output-Packets',
                        'Acct-Terminate-Cause', 'Acct-Multi-Session-Id', 'Acct-Link-Count', 'CHAP-Challenge', 'NAS-Port-Type', 'Port-Limit',
                        'Login-LAT-Port'
                    ],
                    'type': 'str'
                },
                'rsso-ep-one-ip-only': {'choices': ['disable', 'enable'], 'type': 'str'},
                'rsso-flush-ip-session': {'choices': ['disable', 'enable'], 'type': 'str'},
                'rsso-log-flags': {
                    'type': 'list',
                    'choices': [
                        'none', 'protocol-error', 'profile-missing', 'context-missing', 'accounting-stop-missed', 'accounting-event', 'radiusd-other',
                        'endpoint-block'
                    ],
                    'elements': 'str'
                },
                'rsso-log-period': {'type': 'int'},
                'rsso-radius-response': {'choices': ['disable', 'enable'], 'type': 'str'},
                'rsso-radius-server-port': {'type': 'int'},
                'rsso-secret': {'no_log': True, 'type': 'raw'},
                'rsso-validate-request-secret': {'choices': ['disable', 'enable'], 'type': 'str'},
                'secondary-secret': {'no_log': True, 'type': 'raw'},
                'secondary-server': {'type': 'str'},
                'secret': {'no_log': True, 'type': 'raw'},
                'server': {'type': 'str'},
                'source-ip': {'type': 'str'},
                'sso-attribute': {
                    'choices': [
                        'User-Name', 'User-Password', 'CHAP-Password', 'NAS-IP-Address', 'NAS-Port', 'Service-Type', 'Framed-Protocol',
                        'Framed-IP-Address', 'Framed-IP-Netmask', 'Framed-Routing', 'Filter-Id', 'Framed-MTU', 'Framed-Compression', 'Login-IP-Host',
                        'Login-Service', 'Login-TCP-Port', 'Reply-Message', 'Callback-Number', 'Callback-Id', 'Framed-Route', 'Framed-IPX-Network',
                        'State', 'Class', 'Session-Timeout', 'Idle-Timeout', 'Termination-Action', 'Called-Station-Id', 'Calling-Station-Id',
                        'NAS-Identifier', 'Proxy-State', 'Login-LAT-Service', 'Login-LAT-Node', 'Login-LAT-Group', 'Framed-AppleTalk-Link',
                        'Framed-AppleTalk-Network', 'Framed-AppleTalk-Zone', 'Acct-Status-Type', 'Acct-Delay-Time', 'Acct-Input-Octets',
                        'Acct-Output-Octets', 'Acct-Session-Id', 'Acct-Authentic', 'Acct-Session-Time', 'Acct-Input-Packets', 'Acct-Output-Packets',
                        'Acct-Terminate-Cause', 'Acct-Multi-Session-Id', 'Acct-Link-Count', 'CHAP-Challenge', 'NAS-Port-Type', 'Port-Limit',
                        'Login-LAT-Port'
                    ],
                    'type': 'str'
                },
                'sso-attribute-key': {'no_log': True, 'type': 'str'},
                'sso-attribute-value-override': {'choices': ['disable', 'enable'], 'type': 'str'},
                'tertiary-secret': {'no_log': True, 'type': 'raw'},
                'tertiary-server': {'type': 'str'},
                'timeout': {'type': 'int'},
                'use-management-vdom': {'choices': ['disable', 'enable'], 'type': 'str'},
                'username-case-sensitive': {'choices': ['disable', 'enable'], 'type': 'str'},
                'interface': {'v_range': [['6.2.5', '6.2.12'], ['6.4.1', '']], 'type': 'str'},
                'interface-select-method': {'v_range': [['6.2.5', '6.2.12'], ['6.4.1', '']], 'choices': ['auto', 'sdwan', 'specify'], 'type': 'str'},
                'group-override-attr-type': {'v_range': [['6.4.0', '']], 'choices': ['filter-Id', 'class'], 'type': 'str'},
                'switch-controller-acct-fast-framedip-detect': {'v_range': [['6.4.0', '']], 'type': 'int'},
                'switch-controller-service-type': {
                    'v_range': [['6.4.2', '']],
                    'type': 'list',
                    'choices': [
                        'login', 'framed', 'callback-login', 'callback-framed', 'outbound', 'administrative', 'nas-prompt', 'authenticate-only',
                        'callback-nas-prompt', 'call-check', 'callback-administrative'
                    ],
                    'elements': 'str'
                },
                'delimiter': {'v_range': [['7.2.0', '']], 'choices': ['plus', 'comma'], 'type': 'str'},
                'mac-case': {'v_range': [['7.2.1', '']], 'choices': ['uppercase', 'lowercase'], 'type': 'str'},
                'mac-password-delimiter': {'v_range': [['7.2.1', '']], 'choices': ['hyphen', 'single-hyphen', 'colon', 'none'], 'type': 'str'},
                'mac-username-delimiter': {'v_range': [['7.2.1', '']], 'choices': ['hyphen', 'single-hyphen', 'colon', 'none'], 'type': 'str'},
                'nas-id': {'v_range': [['7.2.2', '']], 'type': 'str'},
                'nas-id-type': {'v_range': [['7.2.2', '']], 'choices': ['legacy', 'custom', 'hostname'], 'type': 'str'},
                'ca-cert': {'v_range': [['7.4.0', '']], 'type': 'str'},
                'client-cert': {'v_range': [['7.4.0', '']], 'type': 'str'},
                'server-identity-check': {'v_range': [['7.4.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'status-ttl': {'v_range': [['7.4.0', '']], 'type': 'int'},
                'tls-min-proto-version': {
                    'v_range': [['7.4.0', '']],
                    'choices': ['default', 'TLSv1', 'TLSv1-1', 'TLSv1-2', 'SSLv3', 'TLSv1-3'],
                    'type': 'str'
                },
                'transport-protocol': {'v_range': [['7.4.0', '']], 'choices': ['udp', 'tcp', 'tls'], 'type': 'str'},
                'account-key-cert-field': {'v_range': [['7.4.1', '']], 'choices': ['othername', 'rfc822name', 'dnsname', 'cn'], 'type': 'str'},
                'account-key-processing': {'v_range': [['7.4.1', '']], 'choices': ['same', 'strip'], 'type': 'str'},
                'call-station-id-type': {'v_range': [['7.4.1', '']], 'choices': ['legacy', 'IP', 'MAC'], 'type': 'str'},
                'switch-controller-nas-ip-dynamic': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'source-ip-interface': {'v_range': [['7.6.0', '']], 'type': 'raw'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('full crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'user_radius'),
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
