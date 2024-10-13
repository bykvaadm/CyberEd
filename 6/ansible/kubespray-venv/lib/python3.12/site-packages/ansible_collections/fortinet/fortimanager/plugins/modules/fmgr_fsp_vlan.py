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
module: fmgr_fsp_vlan
short_description: FortiSwitch VLAN template.
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
    fsp_vlan:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            _dhcp-status:
                type: str
                description: Deprecated, please rename it to _dhcp_status. Dhcp status.
                choices:
                    - 'disable'
                    - 'enable'
            auth:
                type: str
                description: Auth.
                choices:
                    - 'radius'
                    - 'usergroup'
            color:
                type: int
                description: Color.
            comments:
                type: str
                description: Comments.
            dynamic_mapping:
                type: list
                elements: dict
                description: Dynamic mapping.
                suboptions:
                    _dhcp-status:
                        type: str
                        description: Deprecated, please rename it to _dhcp_status. Dhcp status.
                        choices:
                            - 'disable'
                            - 'enable'
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
                    dhcp-server:
                        type: dict
                        description: Deprecated, please rename it to dhcp_server. Dhcp server.
                        suboptions:
                            auto-configuration:
                                type: str
                                description: Deprecated, please rename it to auto_configuration. Enable/disable auto configuration.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            auto-managed-status:
                                type: str
                                description: Deprecated, please rename it to auto_managed_status. Enable/disable use of this DHCP server once this inte...
                                choices:
                                    - 'disable'
                                    - 'enable'
                            conflicted-ip-timeout:
                                type: int
                                description: Deprecated, please rename it to conflicted_ip_timeout. Time in seconds to wait after a conflicted IP addre...
                            ddns-auth:
                                type: str
                                description: Deprecated, please rename it to ddns_auth. DDNS authentication mode.
                                choices:
                                    - 'disable'
                                    - 'tsig'
                            ddns-key:
                                type: raw
                                description: (list or str) Deprecated, please rename it to ddns_key. DDNS update key
                            ddns-keyname:
                                type: str
                                description: Deprecated, please rename it to ddns_keyname. DDNS update key name.
                            ddns-server-ip:
                                type: str
                                description: Deprecated, please rename it to ddns_server_ip. DDNS server IP.
                            ddns-ttl:
                                type: int
                                description: Deprecated, please rename it to ddns_ttl. TTL.
                            ddns-update:
                                type: str
                                description: Deprecated, please rename it to ddns_update. Enable/disable DDNS update for DHCP.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            ddns-update-override:
                                type: str
                                description: Deprecated, please rename it to ddns_update_override. Enable/disable DDNS update override for DHCP.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            ddns-zone:
                                type: str
                                description: Deprecated, please rename it to ddns_zone. Zone of your domain name
                            default-gateway:
                                type: str
                                description: Deprecated, please rename it to default_gateway. Default gateway IP address assigned by the DHCP server.
                            dhcp-settings-from-fortiipam:
                                type: str
                                description: Deprecated, please rename it to dhcp_settings_from_fortiipam. Enable/disable populating of DHCP server set...
                                choices:
                                    - 'disable'
                                    - 'enable'
                            dns-server1:
                                type: str
                                description: Deprecated, please rename it to dns_server1. DNS server 1.
                            dns-server2:
                                type: str
                                description: Deprecated, please rename it to dns_server2. DNS server 2.
                            dns-server3:
                                type: str
                                description: Deprecated, please rename it to dns_server3. DNS server 3.
                            dns-server4:
                                type: str
                                description: Deprecated, please rename it to dns_server4. DNS server 4.
                            dns-service:
                                type: str
                                description: Deprecated, please rename it to dns_service. Options for assigning DNS servers to DHCP clients.
                                choices:
                                    - 'default'
                                    - 'specify'
                                    - 'local'
                            domain:
                                type: str
                                description: Domain name suffix for the IP addresses that the DHCP server assigns to clients.
                            enable:
                                type: str
                                description: Enable.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            exclude-range:
                                type: list
                                elements: dict
                                description: Deprecated, please rename it to exclude_range. Exclude range.
                                suboptions:
                                    end-ip:
                                        type: str
                                        description: Deprecated, please rename it to end_ip. End of IP range.
                                    id:
                                        type: int
                                        description: ID.
                                    start-ip:
                                        type: str
                                        description: Deprecated, please rename it to start_ip. Start of IP range.
                                    vci-match:
                                        type: str
                                        description: Deprecated, please rename it to vci_match. Enable/disable vendor class identifier
                                        choices:
                                            - 'disable'
                                            - 'enable'
                                    vci-string:
                                        type: raw
                                        description: (list) Deprecated, please rename it to vci_string. One or more VCI strings in quotes separated by ...
                                    lease-time:
                                        type: int
                                        description: Deprecated, please rename it to lease_time. Lease time in seconds, 0 means default lease time.
                                    uci-match:
                                        type: str
                                        description: Deprecated, please rename it to uci_match. Enable/disable user class identifier
                                        choices:
                                            - 'disable'
                                            - 'enable'
                                    uci-string:
                                        type: raw
                                        description: (list) Deprecated, please rename it to uci_string. One or more UCI strings in quotes separated by ...
                            filename:
                                type: str
                                description: Name of the boot file on the TFTP server.
                            forticlient-on-net-status:
                                type: str
                                description: Deprecated, please rename it to forticlient_on_net_status. Enable/disable FortiClient-On-Net service for t...
                                choices:
                                    - 'disable'
                                    - 'enable'
                            id:
                                type: int
                                description: ID.
                            ip-mode:
                                type: str
                                description: Deprecated, please rename it to ip_mode. Method used to assign client IP.
                                choices:
                                    - 'range'
                                    - 'usrgrp'
                            ip-range:
                                type: list
                                elements: dict
                                description: Deprecated, please rename it to ip_range. Ip range.
                                suboptions:
                                    end-ip:
                                        type: str
                                        description: Deprecated, please rename it to end_ip. End of IP range.
                                    id:
                                        type: int
                                        description: ID.
                                    start-ip:
                                        type: str
                                        description: Deprecated, please rename it to start_ip. Start of IP range.
                                    vci-match:
                                        type: str
                                        description: Deprecated, please rename it to vci_match. Enable/disable vendor class identifier
                                        choices:
                                            - 'disable'
                                            - 'enable'
                                    vci-string:
                                        type: raw
                                        description: (list) Deprecated, please rename it to vci_string. One or more VCI strings in quotes separated by ...
                                    lease-time:
                                        type: int
                                        description: Deprecated, please rename it to lease_time. Lease time in seconds, 0 means default lease time.
                                    uci-match:
                                        type: str
                                        description: Deprecated, please rename it to uci_match. Enable/disable user class identifier
                                        choices:
                                            - 'disable'
                                            - 'enable'
                                    uci-string:
                                        type: raw
                                        description: (list) Deprecated, please rename it to uci_string. One or more UCI strings in quotes separated by ...
                            ipsec-lease-hold:
                                type: int
                                description: Deprecated, please rename it to ipsec_lease_hold. DHCP over IPsec leases expire this many seconds after tu...
                            lease-time:
                                type: int
                                description: Deprecated, please rename it to lease_time. Lease time in seconds, 0 means unlimited.
                            mac-acl-default-action:
                                type: str
                                description: Deprecated, please rename it to mac_acl_default_action. MAC access control default action
                                choices:
                                    - 'assign'
                                    - 'block'
                            netmask:
                                type: str
                                description: Netmask assigned by the DHCP server.
                            next-server:
                                type: str
                                description: Deprecated, please rename it to next_server. IP address of a server
                            ntp-server1:
                                type: str
                                description: Deprecated, please rename it to ntp_server1. NTP server 1.
                            ntp-server2:
                                type: str
                                description: Deprecated, please rename it to ntp_server2. NTP server 2.
                            ntp-server3:
                                type: str
                                description: Deprecated, please rename it to ntp_server3. NTP server 3.
                            ntp-service:
                                type: str
                                description: Deprecated, please rename it to ntp_service. Options for assigning Network Time Protocol
                                choices:
                                    - 'default'
                                    - 'specify'
                                    - 'local'
                            option1:
                                type: raw
                                description: (list) Option1.
                            option2:
                                type: raw
                                description: (list) Option2.
                            option3:
                                type: raw
                                description: (list) Option3.
                            option4:
                                type: str
                                description: Option4.
                            option5:
                                type: str
                                description: Option5.
                            option6:
                                type: str
                                description: Option6.
                            options:
                                type: list
                                elements: dict
                                description: Options.
                                suboptions:
                                    code:
                                        type: int
                                        description: DHCP option code.
                                    id:
                                        type: int
                                        description: ID.
                                    ip:
                                        type: raw
                                        description: (list) DHCP option IPs.
                                    type:
                                        type: str
                                        description: DHCP option type.
                                        choices:
                                            - 'hex'
                                            - 'string'
                                            - 'ip'
                                            - 'fqdn'
                                    value:
                                        type: str
                                        description: DHCP option value.
                                    vci-match:
                                        type: str
                                        description: Deprecated, please rename it to vci_match. Enable/disable vendor class identifier
                                        choices:
                                            - 'disable'
                                            - 'enable'
                                    vci-string:
                                        type: raw
                                        description: (list) Deprecated, please rename it to vci_string. One or more VCI strings in quotes separated by ...
                                    uci-match:
                                        type: str
                                        description: Deprecated, please rename it to uci_match. Enable/disable user class identifier
                                        choices:
                                            - 'disable'
                                            - 'enable'
                                    uci-string:
                                        type: raw
                                        description: (list) Deprecated, please rename it to uci_string. One or more UCI strings in quotes separated by ...
                            reserved-address:
                                type: list
                                elements: dict
                                description: Deprecated, please rename it to reserved_address. Reserved address.
                                suboptions:
                                    action:
                                        type: str
                                        description: Options for the DHCP server to configure the client with the reserved MAC address.
                                        choices:
                                            - 'assign'
                                            - 'block'
                                            - 'reserved'
                                    circuit-id:
                                        type: str
                                        description: Deprecated, please rename it to circuit_id. Option 82 circuit-ID of the client that will get the r...
                                    circuit-id-type:
                                        type: str
                                        description: Deprecated, please rename it to circuit_id_type. DHCP option type.
                                        choices:
                                            - 'hex'
                                            - 'string'
                                    description:
                                        type: str
                                        description: Description.
                                    id:
                                        type: int
                                        description: ID.
                                    ip:
                                        type: str
                                        description: IP address to be reserved for the MAC address.
                                    mac:
                                        type: str
                                        description: MAC address of the client that will get the reserved IP address.
                                    remote-id:
                                        type: str
                                        description: Deprecated, please rename it to remote_id. Option 82 remote-ID of the client that will get the res...
                                    remote-id-type:
                                        type: str
                                        description: Deprecated, please rename it to remote_id_type. DHCP option type.
                                        choices:
                                            - 'hex'
                                            - 'string'
                                    type:
                                        type: str
                                        description: DHCP reserved-address type.
                                        choices:
                                            - 'mac'
                                            - 'option82'
                            server-type:
                                type: str
                                description: Deprecated, please rename it to server_type. DHCP server can be a normal DHCP server or an IPsec DHCP server.
                                choices:
                                    - 'regular'
                                    - 'ipsec'
                            status:
                                type: str
                                description: Enable/disable this DHCP configuration.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            tftp-server:
                                type: raw
                                description: (list) Deprecated, please rename it to tftp_server. One or more hostnames or IP addresses of the TFTP serv...
                            timezone:
                                type: str
                                description: Select the time zone to be assigned to DHCP clients.
                                choices:
                                    - '00'
                                    - '01'
                                    - '02'
                                    - '03'
                                    - '04'
                                    - '05'
                                    - '06'
                                    - '07'
                                    - '08'
                                    - '09'
                                    - '10'
                                    - '11'
                                    - '12'
                                    - '13'
                                    - '14'
                                    - '15'
                                    - '16'
                                    - '17'
                                    - '18'
                                    - '19'
                                    - '20'
                                    - '21'
                                    - '22'
                                    - '23'
                                    - '24'
                                    - '25'
                                    - '26'
                                    - '27'
                                    - '28'
                                    - '29'
                                    - '30'
                                    - '31'
                                    - '32'
                                    - '33'
                                    - '34'
                                    - '35'
                                    - '36'
                                    - '37'
                                    - '38'
                                    - '39'
                                    - '40'
                                    - '41'
                                    - '42'
                                    - '43'
                                    - '44'
                                    - '45'
                                    - '46'
                                    - '47'
                                    - '48'
                                    - '49'
                                    - '50'
                                    - '51'
                                    - '52'
                                    - '53'
                                    - '54'
                                    - '55'
                                    - '56'
                                    - '57'
                                    - '58'
                                    - '59'
                                    - '60'
                                    - '61'
                                    - '62'
                                    - '63'
                                    - '64'
                                    - '65'
                                    - '66'
                                    - '67'
                                    - '68'
                                    - '69'
                                    - '70'
                                    - '71'
                                    - '72'
                                    - '73'
                                    - '74'
                                    - '75'
                                    - '76'
                                    - '77'
                                    - '78'
                                    - '79'
                                    - '80'
                                    - '81'
                                    - '82'
                                    - '83'
                                    - '84'
                                    - '85'
                                    - '86'
                                    - '87'
                            timezone-option:
                                type: str
                                description: Deprecated, please rename it to timezone_option. Options for the DHCP server to set the clients time zone.
                                choices:
                                    - 'disable'
                                    - 'default'
                                    - 'specify'
                            vci-match:
                                type: str
                                description: Deprecated, please rename it to vci_match. Enable/disable vendor class identifier
                                choices:
                                    - 'disable'
                                    - 'enable'
                            vci-string:
                                type: raw
                                description: (list) Deprecated, please rename it to vci_string. One or more VCI strings in quotes separated by spaces.
                            wifi-ac-service:
                                type: str
                                description: Deprecated, please rename it to wifi_ac_service. Options for assigning WiFi Access Controllers to DHCP clients
                                choices:
                                    - 'specify'
                                    - 'local'
                            wifi-ac1:
                                type: str
                                description: Deprecated, please rename it to wifi_ac1. WiFi Access Controller 1 IP address
                            wifi-ac2:
                                type: str
                                description: Deprecated, please rename it to wifi_ac2. WiFi Access Controller 2 IP address
                            wifi-ac3:
                                type: str
                                description: Deprecated, please rename it to wifi_ac3. WiFi Access Controller 3 IP address
                            wins-server1:
                                type: str
                                description: Deprecated, please rename it to wins_server1. WINS server 1.
                            wins-server2:
                                type: str
                                description: Deprecated, please rename it to wins_server2. WINS server 2.
                            relay-agent:
                                type: str
                                description: Deprecated, please rename it to relay_agent. Relay agent IP.
                            shared-subnet:
                                type: str
                                description: Deprecated, please rename it to shared_subnet. Enable/disable shared subnet.
                                choices:
                                    - 'disable'
                                    - 'enable'
                    interface:
                        type: dict
                        description: Interface.
                        suboptions:
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
                            ip:
                                type: str
                                description: Ip.
                            ipv6:
                                type: dict
                                description: Ipv6.
                                suboptions:
                                    autoconf:
                                        type: str
                                        description: Enable/disable address auto config.
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
                                        description: Deprecated, please rename it to dhcp6_information_request. Enable/disable DHCPv6 information request.
                                        choices:
                                            - 'disable'
                                            - 'enable'
                                    dhcp6-prefix-delegation:
                                        type: str
                                        description: Deprecated, please rename it to dhcp6_prefix_delegation. Enable/disable DHCPv6 prefix delegation.
                                        choices:
                                            - 'disable'
                                            - 'enable'
                                    dhcp6-prefix-hint:
                                        type: str
                                        description: Deprecated, please rename it to dhcp6_prefix_hint. DHCPv6 prefix that will be used as a hint to th...
                                    dhcp6-prefix-hint-plt:
                                        type: int
                                        description: Deprecated, please rename it to dhcp6_prefix_hint_plt. DHCPv6 prefix hint preferred life time
                                    dhcp6-prefix-hint-vlt:
                                        type: int
                                        description: Deprecated, please rename it to dhcp6_prefix_hint_vlt. DHCPv6 prefix hint valid life time
                                    dhcp6-relay-ip:
                                        type: str
                                        description: Deprecated, please rename it to dhcp6_relay_ip. DHCPv6 relay IP address.
                                    dhcp6-relay-service:
                                        type: str
                                        description: Deprecated, please rename it to dhcp6_relay_service. Enable/disable DHCPv6 relay.
                                        choices:
                                            - 'disable'
                                            - 'enable'
                                    dhcp6-relay-type:
                                        type: str
                                        description: Deprecated, please rename it to dhcp6_relay_type. DHCPv6 relay type.
                                        choices:
                                            - 'regular'
                                    icmp6-send-redirect:
                                        type: str
                                        description: Deprecated, please rename it to icmp6_send_redirect. Enable/disable sending of ICMPv6 redirects.
                                        choices:
                                            - 'disable'
                                            - 'enable'
                                    interface-identifier:
                                        type: str
                                        description: Deprecated, please rename it to interface_identifier. IPv6 interface identifier.
                                    ip6-address:
                                        type: str
                                        description: Deprecated, please rename it to ip6_address. Primary IPv6 address prefix, syntax
                                    ip6-allowaccess:
                                        type: list
                                        elements: str
                                        description: Deprecated, please rename it to ip6_allowaccess. Allow management access to the interface.
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
                                        description: Deprecated, please rename it to ip6_default_life. Default life
                                    ip6-delegated-prefix-list:
                                        type: list
                                        elements: dict
                                        description: Deprecated, please rename it to ip6_delegated_prefix_list. Ip6 delegated prefix list.
                                        suboptions:
                                            autonomous-flag:
                                                type: str
                                                description: Deprecated, please rename it to autonomous_flag. Enable/disable the autonomous flag.
                                                choices:
                                                    - 'disable'
                                                    - 'enable'
                                            onlink-flag:
                                                type: str
                                                description: Deprecated, please rename it to onlink_flag. Enable/disable the onlink flag.
                                                choices:
                                                    - 'disable'
                                                    - 'enable'
                                            prefix-id:
                                                type: int
                                                description: Deprecated, please rename it to prefix_id. Prefix ID.
                                            rdnss:
                                                type: raw
                                                description: (list) Recursive DNS server option.
                                            rdnss-service:
                                                type: str
                                                description: Deprecated, please rename it to rdnss_service. Recursive DNS service option.
                                                choices:
                                                    - 'delegated'
                                                    - 'default'
                                                    - 'specify'
                                            subnet:
                                                type: str
                                                description: Add subnet ID to routing prefix.
                                            upstream-interface:
                                                type: str
                                                description: Deprecated, please rename it to upstream_interface. Name of the interface that provides de...
                                            delegated-prefix-iaid:
                                                type: int
                                                description: Deprecated, please rename it to delegated_prefix_iaid. IAID of obtained delegated-prefix f...
                                    ip6-dns-server-override:
                                        type: str
                                        description: Deprecated, please rename it to ip6_dns_server_override. Enable/disable using the DNS server acqui...
                                        choices:
                                            - 'disable'
                                            - 'enable'
                                    ip6-extra-addr:
                                        type: list
                                        elements: dict
                                        description: Deprecated, please rename it to ip6_extra_addr. Ip6 extra addr.
                                        suboptions:
                                            prefix:
                                                type: str
                                                description: IPv6 address prefix.
                                    ip6-hop-limit:
                                        type: int
                                        description: Deprecated, please rename it to ip6_hop_limit. Hop limit
                                    ip6-link-mtu:
                                        type: int
                                        description: Deprecated, please rename it to ip6_link_mtu. IPv6 link MTU.
                                    ip6-manage-flag:
                                        type: str
                                        description: Deprecated, please rename it to ip6_manage_flag. Enable/disable the managed flag.
                                        choices:
                                            - 'disable'
                                            - 'enable'
                                    ip6-max-interval:
                                        type: int
                                        description: Deprecated, please rename it to ip6_max_interval. IPv6 maximum interval
                                    ip6-min-interval:
                                        type: int
                                        description: Deprecated, please rename it to ip6_min_interval. IPv6 minimum interval
                                    ip6-mode:
                                        type: str
                                        description: Deprecated, please rename it to ip6_mode. Addressing mode
                                        choices:
                                            - 'static'
                                            - 'dhcp'
                                            - 'pppoe'
                                            - 'delegated'
                                    ip6-other-flag:
                                        type: str
                                        description: Deprecated, please rename it to ip6_other_flag. Enable/disable the other IPv6 flag.
                                        choices:
                                            - 'disable'
                                            - 'enable'
                                    ip6-prefix-list:
                                        type: list
                                        elements: dict
                                        description: Deprecated, please rename it to ip6_prefix_list. Ip6 prefix list.
                                        suboptions:
                                            autonomous-flag:
                                                type: str
                                                description: Deprecated, please rename it to autonomous_flag. Enable/disable the autonomous flag.
                                                choices:
                                                    - 'disable'
                                                    - 'enable'
                                            dnssl:
                                                type: raw
                                                description: (list) DNS search list option.
                                            onlink-flag:
                                                type: str
                                                description: Deprecated, please rename it to onlink_flag. Enable/disable the onlink flag.
                                                choices:
                                                    - 'disable'
                                                    - 'enable'
                                            preferred-life-time:
                                                type: int
                                                description: Deprecated, please rename it to preferred_life_time. Preferred life time
                                            prefix:
                                                type: str
                                                description: IPv6 prefix.
                                            rdnss:
                                                type: raw
                                                description: (list) Recursive DNS server option.
                                            valid-life-time:
                                                type: int
                                                description: Deprecated, please rename it to valid_life_time. Valid life time
                                    ip6-reachable-time:
                                        type: int
                                        description: Deprecated, please rename it to ip6_reachable_time. IPv6 reachable time
                                    ip6-retrans-time:
                                        type: int
                                        description: Deprecated, please rename it to ip6_retrans_time. IPv6 retransmit time
                                    ip6-send-adv:
                                        type: str
                                        description: Deprecated, please rename it to ip6_send_adv. Enable/disable sending advertisements about the inte...
                                        choices:
                                            - 'disable'
                                            - 'enable'
                                    ip6-subnet:
                                        type: str
                                        description: Deprecated, please rename it to ip6_subnet. Subnet to routing prefix, syntax
                                    ip6-upstream-interface:
                                        type: str
                                        description: Deprecated, please rename it to ip6_upstream_interface. Interface name providing delegated informa...
                                    nd-cert:
                                        type: str
                                        description: Deprecated, please rename it to nd_cert. Neighbor discovery certificate.
                                    nd-cga-modifier:
                                        type: str
                                        description: Deprecated, please rename it to nd_cga_modifier. Neighbor discovery CGA modifier.
                                    nd-mode:
                                        type: str
                                        description: Deprecated, please rename it to nd_mode. Neighbor discovery mode.
                                        choices:
                                            - 'basic'
                                            - 'SEND-compatible'
                                    nd-security-level:
                                        type: int
                                        description: Deprecated, please rename it to nd_security_level. Neighbor discovery security level
                                    nd-timestamp-delta:
                                        type: int
                                        description: Deprecated, please rename it to nd_timestamp_delta. Neighbor discovery timestamp delta value
                                    nd-timestamp-fuzz:
                                        type: int
                                        description: Deprecated, please rename it to nd_timestamp_fuzz. Neighbor discovery timestamp fuzz factor
                                    unique-autoconf-addr:
                                        type: str
                                        description: Deprecated, please rename it to unique_autoconf_addr. Enable/disable unique auto config address.
                                        choices:
                                            - 'disable'
                                            - 'enable'
                                    vrip6_link_local:
                                        type: str
                                        description: Link-local IPv6 address of virtual router.
                                    vrrp-virtual-mac6:
                                        type: str
                                        description: Deprecated, please rename it to vrrp_virtual_mac6. Enable/disable virtual MAC for VRRP.
                                        choices:
                                            - 'disable'
                                            - 'enable'
                                    vrrp6:
                                        type: list
                                        elements: dict
                                        description: Vrrp6.
                                        suboptions:
                                            accept-mode:
                                                type: str
                                                description: Deprecated, please rename it to accept_mode. Enable/disable accept mode.
                                                choices:
                                                    - 'disable'
                                                    - 'enable'
                                            adv-interval:
                                                type: int
                                                description: Deprecated, please rename it to adv_interval. Advertisement interval
                                            preempt:
                                                type: str
                                                description: Enable/disable preempt mode.
                                                choices:
                                                    - 'disable'
                                                    - 'enable'
                                            priority:
                                                type: int
                                                description: Priority of the virtual router
                                            start-time:
                                                type: int
                                                description: Deprecated, please rename it to start_time. Startup time
                                            status:
                                                type: str
                                                description: Enable/disable VRRP.
                                                choices:
                                                    - 'disable'
                                                    - 'enable'
                                            vrdst6:
                                                type: str
                                                description: Monitor the route to this destination.
                                            vrgrp:
                                                type: int
                                                description: VRRP group ID
                                            vrid:
                                                type: int
                                                description: Virtual router identifier
                                            vrip6:
                                                type: str
                                                description: IPv6 address of the virtual router.
                                            ignore-default-route:
                                                type: str
                                                description: Deprecated, please rename it to ignore_default_route. Enable/disable ignoring of default r...
                                                choices:
                                                    - 'disable'
                                                    - 'enable'
                                            vrdst-priority:
                                                type: int
                                                description: Deprecated, please rename it to vrdst_priority. Priority of the virtual router when the vi...
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
                                        description: Deprecated, please rename it to ip6_delegated_prefix_iaid. IAID of obtained delegated-prefix from ...
                                    dhcp6-relay-source-interface:
                                        type: str
                                        description: Deprecated, please rename it to dhcp6_relay_source_interface. Enable/disable use of address on thi...
                                        choices:
                                            - 'disable'
                                            - 'enable'
                                    dhcp6-relay-interface-id:
                                        type: str
                                        description: Deprecated, please rename it to dhcp6_relay_interface_id. DHCP6 relay interface ID.
                                    dhcp6-relay-source-ip:
                                        type: str
                                        description: Deprecated, please rename it to dhcp6_relay_source_ip. IPv6 address used by the DHCP6 relay as its...
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
                                        description: Management access settings for the secondary IP address.
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
                                        description: Protocols used to detect the server.
                                        choices:
                                            - 'ping'
                                            - 'tcp-echo'
                                            - 'udp-echo'
                                    detectserver:
                                        type: str
                                        description: Gateways ping server for this IP.
                                    gwdetect:
                                        type: str
                                        description: Enable/disable detect gateway alive for first.
                                        choices:
                                            - 'disable'
                                            - 'enable'
                                    ha-priority:
                                        type: int
                                        description: Deprecated, please rename it to ha_priority. HA election priority for the PING server.
                                    id:
                                        type: int
                                        description: ID.
                                    ip:
                                        type: str
                                        description: Secondary IP address of the interface.
                                    ping-serv-status:
                                        type: int
                                        description: Deprecated, please rename it to ping_serv_status. Ping serv status.
                                    seq:
                                        type: int
                                        description: Seq.
                                    secip-relay-ip:
                                        type: str
                                        description: Deprecated, please rename it to secip_relay_ip. DHCP relay IP address.
                            vlanid:
                                type: int
                                description: Vlanid.
                            dhcp-relay-interface-select-method:
                                type: str
                                description: Deprecated, please rename it to dhcp_relay_interface_select_method. Dhcp relay interface select method.
                                choices:
                                    - 'auto'
                                    - 'sdwan'
                                    - 'specify'
                            vrrp:
                                type: list
                                elements: dict
                                description: Vrrp.
                                suboptions:
                                    accept-mode:
                                        type: str
                                        description: Deprecated, please rename it to accept_mode. Enable/disable accept mode.
                                        choices:
                                            - 'disable'
                                            - 'enable'
                                    adv-interval:
                                        type: int
                                        description: Deprecated, please rename it to adv_interval. Advertisement interval
                                    ignore-default-route:
                                        type: str
                                        description: Deprecated, please rename it to ignore_default_route. Enable/disable ignoring of default route whe...
                                        choices:
                                            - 'disable'
                                            - 'enable'
                                    preempt:
                                        type: str
                                        description: Enable/disable preempt mode.
                                        choices:
                                            - 'disable'
                                            - 'enable'
                                    priority:
                                        type: int
                                        description: Priority of the virtual router
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
                                    start-time:
                                        type: int
                                        description: Deprecated, please rename it to start_time. Startup time
                                    status:
                                        type: str
                                        description: Enable/disable this VRRP configuration.
                                        choices:
                                            - 'disable'
                                            - 'enable'
                                    version:
                                        type: str
                                        description: VRRP version.
                                        choices:
                                            - '2'
                                            - '3'
                                    vrdst:
                                        type: raw
                                        description: (list) Monitor the route to this destination.
                                    vrdst-priority:
                                        type: int
                                        description: Deprecated, please rename it to vrdst_priority. Priority of the virtual router when the virtual ro...
                                    vrgrp:
                                        type: int
                                        description: VRRP group ID
                                    vrid:
                                        type: int
                                        description: Virtual router identifier
                                    vrip:
                                        type: str
                                        description: IP address of the virtual router.
            name:
                type: str
                description: Name.
                required: true
            portal-message-override-group:
                type: str
                description: Deprecated, please rename it to portal_message_override_group. Portal message override group.
            radius-server:
                type: str
                description: Deprecated, please rename it to radius_server. Radius server.
            security:
                type: str
                description: Security.
                choices:
                    - 'open'
                    - 'captive-portal'
                    - '8021x'
            selected-usergroups:
                type: str
                description: Deprecated, please rename it to selected_usergroups. Selected usergroups.
            usergroup:
                type: str
                description: Usergroup.
            vdom:
                type: str
                description: Vdom.
            vlanid:
                type: int
                description: Vlanid.
            dhcp-server:
                type: dict
                description: Deprecated, please rename it to dhcp_server. Dhcp server.
                suboptions:
                    auto-configuration:
                        type: str
                        description: Deprecated, please rename it to auto_configuration. Enable/disable auto configuration.
                        choices:
                            - 'disable'
                            - 'enable'
                    auto-managed-status:
                        type: str
                        description: Deprecated, please rename it to auto_managed_status. Enable/disable use of this DHCP server once this interface ha...
                        choices:
                            - 'disable'
                            - 'enable'
                    conflicted-ip-timeout:
                        type: int
                        description: Deprecated, please rename it to conflicted_ip_timeout. Time in seconds to wait after a conflicted IP address is re...
                    ddns-auth:
                        type: str
                        description: Deprecated, please rename it to ddns_auth. DDNS authentication mode.
                        choices:
                            - 'disable'
                            - 'tsig'
                    ddns-key:
                        type: raw
                        description: (list or str) Deprecated, please rename it to ddns_key. DDNS update key
                    ddns-keyname:
                        type: str
                        description: Deprecated, please rename it to ddns_keyname. DDNS update key name.
                    ddns-server-ip:
                        type: str
                        description: Deprecated, please rename it to ddns_server_ip. DDNS server IP.
                    ddns-ttl:
                        type: int
                        description: Deprecated, please rename it to ddns_ttl. TTL.
                    ddns-update:
                        type: str
                        description: Deprecated, please rename it to ddns_update. Enable/disable DDNS update for DHCP.
                        choices:
                            - 'disable'
                            - 'enable'
                    ddns-update-override:
                        type: str
                        description: Deprecated, please rename it to ddns_update_override. Enable/disable DDNS update override for DHCP.
                        choices:
                            - 'disable'
                            - 'enable'
                    ddns-zone:
                        type: str
                        description: Deprecated, please rename it to ddns_zone. Zone of your domain name
                    default-gateway:
                        type: str
                        description: Deprecated, please rename it to default_gateway. Default gateway IP address assigned by the DHCP server.
                    dhcp-settings-from-fortiipam:
                        type: str
                        description: Deprecated, please rename it to dhcp_settings_from_fortiipam. Enable/disable populating of DHCP server settings fr...
                        choices:
                            - 'disable'
                            - 'enable'
                    dns-server1:
                        type: str
                        description: Deprecated, please rename it to dns_server1. DNS server 1.
                    dns-server2:
                        type: str
                        description: Deprecated, please rename it to dns_server2. DNS server 2.
                    dns-server3:
                        type: str
                        description: Deprecated, please rename it to dns_server3. DNS server 3.
                    dns-server4:
                        type: str
                        description: Deprecated, please rename it to dns_server4. DNS server 4.
                    dns-service:
                        type: str
                        description: Deprecated, please rename it to dns_service. Options for assigning DNS servers to DHCP clients.
                        choices:
                            - 'default'
                            - 'specify'
                            - 'local'
                    domain:
                        type: str
                        description: Domain name suffix for the IP addresses that the DHCP server assigns to clients.
                    enable:
                        type: str
                        description: Enable.
                        choices:
                            - 'disable'
                            - 'enable'
                    exclude-range:
                        type: list
                        elements: dict
                        description: Deprecated, please rename it to exclude_range. Exclude range.
                        suboptions:
                            end-ip:
                                type: str
                                description: Deprecated, please rename it to end_ip. End of IP range.
                            id:
                                type: int
                                description: ID.
                            start-ip:
                                type: str
                                description: Deprecated, please rename it to start_ip. Start of IP range.
                            vci-match:
                                type: str
                                description: Deprecated, please rename it to vci_match. Enable/disable vendor class identifier
                                choices:
                                    - 'disable'
                                    - 'enable'
                            vci-string:
                                type: raw
                                description: (list) Deprecated, please rename it to vci_string. One or more VCI strings in quotes separated by spaces.
                            lease-time:
                                type: int
                                description: Deprecated, please rename it to lease_time. Lease time in seconds, 0 means default lease time.
                            uci-match:
                                type: str
                                description: Deprecated, please rename it to uci_match. Enable/disable user class identifier
                                choices:
                                    - 'disable'
                                    - 'enable'
                            uci-string:
                                type: raw
                                description: (list) Deprecated, please rename it to uci_string. One or more UCI strings in quotes separated by spaces.
                    filename:
                        type: str
                        description: Name of the boot file on the TFTP server.
                    forticlient-on-net-status:
                        type: str
                        description: Deprecated, please rename it to forticlient_on_net_status. Enable/disable FortiClient-On-Net service for this DHCP...
                        choices:
                            - 'disable'
                            - 'enable'
                    id:
                        type: int
                        description: ID.
                    ip-mode:
                        type: str
                        description: Deprecated, please rename it to ip_mode. Method used to assign client IP.
                        choices:
                            - 'range'
                            - 'usrgrp'
                    ip-range:
                        type: list
                        elements: dict
                        description: Deprecated, please rename it to ip_range. Ip range.
                        suboptions:
                            end-ip:
                                type: str
                                description: Deprecated, please rename it to end_ip. End of IP range.
                            id:
                                type: int
                                description: ID.
                            start-ip:
                                type: str
                                description: Deprecated, please rename it to start_ip. Start of IP range.
                            vci-match:
                                type: str
                                description: Deprecated, please rename it to vci_match. Enable/disable vendor class identifier
                                choices:
                                    - 'disable'
                                    - 'enable'
                            vci-string:
                                type: raw
                                description: (list) Deprecated, please rename it to vci_string. One or more VCI strings in quotes separated by spaces.
                            lease-time:
                                type: int
                                description: Deprecated, please rename it to lease_time. Lease time in seconds, 0 means default lease time.
                            uci-match:
                                type: str
                                description: Deprecated, please rename it to uci_match. Enable/disable user class identifier
                                choices:
                                    - 'disable'
                                    - 'enable'
                            uci-string:
                                type: raw
                                description: (list) Deprecated, please rename it to uci_string. One or more UCI strings in quotes separated by spaces.
                    ipsec-lease-hold:
                        type: int
                        description: Deprecated, please rename it to ipsec_lease_hold. DHCP over IPsec leases expire this many seconds after tunnel down
                    lease-time:
                        type: int
                        description: Deprecated, please rename it to lease_time. Lease time in seconds, 0 means unlimited.
                    mac-acl-default-action:
                        type: str
                        description: Deprecated, please rename it to mac_acl_default_action. MAC access control default action
                        choices:
                            - 'assign'
                            - 'block'
                    netmask:
                        type: str
                        description: Netmask assigned by the DHCP server.
                    next-server:
                        type: str
                        description: Deprecated, please rename it to next_server. IP address of a server
                    ntp-server1:
                        type: str
                        description: Deprecated, please rename it to ntp_server1. NTP server 1.
                    ntp-server2:
                        type: str
                        description: Deprecated, please rename it to ntp_server2. NTP server 2.
                    ntp-server3:
                        type: str
                        description: Deprecated, please rename it to ntp_server3. NTP server 3.
                    ntp-service:
                        type: str
                        description: Deprecated, please rename it to ntp_service. Options for assigning Network Time Protocol
                        choices:
                            - 'default'
                            - 'specify'
                            - 'local'
                    option1:
                        type: raw
                        description: (list) Option1.
                    option2:
                        type: raw
                        description: (list) Option2.
                    option3:
                        type: raw
                        description: (list) Option3.
                    option4:
                        type: str
                        description: Option4.
                    option5:
                        type: str
                        description: Option5.
                    option6:
                        type: str
                        description: Option6.
                    options:
                        type: list
                        elements: dict
                        description: Options.
                        suboptions:
                            code:
                                type: int
                                description: DHCP option code.
                            id:
                                type: int
                                description: ID.
                            ip:
                                type: raw
                                description: (list) DHCP option IPs.
                            type:
                                type: str
                                description: DHCP option type.
                                choices:
                                    - 'hex'
                                    - 'string'
                                    - 'ip'
                                    - 'fqdn'
                            value:
                                type: str
                                description: DHCP option value.
                            vci-match:
                                type: str
                                description: Deprecated, please rename it to vci_match. Enable/disable vendor class identifier
                                choices:
                                    - 'disable'
                                    - 'enable'
                            vci-string:
                                type: raw
                                description: (list) Deprecated, please rename it to vci_string. One or more VCI strings in quotes separated by spaces.
                            uci-match:
                                type: str
                                description: Deprecated, please rename it to uci_match. Enable/disable user class identifier
                                choices:
                                    - 'disable'
                                    - 'enable'
                            uci-string:
                                type: raw
                                description: (list) Deprecated, please rename it to uci_string. One or more UCI strings in quotes separated by spaces.
                    reserved-address:
                        type: list
                        elements: dict
                        description: Deprecated, please rename it to reserved_address. Reserved address.
                        suboptions:
                            action:
                                type: str
                                description: Options for the DHCP server to configure the client with the reserved MAC address.
                                choices:
                                    - 'assign'
                                    - 'block'
                                    - 'reserved'
                            circuit-id:
                                type: str
                                description: Deprecated, please rename it to circuit_id. Option 82 circuit-ID of the client that will get the reserved ...
                            circuit-id-type:
                                type: str
                                description: Deprecated, please rename it to circuit_id_type. DHCP option type.
                                choices:
                                    - 'hex'
                                    - 'string'
                            description:
                                type: str
                                description: Description.
                            id:
                                type: int
                                description: ID.
                            ip:
                                type: str
                                description: IP address to be reserved for the MAC address.
                            mac:
                                type: str
                                description: MAC address of the client that will get the reserved IP address.
                            remote-id:
                                type: str
                                description: Deprecated, please rename it to remote_id. Option 82 remote-ID of the client that will get the reserved IP...
                            remote-id-type:
                                type: str
                                description: Deprecated, please rename it to remote_id_type. DHCP option type.
                                choices:
                                    - 'hex'
                                    - 'string'
                            type:
                                type: str
                                description: DHCP reserved-address type.
                                choices:
                                    - 'mac'
                                    - 'option82'
                    server-type:
                        type: str
                        description: Deprecated, please rename it to server_type. DHCP server can be a normal DHCP server or an IPsec DHCP server.
                        choices:
                            - 'regular'
                            - 'ipsec'
                    status:
                        type: str
                        description: Enable/disable this DHCP configuration.
                        choices:
                            - 'disable'
                            - 'enable'
                    tftp-server:
                        type: raw
                        description: (list) Deprecated, please rename it to tftp_server. One or more hostnames or IP addresses of the TFTP servers in q...
                    timezone:
                        type: str
                        description: Select the time zone to be assigned to DHCP clients.
                        choices:
                            - '00'
                            - '01'
                            - '02'
                            - '03'
                            - '04'
                            - '05'
                            - '06'
                            - '07'
                            - '08'
                            - '09'
                            - '10'
                            - '11'
                            - '12'
                            - '13'
                            - '14'
                            - '15'
                            - '16'
                            - '17'
                            - '18'
                            - '19'
                            - '20'
                            - '21'
                            - '22'
                            - '23'
                            - '24'
                            - '25'
                            - '26'
                            - '27'
                            - '28'
                            - '29'
                            - '30'
                            - '31'
                            - '32'
                            - '33'
                            - '34'
                            - '35'
                            - '36'
                            - '37'
                            - '38'
                            - '39'
                            - '40'
                            - '41'
                            - '42'
                            - '43'
                            - '44'
                            - '45'
                            - '46'
                            - '47'
                            - '48'
                            - '49'
                            - '50'
                            - '51'
                            - '52'
                            - '53'
                            - '54'
                            - '55'
                            - '56'
                            - '57'
                            - '58'
                            - '59'
                            - '60'
                            - '61'
                            - '62'
                            - '63'
                            - '64'
                            - '65'
                            - '66'
                            - '67'
                            - '68'
                            - '69'
                            - '70'
                            - '71'
                            - '72'
                            - '73'
                            - '74'
                            - '75'
                            - '76'
                            - '77'
                            - '78'
                            - '79'
                            - '80'
                            - '81'
                            - '82'
                            - '83'
                            - '84'
                            - '85'
                            - '86'
                            - '87'
                    timezone-option:
                        type: str
                        description: Deprecated, please rename it to timezone_option. Options for the DHCP server to set the clients time zone.
                        choices:
                            - 'disable'
                            - 'default'
                            - 'specify'
                    vci-match:
                        type: str
                        description: Deprecated, please rename it to vci_match. Enable/disable vendor class identifier
                        choices:
                            - 'disable'
                            - 'enable'
                    vci-string:
                        type: raw
                        description: (list) Deprecated, please rename it to vci_string. One or more VCI strings in quotes separated by spaces.
                    wifi-ac-service:
                        type: str
                        description: Deprecated, please rename it to wifi_ac_service. Options for assigning WiFi Access Controllers to DHCP clients
                        choices:
                            - 'specify'
                            - 'local'
                    wifi-ac1:
                        type: str
                        description: Deprecated, please rename it to wifi_ac1. WiFi Access Controller 1 IP address
                    wifi-ac2:
                        type: str
                        description: Deprecated, please rename it to wifi_ac2. WiFi Access Controller 2 IP address
                    wifi-ac3:
                        type: str
                        description: Deprecated, please rename it to wifi_ac3. WiFi Access Controller 3 IP address
                    wins-server1:
                        type: str
                        description: Deprecated, please rename it to wins_server1. WINS server 1.
                    wins-server2:
                        type: str
                        description: Deprecated, please rename it to wins_server2. WINS server 2.
                    relay-agent:
                        type: str
                        description: Deprecated, please rename it to relay_agent. Relay agent IP.
                    shared-subnet:
                        type: str
                        description: Deprecated, please rename it to shared_subnet. Enable/disable shared subnet.
                        choices:
                            - 'disable'
                            - 'enable'
            interface:
                type: dict
                description: Interface.
                suboptions:
                    ac-name:
                        type: str
                        description: Deprecated, please rename it to ac_name. PPPoE server name.
                    aggregate:
                        type: str
                        description: Aggregate.
                    algorithm:
                        type: str
                        description: Frame distribution algorithm.
                        choices:
                            - 'L2'
                            - 'L3'
                            - 'L4'
                            - 'LB'
                            - 'Source-MAC'
                    alias:
                        type: str
                        description: Alias will be displayed with the interface name to make it easier to distinguish.
                    allowaccess:
                        type: list
                        elements: str
                        description: Permitted types of management access to this interface.
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
                        description: Deprecated, please rename it to ap_discover. Enable/disable automatic registration of unknown FortiAP devices.
                        choices:
                            - 'disable'
                            - 'enable'
                    arpforward:
                        type: str
                        description: Enable/disable ARP forwarding.
                        choices:
                            - 'disable'
                            - 'enable'
                    atm-protocol:
                        type: str
                        description: Deprecated, please rename it to atm_protocol. ATM protocol.
                        choices:
                            - 'none'
                            - 'ipoa'
                    auth-type:
                        type: str
                        description: Deprecated, please rename it to auth_type. PPP authentication type to use.
                        choices:
                            - 'auto'
                            - 'pap'
                            - 'chap'
                            - 'mschapv1'
                            - 'mschapv2'
                    auto-auth-extension-device:
                        type: str
                        description: Deprecated, please rename it to auto_auth_extension_device. Enable/disable automatic authorization of dedicated Fo...
                        choices:
                            - 'disable'
                            - 'enable'
                    bandwidth-measure-time:
                        type: int
                        description: Deprecated, please rename it to bandwidth_measure_time. Bandwidth measure time
                    bfd:
                        type: str
                        description: Bidirectional Forwarding Detection
                        choices:
                            - 'global'
                            - 'enable'
                            - 'disable'
                    bfd-desired-min-tx:
                        type: int
                        description: Deprecated, please rename it to bfd_desired_min_tx. BFD desired minimal transmit interval.
                    bfd-detect-mult:
                        type: int
                        description: Deprecated, please rename it to bfd_detect_mult. BFD detection multiplier.
                    bfd-required-min-rx:
                        type: int
                        description: Deprecated, please rename it to bfd_required_min_rx. BFD required minimal receive interval.
                    broadcast-forticlient-discovery:
                        type: str
                        description: Deprecated, please rename it to broadcast_forticlient_discovery. Enable/disable broadcasting FortiClient discovery...
                        choices:
                            - 'disable'
                            - 'enable'
                    broadcast-forward:
                        type: str
                        description: Deprecated, please rename it to broadcast_forward. Enable/disable broadcast forwarding.
                        choices:
                            - 'disable'
                            - 'enable'
                    captive-portal:
                        type: int
                        description: Deprecated, please rename it to captive_portal. Enable/disable captive portal.
                    cli-conn-status:
                        type: int
                        description: Deprecated, please rename it to cli_conn_status. Cli conn status.
                    color:
                        type: int
                        description: Color of icon on the GUI.
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
                        description: Deprecated, please rename it to dedicated_to. Configure interface for single purpose.
                        choices:
                            - 'none'
                            - 'management'
                    defaultgw:
                        type: str
                        description: Enable to get the gateway IP from the DHCP or PPPoE server.
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
                        description: Protocols used to detect the server.
                        choices:
                            - 'ping'
                            - 'tcp-echo'
                            - 'udp-echo'
                    detectserver:
                        type: str
                        description: Gateways ping server for this IP.
                    device-access-list:
                        type: raw
                        description: (list or str) Deprecated, please rename it to device_access_list. Device access list.
                    device-identification:
                        type: str
                        description: Deprecated, please rename it to device_identification. Enable/disable passively gathering of device identity infor...
                        choices:
                            - 'disable'
                            - 'enable'
                    device-identification-active-scan:
                        type: str
                        description: Deprecated, please rename it to device_identification_active_scan. Enable/disable active gathering of device ident...
                        choices:
                            - 'disable'
                            - 'enable'
                    device-netscan:
                        type: str
                        description: Deprecated, please rename it to device_netscan. Enable/disable inclusion of devices detected on this interface in ...
                        choices:
                            - 'disable'
                            - 'enable'
                    device-user-identification:
                        type: str
                        description: Deprecated, please rename it to device_user_identification. Enable/disable passive gathering of user identity info...
                        choices:
                            - 'disable'
                            - 'enable'
                    devindex:
                        type: int
                        description: Devindex.
                    dhcp-client-identifier:
                        type: str
                        description: Deprecated, please rename it to dhcp_client_identifier. DHCP client identifier.
                    dhcp-relay-agent-option:
                        type: str
                        description: Deprecated, please rename it to dhcp_relay_agent_option. Enable/disable DHCP relay agent option.
                        choices:
                            - 'disable'
                            - 'enable'
                    dhcp-relay-interface:
                        type: str
                        description: Deprecated, please rename it to dhcp_relay_interface. Specify outgoing interface to reach server.
                    dhcp-relay-interface-select-method:
                        type: str
                        description: Deprecated, please rename it to dhcp_relay_interface_select_method. Specify how to select outgoing interface to re...
                        choices:
                            - 'auto'
                            - 'sdwan'
                            - 'specify'
                    dhcp-relay-ip:
                        type: raw
                        description: (list) Deprecated, please rename it to dhcp_relay_ip. DHCP relay IP address.
                    dhcp-relay-service:
                        type: str
                        description: Deprecated, please rename it to dhcp_relay_service. Enable/disable allowing this interface to act as a DHCP relay.
                        choices:
                            - 'disable'
                            - 'enable'
                    dhcp-relay-type:
                        type: str
                        description: Deprecated, please rename it to dhcp_relay_type. DHCP relay type
                        choices:
                            - 'regular'
                            - 'ipsec'
                    dhcp-renew-time:
                        type: int
                        description: Deprecated, please rename it to dhcp_renew_time. DHCP renew time in seconds
                    disc-retry-timeout:
                        type: int
                        description: Deprecated, please rename it to disc_retry_timeout. Time in seconds to wait before retrying to start a PPPoE disco...
                    disconnect-threshold:
                        type: int
                        description: Deprecated, please rename it to disconnect_threshold. Time in milliseconds to wait before sending a notification t...
                    distance:
                        type: int
                        description: Distance for routes learned through PPPoE or DHCP, lower distance indicates preferred route.
                    dns-query:
                        type: str
                        description: Deprecated, please rename it to dns_query. Dns query.
                        choices:
                            - 'disable'
                            - 'recursive'
                            - 'non-recursive'
                    dns-server-override:
                        type: str
                        description: Deprecated, please rename it to dns_server_override. Enable/disable use DNS acquired by DHCP or PPPoE.
                        choices:
                            - 'disable'
                            - 'enable'
                    drop-fragment:
                        type: str
                        description: Deprecated, please rename it to drop_fragment. Enable/disable drop fragment packets.
                        choices:
                            - 'disable'
                            - 'enable'
                    drop-overlapped-fragment:
                        type: str
                        description: Deprecated, please rename it to drop_overlapped_fragment. Enable/disable drop overlapped fragment packets.
                        choices:
                            - 'disable'
                            - 'enable'
                    egress-cos:
                        type: str
                        description: Deprecated, please rename it to egress_cos. Override outgoing CoS in user VLAN tag.
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
                        description: Deprecated, please rename it to egress_shaping_profile. Outgoing traffic shaping profile.
                    eip:
                        type: str
                        description: Eip.
                    endpoint-compliance:
                        type: str
                        description: Deprecated, please rename it to endpoint_compliance. Enable/disable endpoint compliance enforcement.
                        choices:
                            - 'disable'
                            - 'enable'
                    estimated-downstream-bandwidth:
                        type: int
                        description: Deprecated, please rename it to estimated_downstream_bandwidth. Estimated maximum downstream bandwidth
                    estimated-upstream-bandwidth:
                        type: int
                        description: Deprecated, please rename it to estimated_upstream_bandwidth. Estimated maximum upstream bandwidth
                    explicit-ftp-proxy:
                        type: str
                        description: Deprecated, please rename it to explicit_ftp_proxy. Enable/disable the explicit FTP proxy on this interface.
                        choices:
                            - 'disable'
                            - 'enable'
                    explicit-web-proxy:
                        type: str
                        description: Deprecated, please rename it to explicit_web_proxy. Enable/disable the explicit web proxy on this interface.
                        choices:
                            - 'disable'
                            - 'enable'
                    external:
                        type: str
                        description: Enable/disable identifying the interface as an external interface
                        choices:
                            - 'disable'
                            - 'enable'
                    fail-action-on-extender:
                        type: str
                        description: Deprecated, please rename it to fail_action_on_extender. Action on extender when interface fail .
                        choices:
                            - 'soft-restart'
                            - 'hard-restart'
                            - 'reboot'
                    fail-alert-interfaces:
                        type: raw
                        description: (list or str) Deprecated, please rename it to fail_alert_interfaces. Names of the FortiGate interfaces to which th...
                    fail-alert-method:
                        type: str
                        description: Deprecated, please rename it to fail_alert_method. Select link-failed-signal or link-down method to alert about a ...
                        choices:
                            - 'link-failed-signal'
                            - 'link-down'
                    fail-detect:
                        type: str
                        description: Deprecated, please rename it to fail_detect. Enable/disable fail detection features for this interface.
                        choices:
                            - 'disable'
                            - 'enable'
                    fail-detect-option:
                        type: list
                        elements: str
                        description: Deprecated, please rename it to fail_detect_option. Options for detecting that this interface has failed.
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
                        description: Enable/disable FortiHeartBeat
                        choices:
                            - 'disable'
                            - 'enable'
                    fortilink:
                        type: str
                        description: Enable FortiLink to dedicate this interface to manage other Fortinet devices.
                        choices:
                            - 'disable'
                            - 'enable'
                    fortilink-backup-link:
                        type: int
                        description: Deprecated, please rename it to fortilink_backup_link. Fortilink backup link.
                    fortilink-neighbor-detect:
                        type: str
                        description: Deprecated, please rename it to fortilink_neighbor_detect. Protocol for FortiGate neighbor discovery.
                        choices:
                            - 'lldp'
                            - 'fortilink'
                    fortilink-split-interface:
                        type: str
                        description: Deprecated, please rename it to fortilink_split_interface. Enable/disable FortiLink split interface to connect mem...
                        choices:
                            - 'disable'
                            - 'enable'
                    fortilink-stacking:
                        type: str
                        description: Deprecated, please rename it to fortilink_stacking. Enable/disable FortiLink switch-stacking on this interface.
                        choices:
                            - 'disable'
                            - 'enable'
                    forward-domain:
                        type: int
                        description: Deprecated, please rename it to forward_domain. Transparent mode forward domain.
                    forward-error-correction:
                        type: str
                        description: Deprecated, please rename it to forward_error_correction. Enable/disable forward error correction
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
                        description: Deprecated, please rename it to fp_anomaly. Pass or drop different types of anomalies using Fastpath
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
                        description: Deprecated, please rename it to gateway_address. Gateway address
                    gi-gk:
                        type: str
                        description: Deprecated, please rename it to gi_gk. Enable/disable Gi Gatekeeper.
                        choices:
                            - 'disable'
                            - 'enable'
                    gwaddr:
                        type: str
                        description: Gateway address
                    gwdetect:
                        type: str
                        description: Enable/disable detect gateway alive for first.
                        choices:
                            - 'disable'
                            - 'enable'
                    ha-priority:
                        type: int
                        description: Deprecated, please rename it to ha_priority. HA election priority for the PING server.
                    icmp-accept-redirect:
                        type: str
                        description: Deprecated, please rename it to icmp_accept_redirect. Enable/disable ICMP accept redirect.
                        choices:
                            - 'disable'
                            - 'enable'
                    icmp-redirect:
                        type: str
                        description: Deprecated, please rename it to icmp_redirect. Enable/disable ICMP redirect.
                        choices:
                            - 'disable'
                            - 'enable'
                    icmp-send-redirect:
                        type: str
                        description: Deprecated, please rename it to icmp_send_redirect. Enable/disable sending of ICMP redirects.
                        choices:
                            - 'disable'
                            - 'enable'
                    ident-accept:
                        type: str
                        description: Deprecated, please rename it to ident_accept. Enable/disable authentication for this interface.
                        choices:
                            - 'disable'
                            - 'enable'
                    idle-timeout:
                        type: int
                        description: Deprecated, please rename it to idle_timeout. PPPoE auto disconnect after idle timeout seconds, 0 means no timeout.
                    if-mdix:
                        type: str
                        description: Deprecated, please rename it to if_mdix. Interface MDIX mode
                        choices:
                            - 'auto'
                            - 'normal'
                            - 'crossover'
                    if-media:
                        type: str
                        description: Deprecated, please rename it to if_media. Select interface media type
                        choices:
                            - 'auto'
                            - 'copper'
                            - 'fiber'
                    in-force-vlan-cos:
                        type: int
                        description: Deprecated, please rename it to in_force_vlan_cos. In force vlan cos.
                    inbandwidth:
                        type: int
                        description: Bandwidth limit for incoming traffic
                    ingress-cos:
                        type: str
                        description: Deprecated, please rename it to ingress_cos. Override incoming CoS in user VLAN tag on VLAN interface or assign a ...
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
                    ingress-shaping-profile:
                        type: str
                        description: Deprecated, please rename it to ingress_shaping_profile. Incoming traffic shaping profile.
                    ingress-spillover-threshold:
                        type: int
                        description: Deprecated, please rename it to ingress_spillover_threshold. Ingress Spillover threshold
                    internal:
                        type: int
                        description: Implicitly created.
                    ip:
                        type: str
                        description: Interface IPv4 address and subnet mask, syntax
                    ip-managed-by-fortiipam:
                        type: str
                        description: Deprecated, please rename it to ip_managed_by_fortiipam. Enable/disable automatic IP address assignment of this in...
                        choices:
                            - 'disable'
                            - 'enable'
                            - 'inherit-global'
                    ipmac:
                        type: str
                        description: Enable/disable IP/MAC binding.
                        choices:
                            - 'disable'
                            - 'enable'
                    ips-sniffer-mode:
                        type: str
                        description: Deprecated, please rename it to ips_sniffer_mode. Enable/disable the use of this interface as a one-armed sniffer.
                        choices:
                            - 'disable'
                            - 'enable'
                    ipunnumbered:
                        type: str
                        description: Unnumbered IP used for PPPoE interfaces for which no unique local address is provided.
                    ipv6:
                        type: dict
                        description: Ipv6.
                        suboptions:
                            autoconf:
                                type: str
                                description: Enable/disable address auto config.
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
                                description: Deprecated, please rename it to dhcp6_information_request. Enable/disable DHCPv6 information request.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            dhcp6-prefix-delegation:
                                type: str
                                description: Deprecated, please rename it to dhcp6_prefix_delegation. Enable/disable DHCPv6 prefix delegation.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            dhcp6-prefix-hint:
                                type: str
                                description: Deprecated, please rename it to dhcp6_prefix_hint. DHCPv6 prefix that will be used as a hint to the upstre...
                            dhcp6-prefix-hint-plt:
                                type: int
                                description: Deprecated, please rename it to dhcp6_prefix_hint_plt. DHCPv6 prefix hint preferred life time
                            dhcp6-prefix-hint-vlt:
                                type: int
                                description: Deprecated, please rename it to dhcp6_prefix_hint_vlt. DHCPv6 prefix hint valid life time
                            dhcp6-relay-ip:
                                type: str
                                description: Deprecated, please rename it to dhcp6_relay_ip. DHCPv6 relay IP address.
                            dhcp6-relay-service:
                                type: str
                                description: Deprecated, please rename it to dhcp6_relay_service. Enable/disable DHCPv6 relay.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            dhcp6-relay-type:
                                type: str
                                description: Deprecated, please rename it to dhcp6_relay_type. DHCPv6 relay type.
                                choices:
                                    - 'regular'
                            icmp6-send-redirect:
                                type: str
                                description: Deprecated, please rename it to icmp6_send_redirect. Enable/disable sending of ICMPv6 redirects.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            interface-identifier:
                                type: str
                                description: Deprecated, please rename it to interface_identifier. IPv6 interface identifier.
                            ip6-address:
                                type: str
                                description: Deprecated, please rename it to ip6_address. Primary IPv6 address prefix, syntax
                            ip6-allowaccess:
                                type: list
                                elements: str
                                description: Deprecated, please rename it to ip6_allowaccess. Allow management access to the interface.
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
                                description: Deprecated, please rename it to ip6_default_life. Default life
                            ip6-delegated-prefix-list:
                                type: list
                                elements: dict
                                description: Deprecated, please rename it to ip6_delegated_prefix_list. Ip6 delegated prefix list.
                                suboptions:
                                    autonomous-flag:
                                        type: str
                                        description: Deprecated, please rename it to autonomous_flag. Enable/disable the autonomous flag.
                                        choices:
                                            - 'disable'
                                            - 'enable'
                                    onlink-flag:
                                        type: str
                                        description: Deprecated, please rename it to onlink_flag. Enable/disable the onlink flag.
                                        choices:
                                            - 'disable'
                                            - 'enable'
                                    prefix-id:
                                        type: int
                                        description: Deprecated, please rename it to prefix_id. Prefix ID.
                                    rdnss:
                                        type: raw
                                        description: (list) Recursive DNS server option.
                                    rdnss-service:
                                        type: str
                                        description: Deprecated, please rename it to rdnss_service. Recursive DNS service option.
                                        choices:
                                            - 'delegated'
                                            - 'default'
                                            - 'specify'
                                    subnet:
                                        type: str
                                        description: Add subnet ID to routing prefix.
                                    upstream-interface:
                                        type: str
                                        description: Deprecated, please rename it to upstream_interface. Name of the interface that provides delegated ...
                                    delegated-prefix-iaid:
                                        type: int
                                        description: Deprecated, please rename it to delegated_prefix_iaid. IAID of obtained delegated-prefix from the ...
                            ip6-dns-server-override:
                                type: str
                                description: Deprecated, please rename it to ip6_dns_server_override. Enable/disable using the DNS server acquired by DHCP.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            ip6-extra-addr:
                                type: list
                                elements: dict
                                description: Deprecated, please rename it to ip6_extra_addr. Ip6 extra addr.
                                suboptions:
                                    prefix:
                                        type: str
                                        description: IPv6 address prefix.
                            ip6-hop-limit:
                                type: int
                                description: Deprecated, please rename it to ip6_hop_limit. Hop limit
                            ip6-link-mtu:
                                type: int
                                description: Deprecated, please rename it to ip6_link_mtu. IPv6 link MTU.
                            ip6-manage-flag:
                                type: str
                                description: Deprecated, please rename it to ip6_manage_flag. Enable/disable the managed flag.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            ip6-max-interval:
                                type: int
                                description: Deprecated, please rename it to ip6_max_interval. IPv6 maximum interval
                            ip6-min-interval:
                                type: int
                                description: Deprecated, please rename it to ip6_min_interval. IPv6 minimum interval
                            ip6-mode:
                                type: str
                                description: Deprecated, please rename it to ip6_mode. Addressing mode
                                choices:
                                    - 'static'
                                    - 'dhcp'
                                    - 'pppoe'
                                    - 'delegated'
                            ip6-other-flag:
                                type: str
                                description: Deprecated, please rename it to ip6_other_flag. Enable/disable the other IPv6 flag.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            ip6-prefix-list:
                                type: list
                                elements: dict
                                description: Deprecated, please rename it to ip6_prefix_list. Ip6 prefix list.
                                suboptions:
                                    autonomous-flag:
                                        type: str
                                        description: Deprecated, please rename it to autonomous_flag. Enable/disable the autonomous flag.
                                        choices:
                                            - 'disable'
                                            - 'enable'
                                    dnssl:
                                        type: raw
                                        description: (list) DNS search list option.
                                    onlink-flag:
                                        type: str
                                        description: Deprecated, please rename it to onlink_flag. Enable/disable the onlink flag.
                                        choices:
                                            - 'disable'
                                            - 'enable'
                                    preferred-life-time:
                                        type: int
                                        description: Deprecated, please rename it to preferred_life_time. Preferred life time
                                    prefix:
                                        type: str
                                        description: IPv6 prefix.
                                    rdnss:
                                        type: raw
                                        description: (list) Recursive DNS server option.
                                    valid-life-time:
                                        type: int
                                        description: Deprecated, please rename it to valid_life_time. Valid life time
                            ip6-reachable-time:
                                type: int
                                description: Deprecated, please rename it to ip6_reachable_time. IPv6 reachable time
                            ip6-retrans-time:
                                type: int
                                description: Deprecated, please rename it to ip6_retrans_time. IPv6 retransmit time
                            ip6-send-adv:
                                type: str
                                description: Deprecated, please rename it to ip6_send_adv. Enable/disable sending advertisements about the interface.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            ip6-subnet:
                                type: str
                                description: Deprecated, please rename it to ip6_subnet. Subnet to routing prefix, syntax
                            ip6-upstream-interface:
                                type: str
                                description: Deprecated, please rename it to ip6_upstream_interface. Interface name providing delegated information.
                            nd-cert:
                                type: str
                                description: Deprecated, please rename it to nd_cert. Neighbor discovery certificate.
                            nd-cga-modifier:
                                type: str
                                description: Deprecated, please rename it to nd_cga_modifier. Neighbor discovery CGA modifier.
                            nd-mode:
                                type: str
                                description: Deprecated, please rename it to nd_mode. Neighbor discovery mode.
                                choices:
                                    - 'basic'
                                    - 'SEND-compatible'
                            nd-security-level:
                                type: int
                                description: Deprecated, please rename it to nd_security_level. Neighbor discovery security level
                            nd-timestamp-delta:
                                type: int
                                description: Deprecated, please rename it to nd_timestamp_delta. Neighbor discovery timestamp delta value
                            nd-timestamp-fuzz:
                                type: int
                                description: Deprecated, please rename it to nd_timestamp_fuzz. Neighbor discovery timestamp fuzz factor
                            unique-autoconf-addr:
                                type: str
                                description: Deprecated, please rename it to unique_autoconf_addr. Enable/disable unique auto config address.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            vrip6_link_local:
                                type: str
                                description: Link-local IPv6 address of virtual router.
                            vrrp-virtual-mac6:
                                type: str
                                description: Deprecated, please rename it to vrrp_virtual_mac6. Enable/disable virtual MAC for VRRP.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            vrrp6:
                                type: list
                                elements: dict
                                description: Vrrp6.
                                suboptions:
                                    accept-mode:
                                        type: str
                                        description: Deprecated, please rename it to accept_mode. Enable/disable accept mode.
                                        choices:
                                            - 'disable'
                                            - 'enable'
                                    adv-interval:
                                        type: int
                                        description: Deprecated, please rename it to adv_interval. Advertisement interval
                                    preempt:
                                        type: str
                                        description: Enable/disable preempt mode.
                                        choices:
                                            - 'disable'
                                            - 'enable'
                                    priority:
                                        type: int
                                        description: Priority of the virtual router
                                    start-time:
                                        type: int
                                        description: Deprecated, please rename it to start_time. Startup time
                                    status:
                                        type: str
                                        description: Enable/disable VRRP.
                                        choices:
                                            - 'disable'
                                            - 'enable'
                                    vrdst6:
                                        type: str
                                        description: Monitor the route to this destination.
                                    vrgrp:
                                        type: int
                                        description: VRRP group ID
                                    vrid:
                                        type: int
                                        description: Virtual router identifier
                                    vrip6:
                                        type: str
                                        description: IPv6 address of the virtual router.
                                    ignore-default-route:
                                        type: str
                                        description: Deprecated, please rename it to ignore_default_route. Enable/disable ignoring of default route whe...
                                        choices:
                                            - 'disable'
                                            - 'enable'
                                    vrdst-priority:
                                        type: int
                                        description: Deprecated, please rename it to vrdst_priority. Priority of the virtual router when the virtual ro...
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
                                description: Deprecated, please rename it to ip6_delegated_prefix_iaid. IAID of obtained delegated-prefix from the upst...
                            dhcp6-relay-source-interface:
                                type: str
                                description: Deprecated, please rename it to dhcp6_relay_source_interface. Enable/disable use of address on this interf...
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
                        description: Enable/disable l2 forwarding.
                        choices:
                            - 'disable'
                            - 'enable'
                    l2tp-client:
                        type: str
                        description: Deprecated, please rename it to l2tp_client. Enable/disable this interface as a Layer 2 Tunnelling Protocol
                        choices:
                            - 'disable'
                            - 'enable'
                    lacp-ha-slave:
                        type: str
                        description: Deprecated, please rename it to lacp_ha_slave. LACP HA slave.
                        choices:
                            - 'disable'
                            - 'enable'
                    lacp-mode:
                        type: str
                        description: Deprecated, please rename it to lacp_mode. LACP mode.
                        choices:
                            - 'static'
                            - 'passive'
                            - 'active'
                    lacp-speed:
                        type: str
                        description: Deprecated, please rename it to lacp_speed. How often the interface sends LACP messages.
                        choices:
                            - 'slow'
                            - 'fast'
                    lcp-echo-interval:
                        type: int
                        description: Deprecated, please rename it to lcp_echo_interval. Time in seconds between PPPoE Link Control Protocol
                    lcp-max-echo-fails:
                        type: int
                        description: Deprecated, please rename it to lcp_max_echo_fails. Maximum missed LCP echo messages before disconnect.
                    link-up-delay:
                        type: int
                        description: Deprecated, please rename it to link_up_delay. Number of milliseconds to wait before considering a link is up.
                    listen-forticlient-connection:
                        type: str
                        description: Deprecated, please rename it to listen_forticlient_connection. Listen forticlient connection.
                        choices:
                            - 'disable'
                            - 'enable'
                    lldp-network-policy:
                        type: str
                        description: Deprecated, please rename it to lldp_network_policy. LLDP-MED network policy profile.
                    lldp-reception:
                        type: str
                        description: Deprecated, please rename it to lldp_reception. Enable/disable Link Layer Discovery Protocol
                        choices:
                            - 'disable'
                            - 'enable'
                            - 'vdom'
                    lldp-transmission:
                        type: str
                        description: Deprecated, please rename it to lldp_transmission. Enable/disable Link Layer Discovery Protocol
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
                        description: Change the interfaces MAC address.
                    managed-subnetwork-size:
                        type: str
                        description: Deprecated, please rename it to managed_subnetwork_size. Number of IP addresses to be allocated by FortiIPAM and u...
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
                    management-ip:
                        type: str
                        description: Deprecated, please rename it to management_ip. High Availability in-band management IP address of this interface.
                    max-egress-burst-rate:
                        type: int
                        description: Deprecated, please rename it to max_egress_burst_rate. Max egress burst rate
                    max-egress-rate:
                        type: int
                        description: Deprecated, please rename it to max_egress_rate. Max egress rate
                    measured-downstream-bandwidth:
                        type: int
                        description: Deprecated, please rename it to measured_downstream_bandwidth. Measured downstream bandwidth
                    measured-upstream-bandwidth:
                        type: int
                        description: Deprecated, please rename it to measured_upstream_bandwidth. Measured upstream bandwidth
                    mediatype:
                        type: str
                        description: Select SFP media interface type
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
                        description: (list or str) Physical interfaces that belong to the aggregate or redundant interface.
                    min-links:
                        type: int
                        description: Deprecated, please rename it to min_links. Minimum number of aggregated ports that must be up.
                    min-links-down:
                        type: str
                        description: Deprecated, please rename it to min_links_down. Action to take when less than the configured minimum number of lin...
                        choices:
                            - 'operational'
                            - 'administrative'
                    mode:
                        type: str
                        description: Addressing mode
                        choices:
                            - 'static'
                            - 'dhcp'
                            - 'pppoe'
                            - 'pppoa'
                            - 'ipoa'
                            - 'eoa'
                    monitor-bandwidth:
                        type: str
                        description: Deprecated, please rename it to monitor_bandwidth. Enable monitoring bandwidth on this interface.
                        choices:
                            - 'disable'
                            - 'enable'
                    mtu:
                        type: int
                        description: MTU value for this interface.
                    mtu-override:
                        type: str
                        description: Deprecated, please rename it to mtu_override. Enable to set a custom MTU for this interface.
                        choices:
                            - 'disable'
                            - 'enable'
                    mux-type:
                        type: str
                        description: Deprecated, please rename it to mux_type. Multiplexer type
                        choices:
                            - 'llc-encaps'
                            - 'vc-encaps'
                    name:
                        type: str
                        description: Name.
                    ndiscforward:
                        type: str
                        description: Enable/disable NDISC forwarding.
                        choices:
                            - 'disable'
                            - 'enable'
                    netbios-forward:
                        type: str
                        description: Deprecated, please rename it to netbios_forward. Enable/disable NETBIOS forwarding.
                        choices:
                            - 'disable'
                            - 'enable'
                    netflow-sampler:
                        type: str
                        description: Deprecated, please rename it to netflow_sampler. Enable/disable NetFlow on this interface and set the data that Ne...
                        choices:
                            - 'disable'
                            - 'tx'
                            - 'rx'
                            - 'both'
                    np-qos-profile:
                        type: int
                        description: Deprecated, please rename it to np_qos_profile. NP QoS profile ID.
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
                        description: Bandwidth limit for outgoing traffic
                    padt-retry-timeout:
                        type: int
                        description: Deprecated, please rename it to padt_retry_timeout. PPPoE Active Discovery Terminate
                    password:
                        type: raw
                        description: (list) PPPoE accounts password.
                    peer-interface:
                        type: raw
                        description: (list or str) Deprecated, please rename it to peer_interface. Peer interface.
                    phy-mode:
                        type: str
                        description: Deprecated, please rename it to phy_mode. DSL physical mode.
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
                        description: Enable/disable PoE status.
                        choices:
                            - 'disable'
                            - 'enable'
                    polling-interval:
                        type: int
                        description: Deprecated, please rename it to polling_interval. SFlow polling interval
                    pppoe-unnumbered-negotiate:
                        type: str
                        description: Deprecated, please rename it to pppoe_unnumbered_negotiate. Enable/disable PPPoE unnumbered negotiation.
                        choices:
                            - 'disable'
                            - 'enable'
                    pptp-auth-type:
                        type: str
                        description: Deprecated, please rename it to pptp_auth_type. PPTP authentication type.
                        choices:
                            - 'auto'
                            - 'pap'
                            - 'chap'
                            - 'mschapv1'
                            - 'mschapv2'
                    pptp-client:
                        type: str
                        description: Deprecated, please rename it to pptp_client. Enable/disable PPTP client.
                        choices:
                            - 'disable'
                            - 'enable'
                    pptp-password:
                        type: raw
                        description: (list) Deprecated, please rename it to pptp_password. PPTP password.
                    pptp-server-ip:
                        type: str
                        description: Deprecated, please rename it to pptp_server_ip. PPTP server IP address.
                    pptp-timeout:
                        type: int
                        description: Deprecated, please rename it to pptp_timeout. Idle timer in minutes
                    pptp-user:
                        type: str
                        description: Deprecated, please rename it to pptp_user. PPTP user name.
                    preserve-session-route:
                        type: str
                        description: Deprecated, please rename it to preserve_session_route. Enable/disable preservation of session route when dirty.
                        choices:
                            - 'disable'
                            - 'enable'
                    priority:
                        type: int
                        description: Priority of learned routes.
                    priority-override:
                        type: str
                        description: Deprecated, please rename it to priority_override. Enable/disable fail back to higher priority port once recovered.
                        choices:
                            - 'disable'
                            - 'enable'
                    proxy-captive-portal:
                        type: str
                        description: Deprecated, please rename it to proxy_captive_portal. Enable/disable proxy captive portal on this interface.
                        choices:
                            - 'disable'
                            - 'enable'
                    redundant-interface:
                        type: str
                        description: Deprecated, please rename it to redundant_interface. Redundant interface.
                    remote-ip:
                        type: str
                        description: Deprecated, please rename it to remote_ip. Remote IP address of tunnel.
                    replacemsg-override-group:
                        type: str
                        description: Deprecated, please rename it to replacemsg_override_group. Replacement message override group.
                    retransmission:
                        type: str
                        description: Enable/disable DSL retransmission.
                        choices:
                            - 'disable'
                            - 'enable'
                    ring-rx:
                        type: int
                        description: Deprecated, please rename it to ring_rx. RX ring size.
                    ring-tx:
                        type: int
                        description: Deprecated, please rename it to ring_tx. TX ring size.
                    role:
                        type: str
                        description: Interface role.
                        choices:
                            - 'lan'
                            - 'wan'
                            - 'dmz'
                            - 'undefined'
                    sample-direction:
                        type: str
                        description: Deprecated, please rename it to sample_direction. Data that NetFlow collects
                        choices:
                            - 'rx'
                            - 'tx'
                            - 'both'
                    sample-rate:
                        type: int
                        description: Deprecated, please rename it to sample_rate. SFlow sample rate
                    scan-botnet-connections:
                        type: str
                        description: Deprecated, please rename it to scan_botnet_connections. Enable monitoring or blocking connections to Botnet serve...
                        choices:
                            - 'disable'
                            - 'block'
                            - 'monitor'
                    secondary-IP:
                        type: str
                        description: Deprecated, please rename it to secondary_IP. Enable/disable adding a secondary IP to this interface.
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
                                description: Management access settings for the secondary IP address.
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
                                description: Protocols used to detect the server.
                                choices:
                                    - 'ping'
                                    - 'tcp-echo'
                                    - 'udp-echo'
                            detectserver:
                                type: str
                                description: Gateways ping server for this IP.
                            gwdetect:
                                type: str
                                description: Enable/disable detect gateway alive for first.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            ha-priority:
                                type: int
                                description: Deprecated, please rename it to ha_priority. HA election priority for the PING server.
                            id:
                                type: int
                                description: ID.
                            ip:
                                type: str
                                description: Secondary IP address of the interface.
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
                        description: Deprecated, please rename it to security_8021x_dynamic_vlan_id. VLAN ID for virtual switch.
                    security-8021x-master:
                        type: str
                        description: Deprecated, please rename it to security_8021x_master. '802.'
                    security-8021x-mode:
                        type: str
                        description: Deprecated, please rename it to security_8021x_mode. '802.'
                        choices:
                            - 'default'
                            - 'dynamic-vlan'
                            - 'fallback'
                            - 'slave'
                    security-exempt-list:
                        type: str
                        description: Deprecated, please rename it to security_exempt_list. Name of security-exempt-list.
                    security-external-logout:
                        type: str
                        description: Deprecated, please rename it to security_external_logout. URL of external authentication logout server.
                    security-external-web:
                        type: str
                        description: Deprecated, please rename it to security_external_web. URL of external authentication web server.
                    security-groups:
                        type: raw
                        description: (list or str) Deprecated, please rename it to security_groups. User groups that can authenticate with the captive ...
                    security-mac-auth-bypass:
                        type: str
                        description: Deprecated, please rename it to security_mac_auth_bypass. Enable/disable MAC authentication bypass.
                        choices:
                            - 'disable'
                            - 'enable'
                            - 'mac-auth-only'
                    security-mode:
                        type: str
                        description: Deprecated, please rename it to security_mode. Turn on captive portal authentication for this interface.
                        choices:
                            - 'none'
                            - 'captive-portal'
                            - '802.1X'
                    security-redirect-url:
                        type: str
                        description: Deprecated, please rename it to security_redirect_url. URL redirection after disclaimer/authentication.
                    service-name:
                        type: str
                        description: Deprecated, please rename it to service_name. PPPoE service name.
                    sflow-sampler:
                        type: str
                        description: Deprecated, please rename it to sflow_sampler. Enable/disable sFlow on this interface.
                        choices:
                            - 'disable'
                            - 'enable'
                    speed:
                        type: str
                        description: Interface speed.
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
                        description: Deprecated, please rename it to spillover_threshold. Egress Spillover threshold
                    src-check:
                        type: str
                        description: Deprecated, please rename it to src_check. Enable/disable source IP check.
                        choices:
                            - 'disable'
                            - 'enable'
                    status:
                        type: str
                        description: Bring the interface up or shut the interface down.
                        choices:
                            - 'down'
                            - 'up'
                    stp:
                        type: str
                        description: Enable/disable STP.
                        choices:
                            - 'disable'
                            - 'enable'
                    stp-ha-slave:
                        type: str
                        description: Deprecated, please rename it to stp_ha_slave. Control STP behaviour on HA slave.
                        choices:
                            - 'disable'
                            - 'enable'
                            - 'priority-adjust'
                    stpforward:
                        type: str
                        description: Enable/disable STP forwarding.
                        choices:
                            - 'disable'
                            - 'enable'
                    stpforward-mode:
                        type: str
                        description: Deprecated, please rename it to stpforward_mode. Configure STP forwarding mode.
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
                        description: Enable to always send packets from this interface to a destination MAC address.
                        choices:
                            - 'disable'
                            - 'enable'
                    substitute-dst-mac:
                        type: str
                        description: Deprecated, please rename it to substitute_dst_mac. Destination MAC address that all packets are sent to from this...
                    swc-first-create:
                        type: int
                        description: Deprecated, please rename it to swc_first_create. Initial create for switch-controller VLANs.
                    swc-vlan:
                        type: int
                        description: Deprecated, please rename it to swc_vlan. Swc vlan.
                    switch:
                        type: str
                        description: Switch.
                    switch-controller-access-vlan:
                        type: str
                        description: Deprecated, please rename it to switch_controller_access_vlan. Block FortiSwitch port-to-port traffic.
                        choices:
                            - 'disable'
                            - 'enable'
                    switch-controller-arp-inspection:
                        type: str
                        description: Deprecated, please rename it to switch_controller_arp_inspection. Enable/disable FortiSwitch ARP inspection.
                        choices:
                            - 'disable'
                            - 'enable'
                            - 'monitor'
                    switch-controller-auth:
                        type: str
                        description: Deprecated, please rename it to switch_controller_auth. Switch controller authentication.
                        choices:
                            - 'radius'
                            - 'usergroup'
                    switch-controller-dhcp-snooping:
                        type: str
                        description: Deprecated, please rename it to switch_controller_dhcp_snooping. Switch controller DHCP snooping.
                        choices:
                            - 'disable'
                            - 'enable'
                    switch-controller-dhcp-snooping-option82:
                        type: str
                        description: Deprecated, please rename it to switch_controller_dhcp_snooping_option82. Switch controller DHCP snooping option82.
                        choices:
                            - 'disable'
                            - 'enable'
                    switch-controller-dhcp-snooping-verify-mac:
                        type: str
                        description: Deprecated, please rename it to switch_controller_dhcp_snooping_verify_mac. Switch controller DHCP snooping verify...
                        choices:
                            - 'disable'
                            - 'enable'
                    switch-controller-feature:
                        type: str
                        description: Deprecated, please rename it to switch_controller_feature. Interfaces purpose when assigning traffic
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
                    switch-controller-igmp-snooping:
                        type: str
                        description: Deprecated, please rename it to switch_controller_igmp_snooping. Switch controller IGMP snooping.
                        choices:
                            - 'disable'
                            - 'enable'
                    switch-controller-igmp-snooping-fast-leave:
                        type: str
                        description: Deprecated, please rename it to switch_controller_igmp_snooping_fast_leave. Switch controller IGMP snooping fast-l...
                        choices:
                            - 'disable'
                            - 'enable'
                    switch-controller-igmp-snooping-proxy:
                        type: str
                        description: Deprecated, please rename it to switch_controller_igmp_snooping_proxy. Switch controller IGMP snooping proxy.
                        choices:
                            - 'disable'
                            - 'enable'
                    switch-controller-iot-scanning:
                        type: str
                        description: Deprecated, please rename it to switch_controller_iot_scanning. Enable/disable managed FortiSwitch IoT scanning.
                        choices:
                            - 'disable'
                            - 'enable'
                    switch-controller-learning-limit:
                        type: int
                        description: Deprecated, please rename it to switch_controller_learning_limit. Limit the number of dynamic MAC addresses on thi...
                    switch-controller-mgmt-vlan:
                        type: int
                        description: Deprecated, please rename it to switch_controller_mgmt_vlan. VLAN to use for FortiLink management purposes.
                    switch-controller-nac:
                        type: str
                        description: Deprecated, please rename it to switch_controller_nac. Integrated NAC settings for managed FortiSwitch.
                    switch-controller-radius-server:
                        type: str
                        description: Deprecated, please rename it to switch_controller_radius_server. RADIUS server name for this FortiSwitch VLAN.
                    switch-controller-rspan-mode:
                        type: str
                        description: Deprecated, please rename it to switch_controller_rspan_mode. Stop Layer2 MAC learning and interception of BPDUs a...
                        choices:
                            - 'disable'
                            - 'enable'
                    switch-controller-source-ip:
                        type: str
                        description: Deprecated, please rename it to switch_controller_source_ip. Source IP address used in FortiLink over L3 connections.
                        choices:
                            - 'outbound'
                            - 'fixed'
                    switch-controller-traffic-policy:
                        type: str
                        description: Deprecated, please rename it to switch_controller_traffic_policy. Switch controller traffic policy for the VLAN.
                    tc-mode:
                        type: str
                        description: Deprecated, please rename it to tc_mode. DSL transfer mode.
                        choices:
                            - 'ptm'
                            - 'atm'
                    tcp-mss:
                        type: int
                        description: Deprecated, please rename it to tcp_mss. TCP maximum segment size.
                    trunk:
                        type: str
                        description: Enable/disable VLAN trunk.
                        choices:
                            - 'disable'
                            - 'enable'
                    trust-ip-1:
                        type: str
                        description: Deprecated, please rename it to trust_ip_1. Trusted host for dedicated management traffic
                    trust-ip-2:
                        type: str
                        description: Deprecated, please rename it to trust_ip_2. Trusted host for dedicated management traffic
                    trust-ip-3:
                        type: str
                        description: Deprecated, please rename it to trust_ip_3. Trusted host for dedicated management traffic
                    trust-ip6-1:
                        type: str
                        description: Deprecated, please rename it to trust_ip6_1. Trusted IPv6 host for dedicated management traffic
                    trust-ip6-2:
                        type: str
                        description: Deprecated, please rename it to trust_ip6_2. Trusted IPv6 host for dedicated management traffic
                    trust-ip6-3:
                        type: str
                        description: Deprecated, please rename it to trust_ip6_3. Trusted IPv6 host for dedicated management traffic
                    type:
                        type: str
                        description: Interface type.
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
                        description: Username of the PPPoE account, provided by your ISP.
                    vci:
                        type: int
                        description: Virtual Channel ID
                    vectoring:
                        type: str
                        description: Enable/disable DSL vectoring.
                        choices:
                            - 'disable'
                            - 'enable'
                    vindex:
                        type: int
                        description: Vindex.
                    vlan-protocol:
                        type: str
                        description: Deprecated, please rename it to vlan_protocol. Ethernet protocol of VLAN.
                        choices:
                            - '8021q'
                            - '8021ad'
                    vlanforward:
                        type: str
                        description: Enable/disable traffic forwarding between VLANs on this interface.
                        choices:
                            - 'disable'
                            - 'enable'
                    vlanid:
                        type: int
                        description: VLAN ID
                    vpi:
                        type: int
                        description: Virtual Path ID
                    vrf:
                        type: int
                        description: Virtual Routing Forwarding ID.
                    vrrp:
                        type: list
                        elements: dict
                        description: Vrrp.
                        suboptions:
                            accept-mode:
                                type: str
                                description: Deprecated, please rename it to accept_mode. Enable/disable accept mode.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            adv-interval:
                                type: int
                                description: Deprecated, please rename it to adv_interval. Advertisement interval
                            ignore-default-route:
                                type: str
                                description: Deprecated, please rename it to ignore_default_route. Enable/disable ignoring of default route when checki...
                                choices:
                                    - 'disable'
                                    - 'enable'
                            preempt:
                                type: str
                                description: Enable/disable preempt mode.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            priority:
                                type: int
                                description: Priority of the virtual router
                            start-time:
                                type: int
                                description: Deprecated, please rename it to start_time. Startup time
                            status:
                                type: str
                                description: Enable/disable this VRRP configuration.
                                choices:
                                    - 'disable'
                                    - 'enable'
                            version:
                                type: str
                                description: VRRP version.
                                choices:
                                    - '2'
                                    - '3'
                            vrdst:
                                type: raw
                                description: (list) Monitor the route to this destination.
                            vrdst-priority:
                                type: int
                                description: Deprecated, please rename it to vrdst_priority. Priority of the virtual router when the virtual router des...
                            vrgrp:
                                type: int
                                description: VRRP group ID
                            vrid:
                                type: int
                                description: Virtual router identifier
                            vrip:
                                type: str
                                description: IP address of the virtual router.
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
                        description: Deprecated, please rename it to vrrp_virtual_mac. Enable/disable use of virtual MAC for VRRP.
                        choices:
                            - 'disable'
                            - 'enable'
                    wccp:
                        type: str
                        description: Enable/disable WCCP on this interface.
                        choices:
                            - 'disable'
                            - 'enable'
                    weight:
                        type: int
                        description: Default weight for static routes
                    wifi-5g-threshold:
                        type: str
                        description: Deprecated, please rename it to wifi_5g_threshold. Minimal signal strength to be considered as a good 5G AP.
                    wifi-acl:
                        type: str
                        description: Deprecated, please rename it to wifi_acl. Access control for MAC addresses in the MAC list.
                        choices:
                            - 'deny'
                            - 'allow'
                    wifi-ap-band:
                        type: str
                        description: Deprecated, please rename it to wifi_ap_band. How to select the AP to connect.
                        choices:
                            - 'any'
                            - '5g-preferred'
                            - '5g-only'
                    wifi-auth:
                        type: str
                        description: Deprecated, please rename it to wifi_auth. WiFi authentication.
                        choices:
                            - 'PSK'
                            - 'RADIUS'
                            - 'radius'
                            - 'usergroup'
                    wifi-auto-connect:
                        type: str
                        description: Deprecated, please rename it to wifi_auto_connect. Enable/disable WiFi network auto connect.
                        choices:
                            - 'disable'
                            - 'enable'
                    wifi-auto-save:
                        type: str
                        description: Deprecated, please rename it to wifi_auto_save. Enable/disable WiFi network automatic save.
                        choices:
                            - 'disable'
                            - 'enable'
                    wifi-broadcast-ssid:
                        type: str
                        description: Deprecated, please rename it to wifi_broadcast_ssid. Enable/disable SSID broadcast in the beacon.
                        choices:
                            - 'disable'
                            - 'enable'
                    wifi-encrypt:
                        type: str
                        description: Deprecated, please rename it to wifi_encrypt. Data encryption.
                        choices:
                            - 'TKIP'
                            - 'AES'
                    wifi-fragment-threshold:
                        type: int
                        description: Deprecated, please rename it to wifi_fragment_threshold. WiFi fragment threshold
                    wifi-key:
                        type: raw
                        description: (list) Deprecated, please rename it to wifi_key. WiFi WEP Key.
                    wifi-keyindex:
                        type: int
                        description: Deprecated, please rename it to wifi_keyindex. WEP key index
                    wifi-mac-filter:
                        type: str
                        description: Deprecated, please rename it to wifi_mac_filter. Enable/disable MAC filter status.
                        choices:
                            - 'disable'
                            - 'enable'
                    wifi-passphrase:
                        type: raw
                        description: (list) Deprecated, please rename it to wifi_passphrase. WiFi pre-shared key for WPA.
                    wifi-radius-server:
                        type: str
                        description: Deprecated, please rename it to wifi_radius_server. WiFi RADIUS server for WPA.
                    wifi-rts-threshold:
                        type: int
                        description: Deprecated, please rename it to wifi_rts_threshold. WiFi RTS threshold
                    wifi-security:
                        type: str
                        description: Deprecated, please rename it to wifi_security. Wireless access security of SSID.
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
                        description: Deprecated, please rename it to wifi_ssid. IEEE 802.
                    wifi-usergroup:
                        type: str
                        description: Deprecated, please rename it to wifi_usergroup. WiFi user group for WPA.
                    wins-ip:
                        type: str
                        description: Deprecated, please rename it to wins_ip. WINS server IP.
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
                        description: Deprecated, please rename it to dhcp_classless_route_addition. Enable/disable addition of classless static routes ...
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
                        description: Deprecated, please rename it to dhcp_broadcast_flag. Enable/disable setting of the broadcast flag in messages sent...
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
                        description: Deprecated, please rename it to switch_controller_offload_gw. Enable/disable managed FortiSwitch routing offload g...
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
                        description: Deprecated, please rename it to dhcp_relay_allow_no_end_option. Enable/disable relaying DHCP messages with no end ...
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
    - name: FortiSwitch VLAN template.
      fortinet.fortimanager.fmgr_fsp_vlan:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: present # <value in [present, absent]>
        fsp_vlan:
          _dhcp_status: <value in [disable, enable]>
          auth: <value in [radius, usergroup]>
          color: <integer>
          comments: <string>
          dynamic_mapping:
            -
              _dhcp_status: <value in [disable, enable]>
              _scope:
                -
                  name: <string>
                  vdom: <string>
              dhcp_server:
                auto_configuration: <value in [disable, enable]>
                auto_managed_status: <value in [disable, enable]>
                conflicted_ip_timeout: <integer>
                ddns_auth: <value in [disable, tsig]>
                ddns_key: <list or string>
                ddns_keyname: <string>
                ddns_server_ip: <string>
                ddns_ttl: <integer>
                ddns_update: <value in [disable, enable]>
                ddns_update_override: <value in [disable, enable]>
                ddns_zone: <string>
                default_gateway: <string>
                dhcp_settings_from_fortiipam: <value in [disable, enable]>
                dns_server1: <string>
                dns_server2: <string>
                dns_server3: <string>
                dns_server4: <string>
                dns_service: <value in [default, specify, local]>
                domain: <string>
                enable: <value in [disable, enable]>
                exclude_range:
                  -
                    end_ip: <string>
                    id: <integer>
                    start_ip: <string>
                    vci_match: <value in [disable, enable]>
                    vci_string: <list or string>
                    lease_time: <integer>
                    uci_match: <value in [disable, enable]>
                    uci_string: <list or string>
                filename: <string>
                forticlient_on_net_status: <value in [disable, enable]>
                id: <integer>
                ip_mode: <value in [range, usrgrp]>
                ip_range:
                  -
                    end_ip: <string>
                    id: <integer>
                    start_ip: <string>
                    vci_match: <value in [disable, enable]>
                    vci_string: <list or string>
                    lease_time: <integer>
                    uci_match: <value in [disable, enable]>
                    uci_string: <list or string>
                ipsec_lease_hold: <integer>
                lease_time: <integer>
                mac_acl_default_action: <value in [assign, block]>
                netmask: <string>
                next_server: <string>
                ntp_server1: <string>
                ntp_server2: <string>
                ntp_server3: <string>
                ntp_service: <value in [default, specify, local]>
                option1: <list or string>
                option2: <list or string>
                option3: <list or string>
                option4: <string>
                option5: <string>
                option6: <string>
                options:
                  -
                    code: <integer>
                    id: <integer>
                    ip: <list or string>
                    type: <value in [hex, string, ip, ...]>
                    value: <string>
                    vci_match: <value in [disable, enable]>
                    vci_string: <list or string>
                    uci_match: <value in [disable, enable]>
                    uci_string: <list or string>
                reserved_address:
                  -
                    action: <value in [assign, block, reserved]>
                    circuit_id: <string>
                    circuit_id_type: <value in [hex, string]>
                    description: <string>
                    id: <integer>
                    ip: <string>
                    mac: <string>
                    remote_id: <string>
                    remote_id_type: <value in [hex, string]>
                    type: <value in [mac, option82]>
                server_type: <value in [regular, ipsec]>
                status: <value in [disable, enable]>
                tftp_server: <list or string>
                timezone: <value in [00, 01, 02, ...]>
                timezone_option: <value in [disable, default, specify]>
                vci_match: <value in [disable, enable]>
                vci_string: <list or string>
                wifi_ac_service: <value in [specify, local]>
                wifi_ac1: <string>
                wifi_ac2: <string>
                wifi_ac3: <string>
                wins_server1: <string>
                wins_server2: <string>
                relay_agent: <string>
                shared_subnet: <value in [disable, enable]>
              interface:
                dhcp_relay_agent_option: <value in [disable, enable]>
                dhcp_relay_ip: <list or string>
                dhcp_relay_service: <value in [disable, enable]>
                dhcp_relay_type: <value in [regular, ipsec]>
                ip: <string>
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
                  icmp6_send_redirect: <value in [disable, enable]>
                  interface_identifier: <string>
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
                  ip6_dns_server_override: <value in [disable, enable]>
                  ip6_extra_addr:
                    -
                      prefix: <string>
                  ip6_hop_limit: <integer>
                  ip6_link_mtu: <integer>
                  ip6_manage_flag: <value in [disable, enable]>
                  ip6_max_interval: <integer>
                  ip6_min_interval: <integer>
                  ip6_mode: <value in [static, dhcp, pppoe, ...]>
                  ip6_other_flag: <value in [disable, enable]>
                  ip6_prefix_list:
                    -
                      autonomous_flag: <value in [disable, enable]>
                      dnssl: <list or string>
                      onlink_flag: <value in [disable, enable]>
                      preferred_life_time: <integer>
                      prefix: <string>
                      rdnss: <list or string>
                      valid_life_time: <integer>
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
                  unique_autoconf_addr: <value in [disable, enable]>
                  vrip6_link_local: <string>
                  vrrp_virtual_mac6: <value in [disable, enable]>
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
                  cli_conn6_status: <integer>
                  ip6_prefix_mode: <value in [dhcp6, ra]>
                  ra_send_mtu: <value in [disable, enable]>
                  ip6_delegated_prefix_iaid: <integer>
                  dhcp6_relay_source_interface: <value in [disable, enable]>
                  dhcp6_relay_interface_id: <string>
                  dhcp6_relay_source_ip: <string>
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
                vlanid: <integer>
                dhcp_relay_interface_select_method: <value in [auto, sdwan, specify]>
                vrrp:
                  -
                    accept_mode: <value in [disable, enable]>
                    adv_interval: <integer>
                    ignore_default_route: <value in [disable, enable]>
                    preempt: <value in [disable, enable]>
                    priority: <integer>
                    proxy_arp:
                      -
                        id: <integer>
                        ip: <string>
                    start_time: <integer>
                    status: <value in [disable, enable]>
                    version: <value in [2, 3]>
                    vrdst: <list or string>
                    vrdst_priority: <integer>
                    vrgrp: <integer>
                    vrid: <integer>
                    vrip: <string>
          name: <string>
          portal_message_override_group: <string>
          radius_server: <string>
          security: <value in [open, captive-portal, 8021x]>
          selected_usergroups: <string>
          usergroup: <string>
          vdom: <string>
          vlanid: <integer>
          dhcp_server:
            auto_configuration: <value in [disable, enable]>
            auto_managed_status: <value in [disable, enable]>
            conflicted_ip_timeout: <integer>
            ddns_auth: <value in [disable, tsig]>
            ddns_key: <list or string>
            ddns_keyname: <string>
            ddns_server_ip: <string>
            ddns_ttl: <integer>
            ddns_update: <value in [disable, enable]>
            ddns_update_override: <value in [disable, enable]>
            ddns_zone: <string>
            default_gateway: <string>
            dhcp_settings_from_fortiipam: <value in [disable, enable]>
            dns_server1: <string>
            dns_server2: <string>
            dns_server3: <string>
            dns_server4: <string>
            dns_service: <value in [default, specify, local]>
            domain: <string>
            enable: <value in [disable, enable]>
            exclude_range:
              -
                end_ip: <string>
                id: <integer>
                start_ip: <string>
                vci_match: <value in [disable, enable]>
                vci_string: <list or string>
                lease_time: <integer>
                uci_match: <value in [disable, enable]>
                uci_string: <list or string>
            filename: <string>
            forticlient_on_net_status: <value in [disable, enable]>
            id: <integer>
            ip_mode: <value in [range, usrgrp]>
            ip_range:
              -
                end_ip: <string>
                id: <integer>
                start_ip: <string>
                vci_match: <value in [disable, enable]>
                vci_string: <list or string>
                lease_time: <integer>
                uci_match: <value in [disable, enable]>
                uci_string: <list or string>
            ipsec_lease_hold: <integer>
            lease_time: <integer>
            mac_acl_default_action: <value in [assign, block]>
            netmask: <string>
            next_server: <string>
            ntp_server1: <string>
            ntp_server2: <string>
            ntp_server3: <string>
            ntp_service: <value in [default, specify, local]>
            option1: <list or string>
            option2: <list or string>
            option3: <list or string>
            option4: <string>
            option5: <string>
            option6: <string>
            options:
              -
                code: <integer>
                id: <integer>
                ip: <list or string>
                type: <value in [hex, string, ip, ...]>
                value: <string>
                vci_match: <value in [disable, enable]>
                vci_string: <list or string>
                uci_match: <value in [disable, enable]>
                uci_string: <list or string>
            reserved_address:
              -
                action: <value in [assign, block, reserved]>
                circuit_id: <string>
                circuit_id_type: <value in [hex, string]>
                description: <string>
                id: <integer>
                ip: <string>
                mac: <string>
                remote_id: <string>
                remote_id_type: <value in [hex, string]>
                type: <value in [mac, option82]>
            server_type: <value in [regular, ipsec]>
            status: <value in [disable, enable]>
            tftp_server: <list or string>
            timezone: <value in [00, 01, 02, ...]>
            timezone_option: <value in [disable, default, specify]>
            vci_match: <value in [disable, enable]>
            vci_string: <list or string>
            wifi_ac_service: <value in [specify, local]>
            wifi_ac1: <string>
            wifi_ac2: <string>
            wifi_ac3: <string>
            wins_server1: <string>
            wins_server2: <string>
            relay_agent: <string>
            shared_subnet: <value in [disable, enable]>
          interface:
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
            bandwidth_measure_time: <integer>
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
            dhcp_relay_interface: <string>
            dhcp_relay_interface_select_method: <value in [auto, sdwan, specify]>
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
            eip: <string>
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
            fortilink_neighbor_detect: <value in [lldp, fortilink]>
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
            ingress_shaping_profile: <string>
            ingress_spillover_threshold: <integer>
            internal: <integer>
            ip: <string>
            ip_managed_by_fortiipam: <value in [disable, enable, inherit-global]>
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
              icmp6_send_redirect: <value in [disable, enable]>
              interface_identifier: <string>
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
              ip6_dns_server_override: <value in [disable, enable]>
              ip6_extra_addr:
                -
                  prefix: <string>
              ip6_hop_limit: <integer>
              ip6_link_mtu: <integer>
              ip6_manage_flag: <value in [disable, enable]>
              ip6_max_interval: <integer>
              ip6_min_interval: <integer>
              ip6_mode: <value in [static, dhcp, pppoe, ...]>
              ip6_other_flag: <value in [disable, enable]>
              ip6_prefix_list:
                -
                  autonomous_flag: <value in [disable, enable]>
                  dnssl: <list or string>
                  onlink_flag: <value in [disable, enable]>
                  preferred_life_time: <integer>
                  prefix: <string>
                  rdnss: <list or string>
                  valid_life_time: <integer>
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
              unique_autoconf_addr: <value in [disable, enable]>
              vrip6_link_local: <string>
              vrrp_virtual_mac6: <value in [disable, enable]>
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
            managed_subnetwork_size: <value in [256, 512, 1024, ...]>
            management_ip: <string>
            max_egress_burst_rate: <integer>
            max_egress_rate: <integer>
            measured_downstream_bandwidth: <integer>
            measured_upstream_bandwidth: <integer>
            mediatype: <value in [serdes-sfp, sgmii-sfp, cfp2-sr10, ...]>
            member: <list or string>
            min_links: <integer>
            min_links_down: <value in [operational, administrative]>
            mode: <value in [static, dhcp, pppoe, ...]>
            monitor_bandwidth: <value in [disable, enable]>
            mtu: <integer>
            mtu_override: <value in [disable, enable]>
            mux_type: <value in [llc-encaps, vc-encaps]>
            name: <string>
            ndiscforward: <value in [disable, enable]>
            netbios_forward: <value in [disable, enable]>
            netflow_sampler: <value in [disable, tx, rx, ...]>
            np_qos_profile: <integer>
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
            ring_rx: <integer>
            ring_tx: <integer>
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
            swc_first_create: <integer>
            swc_vlan: <integer>
            switch: <string>
            switch_controller_access_vlan: <value in [disable, enable]>
            switch_controller_arp_inspection: <value in [disable, enable, monitor]>
            switch_controller_auth: <value in [radius, usergroup]>
            switch_controller_dhcp_snooping: <value in [disable, enable]>
            switch_controller_dhcp_snooping_option82: <value in [disable, enable]>
            switch_controller_dhcp_snooping_verify_mac: <value in [disable, enable]>
            switch_controller_feature: <value in [none, default-vlan, quarantine, ...]>
            switch_controller_igmp_snooping: <value in [disable, enable]>
            switch_controller_igmp_snooping_fast_leave: <value in [disable, enable]>
            switch_controller_igmp_snooping_proxy: <value in [disable, enable]>
            switch_controller_iot_scanning: <value in [disable, enable]>
            switch_controller_learning_limit: <integer>
            switch_controller_mgmt_vlan: <integer>
            switch_controller_nac: <string>
            switch_controller_radius_server: <string>
            switch_controller_rspan_mode: <value in [disable, enable]>
            switch_controller_source_ip: <value in [outbound, fixed]>
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
            vlan_protocol: <value in [8021q, 8021ad]>
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
        '/pm/config/adom/{adom}/obj/fsp/vlan',
        '/pm/config/global/obj/fsp/vlan'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/fsp/vlan/{vlan}',
        '/pm/config/global/obj/fsp/vlan/{vlan}'
    ]

    url_params = ['adom']
    module_primary_key = 'name'
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'fsp_vlan': {
            'type': 'dict',
            'v_range': [['6.0.0', '']],
            'options': {
                '_dhcp-status': {'choices': ['disable', 'enable'], 'type': 'str'},
                'auth': {'v_range': [['6.0.0', '6.2.1']], 'choices': ['radius', 'usergroup'], 'type': 'str'},
                'color': {'type': 'int'},
                'comments': {'v_range': [['6.0.0', '6.2.1']], 'type': 'str'},
                'dynamic_mapping': {
                    'type': 'list',
                    'options': {
                        '_dhcp-status': {'choices': ['disable', 'enable'], 'type': 'str'},
                        '_scope': {'type': 'list', 'options': {'name': {'type': 'str'}, 'vdom': {'type': 'str'}}, 'elements': 'dict'},
                        'dhcp-server': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'type': 'dict',
                            'options': {
                                'auto-configuration': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'auto-managed-status': {'v_range': [['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'conflicted-ip-timeout': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                'ddns-auth': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'tsig'], 'type': 'str'},
                                'ddns-key': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'no_log': True, 'type': 'raw'},
                                'ddns-keyname': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'no_log': True, 'type': 'str'},
                                'ddns-server-ip': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'ddns-ttl': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                'ddns-update': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'ddns-update-override': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'ddns-zone': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'default-gateway': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'dhcp-settings-from-fortiipam': {'v_range': [['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'dns-server1': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'dns-server2': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'dns-server3': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'dns-server4': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'dns-service': {
                                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                    'choices': ['default', 'specify', 'local'],
                                    'type': 'str'
                                },
                                'domain': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'enable': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'exclude-range': {
                                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                    'type': 'list',
                                    'options': {
                                        'end-ip': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                        'id': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                        'start-ip': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                        'vci-match': {'v_range': [['7.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                        'vci-string': {'v_range': [['7.2.1', '']], 'type': 'raw'},
                                        'lease-time': {'v_range': [['7.2.2', '']], 'type': 'int'},
                                        'uci-match': {'v_range': [['7.2.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                        'uci-string': {'v_range': [['7.2.2', '']], 'type': 'raw'}
                                    },
                                    'elements': 'dict'
                                },
                                'filename': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'forticlient-on-net-status': {
                                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                    'choices': ['disable', 'enable'],
                                    'type': 'str'
                                },
                                'id': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                'ip-mode': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['range', 'usrgrp'], 'type': 'str'},
                                'ip-range': {
                                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                    'type': 'list',
                                    'options': {
                                        'end-ip': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                        'id': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                        'start-ip': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                        'vci-match': {'v_range': [['7.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                        'vci-string': {'v_range': [['7.2.1', '']], 'type': 'raw'},
                                        'lease-time': {'v_range': [['7.2.2', '']], 'type': 'int'},
                                        'uci-match': {'v_range': [['7.2.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                        'uci-string': {'v_range': [['7.2.2', '']], 'type': 'raw'}
                                    },
                                    'elements': 'dict'
                                },
                                'ipsec-lease-hold': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                'lease-time': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                'mac-acl-default-action': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['assign', 'block'], 'type': 'str'},
                                'netmask': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'next-server': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'ntp-server1': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'ntp-server2': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'ntp-server3': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'ntp-service': {
                                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                    'choices': ['default', 'specify', 'local'],
                                    'type': 'str'
                                },
                                'option1': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'raw'},
                                'option2': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'raw'},
                                'option3': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'raw'},
                                'option4': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'option5': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'option6': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'options': {
                                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                    'type': 'list',
                                    'options': {
                                        'code': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                        'id': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                        'ip': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'raw'},
                                        'type': {
                                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                            'choices': ['hex', 'string', 'ip', 'fqdn'],
                                            'type': 'str'
                                        },
                                        'value': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                        'vci-match': {'v_range': [['7.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                        'vci-string': {'v_range': [['7.2.1', '']], 'type': 'raw'},
                                        'uci-match': {'v_range': [['7.2.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                        'uci-string': {'v_range': [['7.2.2', '']], 'type': 'raw'}
                                    },
                                    'elements': 'dict'
                                },
                                'reserved-address': {
                                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                    'type': 'list',
                                    'options': {
                                        'action': {
                                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                            'choices': ['assign', 'block', 'reserved'],
                                            'type': 'str'
                                        },
                                        'circuit-id': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                        'circuit-id-type': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['hex', 'string'], 'type': 'str'},
                                        'description': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                        'id': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                        'ip': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                        'mac': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                        'remote-id': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                        'remote-id-type': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['hex', 'string'], 'type': 'str'},
                                        'type': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['mac', 'option82'], 'type': 'str'}
                                    },
                                    'elements': 'dict'
                                },
                                'server-type': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['regular', 'ipsec'], 'type': 'str'},
                                'status': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'tftp-server': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'raw'},
                                'timezone': {
                                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                    'choices': [
                                        '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                                        '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37',
                                        '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56',
                                        '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75',
                                        '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87'
                                    ],
                                    'type': 'str'
                                },
                                'timezone-option': {
                                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                    'choices': ['disable', 'default', 'specify'],
                                    'type': 'str'
                                },
                                'vci-match': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'vci-string': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'raw'},
                                'wifi-ac-service': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['specify', 'local'], 'type': 'str'},
                                'wifi-ac1': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'wifi-ac2': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'wifi-ac3': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'wins-server1': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'wins-server2': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'relay-agent': {'v_range': [['7.4.0', '']], 'type': 'str'},
                                'shared-subnet': {'v_range': [['7.4.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'}
                            }
                        },
                        'interface': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'type': 'dict',
                            'options': {
                                'dhcp-relay-agent-option': {
                                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                    'choices': ['disable', 'enable'],
                                    'type': 'str'
                                },
                                'dhcp-relay-ip': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'raw'},
                                'dhcp-relay-service': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'dhcp-relay-type': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['regular', 'ipsec'], 'type': 'str'},
                                'ip': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'ipv6': {
                                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                    'type': 'dict',
                                    'options': {
                                        'autoconf': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                        'dhcp6-client-options': {
                                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                            'type': 'list',
                                            'choices': ['rapid', 'iapd', 'iana', 'dns', 'dnsname'],
                                            'elements': 'str'
                                        },
                                        'dhcp6-information-request': {
                                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                            'choices': ['disable', 'enable'],
                                            'type': 'str'
                                        },
                                        'dhcp6-prefix-delegation': {
                                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                            'choices': ['disable', 'enable'],
                                            'type': 'str'
                                        },
                                        'dhcp6-prefix-hint': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                        'dhcp6-prefix-hint-plt': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                        'dhcp6-prefix-hint-vlt': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                        'dhcp6-relay-ip': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                        'dhcp6-relay-service': {
                                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                            'choices': ['disable', 'enable'],
                                            'type': 'str'
                                        },
                                        'dhcp6-relay-type': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['regular'], 'type': 'str'},
                                        'icmp6-send-redirect': {'v_range': [['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                        'interface-identifier': {'v_range': [['6.4.5', '']], 'type': 'str'},
                                        'ip6-address': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                        'ip6-allowaccess': {
                                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                            'type': 'list',
                                            'choices': ['https', 'ping', 'ssh', 'snmp', 'http', 'telnet', 'fgfm', 'capwap', 'fabric'],
                                            'elements': 'str'
                                        },
                                        'ip6-default-life': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                        'ip6-delegated-prefix-list': {
                                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                            'type': 'list',
                                            'options': {
                                                'autonomous-flag': {
                                                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                                    'choices': ['disable', 'enable'],
                                                    'type': 'str'
                                                },
                                                'onlink-flag': {
                                                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                                    'choices': ['disable', 'enable'],
                                                    'type': 'str'
                                                },
                                                'prefix-id': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                                'rdnss': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'raw'},
                                                'rdnss-service': {
                                                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                                    'choices': ['delegated', 'default', 'specify'],
                                                    'type': 'str'
                                                },
                                                'subnet': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                                'upstream-interface': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                                'delegated-prefix-iaid': {'v_range': [['7.0.2', '']], 'type': 'int'}
                                            },
                                            'elements': 'dict'
                                        },
                                        'ip6-dns-server-override': {
                                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                            'choices': ['disable', 'enable'],
                                            'type': 'str'
                                        },
                                        'ip6-extra-addr': {
                                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                            'type': 'list',
                                            'options': {'prefix': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'}},
                                            'elements': 'dict'
                                        },
                                        'ip6-hop-limit': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                        'ip6-link-mtu': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                        'ip6-manage-flag': {
                                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                            'choices': ['disable', 'enable'],
                                            'type': 'str'
                                        },
                                        'ip6-max-interval': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                        'ip6-min-interval': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                        'ip6-mode': {
                                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                            'choices': ['static', 'dhcp', 'pppoe', 'delegated'],
                                            'type': 'str'
                                        },
                                        'ip6-other-flag': {
                                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                            'choices': ['disable', 'enable'],
                                            'type': 'str'
                                        },
                                        'ip6-prefix-list': {
                                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                            'type': 'list',
                                            'options': {
                                                'autonomous-flag': {
                                                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                                    'choices': ['disable', 'enable'],
                                                    'type': 'str'
                                                },
                                                'dnssl': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'raw'},
                                                'onlink-flag': {
                                                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                                    'choices': ['disable', 'enable'],
                                                    'type': 'str'
                                                },
                                                'preferred-life-time': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                                'prefix': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                                'rdnss': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'raw'},
                                                'valid-life-time': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'}
                                            },
                                            'elements': 'dict'
                                        },
                                        'ip6-reachable-time': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                        'ip6-retrans-time': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                        'ip6-send-adv': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                        'ip6-subnet': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                        'ip6-upstream-interface': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                        'nd-cert': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                        'nd-cga-modifier': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                        'nd-mode': {
                                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                            'choices': ['basic', 'SEND-compatible'],
                                            'type': 'str'
                                        },
                                        'nd-security-level': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                        'nd-timestamp-delta': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                        'nd-timestamp-fuzz': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                        'unique-autoconf-addr': {'v_range': [['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                        'vrip6_link_local': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                        'vrrp-virtual-mac6': {
                                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                            'choices': ['disable', 'enable'],
                                            'type': 'str'
                                        },
                                        'vrrp6': {
                                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                            'type': 'list',
                                            'options': {
                                                'accept-mode': {
                                                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                                    'choices': ['disable', 'enable'],
                                                    'type': 'str'
                                                },
                                                'adv-interval': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                                'preempt': {
                                                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                                    'choices': ['disable', 'enable'],
                                                    'type': 'str'
                                                },
                                                'priority': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                                'start-time': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                                'status': {
                                                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                                    'choices': ['disable', 'enable'],
                                                    'type': 'str'
                                                },
                                                'vrdst6': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                                'vrgrp': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                                'vrid': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                                'vrip6': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                                'ignore-default-route': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                                'vrdst-priority': {'v_range': [['7.6.0', '']], 'type': 'int'}
                                            },
                                            'elements': 'dict'
                                        },
                                        'cli-conn6-status': {'v_range': [['7.0.0', '']], 'type': 'int'},
                                        'ip6-prefix-mode': {'v_range': [['7.0.0', '']], 'choices': ['dhcp6', 'ra'], 'type': 'str'},
                                        'ra-send-mtu': {'v_range': [['6.4.6', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                        'ip6-delegated-prefix-iaid': {'v_range': [['7.0.2', '']], 'type': 'int'},
                                        'dhcp6-relay-source-interface': {'v_range': [['7.2.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                        'dhcp6-relay-interface-id': {'v_range': [['7.4.1', '']], 'type': 'str'},
                                        'dhcp6-relay-source-ip': {'v_range': [['7.4.1', '']], 'type': 'str'}
                                    }
                                },
                                'secondary-IP': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'secondaryip': {
                                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                    'type': 'list',
                                    'options': {
                                        'allowaccess': {
                                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                            'type': 'list',
                                            'choices': [
                                                'https', 'ping', 'ssh', 'snmp', 'http', 'telnet', 'fgfm', 'auto-ipsec', 'radius-acct', 'probe-response',
                                                'capwap', 'dnp', 'ftm', 'fabric', 'speed-test', 'icond', 'scim'
                                            ],
                                            'elements': 'str'
                                        },
                                        'detectprotocol': {
                                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '7.2.0']],
                                            'type': 'list',
                                            'choices': ['ping', 'tcp-echo', 'udp-echo'],
                                            'elements': 'str'
                                        },
                                        'detectserver': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '7.2.0']], 'type': 'str'},
                                        'gwdetect': {
                                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '7.2.0']],
                                            'choices': ['disable', 'enable'],
                                            'type': 'str'
                                        },
                                        'ha-priority': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '7.2.0']], 'type': 'int'},
                                        'id': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                        'ip': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                        'ping-serv-status': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '7.2.0']], 'type': 'int'},
                                        'seq': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                        'secip-relay-ip': {'v_range': [['7.4.0', '']], 'type': 'str'}
                                    },
                                    'elements': 'dict'
                                },
                                'vlanid': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                'dhcp-relay-interface-select-method': {
                                    'v_range': [['6.4.8', '6.4.14'], ['7.0.4', '']],
                                    'choices': ['auto', 'sdwan', 'specify'],
                                    'type': 'str'
                                },
                                'vrrp': {
                                    'v_range': [['7.4.0', '']],
                                    'type': 'list',
                                    'options': {
                                        'accept-mode': {'v_range': [['7.4.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                        'adv-interval': {'v_range': [['7.4.0', '']], 'type': 'int'},
                                        'ignore-default-route': {'v_range': [['7.4.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                        'preempt': {'v_range': [['7.4.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                        'priority': {'v_range': [['7.4.0', '']], 'type': 'int'},
                                        'proxy-arp': {
                                            'v_range': [['7.4.0', '']],
                                            'type': 'list',
                                            'options': {
                                                'id': {'v_range': [['7.4.0', '']], 'type': 'int'},
                                                'ip': {'v_range': [['7.4.0', '']], 'type': 'str'}
                                            },
                                            'elements': 'dict'
                                        },
                                        'start-time': {'v_range': [['7.4.0', '']], 'type': 'int'},
                                        'status': {'v_range': [['7.4.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                        'version': {'v_range': [['7.4.0', '']], 'choices': ['2', '3'], 'type': 'str'},
                                        'vrdst': {'v_range': [['7.4.0', '']], 'type': 'raw'},
                                        'vrdst-priority': {'v_range': [['7.4.0', '']], 'type': 'int'},
                                        'vrgrp': {'v_range': [['7.4.0', '']], 'type': 'int'},
                                        'vrid': {'v_range': [['7.4.0', '']], 'type': 'int'},
                                        'vrip': {'v_range': [['7.4.0', '']], 'type': 'str'}
                                    },
                                    'elements': 'dict'
                                }
                            }
                        }
                    },
                    'elements': 'dict'
                },
                'name': {'required': True, 'type': 'str'},
                'portal-message-override-group': {'v_range': [['6.0.0', '6.2.1']], 'type': 'str'},
                'radius-server': {'v_range': [['6.0.0', '6.2.1']], 'type': 'str'},
                'security': {'v_range': [['6.0.0', '6.2.1']], 'choices': ['open', 'captive-portal', '8021x'], 'type': 'str'},
                'selected-usergroups': {'v_range': [['6.0.0', '6.2.1']], 'type': 'str'},
                'usergroup': {'v_range': [['6.0.0', '6.2.1']], 'type': 'str'},
                'vdom': {'type': 'str'},
                'vlanid': {'type': 'int'},
                'dhcp-server': {
                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                    'type': 'dict',
                    'options': {
                        'auto-configuration': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'auto-managed-status': {'v_range': [['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'conflicted-ip-timeout': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'ddns-auth': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'tsig'], 'type': 'str'},
                        'ddns-key': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'no_log': True, 'type': 'raw'},
                        'ddns-keyname': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'no_log': True, 'type': 'str'},
                        'ddns-server-ip': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'ddns-ttl': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'ddns-update': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'ddns-update-override': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'ddns-zone': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'default-gateway': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'dhcp-settings-from-fortiipam': {'v_range': [['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'dns-server1': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'dns-server2': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'dns-server3': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'dns-server4': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'dns-service': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['default', 'specify', 'local'], 'type': 'str'},
                        'domain': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'enable': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'exclude-range': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'type': 'list',
                            'options': {
                                'end-ip': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'id': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                'start-ip': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'vci-match': {'v_range': [['7.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'vci-string': {'v_range': [['7.2.1', '']], 'type': 'raw'},
                                'lease-time': {'v_range': [['7.2.2', '']], 'type': 'int'},
                                'uci-match': {'v_range': [['7.2.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'uci-string': {'v_range': [['7.2.2', '']], 'type': 'raw'}
                            },
                            'elements': 'dict'
                        },
                        'filename': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'forticlient-on-net-status': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'id': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'ip-mode': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['range', 'usrgrp'], 'type': 'str'},
                        'ip-range': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'type': 'list',
                            'options': {
                                'end-ip': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'id': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                'start-ip': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'vci-match': {'v_range': [['7.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'vci-string': {'v_range': [['7.2.1', '']], 'type': 'raw'},
                                'lease-time': {'v_range': [['7.2.2', '']], 'type': 'int'},
                                'uci-match': {'v_range': [['7.2.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'uci-string': {'v_range': [['7.2.2', '']], 'type': 'raw'}
                            },
                            'elements': 'dict'
                        },
                        'ipsec-lease-hold': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'lease-time': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'mac-acl-default-action': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['assign', 'block'], 'type': 'str'},
                        'netmask': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'next-server': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'ntp-server1': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'ntp-server2': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'ntp-server3': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'ntp-service': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['default', 'specify', 'local'], 'type': 'str'},
                        'option1': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'raw'},
                        'option2': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'raw'},
                        'option3': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'raw'},
                        'option4': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'option5': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'option6': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'options': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'type': 'list',
                            'options': {
                                'code': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                'id': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                'ip': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'raw'},
                                'type': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['hex', 'string', 'ip', 'fqdn'], 'type': 'str'},
                                'value': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'vci-match': {'v_range': [['7.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'vci-string': {'v_range': [['7.2.1', '']], 'type': 'raw'},
                                'uci-match': {'v_range': [['7.2.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'uci-string': {'v_range': [['7.2.2', '']], 'type': 'raw'}
                            },
                            'elements': 'dict'
                        },
                        'reserved-address': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'type': 'list',
                            'options': {
                                'action': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['assign', 'block', 'reserved'], 'type': 'str'},
                                'circuit-id': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'circuit-id-type': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['hex', 'string'], 'type': 'str'},
                                'description': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'id': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                'ip': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'mac': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'remote-id': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'remote-id-type': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['hex', 'string'], 'type': 'str'},
                                'type': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['mac', 'option82'], 'type': 'str'}
                            },
                            'elements': 'dict'
                        },
                        'server-type': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['regular', 'ipsec'], 'type': 'str'},
                        'status': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'tftp-server': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'raw'},
                        'timezone': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': [
                                '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
                                '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39',
                                '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59',
                                '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79',
                                '80', '81', '82', '83', '84', '85', '86', '87'
                            ],
                            'type': 'str'
                        },
                        'timezone-option': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'default', 'specify'], 'type': 'str'},
                        'vci-match': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'vci-string': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'raw'},
                        'wifi-ac-service': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['specify', 'local'], 'type': 'str'},
                        'wifi-ac1': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'wifi-ac2': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'wifi-ac3': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'wins-server1': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'wins-server2': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'relay-agent': {'v_range': [['7.4.0', '']], 'type': 'str'},
                        'shared-subnet': {'v_range': [['7.4.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'}
                    }
                },
                'interface': {
                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                    'type': 'dict',
                    'options': {
                        'ac-name': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'aggregate': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'algorithm': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['L2', 'L3', 'L4', 'LB', 'Source-MAC'], 'type': 'str'},
                        'alias': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'allowaccess': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'type': 'list',
                            'choices': [
                                'https', 'ping', 'ssh', 'snmp', 'http', 'telnet', 'fgfm', 'auto-ipsec', 'radius-acct', 'probe-response', 'capwap', 'dnp',
                                'ftm', 'fabric', 'speed-test'
                            ],
                            'elements': 'str'
                        },
                        'ap-discover': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'arpforward': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'atm-protocol': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['none', 'ipoa'], 'type': 'str'},
                        'auth-type': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['auto', 'pap', 'chap', 'mschapv1', 'mschapv2'],
                            'type': 'str'
                        },
                        'auto-auth-extension-device': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'bandwidth-measure-time': {'v_range': [['6.4.5', '']], 'type': 'int'},
                        'bfd': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['global', 'enable', 'disable'], 'type': 'str'},
                        'bfd-desired-min-tx': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'bfd-detect-mult': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'bfd-required-min-rx': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'broadcast-forticlient-discovery': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['disable', 'enable'],
                            'type': 'str'
                        },
                        'broadcast-forward': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'captive-portal': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'cli-conn-status': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'color': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'ddns': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'ddns-auth': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'tsig'], 'type': 'str'},
                        'ddns-domain': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'ddns-key': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'no_log': True, 'type': 'raw'},
                        'ddns-keyname': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'no_log': True, 'type': 'str'},
                        'ddns-password': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'no_log': True, 'type': 'raw'},
                        'ddns-server': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': [
                                'dhs.org', 'dyndns.org', 'dyns.net', 'tzo.com', 'ods.org', 'vavic.com', 'now.net.cn', 'dipdns.net', 'easydns.com',
                                'genericDDNS'
                            ],
                            'type': 'str'
                        },
                        'ddns-server-ip': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'ddns-sn': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'ddns-ttl': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'ddns-username': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'ddns-zone': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'dedicated-to': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['none', 'management'], 'type': 'str'},
                        'defaultgw': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'description': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'detected-peer-mtu': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'detectprotocol': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'type': 'list',
                            'choices': ['ping', 'tcp-echo', 'udp-echo'],
                            'elements': 'str'
                        },
                        'detectserver': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'device-access-list': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'raw'},
                        'device-identification': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'device-identification-active-scan': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['disable', 'enable'],
                            'type': 'str'
                        },
                        'device-netscan': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'device-user-identification': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'devindex': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'dhcp-client-identifier': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'dhcp-relay-agent-option': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'dhcp-relay-interface': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'dhcp-relay-interface-select-method': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['auto', 'sdwan', 'specify'],
                            'type': 'str'
                        },
                        'dhcp-relay-ip': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'raw'},
                        'dhcp-relay-service': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'dhcp-relay-type': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['regular', 'ipsec'], 'type': 'str'},
                        'dhcp-renew-time': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'disc-retry-timeout': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'disconnect-threshold': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'distance': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'dns-query': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['disable', 'recursive', 'non-recursive'],
                            'type': 'str'
                        },
                        'dns-server-override': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'drop-fragment': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'drop-overlapped-fragment': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'egress-cos': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['disable', 'cos0', 'cos1', 'cos2', 'cos3', 'cos4', 'cos5', 'cos6', 'cos7'],
                            'type': 'str'
                        },
                        'egress-shaping-profile': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'eip': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'endpoint-compliance': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'estimated-downstream-bandwidth': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'estimated-upstream-bandwidth': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'explicit-ftp-proxy': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'explicit-web-proxy': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'external': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'fail-action-on-extender': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['soft-restart', 'hard-restart', 'reboot'],
                            'type': 'str'
                        },
                        'fail-alert-interfaces': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'raw'},
                        'fail-alert-method': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['link-failed-signal', 'link-down'],
                            'type': 'str'
                        },
                        'fail-detect': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'fail-detect-option': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'type': 'list',
                            'choices': ['detectserver', 'link-down'],
                            'elements': 'str'
                        },
                        'fdp': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'fortiheartbeat': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'fortilink': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'fortilink-backup-link': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'fortilink-neighbor-detect': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['lldp', 'fortilink'], 'type': 'str'},
                        'fortilink-split-interface': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'fortilink-stacking': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'forward-domain': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'forward-error-correction': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': [
                                'disable', 'enable', 'rs-fec', 'base-r-fec', 'fec-cl91', 'fec-cl74', 'rs-544', 'none', 'cl91-rs-fec', 'cl74-fc-fec',
                                'auto'
                            ],
                            'type': 'str'
                        },
                        'fp-anomaly': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'type': 'list',
                            'choices': [
                                'drop_tcp_fin_noack', 'pass_winnuke', 'pass_tcpland', 'pass_udpland', 'pass_icmpland', 'pass_ipland', 'pass_iprr',
                                'pass_ipssrr', 'pass_iplsrr', 'pass_ipstream', 'pass_ipsecurity', 'pass_iptimestamp', 'pass_ipunknown_option',
                                'pass_ipunknown_prot', 'pass_icmp_frag', 'pass_tcp_no_flag', 'pass_tcp_fin_noack', 'drop_winnuke', 'drop_tcpland',
                                'drop_udpland', 'drop_icmpland', 'drop_ipland', 'drop_iprr', 'drop_ipssrr', 'drop_iplsrr', 'drop_ipstream',
                                'drop_ipsecurity', 'drop_iptimestamp', 'drop_ipunknown_option', 'drop_ipunknown_prot', 'drop_icmp_frag',
                                'drop_tcp_no_flag'
                            ],
                            'elements': 'str'
                        },
                        'fp-disable': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'type': 'list',
                            'choices': ['all', 'ipsec', 'none'],
                            'elements': 'str'
                        },
                        'gateway-address': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'gi-gk': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'gwaddr': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '7.2.0']], 'type': 'str'},
                        'gwdetect': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'ha-priority': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'icmp-accept-redirect': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'icmp-redirect': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'icmp-send-redirect': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'ident-accept': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'idle-timeout': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'if-mdix': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['auto', 'normal', 'crossover'], 'type': 'str'},
                        'if-media': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['auto', 'copper', 'fiber'], 'type': 'str'},
                        'in-force-vlan-cos': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'inbandwidth': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'ingress-cos': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['disable', 'cos0', 'cos1', 'cos2', 'cos3', 'cos4', 'cos5', 'cos6', 'cos7'],
                            'type': 'str'
                        },
                        'ingress-shaping-profile': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'ingress-spillover-threshold': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'internal': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'ip': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'ip-managed-by-fortiipam': {'v_range': [['6.4.5', '']], 'choices': ['disable', 'enable', 'inherit-global'], 'type': 'str'},
                        'ipmac': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'ips-sniffer-mode': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'ipunnumbered': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'ipv6': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'type': 'dict',
                            'options': {
                                'autoconf': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'dhcp6-client-options': {
                                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                    'type': 'list',
                                    'choices': ['rapid', 'iapd', 'iana', 'dns', 'dnsname'],
                                    'elements': 'str'
                                },
                                'dhcp6-information-request': {
                                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                    'choices': ['disable', 'enable'],
                                    'type': 'str'
                                },
                                'dhcp6-prefix-delegation': {
                                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                    'choices': ['disable', 'enable'],
                                    'type': 'str'
                                },
                                'dhcp6-prefix-hint': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'dhcp6-prefix-hint-plt': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                'dhcp6-prefix-hint-vlt': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                'dhcp6-relay-ip': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'dhcp6-relay-service': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'dhcp6-relay-type': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['regular'], 'type': 'str'},
                                'icmp6-send-redirect': {'v_range': [['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'interface-identifier': {'v_range': [['6.4.5', '']], 'type': 'str'},
                                'ip6-address': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'ip6-allowaccess': {
                                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                    'type': 'list',
                                    'choices': ['https', 'ping', 'ssh', 'snmp', 'http', 'telnet', 'fgfm', 'capwap', 'fabric'],
                                    'elements': 'str'
                                },
                                'ip6-default-life': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                'ip6-delegated-prefix-list': {
                                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                    'type': 'list',
                                    'options': {
                                        'autonomous-flag': {
                                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                            'choices': ['disable', 'enable'],
                                            'type': 'str'
                                        },
                                        'onlink-flag': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                        'prefix-id': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                        'rdnss': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'raw'},
                                        'rdnss-service': {
                                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                            'choices': ['delegated', 'default', 'specify'],
                                            'type': 'str'
                                        },
                                        'subnet': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                        'upstream-interface': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                        'delegated-prefix-iaid': {'v_range': [['7.0.2', '']], 'type': 'int'}
                                    },
                                    'elements': 'dict'
                                },
                                'ip6-dns-server-override': {
                                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                    'choices': ['disable', 'enable'],
                                    'type': 'str'
                                },
                                'ip6-extra-addr': {
                                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                    'type': 'list',
                                    'options': {'prefix': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'}},
                                    'elements': 'dict'
                                },
                                'ip6-hop-limit': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                'ip6-link-mtu': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                'ip6-manage-flag': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'ip6-max-interval': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                'ip6-min-interval': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                'ip6-mode': {
                                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                    'choices': ['static', 'dhcp', 'pppoe', 'delegated'],
                                    'type': 'str'
                                },
                                'ip6-other-flag': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'ip6-prefix-list': {
                                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                    'type': 'list',
                                    'options': {
                                        'autonomous-flag': {
                                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                            'choices': ['disable', 'enable'],
                                            'type': 'str'
                                        },
                                        'dnssl': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'raw'},
                                        'onlink-flag': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                        'preferred-life-time': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                        'prefix': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                        'rdnss': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'raw'},
                                        'valid-life-time': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'}
                                    },
                                    'elements': 'dict'
                                },
                                'ip6-reachable-time': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                'ip6-retrans-time': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                'ip6-send-adv': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'ip6-subnet': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'ip6-upstream-interface': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'nd-cert': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'nd-cga-modifier': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'nd-mode': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['basic', 'SEND-compatible'], 'type': 'str'},
                                'nd-security-level': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                'nd-timestamp-delta': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                'nd-timestamp-fuzz': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                'unique-autoconf-addr': {'v_range': [['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'vrip6_link_local': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'vrrp-virtual-mac6': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'vrrp6': {
                                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                    'type': 'list',
                                    'options': {
                                        'accept-mode': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                        'adv-interval': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                        'preempt': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                        'priority': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                        'start-time': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                        'status': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                        'vrdst6': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                        'vrgrp': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                        'vrid': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                        'vrip6': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                        'ignore-default-route': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                        'vrdst-priority': {'v_range': [['7.6.0', '']], 'type': 'int'}
                                    },
                                    'elements': 'dict'
                                },
                                'cli-conn6-status': {'v_range': [['7.0.0', '']], 'type': 'int'},
                                'ip6-prefix-mode': {'v_range': [['7.0.0', '']], 'choices': ['dhcp6', 'ra'], 'type': 'str'},
                                'ra-send-mtu': {'v_range': [['6.4.6', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'ip6-delegated-prefix-iaid': {'v_range': [['7.0.2', '']], 'type': 'int'},
                                'dhcp6-relay-source-interface': {'v_range': [['7.2.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'dhcp6-relay-interface-id': {'v_range': [['7.4.1', '']], 'type': 'str'},
                                'dhcp6-relay-source-ip': {'v_range': [['7.4.1', '']], 'type': 'str'}
                            }
                        },
                        'l2forward': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'l2tp-client': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'lacp-ha-slave': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'lacp-mode': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['static', 'passive', 'active'], 'type': 'str'},
                        'lacp-speed': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['slow', 'fast'], 'type': 'str'},
                        'lcp-echo-interval': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'lcp-max-echo-fails': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'link-up-delay': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'listen-forticlient-connection': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['disable', 'enable'],
                            'type': 'str'
                        },
                        'lldp-network-policy': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'lldp-reception': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable', 'vdom'], 'type': 'str'},
                        'lldp-transmission': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['enable', 'disable', 'vdom'], 'type': 'str'},
                        'log': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'macaddr': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'managed-subnetwork-size': {
                            'v_range': [['6.4.5', '']],
                            'choices': ['256', '512', '1024', '2048', '4096', '8192', '16384', '32768', '65536', '32', '64', '128'],
                            'type': 'str'
                        },
                        'management-ip': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'max-egress-burst-rate': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'max-egress-rate': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'measured-downstream-bandwidth': {'v_range': [['6.4.5', '']], 'type': 'int'},
                        'measured-upstream-bandwidth': {'v_range': [['6.4.5', '']], 'type': 'int'},
                        'mediatype': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': [
                                'serdes-sfp', 'sgmii-sfp', 'cfp2-sr10', 'cfp2-lr4', 'serdes-copper-sfp', 'sr', 'cr', 'lr', 'qsfp28-sr4', 'qsfp28-lr4',
                                'qsfp28-cr4', 'sr4', 'cr4', 'lr4', 'none', 'gmii', 'sgmii', 'sr2', 'lr2', 'cr2', 'sr8', 'lr8', 'cr8'
                            ],
                            'type': 'str'
                        },
                        'member': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'raw'},
                        'min-links': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'min-links-down': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['operational', 'administrative'], 'type': 'str'},
                        'mode': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['static', 'dhcp', 'pppoe', 'pppoa', 'ipoa', 'eoa'],
                            'type': 'str'
                        },
                        'monitor-bandwidth': {'v_range': [['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'mtu': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'mtu-override': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'mux-type': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['llc-encaps', 'vc-encaps'], 'type': 'str'},
                        'name': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'ndiscforward': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'netbios-forward': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'netflow-sampler': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'tx', 'rx', 'both'], 'type': 'str'},
                        'np-qos-profile': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'npu-fastpath': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'nst': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'out-force-vlan-cos': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'outbandwidth': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'padt-retry-timeout': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'password': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'no_log': True, 'type': 'raw'},
                        'peer-interface': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'raw'},
                        'phy-mode': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': [
                                'auto', 'adsl', 'vdsl', 'adsl-auto', 'vdsl2', 'adsl2+', 'adsl2', 'g.dmt', 't1.413', 'g.lite', 'g-dmt', 't1-413',
                                'g-lite'
                            ],
                            'type': 'str'
                        },
                        'ping-serv-status': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '7.2.0']], 'type': 'int'},
                        'poe': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'polling-interval': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'pppoe-unnumbered-negotiate': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'pptp-auth-type': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['auto', 'pap', 'chap', 'mschapv1', 'mschapv2'],
                            'type': 'str'
                        },
                        'pptp-client': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'pptp-password': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'no_log': True, 'type': 'raw'},
                        'pptp-server-ip': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'pptp-timeout': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'pptp-user': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'preserve-session-route': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'priority': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'priority-override': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'proxy-captive-portal': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'redundant-interface': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'remote-ip': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'replacemsg-override-group': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'retransmission': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'ring-rx': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'ring-tx': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'role': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['lan', 'wan', 'dmz', 'undefined'], 'type': 'str'},
                        'sample-direction': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['rx', 'tx', 'both'], 'type': 'str'},
                        'sample-rate': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'scan-botnet-connections': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['disable', 'block', 'monitor'],
                            'type': 'str'
                        },
                        'secondary-IP': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'secondaryip': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'type': 'list',
                            'options': {
                                'allowaccess': {
                                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                                    'type': 'list',
                                    'choices': [
                                        'https', 'ping', 'ssh', 'snmp', 'http', 'telnet', 'fgfm', 'auto-ipsec', 'radius-acct', 'probe-response',
                                        'capwap', 'dnp', 'ftm', 'fabric', 'speed-test', 'icond', 'scim'
                                    ],
                                    'elements': 'str'
                                },
                                'detectprotocol': {
                                    'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '7.2.0']],
                                    'type': 'list',
                                    'choices': ['ping', 'tcp-echo', 'udp-echo'],
                                    'elements': 'str'
                                },
                                'detectserver': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '7.2.0']], 'type': 'str'},
                                'gwdetect': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '7.2.0']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'ha-priority': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '7.2.0']], 'type': 'int'},
                                'id': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                'ip': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'ping-serv-status': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '7.2.0']], 'type': 'int'},
                                'seq': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                'secip-relay-ip': {'v_range': [['7.4.0', '']], 'type': 'str'}
                            },
                            'elements': 'dict'
                        },
                        'security-8021x-dynamic-vlan-id': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'security-8021x-master': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'security-8021x-mode': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['default', 'dynamic-vlan', 'fallback', 'slave'],
                            'type': 'str'
                        },
                        'security-exempt-list': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'security-external-logout': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'security-external-web': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'security-groups': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'raw'},
                        'security-mac-auth-bypass': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['disable', 'enable', 'mac-auth-only'],
                            'type': 'str'
                        },
                        'security-mode': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['none', 'captive-portal', '802.1X'], 'type': 'str'},
                        'security-redirect-url': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'service-name': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'sflow-sampler': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'speed': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': [
                                'auto', '10full', '10half', '100full', '100half', '1000full', '1000half', '10000full', '1000auto', '10000auto',
                                '40000full', '100Gfull', '25000full', '40000auto', '25000auto', '100Gauto', '400Gfull', '400Gauto', '50000full',
                                '2500auto', '5000auto', '50000auto', '200Gfull', '200Gauto', '100auto'
                            ],
                            'type': 'str'
                        },
                        'spillover-threshold': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'src-check': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'status': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['down', 'up'], 'type': 'str'},
                        'stp': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'stp-ha-slave': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['disable', 'enable', 'priority-adjust'],
                            'type': 'str'
                        },
                        'stpforward': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'stpforward-mode': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['rpl-all-ext-id', 'rpl-bridge-ext-id', 'rpl-nothing'],
                            'type': 'str'
                        },
                        'strip-priority-vlan-tag': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'subst': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'substitute-dst-mac': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'swc-first-create': {'v_range': [['6.4.5', '']], 'type': 'int'},
                        'swc-vlan': {'v_range': [['6.4.5', '']], 'type': 'int'},
                        'switch': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'switch-controller-access-vlan': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['disable', 'enable'],
                            'type': 'str'
                        },
                        'switch-controller-arp-inspection': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['disable', 'enable', 'monitor'],
                            'type': 'str'
                        },
                        'switch-controller-auth': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['radius', 'usergroup'], 'type': 'str'},
                        'switch-controller-dhcp-snooping': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['disable', 'enable'],
                            'type': 'str'
                        },
                        'switch-controller-dhcp-snooping-option82': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['disable', 'enable'],
                            'type': 'str'
                        },
                        'switch-controller-dhcp-snooping-verify-mac': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['disable', 'enable'],
                            'type': 'str'
                        },
                        'switch-controller-feature': {
                            'v_range': [['6.4.5', '']],
                            'choices': ['none', 'default-vlan', 'quarantine', 'sniffer', 'voice', 'camera', 'rspan', 'video', 'nac', 'nac-segment'],
                            'type': 'str'
                        },
                        'switch-controller-igmp-snooping': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['disable', 'enable'],
                            'type': 'str'
                        },
                        'switch-controller-igmp-snooping-fast-leave': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['disable', 'enable'],
                            'type': 'str'
                        },
                        'switch-controller-igmp-snooping-proxy': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': ['disable', 'enable'],
                            'type': 'str'
                        },
                        'switch-controller-iot-scanning': {'v_range': [['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'switch-controller-learning-limit': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'switch-controller-mgmt-vlan': {'v_range': [['6.4.5', '']], 'type': 'int'},
                        'switch-controller-nac': {'v_range': [['6.4.5', '']], 'type': 'str'},
                        'switch-controller-radius-server': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'switch-controller-rspan-mode': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'switch-controller-source-ip': {'v_range': [['6.4.5', '']], 'choices': ['outbound', 'fixed'], 'type': 'str'},
                        'switch-controller-traffic-policy': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'tc-mode': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['ptm', 'atm'], 'type': 'str'},
                        'tcp-mss': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'trunk': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'trust-ip-1': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'trust-ip-2': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'trust-ip-3': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'trust-ip6-1': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'trust-ip6-2': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'trust-ip6-3': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'type': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': [
                                'physical', 'vlan', 'aggregate', 'redundant', 'tunnel', 'wireless', 'vdom-link', 'loopback', 'switch', 'hard-switch',
                                'hdlc', 'vap-switch', 'wl-mesh', 'fortilink', 'switch-vlan', 'fctrl-trunk', 'tdm', 'fext-wan', 'vxlan', 'emac-vlan',
                                'geneve', 'ssl', 'lan-extension'
                            ],
                            'type': 'str'
                        },
                        'username': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'vci': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'vectoring': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'vindex': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'vlan-protocol': {'v_range': [['6.4.5', '']], 'choices': ['8021q', '8021ad'], 'type': 'str'},
                        'vlanforward': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'vlanid': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'vpi': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'vrf': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'vrrp': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'type': 'list',
                            'options': {
                                'accept-mode': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'adv-interval': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                'ignore-default-route': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'preempt': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'priority': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                'start-time': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                'status': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                                'version': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['2', '3'], 'type': 'str'},
                                'vrdst': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'raw'},
                                'vrdst-priority': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                'vrgrp': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                'vrid': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                                'vrip': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                                'proxy-arp': {
                                    'v_range': [['7.4.0', '']],
                                    'type': 'list',
                                    'options': {'id': {'v_range': [['7.4.0', '']], 'type': 'int'}, 'ip': {'v_range': [['7.4.0', '']], 'type': 'str'}},
                                    'elements': 'dict'
                                }
                            },
                            'elements': 'dict'
                        },
                        'vrrp-virtual-mac': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'wccp': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'weight': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'wifi-5g-threshold': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'wifi-acl': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['deny', 'allow'], 'type': 'str'},
                        'wifi-ap-band': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['any', '5g-preferred', '5g-only'], 'type': 'str'},
                        'wifi-auth': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['PSK', 'RADIUS', 'radius', 'usergroup'], 'type': 'str'},
                        'wifi-auto-connect': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'wifi-auto-save': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'wifi-broadcast-ssid': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'wifi-encrypt': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['TKIP', 'AES'], 'type': 'str'},
                        'wifi-fragment-threshold': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'wifi-key': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'no_log': True, 'type': 'raw'},
                        'wifi-keyindex': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'no_log': True, 'type': 'int'},
                        'wifi-mac-filter': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'wifi-passphrase': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'no_log': True, 'type': 'raw'},
                        'wifi-radius-server': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'wifi-rts-threshold': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'int'},
                        'wifi-security': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']],
                            'choices': [
                                'None', 'WEP64', 'wep64', 'WEP128', 'wep128', 'WPA_PSK', 'WPA_RADIUS', 'WPA', 'WPA2', 'WPA2_AUTO', 'open',
                                'wpa-personal', 'wpa-enterprise', 'wpa-only-personal', 'wpa-only-enterprise', 'wpa2-only-personal',
                                'wpa2-only-enterprise'
                            ],
                            'type': 'str'
                        },
                        'wifi-ssid': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'wifi-usergroup': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'wins-ip': {'v_range': [['6.2.8', '6.2.12'], ['6.4.5', '']], 'type': 'str'},
                        'dhcp-relay-request-all-server': {
                            'v_range': [['6.2.8', '6.2.12'], ['6.4.6', '']],
                            'choices': ['disable', 'enable'],
                            'type': 'str'
                        },
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
                        'pvc-vlan-rx-op': {
                            'v_range': [['6.4.8', '6.4.14'], ['7.0.2', '']],
                            'choices': ['pass-through', 'replace', 'remove'],
                            'type': 'str'
                        },
                        'pvc-vlan-tx-id': {'v_range': [['6.4.8', '6.4.14'], ['7.0.2', '']], 'type': 'int'},
                        'pvc-vlan-tx-op': {
                            'v_range': [['6.4.8', '6.4.14'], ['7.0.2', '']],
                            'choices': ['pass-through', 'replace', 'remove'],
                            'type': 'str'
                        },
                        'reachable-time': {'v_range': [['7.0.3', '']], 'type': 'int'},
                        'select-profile-30a-35b': {
                            'v_range': [['6.2.9', '6.2.12'], ['6.4.8', '6.4.14'], ['7.0.3', '']],
                            'choices': ['30A', '35B'],
                            'type': 'str'
                        },
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
                        'interconnect-profile': {
                            'v_range': [['7.0.5', '7.0.12'], ['7.2.1', '']],
                            'choices': ['default', 'profile1', 'profile2'],
                            'type': 'str'
                        },
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
                        'default-purdue-level': {
                            'v_range': [['7.4.0', '']],
                            'choices': ['1', '2', '3', '4', '5', '1.5', '2.5', '3.5', '5.5'],
                            'type': 'str'
                        },
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

        }
    }

    module_option_spec = get_module_arg_spec('full crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'fsp_vlan'),
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
