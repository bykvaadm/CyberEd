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
module: fmgr_wtpprofile_radio2
short_description: Configuration options for radio 2.
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
    wtp-profile:
        description: Deprecated, please use "wtp_profile"
        type: str
    wtp_profile:
        description: The parameter (wtp-profile) in requested url.
        type: str
    wtpprofile_radio2:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            amsdu:
                type: str
                description: Enable/disable 802.
                choices:
                    - 'disable'
                    - 'enable'
            ap-handoff:
                type: str
                description: Deprecated, please rename it to ap_handoff. Enable/disable AP handoff of clients to other APs
                choices:
                    - 'disable'
                    - 'enable'
            ap-sniffer-addr:
                type: str
                description: Deprecated, please rename it to ap_sniffer_addr. MAC address to monitor.
            ap-sniffer-bufsize:
                type: int
                description: Deprecated, please rename it to ap_sniffer_bufsize. Sniffer buffer size
            ap-sniffer-chan:
                type: int
                description: Deprecated, please rename it to ap_sniffer_chan. Channel on which to operate the sniffer
            ap-sniffer-ctl:
                type: str
                description: Deprecated, please rename it to ap_sniffer_ctl. Enable/disable sniffer on WiFi control frame
                choices:
                    - 'disable'
                    - 'enable'
            ap-sniffer-data:
                type: str
                description: Deprecated, please rename it to ap_sniffer_data. Enable/disable sniffer on WiFi data frame
                choices:
                    - 'disable'
                    - 'enable'
            ap-sniffer-mgmt-beacon:
                type: str
                description: Deprecated, please rename it to ap_sniffer_mgmt_beacon. Enable/disable sniffer on WiFi management Beacon frames
                choices:
                    - 'disable'
                    - 'enable'
            ap-sniffer-mgmt-other:
                type: str
                description: Deprecated, please rename it to ap_sniffer_mgmt_other. Enable/disable sniffer on WiFi management other frames
                choices:
                    - 'disable'
                    - 'enable'
            ap-sniffer-mgmt-probe:
                type: str
                description: Deprecated, please rename it to ap_sniffer_mgmt_probe. Enable/disable sniffer on WiFi management probe frames
                choices:
                    - 'disable'
                    - 'enable'
            auto-power-high:
                type: int
                description: Deprecated, please rename it to auto_power_high. Automatic transmit power high limit in dBm
            auto-power-level:
                type: str
                description: Deprecated, please rename it to auto_power_level. Enable/disable automatic power-level adjustment to prevent co-channel in...
                choices:
                    - 'disable'
                    - 'enable'
            auto-power-low:
                type: int
                description: Deprecated, please rename it to auto_power_low. Automatic transmission power low limit in dBm
            band:
                type: str
                description: WiFi band that Radio 2 operates on.
                choices:
                    - '802.11b'
                    - '802.11a'
                    - '802.11g'
                    - '802.11n'
                    - '802.11ac'
                    - '802.11n-5G'
                    - '802.11g-only'
                    - '802.11n-only'
                    - '802.11n,g-only'
                    - '802.11ac-only'
                    - '802.11ac,n-only'
                    - '802.11n-5G-only'
                    - '802.11ax-5G'
                    - '802.11ax'
                    - '802.11ax-5G-only'
                    - '802.11ax,ac-only'
                    - '802.11ax,ac,n-only'
                    - '802.11ax-only'
                    - '802.11ax,n-only'
                    - '802.11ax,n,g-only'
                    - '802.11ac-2G'
                    - '802.11ax-6G'
                    - '802.11n-2G'
                    - '802.11ac-5G'
                    - '802.11ax-2G'
                    - '802.11be-2G'
                    - '802.11be-5G'
                    - '802.11be-6G'
            bandwidth-admission-control:
                type: str
                description: Deprecated, please rename it to bandwidth_admission_control. Enable/disable WiFi multimedia
                choices:
                    - 'disable'
                    - 'enable'
            bandwidth-capacity:
                type: int
                description: Deprecated, please rename it to bandwidth_capacity. Maximum bandwidth capacity allowed
            beacon-interval:
                type: int
                description: Deprecated, please rename it to beacon_interval. Beacon interval.
            call-admission-control:
                type: str
                description: Deprecated, please rename it to call_admission_control. Enable/disable WiFi multimedia
                choices:
                    - 'disable'
                    - 'enable'
            call-capacity:
                type: int
                description: Deprecated, please rename it to call_capacity. Maximum number of Voice over WLAN
            channel:
                type: raw
                description: (list) Selected list of wireless radio channels.
            channel-bonding:
                type: str
                description: Deprecated, please rename it to channel_bonding. Channel bandwidth
                choices:
                    - 'disable'
                    - 'enable'
                    - '80MHz'
                    - '40MHz'
                    - '20MHz'
                    - '160MHz'
                    - '320MHz'
                    - '240MHz'
            channel-utilization:
                type: str
                description: Deprecated, please rename it to channel_utilization. Enable/disable measuring channel utilization.
                choices:
                    - 'disable'
                    - 'enable'
            coexistence:
                type: str
                description: Enable/disable allowing both HT20 and HT40 on the same radio
                choices:
                    - 'disable'
                    - 'enable'
            darrp:
                type: str
                description: Enable/disable Distributed Automatic Radio Resource Provisioning
                choices:
                    - 'disable'
                    - 'enable'
            dtim:
                type: int
                description: DTIM interval.
            frag-threshold:
                type: int
                description: Deprecated, please rename it to frag_threshold. Maximum packet size that can be sent without fragmentation
            frequency-handoff:
                type: str
                description: Deprecated, please rename it to frequency_handoff. Enable/disable frequency handoff of clients to other channels
                choices:
                    - 'disable'
                    - 'enable'
            max-clients:
                type: int
                description: Deprecated, please rename it to max_clients. Maximum number of stations
            max-distance:
                type: int
                description: Deprecated, please rename it to max_distance. Maximum expected distance between the AP and clients
            mode:
                type: str
                description: Mode of radio 2.
                choices:
                    - 'disabled'
                    - 'ap'
                    - 'monitor'
                    - 'sniffer'
                    - 'sam'
            power-level:
                type: int
                description: Deprecated, please rename it to power_level. Radio power level as a percentage of the maximum transmit power
            powersave-optimize:
                type: list
                elements: str
                description: Deprecated, please rename it to powersave_optimize. Enable client power-saving features such as TIM, AC VO, and OBSS etc.
                choices:
                    - 'tim'
                    - 'ac-vo'
                    - 'no-obss-scan'
                    - 'no-11b-rate'
                    - 'client-rate-follow'
            protection-mode:
                type: str
                description: Deprecated, please rename it to protection_mode. Enable/disable 802.
                choices:
                    - 'rtscts'
                    - 'ctsonly'
                    - 'disable'
            radio-id:
                type: int
                description: Deprecated, please rename it to radio_id. Radio id.
            rts-threshold:
                type: int
                description: Deprecated, please rename it to rts_threshold. Maximum packet size for RTS transmissions, specifying the maximum size of a...
            short-guard-interval:
                type: str
                description: Deprecated, please rename it to short_guard_interval. Use either the short guard interval
                choices:
                    - 'disable'
                    - 'enable'
            spectrum-analysis:
                type: str
                description: Deprecated, please rename it to spectrum_analysis. Enable/disable spectrum analysis to find interference that would negati...
                choices:
                    - 'disable'
                    - 'enable'
                    - 'scan-only'
            transmit-optimize:
                type: list
                elements: str
                description: Deprecated, please rename it to transmit_optimize. Packet transmission optimization options including power saving, aggreg...
                choices:
                    - 'disable'
                    - 'power-save'
                    - 'aggr-limit'
                    - 'retry-limit'
                    - 'send-bar'
            vap-all:
                type: str
                description: Deprecated, please rename it to vap_all. Enable/disable the automatic inheritance of all Virtual Access Points
                choices:
                    - 'disable'
                    - 'enable'
                    - 'tunnel'
                    - 'bridge'
                    - 'manual'
            vaps:
                type: raw
                description: (list or str) Manually selected list of Virtual Access Points
            wids-profile:
                type: str
                description: Deprecated, please rename it to wids_profile. Wireless Intrusion Detection System
            airtime-fairness:
                type: str
                description: Deprecated, please rename it to airtime_fairness. Enable/disable airtime fairness
                choices:
                    - 'disable'
                    - 'enable'
            band-5g-type:
                type: str
                description: Deprecated, please rename it to band_5g_type. WiFi 5G band type.
                choices:
                    - '5g-full'
                    - '5g-high'
                    - '5g-low'
            zero-wait-dfs:
                type: str
                description: Deprecated, please rename it to zero_wait_dfs. Enable/disable zero wait DFS on radio
                choices:
                    - 'disable'
                    - 'enable'
            vap1:
                type: str
                description: Virtual Access Point
            vap2:
                type: str
                description: Virtual Access Point
            vap3:
                type: str
                description: Virtual Access Point
            vap4:
                type: str
                description: Virtual Access Point
            vap5:
                type: str
                description: Virtual Access Point
            vap6:
                type: str
                description: Virtual Access Point
            vap7:
                type: str
                description: Virtual Access Point
            vap8:
                type: str
                description: Virtual Access Point
            bss-color:
                type: int
                description: Deprecated, please rename it to bss_color. BSS color value for this 11ax radio
            auto-power-target:
                type: str
                description: Deprecated, please rename it to auto_power_target. The target of automatic transmit power adjustment in dBm.
            drma:
                type: str
                description: Enable/disable dynamic radio mode assignment
                choices:
                    - 'disable'
                    - 'enable'
            drma-sensitivity:
                type: str
                description: Deprecated, please rename it to drma_sensitivity. Network Coverage Factor
                choices:
                    - 'low'
                    - 'medium'
                    - 'high'
            iperf-protocol:
                type: str
                description: Deprecated, please rename it to iperf_protocol. Iperf test protocol
                choices:
                    - 'udp'
                    - 'tcp'
            iperf-server-port:
                type: int
                description: Deprecated, please rename it to iperf_server_port. Iperf service port number.
            power-mode:
                type: str
                description: Deprecated, please rename it to power_mode. Set radio effective isotropic radiated power
                choices:
                    - 'dBm'
                    - 'percentage'
            power-value:
                type: int
                description: Deprecated, please rename it to power_value. Radio EIRP power in dBm
            sam-bssid:
                type: str
                description: Deprecated, please rename it to sam_bssid. BSSID for WiFi network.
            sam-captive-portal:
                type: str
                description: Deprecated, please rename it to sam_captive_portal. Enable/disable Captive Portal Authentication
                choices:
                    - 'disable'
                    - 'enable'
            sam-password:
                type: raw
                description: (list) Deprecated, please rename it to sam_password. Passphrase for WiFi network connection.
            sam-report-intv:
                type: int
                description: Deprecated, please rename it to sam_report_intv. SAM report interval
            sam-security-type:
                type: str
                description: Deprecated, please rename it to sam_security_type. Select WiFi network security type
                choices:
                    - 'open'
                    - 'wpa-personal'
                    - 'wpa-enterprise'
                    - 'owe'
                    - 'wpa3-sae'
            sam-server:
                type: str
                description: Deprecated, please rename it to sam_server. SAM test server IP address or domain name.
            sam-ssid:
                type: str
                description: Deprecated, please rename it to sam_ssid. SSID for WiFi network.
            sam-test:
                type: str
                description: Deprecated, please rename it to sam_test. Select SAM test type
                choices:
                    - 'ping'
                    - 'iperf'
            sam-username:
                type: str
                description: Deprecated, please rename it to sam_username. Username for WiFi network connection.
            arrp-profile:
                type: str
                description: Deprecated, please rename it to arrp_profile. Distributed Automatic Radio Resource Provisioning
            bss-color-mode:
                type: str
                description: Deprecated, please rename it to bss_color_mode. BSS color mode for this 11ax radio
                choices:
                    - 'auto'
                    - 'static'
            sam-cwp-failure-string:
                type: str
                description: Deprecated, please rename it to sam_cwp_failure_string. Failure identification on the page after an incorrect login.
            sam-cwp-match-string:
                type: str
                description: Deprecated, please rename it to sam_cwp_match_string. Identification string from the captive portal login form.
            sam-cwp-password:
                type: raw
                description: (list) Deprecated, please rename it to sam_cwp_password. Password for captive portal authentication.
            sam-cwp-success-string:
                type: str
                description: Deprecated, please rename it to sam_cwp_success_string. Success identification on the page after a successful login.
            sam-cwp-test-url:
                type: str
                description: Deprecated, please rename it to sam_cwp_test_url. Website the client is trying to access.
            sam-cwp-username:
                type: str
                description: Deprecated, please rename it to sam_cwp_username. Username for captive portal authentication.
            sam-server-fqdn:
                type: str
                description: Deprecated, please rename it to sam_server_fqdn. SAM test server domain name.
            sam-server-ip:
                type: str
                description: Deprecated, please rename it to sam_server_ip. SAM test server IP address.
            sam-server-type:
                type: str
                description: Deprecated, please rename it to sam_server_type. Select SAM server type
                choices:
                    - 'ip'
                    - 'fqdn'
            80211d:
                type: str
                description: Deprecated, please rename it to d80211d. Enable/disable 802.
                choices:
                    - 'disable'
                    - 'enable'
            optional-antenna:
                type: str
                description: Deprecated, please rename it to optional_antenna. Optional antenna used on FAP
                choices:
                    - 'none'
                    - 'FANT-04ABGN-0606-O-N'
                    - 'FANT-04ABGN-1414-P-N'
                    - 'FANT-04ABGN-8065-P-N'
                    - 'FANT-04ABGN-0606-O-R'
                    - 'FANT-04ABGN-0606-P-R'
                    - 'FANT-10ACAX-1213-D-N'
                    - 'FANT-08ABGN-1213-D-R'
                    - 'custom'
            mimo-mode:
                type: str
                description: Deprecated, please rename it to mimo_mode. Configure radio MIMO mode
                choices:
                    - 'default'
                    - '1x1'
                    - '2x2'
                    - '3x3'
                    - '4x4'
                    - '8x8'
            optional-antenna-gain:
                type: str
                description: Deprecated, please rename it to optional_antenna_gain. Optional antenna gain in dBi
            sam-ca-certificate:
                type: str
                description: Deprecated, please rename it to sam_ca_certificate. CA certificate for WPA2/WPA3-ENTERPRISE.
            sam-client-certificate:
                type: str
                description: Deprecated, please rename it to sam_client_certificate. Client certificate for WPA2/WPA3-ENTERPRISE.
            sam-eap-method:
                type: str
                description: Deprecated, please rename it to sam_eap_method. Select WPA2/WPA3-ENTERPRISE EAP Method
                choices:
                    - 'tls'
                    - 'peap'
                    - 'both'
            sam-private-key:
                type: str
                description: Deprecated, please rename it to sam_private_key. Private key for WPA2/WPA3-ENTERPRISE.
            sam-private-key-password:
                type: raw
                description: (list) Deprecated, please rename it to sam_private_key_password. Password for private key file for WPA2/WPA3-ENTERPRISE.
            channel-bonding-ext:
                type: str
                description: Deprecated, please rename it to channel_bonding_ext. Channel bandwidth extension
                choices:
                    - '320MHz-1'
                    - '320MHz-2'
            80211mc:
                type: str
                description: Deprecated, please rename it to d80211mc. Enable/disable 802.
                choices:
                    - 'disable'
                    - 'enable'
            ap-sniffer-chan-width:
                type: str
                description: Deprecated, please rename it to ap_sniffer_chan_width. Channel bandwidth for sniffer.
                choices:
                    - '320MHz'
                    - '240MHz'
                    - '160MHz'
                    - '80MHz'
                    - '40MHz'
                    - '20MHz'
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
    - name: Configuration options for radio 2.
      fortinet.fortimanager.fmgr_wtpprofile_radio2:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        adom: <your own value>
        wtp_profile: <your own value>
        wtpprofile_radio2:
          amsdu: <value in [disable, enable]>
          ap_handoff: <value in [disable, enable]>
          ap_sniffer_addr: <string>
          ap_sniffer_bufsize: <integer>
          ap_sniffer_chan: <integer>
          ap_sniffer_ctl: <value in [disable, enable]>
          ap_sniffer_data: <value in [disable, enable]>
          ap_sniffer_mgmt_beacon: <value in [disable, enable]>
          ap_sniffer_mgmt_other: <value in [disable, enable]>
          ap_sniffer_mgmt_probe: <value in [disable, enable]>
          auto_power_high: <integer>
          auto_power_level: <value in [disable, enable]>
          auto_power_low: <integer>
          band: <value in [802.11b, 802.11a, 802.11g, ...]>
          bandwidth_admission_control: <value in [disable, enable]>
          bandwidth_capacity: <integer>
          beacon_interval: <integer>
          call_admission_control: <value in [disable, enable]>
          call_capacity: <integer>
          channel: <list or string>
          channel_bonding: <value in [disable, enable, 80MHz, ...]>
          channel_utilization: <value in [disable, enable]>
          coexistence: <value in [disable, enable]>
          darrp: <value in [disable, enable]>
          dtim: <integer>
          frag_threshold: <integer>
          frequency_handoff: <value in [disable, enable]>
          max_clients: <integer>
          max_distance: <integer>
          mode: <value in [disabled, ap, monitor, ...]>
          power_level: <integer>
          powersave_optimize:
            - tim
            - ac-vo
            - no-obss-scan
            - no-11b-rate
            - client-rate-follow
          protection_mode: <value in [rtscts, ctsonly, disable]>
          radio_id: <integer>
          rts_threshold: <integer>
          short_guard_interval: <value in [disable, enable]>
          spectrum_analysis: <value in [disable, enable, scan-only]>
          transmit_optimize:
            - disable
            - power-save
            - aggr-limit
            - retry-limit
            - send-bar
          vap_all: <value in [disable, enable, tunnel, ...]>
          vaps: <list or string>
          wids_profile: <string>
          airtime_fairness: <value in [disable, enable]>
          band_5g_type: <value in [5g-full, 5g-high, 5g-low]>
          zero_wait_dfs: <value in [disable, enable]>
          vap1: <string>
          vap2: <string>
          vap3: <string>
          vap4: <string>
          vap5: <string>
          vap6: <string>
          vap7: <string>
          vap8: <string>
          bss_color: <integer>
          auto_power_target: <string>
          drma: <value in [disable, enable]>
          drma_sensitivity: <value in [low, medium, high]>
          iperf_protocol: <value in [udp, tcp]>
          iperf_server_port: <integer>
          power_mode: <value in [dBm, percentage]>
          power_value: <integer>
          sam_bssid: <string>
          sam_captive_portal: <value in [disable, enable]>
          sam_password: <list or string>
          sam_report_intv: <integer>
          sam_security_type: <value in [open, wpa-personal, wpa-enterprise, ...]>
          sam_server: <string>
          sam_ssid: <string>
          sam_test: <value in [ping, iperf]>
          sam_username: <string>
          arrp_profile: <string>
          bss_color_mode: <value in [auto, static]>
          sam_cwp_failure_string: <string>
          sam_cwp_match_string: <string>
          sam_cwp_password: <list or string>
          sam_cwp_success_string: <string>
          sam_cwp_test_url: <string>
          sam_cwp_username: <string>
          sam_server_fqdn: <string>
          sam_server_ip: <string>
          sam_server_type: <value in [ip, fqdn]>
          d80211d: <value in [disable, enable]>
          optional_antenna: <value in [none, FANT-04ABGN-0606-O-N, FANT-04ABGN-1414-P-N, ...]>
          mimo_mode: <value in [default, 1x1, 2x2, ...]>
          optional_antenna_gain: <string>
          sam_ca_certificate: <string>
          sam_client_certificate: <string>
          sam_eap_method: <value in [tls, peap, both]>
          sam_private_key: <string>
          sam_private_key_password: <list or string>
          channel_bonding_ext: <value in [320MHz-1, 320MHz-2]>
          d80211mc: <value in [disable, enable]>
          ap_sniffer_chan_width: <value in [320MHz, 240MHz, 160MHz, ...]>
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
        '/pm/config/adom/{adom}/obj/wireless-controller/wtp-profile/{wtp-profile}/radio-2',
        '/pm/config/global/obj/wireless-controller/wtp-profile/{wtp-profile}/radio-2'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/wireless-controller/wtp-profile/{wtp-profile}/radio-2/{radio-2}',
        '/pm/config/global/obj/wireless-controller/wtp-profile/{wtp-profile}/radio-2/{radio-2}'
    ]

    url_params = ['adom', 'wtp-profile']
    module_primary_key = None
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'wtp-profile': {'type': 'str', 'api_name': 'wtp_profile'},
        'wtp_profile': {'type': 'str'},
        'wtpprofile_radio2': {
            'type': 'dict',
            'v_range': [['6.0.0', '']],
            'options': {
                'amsdu': {'choices': ['disable', 'enable'], 'type': 'str'},
                'ap-handoff': {'choices': ['disable', 'enable'], 'type': 'str'},
                'ap-sniffer-addr': {'type': 'str'},
                'ap-sniffer-bufsize': {'type': 'int'},
                'ap-sniffer-chan': {'type': 'int'},
                'ap-sniffer-ctl': {'choices': ['disable', 'enable'], 'type': 'str'},
                'ap-sniffer-data': {'choices': ['disable', 'enable'], 'type': 'str'},
                'ap-sniffer-mgmt-beacon': {'choices': ['disable', 'enable'], 'type': 'str'},
                'ap-sniffer-mgmt-other': {'choices': ['disable', 'enable'], 'type': 'str'},
                'ap-sniffer-mgmt-probe': {'choices': ['disable', 'enable'], 'type': 'str'},
                'auto-power-high': {'type': 'int'},
                'auto-power-level': {'choices': ['disable', 'enable'], 'type': 'str'},
                'auto-power-low': {'type': 'int'},
                'band': {
                    'choices': [
                        '802.11b', '802.11a', '802.11g', '802.11n', '802.11ac', '802.11n-5G', '802.11g-only', '802.11n-only', '802.11n,g-only',
                        '802.11ac-only', '802.11ac,n-only', '802.11n-5G-only', '802.11ax-5G', '802.11ax', '802.11ax-5G-only', '802.11ax,ac-only',
                        '802.11ax,ac,n-only', '802.11ax-only', '802.11ax,n-only', '802.11ax,n,g-only', '802.11ac-2G', '802.11ax-6G', '802.11n-2G',
                        '802.11ac-5G', '802.11ax-2G', '802.11be-2G', '802.11be-5G', '802.11be-6G'
                    ],
                    'type': 'str'
                },
                'bandwidth-admission-control': {'choices': ['disable', 'enable'], 'type': 'str'},
                'bandwidth-capacity': {'type': 'int'},
                'beacon-interval': {'type': 'int'},
                'call-admission-control': {'choices': ['disable', 'enable'], 'type': 'str'},
                'call-capacity': {'type': 'int'},
                'channel': {'type': 'raw'},
                'channel-bonding': {'choices': ['disable', 'enable', '80MHz', '40MHz', '20MHz', '160MHz', '320MHz', '240MHz'], 'type': 'str'},
                'channel-utilization': {'choices': ['disable', 'enable'], 'type': 'str'},
                'coexistence': {'choices': ['disable', 'enable'], 'type': 'str'},
                'darrp': {'choices': ['disable', 'enable'], 'type': 'str'},
                'dtim': {'type': 'int'},
                'frag-threshold': {'type': 'int'},
                'frequency-handoff': {'choices': ['disable', 'enable'], 'type': 'str'},
                'max-clients': {'type': 'int'},
                'max-distance': {'type': 'int'},
                'mode': {'choices': ['disabled', 'ap', 'monitor', 'sniffer', 'sam'], 'type': 'str'},
                'power-level': {'type': 'int'},
                'powersave-optimize': {
                    'type': 'list',
                    'choices': ['tim', 'ac-vo', 'no-obss-scan', 'no-11b-rate', 'client-rate-follow'],
                    'elements': 'str'
                },
                'protection-mode': {'choices': ['rtscts', 'ctsonly', 'disable'], 'type': 'str'},
                'radio-id': {'type': 'int'},
                'rts-threshold': {'type': 'int'},
                'short-guard-interval': {'choices': ['disable', 'enable'], 'type': 'str'},
                'spectrum-analysis': {'choices': ['disable', 'enable', 'scan-only'], 'type': 'str'},
                'transmit-optimize': {'type': 'list', 'choices': ['disable', 'power-save', 'aggr-limit', 'retry-limit', 'send-bar'], 'elements': 'str'},
                'vap-all': {'choices': ['disable', 'enable', 'tunnel', 'bridge', 'manual'], 'type': 'str'},
                'vaps': {'type': 'raw'},
                'wids-profile': {'type': 'str'},
                'airtime-fairness': {'v_range': [['6.2.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'band-5g-type': {'v_range': [['6.2.5', '']], 'choices': ['5g-full', '5g-high', '5g-low'], 'type': 'str'},
                'zero-wait-dfs': {'v_range': [['6.2.5', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'vap1': {'v_range': [['6.4.0', '']], 'type': 'str'},
                'vap2': {'v_range': [['6.4.0', '']], 'type': 'str'},
                'vap3': {'v_range': [['6.4.0', '']], 'type': 'str'},
                'vap4': {'v_range': [['6.4.0', '']], 'type': 'str'},
                'vap5': {'v_range': [['6.4.0', '']], 'type': 'str'},
                'vap6': {'v_range': [['6.4.0', '']], 'type': 'str'},
                'vap7': {'v_range': [['6.4.0', '']], 'type': 'str'},
                'vap8': {'v_range': [['6.4.0', '']], 'type': 'str'},
                'bss-color': {'v_range': [['6.4.2', '']], 'type': 'int'},
                'auto-power-target': {'v_range': [['6.4.3', '']], 'type': 'str'},
                'drma': {'v_range': [['6.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'drma-sensitivity': {'v_range': [['6.4.3', '']], 'choices': ['low', 'medium', 'high'], 'type': 'str'},
                'iperf-protocol': {'v_range': [['7.0.0', '']], 'choices': ['udp', 'tcp'], 'type': 'str'},
                'iperf-server-port': {'v_range': [['7.0.0', '']], 'type': 'int'},
                'power-mode': {'v_range': [['7.0.0', '']], 'choices': ['dBm', 'percentage'], 'type': 'str'},
                'power-value': {'v_range': [['7.0.0', '']], 'type': 'int'},
                'sam-bssid': {'v_range': [['7.0.0', '']], 'type': 'str'},
                'sam-captive-portal': {'v_range': [['7.0.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'sam-password': {'v_range': [['7.0.0', '']], 'no_log': True, 'type': 'raw'},
                'sam-report-intv': {'v_range': [['7.0.0', '']], 'type': 'int'},
                'sam-security-type': {'v_range': [['7.0.0', '']], 'choices': ['open', 'wpa-personal', 'wpa-enterprise', 'owe', 'wpa3-sae'], 'type': 'str'},
                'sam-server': {'v_range': [['7.0.0', '']], 'type': 'str'},
                'sam-ssid': {'v_range': [['7.0.0', '']], 'type': 'str'},
                'sam-test': {'v_range': [['7.0.0', '']], 'choices': ['ping', 'iperf'], 'type': 'str'},
                'sam-username': {'v_range': [['7.0.0', '']], 'type': 'str'},
                'arrp-profile': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'bss-color-mode': {'v_range': [['7.0.2', '']], 'choices': ['auto', 'static'], 'type': 'str'},
                'sam-cwp-failure-string': {'v_range': [['7.0.1', '']], 'type': 'str'},
                'sam-cwp-match-string': {'v_range': [['7.0.1', '']], 'type': 'str'},
                'sam-cwp-password': {'v_range': [['7.0.1', '']], 'no_log': True, 'type': 'raw'},
                'sam-cwp-success-string': {'v_range': [['7.0.1', '']], 'type': 'str'},
                'sam-cwp-test-url': {'v_range': [['7.0.1', '']], 'type': 'str'},
                'sam-cwp-username': {'v_range': [['7.0.1', '']], 'type': 'str'},
                'sam-server-fqdn': {'v_range': [['7.0.1', '']], 'type': 'str'},
                'sam-server-ip': {'v_range': [['7.0.1', '']], 'type': 'str'},
                'sam-server-type': {'v_range': [['7.0.1', '']], 'choices': ['ip', 'fqdn'], 'type': 'str'},
                '80211d': {'v_range': [['7.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'optional-antenna': {
                    'v_range': [['7.2.3', '']],
                    'choices': [
                        'none', 'FANT-04ABGN-0606-O-N', 'FANT-04ABGN-1414-P-N', 'FANT-04ABGN-8065-P-N', 'FANT-04ABGN-0606-O-R', 'FANT-04ABGN-0606-P-R',
                        'FANT-10ACAX-1213-D-N', 'FANT-08ABGN-1213-D-R', 'custom'
                    ],
                    'type': 'str'
                },
                'mimo-mode': {'v_range': [['7.4.1', '']], 'choices': ['default', '1x1', '2x2', '3x3', '4x4', '8x8'], 'type': 'str'},
                'optional-antenna-gain': {'v_range': [['7.4.2', '']], 'type': 'str'},
                'sam-ca-certificate': {'v_range': [['7.4.2', '']], 'type': 'str'},
                'sam-client-certificate': {'v_range': [['7.4.2', '']], 'type': 'str'},
                'sam-eap-method': {'v_range': [['7.4.2', '']], 'choices': ['tls', 'peap', 'both'], 'type': 'str'},
                'sam-private-key': {'v_range': [['7.4.2', '']], 'no_log': True, 'type': 'str'},
                'sam-private-key-password': {'v_range': [['7.4.2', '']], 'no_log': True, 'type': 'raw'},
                'channel-bonding-ext': {'v_range': [['7.4.3', '']], 'choices': ['320MHz-1', '320MHz-2'], 'type': 'str'},
                '80211mc': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ap-sniffer-chan-width': {'v_range': [['7.6.0', '']], 'choices': ['320MHz', '240MHz', '160MHz', '80MHz', '40MHz', '20MHz'], 'type': 'str'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('partial crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'wtpprofile_radio2'),
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
