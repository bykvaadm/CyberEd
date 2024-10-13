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
module: fmgr_system_admin_user
short_description: Admin user.
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
    system_admin_user:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            adom:
                type: list
                elements: dict
                description: Adom.
                suboptions:
                    adom-name:
                        type: str
                        description: Deprecated, please rename it to adom_name. Admin domain names.
            adom-exclude:
                type: list
                elements: dict
                description: Deprecated, please rename it to adom_exclude. Adom exclude.
                suboptions:
                    adom-name:
                        type: str
                        description: Deprecated, please rename it to adom_name. Admin domain names.
            app-filter:
                type: list
                elements: dict
                description: Deprecated, please rename it to app_filter. App filter.
                suboptions:
                    app-filter-name:
                        type: str
                        description: Deprecated, please rename it to app_filter_name. App filter name.
            avatar:
                type: str
                description: Image file for avatar
            ca:
                type: str
                description: PKI user certificate CA
            change-password:
                type: str
                description:
                    - Deprecated, please rename it to change_password.
                    - Enable/disable restricted user to change self password.
                    - disable - Disable setting.
                    - enable - Enable setting.
                choices:
                    - 'disable'
                    - 'enable'
            dashboard:
                type: list
                elements: dict
                description: Dashboard.
                suboptions:
                    column:
                        type: int
                        description: Widgets column ID.
                    diskio-content-type:
                        type: str
                        description:
                            - Deprecated, please rename it to diskio_content_type.
                            - Disk I/O Monitor widgets chart type.
                            - util - bandwidth utilization.
                            - iops - the number of I/O requests.
                            - blks - the amount of data of I/O requests.
                        choices:
                            - 'util'
                            - 'iops'
                            - 'blks'
                    diskio-period:
                        type: str
                        description:
                            - Deprecated, please rename it to diskio_period.
                            - Disk I/O Monitor widgets data period.
                            - 1hour - 1 hour.
                            - 8hour - 8 hour.
                            - 24hour - 24 hour.
                        choices:
                            - '1hour'
                            - '8hour'
                            - '24hour'
                    log-rate-period:
                        type: str
                        description:
                            - Deprecated, please rename it to log_rate_period.
                            - Log receive monitor widgets data period.
                            - 2min  - 2 minutes.
                            - 1hour - 1 hour.
                            - 6hours - 6 hours.
                        choices:
                            - '2min'
                            - '1hour'
                            - '6hours'
                    log-rate-topn:
                        type: str
                        description:
                            - Deprecated, please rename it to log_rate_topn.
                            - Log receive monitor widgets number of top items to display.
                            - 1 - Top 1.
                            - 2 - Top 2.
                            - 3 - Top 3.
                            - 4 - Top 4.
                            - 5 - Top 5.
                        choices:
                            - '1'
                            - '2'
                            - '3'
                            - '4'
                            - '5'
                    log-rate-type:
                        type: str
                        description:
                            - Deprecated, please rename it to log_rate_type.
                            - Log receive monitor widgets statistics breakdown options.
                            - log - Show log rates for each log type.
                            - device - Show log rates for each device.
                        choices:
                            - 'log'
                            - 'device'
                    moduleid:
                        type: int
                        description: Widget ID.
                    name:
                        type: str
                        description: Widget name.
                    num-entries:
                        type: int
                        description: Deprecated, please rename it to num_entries. Number of entries.
                    refresh-interval:
                        type: int
                        description: Deprecated, please rename it to refresh_interval. Widgets refresh interval.
                    res-cpu-display:
                        type: str
                        description:
                            - Deprecated, please rename it to res_cpu_display.
                            - Widgets CPU display type.
                            - average  - Average usage of CPU.
                            - each - Each usage of CPU.
                        choices:
                            - 'average'
                            - 'each'
                    res-period:
                        type: str
                        description:
                            - Deprecated, please rename it to res_period.
                            - Widgets data period.
                            - 10min  - Last 10 minutes.
                            - hour - Last hour.
                            - day - Last day.
                        choices:
                            - '10min'
                            - 'hour'
                            - 'day'
                    res-view-type:
                        type: str
                        description:
                            - Deprecated, please rename it to res_view_type.
                            - Widgets data view type.
                            - real-time  - Real-time view.
                            - history - History view.
                        choices:
                            - 'real-time'
                            - 'history'
                    status:
                        type: str
                        description:
                            - Widgets opened/closed state.
                            - close - Widget closed.
                            - open - Widget opened.
                        choices:
                            - 'close'
                            - 'open'
                    tabid:
                        type: int
                        description: ID of tab where widget is displayed.
                    time-period:
                        type: str
                        description:
                            - Deprecated, please rename it to time_period.
                            - Log Database Monitor widgets data period.
                            - 1hour - 1 hour.
                            - 8hour - 8 hour.
                            - 24hour - 24 hour.
                        choices:
                            - '1hour'
                            - '8hour'
                            - '24hour'
                    widget-type:
                        type: str
                        description:
                            - Deprecated, please rename it to widget_type.
                            - Widget type.
                            - top-lograte - Log Receive Monitor.
                            - sysres - System resources.
                            - sysinfo - System Information.
                            - licinfo - License Information.
                            - jsconsole - CLI Console.
                            - sysop - Unit Operation.
                            - alert - Alert Message Console.
                            - statistics - Statistics.
                            - rpteng - Report Engine.
                            - raid - Disk Monitor.
                            - logrecv - Logs/Data Received.
                            - devsummary - Device Summary.
                            - logdb-perf - Log Database Performance Monitor.
                            - logdb-lag - Log Database Lag Time.
                            - disk-io - Disk I/O.
                            - log-rcvd-fwd - Log receive and forwarding Monitor.
                        choices:
                            - 'top-lograte'
                            - 'sysres'
                            - 'sysinfo'
                            - 'licinfo'
                            - 'jsconsole'
                            - 'sysop'
                            - 'alert'
                            - 'statistics'
                            - 'rpteng'
                            - 'raid'
                            - 'logrecv'
                            - 'devsummary'
                            - 'logdb-perf'
                            - 'logdb-lag'
                            - 'disk-io'
                            - 'log-rcvd-fwd'
            dashboard-tabs:
                type: list
                elements: dict
                description: Deprecated, please rename it to dashboard_tabs. Dashboard tabs.
                suboptions:
                    name:
                        type: str
                        description: Tab name.
                    tabid:
                        type: int
                        description: Tab ID.
            description:
                type: str
                description: Description.
            dev-group:
                type: str
                description: Deprecated, please rename it to dev_group. Device group.
            email-address:
                type: str
                description: Deprecated, please rename it to email_address. Email address.
            ext-auth-accprofile-override:
                type: str
                description:
                    - Deprecated, please rename it to ext_auth_accprofile_override.
                    - Allow to use the access profile provided by the remote authentication server.
                    - disable - Disable access profile override.
                    - enable - Enable access profile override.
                choices:
                    - 'disable'
                    - 'enable'
            ext-auth-adom-override:
                type: str
                description:
                    - Deprecated, please rename it to ext_auth_adom_override.
                    - Allow to use the ADOM provided by the remote authentication server.
                    - disable - Disable ADOM override.
                    - enable - Enable ADOM override.
                choices:
                    - 'disable'
                    - 'enable'
            ext-auth-group-match:
                type: str
                description: Deprecated, please rename it to ext_auth_group_match. Only administrators belonging to this group can login.
            first-name:
                type: str
                description: Deprecated, please rename it to first_name. First name.
            force-password-change:
                type: str
                description:
                    - Deprecated, please rename it to force_password_change.
                    - Enable/disable force password change on next login.
                    - disable - Disable setting.
                    - enable - Enable setting.
                choices:
                    - 'disable'
                    - 'enable'
            group:
                type: str
                description: Group name.
            hidden:
                type: int
                description: Hidden administrator.
            ips-filter:
                type: list
                elements: dict
                description: Deprecated, please rename it to ips_filter. Ips filter.
                suboptions:
                    ips-filter-name:
                        type: str
                        description: Deprecated, please rename it to ips_filter_name. IPS filter name.
            ipv6_trusthost1:
                type: str
                description: Admin user trusted host IPv6, default
            ipv6_trusthost10:
                type: str
                description: Admin user trusted host IPv6, default ffff
            ipv6_trusthost2:
                type: str
                description: Admin user trusted host IPv6, default ffff
            ipv6_trusthost3:
                type: str
                description: Admin user trusted host IPv6, default ffff
            ipv6_trusthost4:
                type: str
                description: Admin user trusted host IPv6, default ffff
            ipv6_trusthost5:
                type: str
                description: Admin user trusted host IPv6, default ffff
            ipv6_trusthost6:
                type: str
                description: Admin user trusted host IPv6, default ffff
            ipv6_trusthost7:
                type: str
                description: Admin user trusted host IPv6, default ffff
            ipv6_trusthost8:
                type: str
                description: Admin user trusted host IPv6, default ffff
            ipv6_trusthost9:
                type: str
                description: Admin user trusted host IPv6, default ffff
            last-name:
                type: str
                description: Deprecated, please rename it to last_name. Last name.
            ldap-server:
                type: str
                description: Deprecated, please rename it to ldap_server. LDAP server name.
            meta-data:
                type: list
                elements: dict
                description: Deprecated, please rename it to meta_data. Meta data.
                suboptions:
                    fieldlength:
                        type: int
                        description: Field length.
                    fieldname:
                        type: str
                        description: Field name.
                    fieldvalue:
                        type: str
                        description: Field value.
                    importance:
                        type: str
                        description:
                            - Importance.
                            - optional - This field is optional.
                            - required - This field is required.
                        choices:
                            - 'optional'
                            - 'required'
                    status:
                        type: str
                        description:
                            - Status.
                            - disabled - This field is disabled.
                            - enabled - This field is enabled.
                        choices:
                            - 'disabled'
                            - 'enabled'
            mobile-number:
                type: str
                description: Deprecated, please rename it to mobile_number. Mobile number.
            pager-number:
                type: str
                description: Deprecated, please rename it to pager_number. Pager number.
            password:
                type: raw
                description: (list) Password.
            password-expire:
                type: raw
                description: (list or str) Deprecated, please rename it to password_expire. Password expire time in GMT.
            phone-number:
                type: str
                description: Deprecated, please rename it to phone_number. Phone number.
            policy-package:
                type: list
                elements: dict
                description: Deprecated, please rename it to policy_package. Policy package.
                suboptions:
                    policy-package-name:
                        type: str
                        description: Deprecated, please rename it to policy_package_name. Policy package names.
            profileid:
                type: str
                description: Profile ID.
            radius_server:
                type: str
                description: RADIUS server name.
            restrict-access:
                type: str
                description:
                    - Deprecated, please rename it to restrict_access.
                    - Enable/disable restricted access to development VDOM.
                    - disable - Disable setting.
                    - enable - Enable setting.
                choices:
                    - 'disable'
                    - 'enable'
            restrict-dev-vdom:
                type: list
                elements: dict
                description: Deprecated, please rename it to restrict_dev_vdom. Restrict dev vdom.
                suboptions:
                    dev-vdom:
                        type: str
                        description: Deprecated, please rename it to dev_vdom. Device or device VDOM.
            rpc-permit:
                type: str
                description:
                    - Deprecated, please rename it to rpc_permit.
                    - set none/read/read-write rpc-permission.
                    - read-write - Read-write permission.
                    - none - No permission.
                    - read - Read-only permission.
                choices:
                    - 'read-write'
                    - 'none'
                    - 'read'
                    - 'from-profile'
            ssh-public-key1:
                type: raw
                description: (list) Deprecated, please rename it to ssh_public_key1. SSH public key 1.
            ssh-public-key2:
                type: raw
                description: (list) Deprecated, please rename it to ssh_public_key2. SSH public key 2.
            ssh-public-key3:
                type: raw
                description: (list) Deprecated, please rename it to ssh_public_key3. SSH public key 3.
            subject:
                type: str
                description: PKI user certificate name constraints.
            tacacs-plus-server:
                type: str
                description: Deprecated, please rename it to tacacs_plus_server. TACACS+ server name.
            trusthost1:
                type: str
                description: Admin user trusted host IP, default 0.
            trusthost10:
                type: str
                description: Admin user trusted host IP, default 255.
            trusthost2:
                type: str
                description: Admin user trusted host IP, default 255.
            trusthost3:
                type: str
                description: Admin user trusted host IP, default 255.
            trusthost4:
                type: str
                description: Admin user trusted host IP, default 255.
            trusthost5:
                type: str
                description: Admin user trusted host IP, default 255.
            trusthost6:
                type: str
                description: Admin user trusted host IP, default 255.
            trusthost7:
                type: str
                description: Admin user trusted host IP, default 255.
            trusthost8:
                type: str
                description: Admin user trusted host IP, default 255.
            trusthost9:
                type: str
                description: Admin user trusted host IP, default 255.
            two-factor-auth:
                type: str
                description:
                    - Deprecated, please rename it to two_factor_auth.
                    - Enable 2-factor authentication
                    - disable - Disable 2-factor authentication.
                    - enable - Enable 2-factor authentication.
                choices:
                    - 'disable'
                    - 'enable'
                    - 'password'
                    - 'ftc-ftm'
                    - 'ftc-email'
                    - 'ftc-sms'
            user_type:
                type: str
                description:
                    - User type.
                    - local - Local user.
                    - radius - RADIUS user.
                    - ldap - LDAP user.
                    - tacacs-plus - TACACS+ user.
                    - pki-auth - PKI user.
                    - group - Group user.
                choices:
                    - 'local'
                    - 'radius'
                    - 'ldap'
                    - 'tacacs-plus'
                    - 'pki-auth'
                    - 'group'
                    - 'sso'
                    - 'api'
            userid:
                type: str
                description: User name.
                required: true
            web-filter:
                type: list
                elements: dict
                description: Deprecated, please rename it to web_filter. Web filter.
                suboptions:
                    web-filter-name:
                        type: str
                        description: Deprecated, please rename it to web_filter_name. Web filter name.
            wildcard:
                type: str
                description:
                    - Enable/disable wildcard remote authentication.
                    - disable - Disable username wildcard.
                    - enable - Enable username wildcard.
                choices:
                    - 'disable'
                    - 'enable'
            login-max:
                type: int
                description: Deprecated, please rename it to login_max. Max login session for this user.
            use-global-theme:
                type: str
                description:
                    - Deprecated, please rename it to use_global_theme.
                    - Enable/disble global theme for administration GUI.
                    - disable - Disable setting.
                    - enable - Enable setting.
                choices:
                    - 'disable'
                    - 'enable'
            user-theme:
                type: str
                description:
                    - Deprecated, please rename it to user_theme.
                    - Color scheme to use for the admin user GUI.
                    - blue - Blueberry
                    - green - Kiwi
                    - red - Cherry
                    - melongene - Plum
                    - spring - Spring
                    - summer - Summer
                    - autumn - Autumn
                    - winter - Winter
                    - circuit-board - Circuit Board
                    - calla-lily - Calla Lily
                    - binary-tunnel - Binary Tunnel
                    - mars - Mars
                    - blue-sea - Blue Sea
                    - technology - Technology
                    - landscape - Landscape
                    - twilight - Twilight
                    - canyon - Canyon
                    - northern-light - Northern Light
                    - astronomy - Astronomy
                    - fish - Fish
                    - penguin - Penguin
                    - mountain - Mountain
                    - panda - Panda
                    - parrot - Parrot
                    - cave - Cave
                    - zebra - Zebra
                    - contrast-dark - High Contrast Dark
                choices:
                    - 'blue'
                    - 'green'
                    - 'red'
                    - 'melongene'
                    - 'spring'
                    - 'summer'
                    - 'autumn'
                    - 'winter'
                    - 'circuit-board'
                    - 'calla-lily'
                    - 'binary-tunnel'
                    - 'mars'
                    - 'blue-sea'
                    - 'technology'
                    - 'landscape'
                    - 'twilight'
                    - 'canyon'
                    - 'northern-light'
                    - 'astronomy'
                    - 'fish'
                    - 'penguin'
                    - 'mountain'
                    - 'panda'
                    - 'parrot'
                    - 'cave'
                    - 'zebra'
                    - 'contrast-dark'
                    - 'mariner'
                    - 'jade'
                    - 'neutrino'
                    - 'dark-matter'
                    - 'forest'
                    - 'cat'
                    - 'graphite'
            adom-access:
                type: str
                description:
                    - Deprecated, please rename it to adom_access.
                    - set all/specify/exclude adom access mode.
                    - all - All ADOMs access.
                    - specify - Specify ADOMs access.
                    - exclude - Exclude ADOMs access.
                choices:
                    - 'all'
                    - 'specify'
                    - 'exclude'
                    - 'per-adom-profile'
            fingerprint:
                type: str
                description: PKI user certificate fingerprint
            th-from-profile:
                type: int
                description: Deprecated, please rename it to th_from_profile. Internal use only
            th6-from-profile:
                type: int
                description: Deprecated, please rename it to th6_from_profile. Internal use only
            cors-allow-origin:
                type: str
                description: Deprecated, please rename it to cors_allow_origin. Access-Control-Allow-Origin.
            fortiai:
                type: str
                description:
                    - Enable/disble FortiAI.
                    - disable - Disable setting.
                    - enable - Enable setting.
                choices:
                    - 'disable'
                    - 'enable'
            policy-block:
                type: list
                elements: dict
                description: Deprecated, please rename it to policy_block. Policy block.
                suboptions:
                    policy-block-name:
                        type: str
                        description: Deprecated, please rename it to policy_block_name. Policy block names.
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
    - name: Admin User
      fortinet.fortimanager.fmgr_system_admin_user:
        state: present
        system_admin_user:
          adom:
            - adom-name: ansible
          userid: "ansible-test"
    - name: Admin domain.
      fortinet.fortimanager.fmgr_system_admin_user_adom:
        bypass_validation: false
        user: ansible-test # userid
        state: present
        system_admin_user_adom:
          adom-name: "ALL ADOMS"
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
        '/cli/global/system/admin/user'
    ]

    perobject_jrpc_urls = [
        '/cli/global/system/admin/user/{user}'
    ]

    url_params = []
    module_primary_key = 'userid'
    module_arg_spec = {
        'system_admin_user': {
            'type': 'dict',
            'v_range': [['6.0.0', '']],
            'options': {
                'adom': {'type': 'list', 'options': {'adom-name': {'type': 'str'}}, 'elements': 'dict'},
                'adom-exclude': {
                    'v_range': [['6.0.0', '7.0.2']],
                    'type': 'list',
                    'options': {'adom-name': {'v_range': [['6.0.0', '7.0.2']], 'type': 'str'}},
                    'elements': 'dict'
                },
                'app-filter': {'type': 'list', 'options': {'app-filter-name': {'type': 'str'}}, 'elements': 'dict'},
                'avatar': {'type': 'str'},
                'ca': {'type': 'str'},
                'change-password': {'choices': ['disable', 'enable'], 'type': 'str'},
                'dashboard': {
                    'type': 'list',
                    'options': {
                        'column': {'type': 'int'},
                        'diskio-content-type': {'choices': ['util', 'iops', 'blks'], 'type': 'str'},
                        'diskio-period': {'choices': ['1hour', '8hour', '24hour'], 'type': 'str'},
                        'log-rate-period': {'choices': ['2min', '1hour', '6hours'], 'type': 'str'},
                        'log-rate-topn': {'choices': ['1', '2', '3', '4', '5'], 'type': 'str'},
                        'log-rate-type': {'choices': ['log', 'device'], 'type': 'str'},
                        'moduleid': {'type': 'int'},
                        'name': {'type': 'str'},
                        'num-entries': {'type': 'int'},
                        'refresh-interval': {'type': 'int'},
                        'res-cpu-display': {'choices': ['average', 'each'], 'type': 'str'},
                        'res-period': {'choices': ['10min', 'hour', 'day'], 'type': 'str'},
                        'res-view-type': {'choices': ['real-time', 'history'], 'type': 'str'},
                        'status': {'choices': ['close', 'open'], 'type': 'str'},
                        'tabid': {'type': 'int'},
                        'time-period': {'choices': ['1hour', '8hour', '24hour'], 'type': 'str'},
                        'widget-type': {
                            'choices': [
                                'top-lograte', 'sysres', 'sysinfo', 'licinfo', 'jsconsole', 'sysop', 'alert', 'statistics', 'rpteng', 'raid', 'logrecv',
                                'devsummary', 'logdb-perf', 'logdb-lag', 'disk-io', 'log-rcvd-fwd'
                            ],
                            'type': 'str'
                        }
                    },
                    'elements': 'dict'
                },
                'dashboard-tabs': {'type': 'list', 'options': {'name': {'type': 'str'}, 'tabid': {'type': 'int'}}, 'elements': 'dict'},
                'description': {'type': 'str'},
                'dev-group': {'type': 'str'},
                'email-address': {'type': 'str'},
                'ext-auth-accprofile-override': {'choices': ['disable', 'enable'], 'type': 'str'},
                'ext-auth-adom-override': {'choices': ['disable', 'enable'], 'type': 'str'},
                'ext-auth-group-match': {'type': 'str'},
                'first-name': {'type': 'str'},
                'force-password-change': {'choices': ['disable', 'enable'], 'type': 'str'},
                'group': {'type': 'str'},
                'hidden': {'type': 'int'},
                'ips-filter': {'type': 'list', 'options': {'ips-filter-name': {'type': 'str'}}, 'elements': 'dict'},
                'ipv6_trusthost1': {'type': 'str'},
                'ipv6_trusthost10': {'type': 'str'},
                'ipv6_trusthost2': {'type': 'str'},
                'ipv6_trusthost3': {'type': 'str'},
                'ipv6_trusthost4': {'type': 'str'},
                'ipv6_trusthost5': {'type': 'str'},
                'ipv6_trusthost6': {'type': 'str'},
                'ipv6_trusthost7': {'type': 'str'},
                'ipv6_trusthost8': {'type': 'str'},
                'ipv6_trusthost9': {'type': 'str'},
                'last-name': {'type': 'str'},
                'ldap-server': {'type': 'str'},
                'meta-data': {
                    'type': 'list',
                    'options': {
                        'fieldlength': {'type': 'int'},
                        'fieldname': {'type': 'str'},
                        'fieldvalue': {'type': 'str'},
                        'importance': {'choices': ['optional', 'required'], 'type': 'str'},
                        'status': {'choices': ['disabled', 'enabled'], 'type': 'str'}
                    },
                    'elements': 'dict'
                },
                'mobile-number': {'type': 'str'},
                'pager-number': {'type': 'str'},
                'password': {'no_log': True, 'type': 'raw'},
                'password-expire': {'no_log': True, 'type': 'raw'},
                'phone-number': {'type': 'str'},
                'policy-package': {'type': 'list', 'options': {'policy-package-name': {'type': 'str'}}, 'elements': 'dict'},
                'profileid': {'type': 'str'},
                'radius_server': {'type': 'str'},
                'restrict-access': {'v_range': [['6.0.0', '6.2.3'], ['6.4.0', '6.4.0']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'restrict-dev-vdom': {
                    'v_range': [['6.0.0', '6.2.3'], ['6.4.0', '6.4.0']],
                    'type': 'list',
                    'options': {'dev-vdom': {'v_range': [['6.0.0', '6.2.3'], ['6.4.0', '6.4.0']], 'type': 'str'}},
                    'elements': 'dict'
                },
                'rpc-permit': {'choices': ['read-write', 'none', 'read', 'from-profile'], 'type': 'str'},
                'ssh-public-key1': {'no_log': True, 'type': 'raw'},
                'ssh-public-key2': {'no_log': True, 'type': 'raw'},
                'ssh-public-key3': {'no_log': True, 'type': 'raw'},
                'subject': {'type': 'str'},
                'tacacs-plus-server': {'type': 'str'},
                'trusthost1': {'type': 'str'},
                'trusthost10': {'type': 'str'},
                'trusthost2': {'type': 'str'},
                'trusthost3': {'type': 'str'},
                'trusthost4': {'type': 'str'},
                'trusthost5': {'type': 'str'},
                'trusthost6': {'type': 'str'},
                'trusthost7': {'type': 'str'},
                'trusthost8': {'type': 'str'},
                'trusthost9': {'type': 'str'},
                'two-factor-auth': {'choices': ['disable', 'enable', 'password', 'ftc-ftm', 'ftc-email', 'ftc-sms'], 'type': 'str'},
                'user_type': {'choices': ['local', 'radius', 'ldap', 'tacacs-plus', 'pki-auth', 'group', 'sso', 'api'], 'type': 'str'},
                'userid': {'required': True, 'type': 'str'},
                'web-filter': {'type': 'list', 'options': {'web-filter-name': {'type': 'str'}}, 'elements': 'dict'},
                'wildcard': {'choices': ['disable', 'enable'], 'type': 'str'},
                'login-max': {'v_range': [['6.4.6', '']], 'type': 'int'},
                'use-global-theme': {'v_range': [['7.0.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'user-theme': {
                    'v_range': [['7.0.0', '']],
                    'choices': [
                        'blue', 'green', 'red', 'melongene', 'spring', 'summer', 'autumn', 'winter', 'circuit-board', 'calla-lily', 'binary-tunnel',
                        'mars', 'blue-sea', 'technology', 'landscape', 'twilight', 'canyon', 'northern-light', 'astronomy', 'fish', 'penguin',
                        'mountain', 'panda', 'parrot', 'cave', 'zebra', 'contrast-dark', 'mariner', 'jade', 'neutrino', 'dark-matter', 'forest', 'cat',
                        'graphite'
                    ],
                    'type': 'str'
                },
                'adom-access': {'v_range': [['7.0.3', '']], 'choices': ['all', 'specify', 'exclude', 'per-adom-profile'], 'type': 'str'},
                'fingerprint': {'v_range': [['6.4.8', '6.4.14'], ['7.0.4', '']], 'type': 'str'},
                'th-from-profile': {'v_range': [['7.0.3', '']], 'type': 'int'},
                'th6-from-profile': {'v_range': [['7.0.3', '']], 'type': 'int'},
                'cors-allow-origin': {'v_range': [['7.2.2', '']], 'type': 'str'},
                'fortiai': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'policy-block': {
                    'v_range': [['7.6.0', '']],
                    'type': 'list',
                    'options': {'policy-block-name': {'v_range': [['7.6.0', '']], 'type': 'str'}},
                    'elements': 'dict'
                }
            }

        }
    }

    module_option_spec = get_module_arg_spec('full crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'system_admin_user'),
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
