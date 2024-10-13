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
module: fmgr_devprof_system_global
short_description: Configure global attributes.
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
    devprof:
        description: The parameter (devprof) in requested url.
        type: str
        required: true
    devprof_system_global:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            admin-https-redirect:
                type: str
                description: Deprecated, please rename it to admin_https_redirect. Enable/disable redirection of HTTP administration access to HTTPS.
                choices:
                    - 'disable'
                    - 'enable'
            admin-port:
                type: int
                description: Deprecated, please rename it to admin_port. Administrative access port for HTTP.
            admin-scp:
                type: str
                description: Deprecated, please rename it to admin_scp. Enable/disable using SCP to download the system configuration.
                choices:
                    - 'disable'
                    - 'enable'
            admin-sport:
                type: int
                description: Deprecated, please rename it to admin_sport. Administrative access port for HTTPS.
            admin-ssh-port:
                type: int
                description: Deprecated, please rename it to admin_ssh_port. Administrative access port for SSH.
            admin-ssh-v1:
                type: str
                description: Deprecated, please rename it to admin_ssh_v1. Enable/disable SSH v1 compatibility.
                choices:
                    - 'disable'
                    - 'enable'
            admin-telnet-port:
                type: int
                description: Deprecated, please rename it to admin_telnet_port. Administrative access port for TELNET.
            admintimeout:
                type: int
                description: Number of minutes before an idle administrator session times out
            gui-ipv6:
                type: str
                description: Deprecated, please rename it to gui_ipv6. Enable/disable IPv6 settings on the GUI.
                choices:
                    - 'disable'
                    - 'enable'
            gui-lines-per-page:
                type: int
                description: Deprecated, please rename it to gui_lines_per_page. Number of lines to display per page for web administration.
            gui-theme:
                type: str
                description: Deprecated, please rename it to gui_theme. Color scheme for the administration GUI.
                choices:
                    - 'blue'
                    - 'green'
                    - 'melongene'
                    - 'red'
                    - 'mariner'
                    - 'neutrino'
                    - 'jade'
                    - 'graphite'
                    - 'dark-matter'
                    - 'onyx'
                    - 'eclipse'
                    - 'retro'
                    - 'fpx'
                    - 'jet-stream'
                    - 'security-fabric'
            language:
                type: str
                description: GUI display language.
                choices:
                    - 'english'
                    - 'simch'
                    - 'japanese'
                    - 'korean'
                    - 'spanish'
                    - 'trach'
                    - 'french'
                    - 'portuguese'
            switch-controller:
                type: str
                description: Deprecated, please rename it to switch_controller. Enable/disable switch controller feature.
                choices:
                    - 'disable'
                    - 'enable'
            gui-device-latitude:
                type: str
                description:
                    - Deprecated, please rename it to gui_device_latitude.
                    - Support meta variable
                    - Add the latitude of the location of this FortiGate to position it on the Threat Map.
            gui-device-longitude:
                type: str
                description:
                    - Deprecated, please rename it to gui_device_longitude.
                    - Support meta variable
                    - Add the longitude of the location of this FortiGate to position it on the Threat Map.
            hostname:
                type: str
                description:
                    - Support meta variable
                    - FortiGate units hostname.
            timezone:
                type: raw
                description:
                    - (list)
                    - Support meta variable
                    - Timezone database name.
            check-reset-range:
                type: str
                description: Deprecated, please rename it to check_reset_range. Configure ICMP error message verification.
                choices:
                    - 'disable'
                    - 'strict'
            pmtu-discovery:
                type: str
                description: Deprecated, please rename it to pmtu_discovery. Enable/disable path MTU discovery.
                choices:
                    - 'disable'
                    - 'enable'
            gui-allow-incompatible-fabric-fgt:
                type: str
                description: Deprecated, please rename it to gui_allow_incompatible_fabric_fgt. Enable/disable Allow FGT with incompatible firmware to ...
                choices:
                    - 'disable'
                    - 'enable'
            admin-restrict-local:
                type: str
                description: Deprecated, please rename it to admin_restrict_local. Enable/disable local admin authentication restriction when remote au...
                choices:
                    - 'disable'
                    - 'enable'
                    - 'all'
                    - 'non-console-only'
            gui-workflow-management:
                type: str
                description: Deprecated, please rename it to gui_workflow_management. Enable/disable Workflow management features on the GUI.
                choices:
                    - 'disable'
                    - 'enable'
            send-pmtu-icmp:
                type: str
                description: Deprecated, please rename it to send_pmtu_icmp. Enable/disable sending of path maximum transmission unit
                choices:
                    - 'disable'
                    - 'enable'
            tcp-halfclose-timer:
                type: int
                description: Deprecated, please rename it to tcp_halfclose_timer. Number of seconds the FortiGate unit should wait to close a session a...
            admin-server-cert:
                type: raw
                description: (list) Deprecated, please rename it to admin_server_cert. Server certificate that the FortiGate uses for HTTPS administrat...
            dnsproxy-worker-count:
                type: int
                description: Deprecated, please rename it to dnsproxy_worker_count. DNS proxy worker count.
            show-backplane-intf:
                type: str
                description: Deprecated, please rename it to show_backplane_intf. Show/hide backplane interfaces
                choices:
                    - 'disable'
                    - 'enable'
            gui-custom-language:
                type: str
                description: Deprecated, please rename it to gui_custom_language. Enable/disable custom languages in GUI.
                choices:
                    - 'disable'
                    - 'enable'
            ldapconntimeout:
                type: int
                description: Global timeout for connections with remote LDAP servers in milliseconds
            auth-https-port:
                type: int
                description: Deprecated, please rename it to auth_https_port. User authentication HTTPS port.
            revision-backup-on-logout:
                type: str
                description: Deprecated, please rename it to revision_backup_on_logout. Enable/disable back-up of the latest configuration revision whe...
                choices:
                    - 'disable'
                    - 'enable'
            arp-max-entry:
                type: int
                description: Deprecated, please rename it to arp_max_entry. Maximum number of dynamically learned MAC addresses that can be added to th...
            long-vdom-name:
                type: str
                description: Deprecated, please rename it to long_vdom_name. Enable/disable long VDOM name support.
                choices:
                    - 'disable'
                    - 'enable'
            pre-login-banner:
                type: str
                description: Deprecated, please rename it to pre_login_banner. Enable/disable displaying the administrator access disclaimer message on...
                choices:
                    - 'disable'
                    - 'enable'
            qsfpdd-split8-port:
                type: raw
                description: (list) Deprecated, please rename it to qsfpdd_split8_port. Split qsfpddd port
            max-route-cache-size:
                type: int
                description: Deprecated, please rename it to max_route_cache_size. Maximum number of IP route cache entries
            fortitoken-cloud-push-status:
                type: str
                description: Deprecated, please rename it to fortitoken_cloud_push_status. Enable/disable FTM push service of FortiToken Cloud.
                choices:
                    - 'disable'
                    - 'enable'
            ssh-hostkey-override:
                type: str
                description: Deprecated, please rename it to ssh_hostkey_override. Enable/disable SSH host key override in SSH daemon.
                choices:
                    - 'disable'
                    - 'enable'
            proxy-hardware-acceleration:
                type: str
                description: Deprecated, please rename it to proxy_hardware_acceleration. Enable/disable email proxy hardware acceleration.
                choices:
                    - 'disable'
                    - 'enable'
            switch-controller-reserved-network:
                type: raw
                description: (list) Deprecated, please rename it to switch_controller_reserved_network. Configure reserved network subnet for managed s...
            ssd-trim-date:
                type: int
                description: Deprecated, please rename it to ssd_trim_date. Date within a month to run ssd trim.
            wad-worker-count:
                type: int
                description: Deprecated, please rename it to wad_worker_count. Number of explicit proxy WAN optimization daemon
            ssh-hostkey:
                type: str
                description: Deprecated, please rename it to ssh_hostkey. Config SSH host key.
            wireless-controller-port:
                type: int
                description: Deprecated, please rename it to wireless_controller_port. Port used for the control channel in wireless controller mode
            fgd-alert-subscription:
                type: list
                elements: str
                description: Deprecated, please rename it to fgd_alert_subscription. Type of alert to retrieve from FortiGuard.
                choices:
                    - 'advisory'
                    - 'latest-threat'
                    - 'latest-virus'
                    - 'latest-attack'
                    - 'new-antivirus-db'
                    - 'new-attack-db'
            forticontroller-proxy-port:
                type: int
                description: Deprecated, please rename it to forticontroller_proxy_port. FortiController proxy port
            dh-params:
                type: str
                description: Deprecated, please rename it to dh_params. Number of bits to use in the Diffie-Hellman exchange for HTTPS/SSH protocols.
                choices:
                    - '1024'
                    - '1536'
                    - '2048'
                    - '3072'
                    - '4096'
                    - '6144'
                    - '8192'
            memory-use-threshold-green:
                type: int
                description: Deprecated, please rename it to memory_use_threshold_green. Threshold at which memory usage forces the FortiGate to exit c...
            proxy-cert-use-mgmt-vdom:
                type: str
                description: Deprecated, please rename it to proxy_cert_use_mgmt_vdom. Enable/disable using management VDOM to send requests.
                choices:
                    - 'disable'
                    - 'enable'
            proxy-auth-lifetime-timeout:
                type: int
                description: Deprecated, please rename it to proxy_auth_lifetime_timeout. Lifetime timeout in minutes for authenticated users
            gui-auto-upgrade-setup-warning:
                type: str
                description: Deprecated, please rename it to gui_auto_upgrade_setup_warning. Enable/disable the automatic patch upgrade setup prompt on...
                choices:
                    - 'disable'
                    - 'enable'
            gui-cdn-usage:
                type: str
                description: Deprecated, please rename it to gui_cdn_usage. Enable/disable Load GUI static files from a CDN.
                choices:
                    - 'disable'
                    - 'enable'
            two-factor-email-expiry:
                type: int
                description: Deprecated, please rename it to two_factor_email_expiry. Email-based two-factor authentication session timeout
            udp-idle-timer:
                type: int
                description: Deprecated, please rename it to udp_idle_timer. UDP connection session timeout.
            interface-subnet-usage:
                type: str
                description: Deprecated, please rename it to interface_subnet_usage. Enable/disable allowing use of interface-subnet setting in firewal...
                choices:
                    - 'disable'
                    - 'enable'
            forticontroller-proxy:
                type: str
                description: Deprecated, please rename it to forticontroller_proxy. Enable/disable FortiController proxy.
                choices:
                    - 'disable'
                    - 'enable'
            ssh-enc-algo:
                type: list
                elements: str
                description: Deprecated, please rename it to ssh_enc_algo. Select one or more SSH ciphers.
                choices:
                    - 'chacha20-poly1305@openssh.com'
                    - 'aes128-ctr'
                    - 'aes192-ctr'
                    - 'aes256-ctr'
                    - 'arcfour256'
                    - 'arcfour128'
                    - 'aes128-cbc'
                    - '3des-cbc'
                    - 'blowfish-cbc'
                    - 'cast128-cbc'
                    - 'aes192-cbc'
                    - 'aes256-cbc'
                    - 'arcfour'
                    - 'rijndael-cbc@lysator.liu.se'
                    - 'aes128-gcm@openssh.com'
                    - 'aes256-gcm@openssh.com'
            block-session-timer:
                type: int
                description: Deprecated, please rename it to block_session_timer. Duration in seconds for blocked sessions
            quic-pmtud:
                type: str
                description: Deprecated, please rename it to quic_pmtud. Enable/disable path MTU discovery
                choices:
                    - 'disable'
                    - 'enable'
            admin-https-ssl-ciphersuites:
                type: list
                elements: str
                description: Deprecated, please rename it to admin_https_ssl_ciphersuites. Select one or more TLS 1.
                choices:
                    - 'TLS-AES-128-GCM-SHA256'
                    - 'TLS-AES-256-GCM-SHA384'
                    - 'TLS-CHACHA20-POLY1305-SHA256'
                    - 'TLS-AES-128-CCM-SHA256'
                    - 'TLS-AES-128-CCM-8-SHA256'
            security-rating-result-submission:
                type: str
                description: Deprecated, please rename it to security_rating_result_submission. Enable/disable the submission of Security Rating result...
                choices:
                    - 'disable'
                    - 'enable'
            user-device-store-max-unified-mem:
                type: int
                description: Deprecated, please rename it to user_device_store_max_unified_mem. Maximum unified memory allowed in user device store.
            management-port:
                type: int
                description: Deprecated, please rename it to management_port. Overriding port for management connection
            fortigslb-integration:
                type: str
                description: Deprecated, please rename it to fortigslb_integration. Enable/disable integration with the FortiGSLB cloud service.
                choices:
                    - 'disable'
                    - 'enable'
            admin-https-ssl-versions:
                type: list
                elements: str
                description: Deprecated, please rename it to admin_https_ssl_versions. Allowed TLS versions for web administration.
                choices:
                    - 'tlsv1-0'
                    - 'tlsv1-1'
                    - 'tlsv1-2'
                    - 'sslv3'
                    - 'tlsv1-3'
            cert-chain-max:
                type: int
                description: Deprecated, please rename it to cert_chain_max. Maximum number of certificates that can be traversed in a certificate chain.
            qsfp28-40g-port:
                type: raw
                description: (list) Deprecated, please rename it to qsfp28_40g_port. Set port
            strong-crypto:
                type: str
                description: Deprecated, please rename it to strong_crypto. Enable to use strong encryption and only allow strong ciphers and digest fo...
                choices:
                    - 'disable'
                    - 'enable'
            multi-factor-authentication:
                type: str
                description: Deprecated, please rename it to multi_factor_authentication. Enforce all login methods to require an additional authentica...
                choices:
                    - 'optional'
                    - 'mandatory'
            fds-statistics:
                type: str
                description: Deprecated, please rename it to fds_statistics. Enable/disable sending IPS, Application Control, and AntiVirus data to For...
                choices:
                    - 'disable'
                    - 'enable'
            gui-display-hostname:
                type: str
                description: Deprecated, please rename it to gui_display_hostname. Enable/disable displaying the FortiGates hostname on the GUI login page.
                choices:
                    - 'disable'
                    - 'enable'
            two-factor-ftk-expiry:
                type: int
                description: Deprecated, please rename it to two_factor_ftk_expiry. FortiToken authentication session timeout
            wad-source-affinity:
                type: str
                description: Deprecated, please rename it to wad_source_affinity. Enable/disable dispatching traffic to WAD workers based on source aff...
                choices:
                    - 'disable'
                    - 'enable'
            ssl-static-key-ciphers:
                type: str
                description: Deprecated, please rename it to ssl_static_key_ciphers. Enable/disable static key ciphers in SSL/TLS connections
                choices:
                    - 'disable'
                    - 'enable'
            daily-restart:
                type: str
                description: Deprecated, please rename it to daily_restart. Enable/disable daily restart of FortiGate unit.
                choices:
                    - 'disable'
                    - 'enable'
            snat-route-change:
                type: str
                description: Deprecated, please rename it to snat_route_change. Enable/disable the ability to change the source NAT route.
                choices:
                    - 'disable'
                    - 'enable'
            tcp-rst-timer:
                type: int
                description: Deprecated, please rename it to tcp_rst_timer. Length of the TCP CLOSE state in seconds
            anti-replay:
                type: str
                description: Deprecated, please rename it to anti_replay. Level of checking for packet replay and TCP sequence checking.
                choices:
                    - 'disable'
                    - 'loose'
                    - 'strict'
            ssl-min-proto-version:
                type: str
                description: Deprecated, please rename it to ssl_min_proto_version. Minimum supported protocol version for SSL/TLS connections
                choices:
                    - 'TLSv1'
                    - 'TLSv1-1'
                    - 'TLSv1-2'
                    - 'SSLv3'
                    - 'TLSv1-3'
            speedtestd-server-port:
                type: int
                description: Deprecated, please rename it to speedtestd_server_port. Speedtest server port number.
            cpu-use-threshold:
                type: int
                description: Deprecated, please rename it to cpu_use_threshold. Threshold at which CPU usage is reported
            admin-host:
                type: str
                description: Deprecated, please rename it to admin_host. Administrative host for HTTP and HTTPS.
            csr-ca-attribute:
                type: str
                description: Deprecated, please rename it to csr_ca_attribute. Enable/disable the CA attribute in certificates.
                choices:
                    - 'disable'
                    - 'enable'
            fortiservice-port:
                type: int
                description: Deprecated, please rename it to fortiservice_port. FortiService port
            ssd-trim-hour:
                type: int
                description: Deprecated, please rename it to ssd_trim_hour. Hour of the day on which to run SSD Trim
            purdue-level:
                type: str
                description: Deprecated, please rename it to purdue_level. Purdue Level of this FortiGate.
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
            management-vdom:
                type: raw
                description: (list) Deprecated, please rename it to management_vdom. Management virtual domain name.
            quic-ack-thresold:
                type: int
                description: Deprecated, please rename it to quic_ack_thresold. Maximum number of unacknowledged packets before sending ACK
            qsfpdd-100g-port:
                type: raw
                description: (list) Deprecated, please rename it to qsfpdd_100g_port. Split qsfpddd port
            ips-affinity:
                type: str
                description: Deprecated, please rename it to ips_affinity. Affinity setting for IPS
            vip-arp-range:
                type: str
                description: Deprecated, please rename it to vip_arp_range. Controls the number of ARPs that the FortiGate sends for a Virtual IP
                choices:
                    - 'restricted'
                    - 'unlimited'
            internet-service-database:
                type: str
                description: Deprecated, please rename it to internet_service_database. Configure which Internet Service database size to download from...
                choices:
                    - 'mini'
                    - 'standard'
                    - 'full'
                    - 'on-demand'
            revision-image-auto-backup:
                type: str
                description: Deprecated, please rename it to revision_image_auto_backup. Enable/disable back-up of the latest image revision after the ...
                choices:
                    - 'disable'
                    - 'enable'
            sflowd-max-children-num:
                type: int
                description: Deprecated, please rename it to sflowd_max_children_num. Maximum number of sflowd child processes allowed to run.
            admin-https-pki-required:
                type: str
                description: Deprecated, please rename it to admin_https_pki_required. Enable/disable admin login method.
                choices:
                    - 'disable'
                    - 'enable'
            special-file-23-support:
                type: str
                description: Deprecated, please rename it to special_file_23_support. Enable/disable detection of those special format files when using...
                choices:
                    - 'disable'
                    - 'enable'
            npu-neighbor-update:
                type: str
                description: Deprecated, please rename it to npu_neighbor_update. Enable/disable sending of ARP/ICMP6 probing packets to update neighbo...
                choices:
                    - 'disable'
                    - 'enable'
            log-single-cpu-high:
                type: str
                description: Deprecated, please rename it to log_single_cpu_high. Enable/disable logging the event of a single CPU core reaching CPU us...
                choices:
                    - 'disable'
                    - 'enable'
            management-ip:
                type: str
                description: Deprecated, please rename it to management_ip. Management IP address of this FortiGate.
            proxy-resource-mode:
                type: str
                description: Deprecated, please rename it to proxy_resource_mode. Enable/disable use of the maximum memory usage on the FortiGate units...
                choices:
                    - 'disable'
                    - 'enable'
            admin-ble-button:
                type: str
                description: Deprecated, please rename it to admin_ble_button. Press the BLE button can enable BLE function
                choices:
                    - 'disable'
                    - 'enable'
            gui-firmware-upgrade-warning:
                type: str
                description: Deprecated, please rename it to gui_firmware_upgrade_warning. Enable/disable the firmware upgrade warning on the GUI.
                choices:
                    - 'disable'
                    - 'enable'
            dp-tcp-normal-timer:
                type: int
                description: Deprecated, please rename it to dp_tcp_normal_timer. DP tcp normal timeout
            ipv6-allow-traffic-redirect:
                type: str
                description: Deprecated, please rename it to ipv6_allow_traffic_redirect. Disable to prevent IPv6 traffic with same local ingress and e...
                choices:
                    - 'disable'
                    - 'enable'
            cli-audit-log:
                type: str
                description: Deprecated, please rename it to cli_audit_log. Enable/disable CLI audit log.
                choices:
                    - 'disable'
                    - 'enable'
            memory-use-threshold-extreme:
                type: int
                description: Deprecated, please rename it to memory_use_threshold_extreme. Threshold at which memory usage is considered extreme
            ha-affinity:
                type: str
                description: Deprecated, please rename it to ha_affinity. Affinity setting for HA daemons
            restart-time:
                type: str
                description: Deprecated, please rename it to restart_time. Daily restart time
            speedtestd-ctrl-port:
                type: int
                description: Deprecated, please rename it to speedtestd_ctrl_port. Speedtest server controller port number.
            gui-wireless-opensecurity:
                type: str
                description: Deprecated, please rename it to gui_wireless_opensecurity. Enable/disable wireless open security option on the GUI.
                choices:
                    - 'disable'
                    - 'enable'
            memory-use-threshold-red:
                type: int
                description: Deprecated, please rename it to memory_use_threshold_red. Threshold at which memory usage forces the FortiGate to enter co...
            dp-fragment-timer:
                type: int
                description: Deprecated, please rename it to dp_fragment_timer. DP fragment session timeout
            wad-restart-start-time:
                type: str
                description: Deprecated, please rename it to wad_restart_start_time. WAD workers daily restart time
            proxy-re-authentication-time:
                type: int
                description: Deprecated, please rename it to proxy_re_authentication_time. The time limit that users must re-authenticate if proxy-keep...
            gui-app-detection-sdwan:
                type: str
                description: Deprecated, please rename it to gui_app_detection_sdwan. Enable/disable Allow app-detection based SD-WAN.
                choices:
                    - 'disable'
                    - 'enable'
            scanunit-count:
                type: int
                description: Deprecated, please rename it to scanunit_count. Number of scanunits.
            tftp:
                type: str
                description: Enable/disable TFTP.
                choices:
                    - 'disable'
                    - 'enable'
            xstools-update-frequency:
                type: int
                description: Deprecated, please rename it to xstools_update_frequency. Xenserver tools daemon update frequency
            clt-cert-req:
                type: str
                description: Deprecated, please rename it to clt_cert_req. Enable/disable requiring administrators to have a client certificate to log ...
                choices:
                    - 'disable'
                    - 'enable'
            fortiextender-vlan-mode:
                type: str
                description: Deprecated, please rename it to fortiextender_vlan_mode. Enable/disable FortiExtender VLAN mode.
                choices:
                    - 'disable'
                    - 'enable'
            auth-http-port:
                type: int
                description: Deprecated, please rename it to auth_http_port. User authentication HTTP port.
            per-user-bal:
                type: str
                description: Deprecated, please rename it to per_user_bal. Enable/disable per-user block/allow list filter.
                choices:
                    - 'disable'
                    - 'enable'
            gui-date-format:
                type: str
                description: Deprecated, please rename it to gui_date_format. Default date format used throughout GUI.
                choices:
                    - 'yyyy/MM/dd'
                    - 'dd/MM/yyyy'
                    - 'MM/dd/yyyy'
                    - 'yyyy-MM-dd'
                    - 'dd-MM-yyyy'
                    - 'MM-dd-yyyy'
            log-uuid-address:
                type: str
                description: Deprecated, please rename it to log_uuid_address. Enable/disable insertion of address UUIDs to traffic logs.
                choices:
                    - 'disable'
                    - 'enable'
            cloud-communication:
                type: str
                description: Deprecated, please rename it to cloud_communication. Enable/disable all cloud communication.
                choices:
                    - 'disable'
                    - 'enable'
            lldp-reception:
                type: str
                description: Deprecated, please rename it to lldp_reception. Enable/disable Link Layer Discovery Protocol
                choices:
                    - 'disable'
                    - 'enable'
            two-factor-ftm-expiry:
                type: int
                description: Deprecated, please rename it to two_factor_ftm_expiry. FortiToken Mobile session timeout
            quic-udp-payload-size-shaping-per-cid:
                type: str
                description: Deprecated, please rename it to quic_udp_payload_size_shaping_per_cid. Enable/disable UDP payload size shaping per connect...
                choices:
                    - 'disable'
                    - 'enable'
            autorun-log-fsck:
                type: str
                description: Deprecated, please rename it to autorun_log_fsck. Enable/disable automatic log partition check after ungraceful shutdown.
                choices:
                    - 'disable'
                    - 'enable'
            vpn-ems-sn-check:
                type: str
                description: Deprecated, please rename it to vpn_ems_sn_check. Enable/disable verification of EMS serial number in SSL-VPN connection.
                choices:
                    - 'disable'
                    - 'enable'
            admin-ssh-password:
                type: str
                description: Deprecated, please rename it to admin_ssh_password. Enable/disable password authentication for SSH admin access.
                choices:
                    - 'disable'
                    - 'enable'
            airplane-mode:
                type: str
                description: Deprecated, please rename it to airplane_mode. Enable/disable airplane mode.
                choices:
                    - 'disable'
                    - 'enable'
            batch-cmdb:
                type: str
                description: Deprecated, please rename it to batch_cmdb. Enable/disable batch mode, allowing you to enter a series of CLI commands that...
                choices:
                    - 'disable'
                    - 'enable'
            ip-src-port-range:
                type: raw
                description: (list) Deprecated, please rename it to ip_src_port_range. IP source port range used for traffic originating from the Forti...
            strict-dirty-session-check:
                type: str
                description: Deprecated, please rename it to strict_dirty_session_check. Enable to check the session against the original policy when r...
                choices:
                    - 'disable'
                    - 'enable'
            user-device-store-max-devices:
                type: int
                description: Deprecated, please rename it to user_device_store_max_devices. Maximum number of devices allowed in user device store.
            dp-udp-idle-timer:
                type: int
                description: Deprecated, please rename it to dp_udp_idle_timer. DP udp idle timer
            internal-switch-speed:
                type: list
                elements: str
                description: Deprecated, please rename it to internal_switch_speed. Internal port speed.
                choices:
                    - 'auto'
                    - '10full'
                    - '10half'
                    - '100full'
                    - '100half'
                    - '1000full'
                    - '1000auto'
            forticonverter-config-upload:
                type: str
                description: Deprecated, please rename it to forticonverter_config_upload. Enable/disable config upload to FortiConverter.
                choices:
                    - 'disable'
                    - 'once'
            ipsec-round-robin:
                type: str
                description: Deprecated, please rename it to ipsec_round_robin. Enable/disable round-robin redistribution to multiple CPUs for IPsec VP...
                choices:
                    - 'disable'
                    - 'enable'
            wad-affinity:
                type: str
                description: Deprecated, please rename it to wad_affinity. Affinity setting for wad
            wifi-ca-certificate:
                type: raw
                description: (list) Deprecated, please rename it to wifi_ca_certificate. CA certificate that verifies the WiFi certificate.
            wimax-4g-usb:
                type: str
                description: Deprecated, please rename it to wimax_4g_usb. Enable/disable comparability with WiMAX 4G USB devices.
                choices:
                    - 'disable'
                    - 'enable'
            miglog-affinity:
                type: str
                description: Deprecated, please rename it to miglog_affinity. Affinity setting for logging
            faz-disk-buffer-size:
                type: int
                description: Deprecated, please rename it to faz_disk_buffer_size. Maximum disk buffer size to temporarily store logs destined for Fort...
            ssh-kex-algo:
                type: list
                elements: str
                description: Deprecated, please rename it to ssh_kex_algo. Select one or more SSH kex algorithms.
                choices:
                    - 'diffie-hellman-group1-sha1'
                    - 'diffie-hellman-group14-sha1'
                    - 'diffie-hellman-group-exchange-sha1'
                    - 'diffie-hellman-group-exchange-sha256'
                    - 'curve25519-sha256@libssh.org'
                    - 'ecdh-sha2-nistp256'
                    - 'ecdh-sha2-nistp384'
                    - 'ecdh-sha2-nistp521'
                    - 'diffie-hellman-group14-sha256'
                    - 'diffie-hellman-group16-sha512'
                    - 'diffie-hellman-group18-sha512'
            auto-auth-extension-device:
                type: str
                description: Deprecated, please rename it to auto_auth_extension_device. Enable/disable automatic authorization of dedicated Fortinet e...
                choices:
                    - 'disable'
                    - 'enable'
            forticarrier-bypass:
                type: str
                description: Deprecated, please rename it to forticarrier_bypass. Forticarrier bypass.
                choices:
                    - 'disable'
                    - 'enable'
            reset-sessionless-tcp:
                type: str
                description: Deprecated, please rename it to reset_sessionless_tcp. Action to perform if the FortiGate receives a TCP packet but cannot...
                choices:
                    - 'disable'
                    - 'enable'
            early-tcp-npu-session:
                type: str
                description: Deprecated, please rename it to early_tcp_npu_session. Enable/disable early TCP NPU session.
                choices:
                    - 'disable'
                    - 'enable'
            http-unauthenticated-request-limit:
                type: int
                description: Deprecated, please rename it to http_unauthenticated_request_limit. HTTP request body size limit before authentication.
            gui-local-out:
                type: str
                description: Deprecated, please rename it to gui_local_out. Enable/disable Local-out traffic on the GUI.
                choices:
                    - 'disable'
                    - 'enable'
            tcp-option:
                type: str
                description: Deprecated, please rename it to tcp_option. Enable SACK, timestamp and MSS TCP options.
                choices:
                    - 'disable'
                    - 'enable'
            proxy-auth-timeout:
                type: int
                description: Deprecated, please rename it to proxy_auth_timeout. Authentication timeout in minutes for authenticated users
            fortiextender-discovery-lockdown:
                type: str
                description: Deprecated, please rename it to fortiextender_discovery_lockdown. Enable/disable FortiExtender CAPWAP lockdown.
                choices:
                    - 'disable'
                    - 'enable'
            lldp-transmission:
                type: str
                description: Deprecated, please rename it to lldp_transmission. Enable/disable Link Layer Discovery Protocol
                choices:
                    - 'disable'
                    - 'enable'
            split-port:
                type: raw
                description: (list) Deprecated, please rename it to split_port. Split port
            gui-certificates:
                type: str
                description: Deprecated, please rename it to gui_certificates. Enable/disable the System > Certificate GUI page, allowing you to add an...
                choices:
                    - 'disable'
                    - 'enable'
            cfg-save:
                type: str
                description: Deprecated, please rename it to cfg_save. Configuration file save mode for CLI changes.
                choices:
                    - 'automatic'
                    - 'manual'
                    - 'revert'
            auth-keepalive:
                type: str
                description: Deprecated, please rename it to auth_keepalive. Enable to prevent user authentication sessions from timing out when idle.
                choices:
                    - 'disable'
                    - 'enable'
            split-port-mode:
                type: list
                elements: dict
                description: Deprecated, please rename it to split_port_mode. Split port mode.
                suboptions:
                    interface:
                        type: str
                        description: Split port interface.
                    split-mode:
                        type: str
                        description: Deprecated, please rename it to split_mode. The configuration mode for the split port interface.
                        choices:
                            - 'disable'
                            - '4x10G'
                            - '4x25G'
                            - '4x50G'
                            - '8x50G'
                            - '4x100G'
                            - '2x200G'
                            - '8x25G'
            admin-forticloud-sso-login:
                type: str
                description: Deprecated, please rename it to admin_forticloud_sso_login. Enable/disable FortiCloud admin login via SSO.
                choices:
                    - 'disable'
                    - 'enable'
            post-login-banner:
                type: str
                description: Deprecated, please rename it to post_login_banner. Enable/disable displaying the administrator access disclaimer message a...
                choices:
                    - 'disable'
                    - 'enable'
            br-fdb-max-entry:
                type: int
                description: Deprecated, please rename it to br_fdb_max_entry. Maximum number of bridge forwarding database
            ip-fragment-mem-thresholds:
                type: int
                description: Deprecated, please rename it to ip_fragment_mem_thresholds. Maximum memory
            fortiextender-provision-on-authorization:
                type: str
                description: Deprecated, please rename it to fortiextender_provision_on_authorization. Enable/disable automatic provisioning of latest ...
                choices:
                    - 'disable'
                    - 'enable'
            reboot-upon-config-restore:
                type: str
                description: Deprecated, please rename it to reboot_upon_config_restore. Enable/disable reboot of system upon restoring configuration.
                choices:
                    - 'disable'
                    - 'enable'
            syslog-affinity:
                type: str
                description: Deprecated, please rename it to syslog_affinity. Affinity setting for syslog
            fortiextender-data-port:
                type: int
                description: Deprecated, please rename it to fortiextender_data_port. FortiExtender data port
            quic-tls-handshake-timeout:
                type: int
                description: Deprecated, please rename it to quic_tls_handshake_timeout. Time-to-live
            forticonverter-integration:
                type: str
                description: Deprecated, please rename it to forticonverter_integration. Enable/disable FortiConverter integration service.
                choices:
                    - 'disable'
                    - 'enable'
            proxy-keep-alive-mode:
                type: str
                description: Deprecated, please rename it to proxy_keep_alive_mode. Control if users must re-authenticate after a session is closed, tr...
                choices:
                    - 'session'
                    - 'traffic'
                    - 're-authentication'
            cmdbsvr-affinity:
                type: str
                description: Deprecated, please rename it to cmdbsvr_affinity. Affinity setting for cmdbsvr
            wad-memory-change-granularity:
                type: int
                description: Deprecated, please rename it to wad_memory_change_granularity. Minimum percentage change in system memory usage detected b...
            dhcp-lease-backup-interval:
                type: int
                description: Deprecated, please rename it to dhcp_lease_backup_interval. DHCP leases backup interval in seconds
            check-protocol-header:
                type: str
                description: Deprecated, please rename it to check_protocol_header. Level of checking performed on protocol headers.
                choices:
                    - 'loose'
                    - 'strict'
            av-failopen-session:
                type: str
                description: Deprecated, please rename it to av_failopen_session. When enabled and a proxy for a protocol runs out of room in its sessi...
                choices:
                    - 'disable'
                    - 'enable'
            ipsec-ha-seqjump-rate:
                type: int
                description: Deprecated, please rename it to ipsec_ha_seqjump_rate. ESP jump ahead rate
            admin-hsts-max-age:
                type: int
                description: Deprecated, please rename it to admin_hsts_max_age. HTTPS Strict-Transport-Security header max-age in seconds.
            igmp-state-limit:
                type: int
                description: Deprecated, please rename it to igmp_state_limit. Maximum number of IGMP memberships
            admin-login-max:
                type: int
                description: Deprecated, please rename it to admin_login_max. Maximum number of administrators who can be logged in at the same time
            ipv6-allow-multicast-probe:
                type: str
                description: Deprecated, please rename it to ipv6_allow_multicast_probe. Enable/disable IPv6 address probe through Multicast.
                choices:
                    - 'disable'
                    - 'enable'
            virtual-switch-vlan:
                type: str
                description: Deprecated, please rename it to virtual_switch_vlan. Enable/disable virtual switch VLAN.
                choices:
                    - 'disable'
                    - 'enable'
            admin-lockout-threshold:
                type: int
                description: Deprecated, please rename it to admin_lockout_threshold. Number of failed login attempts before an administrator account i...
            dp-pinhole-timer:
                type: int
                description: Deprecated, please rename it to dp_pinhole_timer. DP pinhole session timeout
            wireless-controller:
                type: str
                description: Deprecated, please rename it to wireless_controller. Enable/disable the wireless controller feature to use the FortiGate u...
                choices:
                    - 'disable'
                    - 'enable'
            bfd-affinity:
                type: str
                description: Deprecated, please rename it to bfd_affinity. Affinity setting for BFD daemon
            ssd-trim-freq:
                type: str
                description: Deprecated, please rename it to ssd_trim_freq. How often to run SSD Trim
                choices:
                    - 'daily'
                    - 'weekly'
                    - 'monthly'
                    - 'hourly'
                    - 'never'
            two-factor-sms-expiry:
                type: int
                description: Deprecated, please rename it to two_factor_sms_expiry. SMS-based two-factor authentication session timeout
            traffic-priority:
                type: str
                description: Deprecated, please rename it to traffic_priority. Choose Type of Service
                choices:
                    - 'tos'
                    - 'dscp'
            proxy-and-explicit-proxy:
                type: str
                description: Deprecated, please rename it to proxy_and_explicit_proxy. Proxy and explicit proxy.
                choices:
                    - 'disable'
                    - 'enable'
            sslvpn-web-mode:
                type: str
                description: Deprecated, please rename it to sslvpn_web_mode. Enable/disable SSL-VPN web mode.
                choices:
                    - 'disable'
                    - 'enable'
            ssh-hostkey-password:
                type: raw
                description: (list) Deprecated, please rename it to ssh_hostkey_password. Password for ssh-hostkey.
            wad-csvc-db-count:
                type: int
                description: Deprecated, please rename it to wad_csvc_db_count. Number of concurrent WAD-cache-service byte-cache processes.
            ipv6-allow-anycast-probe:
                type: str
                description: Deprecated, please rename it to ipv6_allow_anycast_probe. Enable/disable IPv6 address probe through Anycast.
                choices:
                    - 'disable'
                    - 'enable'
            honor-df:
                type: str
                description: Deprecated, please rename it to honor_df. Enable/disable honoring of Dont-Fragment
                choices:
                    - 'disable'
                    - 'enable'
            hyper-scale-vdom-num:
                type: int
                description: Deprecated, please rename it to hyper_scale_vdom_num. Number of VDOMs for hyper scale license.
            wad-csvc-cs-count:
                type: int
                description: Deprecated, please rename it to wad_csvc_cs_count. Number of concurrent WAD-cache-service object-cache processes.
            internal-switch-mode:
                type: str
                description: Deprecated, please rename it to internal_switch_mode. Internal switch mode.
                choices:
                    - 'switch'
                    - 'interface'
                    - 'hub'
            cfg-revert-timeout:
                type: int
                description: Deprecated, please rename it to cfg_revert_timeout. Time-out for reverting to the last saved configuration.
            admin-concurrent:
                type: str
                description: Deprecated, please rename it to admin_concurrent. Enable/disable concurrent administrator logins.
                choices:
                    - 'disable'
                    - 'enable'
            ipv6-allow-local-in-silent-drop:
                type: str
                description: Deprecated, please rename it to ipv6_allow_local_in_silent_drop. Enable/disable silent drop of IPv6 local-in traffic.
                choices:
                    - 'disable'
                    - 'enable'
            tcp-halfopen-timer:
                type: int
                description: Deprecated, please rename it to tcp_halfopen_timer. Number of seconds the FortiGate unit should wait to close a session af...
            dp-rsync-timer:
                type: int
                description: Deprecated, please rename it to dp_rsync_timer. DP rsync session timeout
            management-port-use-admin-sport:
                type: str
                description: Deprecated, please rename it to management_port_use_admin_sport. Enable/disable use of the admin-sport setting for the man...
                choices:
                    - 'disable'
                    - 'enable'
            gui-forticare-registration-setup-warning:
                type: str
                description: Deprecated, please rename it to gui_forticare_registration_setup_warning. Enable/disable the FortiCare registration setup ...
                choices:
                    - 'disable'
                    - 'enable'
            gui-replacement-message-groups:
                type: str
                description: Deprecated, please rename it to gui_replacement_message_groups. Enable/disable replacement message groups on the GUI.
                choices:
                    - 'disable'
                    - 'enable'
            security-rating-run-on-schedule:
                type: str
                description: Deprecated, please rename it to security_rating_run_on_schedule. Enable/disable scheduled runs of Security Rating.
                choices:
                    - 'disable'
                    - 'enable'
            admin-lockout-duration:
                type: int
                description: Deprecated, please rename it to admin_lockout_duration. Amount of time in seconds that an administrator account is locked ...
            optimize-flow-mode:
                type: str
                description: Deprecated, please rename it to optimize_flow_mode. Flow mode optimization option.
                choices:
                    - 'disable'
                    - 'enable'
            private-data-encryption:
                type: str
                description: Deprecated, please rename it to private_data_encryption. Enable/disable private data encryption using an AES 128-bit key o...
                choices:
                    - 'disable'
                    - 'enable'
            wireless-mode:
                type: str
                description: Deprecated, please rename it to wireless_mode. Wireless mode setting.
                choices:
                    - 'ac'
                    - 'client'
                    - 'wtp'
                    - 'fwfap'
            alias:
                type: str
                description: Alias for your FortiGate unit.
            ssh-hostkey-algo:
                type: list
                elements: str
                description: Deprecated, please rename it to ssh_hostkey_algo. Select one or more SSH hostkey algorithms.
                choices:
                    - 'ssh-rsa'
                    - 'ecdsa-sha2-nistp521'
                    - 'rsa-sha2-256'
                    - 'rsa-sha2-512'
                    - 'ssh-ed25519'
                    - 'ecdsa-sha2-nistp384'
                    - 'ecdsa-sha2-nistp256'
            fortitoken-cloud:
                type: str
                description: Deprecated, please rename it to fortitoken_cloud. Enable/disable FortiToken Cloud service.
                choices:
                    - 'disable'
                    - 'enable'
            av-affinity:
                type: str
                description: Deprecated, please rename it to av_affinity. Affinity setting for AV scanning
            proxy-worker-count:
                type: int
                description: Deprecated, please rename it to proxy_worker_count. Proxy worker count.
            ipsec-asic-offload:
                type: str
                description: Deprecated, please rename it to ipsec_asic_offload. Enable/disable ASIC offloading
                choices:
                    - 'disable'
                    - 'enable'
            miglogd-children:
                type: int
                description: Deprecated, please rename it to miglogd_children. Number of logging
            sslvpn-max-worker-count:
                type: int
                description: Deprecated, please rename it to sslvpn_max_worker_count. Maximum number of SSL-VPN processes.
            ssh-mac-algo:
                type: list
                elements: str
                description: Deprecated, please rename it to ssh_mac_algo. Select one or more SSH MAC algorithms.
                choices:
                    - 'hmac-md5'
                    - 'hmac-md5-etm@openssh.com'
                    - 'hmac-md5-96'
                    - 'hmac-md5-96-etm@openssh.com'
                    - 'hmac-sha1'
                    - 'hmac-sha1-etm@openssh.com'
                    - 'hmac-sha2-256'
                    - 'hmac-sha2-256-etm@openssh.com'
                    - 'hmac-sha2-512'
                    - 'hmac-sha2-512-etm@openssh.com'
                    - 'hmac-ripemd160'
                    - 'hmac-ripemd160@openssh.com'
                    - 'hmac-ripemd160-etm@openssh.com'
                    - 'umac-64@openssh.com'
                    - 'umac-128@openssh.com'
                    - 'umac-64-etm@openssh.com'
                    - 'umac-128-etm@openssh.com'
            url-filter-count:
                type: int
                description: Deprecated, please rename it to url_filter_count. URL filter daemon count.
            wifi-certificate:
                type: raw
                description: (list) Deprecated, please rename it to wifi_certificate. Certificate to use for WiFi authentication.
            radius-port:
                type: int
                description: Deprecated, please rename it to radius_port. RADIUS service port number.
            sys-perf-log-interval:
                type: int
                description: Deprecated, please rename it to sys_perf_log_interval. Time in minutes between updates of performance statistics logging.
            gui-fortigate-cloud-sandbox:
                type: str
                description: Deprecated, please rename it to gui_fortigate_cloud_sandbox. Enable/disable displaying FortiGate Cloud Sandbox on the GUI.
                choices:
                    - 'disable'
                    - 'enable'
            auth-cert:
                type: raw
                description: (list) Deprecated, please rename it to auth_cert. Server certificate that the FortiGate uses for HTTPS firewall authentica...
            fortiextender:
                type: str
                description: Enable/disable FortiExtender.
                choices:
                    - 'disable'
                    - 'enable'
            admin-reset-button:
                type: str
                description: Deprecated, please rename it to admin_reset_button. Press the reset button can reset to factory default.
                choices:
                    - 'disable'
                    - 'enable'
            av-failopen:
                type: str
                description: Deprecated, please rename it to av_failopen. Set the action to take if the FortiGate is running low on memory or the proxy...
                choices:
                    - 'off'
                    - 'pass'
                    - 'one-shot'
                    - 'idledrop'
            user-device-store-max-users:
                type: int
                description: Deprecated, please rename it to user_device_store_max_users. Maximum number of users allowed in user device store.
            auth-session-limit:
                type: str
                description: Deprecated, please rename it to auth_session_limit. Action to take when the number of allowed user authenticated sessions ...
                choices:
                    - 'block-new'
                    - 'logout-inactive'
            ipv6-allow-local-in-slient-drop:
                type: str
                description: Deprecated, please rename it to ipv6_allow_local_in_slient_drop. Enable/disable silent drop of IPv6 local-in traffic.
                choices:
                    - 'disable'
                    - 'enable'
            quic-congestion-control-algo:
                type: str
                description: Deprecated, please rename it to quic_congestion_control_algo. QUIC congestion control algorithm
                choices:
                    - 'cubic'
                    - 'bbr'
                    - 'bbr2'
                    - 'reno'
            auth-ike-saml-port:
                type: int
                description: Deprecated, please rename it to auth_ike_saml_port. User IKE SAML authentication port
            wad-restart-end-time:
                type: str
                description: Deprecated, please rename it to wad_restart_end_time. WAD workers daily restart end time
            http-request-limit:
                type: int
                description: Deprecated, please rename it to http_request_limit. HTTP request body size limit.
            irq-time-accounting:
                type: str
                description: Deprecated, please rename it to irq_time_accounting. Configure CPU IRQ time accounting mode.
                choices:
                    - 'auto'
                    - 'force'
            remoteauthtimeout:
                type: int
                description: Number of seconds that the FortiGate waits for responses from remote RADIUS, LDAP, or TACACS+ authentication servers.
            admin-https-ssl-banned-ciphers:
                type: list
                elements: str
                description: Deprecated, please rename it to admin_https_ssl_banned_ciphers. Select one or more cipher technologies that cannot be used...
                choices:
                    - 'RSA'
                    - 'DHE'
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
            allow-traffic-redirect:
                type: str
                description: Deprecated, please rename it to allow_traffic_redirect. Disable to prevent traffic with same local ingress and egress inte...
                choices:
                    - 'disable'
                    - 'enable'
            legacy-poe-device-support:
                type: str
                description: Deprecated, please rename it to legacy_poe_device_support. Enable/disable legacy POE device support.
                choices:
                    - 'disable'
                    - 'enable'
            wad-restart-mode:
                type: str
                description: Deprecated, please rename it to wad_restart_mode. WAD worker restart mode
                choices:
                    - 'none'
                    - 'time'
                    - 'memory'
            fds-statistics-period:
                type: int
                description: Deprecated, please rename it to fds_statistics_period. FortiGuard statistics collection period in minutes.
            admin-telnet:
                type: str
                description: Deprecated, please rename it to admin_telnet. Enable/disable TELNET service.
                choices:
                    - 'disable'
                    - 'enable'
            ipv6-accept-dad:
                type: int
                description: Deprecated, please rename it to ipv6_accept_dad. Enable/disable acceptance of IPv6 Duplicate Address Detection
            tcp-timewait-timer:
                type: int
                description: Deprecated, please rename it to tcp_timewait_timer. Length of the TCP TIME-WAIT state in seconds
            admin-console-timeout:
                type: int
                description: Deprecated, please rename it to admin_console_timeout. Console login timeout that overrides the admin timeout value
            default-service-source-port:
                type: str
                description: Deprecated, please rename it to default_service_source_port. Default service source port range
            quic-max-datagram-size:
                type: int
                description: Deprecated, please rename it to quic_max_datagram_size. Maximum transmit datagram size
            refresh:
                type: int
                description: Statistics refresh interval second
            extender-controller-reserved-network:
                type: raw
                description: (list) Deprecated, please rename it to extender_controller_reserved_network. Configure reserved network subnet for managed...
            url-filter-affinity:
                type: str
                description: Deprecated, please rename it to url_filter_affinity. URL filter CPU affinity.
            policy-auth-concurrent:
                type: int
                description: Deprecated, please rename it to policy_auth_concurrent. Number of concurrent firewall use logins from the same user
            ipsec-hmac-offload:
                type: str
                description: Deprecated, please rename it to ipsec_hmac_offload. Enable/disable offloading
                choices:
                    - 'disable'
                    - 'enable'
            traffic-priority-level:
                type: str
                description: Deprecated, please rename it to traffic_priority_level. Default system-wide level of priority for traffic prioritization.
                choices:
                    - 'high'
                    - 'medium'
                    - 'low'
            ipsec-qat-offload:
                type: str
                description: Deprecated, please rename it to ipsec_qat_offload. Enable/disable QAT offloading
                choices:
                    - 'disable'
                    - 'enable'
            ssd-trim-min:
                type: int
                description: Deprecated, please rename it to ssd_trim_min. Minute of the hour on which to run SSD Trim
            gui-date-time-source:
                type: str
                description: Deprecated, please rename it to gui_date_time_source. Source from which the FortiGate GUI uses to display date and time en...
                choices:
                    - 'system'
                    - 'browser'
            log-ssl-connection:
                type: str
                description: Deprecated, please rename it to log_ssl_connection. Enable/disable logging of SSL connection events.
                choices:
                    - 'disable'
                    - 'enable'
            ndp-max-entry:
                type: int
                description: Deprecated, please rename it to ndp_max_entry. Maximum number of NDP table entries
            vdom-mode:
                type: str
                description: Deprecated, please rename it to vdom_mode. Enable/disable support for multiple virtual domains
                choices:
                    - 'no-vdom'
                    - 'multi-vdom'
                    - 'split-vdom'
            internet-service-download-list:
                type: raw
                description: (list) Deprecated, please rename it to internet_service_download_list. Configure which on-demand Internet Service IDs are ...
            fortitoken-cloud-sync-interval:
                type: int
                description: Deprecated, please rename it to fortitoken_cloud_sync_interval. Interval in which to clean up remote users in FortiToken Cloud
            ssd-trim-weekday:
                type: str
                description: Deprecated, please rename it to ssd_trim_weekday. Day of week to run SSD Trim.
                choices:
                    - 'sunday'
                    - 'monday'
                    - 'tuesday'
                    - 'wednesday'
                    - 'thursday'
                    - 'friday'
                    - 'saturday'
            two-factor-fac-expiry:
                type: int
                description: Deprecated, please rename it to two_factor_fac_expiry. FortiAuthenticator token authentication session timeout
            gui-rest-api-cache:
                type: str
                description: Deprecated, please rename it to gui_rest_api_cache. Enable/disable REST API result caching on FortiGate.
                choices:
                    - 'disable'
                    - 'enable'
            admin-forticloud-sso-default-profile:
                type: raw
                description: (list) Deprecated, please rename it to admin_forticloud_sso_default_profile. Override access profile.
            proxy-auth-lifetime:
                type: str
                description: Deprecated, please rename it to proxy_auth_lifetime. Enable/disable authenticated users lifetime control.
                choices:
                    - 'disable'
                    - 'enable'
            device-idle-timeout:
                type: int
                description: Deprecated, please rename it to device_idle_timeout. Time in seconds that a device must be idle to automatically log the d...
            login-timestamp:
                type: str
                description: Deprecated, please rename it to login_timestamp. Enable/disable login time recording.
                choices:
                    - 'disable'
                    - 'enable'
            speedtest-server:
                type: str
                description: Deprecated, please rename it to speedtest_server. Enable/disable speed test server.
                choices:
                    - 'disable'
                    - 'enable'
            edit-vdom-prompt:
                type: str
                description: Deprecated, please rename it to edit_vdom_prompt. Enable/disable edit new VDOM prompt.
                choices:
                    - 'disable'
                    - 'enable'
            gui-cdn-domain-override:
                type: str
                description: Deprecated, please rename it to gui_cdn_domain_override. Domain of CDN server.
            admin-ssh-grace-time:
                type: int
                description: Deprecated, please rename it to admin_ssh_grace_time. Maximum time in seconds permitted between making an SSH connection t...
            sslvpn-ems-sn-check:
                type: str
                description: Deprecated, please rename it to sslvpn_ems_sn_check. Enable/disable verification of EMS serial number in SSL-VPN connection.
                choices:
                    - 'disable'
                    - 'enable'
            user-server-cert:
                type: raw
                description: (list) Deprecated, please rename it to user_server_cert. Certificate to use for https user authentication.
            gui-allow-default-hostname:
                type: str
                description: Deprecated, please rename it to gui_allow_default_hostname. Enable/disable the factory default hostname warning on the GUI...
                choices:
                    - 'disable'
                    - 'enable'
            proxy-re-authentication-mode:
                type: str
                description: Deprecated, please rename it to proxy_re_authentication_mode. Control if users must re-authenticate after a session is clo...
                choices:
                    - 'session'
                    - 'traffic'
                    - 'absolute'
            ipsec-soft-dec-async:
                type: str
                description: Deprecated, please rename it to ipsec_soft_dec_async. Enable/disable software decryption asynchronization
                choices:
                    - 'disable'
                    - 'enable'
            admin-maintainer:
                type: str
                description: Deprecated, please rename it to admin_maintainer. Enable/disable maintainer administrator login.
                choices:
                    - 'disable'
                    - 'enable'
            dst:
                type: str
                description: Enable/disable daylight saving time.
                choices:
                    - 'disable'
                    - 'enable'
            fec-port:
                type: int
                description: Deprecated, please rename it to fec_port. Local UDP port for Forward Error Correction
            ssh-kex-sha1:
                type: str
                description: Deprecated, please rename it to ssh_kex_sha1. Enable/disable SHA1 key exchange for SSH access.
                choices:
                    - 'disable'
                    - 'enable'
            ssh-mac-weak:
                type: str
                description: Deprecated, please rename it to ssh_mac_weak. Enable/disable HMAC-SHA1 and UMAC-64-ETM for SSH access.
                choices:
                    - 'disable'
                    - 'enable'
            sslvpn-cipher-hardware-acceleration:
                type: str
                description: Deprecated, please rename it to sslvpn_cipher_hardware_acceleration. Enable/disable SSL-VPN hardware acceleration.
                choices:
                    - 'disable'
                    - 'enable'
            sys-file-check-interval:
                type: int
                description: Deprecated, please rename it to sys_file_check_interval. Set scheduled system file checking interval in minutes
            ssh-hmac-md5:
                type: str
                description: Deprecated, please rename it to ssh_hmac_md5. Enable/disable HMAC-MD5 for SSH access.
                choices:
                    - 'disable'
                    - 'enable'
            ssh-cbc-cipher:
                type: str
                description: Deprecated, please rename it to ssh_cbc_cipher. Enable/disable CBC cipher for SSH access.
                choices:
                    - 'disable'
                    - 'enable'
            gui-fortiguard-resource-fetch:
                type: str
                description: Deprecated, please rename it to gui_fortiguard_resource_fetch. Enable/disable retrieving static GUI resources from FortiGuard.
                choices:
                    - 'disable'
                    - 'enable'
            sslvpn-kxp-hardware-acceleration:
                type: str
                description: Deprecated, please rename it to sslvpn_kxp_hardware_acceleration. Enable/disable SSL-VPN KXP hardware acceleration.
                choices:
                    - 'disable'
                    - 'enable'
            sslvpn-plugin-version-check:
                type: str
                description: Deprecated, please rename it to sslvpn_plugin_version_check. Enable/disable checking browsers plugin version by SSL-VPN.
                choices:
                    - 'disable'
                    - 'enable'
            fortiipam-integration:
                type: str
                description: Deprecated, please rename it to fortiipam_integration. Enable/disable integration with the FortiIPAM cloud service.
                choices:
                    - 'disable'
                    - 'enable'
            gui-firmware-upgrade-setup-warning:
                type: str
                description: Deprecated, please rename it to gui_firmware_upgrade_setup_warning. Gui firmware upgrade setup warning.
                choices:
                    - 'disable'
                    - 'enable'
            log-uuid-policy:
                type: str
                description: Deprecated, please rename it to log_uuid_policy. Enable/disable insertion of policy UUIDs to traffic logs.
                choices:
                    - 'disable'
                    - 'enable'
            per-user-bwl:
                type: str
                description: Deprecated, please rename it to per_user_bwl. Enable/disable per-user black/white list filter.
                choices:
                    - 'disable'
                    - 'enable'
            gui-fortisandbox-cloud:
                type: str
                description: Deprecated, please rename it to gui_fortisandbox_cloud. Enable/disable displaying FortiSandbox Cloud on the GUI.
                choices:
                    - 'disable'
                    - 'enable'
            fortitoken-cloud-service:
                type: str
                description: Deprecated, please rename it to fortitoken_cloud_service. Fortitoken cloud service.
                choices:
                    - 'disable'
                    - 'enable'
            hw-switch-ether-filter:
                type: str
                description: Deprecated, please rename it to hw_switch_ether_filter. Enable/disable hardware filter for certain Ethernet packet types.
                choices:
                    - 'disable'
                    - 'enable'
            virtual-server-count:
                type: int
                description: Deprecated, please rename it to virtual_server_count. Maximum number of virtual server processes to create.
            endpoint-control-fds-access:
                type: str
                description: Deprecated, please rename it to endpoint_control_fds_access. Endpoint control fds access.
                choices:
                    - 'disable'
                    - 'enable'
            proxy-cipher-hardware-acceleration:
                type: str
                description: Deprecated, please rename it to proxy_cipher_hardware_acceleration. Enable/disable using content processor
                choices:
                    - 'disable'
                    - 'enable'
            proxy-kxp-hardware-acceleration:
                type: str
                description: Deprecated, please rename it to proxy_kxp_hardware_acceleration. Enable/disable using the content processor to accelerate ...
                choices:
                    - 'disable'
                    - 'enable'
            virtual-server-hardware-acceleration:
                type: str
                description: Deprecated, please rename it to virtual_server_hardware_acceleration. Enable/disable virtual server hardware acceleration.
                choices:
                    - 'disable'
                    - 'enable'
            user-history-password-threshold:
                type: int
                description: Deprecated, please rename it to user_history_password_threshold. Maximum number of previous passwords saved per admin/user
            delay-tcp-npu-session:
                type: str
                description: Deprecated, please rename it to delay_tcp_npu_session. Enable TCP NPU session delay to guarantee packet order of 3-way han...
                choices:
                    - 'disable'
                    - 'enable'
            auth-session-auto-backup-interval:
                type: str
                description: Deprecated, please rename it to auth_session_auto_backup_interval. Configure automatic authentication session backup inter...
                choices:
                    - '1min'
                    - '5min'
                    - '15min'
                    - '30min'
                    - '1hr'
            ip-conflict-detection:
                type: str
                description: Deprecated, please rename it to ip_conflict_detection. Enable/disable logging of IPv4 address conflict detection.
                choices:
                    - 'disable'
                    - 'enable'
            gtpu-dynamic-source-port:
                type: str
                description: Deprecated, please rename it to gtpu_dynamic_source_port. Enable/disable GTP-U dynamic source port support.
                choices:
                    - 'disable'
                    - 'enable'
            ip-fragment-timeout:
                type: int
                description: Deprecated, please rename it to ip_fragment_timeout. Timeout value in seconds for any fragment not being reassembled
            ipv6-fragment-timeout:
                type: int
                description: Deprecated, please rename it to ipv6_fragment_timeout. Timeout value in seconds for any IPv6 fragment not being reassembled
            scim-server-cert:
                type: raw
                description: (list) Deprecated, please rename it to scim_server_cert. Server certificate that the FortiGate uses for SCIM connections.
            scim-http-port:
                type: int
                description: Deprecated, please rename it to scim_http_port. SCIM http port
            auth-session-auto-backup:
                type: str
                description: Deprecated, please rename it to auth_session_auto_backup. Enable/disable automatic and periodic backup of authentication s...
                choices:
                    - 'disable'
                    - 'enable'
            scim-https-port:
                type: int
                description: Deprecated, please rename it to scim_https_port. SCIM port
            httpd-max-worker-count:
                type: int
                description: Deprecated, please rename it to httpd_max_worker_count. Maximum number of simultaneous HTTP requests that will be served.
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
    - name: Configure global attributes.
      fortinet.fortimanager.fmgr_devprof_system_global:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        adom: <your own value>
        devprof: <your own value>
        devprof_system_global:
          admin_https_redirect: <value in [disable, enable]>
          admin_port: <integer>
          admin_scp: <value in [disable, enable]>
          admin_sport: <integer>
          admin_ssh_port: <integer>
          admin_ssh_v1: <value in [disable, enable]>
          admin_telnet_port: <integer>
          admintimeout: <integer>
          gui_ipv6: <value in [disable, enable]>
          gui_lines_per_page: <integer>
          gui_theme: <value in [blue, green, melongene, ...]>
          language: <value in [english, simch, japanese, ...]>
          switch_controller: <value in [disable, enable]>
          gui_device_latitude: <string>
          gui_device_longitude: <string>
          hostname: <string>
          timezone: <list or string>
          check_reset_range: <value in [disable, strict]>
          pmtu_discovery: <value in [disable, enable]>
          gui_allow_incompatible_fabric_fgt: <value in [disable, enable]>
          admin_restrict_local: <value in [disable, enable, all, ...]>
          gui_workflow_management: <value in [disable, enable]>
          send_pmtu_icmp: <value in [disable, enable]>
          tcp_halfclose_timer: <integer>
          admin_server_cert: <list or string>
          dnsproxy_worker_count: <integer>
          show_backplane_intf: <value in [disable, enable]>
          gui_custom_language: <value in [disable, enable]>
          ldapconntimeout: <integer>
          auth_https_port: <integer>
          revision_backup_on_logout: <value in [disable, enable]>
          arp_max_entry: <integer>
          long_vdom_name: <value in [disable, enable]>
          pre_login_banner: <value in [disable, enable]>
          qsfpdd_split8_port: <list or string>
          max_route_cache_size: <integer>
          fortitoken_cloud_push_status: <value in [disable, enable]>
          ssh_hostkey_override: <value in [disable, enable]>
          proxy_hardware_acceleration: <value in [disable, enable]>
          switch_controller_reserved_network: <list or string>
          ssd_trim_date: <integer>
          wad_worker_count: <integer>
          ssh_hostkey: <string>
          wireless_controller_port: <integer>
          fgd_alert_subscription:
            - advisory
            - latest-threat
            - latest-virus
            - latest-attack
            - new-antivirus-db
            - new-attack-db
          forticontroller_proxy_port: <integer>
          dh_params: <value in [1024, 1536, 2048, ...]>
          memory_use_threshold_green: <integer>
          proxy_cert_use_mgmt_vdom: <value in [disable, enable]>
          proxy_auth_lifetime_timeout: <integer>
          gui_auto_upgrade_setup_warning: <value in [disable, enable]>
          gui_cdn_usage: <value in [disable, enable]>
          two_factor_email_expiry: <integer>
          udp_idle_timer: <integer>
          interface_subnet_usage: <value in [disable, enable]>
          forticontroller_proxy: <value in [disable, enable]>
          ssh_enc_algo:
            - chacha20-poly1305@openssh.com
            - aes128-ctr
            - aes192-ctr
            - aes256-ctr
            - arcfour256
            - arcfour128
            - aes128-cbc
            - 3des-cbc
            - blowfish-cbc
            - cast128-cbc
            - aes192-cbc
            - aes256-cbc
            - arcfour
            - rijndael-cbc@lysator.liu.se
            - aes128-gcm@openssh.com
            - aes256-gcm@openssh.com
          block_session_timer: <integer>
          quic_pmtud: <value in [disable, enable]>
          admin_https_ssl_ciphersuites:
            - TLS-AES-128-GCM-SHA256
            - TLS-AES-256-GCM-SHA384
            - TLS-CHACHA20-POLY1305-SHA256
            - TLS-AES-128-CCM-SHA256
            - TLS-AES-128-CCM-8-SHA256
          security_rating_result_submission: <value in [disable, enable]>
          user_device_store_max_unified_mem: <integer>
          management_port: <integer>
          fortigslb_integration: <value in [disable, enable]>
          admin_https_ssl_versions:
            - tlsv1-0
            - tlsv1-1
            - tlsv1-2
            - sslv3
            - tlsv1-3
          cert_chain_max: <integer>
          qsfp28_40g_port: <list or string>
          strong_crypto: <value in [disable, enable]>
          multi_factor_authentication: <value in [optional, mandatory]>
          fds_statistics: <value in [disable, enable]>
          gui_display_hostname: <value in [disable, enable]>
          two_factor_ftk_expiry: <integer>
          wad_source_affinity: <value in [disable, enable]>
          ssl_static_key_ciphers: <value in [disable, enable]>
          daily_restart: <value in [disable, enable]>
          snat_route_change: <value in [disable, enable]>
          tcp_rst_timer: <integer>
          anti_replay: <value in [disable, loose, strict]>
          ssl_min_proto_version: <value in [TLSv1, TLSv1-1, TLSv1-2, ...]>
          speedtestd_server_port: <integer>
          cpu_use_threshold: <integer>
          admin_host: <string>
          csr_ca_attribute: <value in [disable, enable]>
          fortiservice_port: <integer>
          ssd_trim_hour: <integer>
          purdue_level: <value in [1, 2, 3, ...]>
          management_vdom: <list or string>
          quic_ack_thresold: <integer>
          qsfpdd_100g_port: <list or string>
          ips_affinity: <string>
          vip_arp_range: <value in [restricted, unlimited]>
          internet_service_database: <value in [mini, standard, full, ...]>
          revision_image_auto_backup: <value in [disable, enable]>
          sflowd_max_children_num: <integer>
          admin_https_pki_required: <value in [disable, enable]>
          special_file_23_support: <value in [disable, enable]>
          npu_neighbor_update: <value in [disable, enable]>
          log_single_cpu_high: <value in [disable, enable]>
          management_ip: <string>
          proxy_resource_mode: <value in [disable, enable]>
          admin_ble_button: <value in [disable, enable]>
          gui_firmware_upgrade_warning: <value in [disable, enable]>
          dp_tcp_normal_timer: <integer>
          ipv6_allow_traffic_redirect: <value in [disable, enable]>
          cli_audit_log: <value in [disable, enable]>
          memory_use_threshold_extreme: <integer>
          ha_affinity: <string>
          restart_time: <string>
          speedtestd_ctrl_port: <integer>
          gui_wireless_opensecurity: <value in [disable, enable]>
          memory_use_threshold_red: <integer>
          dp_fragment_timer: <integer>
          wad_restart_start_time: <string>
          proxy_re_authentication_time: <integer>
          gui_app_detection_sdwan: <value in [disable, enable]>
          scanunit_count: <integer>
          tftp: <value in [disable, enable]>
          xstools_update_frequency: <integer>
          clt_cert_req: <value in [disable, enable]>
          fortiextender_vlan_mode: <value in [disable, enable]>
          auth_http_port: <integer>
          per_user_bal: <value in [disable, enable]>
          gui_date_format: <value in [yyyy/MM/dd, dd/MM/yyyy, MM/dd/yyyy, ...]>
          log_uuid_address: <value in [disable, enable]>
          cloud_communication: <value in [disable, enable]>
          lldp_reception: <value in [disable, enable]>
          two_factor_ftm_expiry: <integer>
          quic_udp_payload_size_shaping_per_cid: <value in [disable, enable]>
          autorun_log_fsck: <value in [disable, enable]>
          vpn_ems_sn_check: <value in [disable, enable]>
          admin_ssh_password: <value in [disable, enable]>
          airplane_mode: <value in [disable, enable]>
          batch_cmdb: <value in [disable, enable]>
          ip_src_port_range: <list or string>
          strict_dirty_session_check: <value in [disable, enable]>
          user_device_store_max_devices: <integer>
          dp_udp_idle_timer: <integer>
          internal_switch_speed:
            - auto
            - 10full
            - 10half
            - 100full
            - 100half
            - 1000full
            - 1000auto
          forticonverter_config_upload: <value in [disable, once]>
          ipsec_round_robin: <value in [disable, enable]>
          wad_affinity: <string>
          wifi_ca_certificate: <list or string>
          wimax_4g_usb: <value in [disable, enable]>
          miglog_affinity: <string>
          faz_disk_buffer_size: <integer>
          ssh_kex_algo:
            - diffie-hellman-group1-sha1
            - diffie-hellman-group14-sha1
            - diffie-hellman-group-exchange-sha1
            - diffie-hellman-group-exchange-sha256
            - curve25519-sha256@libssh.org
            - ecdh-sha2-nistp256
            - ecdh-sha2-nistp384
            - ecdh-sha2-nistp521
            - diffie-hellman-group14-sha256
            - diffie-hellman-group16-sha512
            - diffie-hellman-group18-sha512
          auto_auth_extension_device: <value in [disable, enable]>
          forticarrier_bypass: <value in [disable, enable]>
          reset_sessionless_tcp: <value in [disable, enable]>
          early_tcp_npu_session: <value in [disable, enable]>
          http_unauthenticated_request_limit: <integer>
          gui_local_out: <value in [disable, enable]>
          tcp_option: <value in [disable, enable]>
          proxy_auth_timeout: <integer>
          fortiextender_discovery_lockdown: <value in [disable, enable]>
          lldp_transmission: <value in [disable, enable]>
          split_port: <list or string>
          gui_certificates: <value in [disable, enable]>
          cfg_save: <value in [automatic, manual, revert]>
          auth_keepalive: <value in [disable, enable]>
          split_port_mode:
            -
              interface: <string>
              split_mode: <value in [disable, 4x10G, 4x25G, ...]>
          admin_forticloud_sso_login: <value in [disable, enable]>
          post_login_banner: <value in [disable, enable]>
          br_fdb_max_entry: <integer>
          ip_fragment_mem_thresholds: <integer>
          fortiextender_provision_on_authorization: <value in [disable, enable]>
          reboot_upon_config_restore: <value in [disable, enable]>
          syslog_affinity: <string>
          fortiextender_data_port: <integer>
          quic_tls_handshake_timeout: <integer>
          forticonverter_integration: <value in [disable, enable]>
          proxy_keep_alive_mode: <value in [session, traffic, re-authentication]>
          cmdbsvr_affinity: <string>
          wad_memory_change_granularity: <integer>
          dhcp_lease_backup_interval: <integer>
          check_protocol_header: <value in [loose, strict]>
          av_failopen_session: <value in [disable, enable]>
          ipsec_ha_seqjump_rate: <integer>
          admin_hsts_max_age: <integer>
          igmp_state_limit: <integer>
          admin_login_max: <integer>
          ipv6_allow_multicast_probe: <value in [disable, enable]>
          virtual_switch_vlan: <value in [disable, enable]>
          admin_lockout_threshold: <integer>
          dp_pinhole_timer: <integer>
          wireless_controller: <value in [disable, enable]>
          bfd_affinity: <string>
          ssd_trim_freq: <value in [daily, weekly, monthly, ...]>
          two_factor_sms_expiry: <integer>
          traffic_priority: <value in [tos, dscp]>
          proxy_and_explicit_proxy: <value in [disable, enable]>
          sslvpn_web_mode: <value in [disable, enable]>
          ssh_hostkey_password: <list or string>
          wad_csvc_db_count: <integer>
          ipv6_allow_anycast_probe: <value in [disable, enable]>
          honor_df: <value in [disable, enable]>
          hyper_scale_vdom_num: <integer>
          wad_csvc_cs_count: <integer>
          internal_switch_mode: <value in [switch, interface, hub]>
          cfg_revert_timeout: <integer>
          admin_concurrent: <value in [disable, enable]>
          ipv6_allow_local_in_silent_drop: <value in [disable, enable]>
          tcp_halfopen_timer: <integer>
          dp_rsync_timer: <integer>
          management_port_use_admin_sport: <value in [disable, enable]>
          gui_forticare_registration_setup_warning: <value in [disable, enable]>
          gui_replacement_message_groups: <value in [disable, enable]>
          security_rating_run_on_schedule: <value in [disable, enable]>
          admin_lockout_duration: <integer>
          optimize_flow_mode: <value in [disable, enable]>
          private_data_encryption: <value in [disable, enable]>
          wireless_mode: <value in [ac, client, wtp, ...]>
          alias: <string>
          ssh_hostkey_algo:
            - ssh-rsa
            - ecdsa-sha2-nistp521
            - rsa-sha2-256
            - rsa-sha2-512
            - ssh-ed25519
            - ecdsa-sha2-nistp384
            - ecdsa-sha2-nistp256
          fortitoken_cloud: <value in [disable, enable]>
          av_affinity: <string>
          proxy_worker_count: <integer>
          ipsec_asic_offload: <value in [disable, enable]>
          miglogd_children: <integer>
          sslvpn_max_worker_count: <integer>
          ssh_mac_algo:
            - hmac-md5
            - hmac-md5-etm@openssh.com
            - hmac-md5-96
            - hmac-md5-96-etm@openssh.com
            - hmac-sha1
            - hmac-sha1-etm@openssh.com
            - hmac-sha2-256
            - hmac-sha2-256-etm@openssh.com
            - hmac-sha2-512
            - hmac-sha2-512-etm@openssh.com
            - hmac-ripemd160
            - hmac-ripemd160@openssh.com
            - hmac-ripemd160-etm@openssh.com
            - umac-64@openssh.com
            - umac-128@openssh.com
            - umac-64-etm@openssh.com
            - umac-128-etm@openssh.com
          url_filter_count: <integer>
          wifi_certificate: <list or string>
          radius_port: <integer>
          sys_perf_log_interval: <integer>
          gui_fortigate_cloud_sandbox: <value in [disable, enable]>
          auth_cert: <list or string>
          fortiextender: <value in [disable, enable]>
          admin_reset_button: <value in [disable, enable]>
          av_failopen: <value in [off, pass, one-shot, ...]>
          user_device_store_max_users: <integer>
          auth_session_limit: <value in [block-new, logout-inactive]>
          ipv6_allow_local_in_slient_drop: <value in [disable, enable]>
          quic_congestion_control_algo: <value in [cubic, bbr, bbr2, ...]>
          auth_ike_saml_port: <integer>
          wad_restart_end_time: <string>
          http_request_limit: <integer>
          irq_time_accounting: <value in [auto, force]>
          remoteauthtimeout: <integer>
          admin_https_ssl_banned_ciphers:
            - RSA
            - DHE
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
          allow_traffic_redirect: <value in [disable, enable]>
          legacy_poe_device_support: <value in [disable, enable]>
          wad_restart_mode: <value in [none, time, memory]>
          fds_statistics_period: <integer>
          admin_telnet: <value in [disable, enable]>
          ipv6_accept_dad: <integer>
          tcp_timewait_timer: <integer>
          admin_console_timeout: <integer>
          default_service_source_port: <string>
          quic_max_datagram_size: <integer>
          refresh: <integer>
          extender_controller_reserved_network: <list or string>
          url_filter_affinity: <string>
          policy_auth_concurrent: <integer>
          ipsec_hmac_offload: <value in [disable, enable]>
          traffic_priority_level: <value in [high, medium, low]>
          ipsec_qat_offload: <value in [disable, enable]>
          ssd_trim_min: <integer>
          gui_date_time_source: <value in [system, browser]>
          log_ssl_connection: <value in [disable, enable]>
          ndp_max_entry: <integer>
          vdom_mode: <value in [no-vdom, multi-vdom, split-vdom]>
          internet_service_download_list: <list or string>
          fortitoken_cloud_sync_interval: <integer>
          ssd_trim_weekday: <value in [sunday, monday, tuesday, ...]>
          two_factor_fac_expiry: <integer>
          gui_rest_api_cache: <value in [disable, enable]>
          admin_forticloud_sso_default_profile: <list or string>
          proxy_auth_lifetime: <value in [disable, enable]>
          device_idle_timeout: <integer>
          login_timestamp: <value in [disable, enable]>
          speedtest_server: <value in [disable, enable]>
          edit_vdom_prompt: <value in [disable, enable]>
          gui_cdn_domain_override: <string>
          admin_ssh_grace_time: <integer>
          sslvpn_ems_sn_check: <value in [disable, enable]>
          user_server_cert: <list or string>
          gui_allow_default_hostname: <value in [disable, enable]>
          proxy_re_authentication_mode: <value in [session, traffic, absolute]>
          ipsec_soft_dec_async: <value in [disable, enable]>
          admin_maintainer: <value in [disable, enable]>
          dst: <value in [disable, enable]>
          fec_port: <integer>
          ssh_kex_sha1: <value in [disable, enable]>
          ssh_mac_weak: <value in [disable, enable]>
          sslvpn_cipher_hardware_acceleration: <value in [disable, enable]>
          sys_file_check_interval: <integer>
          ssh_hmac_md5: <value in [disable, enable]>
          ssh_cbc_cipher: <value in [disable, enable]>
          gui_fortiguard_resource_fetch: <value in [disable, enable]>
          sslvpn_kxp_hardware_acceleration: <value in [disable, enable]>
          sslvpn_plugin_version_check: <value in [disable, enable]>
          fortiipam_integration: <value in [disable, enable]>
          gui_firmware_upgrade_setup_warning: <value in [disable, enable]>
          log_uuid_policy: <value in [disable, enable]>
          per_user_bwl: <value in [disable, enable]>
          gui_fortisandbox_cloud: <value in [disable, enable]>
          fortitoken_cloud_service: <value in [disable, enable]>
          hw_switch_ether_filter: <value in [disable, enable]>
          virtual_server_count: <integer>
          endpoint_control_fds_access: <value in [disable, enable]>
          proxy_cipher_hardware_acceleration: <value in [disable, enable]>
          proxy_kxp_hardware_acceleration: <value in [disable, enable]>
          virtual_server_hardware_acceleration: <value in [disable, enable]>
          user_history_password_threshold: <integer>
          delay_tcp_npu_session: <value in [disable, enable]>
          auth_session_auto_backup_interval: <value in [1min, 5min, 15min, ...]>
          ip_conflict_detection: <value in [disable, enable]>
          gtpu_dynamic_source_port: <value in [disable, enable]>
          ip_fragment_timeout: <integer>
          ipv6_fragment_timeout: <integer>
          scim_server_cert: <list or string>
          scim_http_port: <integer>
          auth_session_auto_backup: <value in [disable, enable]>
          scim_https_port: <integer>
          httpd_max_worker_count: <integer>
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
        '/pm/config/adom/{adom}/devprof/{devprof}/system/global'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/devprof/{devprof}/system/global/{global}'
    ]

    url_params = ['adom', 'devprof']
    module_primary_key = None
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'devprof': {'required': True, 'type': 'str'},
        'devprof_system_global': {
            'type': 'dict',
            'v_range': [['6.0.0', '6.2.5'], ['6.2.7', '6.4.1'], ['6.4.3', '']],
            'options': {
                'admin-https-redirect': {
                    'v_range': [['6.0.0', '6.2.5'], ['6.2.7', '6.4.1'], ['6.4.3', '']],
                    'choices': ['disable', 'enable'],
                    'type': 'str'
                },
                'admin-port': {'v_range': [['6.0.0', '6.2.5'], ['6.2.7', '6.4.1'], ['6.4.3', '']], 'type': 'int'},
                'admin-scp': {'v_range': [['6.0.0', '6.2.5'], ['6.2.7', '6.4.1'], ['6.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'admin-sport': {'v_range': [['6.0.0', '6.2.5'], ['6.2.7', '6.4.1'], ['6.4.3', '']], 'type': 'int'},
                'admin-ssh-port': {'v_range': [['6.0.0', '6.2.5'], ['6.2.7', '6.4.1'], ['6.4.3', '']], 'type': 'int'},
                'admin-ssh-v1': {'v_range': [['6.0.0', '6.2.5'], ['6.2.7', '6.4.1'], ['6.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'admin-telnet-port': {
                    'v_range': [['6.0.0', '6.2.5'], ['6.2.7', '6.4.1'], ['6.4.3', '7.2.4'], ['7.4.0', '7.4.1'], ['7.4.3', '']],
                    'type': 'int'
                },
                'admintimeout': {'v_range': [['6.0.0', '6.2.5'], ['6.2.7', '6.4.1'], ['6.4.3', '']], 'type': 'int'},
                'gui-ipv6': {'v_range': [['6.0.0', '6.2.5'], ['6.2.7', '6.4.1'], ['6.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'gui-lines-per-page': {'v_range': [['6.0.0', '6.2.5'], ['6.2.7', '6.4.1'], ['6.4.3', '']], 'type': 'int'},
                'gui-theme': {
                    'v_range': [['6.0.0', '6.2.5'], ['6.2.7', '6.4.1'], ['6.4.3', '']],
                    'choices': [
                        'blue', 'green', 'melongene', 'red', 'mariner', 'neutrino', 'jade', 'graphite', 'dark-matter', 'onyx', 'eclipse', 'retro', 'fpx',
                        'jet-stream', 'security-fabric'
                    ],
                    'type': 'str'
                },
                'language': {
                    'v_range': [['6.0.0', '6.2.5'], ['6.2.7', '6.4.1'], ['6.4.3', '']],
                    'choices': ['english', 'simch', 'japanese', 'korean', 'spanish', 'trach', 'french', 'portuguese'],
                    'type': 'str'
                },
                'switch-controller': {
                    'v_range': [['6.0.0', '6.2.5'], ['6.2.7', '6.4.1'], ['6.4.3', '7.2.0'], ['7.4.3', '']],
                    'choices': ['disable', 'enable'],
                    'type': 'str'
                },
                'gui-device-latitude': {'v_range': [['7.4.3', '']], 'type': 'str'},
                'gui-device-longitude': {'v_range': [['7.4.3', '']], 'type': 'str'},
                'hostname': {'v_range': [['7.4.3', '']], 'type': 'str'},
                'timezone': {'v_range': [['7.4.3', '']], 'type': 'raw'},
                'check-reset-range': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'strict'], 'type': 'str'},
                'pmtu-discovery': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'gui-allow-incompatible-fabric-fgt': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'admin-restrict-local': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable', 'all', 'non-console-only'], 'type': 'str'},
                'gui-workflow-management': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'send-pmtu-icmp': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'tcp-halfclose-timer': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'admin-server-cert': {'v_range': [['7.4.3', '']], 'type': 'raw'},
                'dnsproxy-worker-count': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'show-backplane-intf': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'gui-custom-language': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ldapconntimeout': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'auth-https-port': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'revision-backup-on-logout': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'arp-max-entry': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'long-vdom-name': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'pre-login-banner': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'qsfpdd-split8-port': {'v_range': [['7.4.3', '']], 'type': 'raw'},
                'max-route-cache-size': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'fortitoken-cloud-push-status': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ssh-hostkey-override': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'proxy-hardware-acceleration': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'switch-controller-reserved-network': {'v_range': [['7.4.3', '']], 'type': 'raw'},
                'ssd-trim-date': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'wad-worker-count': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'ssh-hostkey': {'v_range': [['7.4.3', '']], 'no_log': True, 'type': 'str'},
                'wireless-controller-port': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'fgd-alert-subscription': {
                    'v_range': [['7.4.3', '']],
                    'type': 'list',
                    'choices': ['advisory', 'latest-threat', 'latest-virus', 'latest-attack', 'new-antivirus-db', 'new-attack-db'],
                    'elements': 'str'
                },
                'forticontroller-proxy-port': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'dh-params': {'v_range': [['7.4.3', '']], 'choices': ['1024', '1536', '2048', '3072', '4096', '6144', '8192'], 'type': 'str'},
                'memory-use-threshold-green': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'proxy-cert-use-mgmt-vdom': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'proxy-auth-lifetime-timeout': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'gui-auto-upgrade-setup-warning': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'gui-cdn-usage': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'two-factor-email-expiry': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'udp-idle-timer': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'interface-subnet-usage': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'forticontroller-proxy': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ssh-enc-algo': {
                    'v_range': [['7.4.3', '']],
                    'type': 'list',
                    'choices': [
                        'chacha20-poly1305@openssh.com', 'aes128-ctr', 'aes192-ctr', 'aes256-ctr', 'arcfour256', 'arcfour128', 'aes128-cbc', '3des-cbc',
                        'blowfish-cbc', 'cast128-cbc', 'aes192-cbc', 'aes256-cbc', 'arcfour', 'rijndael-cbc@lysator.liu.se', 'aes128-gcm@openssh.com',
                        'aes256-gcm@openssh.com'
                    ],
                    'elements': 'str'
                },
                'block-session-timer': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'quic-pmtud': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'admin-https-ssl-ciphersuites': {
                    'v_range': [['7.4.3', '']],
                    'type': 'list',
                    'choices': [
                        'TLS-AES-128-GCM-SHA256', 'TLS-AES-256-GCM-SHA384', 'TLS-CHACHA20-POLY1305-SHA256', 'TLS-AES-128-CCM-SHA256',
                        'TLS-AES-128-CCM-8-SHA256'
                    ],
                    'elements': 'str'
                },
                'security-rating-result-submission': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'user-device-store-max-unified-mem': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'management-port': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'fortigslb-integration': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'admin-https-ssl-versions': {
                    'v_range': [['7.4.3', '']],
                    'type': 'list',
                    'choices': ['tlsv1-0', 'tlsv1-1', 'tlsv1-2', 'sslv3', 'tlsv1-3'],
                    'elements': 'str'
                },
                'cert-chain-max': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'qsfp28-40g-port': {'v_range': [['7.4.3', '']], 'type': 'raw'},
                'strong-crypto': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'multi-factor-authentication': {'v_range': [['7.4.3', '']], 'choices': ['optional', 'mandatory'], 'type': 'str'},
                'fds-statistics': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'gui-display-hostname': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'two-factor-ftk-expiry': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'wad-source-affinity': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ssl-static-key-ciphers': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'daily-restart': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'snat-route-change': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'tcp-rst-timer': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'anti-replay': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'loose', 'strict'], 'type': 'str'},
                'ssl-min-proto-version': {'v_range': [['7.4.3', '']], 'choices': ['TLSv1', 'TLSv1-1', 'TLSv1-2', 'SSLv3', 'TLSv1-3'], 'type': 'str'},
                'speedtestd-server-port': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'cpu-use-threshold': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'admin-host': {'v_range': [['7.4.3', '']], 'type': 'str'},
                'csr-ca-attribute': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'fortiservice-port': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'ssd-trim-hour': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'purdue-level': {'v_range': [['7.4.3', '']], 'choices': ['1', '2', '3', '4', '5', '1.5', '2.5', '3.5', '5.5'], 'type': 'str'},
                'management-vdom': {'v_range': [['7.4.3', '']], 'type': 'raw'},
                'quic-ack-thresold': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'qsfpdd-100g-port': {'v_range': [['7.4.3', '']], 'type': 'raw'},
                'ips-affinity': {'v_range': [['7.4.3', '']], 'type': 'str'},
                'vip-arp-range': {'v_range': [['7.4.3', '']], 'choices': ['restricted', 'unlimited'], 'type': 'str'},
                'internet-service-database': {'v_range': [['7.4.3', '']], 'choices': ['mini', 'standard', 'full', 'on-demand'], 'type': 'str'},
                'revision-image-auto-backup': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'sflowd-max-children-num': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'admin-https-pki-required': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'special-file-23-support': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'npu-neighbor-update': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'log-single-cpu-high': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'management-ip': {'v_range': [['7.4.3', '']], 'type': 'str'},
                'proxy-resource-mode': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'admin-ble-button': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'gui-firmware-upgrade-warning': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'dp-tcp-normal-timer': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'ipv6-allow-traffic-redirect': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'cli-audit-log': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'memory-use-threshold-extreme': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'ha-affinity': {'v_range': [['7.4.3', '']], 'type': 'str'},
                'restart-time': {'v_range': [['7.4.3', '']], 'type': 'str'},
                'speedtestd-ctrl-port': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'gui-wireless-opensecurity': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'memory-use-threshold-red': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'dp-fragment-timer': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'wad-restart-start-time': {'v_range': [['7.4.3', '']], 'type': 'str'},
                'proxy-re-authentication-time': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'gui-app-detection-sdwan': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'scanunit-count': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'tftp': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'xstools-update-frequency': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'clt-cert-req': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'fortiextender-vlan-mode': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'auth-http-port': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'per-user-bal': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'gui-date-format': {
                    'v_range': [['7.4.3', '']],
                    'choices': ['yyyy/MM/dd', 'dd/MM/yyyy', 'MM/dd/yyyy', 'yyyy-MM-dd', 'dd-MM-yyyy', 'MM-dd-yyyy'],
                    'type': 'str'
                },
                'log-uuid-address': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'cloud-communication': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'lldp-reception': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'two-factor-ftm-expiry': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'quic-udp-payload-size-shaping-per-cid': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'autorun-log-fsck': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'vpn-ems-sn-check': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'admin-ssh-password': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'airplane-mode': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'batch-cmdb': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ip-src-port-range': {'v_range': [['7.4.3', '']], 'type': 'raw'},
                'strict-dirty-session-check': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'user-device-store-max-devices': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'dp-udp-idle-timer': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'internal-switch-speed': {
                    'v_range': [['7.4.3', '']],
                    'type': 'list',
                    'choices': ['auto', '10full', '10half', '100full', '100half', '1000full', '1000auto'],
                    'elements': 'str'
                },
                'forticonverter-config-upload': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'once'], 'type': 'str'},
                'ipsec-round-robin': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'wad-affinity': {'v_range': [['7.4.3', '']], 'type': 'str'},
                'wifi-ca-certificate': {'v_range': [['7.4.3', '']], 'type': 'raw'},
                'wimax-4g-usb': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'miglog-affinity': {'v_range': [['7.4.3', '']], 'type': 'str'},
                'faz-disk-buffer-size': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'ssh-kex-algo': {
                    'v_range': [['7.4.3', '']],
                    'type': 'list',
                    'choices': [
                        'diffie-hellman-group1-sha1', 'diffie-hellman-group14-sha1', 'diffie-hellman-group-exchange-sha1',
                        'diffie-hellman-group-exchange-sha256', 'curve25519-sha256@libssh.org', 'ecdh-sha2-nistp256', 'ecdh-sha2-nistp384',
                        'ecdh-sha2-nistp521', 'diffie-hellman-group14-sha256', 'diffie-hellman-group16-sha512', 'diffie-hellman-group18-sha512'
                    ],
                    'elements': 'str'
                },
                'auto-auth-extension-device': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'forticarrier-bypass': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'reset-sessionless-tcp': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'early-tcp-npu-session': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'http-unauthenticated-request-limit': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'gui-local-out': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'tcp-option': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'proxy-auth-timeout': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'fortiextender-discovery-lockdown': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'lldp-transmission': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'split-port': {'v_range': [['7.4.3', '']], 'type': 'raw'},
                'gui-certificates': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'cfg-save': {'v_range': [['7.4.3', '']], 'choices': ['automatic', 'manual', 'revert'], 'type': 'str'},
                'auth-keepalive': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'split-port-mode': {
                    'v_range': [['7.4.3', '']],
                    'type': 'list',
                    'options': {
                        'interface': {'v_range': [['7.4.3', '']], 'type': 'str'},
                        'split-mode': {
                            'v_range': [['7.4.3', '']],
                            'choices': ['disable', '4x10G', '4x25G', '4x50G', '8x50G', '4x100G', '2x200G', '8x25G'],
                            'type': 'str'
                        }
                    },
                    'elements': 'dict'
                },
                'admin-forticloud-sso-login': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'post-login-banner': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'br-fdb-max-entry': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'ip-fragment-mem-thresholds': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'fortiextender-provision-on-authorization': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'reboot-upon-config-restore': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'syslog-affinity': {'v_range': [['7.4.3', '']], 'type': 'str'},
                'fortiextender-data-port': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'quic-tls-handshake-timeout': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'forticonverter-integration': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'proxy-keep-alive-mode': {'v_range': [['7.4.3', '']], 'choices': ['session', 'traffic', 're-authentication'], 'type': 'str'},
                'cmdbsvr-affinity': {'v_range': [['7.4.3', '']], 'type': 'str'},
                'wad-memory-change-granularity': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'dhcp-lease-backup-interval': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'check-protocol-header': {'v_range': [['7.4.3', '']], 'choices': ['loose', 'strict'], 'type': 'str'},
                'av-failopen-session': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ipsec-ha-seqjump-rate': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'admin-hsts-max-age': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'igmp-state-limit': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'admin-login-max': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'ipv6-allow-multicast-probe': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'virtual-switch-vlan': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'admin-lockout-threshold': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'dp-pinhole-timer': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'wireless-controller': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'bfd-affinity': {'v_range': [['7.4.3', '']], 'type': 'str'},
                'ssd-trim-freq': {'v_range': [['7.4.3', '']], 'choices': ['daily', 'weekly', 'monthly', 'hourly', 'never'], 'type': 'str'},
                'two-factor-sms-expiry': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'traffic-priority': {'v_range': [['7.4.3', '']], 'choices': ['tos', 'dscp'], 'type': 'str'},
                'proxy-and-explicit-proxy': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'sslvpn-web-mode': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ssh-hostkey-password': {'v_range': [['7.4.3', '']], 'no_log': True, 'type': 'raw'},
                'wad-csvc-db-count': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'ipv6-allow-anycast-probe': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'honor-df': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'hyper-scale-vdom-num': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'wad-csvc-cs-count': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'internal-switch-mode': {'v_range': [['7.4.3', '']], 'choices': ['switch', 'interface', 'hub'], 'type': 'str'},
                'cfg-revert-timeout': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'admin-concurrent': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ipv6-allow-local-in-silent-drop': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'tcp-halfopen-timer': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'dp-rsync-timer': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'management-port-use-admin-sport': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'gui-forticare-registration-setup-warning': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'gui-replacement-message-groups': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'security-rating-run-on-schedule': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'admin-lockout-duration': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'optimize-flow-mode': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'private-data-encryption': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'wireless-mode': {'v_range': [['7.4.3', '']], 'choices': ['ac', 'client', 'wtp', 'fwfap'], 'type': 'str'},
                'alias': {'v_range': [['7.4.3', '']], 'type': 'str'},
                'ssh-hostkey-algo': {
                    'v_range': [['7.4.3', '']],
                    'type': 'list',
                    'choices': [
                        'ssh-rsa', 'ecdsa-sha2-nistp521', 'rsa-sha2-256', 'rsa-sha2-512', 'ssh-ed25519', 'ecdsa-sha2-nistp384', 'ecdsa-sha2-nistp256'
                    ],
                    'elements': 'str'
                },
                'fortitoken-cloud': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'av-affinity': {'v_range': [['7.4.3', '']], 'type': 'str'},
                'proxy-worker-count': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'ipsec-asic-offload': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'miglogd-children': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'sslvpn-max-worker-count': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'ssh-mac-algo': {
                    'v_range': [['7.4.3', '']],
                    'type': 'list',
                    'choices': [
                        'hmac-md5', 'hmac-md5-etm@openssh.com', 'hmac-md5-96', 'hmac-md5-96-etm@openssh.com', 'hmac-sha1', 'hmac-sha1-etm@openssh.com',
                        'hmac-sha2-256', 'hmac-sha2-256-etm@openssh.com', 'hmac-sha2-512', 'hmac-sha2-512-etm@openssh.com', 'hmac-ripemd160',
                        'hmac-ripemd160@openssh.com', 'hmac-ripemd160-etm@openssh.com', 'umac-64@openssh.com', 'umac-128@openssh.com',
                        'umac-64-etm@openssh.com', 'umac-128-etm@openssh.com'
                    ],
                    'elements': 'str'
                },
                'url-filter-count': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'wifi-certificate': {'v_range': [['7.4.3', '']], 'type': 'raw'},
                'radius-port': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'sys-perf-log-interval': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'gui-fortigate-cloud-sandbox': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'auth-cert': {'v_range': [['7.4.3', '']], 'type': 'raw'},
                'fortiextender': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'admin-reset-button': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'av-failopen': {'v_range': [['7.4.3', '']], 'choices': ['off', 'pass', 'one-shot', 'idledrop'], 'type': 'str'},
                'user-device-store-max-users': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'auth-session-limit': {'v_range': [['7.4.3', '']], 'choices': ['block-new', 'logout-inactive'], 'type': 'str'},
                'ipv6-allow-local-in-slient-drop': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'quic-congestion-control-algo': {'v_range': [['7.4.3', '']], 'choices': ['cubic', 'bbr', 'bbr2', 'reno'], 'type': 'str'},
                'auth-ike-saml-port': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'wad-restart-end-time': {'v_range': [['7.4.3', '']], 'type': 'str'},
                'http-request-limit': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'irq-time-accounting': {'v_range': [['7.4.3', '']], 'choices': ['auto', 'force'], 'type': 'str'},
                'remoteauthtimeout': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'admin-https-ssl-banned-ciphers': {
                    'v_range': [['7.4.3', '']],
                    'type': 'list',
                    'choices': [
                        'RSA', 'DHE', 'ECDHE', 'DSS', 'ECDSA', 'AES', 'AESGCM', 'CAMELLIA', '3DES', 'SHA1', 'SHA256', 'SHA384', 'STATIC', 'CHACHA20',
                        'ARIA', 'AESCCM'
                    ],
                    'elements': 'str'
                },
                'allow-traffic-redirect': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'legacy-poe-device-support': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'wad-restart-mode': {'v_range': [['7.4.3', '']], 'choices': ['none', 'time', 'memory'], 'type': 'str'},
                'fds-statistics-period': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'admin-telnet': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ipv6-accept-dad': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'tcp-timewait-timer': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'admin-console-timeout': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'default-service-source-port': {'v_range': [['7.4.3', '']], 'type': 'str'},
                'quic-max-datagram-size': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'refresh': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'extender-controller-reserved-network': {'v_range': [['7.4.3', '']], 'type': 'raw'},
                'url-filter-affinity': {'v_range': [['7.4.3', '']], 'type': 'str'},
                'policy-auth-concurrent': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'ipsec-hmac-offload': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'traffic-priority-level': {'v_range': [['7.4.3', '']], 'choices': ['high', 'medium', 'low'], 'type': 'str'},
                'ipsec-qat-offload': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ssd-trim-min': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'gui-date-time-source': {'v_range': [['7.4.3', '']], 'choices': ['system', 'browser'], 'type': 'str'},
                'log-ssl-connection': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ndp-max-entry': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'vdom-mode': {'v_range': [['7.4.3', '']], 'choices': ['no-vdom', 'multi-vdom', 'split-vdom'], 'type': 'str'},
                'internet-service-download-list': {'v_range': [['7.4.3', '']], 'type': 'raw'},
                'fortitoken-cloud-sync-interval': {'v_range': [['7.4.3', '']], 'no_log': True, 'type': 'int'},
                'ssd-trim-weekday': {
                    'v_range': [['7.4.3', '']],
                    'choices': ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'],
                    'type': 'str'
                },
                'two-factor-fac-expiry': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'gui-rest-api-cache': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'admin-forticloud-sso-default-profile': {'v_range': [['7.4.3', '']], 'type': 'raw'},
                'proxy-auth-lifetime': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'device-idle-timeout': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'login-timestamp': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'speedtest-server': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'edit-vdom-prompt': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'gui-cdn-domain-override': {'v_range': [['7.4.3', '']], 'type': 'str'},
                'admin-ssh-grace-time': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'sslvpn-ems-sn-check': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'user-server-cert': {'v_range': [['7.4.3', '']], 'type': 'raw'},
                'gui-allow-default-hostname': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'proxy-re-authentication-mode': {'v_range': [['7.4.3', '']], 'choices': ['session', 'traffic', 'absolute'], 'type': 'str'},
                'ipsec-soft-dec-async': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'admin-maintainer': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'dst': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'fec-port': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'ssh-kex-sha1': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ssh-mac-weak': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'sslvpn-cipher-hardware-acceleration': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'sys-file-check-interval': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'ssh-hmac-md5': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ssh-cbc-cipher': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'gui-fortiguard-resource-fetch': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'sslvpn-kxp-hardware-acceleration': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'sslvpn-plugin-version-check': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'fortiipam-integration': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'gui-firmware-upgrade-setup-warning': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'log-uuid-policy': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'per-user-bwl': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'gui-fortisandbox-cloud': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'fortitoken-cloud-service': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'hw-switch-ether-filter': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'virtual-server-count': {'v_range': [['7.4.3', '']], 'type': 'int'},
                'endpoint-control-fds-access': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'proxy-cipher-hardware-acceleration': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'proxy-kxp-hardware-acceleration': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'virtual-server-hardware-acceleration': {'v_range': [['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'user-history-password-threshold': {'v_range': [['7.6.0', '']], 'no_log': True, 'type': 'int'},
                'delay-tcp-npu-session': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'auth-session-auto-backup-interval': {'v_range': [['7.6.0', '']], 'choices': ['1min', '5min', '15min', '30min', '1hr'], 'type': 'str'},
                'ip-conflict-detection': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'gtpu-dynamic-source-port': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ip-fragment-timeout': {'v_range': [['7.6.0', '']], 'type': 'int'},
                'ipv6-fragment-timeout': {'v_range': [['7.6.0', '']], 'type': 'int'},
                'scim-server-cert': {'v_range': [['7.6.0', '']], 'type': 'raw'},
                'scim-http-port': {'v_range': [['7.6.0', '']], 'type': 'int'},
                'auth-session-auto-backup': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'scim-https-port': {'v_range': [['7.6.0', '']], 'type': 'int'},
                'httpd-max-worker-count': {'v_range': [['7.6.0', '']], 'type': 'int'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('partial crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'devprof_system_global'),
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
