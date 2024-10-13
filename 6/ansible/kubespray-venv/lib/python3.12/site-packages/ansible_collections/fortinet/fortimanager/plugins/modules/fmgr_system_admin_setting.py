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
module: fmgr_system_admin_setting
short_description: Admin setting.
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
    system_admin_setting:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            access-banner:
                type: str
                description:
                    - Deprecated, please rename it to access_banner.
                    - Enable/disable access banner.
                    - disable - Disable setting.
                    - enable - Enable setting.
                choices:
                    - 'disable'
                    - 'enable'
            admin-https-redirect:
                type: str
                description:
                    - Deprecated, please rename it to admin_https_redirect.
                    - Enable/disable redirection of HTTP admin traffic to HTTPS.
                    - disable - Disable setting.
                    - enable - Enable setting.
                choices:
                    - 'disable'
                    - 'enable'
            admin-login-max:
                type: int
                description: Deprecated, please rename it to admin_login_max. Maximum number admin users logged in at one time
            admin_server_cert:
                type: str
                description: HTTPS & Web Service server certificate.
            allow_register:
                type: str
                description:
                    - Enable/disable allowance of register an unregistered device.
                    - disable - Disable setting.
                    - enable - Enable setting.
                choices:
                    - 'disable'
                    - 'enable'
            auto-update:
                type: str
                description:
                    - Deprecated, please rename it to auto_update.
                    - Enable/disable FortiGate automatic update.
                    - disable - Disable device automatic update.
                    - enable - Enable device automatic update.
                choices:
                    - 'disable'
                    - 'enable'
            banner-message:
                type: str
                description: Deprecated, please rename it to banner_message. Banner message.
            chassis-mgmt:
                type: str
                description:
                    - Deprecated, please rename it to chassis_mgmt.
                    - Enable or disable chassis management.
                    - disable - Disable setting.
                    - enable - Enable setting.
                choices:
                    - 'disable'
                    - 'enable'
            chassis-update-interval:
                type: int
                description: Deprecated, please rename it to chassis_update_interval. Chassis background update interval
            device_sync_status:
                type: str
                description:
                    - Enable/disable device synchronization status indication.
                    - disable - Disable setting.
                    - enable - Enable setting.
                choices:
                    - 'disable'
                    - 'enable'
            gui-theme:
                type: str
                description:
                    - Deprecated, please rename it to gui_theme.
                    - Color scheme to use for the administration GUI.
                    - blue - Blueberry
                    - green - Kiwi
                    - red - Cherry
                    - melongene - Plum
                    - spring - Spring
                    - summer - Summer
                    - autumn - Autumn
                    - winter - Winter
                    - space - Space
                    - calla-lily - Calla Lily
                    - binary-tunnel - Binary Tunnel
                    - diving - Diving
                    - dreamy - Dreamy
                    - technology - Technology
                    - landscape - Landscape
                    - twilight - Twilight
                    - canyon - Canyon
                    - northern-light - Northern Light
                    - astronomy - Astronomy
                    - fish - Fish
                    - penguin - Penguin
                    - panda - Panda
                    - polar-bear - Polar Bear
                    - parrot - Parrot
                    - cave - Cave
                choices:
                    - 'blue'
                    - 'green'
                    - 'red'
                    - 'melongene'
                    - 'spring'
                    - 'summer'
                    - 'autumn'
                    - 'winter'
                    - 'space'
                    - 'calla-lily'
                    - 'binary-tunnel'
                    - 'diving'
                    - 'dreamy'
                    - 'technology'
                    - 'landscape'
                    - 'twilight'
                    - 'canyon'
                    - 'northern-light'
                    - 'astronomy'
                    - 'fish'
                    - 'penguin'
                    - 'panda'
                    - 'polar-bear'
                    - 'parrot'
                    - 'cave'
                    - 'mountain'
                    - 'zebra'
                    - 'contrast-dark'
                    - 'circuit-board'
                    - 'mars'
                    - 'blue-sea'
                    - 'mariner'
                    - 'jade'
                    - 'neutrino'
                    - 'dark-matter'
                    - 'forest'
                    - 'cat'
                    - 'graphite'
            http_port:
                type: int
                description: HTTP port.
            https_port:
                type: int
                description: HTTPS port.
            idle_timeout:
                type: int
                description: Idle timeout
            install-ifpolicy-only:
                type: str
                description:
                    - Deprecated, please rename it to install_ifpolicy_only.
                    - Allow install interface policy only.
                    - disable - Disable setting.
                    - enable - Enable setting.
                choices:
                    - 'disable'
                    - 'enable'
            mgmt-addr:
                type: str
                description: Deprecated, please rename it to mgmt_addr. IP of FortiManager used by FGFM.
            mgmt-fqdn:
                type: str
                description: Deprecated, please rename it to mgmt_fqdn. FQDN of FortiManager used by FGFM.
            objects-force-deletion:
                type: str
                description:
                    - Deprecated, please rename it to objects_force_deletion.
                    - Enable/disable used objects force deletion.
                    - disable - Disable setting.
                    - enable - Enable setting.
                choices:
                    - 'disable'
                    - 'enable'
            offline_mode:
                type: str
                description:
                    - Enable/disable offline mode.
                    - disable - Disable offline mode.
                    - enable - Enable offline mode.
                choices:
                    - 'disable'
                    - 'enable'
            register_passwd:
                type: raw
                description: (list) Password for register a device.
            sdwan-monitor-history:
                type: str
                description:
                    - Deprecated, please rename it to sdwan_monitor_history.
                    - Enable/disable hostname display in the GUI login page.
                    - disable - Disable setting.
                    - enable - Enable setting.
                choices:
                    - 'disable'
                    - 'enable'
            shell-access:
                type: str
                description:
                    - Deprecated, please rename it to shell_access.
                    - Enable/disable shell access.
                    - disable - Disable setting.
                    - enable - Enable setting.
                choices:
                    - 'disable'
                    - 'enable'
            shell-password:
                type: raw
                description: (list) Deprecated, please rename it to shell_password. Password for shell access.
            show-add-multiple:
                type: str
                description:
                    - Deprecated, please rename it to show_add_multiple.
                    - Show add multiple button.
                    - disable - Disable setting.
                    - enable - Enable setting.
                choices:
                    - 'disable'
                    - 'enable'
            show-adom-devman:
                type: str
                description:
                    - Deprecated, please rename it to show_adom_devman.
                    - Show ADOM device manager tools on GUI.
                    - disable - Hide device manager tools on GUI.
                    - enable - Show device manager tools on GUI.
                choices:
                    - 'disable'
                    - 'enable'
            show-checkbox-in-table:
                type: str
                description:
                    - Deprecated, please rename it to show_checkbox_in_table.
                    - Show checkboxs in tables on GUI.
                    - disable - Disable setting.
                    - enable - Enable setting.
                choices:
                    - 'disable'
                    - 'enable'
            show-device-import-export:
                type: str
                description:
                    - Deprecated, please rename it to show_device_import_export.
                    - Enable/disable import/export of ADOM, device, and group lists.
                    - disable - Disable setting.
                    - enable - Enable setting.
                choices:
                    - 'disable'
                    - 'enable'
            show-hostname:
                type: str
                description:
                    - Deprecated, please rename it to show_hostname.
                    - Enable/disable hostname display in the GUI login page.
                    - disable - Disable setting.
                    - enable - Enable setting.
                choices:
                    - 'disable'
                    - 'enable'
            show_automatic_script:
                type: str
                description:
                    - Enable/disable automatic script.
                    - disable - Disable script option.
                    - enable - Enable script option.
                choices:
                    - 'disable'
                    - 'enable'
            show_grouping_script:
                type: str
                description:
                    - Enable/disable grouping script.
                    - disable - Disable script option.
                    - enable - Enable script option.
                choices:
                    - 'disable'
                    - 'enable'
            show_schedule_script:
                type: str
                description:
                    - Enable or disable schedule script.
                    - disable - Disable script option.
                    - enable - Enable script option.
                choices:
                    - 'disable'
                    - 'enable'
            show_tcl_script:
                type: str
                description:
                    - Enable/disable TCL script.
                    - disable - Disable script option.
                    - enable - Enable script option.
                choices:
                    - 'disable'
                    - 'enable'
            unreg_dev_opt:
                type: str
                description:
                    - Action to take when unregistered device connects to FortiManager.
                    - add_no_service - Add unregistered devices but deny service requests.
                    - ignore - Ignore unregistered devices.
                    - add_allow_service - Add unregistered devices and allow service requests.
                choices:
                    - 'add_no_service'
                    - 'ignore'
                    - 'add_allow_service'
            webadmin_language:
                type: str
                description:
                    - Web admin language.
                    - auto_detect - Automatically detect language.
                    - english - English.
                    - simplified_chinese - Simplified Chinese.
                    - traditional_chinese - Traditional Chinese.
                    - japanese - Japanese.
                    - korean - Korean.
                    - spanish - Spanish.
                choices:
                    - 'auto_detect'
                    - 'english'
                    - 'simplified_chinese'
                    - 'traditional_chinese'
                    - 'japanese'
                    - 'korean'
                    - 'spanish'
                    - 'french'
            show-fct-manager:
                type: str
                description:
                    - Deprecated, please rename it to show_fct_manager.
                    - Enable/disable FCT manager.
                    - disable - Disable setting.
                    - enable - Enable setting.
                choices:
                    - 'disable'
                    - 'enable'
            sdwan-skip-unmapped-input-device:
                type: str
                description:
                    - Deprecated, please rename it to sdwan_skip_unmapped_input_device.
                    - Skip unmapped interface for sdwan/rule/input-device instead of report mapping error.
                    - disable - Disable setting.
                    - enable - Enable setting.
                choices:
                    - 'disable'
                    - 'enable'
            auth-addr:
                type: str
                description: Deprecated, please rename it to auth_addr. IP which is used by FGT to authorize FMG.
            auth-port:
                type: int
                description: Deprecated, please rename it to auth_port. Port which is used by FGT to authorize FMG.
            idle_timeout_api:
                type: int
                description: Idle timeout for API sessions
            idle_timeout_gui:
                type: int
                description: Idle timeout for GUI sessions
            central-ftgd-local-cat-id:
                type: str
                description:
                    - Deprecated, please rename it to central_ftgd_local_cat_id.
                    - Central FortiGuard local category id management, and do not auto assign id during installation.
                    - disable - Disable setting.
                    - enable - Enable setting.
                choices:
                    - 'disable'
                    - 'enable'
            idle_timeout_sso:
                type: int
                description: Idle timeout for SSO sessions
            preferred-fgfm-intf:
                type: str
                description: Deprecated, please rename it to preferred_fgfm_intf. Preferred interface for FGFM connection.
            traffic-shaping-history:
                type: str
                description:
                    - Deprecated, please rename it to traffic_shaping_history.
                    - Enable/disable traffic-shaping-history.
                    - disable - Disable setting.
                    - enable - Enable setting.
                choices:
                    - 'disable'
                    - 'enable'
            fsw-ignore-platform-check:
                type: str
                description:
                    - Deprecated, please rename it to fsw_ignore_platform_check.
                    - Enable/disable FortiSwitch Manager switch platform support check.
                    - disable - Disable setting.
                    - enable - Enable setting.
                choices:
                    - 'disable'
                    - 'enable'
            rtm-max-monitor-by-days:
                type: int
                description: Deprecated, please rename it to rtm_max_monitor_by_days. Maximum rtm monitor
            rtm-temp-file-limit:
                type: int
                description: Deprecated, please rename it to rtm_temp_file_limit. Set rtm monitor temp file limit by hours.
            firmware-upgrade-check:
                type: str
                description:
                    - Deprecated, please rename it to firmware_upgrade_check.
                    - Enable/disable firmware upgrade check.
                    - disable - Disable setting.
                    - enable - Enable setting.
                choices:
                    - 'disable'
                    - 'enable'
            fgt-gui-proxy:
                type: str
                description:
                    - Deprecated, please rename it to fgt_gui_proxy.
                    - Enable/disable FortiGate GUI proxy.
                    - disable - Disable setting.
                    - enable - Enable setting.
                choices:
                    - 'disable'
                    - 'enable'
            fgt-gui-proxy-port:
                type: int
                description: Deprecated, please rename it to fgt_gui_proxy_port. FortiGate GUI proxy port.
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
    - name: Admin setting.
      fortinet.fortimanager.fmgr_system_admin_setting:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        system_admin_setting:
          access_banner: <value in [disable, enable]>
          admin_https_redirect: <value in [disable, enable]>
          admin_login_max: <integer>
          admin_server_cert: <string>
          allow_register: <value in [disable, enable]>
          auto_update: <value in [disable, enable]>
          banner_message: <string>
          chassis_mgmt: <value in [disable, enable]>
          chassis_update_interval: <integer>
          device_sync_status: <value in [disable, enable]>
          gui_theme: <value in [blue, green, red, ...]>
          http_port: <integer>
          https_port: <integer>
          idle_timeout: <integer>
          install_ifpolicy_only: <value in [disable, enable]>
          mgmt_addr: <string>
          mgmt_fqdn: <string>
          objects_force_deletion: <value in [disable, enable]>
          offline_mode: <value in [disable, enable]>
          register_passwd: <list or string>
          sdwan_monitor_history: <value in [disable, enable]>
          shell_access: <value in [disable, enable]>
          shell_password: <list or string>
          show_add_multiple: <value in [disable, enable]>
          show_adom_devman: <value in [disable, enable]>
          show_checkbox_in_table: <value in [disable, enable]>
          show_device_import_export: <value in [disable, enable]>
          show_hostname: <value in [disable, enable]>
          show_automatic_script: <value in [disable, enable]>
          show_grouping_script: <value in [disable, enable]>
          show_schedule_script: <value in [disable, enable]>
          show_tcl_script: <value in [disable, enable]>
          unreg_dev_opt: <value in [add_no_service, ignore, add_allow_service]>
          webadmin_language: <value in [auto_detect, english, simplified_chinese, ...]>
          show_fct_manager: <value in [disable, enable]>
          sdwan_skip_unmapped_input_device: <value in [disable, enable]>
          auth_addr: <string>
          auth_port: <integer>
          idle_timeout_api: <integer>
          idle_timeout_gui: <integer>
          central_ftgd_local_cat_id: <value in [disable, enable]>
          idle_timeout_sso: <integer>
          preferred_fgfm_intf: <string>
          traffic_shaping_history: <value in [disable, enable]>
          fsw_ignore_platform_check: <value in [disable, enable]>
          rtm_max_monitor_by_days: <integer>
          rtm_temp_file_limit: <integer>
          firmware_upgrade_check: <value in [disable, enable]>
          fgt_gui_proxy: <value in [disable, enable]>
          fgt_gui_proxy_port: <integer>
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
        '/cli/global/system/admin/setting'
    ]

    perobject_jrpc_urls = [
        '/cli/global/system/admin/setting/{setting}'
    ]

    url_params = []
    module_primary_key = None
    module_arg_spec = {
        'system_admin_setting': {
            'type': 'dict',
            'v_range': [['6.0.0', '']],
            'options': {
                'access-banner': {'choices': ['disable', 'enable'], 'type': 'str'},
                'admin-https-redirect': {'choices': ['disable', 'enable'], 'type': 'str'},
                'admin-login-max': {'type': 'int'},
                'admin_server_cert': {'type': 'str'},
                'allow_register': {'choices': ['disable', 'enable'], 'type': 'str'},
                'auto-update': {'choices': ['disable', 'enable'], 'type': 'str'},
                'banner-message': {'type': 'str'},
                'chassis-mgmt': {'choices': ['disable', 'enable'], 'type': 'str'},
                'chassis-update-interval': {'type': 'int'},
                'device_sync_status': {'choices': ['disable', 'enable'], 'type': 'str'},
                'gui-theme': {
                    'choices': [
                        'blue', 'green', 'red', 'melongene', 'spring', 'summer', 'autumn', 'winter', 'space', 'calla-lily', 'binary-tunnel', 'diving',
                        'dreamy', 'technology', 'landscape', 'twilight', 'canyon', 'northern-light', 'astronomy', 'fish', 'penguin', 'panda',
                        'polar-bear', 'parrot', 'cave', 'mountain', 'zebra', 'contrast-dark', 'circuit-board', 'mars', 'blue-sea', 'mariner', 'jade',
                        'neutrino', 'dark-matter', 'forest', 'cat', 'graphite'
                    ],
                    'type': 'str'
                },
                'http_port': {'type': 'int'},
                'https_port': {'type': 'int'},
                'idle_timeout': {'type': 'int'},
                'install-ifpolicy-only': {'choices': ['disable', 'enable'], 'type': 'str'},
                'mgmt-addr': {'type': 'str'},
                'mgmt-fqdn': {'type': 'str'},
                'objects-force-deletion': {'choices': ['disable', 'enable'], 'type': 'str'},
                'offline_mode': {'choices': ['disable', 'enable'], 'type': 'str'},
                'register_passwd': {'no_log': True, 'type': 'raw'},
                'sdwan-monitor-history': {'choices': ['disable', 'enable'], 'type': 'str'},
                'shell-access': {'v_range': [['6.0.0', '7.4.3']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'shell-password': {'v_range': [['6.0.0', '7.4.3']], 'no_log': True, 'type': 'raw'},
                'show-add-multiple': {'choices': ['disable', 'enable'], 'type': 'str'},
                'show-adom-devman': {'choices': ['disable', 'enable'], 'type': 'str'},
                'show-checkbox-in-table': {'choices': ['disable', 'enable'], 'type': 'str'},
                'show-device-import-export': {'choices': ['disable', 'enable'], 'type': 'str'},
                'show-hostname': {'choices': ['disable', 'enable'], 'type': 'str'},
                'show_automatic_script': {'choices': ['disable', 'enable'], 'type': 'str'},
                'show_grouping_script': {'choices': ['disable', 'enable'], 'type': 'str'},
                'show_schedule_script': {'choices': ['disable', 'enable'], 'type': 'str'},
                'show_tcl_script': {'choices': ['disable', 'enable'], 'type': 'str'},
                'unreg_dev_opt': {'choices': ['add_no_service', 'ignore', 'add_allow_service'], 'type': 'str'},
                'webadmin_language': {
                    'choices': ['auto_detect', 'english', 'simplified_chinese', 'traditional_chinese', 'japanese', 'korean', 'spanish', 'french'],
                    'type': 'str'
                },
                'show-fct-manager': {'v_range': [['6.4.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'sdwan-skip-unmapped-input-device': {'v_range': [['6.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'auth-addr': {'v_range': [['7.0.0', '']], 'type': 'str'},
                'auth-port': {'v_range': [['7.0.0', '']], 'type': 'int'},
                'idle_timeout_api': {'v_range': [['6.4.6', '']], 'type': 'int'},
                'idle_timeout_gui': {'v_range': [['6.4.6', '']], 'type': 'int'},
                'central-ftgd-local-cat-id': {'v_range': [['6.4.6', '6.4.14'], ['7.0.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'idle_timeout_sso': {'v_range': [['7.0.3', '']], 'type': 'int'},
                'preferred-fgfm-intf': {'v_range': [['7.0.2', '']], 'type': 'str'},
                'traffic-shaping-history': {'v_range': [['7.0.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'fsw-ignore-platform-check': {'v_range': [['7.0.7', '7.0.12'], ['7.2.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'rtm-max-monitor-by-days': {'v_range': [['7.2.2', '']], 'type': 'int'},
                'rtm-temp-file-limit': {'v_range': [['7.2.2', '']], 'type': 'int'},
                'firmware-upgrade-check': {'v_range': [['7.2.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'fgt-gui-proxy': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'fgt-gui-proxy-port': {'v_range': [['7.4.2', '']], 'type': 'int'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('partial crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'system_admin_setting'),
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
