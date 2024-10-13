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
module: fmgr_fmupdate_webspam_fgdsetting
short_description: Configure the FortiGuard run parameters.
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
    fmupdate_webspam_fgdsetting:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            as-cache:
                type: int
                description: Deprecated, please rename it to as_cache. Antispam service maximum memory usage in megabytes
            as-log:
                type: str
                description:
                    - Deprecated, please rename it to as_log.
                    - Antispam log setting
                    - disable - Disable spam log.
                    - nospam - Log non-spam events.
                    - all - Log all spam lookups.
                choices:
                    - 'disable'
                    - 'nospam'
                    - 'all'
            as-preload:
                type: str
                description:
                    - Deprecated, please rename it to as_preload.
                    - Enable/disable preloading antispam database to memory
                    - disable - Disable antispam database preload.
                    - enable - Enable antispam database preload.
                choices:
                    - 'disable'
                    - 'enable'
            av-cache:
                type: int
                description: Deprecated, please rename it to av_cache. Antivirus service maximum memory usage, in megabytes
            av-log:
                type: str
                description:
                    - Deprecated, please rename it to av_log.
                    - Antivirus log setting
                    - disable - Disable virus log.
                    - novirus - Log non-virus events.
                    - all - Log all virus lookups.
                choices:
                    - 'disable'
                    - 'novirus'
                    - 'all'
            av-preload:
                type: str
                description:
                    - Deprecated, please rename it to av_preload.
                    - Enable/disable preloading antivirus database to memory
                    - disable - Disable antivirus database preload.
                    - enable - Enable antivirus database preload.
                choices:
                    - 'disable'
                    - 'enable'
            av2-cache:
                type: int
                description: Deprecated, please rename it to av2_cache. Antispam service maximum memory usage in megabytes
            av2-log:
                type: str
                description:
                    - Deprecated, please rename it to av2_log.
                    - Outbreak prevention log setting
                    - disable - Disable av2 log.
                    - noav2 - Log non-av2 events.
                    - all - Log all av2 lookups.
                choices:
                    - 'disable'
                    - 'noav2'
                    - 'all'
            av2-preload:
                type: str
                description:
                    - Deprecated, please rename it to av2_preload.
                    - Enable/disable preloading outbreak prevention database to memory
                    - disable - Disable outbreak prevention database preload.
                    - enable - Enable outbreak prevention database preload.
                choices:
                    - 'disable'
                    - 'enable'
            eventlog-query:
                type: str
                description:
                    - Deprecated, please rename it to eventlog_query.
                    - Enable/disable record query to event-log besides fgd-log
                    - disable - Record query to event-log besides fgd-log.
                    - enable - Do not log to event-log.
                choices:
                    - 'disable'
                    - 'enable'
            fgd-pull-interval:
                type: int
                description: Deprecated, please rename it to fgd_pull_interval. Fgd pull interval setting, in minutes
            fq-cache:
                type: int
                description: Deprecated, please rename it to fq_cache. File query service maximum memory usage, in megabytes
            fq-log:
                type: str
                description:
                    - Deprecated, please rename it to fq_log.
                    - File query log setting
                    - disable - Disable file query log.
                    - nofilequery - Log non-file query events.
                    - all - Log all file query events.
                choices:
                    - 'disable'
                    - 'nofilequery'
                    - 'all'
            fq-preload:
                type: str
                description:
                    - Deprecated, please rename it to fq_preload.
                    - Enable/disable preloading file query database to memory
                    - disable - Disable file query db preload.
                    - enable - Enable file query db preload.
                choices:
                    - 'disable'
                    - 'enable'
            linkd-log:
                type: str
                description:
                    - Deprecated, please rename it to linkd_log.
                    - Linkd log setting
                    - emergency - The unit is unusable.
                    - alert - Immediate action is required
                    - critical - Functionality is affected.
                    - error - Functionality is probably affected.
                    - warn - Functionality might be affected.
                    - notice - Information about normal events.
                    - info - General information.
                    - debug - Debug information.
                    - disable - Linkd logging is disabled.
                choices:
                    - 'emergency'
                    - 'alert'
                    - 'critical'
                    - 'error'
                    - 'warn'
                    - 'notice'
                    - 'info'
                    - 'debug'
                    - 'disable'
            max-client-worker:
                type: int
                description: Deprecated, please rename it to max_client_worker. Max worker for tcp client connection
            max-log-quota:
                type: int
                description: Deprecated, please rename it to max_log_quota. Maximum log quota setting, in megabytes
            max-unrated-site:
                type: int
                description: Deprecated, please rename it to max_unrated_site. Maximum number of unrated site in memory, in kilobytes
            restrict-as1-dbver:
                type: str
                description: Deprecated, please rename it to restrict_as1_dbver. Restrict system update to indicated antispam
            restrict-as2-dbver:
                type: str
                description: Deprecated, please rename it to restrict_as2_dbver. Restrict system update to indicated antispam
            restrict-as4-dbver:
                type: str
                description: Deprecated, please rename it to restrict_as4_dbver. Restrict system update to indicated antispam
            restrict-av-dbver:
                type: str
                description: Deprecated, please rename it to restrict_av_dbver. Restrict system update to indicated antivirus database version
            restrict-av2-dbver:
                type: str
                description: Deprecated, please rename it to restrict_av2_dbver. Restrict system update to indicated outbreak prevention database version
            restrict-fq-dbver:
                type: str
                description: Deprecated, please rename it to restrict_fq_dbver. Restrict system update to indicated file query database version
            restrict-wf-dbver:
                type: str
                description: Deprecated, please rename it to restrict_wf_dbver. Restrict system update to indicated web filter database version
            server-override:
                type: dict
                description: Deprecated, please rename it to server_override. Server override.
                suboptions:
                    servlist:
                        type: list
                        elements: dict
                        description: Servlist.
                        suboptions:
                            id:
                                type: int
                                description: Override server ID
                            ip:
                                type: str
                                description: IPv4 address of the override server.
                            ip6:
                                type: str
                                description: IPv6 address of the override server.
                            port:
                                type: int
                                description: Port number to use when contacting FortiGuard
                            service-type:
                                type: raw
                                description:
                                    - (list or str)
                                    - Deprecated, please rename it to service_type.
                                    - Override service type.
                                    - fgd - Server override config for fgd
                                    - fgc - Server override config for fgc
                                    - fsa - Server override config for fsa
                                choices:
                                    - 'fgd'
                                    - 'fgc'
                                    - 'fsa'
                                    - 'fgfq'
                                    - 'geoip'
                                    - 'iot-collect'
                    status:
                        type: str
                        description:
                            - Override status.
                            - disable - Disable setting.
                            - enable - Enable setting.
                        choices:
                            - 'disable'
                            - 'enable'
            stat-log-interval:
                type: int
                description: Deprecated, please rename it to stat_log_interval. Statistic log interval setting, in minutes
            stat-sync-interval:
                type: int
                description: Deprecated, please rename it to stat_sync_interval. Synchronization interval for statistic of unrated site in minutes
            update-interval:
                type: int
                description: Deprecated, please rename it to update_interval. FortiGuard database update wait time if not enough delta files, in hours
            update-log:
                type: str
                description:
                    - Deprecated, please rename it to update_log.
                    - Enable/disable update log setting
                    - disable - Disable update log.
                    - enable - Enable update log.
                choices:
                    - 'disable'
                    - 'enable'
            wf-cache:
                type: int
                description: Deprecated, please rename it to wf_cache. Web filter service maximum memory usage, in megabytes
            wf-dn-cache-expire-time:
                type: int
                description: Deprecated, please rename it to wf_dn_cache_expire_time. Web filter DN cache expire time, in minutes
            wf-dn-cache-max-number:
                type: int
                description: Deprecated, please rename it to wf_dn_cache_max_number. Maximum number of Web filter DN cache
            wf-log:
                type: str
                description:
                    - Deprecated, please rename it to wf_log.
                    - Web filter log setting
                    - disable - Disable URL log.
                    - nourl - Log non-URL events.
                    - all - Log all URL lookups.
                choices:
                    - 'disable'
                    - 'nourl'
                    - 'all'
            wf-preload:
                type: str
                description:
                    - Deprecated, please rename it to wf_preload.
                    - Enable/disable preloading the web filter database into memory
                    - disable - Disable web filter database preload.
                    - enable - Enable web filter database preload.
                choices:
                    - 'disable'
                    - 'enable'
            iot-cache:
                type: int
                description: Deprecated, please rename it to iot_cache. IoT service maximum memory usage, in megabytes
            iot-log:
                type: str
                description:
                    - Deprecated, please rename it to iot_log.
                    - IoT log setting
                    - disable - Disable IoT log.
                    - nofilequery - Log non-IoT events.
                    - all - Log all IoT events.
                choices:
                    - 'disable'
                    - 'nofilequery'
                    - 'all'
                    - 'noiot'
            iot-preload:
                type: str
                description:
                    - Deprecated, please rename it to iot_preload.
                    - Enable/disable preloading IoT database to memory
                    - disable - Disable IoT db preload.
                    - enable - Enable IoT db preload.
                choices:
                    - 'disable'
                    - 'enable'
            restrict-iots-dbver:
                type: str
                description: Deprecated, please rename it to restrict_iots_dbver. Restrict system update to indicated file query database version
            stat-log:
                type: str
                description:
                    - Deprecated, please rename it to stat_log.
                    - stat log setting
                    - emergency - The unit is unusable
                    - alert - Immediate action is required
                    - critical - Functionality is affected
                    - error - Functionality is probably affected
                    - warn - Functionality might be affected
                    - notice - Information about normal events
                    - info - General information
                    - debug - Debug information
                    - disable - Linkd logging is disabled.
                choices:
                    - 'emergency'
                    - 'alert'
                    - 'critical'
                    - 'error'
                    - 'warn'
                    - 'notice'
                    - 'info'
                    - 'debug'
                    - 'disable'
            iotv-preload:
                type: str
                description:
                    - Deprecated, please rename it to iotv_preload.
                    - Enable/disable preloading IoT-Vulnerability database to memory
                    - disable - Disable IoT-Vulnerability db preload.
                    - enable - Enable IoT-Vulnerability db preload.
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
    - name: Configure the FortiGuard run parameters.
      fortinet.fortimanager.fmgr_fmupdate_webspam_fgdsetting:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        fmupdate_webspam_fgdsetting:
          as_cache: <integer>
          as_log: <value in [disable, nospam, all]>
          as_preload: <value in [disable, enable]>
          av_cache: <integer>
          av_log: <value in [disable, novirus, all]>
          av_preload: <value in [disable, enable]>
          av2_cache: <integer>
          av2_log: <value in [disable, noav2, all]>
          av2_preload: <value in [disable, enable]>
          eventlog_query: <value in [disable, enable]>
          fgd_pull_interval: <integer>
          fq_cache: <integer>
          fq_log: <value in [disable, nofilequery, all]>
          fq_preload: <value in [disable, enable]>
          linkd_log: <value in [emergency, alert, critical, ...]>
          max_client_worker: <integer>
          max_log_quota: <integer>
          max_unrated_site: <integer>
          restrict_as1_dbver: <string>
          restrict_as2_dbver: <string>
          restrict_as4_dbver: <string>
          restrict_av_dbver: <string>
          restrict_av2_dbver: <string>
          restrict_fq_dbver: <string>
          restrict_wf_dbver: <string>
          server_override:
            servlist:
              -
                id: <integer>
                ip: <string>
                ip6: <string>
                port: <integer>
                service_type: # <list or string>
                  - fgd
                  - fgc
                  - fsa
                  - fgfq
                  - geoip
                  - iot-collect
            status: <value in [disable, enable]>
          stat_log_interval: <integer>
          stat_sync_interval: <integer>
          update_interval: <integer>
          update_log: <value in [disable, enable]>
          wf_cache: <integer>
          wf_dn_cache_expire_time: <integer>
          wf_dn_cache_max_number: <integer>
          wf_log: <value in [disable, nourl, all]>
          wf_preload: <value in [disable, enable]>
          iot_cache: <integer>
          iot_log: <value in [disable, nofilequery, all, ...]>
          iot_preload: <value in [disable, enable]>
          restrict_iots_dbver: <string>
          stat_log: <value in [emergency, alert, critical, ...]>
          iotv_preload: <value in [disable, enable]>
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
        '/cli/global/fmupdate/web-spam/fgd-setting'
    ]

    perobject_jrpc_urls = [
        '/cli/global/fmupdate/web-spam/fgd-setting/{fgd-setting}'
    ]

    url_params = []
    module_primary_key = None
    module_arg_spec = {
        'fmupdate_webspam_fgdsetting': {
            'type': 'dict',
            'v_range': [['6.0.0', '']],
            'options': {
                'as-cache': {'type': 'int'},
                'as-log': {'choices': ['disable', 'nospam', 'all'], 'type': 'str'},
                'as-preload': {'choices': ['disable', 'enable'], 'type': 'str'},
                'av-cache': {'type': 'int'},
                'av-log': {'choices': ['disable', 'novirus', 'all'], 'type': 'str'},
                'av-preload': {'choices': ['disable', 'enable'], 'type': 'str'},
                'av2-cache': {'type': 'int'},
                'av2-log': {'choices': ['disable', 'noav2', 'all'], 'type': 'str'},
                'av2-preload': {'choices': ['disable', 'enable'], 'type': 'str'},
                'eventlog-query': {'choices': ['disable', 'enable'], 'type': 'str'},
                'fgd-pull-interval': {'type': 'int'},
                'fq-cache': {'type': 'int'},
                'fq-log': {'choices': ['disable', 'nofilequery', 'all'], 'type': 'str'},
                'fq-preload': {'choices': ['disable', 'enable'], 'type': 'str'},
                'linkd-log': {'choices': ['emergency', 'alert', 'critical', 'error', 'warn', 'notice', 'info', 'debug', 'disable'], 'type': 'str'},
                'max-client-worker': {'type': 'int'},
                'max-log-quota': {'type': 'int'},
                'max-unrated-site': {'type': 'int'},
                'restrict-as1-dbver': {'type': 'str'},
                'restrict-as2-dbver': {'type': 'str'},
                'restrict-as4-dbver': {'type': 'str'},
                'restrict-av-dbver': {'type': 'str'},
                'restrict-av2-dbver': {'type': 'str'},
                'restrict-fq-dbver': {'type': 'str'},
                'restrict-wf-dbver': {'type': 'str'},
                'server-override': {
                    'type': 'dict',
                    'options': {
                        'servlist': {
                            'type': 'list',
                            'options': {
                                'id': {'type': 'int'},
                                'ip': {'type': 'str'},
                                'ip6': {'type': 'str'},
                                'port': {'type': 'int'},
                                'service-type': {'type': 'raw', 'choices': ['fgd', 'fgc', 'fsa', 'fgfq', 'geoip', 'iot-collect']}
                            },
                            'elements': 'dict'
                        },
                        'status': {'choices': ['disable', 'enable'], 'type': 'str'}
                    }
                },
                'stat-log-interval': {'type': 'int'},
                'stat-sync-interval': {'type': 'int'},
                'update-interval': {'type': 'int'},
                'update-log': {'choices': ['disable', 'enable'], 'type': 'str'},
                'wf-cache': {'type': 'int'},
                'wf-dn-cache-expire-time': {'type': 'int'},
                'wf-dn-cache-max-number': {'type': 'int'},
                'wf-log': {'choices': ['disable', 'nourl', 'all'], 'type': 'str'},
                'wf-preload': {'choices': ['disable', 'enable'], 'type': 'str'},
                'iot-cache': {'v_range': [['6.4.6', '6.4.14'], ['7.0.1', '']], 'type': 'int'},
                'iot-log': {'v_range': [['6.4.6', '6.4.14'], ['7.0.1', '']], 'choices': ['disable', 'nofilequery', 'all', 'noiot'], 'type': 'str'},
                'iot-preload': {'v_range': [['6.4.6', '6.4.14'], ['7.0.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'restrict-iots-dbver': {'v_range': [['6.4.6', '6.4.14'], ['7.0.1', '']], 'type': 'str'},
                'stat-log': {
                    'v_range': [['7.0.10', '7.0.12'], ['7.2.5', '7.2.5'], ['7.4.2', '']],
                    'choices': ['emergency', 'alert', 'critical', 'error', 'warn', 'notice', 'info', 'debug', 'disable'],
                    'type': 'str'
                },
                'iotv-preload': {'v_range': [['7.2.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('partial crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'fmupdate_webspam_fgdsetting'),
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
