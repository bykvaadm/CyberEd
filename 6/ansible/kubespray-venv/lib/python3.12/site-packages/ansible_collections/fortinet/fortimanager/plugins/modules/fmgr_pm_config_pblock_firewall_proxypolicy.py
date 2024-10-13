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
module: fmgr_pm_config_pblock_firewall_proxypolicy
short_description: Configure proxy policies.
description:
    - This module is able to configure a FortiManager device.
    - Examples include all parameters and values which need to be adjusted to data sources before usage.

version_added: "2.7.0"
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
    pblock:
        description: The parameter (pblock) in requested url.
        type: str
        required: true
    pm_config_pblock_firewall_proxypolicy:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            _policy_block:
                type: int
                description: Assigned policy block.
            access-proxy:
                type: list
                elements: str
                description: Deprecated, please rename it to access_proxy. IPv4 access proxy.
            access-proxy6:
                type: list
                elements: str
                description: Deprecated, please rename it to access_proxy6. IPv6 access proxy.
            action:
                type: str
                description: Accept or deny traffic matching the policy parameters.
                choices:
                    - 'accept'
                    - 'deny'
                    - 'redirect'
            application-list:
                type: list
                elements: str
                description: Deprecated, please rename it to application_list. Name of an existing Application list.
            av-profile:
                type: list
                elements: str
                description: Deprecated, please rename it to av_profile. Name of an existing Antivirus profile.
            block-notification:
                type: str
                description: Deprecated, please rename it to block_notification. Enable/disable block notification.
                choices:
                    - 'disable'
                    - 'enable'
            casb-profile:
                type: list
                elements: str
                description: Deprecated, please rename it to casb_profile. Name of an existing CASB profile.
            comments:
                type: str
                description: Optional comments.
            decrypted-traffic-mirror:
                type: list
                elements: str
                description: Deprecated, please rename it to decrypted_traffic_mirror. Decrypted traffic mirror.
            detect-https-in-http-request:
                type: str
                description: Deprecated, please rename it to detect_https_in_http_request. Enable/disable detection of HTTPS in HTTP request.
                choices:
                    - 'disable'
                    - 'enable'
            device-ownership:
                type: str
                description: Deprecated, please rename it to device_ownership. When enabled, the ownership enforcement will be done at policy level.
                choices:
                    - 'disable'
                    - 'enable'
            disclaimer:
                type: str
                description: Web proxy disclaimer setting
                choices:
                    - 'disable'
                    - 'domain'
                    - 'policy'
                    - 'user'
            dlp-profile:
                type: list
                elements: str
                description: Deprecated, please rename it to dlp_profile. Name of an existing DLP profile.
            dnsfilter-profile:
                type: list
                elements: str
                description: Deprecated, please rename it to dnsfilter_profile. Name of an existing DNS filter profile.
            dstaddr:
                type: list
                elements: str
                description: Destination address objects.
            dstaddr-negate:
                type: str
                description: Deprecated, please rename it to dstaddr_negate. When enabled, destination addresses match against any address EXCEPT the s...
                choices:
                    - 'disable'
                    - 'enable'
            dstaddr6:
                type: list
                elements: str
                description: IPv6 destination address objects.
            dstintf:
                type: list
                elements: str
                description: Destination interface names.
            emailfilter-profile:
                type: list
                elements: str
                description: Deprecated, please rename it to emailfilter_profile. Name of an existing email filter profile.
            file-filter-profile:
                type: list
                elements: str
                description: Deprecated, please rename it to file_filter_profile. Name of an existing file-filter profile.
            global-label:
                type: str
                description: Deprecated, please rename it to global_label. Global web-based manager visible label.
            groups:
                type: list
                elements: str
                description: Names of group objects.
            http-tunnel-auth:
                type: str
                description: Deprecated, please rename it to http_tunnel_auth. Enable/disable HTTP tunnel authentication.
                choices:
                    - 'disable'
                    - 'enable'
            icap-profile:
                type: list
                elements: str
                description: Deprecated, please rename it to icap_profile. Name of an existing ICAP profile.
            internet-service:
                type: str
                description: Deprecated, please rename it to internet_service. Enable/disable use of Internet Services for this policy.
                choices:
                    - 'disable'
                    - 'enable'
            internet-service-custom:
                type: list
                elements: str
                description: Deprecated, please rename it to internet_service_custom. Custom Internet Service name.
            internet-service-custom-group:
                type: list
                elements: str
                description: Deprecated, please rename it to internet_service_custom_group. Custom Internet Service group name.
            internet-service-group:
                type: list
                elements: str
                description: Deprecated, please rename it to internet_service_group. Internet Service group name.
            internet-service-name:
                type: list
                elements: str
                description: Deprecated, please rename it to internet_service_name. Internet Service name.
            internet-service-negate:
                type: str
                description: Deprecated, please rename it to internet_service_negate. When enabled, Internet Services match against any internet servic...
                choices:
                    - 'disable'
                    - 'enable'
            internet-service6:
                type: str
                description: Deprecated, please rename it to internet_service6. Enable/disable use of Internet Services IPv6 for this policy.
                choices:
                    - 'disable'
                    - 'enable'
            internet-service6-custom:
                type: list
                elements: str
                description: Deprecated, please rename it to internet_service6_custom. Custom Internet Service IPv6 name.
            internet-service6-custom-group:
                type: list
                elements: str
                description: Deprecated, please rename it to internet_service6_custom_group. Custom Internet Service IPv6 group name.
            internet-service6-group:
                type: list
                elements: str
                description: Deprecated, please rename it to internet_service6_group. Internet Service IPv6 group name.
            internet-service6-name:
                type: list
                elements: str
                description: Deprecated, please rename it to internet_service6_name. Internet Service IPv6 name.
            internet-service6-negate:
                type: str
                description: Deprecated, please rename it to internet_service6_negate. When enabled, Internet Services match against any internet servi...
                choices:
                    - 'disable'
                    - 'enable'
            ips-sensor:
                type: list
                elements: str
                description: Deprecated, please rename it to ips_sensor. Name of an existing IPS sensor.
            ips-voip-filter:
                type: list
                elements: str
                description: Deprecated, please rename it to ips_voip_filter. Name of an existing VoIP
            label:
                type: str
                description: VDOM-specific GUI visible label.
            log-http-transaction:
                type: str
                description: Deprecated, please rename it to log_http_transaction. Enable/disable HTTP transaction log.
                choices:
                    - 'disable'
                    - 'enable'
            logtraffic:
                type: str
                description: Enable/disable logging traffic through the policy.
                choices:
                    - 'disable'
                    - 'all'
                    - 'utm'
            logtraffic-start:
                type: str
                description: Deprecated, please rename it to logtraffic_start. Enable/disable policy log traffic start.
                choices:
                    - 'disable'
                    - 'enable'
            name:
                type: str
                description: Policy name.
            policyid:
                type: int
                description: Policy ID.
                required: true
            poolname:
                type: list
                elements: str
                description: Name of IP pool object.
            profile-group:
                type: list
                elements: str
                description: Deprecated, please rename it to profile_group. Name of profile group.
            profile-protocol-options:
                type: list
                elements: str
                description: Deprecated, please rename it to profile_protocol_options. Name of an existing Protocol options profile.
            profile-type:
                type: str
                description: Deprecated, please rename it to profile_type. Determine whether the firewall policy allows security profile groups or sing...
                choices:
                    - 'single'
                    - 'group'
            proxy:
                type: str
                description: Type of explicit proxy.
                choices:
                    - 'explicit-web'
                    - 'transparent-web'
                    - 'ftp'
                    - 'wanopt'
                    - 'ssh'
                    - 'ssh-tunnel'
                    - 'access-proxy'
                    - 'ztna-proxy'
            redirect-url:
                type: str
                description: Deprecated, please rename it to redirect_url. Redirect URL for further explicit web proxy processing.
            replacemsg-override-group:
                type: list
                elements: str
                description: Deprecated, please rename it to replacemsg_override_group. Authentication replacement message override group.
            schedule:
                type: list
                elements: str
                description: Name of schedule object.
            sctp-filter-profile:
                type: list
                elements: str
                description: Deprecated, please rename it to sctp_filter_profile. Name of an existing SCTP filter profile.
            service:
                type: list
                elements: str
                description: Name of service objects.
            service-negate:
                type: str
                description: Deprecated, please rename it to service_negate. When enabled, services match against any service EXCEPT the specified dest...
                choices:
                    - 'disable'
                    - 'enable'
            session-ttl:
                type: str
                description: Deprecated, please rename it to session_ttl. TTL in seconds for sessions accepted by this policy
            srcaddr:
                type: list
                elements: str
                description: Source address objects.
            srcaddr-negate:
                type: str
                description: Deprecated, please rename it to srcaddr_negate. When enabled, source addresses match against any address EXCEPT the specif...
                choices:
                    - 'disable'
                    - 'enable'
            srcaddr6:
                type: list
                elements: str
                description: IPv6 source address objects.
            srcintf:
                type: list
                elements: str
                description: Source interface names.
            ssh-filter-profile:
                type: list
                elements: str
                description: Deprecated, please rename it to ssh_filter_profile. Name of an existing SSH filter profile.
            ssh-policy-redirect:
                type: str
                description: Deprecated, please rename it to ssh_policy_redirect. Redirect SSH traffic to matching transparent proxy policy.
                choices:
                    - 'disable'
                    - 'enable'
            ssl-ssh-profile:
                type: list
                elements: str
                description: Deprecated, please rename it to ssl_ssh_profile. Name of an existing SSL SSH profile.
            status:
                type: str
                description: Enable/disable the active status of the policy.
                choices:
                    - 'disable'
                    - 'enable'
            transparent:
                type: str
                description: Enable to use the IP address of the client to connect to the server.
                choices:
                    - 'disable'
                    - 'enable'
            users:
                type: list
                elements: str
                description: Names of user objects.
            utm-status:
                type: str
                description: Deprecated, please rename it to utm_status. Enable the use of UTM profiles/sensors/lists.
                choices:
                    - 'disable'
                    - 'enable'
            uuid:
                type: str
                description: Universally Unique Identifier
            videofilter-profile:
                type: list
                elements: str
                description: Deprecated, please rename it to videofilter_profile. Name of an existing VideoFilter profile.
            waf-profile:
                type: list
                elements: str
                description: Deprecated, please rename it to waf_profile. Name of an existing Web application firewall profile.
            webcache:
                type: str
                description: Enable/disable web caching.
                choices:
                    - 'disable'
                    - 'enable'
            webcache-https:
                type: str
                description: Deprecated, please rename it to webcache_https. Enable/disable web caching for HTTPS
                choices:
                    - 'disable'
                    - 'enable'
            webfilter-profile:
                type: list
                elements: str
                description: Deprecated, please rename it to webfilter_profile. Name of an existing Web filter profile.
            webproxy-forward-server:
                type: list
                elements: str
                description: Deprecated, please rename it to webproxy_forward_server. Web proxy forward server name.
            webproxy-profile:
                type: list
                elements: str
                description: Deprecated, please rename it to webproxy_profile. Name of web proxy profile.
            ztna-ems-tag:
                type: list
                elements: str
                description: Deprecated, please rename it to ztna_ems_tag. ZTNA EMS Tag names.
            ztna-proxy:
                type: list
                elements: str
                description: Deprecated, please rename it to ztna_proxy. IPv4 ZTNA traffic forward proxy.
            ztna-tags-match-logic:
                type: str
                description: Deprecated, please rename it to ztna_tags_match_logic. ZTNA tag matching logic.
                choices:
                    - 'or'
                    - 'and'
            diameter-filter-profile:
                type: list
                elements: str
                description: Deprecated, please rename it to diameter_filter_profile. Name of an existing Diameter filter profile.
            virtual-patch-profile:
                type: list
                elements: str
                description: Deprecated, please rename it to virtual_patch_profile. Virtual patch profile.
            voip-profile:
                type: list
                elements: str
                description: Deprecated, please rename it to voip_profile. Name of an existing VoIP profile.
            dlp-sensor:
                type: list
                elements: str
                description: Deprecated, please rename it to dlp_sensor. Name of an existing DLP sensor.
            cifs-profile:
                type: list
                elements: str
                description: Deprecated, please rename it to cifs_profile. Name of an existing CIFS profile.
            internet-service-id:
                type: list
                elements: str
                description: Deprecated, please rename it to internet_service_id. Internet Service ID.
            mms-profile:
                type: list
                elements: str
                description: Deprecated, please rename it to mms_profile. Name of an existing MMS profile.
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
    - name: Configure proxy policies.
      fortinet.fortimanager.fmgr_pm_config_pblock_firewall_proxypolicy:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        adom: <your own value>
        pblock: <your own value>
        state: present # <value in [present, absent]>
        pm_config_pblock_firewall_proxypolicy:
          _policy_block: <integer>
          access_proxy: <list or string>
          access_proxy6: <list or string>
          action: <value in [accept, deny, redirect]>
          application_list: <list or string>
          av_profile: <list or string>
          block_notification: <value in [disable, enable]>
          casb_profile: <list or string>
          comments: <string>
          decrypted_traffic_mirror: <list or string>
          detect_https_in_http_request: <value in [disable, enable]>
          device_ownership: <value in [disable, enable]>
          disclaimer: <value in [disable, domain, policy, ...]>
          dlp_profile: <list or string>
          dnsfilter_profile: <list or string>
          dstaddr: <list or string>
          dstaddr_negate: <value in [disable, enable]>
          dstaddr6: <list or string>
          dstintf: <list or string>
          emailfilter_profile: <list or string>
          file_filter_profile: <list or string>
          global_label: <string>
          groups: <list or string>
          http_tunnel_auth: <value in [disable, enable]>
          icap_profile: <list or string>
          internet_service: <value in [disable, enable]>
          internet_service_custom: <list or string>
          internet_service_custom_group: <list or string>
          internet_service_group: <list or string>
          internet_service_name: <list or string>
          internet_service_negate: <value in [disable, enable]>
          internet_service6: <value in [disable, enable]>
          internet_service6_custom: <list or string>
          internet_service6_custom_group: <list or string>
          internet_service6_group: <list or string>
          internet_service6_name: <list or string>
          internet_service6_negate: <value in [disable, enable]>
          ips_sensor: <list or string>
          ips_voip_filter: <list or string>
          label: <string>
          log_http_transaction: <value in [disable, enable]>
          logtraffic: <value in [disable, all, utm]>
          logtraffic_start: <value in [disable, enable]>
          name: <string>
          policyid: <integer>
          poolname: <list or string>
          profile_group: <list or string>
          profile_protocol_options: <list or string>
          profile_type: <value in [single, group]>
          proxy: <value in [explicit-web, transparent-web, ftp, ...]>
          redirect_url: <string>
          replacemsg_override_group: <list or string>
          schedule: <list or string>
          sctp_filter_profile: <list or string>
          service: <list or string>
          service_negate: <value in [disable, enable]>
          session_ttl: <string>
          srcaddr: <list or string>
          srcaddr_negate: <value in [disable, enable]>
          srcaddr6: <list or string>
          srcintf: <list or string>
          ssh_filter_profile: <list or string>
          ssh_policy_redirect: <value in [disable, enable]>
          ssl_ssh_profile: <list or string>
          status: <value in [disable, enable]>
          transparent: <value in [disable, enable]>
          users: <list or string>
          utm_status: <value in [disable, enable]>
          uuid: <string>
          videofilter_profile: <list or string>
          waf_profile: <list or string>
          webcache: <value in [disable, enable]>
          webcache_https: <value in [disable, enable]>
          webfilter_profile: <list or string>
          webproxy_forward_server: <list or string>
          webproxy_profile: <list or string>
          ztna_ems_tag: <list or string>
          ztna_proxy: <list or string>
          ztna_tags_match_logic: <value in [or, and]>
          diameter_filter_profile: <list or string>
          virtual_patch_profile: <list or string>
          voip_profile: <list or string>
          dlp_sensor: <list or string>
          cifs_profile: <list or string>
          internet_service_id: <list or string>
          mms_profile: <list or string>
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
        '/pm/config/adom/{adom}/pblock/{pblock}/firewall/proxy-policy'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/pblock/{pblock}/firewall/proxy-policy/{proxy-policy}'
    ]

    url_params = ['adom', 'pblock']
    module_primary_key = 'policyid'
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'pblock': {'required': True, 'type': 'str'},
        'pm_config_pblock_firewall_proxypolicy': {
            'type': 'dict',
            'v_range': [['7.6.0', '']],
            'options': {
                '_policy_block': {'v_range': [['7.6.0', '']], 'type': 'int'},
                'access-proxy': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'access-proxy6': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'action': {'v_range': [['7.6.0', '']], 'choices': ['accept', 'deny', 'redirect'], 'type': 'str'},
                'application-list': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'av-profile': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'block-notification': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'casb-profile': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'comments': {'v_range': [['7.6.0', '']], 'type': 'str'},
                'decrypted-traffic-mirror': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'detect-https-in-http-request': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'device-ownership': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'disclaimer': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'domain', 'policy', 'user'], 'type': 'str'},
                'dlp-profile': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'dnsfilter-profile': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'dstaddr': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'dstaddr-negate': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'dstaddr6': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'dstintf': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'emailfilter-profile': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'file-filter-profile': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'global-label': {'v_range': [['7.6.0', '']], 'type': 'str'},
                'groups': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'http-tunnel-auth': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'icap-profile': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'internet-service': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'internet-service-custom': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'internet-service-custom-group': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'internet-service-group': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'internet-service-name': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'internet-service-negate': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'internet-service6': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'internet-service6-custom': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'internet-service6-custom-group': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'internet-service6-group': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'internet-service6-name': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'internet-service6-negate': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ips-sensor': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'ips-voip-filter': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'label': {'v_range': [['7.6.0', '']], 'type': 'str'},
                'log-http-transaction': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'logtraffic': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'all', 'utm'], 'type': 'str'},
                'logtraffic-start': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'name': {'v_range': [['7.6.0', '']], 'type': 'str'},
                'policyid': {'v_range': [['7.6.0', '']], 'required': True, 'type': 'int'},
                'poolname': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'profile-group': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'profile-protocol-options': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'profile-type': {'v_range': [['7.6.0', '']], 'choices': ['single', 'group'], 'type': 'str'},
                'proxy': {
                    'v_range': [['7.6.0', '']],
                    'choices': ['explicit-web', 'transparent-web', 'ftp', 'wanopt', 'ssh', 'ssh-tunnel', 'access-proxy', 'ztna-proxy'],
                    'type': 'str'
                },
                'redirect-url': {'v_range': [['7.6.0', '']], 'type': 'str'},
                'replacemsg-override-group': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'schedule': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'sctp-filter-profile': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'service': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'service-negate': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'session-ttl': {'v_range': [['7.6.0', '']], 'type': 'str'},
                'srcaddr': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'srcaddr-negate': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'srcaddr6': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'srcintf': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'ssh-filter-profile': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'ssh-policy-redirect': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ssl-ssh-profile': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'status': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'transparent': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'users': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'utm-status': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'uuid': {'v_range': [['7.6.0', '']], 'type': 'str'},
                'videofilter-profile': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'waf-profile': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'webcache': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'webcache-https': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'webfilter-profile': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'webproxy-forward-server': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'webproxy-profile': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'ztna-ems-tag': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'ztna-proxy': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'ztna-tags-match-logic': {'v_range': [['7.6.0', '']], 'choices': ['or', 'and'], 'type': 'str'},
                'diameter-filter-profile': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'virtual-patch-profile': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'voip-profile': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'dlp-sensor': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'cifs-profile': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'internet-service-id': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'},
                'mms-profile': {'v_range': [['7.6.0', '']], 'type': 'list', 'elements': 'str'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('full crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'pm_config_pblock_firewall_proxypolicy'),
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
