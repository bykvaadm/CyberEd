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
module: fmgr_system_fortiguard
short_description: Configure FortiGuard services.
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
    system_fortiguard:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            antispam-cache:
                type: str
                description: Deprecated, please rename it to antispam_cache. Enable/disable FortiGuard antispam request caching.
                choices:
                    - 'disable'
                    - 'enable'
            antispam-cache-mpercent:
                type: int
                description: Deprecated, please rename it to antispam_cache_mpercent. Maximum percent of FortiGate memory the antispam cache is allowed...
            antispam-cache-ttl:
                type: int
                description: Deprecated, please rename it to antispam_cache_ttl. Time-to-live for antispam cache entries in seconds
            antispam-expiration:
                type: int
                description: Deprecated, please rename it to antispam_expiration. Antispam expiration.
            antispam-force-off:
                type: str
                description: Deprecated, please rename it to antispam_force_off. Enable/disable turning off the FortiGuard antispam service.
                choices:
                    - 'disable'
                    - 'enable'
            antispam-license:
                type: int
                description: Deprecated, please rename it to antispam_license. Antispam license.
            antispam-timeout:
                type: int
                description: Deprecated, please rename it to antispam_timeout. Antispam query time out
            auto-join-forticloud:
                type: str
                description: Deprecated, please rename it to auto_join_forticloud. Automatically connect to and login to FortiCloud.
                choices:
                    - 'disable'
                    - 'enable'
            ddns-server-ip:
                type: str
                description: Deprecated, please rename it to ddns_server_ip. IP address of the FortiDDNS server.
            ddns-server-port:
                type: int
                description: Deprecated, please rename it to ddns_server_port. Port used to communicate with FortiDDNS servers.
            load-balance-servers:
                type: int
                description: Deprecated, please rename it to load_balance_servers. Number of servers to alternate between as first FortiGuard option.
            outbreak-prevention-cache:
                type: str
                description: Deprecated, please rename it to outbreak_prevention_cache. Enable/disable FortiGuard Virus Outbreak Prevention cache.
                choices:
                    - 'disable'
                    - 'enable'
            outbreak-prevention-cache-mpercent:
                type: int
                description: Deprecated, please rename it to outbreak_prevention_cache_mpercent. Maximum percent of memory FortiGuard Virus Outbreak Pr...
            outbreak-prevention-cache-ttl:
                type: int
                description: Deprecated, please rename it to outbreak_prevention_cache_ttl. Time-to-live for FortiGuard Virus Outbreak Prevention cache...
            outbreak-prevention-expiration:
                type: int
                description: Deprecated, please rename it to outbreak_prevention_expiration. Outbreak prevention expiration.
            outbreak-prevention-force-off:
                type: str
                description: Deprecated, please rename it to outbreak_prevention_force_off. Turn off FortiGuard Virus Outbreak Prevention service.
                choices:
                    - 'disable'
                    - 'enable'
            outbreak-prevention-license:
                type: int
                description: Deprecated, please rename it to outbreak_prevention_license. Outbreak prevention license.
            outbreak-prevention-timeout:
                type: int
                description: Deprecated, please rename it to outbreak_prevention_timeout. FortiGuard Virus Outbreak Prevention time out
            port:
                type: str
                description: Port used to communicate with the FortiGuard servers.
                choices:
                    - '53'
                    - '80'
                    - '8888'
                    - '443'
            sdns-server-ip:
                type: raw
                description: (list) Deprecated, please rename it to sdns_server_ip. IP address of the FortiDNS server.
            sdns-server-port:
                type: int
                description: Deprecated, please rename it to sdns_server_port. Port used to communicate with FortiDNS servers.
            service-account-id:
                type: str
                description: Deprecated, please rename it to service_account_id. Service account ID.
            source-ip:
                type: str
                description: Deprecated, please rename it to source_ip. Source IPv4 address used to communicate with FortiGuard.
            source-ip6:
                type: str
                description: Deprecated, please rename it to source_ip6. Source IPv6 address used to communicate with FortiGuard.
            update-server-location:
                type: str
                description: Deprecated, please rename it to update_server_location. Signature update server location.
                choices:
                    - 'any'
                    - 'usa'
                    - 'automatic'
                    - 'eu'
            webfilter-cache:
                type: str
                description: Deprecated, please rename it to webfilter_cache. Enable/disable FortiGuard web filter caching.
                choices:
                    - 'disable'
                    - 'enable'
            webfilter-cache-ttl:
                type: int
                description: Deprecated, please rename it to webfilter_cache_ttl. Time-to-live for web filter cache entries in seconds
            webfilter-expiration:
                type: int
                description: Deprecated, please rename it to webfilter_expiration. Webfilter expiration.
            webfilter-force-off:
                type: str
                description: Deprecated, please rename it to webfilter_force_off. Enable/disable turning off the FortiGuard web filtering service.
                choices:
                    - 'disable'
                    - 'enable'
            webfilter-license:
                type: int
                description: Deprecated, please rename it to webfilter_license. Webfilter license.
            webfilter-timeout:
                type: int
                description: Deprecated, please rename it to webfilter_timeout. Web filter query time out
            protocol:
                type: str
                description: Protocol used to communicate with the FortiGuard servers.
                choices:
                    - 'udp'
                    - 'http'
                    - 'https'
            proxy-password:
                type: raw
                description: (list) Deprecated, please rename it to proxy_password. Proxy user password.
            proxy-server-ip:
                type: str
                description: Deprecated, please rename it to proxy_server_ip. IP address of the proxy server.
            proxy-server-port:
                type: int
                description: Deprecated, please rename it to proxy_server_port. Port used to communicate with the proxy server.
            proxy-username:
                type: str
                description: Deprecated, please rename it to proxy_username. Proxy user name.
            sandbox-region:
                type: str
                description: Deprecated, please rename it to sandbox_region. Cloud sandbox region.
            avquery-cache-ttl:
                type: int
                description: Deprecated, please rename it to avquery_cache_ttl. Time-to-live for antivirus cache entries
            avquery-timeout:
                type: int
                description: Deprecated, please rename it to avquery_timeout. Antivirus query time out
            avquery-cache:
                type: str
                description: Deprecated, please rename it to avquery_cache. Enable/disable the FortiGuard antivirus cache.
                choices:
                    - 'disable'
                    - 'enable'
            avquery-cache-mpercent:
                type: int
                description: Deprecated, please rename it to avquery_cache_mpercent. Maximum percent of memory the antivirus cache can use
            avquery-license:
                type: int
                description: Deprecated, please rename it to avquery_license. Interval of time between license checks for the FortiGuard antivirus cont...
            avquery-force-off:
                type: str
                description: Deprecated, please rename it to avquery_force_off. Turn off the FortiGuard antivirus service.
                choices:
                    - 'disable'
                    - 'enable'
            fortiguard-anycast:
                type: str
                description: Deprecated, please rename it to fortiguard_anycast. Enable/disable use of FortiGuards anycast network.
                choices:
                    - 'disable'
                    - 'enable'
            fortiguard-anycast-source:
                type: str
                description: Deprecated, please rename it to fortiguard_anycast_source. Configure which of Fortinets servers to provide FortiGuard serv...
                choices:
                    - 'fortinet'
                    - 'aws'
                    - 'debug'
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
            sdns-options:
                type: list
                elements: str
                description: Deprecated, please rename it to sdns_options. Customization options for the FortiGuard DNS service.
                choices:
                    - 'include-question-section'
            anycast-sdns-server-ip:
                type: str
                description: Deprecated, please rename it to anycast_sdns_server_ip. IP address of the FortiGuard anycast DNS rating server.
            anycast-sdns-server-port:
                type: int
                description: Deprecated, please rename it to anycast_sdns_server_port. Port to connect to on the FortiGuard anycast DNS rating server.
            persistent-connection:
                type: str
                description: Deprecated, please rename it to persistent_connection. Enable/disable use of persistent connection to receive update notif...
                choices:
                    - 'disable'
                    - 'enable'
            update-build-proxy:
                type: str
                description: Deprecated, please rename it to update_build_proxy. Enable/disable proxy dictionary rebuild.
                choices:
                    - 'disable'
                    - 'enable'
            update-extdb:
                type: str
                description: Deprecated, please rename it to update_extdb. Enable/disable external resource update.
                choices:
                    - 'disable'
                    - 'enable'
            update-ffdb:
                type: str
                description: Deprecated, please rename it to update_ffdb. Enable/disable Internet Service Database update.
                choices:
                    - 'disable'
                    - 'enable'
            update-uwdb:
                type: str
                description: Deprecated, please rename it to update_uwdb. Enable/disable allowlist update.
                choices:
                    - 'disable'
                    - 'enable'
            videofilter-expiration:
                type: int
                description: Deprecated, please rename it to videofilter_expiration. Videofilter expiration.
            videofilter-license:
                type: int
                description: Deprecated, please rename it to videofilter_license. Videofilter license.
            ddns-server-ip6:
                type: str
                description: Deprecated, please rename it to ddns_server_ip6. IPv6 address of the FortiDDNS server.
            vdom:
                type: str
                description: FortiGuard Service virtual domain name.
            auto-firmware-upgrade:
                type: str
                description: Deprecated, please rename it to auto_firmware_upgrade. Enable/disable automatic patch-level firmware upgrade from FortiGuard.
                choices:
                    - 'disable'
                    - 'enable'
            auto-firmware-upgrade-day:
                type: list
                elements: str
                description: Deprecated, please rename it to auto_firmware_upgrade_day. Allowed day
                choices:
                    - 'sunday'
                    - 'monday'
                    - 'tuesday'
                    - 'wednesday'
                    - 'thursday'
                    - 'friday'
                    - 'saturday'
            auto-firmware-upgrade-end-hour:
                type: int
                description: Deprecated, please rename it to auto_firmware_upgrade_end_hour. End time in the designated time window for automatic patch...
            auto-firmware-upgrade-start-hour:
                type: int
                description: Deprecated, please rename it to auto_firmware_upgrade_start_hour. Start time in the designated time window for automatic p...
            sandbox-inline-scan:
                type: str
                description: Deprecated, please rename it to sandbox_inline_scan. Enable/disable FortiCloud Sandbox inline-scan.
                choices:
                    - 'disable'
                    - 'enable'
            auto-firmware-upgrade-delay:
                type: int
                description: Deprecated, please rename it to auto_firmware_upgrade_delay. Delay of day
            gui-prompt-auto-upgrade:
                type: str
                description: Deprecated, please rename it to gui_prompt_auto_upgrade. Enable/disable prompting of automatic patch-level firmware upgrad...
                choices:
                    - 'disable'
                    - 'enable'
            FDS-license-expiring-days:
                type: int
                description: Deprecated, please rename it to FDS_license_expiring_days. Threshold for number of days before FortiGuard license expirati...
            antispam-cache-mpermille:
                type: int
                description: Deprecated, please rename it to antispam_cache_mpermille. Maximum permille of FortiGate memory the antispam cache is allow...
            outbreak-prevention-cache-mpermille:
                type: int
                description: Deprecated, please rename it to outbreak_prevention_cache_mpermille. Maximum permille of memory FortiGuard Virus Outbreak ...
            update-dldb:
                type: str
                description: Deprecated, please rename it to update_dldb. Enable/disable DLP signature update.
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
    - name: Configure FortiGuard services.
      fortinet.fortimanager.fmgr_system_fortiguard:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        adom: <your own value>
        system_fortiguard:
          antispam_cache: <value in [disable, enable]>
          antispam_cache_mpercent: <integer>
          antispam_cache_ttl: <integer>
          antispam_expiration: <integer>
          antispam_force_off: <value in [disable, enable]>
          antispam_license: <integer>
          antispam_timeout: <integer>
          auto_join_forticloud: <value in [disable, enable]>
          ddns_server_ip: <string>
          ddns_server_port: <integer>
          load_balance_servers: <integer>
          outbreak_prevention_cache: <value in [disable, enable]>
          outbreak_prevention_cache_mpercent: <integer>
          outbreak_prevention_cache_ttl: <integer>
          outbreak_prevention_expiration: <integer>
          outbreak_prevention_force_off: <value in [disable, enable]>
          outbreak_prevention_license: <integer>
          outbreak_prevention_timeout: <integer>
          port: <value in [53, 80, 8888, ...]>
          sdns_server_ip: <list or string>
          sdns_server_port: <integer>
          service_account_id: <string>
          source_ip: <string>
          source_ip6: <string>
          update_server_location: <value in [any, usa, automatic, ...]>
          webfilter_cache: <value in [disable, enable]>
          webfilter_cache_ttl: <integer>
          webfilter_expiration: <integer>
          webfilter_force_off: <value in [disable, enable]>
          webfilter_license: <integer>
          webfilter_timeout: <integer>
          protocol: <value in [udp, http, https]>
          proxy_password: <list or string>
          proxy_server_ip: <string>
          proxy_server_port: <integer>
          proxy_username: <string>
          sandbox_region: <string>
          avquery_cache_ttl: <integer>
          avquery_timeout: <integer>
          avquery_cache: <value in [disable, enable]>
          avquery_cache_mpercent: <integer>
          avquery_license: <integer>
          avquery_force_off: <value in [disable, enable]>
          fortiguard_anycast: <value in [disable, enable]>
          fortiguard_anycast_source: <value in [fortinet, aws, debug]>
          interface: <string>
          interface_select_method: <value in [auto, sdwan, specify]>
          sdns_options:
            - include-question-section
          anycast_sdns_server_ip: <string>
          anycast_sdns_server_port: <integer>
          persistent_connection: <value in [disable, enable]>
          update_build_proxy: <value in [disable, enable]>
          update_extdb: <value in [disable, enable]>
          update_ffdb: <value in [disable, enable]>
          update_uwdb: <value in [disable, enable]>
          videofilter_expiration: <integer>
          videofilter_license: <integer>
          ddns_server_ip6: <string>
          vdom: <string>
          auto_firmware_upgrade: <value in [disable, enable]>
          auto_firmware_upgrade_day:
            - sunday
            - monday
            - tuesday
            - wednesday
            - thursday
            - friday
            - saturday
          auto_firmware_upgrade_end_hour: <integer>
          auto_firmware_upgrade_start_hour: <integer>
          sandbox_inline_scan: <value in [disable, enable]>
          auto_firmware_upgrade_delay: <integer>
          gui_prompt_auto_upgrade: <value in [disable, enable]>
          FDS_license_expiring_days: <integer>
          antispam_cache_mpermille: <integer>
          outbreak_prevention_cache_mpermille: <integer>
          update_dldb: <value in [disable, enable]>
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
        '/pm/config/adom/{adom}/obj/system/fortiguard',
        '/pm/config/global/obj/system/fortiguard'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/system/fortiguard/{fortiguard}',
        '/pm/config/global/obj/system/fortiguard/{fortiguard}'
    ]

    url_params = ['adom']
    module_primary_key = None
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'system_fortiguard': {
            'type': 'dict',
            'v_range': [['6.0.0', '']],
            'options': {
                'antispam-cache': {'choices': ['disable', 'enable'], 'type': 'str'},
                'antispam-cache-mpercent': {'type': 'int'},
                'antispam-cache-ttl': {'type': 'int'},
                'antispam-expiration': {'type': 'int'},
                'antispam-force-off': {'choices': ['disable', 'enable'], 'type': 'str'},
                'antispam-license': {'type': 'int'},
                'antispam-timeout': {'type': 'int'},
                'auto-join-forticloud': {'choices': ['disable', 'enable'], 'type': 'str'},
                'ddns-server-ip': {'type': 'str'},
                'ddns-server-port': {'type': 'int'},
                'load-balance-servers': {'type': 'int'},
                'outbreak-prevention-cache': {'choices': ['disable', 'enable'], 'type': 'str'},
                'outbreak-prevention-cache-mpercent': {'type': 'int'},
                'outbreak-prevention-cache-ttl': {'type': 'int'},
                'outbreak-prevention-expiration': {'type': 'int'},
                'outbreak-prevention-force-off': {'choices': ['disable', 'enable'], 'type': 'str'},
                'outbreak-prevention-license': {'type': 'int'},
                'outbreak-prevention-timeout': {'type': 'int'},
                'port': {'choices': ['53', '80', '8888', '443'], 'type': 'str'},
                'sdns-server-ip': {'type': 'raw'},
                'sdns-server-port': {'type': 'int'},
                'service-account-id': {'type': 'str'},
                'source-ip': {'type': 'str'},
                'source-ip6': {'type': 'str'},
                'update-server-location': {'choices': ['any', 'usa', 'automatic', 'eu'], 'type': 'str'},
                'webfilter-cache': {'choices': ['disable', 'enable'], 'type': 'str'},
                'webfilter-cache-ttl': {'type': 'int'},
                'webfilter-expiration': {'type': 'int'},
                'webfilter-force-off': {'choices': ['disable', 'enable'], 'type': 'str'},
                'webfilter-license': {'type': 'int'},
                'webfilter-timeout': {'type': 'int'},
                'protocol': {'v_range': [['6.2.0', '']], 'choices': ['udp', 'http', 'https'], 'type': 'str'},
                'proxy-password': {'v_range': [['6.2.1', '']], 'no_log': True, 'type': 'raw'},
                'proxy-server-ip': {'v_range': [['6.2.1', '']], 'type': 'str'},
                'proxy-server-port': {'v_range': [['6.2.1', '']], 'type': 'int'},
                'proxy-username': {'v_range': [['6.2.1', '']], 'type': 'str'},
                'sandbox-region': {'v_range': [['6.2.0', '']], 'type': 'str'},
                'avquery-cache-ttl': {'v_range': [['6.2.0', '6.4.14']], 'type': 'int'},
                'avquery-timeout': {'v_range': [['6.2.0', '6.4.14']], 'type': 'int'},
                'avquery-cache': {'v_range': [['6.2.0', '6.4.14']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'avquery-cache-mpercent': {'v_range': [['6.2.0', '6.4.14']], 'type': 'int'},
                'avquery-license': {'v_range': [['6.2.0', '6.4.14']], 'type': 'int'},
                'avquery-force-off': {'v_range': [['6.2.0', '6.4.14']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'fortiguard-anycast': {'v_range': [['6.2.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'fortiguard-anycast-source': {'v_range': [['6.2.2', '']], 'choices': ['fortinet', 'aws', 'debug'], 'type': 'str'},
                'interface': {'v_range': [['6.2.5', '6.2.12'], ['6.4.1', '']], 'type': 'str'},
                'interface-select-method': {'v_range': [['6.2.5', '6.2.12'], ['6.4.1', '']], 'choices': ['auto', 'sdwan', 'specify'], 'type': 'str'},
                'sdns-options': {'v_range': [['6.4.0', '']], 'type': 'list', 'choices': ['include-question-section'], 'elements': 'str'},
                'anycast-sdns-server-ip': {'v_range': [['6.4.1', '']], 'type': 'str'},
                'anycast-sdns-server-port': {'v_range': [['6.4.1', '']], 'type': 'int'},
                'persistent-connection': {'v_range': [['7.0.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'update-build-proxy': {'v_range': [['7.0.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'update-extdb': {'v_range': [['7.0.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'update-ffdb': {'v_range': [['7.0.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'update-uwdb': {'v_range': [['7.0.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'videofilter-expiration': {'v_range': [['7.0.0', '']], 'type': 'int'},
                'videofilter-license': {'v_range': [['7.0.0', '']], 'type': 'int'},
                'ddns-server-ip6': {'v_range': [['7.0.1', '']], 'type': 'str'},
                'vdom': {'v_range': [['7.2.0', '']], 'type': 'str'},
                'auto-firmware-upgrade': {'v_range': [['7.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'auto-firmware-upgrade-day': {
                    'v_range': [['7.2.1', '']],
                    'type': 'list',
                    'choices': ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'],
                    'elements': 'str'
                },
                'auto-firmware-upgrade-end-hour': {'v_range': [['7.2.1', '']], 'type': 'int'},
                'auto-firmware-upgrade-start-hour': {'v_range': [['7.2.1', '']], 'type': 'int'},
                'sandbox-inline-scan': {'v_range': [['7.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'auto-firmware-upgrade-delay': {'v_range': [['7.2.4', '']], 'type': 'int'},
                'gui-prompt-auto-upgrade': {'v_range': [['7.2.4', '7.2.5'], ['7.4.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'FDS-license-expiring-days': {'v_range': [['7.4.0', '']], 'type': 'int'},
                'antispam-cache-mpermille': {'v_range': [['7.4.0', '']], 'type': 'int'},
                'outbreak-prevention-cache-mpermille': {'v_range': [['7.4.0', '']], 'type': 'int'},
                'update-dldb': {'v_range': [['7.4.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('partial crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'system_fortiguard'),
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
