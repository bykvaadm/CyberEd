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
module: fmgr_fmupdate_fdssetting
short_description: Configure FortiGuard settings.
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
    fmupdate_fdssetting:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            User-Agent:
                type: str
                description: Deprecated, please rename it to User_Agent. Configure the user agent string.
            fds-clt-ssl-protocol:
                type: str
                description:
                    - Deprecated, please rename it to fds_clt_ssl_protocol.
                    - The SSL protocols version for connecting fds server
                    - sslv3 - set SSLv3 as the client version.
                    - tlsv1.
                    - tlsv1.
                    - tlsv1.
                choices:
                    - 'sslv3'
                    - 'tlsv1.0'
                    - 'tlsv1.1'
                    - 'tlsv1.2'
                    - 'tlsv1.3'
            fds-ssl-protocol:
                type: str
                description:
                    - Deprecated, please rename it to fds_ssl_protocol.
                    - The SSL protocols version for receiving fgt connection
                    - sslv3 - set SSLv3 as the lowest version.
                    - tlsv1.
                    - tlsv1.
                    - tlsv1.
                choices:
                    - 'sslv3'
                    - 'tlsv1.0'
                    - 'tlsv1.1'
                    - 'tlsv1.2'
                    - 'tlsv1.3'
            fmtr-log:
                type: str
                description:
                    - Deprecated, please rename it to fmtr_log.
                    - fmtr log level
                    - emergency - Log level - emergency
                    - alert - Log level - alert
                    - critical - Log level - critical
                    - error - Log level - error
                    - warn - Log level - warn
                    - notice - Log level - notice
                    - info - Log level - info
                    - debug - Log level - debug
                    - disable - Disable linkd log
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
            linkd-log:
                type: str
                description:
                    - Deprecated, please rename it to linkd_log.
                    - The linkd log level
                    - emergency - Log level - emergency
                    - alert - Log level - alert
                    - critical - Log level - critical
                    - error - Log level - error
                    - warn - Log level - warn
                    - notice - Log level - notice
                    - info - Log level - info
                    - debug - Log level - debug
                    - disable - Disable linkd log
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
            max-av-ips-version:
                type: int
                description: Deprecated, please rename it to max_av_ips_version. The maximum number of downloadable, full version AV/IPS packages
            max-work:
                type: int
                description: Deprecated, please rename it to max_work. The maximum number of worker processing download requests
            push-override:
                type: dict
                description: Deprecated, please rename it to push_override. Push override.
                suboptions:
                    ip:
                        type: str
                        description: External or virtual IP address of the NAT device that will forward push messages to the FortiManager unit.
                    port:
                        type: int
                        description: Receiving port number on the NAT device
                    status:
                        type: str
                        description:
                            - Enable/disable push updates for clients
                            - disable - Disable setting.
                            - enable - Enable setting.
                        choices:
                            - 'disable'
                            - 'enable'
            push-override-to-client:
                type: dict
                description: Deprecated, please rename it to push_override_to_client. Push override to client.
                suboptions:
                    announce-ip:
                        type: list
                        elements: dict
                        description: Deprecated, please rename it to announce_ip. Announce ip.
                        suboptions:
                            id:
                                type: int
                                description: ID of the announce IP address
                            ip:
                                type: str
                                description: Announce IPv4 address.
                            port:
                                type: int
                                description: Announce IP port
                    status:
                        type: str
                        description:
                            - Enable/disable push updates
                            - disable - Disable setting.
                            - enable - Enable setting.
                        choices:
                            - 'disable'
                            - 'enable'
            send_report:
                type: str
                description:
                    - send report/fssi to fds server.
                    - disable - Disable setting.
                    - enable - Enable setting.
                choices:
                    - 'disable'
                    - 'enable'
            send_setup:
                type: str
                description:
                    - forward setup to fds server.
                    - disable - Disable setting.
                    - enable - Enable setting.
                choices:
                    - 'disable'
                    - 'enable'
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
                                    - fds - Server override config for fds
                                    - fct - Server override config for fct
                                choices:
                                    - 'fds'
                                    - 'fct'
                                    - 'fai'
                    status:
                        type: str
                        description:
                            - Override status.
                            - disable - Disable setting.
                            - enable - Enable setting.
                        choices:
                            - 'disable'
                            - 'enable'
            system-support-fct:
                type: list
                elements: str
                description:
                    - Deprecated, please rename it to system_support_fct.
                    - Supported FortiClient versions.
                    - '4.'
                    - '5.'
                    - '5.'
                    - '5.'
                    - '5.'
                    - '6.'
                choices:
                    - '4.x'
                    - '5.0'
                    - '5.2'
                    - '5.4'
                    - '5.6'
                    - '6.0'
                    - '6.2'
                    - '6.4'
                    - '7.0'
                    - '7.2'
            system-support-fgt:
                type: list
                elements: str
                description:
                    - Deprecated, please rename it to system_support_fgt.
                    - Supported FortiOS versions.
                    - '5.'
                    - '5.'
                    - '6.'
                    - '6.'
                choices:
                    - '5.4'
                    - '5.6'
                    - '6.0'
                    - '6.2'
                    - '6.4'
                    - '7.0'
                    - '7.2'
                    - '7.4'
                    - '7.6'
            system-support-fml:
                type: list
                elements: str
                description:
                    - Deprecated, please rename it to system_support_fml.
                    - Supported FortiMail versions.
                    - '4.'
                    - '5.'
                    - '6.'
                choices:
                    - '4.x'
                    - '5.x'
                    - '6.x'
                    - '6.0'
                    - '6.2'
                    - '6.4'
                    - '7.0'
                    - '7.2'
                    - '7.x'
            system-support-fsa:
                type: list
                elements: str
                description:
                    - Deprecated, please rename it to system_support_fsa.
                    - Supported FortiSandbox versions.
                    - '1.'
                    - '2.'
                    - '3.'
                choices:
                    - '1.x'
                    - '2.x'
                    - '3.x'
                    - '4.x'
                    - '3.0'
                    - '3.1'
                    - '3.2'
            system-support-fsw:
                type: list
                elements: str
                description:
                    - Deprecated, please rename it to system_support_fsw.
                    - Supported FortiSwitch versions.
                    - '5.'
                    - '5.'
                    - '6.'
                    - '6.'
                choices:
                    - '5.4'
                    - '5.6'
                    - '6.0'
                    - '6.2'
                    - '4.x'
                    - '5.0'
                    - '5.2'
                    - '6.4'
            umsvc-log:
                type: str
                description:
                    - Deprecated, please rename it to umsvc_log.
                    - The um_service log level
                    - emergency - Log level - emergency
                    - alert - Log level - alert
                    - critical - Log level - critical
                    - error - Log level - error
                    - warn - Log level - warn
                    - notice - Log level - notice
                    - info - Log level - info
                    - debug - Log level - debug
                    - disable - Disable linkd log
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
            unreg-dev-option:
                type: str
                description:
                    - Deprecated, please rename it to unreg_dev_option.
                    - set the option for unregister devices
                    - ignore - Ignore all unregistered devices.
                    - svc-only - Allow update requests without adding the device.
                    - add-service - Add unregistered devices and allow update request.
                choices:
                    - 'ignore'
                    - 'svc-only'
                    - 'add-service'
            update-schedule:
                type: dict
                description: Deprecated, please rename it to update_schedule. Update schedule.
                suboptions:
                    day:
                        type: str
                        description:
                            - Configure the day the update will occur, if the freqnecy is weekly
                            - Sunday - Update every Sunday.
                            - Monday - Update every Monday.
                            - Tuesday - Update every Tuesday.
                            - Wednesday - Update every Wednesday.
                            - Thursday - Update every Thursday.
                            - Friday - Update every Friday.
                            - Saturday - Update every Saturday.
                        choices:
                            - 'Sunday'
                            - 'Monday'
                            - 'Tuesday'
                            - 'Wednesday'
                            - 'Thursday'
                            - 'Friday'
                            - 'Saturday'
                    frequency:
                        type: str
                        description:
                            - Configure update frequency
                            - every - Time interval.
                            - daily - Every day.
                            - weekly - Every week.
                        choices:
                            - 'every'
                            - 'daily'
                            - 'weekly'
                    status:
                        type: str
                        description:
                            - Enable/disable scheduled updates.
                            - disable - Disable setting.
                            - enable - Enable setting.
                        choices:
                            - 'disable'
                            - 'enable'
                    time:
                        type: raw
                        description: (list) Time interval between updates, or the hour and minute when the update occurs
            wanip-query-mode:
                type: str
                description:
                    - Deprecated, please rename it to wanip_query_mode.
                    - public ip query mode
                    - disable - Do not query public ip
                    - ipify - Get public IP through https
                choices:
                    - 'disable'
                    - 'ipify'
            fortiguard-anycast:
                type: str
                description:
                    - Deprecated, please rename it to fortiguard_anycast.
                    - Enable/disable use of FortiGuards anycast network
                    - disable - Disable setting.
                    - enable - Enable setting.
                choices:
                    - 'disable'
                    - 'enable'
            fortiguard-anycast-source:
                type: str
                description:
                    - Deprecated, please rename it to fortiguard_anycast_source.
                    - Configure which of Fortinets servers to provide FortiGuard services in FortiGuards anycast network.
                    - fortinet - Use Fortinets servers to provide FortiGuard services in FortiGuards anycast network.
                    - aws - Use Fortinets AWS servers to provide FortiGuard services in FortiGuards anycast network.
                choices:
                    - 'fortinet'
                    - 'aws'
            system-support-fdc:
                type: list
                elements: str
                description:
                    - Deprecated, please rename it to system_support_fdc.
                    - Supported FortiDeceptor versions.
                    - '3.'
                    - '4.'
                choices:
                    - '3.x'
                    - '4.x'
            system-support-fts:
                type: list
                elements: str
                description:
                    - Deprecated, please rename it to system_support_fts.
                    - Supported FortiTester versions.
                    - '3.'
                    - '4.'
                    - '7.'
                choices:
                    - '3.x'
                    - '4.x'
                    - '7.x'
            system-support-faz:
                type: list
                elements: str
                description:
                    - Deprecated, please rename it to system_support_faz.
                    - Supported FortiAnalyzer versions.
                    - '6.'
                    - '7.'
                choices:
                    - '6.x'
                    - '7.x'
            system-support-fis:
                type: list
                elements: str
                description:
                    - Deprecated, please rename it to system_support_fis.
                    - Supported FortiIsolator versions.
                    - '1.'
                    - '2.'
                choices:
                    - '1.x'
                    - '2.x'
            system-support-fai:
                type: list
                elements: str
                description:
                    - Deprecated, please rename it to system_support_fai.
                    - Supported FortiNDR versions.
                    - '7.'
                choices:
                    - '7.x'
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
    - name: Configure FortiGuard settings.
      fortinet.fortimanager.fmgr_fmupdate_fdssetting:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        fmupdate_fdssetting:
          User_Agent: <string>
          fds_clt_ssl_protocol: <value in [sslv3, tlsv1.0, tlsv1.1, ...]>
          fds_ssl_protocol: <value in [sslv3, tlsv1.0, tlsv1.1, ...]>
          fmtr_log: <value in [emergency, alert, critical, ...]>
          linkd_log: <value in [emergency, alert, critical, ...]>
          max_av_ips_version: <integer>
          max_work: <integer>
          push_override:
            ip: <string>
            port: <integer>
            status: <value in [disable, enable]>
          push_override_to_client:
            announce_ip:
              -
                id: <integer>
                ip: <string>
                port: <integer>
            status: <value in [disable, enable]>
          send_report: <value in [disable, enable]>
          send_setup: <value in [disable, enable]>
          server_override:
            servlist:
              -
                id: <integer>
                ip: <string>
                ip6: <string>
                port: <integer>
                service_type: # <list or string>
                  - fds
                  - fct
                  - fai
            status: <value in [disable, enable]>
          system_support_fct:
            - 4.x
            - 5.0
            - 5.2
            - 5.4
            - 5.6
            - 6.0
            - 6.2
            - 6.4
            - 7.0
            - 7.2
          system_support_fgt:
            - 5.4
            - 5.6
            - 6.0
            - 6.2
            - 6.4
            - 7.0
            - 7.2
            - 7.4
            - 7.6
          system_support_fml:
            - 4.x
            - 5.x
            - 6.x
            - 6.0
            - 6.2
            - 6.4
            - 7.0
            - 7.2
            - 7.x
          system_support_fsa:
            - 1.x
            - 2.x
            - 3.x
            - 4.x
            - 3.0
            - 3.1
            - 3.2
          system_support_fsw:
            - 5.4
            - 5.6
            - 6.0
            - 6.2
            - 4.x
            - 5.0
            - 5.2
            - 6.4
          umsvc_log: <value in [emergency, alert, critical, ...]>
          unreg_dev_option: <value in [ignore, svc-only, add-service]>
          update_schedule:
            day: <value in [Sunday, Monday, Tuesday, ...]>
            frequency: <value in [every, daily, weekly]>
            status: <value in [disable, enable]>
            time: <list or string>
          wanip_query_mode: <value in [disable, ipify]>
          fortiguard_anycast: <value in [disable, enable]>
          fortiguard_anycast_source: <value in [fortinet, aws]>
          system_support_fdc:
            - 3.x
            - 4.x
          system_support_fts:
            - 3.x
            - 4.x
            - 7.x
          system_support_faz:
            - 6.x
            - 7.x
          system_support_fis:
            - 1.x
            - 2.x
          system_support_fai:
            - 7.x
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
        '/cli/global/fmupdate/fds-setting'
    ]

    perobject_jrpc_urls = [
        '/cli/global/fmupdate/fds-setting/{fds-setting}'
    ]

    url_params = []
    module_primary_key = None
    module_arg_spec = {
        'fmupdate_fdssetting': {
            'type': 'dict',
            'v_range': [['6.0.0', '']],
            'options': {
                'User-Agent': {'type': 'str'},
                'fds-clt-ssl-protocol': {'choices': ['sslv3', 'tlsv1.0', 'tlsv1.1', 'tlsv1.2', 'tlsv1.3'], 'type': 'str'},
                'fds-ssl-protocol': {'choices': ['sslv3', 'tlsv1.0', 'tlsv1.1', 'tlsv1.2', 'tlsv1.3'], 'type': 'str'},
                'fmtr-log': {'choices': ['emergency', 'alert', 'critical', 'error', 'warn', 'notice', 'info', 'debug', 'disable'], 'type': 'str'},
                'linkd-log': {'choices': ['emergency', 'alert', 'critical', 'error', 'warn', 'notice', 'info', 'debug', 'disable'], 'type': 'str'},
                'max-av-ips-version': {'type': 'int'},
                'max-work': {'type': 'int'},
                'push-override': {
                    'type': 'dict',
                    'options': {'ip': {'type': 'str'}, 'port': {'type': 'int'}, 'status': {'choices': ['disable', 'enable'], 'type': 'str'}}
                },
                'push-override-to-client': {
                    'type': 'dict',
                    'options': {
                        'announce-ip': {
                            'type': 'list',
                            'options': {'id': {'type': 'int'}, 'ip': {'type': 'str'}, 'port': {'type': 'int'}},
                            'elements': 'dict'
                        },
                        'status': {'choices': ['disable', 'enable'], 'type': 'str'}
                    }
                },
                'send_report': {'choices': ['disable', 'enable'], 'type': 'str'},
                'send_setup': {'choices': ['disable', 'enable'], 'type': 'str'},
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
                                'service-type': {'type': 'raw', 'choices': ['fds', 'fct', 'fai']}
                            },
                            'elements': 'dict'
                        },
                        'status': {'choices': ['disable', 'enable'], 'type': 'str'}
                    }
                },
                'system-support-fct': {
                    'type': 'list',
                    'choices': ['4.x', '5.0', '5.2', '5.4', '5.6', '6.0', '6.2', '6.4', '7.0', '7.2'],
                    'elements': 'str'
                },
                'system-support-fgt': {'type': 'list', 'choices': ['5.4', '5.6', '6.0', '6.2', '6.4', '7.0', '7.2', '7.4', '7.6'], 'elements': 'str'},
                'system-support-fml': {'type': 'list', 'choices': ['4.x', '5.x', '6.x', '6.0', '6.2', '6.4', '7.0', '7.2', '7.x'], 'elements': 'str'},
                'system-support-fsa': {'type': 'list', 'choices': ['1.x', '2.x', '3.x', '4.x', '3.0', '3.1', '3.2'], 'elements': 'str'},
                'system-support-fsw': {
                    'v_range': [['6.0.0', '6.4.5'], ['7.0.0', '7.0.0']],
                    'type': 'list',
                    'choices': ['5.4', '5.6', '6.0', '6.2', '4.x', '5.0', '5.2', '6.4'],
                    'elements': 'str'
                },
                'umsvc-log': {'choices': ['emergency', 'alert', 'critical', 'error', 'warn', 'notice', 'info', 'debug', 'disable'], 'type': 'str'},
                'unreg-dev-option': {'choices': ['ignore', 'svc-only', 'add-service'], 'type': 'str'},
                'update-schedule': {
                    'type': 'dict',
                    'options': {
                        'day': {'choices': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], 'type': 'str'},
                        'frequency': {'choices': ['every', 'daily', 'weekly'], 'type': 'str'},
                        'status': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'time': {'type': 'raw'}
                    }
                },
                'wanip-query-mode': {'choices': ['disable', 'ipify'], 'type': 'str'},
                'fortiguard-anycast': {'v_range': [['6.4.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'fortiguard-anycast-source': {'v_range': [['6.4.0', '']], 'choices': ['fortinet', 'aws'], 'type': 'str'},
                'system-support-fdc': {'v_range': [['6.4.6', '6.4.14'], ['7.0.1', '']], 'type': 'list', 'choices': ['3.x', '4.x'], 'elements': 'str'},
                'system-support-fts': {
                    'v_range': [['6.4.6', '6.4.14'], ['7.0.1', '']],
                    'type': 'list',
                    'choices': ['3.x', '4.x', '7.x'],
                    'elements': 'str'
                },
                'system-support-faz': {'v_range': [['7.0.7', '7.0.12'], ['7.2.2', '']], 'type': 'list', 'choices': ['6.x', '7.x'], 'elements': 'str'},
                'system-support-fis': {'v_range': [['7.4.0', '']], 'type': 'list', 'choices': ['1.x', '2.x'], 'elements': 'str'},
                'system-support-fai': {'v_range': [['7.6.0', '']], 'type': 'list', 'choices': ['7.x'], 'elements': 'str'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('partial crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'fmupdate_fdssetting'),
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
