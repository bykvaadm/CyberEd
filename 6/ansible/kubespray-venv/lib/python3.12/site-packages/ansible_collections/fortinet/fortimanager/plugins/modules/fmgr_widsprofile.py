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
module: fmgr_widsprofile
short_description: Configure wireless intrusion detection system
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
    widsprofile:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            ap-auto-suppress:
                type: str
                description: Deprecated, please rename it to ap_auto_suppress. Enable/disable on-wire rogue AP auto-suppression
                choices:
                    - 'disable'
                    - 'enable'
            ap-bgscan-disable-day:
                type: list
                elements: str
                description: Deprecated, please rename it to ap_bgscan_disable_day. Optionally turn off scanning for one or more days of the week.
                choices:
                    - 'sunday'
                    - 'monday'
                    - 'tuesday'
                    - 'wednesday'
                    - 'thursday'
                    - 'friday'
                    - 'saturday'
            ap-bgscan-disable-end:
                type: str
                description: Deprecated, please rename it to ap_bgscan_disable_end. End time, using a 24-hour clock in the format of hh
            ap-bgscan-disable-start:
                type: str
                description: Deprecated, please rename it to ap_bgscan_disable_start. Start time, using a 24-hour clock in the format of hh
            ap-bgscan-duration:
                type: int
                description: Deprecated, please rename it to ap_bgscan_duration. Listening time on a scanning channel
            ap-bgscan-idle:
                type: int
                description: Deprecated, please rename it to ap_bgscan_idle. Waiting time for channel inactivity before scanning this channel
            ap-bgscan-intv:
                type: int
                description: Deprecated, please rename it to ap_bgscan_intv. Period of time between scanning two channels
            ap-bgscan-period:
                type: int
                description: Deprecated, please rename it to ap_bgscan_period. Period of time between background scans
            ap-bgscan-report-intv:
                type: int
                description: Deprecated, please rename it to ap_bgscan_report_intv. Period of time between background scan reports
            ap-fgscan-report-intv:
                type: int
                description: Deprecated, please rename it to ap_fgscan_report_intv. Period of time between foreground scan reports
            ap-scan:
                type: str
                description: Deprecated, please rename it to ap_scan. Enable/disable rogue AP detection.
                choices:
                    - 'disable'
                    - 'enable'
            ap-scan-passive:
                type: str
                description: Deprecated, please rename it to ap_scan_passive. Enable/disable passive scanning.
                choices:
                    - 'disable'
                    - 'enable'
            asleap-attack:
                type: str
                description: Deprecated, please rename it to asleap_attack. Enable/disable asleap attack detection
                choices:
                    - 'disable'
                    - 'enable'
            assoc-flood-thresh:
                type: int
                description: Deprecated, please rename it to assoc_flood_thresh. The threshold value for association frame flooding.
            assoc-flood-time:
                type: int
                description: Deprecated, please rename it to assoc_flood_time. Number of seconds after which a station is considered not connected.
            assoc-frame-flood:
                type: str
                description: Deprecated, please rename it to assoc_frame_flood. Enable/disable association frame flooding detection
                choices:
                    - 'disable'
                    - 'enable'
            auth-flood-thresh:
                type: int
                description: Deprecated, please rename it to auth_flood_thresh. The threshold value for authentication frame flooding.
            auth-flood-time:
                type: int
                description: Deprecated, please rename it to auth_flood_time. Number of seconds after which a station is considered not connected.
            auth-frame-flood:
                type: str
                description: Deprecated, please rename it to auth_frame_flood. Enable/disable authentication frame flooding detection
                choices:
                    - 'disable'
                    - 'enable'
            comment:
                type: str
                description: Comment.
            deauth-broadcast:
                type: str
                description: Deprecated, please rename it to deauth_broadcast. Enable/disable broadcasting de-authentication detection
                choices:
                    - 'disable'
                    - 'enable'
            deauth-unknown-src-thresh:
                type: int
                description: Deprecated, please rename it to deauth_unknown_src_thresh. Threshold value per second to deauth unknown src for DoS attack
            eapol-fail-flood:
                type: str
                description: Deprecated, please rename it to eapol_fail_flood. Enable/disable EAPOL-Failure flooding
                choices:
                    - 'disable'
                    - 'enable'
            eapol-fail-intv:
                type: int
                description: Deprecated, please rename it to eapol_fail_intv. The detection interval for EAPOL-Failure flooding
            eapol-fail-thresh:
                type: int
                description: Deprecated, please rename it to eapol_fail_thresh. The threshold value for EAPOL-Failure flooding in specified interval.
            eapol-logoff-flood:
                type: str
                description: Deprecated, please rename it to eapol_logoff_flood. Enable/disable EAPOL-Logoff flooding
                choices:
                    - 'disable'
                    - 'enable'
            eapol-logoff-intv:
                type: int
                description: Deprecated, please rename it to eapol_logoff_intv. The detection interval for EAPOL-Logoff flooding
            eapol-logoff-thresh:
                type: int
                description: Deprecated, please rename it to eapol_logoff_thresh. The threshold value for EAPOL-Logoff flooding in specified interval.
            eapol-pre-fail-flood:
                type: str
                description: Deprecated, please rename it to eapol_pre_fail_flood. Enable/disable premature EAPOL-Failure flooding
                choices:
                    - 'disable'
                    - 'enable'
            eapol-pre-fail-intv:
                type: int
                description: Deprecated, please rename it to eapol_pre_fail_intv. The detection interval for premature EAPOL-Failure flooding
            eapol-pre-fail-thresh:
                type: int
                description: Deprecated, please rename it to eapol_pre_fail_thresh. The threshold value for premature EAPOL-Failure flooding in specifi...
            eapol-pre-succ-flood:
                type: str
                description: Deprecated, please rename it to eapol_pre_succ_flood. Enable/disable premature EAPOL-Success flooding
                choices:
                    - 'disable'
                    - 'enable'
            eapol-pre-succ-intv:
                type: int
                description: Deprecated, please rename it to eapol_pre_succ_intv. The detection interval for premature EAPOL-Success flooding
            eapol-pre-succ-thresh:
                type: int
                description: Deprecated, please rename it to eapol_pre_succ_thresh. The threshold value for premature EAPOL-Success flooding in specifi...
            eapol-start-flood:
                type: str
                description: Deprecated, please rename it to eapol_start_flood. Enable/disable EAPOL-Start flooding
                choices:
                    - 'disable'
                    - 'enable'
            eapol-start-intv:
                type: int
                description: Deprecated, please rename it to eapol_start_intv. The detection interval for EAPOL-Start flooding
            eapol-start-thresh:
                type: int
                description: Deprecated, please rename it to eapol_start_thresh. The threshold value for EAPOL-Start flooding in specified interval.
            eapol-succ-flood:
                type: str
                description: Deprecated, please rename it to eapol_succ_flood. Enable/disable EAPOL-Success flooding
                choices:
                    - 'disable'
                    - 'enable'
            eapol-succ-intv:
                type: int
                description: Deprecated, please rename it to eapol_succ_intv. The detection interval for EAPOL-Success flooding
            eapol-succ-thresh:
                type: int
                description: Deprecated, please rename it to eapol_succ_thresh. The threshold value for EAPOL-Success flooding in specified interval.
            invalid-mac-oui:
                type: str
                description: Deprecated, please rename it to invalid_mac_oui. Enable/disable invalid MAC OUI detection.
                choices:
                    - 'disable'
                    - 'enable'
            long-duration-attack:
                type: str
                description: Deprecated, please rename it to long_duration_attack. Enable/disable long duration attack detection based on user configur...
                choices:
                    - 'disable'
                    - 'enable'
            long-duration-thresh:
                type: int
                description: Deprecated, please rename it to long_duration_thresh. Threshold value for long duration attack detection
            name:
                type: str
                description: WIDS profile name.
                required: true
            null-ssid-probe-resp:
                type: str
                description: Deprecated, please rename it to null_ssid_probe_resp. Enable/disable null SSID probe response detection
                choices:
                    - 'disable'
                    - 'enable'
            sensor-mode:
                type: str
                description: Deprecated, please rename it to sensor_mode. Scan WiFi nearby stations
                choices:
                    - 'disable'
                    - 'foreign'
                    - 'both'
            spoofed-deauth:
                type: str
                description: Deprecated, please rename it to spoofed_deauth. Enable/disable spoofed de-authentication attack detection
                choices:
                    - 'disable'
                    - 'enable'
            weak-wep-iv:
                type: str
                description: Deprecated, please rename it to weak_wep_iv. Enable/disable weak WEP IV
                choices:
                    - 'disable'
                    - 'enable'
            wireless-bridge:
                type: str
                description: Deprecated, please rename it to wireless_bridge. Enable/disable wireless bridge detection
                choices:
                    - 'disable'
                    - 'enable'
            ap-bgscan-disable-schedules:
                type: raw
                description: (list or str) Deprecated, please rename it to ap_bgscan_disable_schedules. Firewall schedules for turning off FortiAP radi...
            rogue-scan:
                type: str
                description: Deprecated, please rename it to rogue_scan. Enable/disable rogue AP on-wire scan.
                choices:
                    - 'disable'
                    - 'enable'
            ap-scan-threshold:
                type: str
                description: Deprecated, please rename it to ap_scan_threshold. Minimum signal level/threshold in dBm required for the AP to report det...
            ap-scan-channel-list-2G-5G:
                type: raw
                description: (list) Deprecated, please rename it to ap_scan_channel_list_2G_5G. Selected ap scan channel list for 2.
            ap-scan-channel-list-6G:
                type: raw
                description: (list) Deprecated, please rename it to ap_scan_channel_list_6G. Selected ap scan channel list for 6G band.
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
    - name: Configure wireless intrusion detection system
      fortinet.fortimanager.fmgr_widsprofile:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: present # <value in [present, absent]>
        widsprofile:
          ap_auto_suppress: <value in [disable, enable]>
          ap_bgscan_disable_day:
            - sunday
            - monday
            - tuesday
            - wednesday
            - thursday
            - friday
            - saturday
          ap_bgscan_disable_end: <string>
          ap_bgscan_disable_start: <string>
          ap_bgscan_duration: <integer>
          ap_bgscan_idle: <integer>
          ap_bgscan_intv: <integer>
          ap_bgscan_period: <integer>
          ap_bgscan_report_intv: <integer>
          ap_fgscan_report_intv: <integer>
          ap_scan: <value in [disable, enable]>
          ap_scan_passive: <value in [disable, enable]>
          asleap_attack: <value in [disable, enable]>
          assoc_flood_thresh: <integer>
          assoc_flood_time: <integer>
          assoc_frame_flood: <value in [disable, enable]>
          auth_flood_thresh: <integer>
          auth_flood_time: <integer>
          auth_frame_flood: <value in [disable, enable]>
          comment: <string>
          deauth_broadcast: <value in [disable, enable]>
          deauth_unknown_src_thresh: <integer>
          eapol_fail_flood: <value in [disable, enable]>
          eapol_fail_intv: <integer>
          eapol_fail_thresh: <integer>
          eapol_logoff_flood: <value in [disable, enable]>
          eapol_logoff_intv: <integer>
          eapol_logoff_thresh: <integer>
          eapol_pre_fail_flood: <value in [disable, enable]>
          eapol_pre_fail_intv: <integer>
          eapol_pre_fail_thresh: <integer>
          eapol_pre_succ_flood: <value in [disable, enable]>
          eapol_pre_succ_intv: <integer>
          eapol_pre_succ_thresh: <integer>
          eapol_start_flood: <value in [disable, enable]>
          eapol_start_intv: <integer>
          eapol_start_thresh: <integer>
          eapol_succ_flood: <value in [disable, enable]>
          eapol_succ_intv: <integer>
          eapol_succ_thresh: <integer>
          invalid_mac_oui: <value in [disable, enable]>
          long_duration_attack: <value in [disable, enable]>
          long_duration_thresh: <integer>
          name: <string>
          null_ssid_probe_resp: <value in [disable, enable]>
          sensor_mode: <value in [disable, foreign, both]>
          spoofed_deauth: <value in [disable, enable]>
          weak_wep_iv: <value in [disable, enable]>
          wireless_bridge: <value in [disable, enable]>
          ap_bgscan_disable_schedules: <list or string>
          rogue_scan: <value in [disable, enable]>
          ap_scan_threshold: <string>
          ap_scan_channel_list_2G_5G: <list or string>
          ap_scan_channel_list_6G: <list or string>
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
        '/pm/config/adom/{adom}/obj/wireless-controller/wids-profile',
        '/pm/config/global/obj/wireless-controller/wids-profile'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/wireless-controller/wids-profile/{wids-profile}',
        '/pm/config/global/obj/wireless-controller/wids-profile/{wids-profile}'
    ]

    url_params = ['adom']
    module_primary_key = 'name'
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'widsprofile': {
            'type': 'dict',
            'v_range': [['6.0.0', '']],
            'options': {
                'ap-auto-suppress': {'choices': ['disable', 'enable'], 'type': 'str'},
                'ap-bgscan-disable-day': {
                    'v_range': [['6.0.0', '7.2.1']],
                    'type': 'list',
                    'choices': ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'],
                    'elements': 'str'
                },
                'ap-bgscan-disable-end': {'v_range': [['6.0.0', '7.2.1']], 'type': 'str'},
                'ap-bgscan-disable-start': {'v_range': [['6.0.0', '7.2.1']], 'type': 'str'},
                'ap-bgscan-duration': {'type': 'int'},
                'ap-bgscan-idle': {'type': 'int'},
                'ap-bgscan-intv': {'type': 'int'},
                'ap-bgscan-period': {'type': 'int'},
                'ap-bgscan-report-intv': {'type': 'int'},
                'ap-fgscan-report-intv': {'type': 'int'},
                'ap-scan': {'choices': ['disable', 'enable'], 'type': 'str'},
                'ap-scan-passive': {'choices': ['disable', 'enable'], 'type': 'str'},
                'asleap-attack': {'choices': ['disable', 'enable'], 'type': 'str'},
                'assoc-flood-thresh': {'type': 'int'},
                'assoc-flood-time': {'type': 'int'},
                'assoc-frame-flood': {'choices': ['disable', 'enable'], 'type': 'str'},
                'auth-flood-thresh': {'type': 'int'},
                'auth-flood-time': {'type': 'int'},
                'auth-frame-flood': {'choices': ['disable', 'enable'], 'type': 'str'},
                'comment': {'type': 'str'},
                'deauth-broadcast': {'choices': ['disable', 'enable'], 'type': 'str'},
                'deauth-unknown-src-thresh': {'type': 'int'},
                'eapol-fail-flood': {'choices': ['disable', 'enable'], 'type': 'str'},
                'eapol-fail-intv': {'type': 'int'},
                'eapol-fail-thresh': {'type': 'int'},
                'eapol-logoff-flood': {'choices': ['disable', 'enable'], 'type': 'str'},
                'eapol-logoff-intv': {'type': 'int'},
                'eapol-logoff-thresh': {'type': 'int'},
                'eapol-pre-fail-flood': {'choices': ['disable', 'enable'], 'type': 'str'},
                'eapol-pre-fail-intv': {'type': 'int'},
                'eapol-pre-fail-thresh': {'type': 'int'},
                'eapol-pre-succ-flood': {'choices': ['disable', 'enable'], 'type': 'str'},
                'eapol-pre-succ-intv': {'type': 'int'},
                'eapol-pre-succ-thresh': {'type': 'int'},
                'eapol-start-flood': {'choices': ['disable', 'enable'], 'type': 'str'},
                'eapol-start-intv': {'type': 'int'},
                'eapol-start-thresh': {'type': 'int'},
                'eapol-succ-flood': {'choices': ['disable', 'enable'], 'type': 'str'},
                'eapol-succ-intv': {'type': 'int'},
                'eapol-succ-thresh': {'type': 'int'},
                'invalid-mac-oui': {'choices': ['disable', 'enable'], 'type': 'str'},
                'long-duration-attack': {'choices': ['disable', 'enable'], 'type': 'str'},
                'long-duration-thresh': {'type': 'int'},
                'name': {'required': True, 'type': 'str'},
                'null-ssid-probe-resp': {'choices': ['disable', 'enable'], 'type': 'str'},
                'sensor-mode': {'choices': ['disable', 'foreign', 'both'], 'type': 'str'},
                'spoofed-deauth': {'choices': ['disable', 'enable'], 'type': 'str'},
                'weak-wep-iv': {'choices': ['disable', 'enable'], 'type': 'str'},
                'wireless-bridge': {'choices': ['disable', 'enable'], 'type': 'str'},
                'ap-bgscan-disable-schedules': {'v_range': [['6.2.1', '']], 'type': 'raw'},
                'rogue-scan': {'v_range': [['6.2.0', '6.2.12']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ap-scan-threshold': {'v_range': [['6.2.3', '']], 'type': 'str'},
                'ap-scan-channel-list-2G-5G': {'v_range': [['7.4.1', '']], 'type': 'raw'},
                'ap-scan-channel-list-6G': {'v_range': [['7.4.1', '']], 'type': 'raw'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('full crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'widsprofile'),
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
