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
module: fmgr_system_log_settings
short_description: Log settings.
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
    system_log_settings:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            FAC-custom-field1:
                type: str
                description: Deprecated, please rename it to FAC_custom_field1. Name of custom log field to index.
            FAZ-custom-field1:
                type: str
                description: Deprecated, please rename it to FAZ_custom_field1. Name of custom log field to index.
            FCH-custom-field1:
                type: str
                description: Deprecated, please rename it to FCH_custom_field1. Name of custom log field to index.
            FCT-custom-field1:
                type: str
                description: Deprecated, please rename it to FCT_custom_field1. Name of custom log field to index.
            FDD-custom-field1:
                type: str
                description: Deprecated, please rename it to FDD_custom_field1. Name of custom log field to index.
            FGT-custom-field1:
                type: str
                description: Deprecated, please rename it to FGT_custom_field1. Name of custom log field to index.
            FMG-custom-field1:
                type: str
                description: Deprecated, please rename it to FMG_custom_field1. Name of custom log field to index.
            FML-custom-field1:
                type: str
                description: Deprecated, please rename it to FML_custom_field1. Name of custom log field to index.
            FPX-custom-field1:
                type: str
                description: Deprecated, please rename it to FPX_custom_field1. Name of custom log field to index.
            FSA-custom-field1:
                type: str
                description: Deprecated, please rename it to FSA_custom_field1. Name of custom log field to index.
            FWB-custom-field1:
                type: str
                description: Deprecated, please rename it to FWB_custom_field1. Name of custom log field to index.
            browse-max-logfiles:
                type: int
                description: Deprecated, please rename it to browse_max_logfiles. Maximum number of log files for each log browse attempt for each Adom.
            dns-resolve-dstip:
                type: str
                description:
                    - Deprecated, please rename it to dns_resolve_dstip.
                    - Enable/Disable resolving destination IP by DNS.
                    - disable - Disable resolving destination IP by DNS.
                    - enable - Enable resolving destination IP by DNS.
                choices:
                    - 'disable'
                    - 'enable'
            download-max-logs:
                type: int
                description: Deprecated, please rename it to download_max_logs. Maximum number of logs for each log download attempt.
            ha-auto-migrate:
                type: str
                description:
                    - Deprecated, please rename it to ha_auto_migrate.
                    - Enabled/Disable automatically merging HA members logs to HA cluster.
                    - disable - Disable automatically merging HA members logs to HA cluster.
                    - enable - Enable automatically merging HA members logs to HA cluster.
                choices:
                    - 'disable'
                    - 'enable'
            import-max-logfiles:
                type: int
                description: Deprecated, please rename it to import_max_logfiles. Maximum number of log files for each log import attempt.
            log-file-archive-name:
                type: str
                description:
                    - Deprecated, please rename it to log_file_archive_name.
                    - Log file name format for archiving, such as backup, upload or download.
                    - basic - Basic format for log archive file name, e.
                    - extended - Extended format for log archive file name, e.
                choices:
                    - 'basic'
                    - 'extended'
            rolling-analyzer:
                type: dict
                description: Deprecated, please rename it to rolling_analyzer. Rolling analyzer.
                suboptions:
                    days:
                        type: list
                        elements: str
                        description:
                            - Log files rolling schedule
                            - sun - Sunday.
                            - mon - Monday.
                            - tue - Tuesday.
                            - wed - Wednesday.
                            - thu - Thursday.
                            - fri - Friday.
                            - sat - Saturday.
                        choices:
                            - 'sun'
                            - 'mon'
                            - 'tue'
                            - 'wed'
                            - 'thu'
                            - 'fri'
                            - 'sat'
                    del-files:
                        type: str
                        description:
                            - Deprecated, please rename it to del_files.
                            - Enable/disable log file deletion after uploading.
                            - disable - Disable log file deletion.
                            - enable - Enable log file deletion.
                        choices:
                            - 'disable'
                            - 'enable'
                    directory:
                        type: str
                        description: Upload server directory, for Unix server, use absolute
                    file-size:
                        type: int
                        description: Deprecated, please rename it to file_size. Roll log files when they reach this size
                    gzip-format:
                        type: str
                        description:
                            - Deprecated, please rename it to gzip_format.
                            - Enable/disable compression of uploaded log files.
                            - disable - Disable compression.
                            - enable - Enable compression.
                        choices:
                            - 'disable'
                            - 'enable'
                    hour:
                        type: int
                        description: Log files rolling schedule
                    ip:
                        type: str
                        description: Upload server IP address.
                    ip2:
                        type: str
                        description: Upload server IP2 address.
                    ip3:
                        type: str
                        description: Upload server IP3 address.
                    log-format:
                        type: str
                        description:
                            - Deprecated, please rename it to log_format.
                            - Format of uploaded log files.
                            - native - Native format
                            - text - Text format
                            - csv - CSV
                        choices:
                            - 'native'
                            - 'text'
                            - 'csv'
                    min:
                        type: int
                        description: Log files rolling schedule
                    password:
                        type: raw
                        description: (list) Upload server login password.
                    password2:
                        type: raw
                        description: (list) Upload server login password2.
                    password3:
                        type: raw
                        description: (list) Upload server login password3.
                    server-type:
                        type: str
                        description:
                            - Deprecated, please rename it to server_type.
                            - Upload server type.
                            - ftp - Upload via FTP.
                            - sftp - Upload via SFTP.
                            - scp - Upload via SCP.
                        choices:
                            - 'ftp'
                            - 'sftp'
                            - 'scp'
                    upload:
                        type: str
                        description:
                            - Enable/disable log file uploads.
                            - disable - Disable log files uploading.
                            - enable - Enable log files uploading.
                        choices:
                            - 'disable'
                            - 'enable'
                    upload-hour:
                        type: int
                        description: Deprecated, please rename it to upload_hour. Log files upload schedule
                    upload-mode:
                        type: str
                        description:
                            - Deprecated, please rename it to upload_mode.
                            - Upload mode with multiple servers.
                            - backup - Servers are attempted and used one after the other upon failure to connect.
                            - mirror - All configured servers are attempted and used.
                        choices:
                            - 'backup'
                            - 'mirror'
                    upload-trigger:
                        type: str
                        description:
                            - Deprecated, please rename it to upload_trigger.
                            - Event triggering log files upload.
                            - on-roll - Upload log files after they are rolled.
                            - on-schedule - Upload log files daily.
                        choices:
                            - 'on-roll'
                            - 'on-schedule'
                    username:
                        type: str
                        description: Upload server login username.
                    username2:
                        type: str
                        description: Upload server login username2.
                    username3:
                        type: str
                        description: Upload server login username3.
                    when:
                        type: str
                        description:
                            - Roll log files periodically.
                            - none - Do not roll log files periodically.
                            - daily - Roll log files daily.
                            - weekly - Roll log files on certain days of week.
                        choices:
                            - 'none'
                            - 'daily'
                            - 'weekly'
                    port:
                        type: int
                        description: Upload server IP1 port number.
                    port2:
                        type: int
                        description: Upload server IP2 port number.
                    port3:
                        type: int
                        description: Upload server IP3 port number.
                    rolling-upgrade-status:
                        type: int
                        description: Deprecated, please rename it to rolling_upgrade_status. Rolling upgrade status
                    server:
                        type: str
                        description: Upload server FQDN/IP.
                    server2:
                        type: str
                        description: Upload server2 FQDN/IP.
                    server3:
                        type: str
                        description: Upload server3 FQDN/IP.
            rolling-local:
                type: dict
                description: Deprecated, please rename it to rolling_local. Rolling local.
                suboptions:
                    days:
                        type: list
                        elements: str
                        description:
                            - Log files rolling schedule
                            - sun - Sunday.
                            - mon - Monday.
                            - tue - Tuesday.
                            - wed - Wednesday.
                            - thu - Thursday.
                            - fri - Friday.
                            - sat - Saturday.
                        choices:
                            - 'sun'
                            - 'mon'
                            - 'tue'
                            - 'wed'
                            - 'thu'
                            - 'fri'
                            - 'sat'
                    del-files:
                        type: str
                        description:
                            - Deprecated, please rename it to del_files.
                            - Enable/disable log file deletion after uploading.
                            - disable - Disable log file deletion.
                            - enable - Enable log file deletion.
                        choices:
                            - 'disable'
                            - 'enable'
                    directory:
                        type: str
                        description: Upload server directory, for Unix server, use absolute
                    file-size:
                        type: int
                        description: Deprecated, please rename it to file_size. Roll log files when they reach this size
                    gzip-format:
                        type: str
                        description:
                            - Deprecated, please rename it to gzip_format.
                            - Enable/disable compression of uploaded log files.
                            - disable - Disable compression.
                            - enable - Enable compression.
                        choices:
                            - 'disable'
                            - 'enable'
                    hour:
                        type: int
                        description: Log files rolling schedule
                    ip:
                        type: str
                        description: Upload server IP address.
                    ip2:
                        type: str
                        description: Upload server IP2 address.
                    ip3:
                        type: str
                        description: Upload server IP3 address.
                    log-format:
                        type: str
                        description:
                            - Deprecated, please rename it to log_format.
                            - Format of uploaded log files.
                            - native - Native format
                            - text - Text format
                            - csv - CSV
                        choices:
                            - 'native'
                            - 'text'
                            - 'csv'
                    min:
                        type: int
                        description: Log files rolling schedule
                    password:
                        type: raw
                        description: (list) Upload server login password.
                    password2:
                        type: raw
                        description: (list) Upload server login password2.
                    password3:
                        type: raw
                        description: (list) Upload server login password3.
                    server-type:
                        type: str
                        description:
                            - Deprecated, please rename it to server_type.
                            - Upload server type.
                            - ftp - Upload via FTP.
                            - sftp - Upload via SFTP.
                            - scp - Upload via SCP.
                        choices:
                            - 'ftp'
                            - 'sftp'
                            - 'scp'
                    upload:
                        type: str
                        description:
                            - Enable/disable log file uploads.
                            - disable - Disable log files uploading.
                            - enable - Enable log files uploading.
                        choices:
                            - 'disable'
                            - 'enable'
                    upload-hour:
                        type: int
                        description: Deprecated, please rename it to upload_hour. Log files upload schedule
                    upload-mode:
                        type: str
                        description:
                            - Deprecated, please rename it to upload_mode.
                            - Upload mode with multiple servers.
                            - backup - Servers are attempted and used one after the other upon failure to connect.
                            - mirror - All configured servers are attempted and used.
                        choices:
                            - 'backup'
                            - 'mirror'
                    upload-trigger:
                        type: str
                        description:
                            - Deprecated, please rename it to upload_trigger.
                            - Event triggering log files upload.
                            - on-roll - Upload log files after they are rolled.
                            - on-schedule - Upload log files daily.
                        choices:
                            - 'on-roll'
                            - 'on-schedule'
                    username:
                        type: str
                        description: Upload server login username.
                    username2:
                        type: str
                        description: Upload server login username2.
                    username3:
                        type: str
                        description: Upload server login username3.
                    when:
                        type: str
                        description:
                            - Roll log files periodically.
                            - none - Do not roll log files periodically.
                            - daily - Roll log files daily.
                            - weekly - Roll log files on certain days of week.
                        choices:
                            - 'none'
                            - 'daily'
                            - 'weekly'
                    port:
                        type: int
                        description: Upload server IP1 port number.
                    port2:
                        type: int
                        description: Upload server IP2 port number.
                    port3:
                        type: int
                        description: Upload server IP3 port number.
                    rolling-upgrade-status:
                        type: int
                        description: Deprecated, please rename it to rolling_upgrade_status. Rolling upgrade status
                    server:
                        type: str
                        description: Upload server FQDN/IP.
                    server2:
                        type: str
                        description: Upload server2 FQDN/IP.
                    server3:
                        type: str
                        description: Upload server3 FQDN/IP.
            rolling-regular:
                type: dict
                description: Deprecated, please rename it to rolling_regular. Rolling regular.
                suboptions:
                    days:
                        type: list
                        elements: str
                        description:
                            - Log files rolling schedule
                            - sun - Sunday.
                            - mon - Monday.
                            - tue - Tuesday.
                            - wed - Wednesday.
                            - thu - Thursday.
                            - fri - Friday.
                            - sat - Saturday.
                        choices:
                            - 'sun'
                            - 'mon'
                            - 'tue'
                            - 'wed'
                            - 'thu'
                            - 'fri'
                            - 'sat'
                    del-files:
                        type: str
                        description:
                            - Deprecated, please rename it to del_files.
                            - Enable/disable log file deletion after uploading.
                            - disable - Disable log file deletion.
                            - enable - Enable log file deletion.
                        choices:
                            - 'disable'
                            - 'enable'
                    directory:
                        type: str
                        description: Upload server directory, for Unix server, use absolute
                    file-size:
                        type: int
                        description: Deprecated, please rename it to file_size. Roll log files when they reach this size
                    gzip-format:
                        type: str
                        description:
                            - Deprecated, please rename it to gzip_format.
                            - Enable/disable compression of uploaded log files.
                            - disable - Disable compression.
                            - enable - Enable compression.
                        choices:
                            - 'disable'
                            - 'enable'
                    hour:
                        type: int
                        description: Log files rolling schedule
                    ip:
                        type: str
                        description: Upload server IP address.
                    ip2:
                        type: str
                        description: Upload server IP2 address.
                    ip3:
                        type: str
                        description: Upload server IP3 address.
                    log-format:
                        type: str
                        description:
                            - Deprecated, please rename it to log_format.
                            - Format of uploaded log files.
                            - native - Native format
                            - text - Text format
                            - csv - CSV
                        choices:
                            - 'native'
                            - 'text'
                            - 'csv'
                    min:
                        type: int
                        description: Log files rolling schedule
                    password:
                        type: raw
                        description: (list) Upload server login password.
                    password2:
                        type: raw
                        description: (list) Upload server login password2.
                    password3:
                        type: raw
                        description: (list) Upload server login password3.
                    server-type:
                        type: str
                        description:
                            - Deprecated, please rename it to server_type.
                            - Upload server type.
                            - ftp - Upload via FTP.
                            - sftp - Upload via SFTP.
                            - scp - Upload via SCP.
                        choices:
                            - 'ftp'
                            - 'sftp'
                            - 'scp'
                    upload:
                        type: str
                        description:
                            - Enable/disable log file uploads.
                            - disable - Disable log files uploading.
                            - enable - Enable log files uploading.
                        choices:
                            - 'disable'
                            - 'enable'
                    upload-hour:
                        type: int
                        description: Deprecated, please rename it to upload_hour. Log files upload schedule
                    upload-mode:
                        type: str
                        description:
                            - Deprecated, please rename it to upload_mode.
                            - Upload mode with multiple servers.
                            - backup - Servers are attempted and used one after the other upon failure to connect.
                            - mirror - All configured servers are attempted and used.
                        choices:
                            - 'backup'
                            - 'mirror'
                    upload-trigger:
                        type: str
                        description:
                            - Deprecated, please rename it to upload_trigger.
                            - Event triggering log files upload.
                            - on-roll - Upload log files after they are rolled.
                            - on-schedule - Upload log files daily.
                        choices:
                            - 'on-roll'
                            - 'on-schedule'
                    username:
                        type: str
                        description: Upload server login username.
                    username2:
                        type: str
                        description: Upload server login username2.
                    username3:
                        type: str
                        description: Upload server login username3.
                    when:
                        type: str
                        description:
                            - Roll log files periodically.
                            - none - Do not roll log files periodically.
                            - daily - Roll log files daily.
                            - weekly - Roll log files on certain days of week.
                        choices:
                            - 'none'
                            - 'daily'
                            - 'weekly'
                    port:
                        type: int
                        description: Upload server IP1 port number.
                    port2:
                        type: int
                        description: Upload server IP2 port number.
                    port3:
                        type: int
                        description: Upload server IP3 port number.
                    rolling-upgrade-status:
                        type: int
                        description: Deprecated, please rename it to rolling_upgrade_status. Rolling upgrade status
                    server:
                        type: str
                        description: Upload server FQDN/IP.
                    server2:
                        type: str
                        description: Upload server2 FQDN/IP.
                    server3:
                        type: str
                        description: Upload server3 FQDN/IP.
            sync-search-timeout:
                type: int
                description: Deprecated, please rename it to sync_search_timeout. Maximum number of seconds for running a log search session in synchro...
            keep-dev-logs:
                type: str
                description:
                    - Deprecated, please rename it to keep_dev_logs.
                    - Enable/Disable keeping the dev logs after the device has been deleted.
                    - disable - Disable keeping the dev logs after the device has been deleted.
                    - enable - Enable keeping the dev logs after the device has been deleted.
                choices:
                    - 'disable'
                    - 'enable'
            device-auto-detect:
                type: str
                description:
                    - Deprecated, please rename it to device_auto_detect.
                    - Enable/Disable looking up device ID in syslog received with no encryption.
                    - disable - Disable looking up device ID in syslog received with no encryption.
                    - enable - Enable looking up device ID in syslog received with no encryption.
                choices:
                    - 'disable'
                    - 'enable'
            unencrypted-logging:
                type: str
                description:
                    - Deprecated, please rename it to unencrypted_logging.
                    - Enable/Disable receiving syslog through UDP
                    - disable - Disable receiving syslog through UDP
                    - enable - Enable receiving syslog through UDP
                choices:
                    - 'disable'
                    - 'enable'
            log-interval-dev-no-logging:
                type: int
                description: Deprecated, please rename it to log_interval_dev_no_logging. Interval in minute of no log received from a device when cons...
            log-upload-interval-dev-no-logging:
                type: int
                description: Deprecated, please rename it to log_upload_interval_dev_no_logging. Interval in minute of no log uploaded from a device wh...
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
    - name: Log settings.
      fortinet.fortimanager.fmgr_system_log_settings:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        system_log_settings:
          FAC_custom_field1: <string>
          FAZ_custom_field1: <string>
          FCH_custom_field1: <string>
          FCT_custom_field1: <string>
          FDD_custom_field1: <string>
          FGT_custom_field1: <string>
          FMG_custom_field1: <string>
          FML_custom_field1: <string>
          FPX_custom_field1: <string>
          FSA_custom_field1: <string>
          FWB_custom_field1: <string>
          browse_max_logfiles: <integer>
          dns_resolve_dstip: <value in [disable, enable]>
          download_max_logs: <integer>
          ha_auto_migrate: <value in [disable, enable]>
          import_max_logfiles: <integer>
          log_file_archive_name: <value in [basic, extended]>
          rolling_analyzer:
            days:
              - sun
              - mon
              - tue
              - wed
              - thu
              - fri
              - sat
            del_files: <value in [disable, enable]>
            directory: <string>
            file_size: <integer>
            gzip_format: <value in [disable, enable]>
            hour: <integer>
            ip: <string>
            ip2: <string>
            ip3: <string>
            log_format: <value in [native, text, csv]>
            min: <integer>
            password: <list or string>
            password2: <list or string>
            password3: <list or string>
            server_type: <value in [ftp, sftp, scp]>
            upload: <value in [disable, enable]>
            upload_hour: <integer>
            upload_mode: <value in [backup, mirror]>
            upload_trigger: <value in [on-roll, on-schedule]>
            username: <string>
            username2: <string>
            username3: <string>
            when: <value in [none, daily, weekly]>
            port: <integer>
            port2: <integer>
            port3: <integer>
            rolling_upgrade_status: <integer>
            server: <string>
            server2: <string>
            server3: <string>
          rolling_local:
            days:
              - sun
              - mon
              - tue
              - wed
              - thu
              - fri
              - sat
            del_files: <value in [disable, enable]>
            directory: <string>
            file_size: <integer>
            gzip_format: <value in [disable, enable]>
            hour: <integer>
            ip: <string>
            ip2: <string>
            ip3: <string>
            log_format: <value in [native, text, csv]>
            min: <integer>
            password: <list or string>
            password2: <list or string>
            password3: <list or string>
            server_type: <value in [ftp, sftp, scp]>
            upload: <value in [disable, enable]>
            upload_hour: <integer>
            upload_mode: <value in [backup, mirror]>
            upload_trigger: <value in [on-roll, on-schedule]>
            username: <string>
            username2: <string>
            username3: <string>
            when: <value in [none, daily, weekly]>
            port: <integer>
            port2: <integer>
            port3: <integer>
            rolling_upgrade_status: <integer>
            server: <string>
            server2: <string>
            server3: <string>
          rolling_regular:
            days:
              - sun
              - mon
              - tue
              - wed
              - thu
              - fri
              - sat
            del_files: <value in [disable, enable]>
            directory: <string>
            file_size: <integer>
            gzip_format: <value in [disable, enable]>
            hour: <integer>
            ip: <string>
            ip2: <string>
            ip3: <string>
            log_format: <value in [native, text, csv]>
            min: <integer>
            password: <list or string>
            password2: <list or string>
            password3: <list or string>
            server_type: <value in [ftp, sftp, scp]>
            upload: <value in [disable, enable]>
            upload_hour: <integer>
            upload_mode: <value in [backup, mirror]>
            upload_trigger: <value in [on-roll, on-schedule]>
            username: <string>
            username2: <string>
            username3: <string>
            when: <value in [none, daily, weekly]>
            port: <integer>
            port2: <integer>
            port3: <integer>
            rolling_upgrade_status: <integer>
            server: <string>
            server2: <string>
            server3: <string>
          sync_search_timeout: <integer>
          keep_dev_logs: <value in [disable, enable]>
          device_auto_detect: <value in [disable, enable]>
          unencrypted_logging: <value in [disable, enable]>
          log_interval_dev_no_logging: <integer>
          log_upload_interval_dev_no_logging: <integer>
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
        '/cli/global/system/log/settings'
    ]

    perobject_jrpc_urls = [
        '/cli/global/system/log/settings/{settings}'
    ]

    url_params = []
    module_primary_key = None
    module_arg_spec = {
        'system_log_settings': {
            'type': 'dict',
            'v_range': [['6.0.0', '']],
            'options': {
                'FAC-custom-field1': {'type': 'str'},
                'FAZ-custom-field1': {'v_range': [['6.0.0', '7.2.0']], 'type': 'str'},
                'FCH-custom-field1': {'type': 'str'},
                'FCT-custom-field1': {'type': 'str'},
                'FDD-custom-field1': {'type': 'str'},
                'FGT-custom-field1': {'type': 'str'},
                'FMG-custom-field1': {'v_range': [['6.0.0', '7.2.0']], 'type': 'str'},
                'FML-custom-field1': {'type': 'str'},
                'FPX-custom-field1': {'type': 'str'},
                'FSA-custom-field1': {'type': 'str'},
                'FWB-custom-field1': {'type': 'str'},
                'browse-max-logfiles': {'type': 'int'},
                'dns-resolve-dstip': {'choices': ['disable', 'enable'], 'type': 'str'},
                'download-max-logs': {'type': 'int'},
                'ha-auto-migrate': {'choices': ['disable', 'enable'], 'type': 'str'},
                'import-max-logfiles': {'type': 'int'},
                'log-file-archive-name': {'choices': ['basic', 'extended'], 'type': 'str'},
                'rolling-analyzer': {
                    'type': 'dict',
                    'options': {
                        'days': {'type': 'list', 'choices': ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'], 'elements': 'str'},
                        'del-files': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'directory': {'type': 'str'},
                        'file-size': {'type': 'int'},
                        'gzip-format': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'hour': {'type': 'int'},
                        'ip': {'v_range': [['6.0.0', '7.0.12']], 'type': 'str'},
                        'ip2': {'v_range': [['6.0.0', '7.0.12']], 'type': 'str'},
                        'ip3': {'v_range': [['6.0.0', '7.0.12']], 'type': 'str'},
                        'log-format': {'choices': ['native', 'text', 'csv'], 'type': 'str'},
                        'min': {'type': 'int'},
                        'password': {'no_log': True, 'type': 'raw'},
                        'password2': {'no_log': True, 'type': 'raw'},
                        'password3': {'no_log': True, 'type': 'raw'},
                        'server-type': {'choices': ['ftp', 'sftp', 'scp'], 'type': 'str'},
                        'upload': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'upload-hour': {'type': 'int'},
                        'upload-mode': {'choices': ['backup', 'mirror'], 'type': 'str'},
                        'upload-trigger': {'choices': ['on-roll', 'on-schedule'], 'type': 'str'},
                        'username': {'type': 'str'},
                        'username2': {'type': 'str'},
                        'username3': {'type': 'str'},
                        'when': {'choices': ['none', 'daily', 'weekly'], 'type': 'str'},
                        'port': {'v_range': [['6.2.2', '']], 'type': 'int'},
                        'port2': {'v_range': [['6.2.2', '']], 'type': 'int'},
                        'port3': {'v_range': [['6.2.2', '']], 'type': 'int'},
                        'rolling-upgrade-status': {'v_range': [['7.0.3', '']], 'type': 'int'},
                        'server': {'v_range': [['7.2.0', '']], 'type': 'str'},
                        'server2': {'v_range': [['7.2.0', '']], 'type': 'str'},
                        'server3': {'v_range': [['7.2.0', '']], 'type': 'str'}
                    }
                },
                'rolling-local': {
                    'type': 'dict',
                    'options': {
                        'days': {'type': 'list', 'choices': ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'], 'elements': 'str'},
                        'del-files': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'directory': {'type': 'str'},
                        'file-size': {'type': 'int'},
                        'gzip-format': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'hour': {'type': 'int'},
                        'ip': {'v_range': [['6.0.0', '7.0.12']], 'type': 'str'},
                        'ip2': {'v_range': [['6.0.0', '7.0.12']], 'type': 'str'},
                        'ip3': {'v_range': [['6.0.0', '7.0.12']], 'type': 'str'},
                        'log-format': {'choices': ['native', 'text', 'csv'], 'type': 'str'},
                        'min': {'type': 'int'},
                        'password': {'no_log': True, 'type': 'raw'},
                        'password2': {'no_log': True, 'type': 'raw'},
                        'password3': {'no_log': True, 'type': 'raw'},
                        'server-type': {'choices': ['ftp', 'sftp', 'scp'], 'type': 'str'},
                        'upload': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'upload-hour': {'type': 'int'},
                        'upload-mode': {'choices': ['backup', 'mirror'], 'type': 'str'},
                        'upload-trigger': {'choices': ['on-roll', 'on-schedule'], 'type': 'str'},
                        'username': {'type': 'str'},
                        'username2': {'type': 'str'},
                        'username3': {'type': 'str'},
                        'when': {'choices': ['none', 'daily', 'weekly'], 'type': 'str'},
                        'port': {'v_range': [['6.2.2', '']], 'type': 'int'},
                        'port2': {'v_range': [['6.2.2', '']], 'type': 'int'},
                        'port3': {'v_range': [['6.2.2', '']], 'type': 'int'},
                        'rolling-upgrade-status': {'v_range': [['7.0.3', '']], 'type': 'int'},
                        'server': {'v_range': [['7.2.0', '']], 'type': 'str'},
                        'server2': {'v_range': [['7.2.0', '']], 'type': 'str'},
                        'server3': {'v_range': [['7.2.0', '']], 'type': 'str'}
                    }
                },
                'rolling-regular': {
                    'type': 'dict',
                    'options': {
                        'days': {'type': 'list', 'choices': ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'], 'elements': 'str'},
                        'del-files': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'directory': {'type': 'str'},
                        'file-size': {'type': 'int'},
                        'gzip-format': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'hour': {'type': 'int'},
                        'ip': {'v_range': [['6.0.0', '7.0.12']], 'type': 'str'},
                        'ip2': {'v_range': [['6.0.0', '7.0.12']], 'type': 'str'},
                        'ip3': {'v_range': [['6.0.0', '7.0.12']], 'type': 'str'},
                        'log-format': {'choices': ['native', 'text', 'csv'], 'type': 'str'},
                        'min': {'type': 'int'},
                        'password': {'no_log': True, 'type': 'raw'},
                        'password2': {'no_log': True, 'type': 'raw'},
                        'password3': {'no_log': True, 'type': 'raw'},
                        'server-type': {'choices': ['ftp', 'sftp', 'scp'], 'type': 'str'},
                        'upload': {'choices': ['disable', 'enable'], 'type': 'str'},
                        'upload-hour': {'type': 'int'},
                        'upload-mode': {'choices': ['backup', 'mirror'], 'type': 'str'},
                        'upload-trigger': {'choices': ['on-roll', 'on-schedule'], 'type': 'str'},
                        'username': {'type': 'str'},
                        'username2': {'type': 'str'},
                        'username3': {'type': 'str'},
                        'when': {'choices': ['none', 'daily', 'weekly'], 'type': 'str'},
                        'port': {'v_range': [['6.2.2', '']], 'type': 'int'},
                        'port2': {'v_range': [['6.2.2', '']], 'type': 'int'},
                        'port3': {'v_range': [['6.2.2', '']], 'type': 'int'},
                        'rolling-upgrade-status': {'v_range': [['7.0.3', '']], 'type': 'int'},
                        'server': {'v_range': [['7.2.0', '']], 'type': 'str'},
                        'server2': {'v_range': [['7.2.0', '']], 'type': 'str'},
                        'server3': {'v_range': [['7.2.0', '']], 'type': 'str'}
                    }
                },
                'sync-search-timeout': {'type': 'int'},
                'keep-dev-logs': {'v_range': [['6.4.7', '6.4.14'], ['7.0.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'device-auto-detect': {
                    'v_range': [['7.0.10', '7.0.12'], ['7.2.4', '7.2.5'], ['7.4.1', '']],
                    'choices': ['disable', 'enable'],
                    'type': 'str'
                },
                'unencrypted-logging': {
                    'v_range': [['7.0.10', '7.0.12'], ['7.2.4', '7.2.5'], ['7.4.1', '']],
                    'choices': ['disable', 'enable'],
                    'type': 'str'
                },
                'log-interval-dev-no-logging': {'v_range': [['7.2.5', '7.2.5'], ['7.4.2', '']], 'type': 'int'},
                'log-upload-interval-dev-no-logging': {'v_range': [['7.2.5', '7.2.5'], ['7.4.2', '']], 'type': 'int'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('partial crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'system_log_settings'),
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
