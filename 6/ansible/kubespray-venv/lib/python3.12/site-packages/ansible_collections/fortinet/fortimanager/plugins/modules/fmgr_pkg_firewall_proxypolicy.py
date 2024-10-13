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
module: fmgr_pkg_firewall_proxypolicy
short_description: Configure proxy policies.
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
    pkg:
        description: The parameter (pkg) in requested url.
        type: str
        required: true
    pkg_firewall_proxypolicy:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            action:
                type: str
                description: Accept or deny traffic matching the policy parameters.
                choices:
                    - 'accept'
                    - 'deny'
                    - 'redirect'
            application-list:
                type: str
                description: Deprecated, please rename it to application_list. Name of an existing Application list.
            av-profile:
                type: str
                description: Deprecated, please rename it to av_profile. Name of an existing Antivirus profile.
            comments:
                type: str
                description: Optional comments.
            disclaimer:
                type: str
                description: Web proxy disclaimer setting
                choices:
                    - 'disable'
                    - 'domain'
                    - 'policy'
                    - 'user'
            dlp-sensor:
                type: str
                description: Deprecated, please rename it to dlp_sensor. Name of an existing DLP sensor.
            dstaddr:
                type: raw
                description: (list or str) Destination address objects.
            dstaddr-negate:
                type: str
                description: Deprecated, please rename it to dstaddr_negate. When enabled, destination addresses match against any address EXCEPT the s...
                choices:
                    - 'disable'
                    - 'enable'
            dstaddr6:
                type: raw
                description: (list or str) IPv6 destination address objects.
            dstintf:
                type: raw
                description: (list or str) Destination interface names.
            global-label:
                type: str
                description: Deprecated, please rename it to global_label. Global web-based manager visible label.
            groups:
                type: raw
                description: (list or str) Names of group objects.
            http-tunnel-auth:
                type: str
                description: Deprecated, please rename it to http_tunnel_auth. Enable/disable HTTP tunnel authentication.
                choices:
                    - 'disable'
                    - 'enable'
            icap-profile:
                type: str
                description: Deprecated, please rename it to icap_profile. Name of an existing ICAP profile.
            internet-service:
                type: str
                description: Deprecated, please rename it to internet_service. Enable/disable use of Internet Services for this policy.
                choices:
                    - 'disable'
                    - 'enable'
            internet-service-custom:
                type: raw
                description: (list or str) Deprecated, please rename it to internet_service_custom. Custom Internet Service name.
            internet-service-id:
                type: raw
                description: (list or str) Deprecated, please rename it to internet_service_id. Internet Service ID.
            internet-service-negate:
                type: str
                description: Deprecated, please rename it to internet_service_negate. When enabled, Internet Services match against any internet servic...
                choices:
                    - 'disable'
                    - 'enable'
            ips-sensor:
                type: str
                description: Deprecated, please rename it to ips_sensor. Name of an existing IPS sensor.
            label:
                type: str
                description: VDOM-specific GUI visible label.
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
            mms-profile:
                type: str
                description: Deprecated, please rename it to mms_profile. Name of an existing MMS profile.
            policyid:
                type: int
                description: Policy ID.
                required: true
            poolname:
                type: raw
                description: (list or str) Name of IP pool object.
            profile-group:
                type: str
                description: Deprecated, please rename it to profile_group. Name of profile group.
            profile-protocol-options:
                type: str
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
                type: str
                description: Deprecated, please rename it to replacemsg_override_group. Authentication replacement message override group.
            scan-botnet-connections:
                type: str
                description: Deprecated, please rename it to scan_botnet_connections. Enable/disable scanning of connections to Botnet servers.
                choices:
                    - 'disable'
                    - 'block'
                    - 'monitor'
            schedule:
                type: str
                description: Name of schedule object.
            service:
                type: raw
                description: (list or str) Name of service objects.
            service-negate:
                type: str
                description: Deprecated, please rename it to service_negate. When enabled, services match against any service EXCEPT the specified dest...
                choices:
                    - 'disable'
                    - 'enable'
            spamfilter-profile:
                type: str
                description: Deprecated, please rename it to spamfilter_profile. Name of an existing Spam filter profile.
            srcaddr:
                type: raw
                description: (list or str) Source address objects
            srcaddr-negate:
                type: str
                description: Deprecated, please rename it to srcaddr_negate. When enabled, source addresses match against any address EXCEPT the specif...
                choices:
                    - 'disable'
                    - 'enable'
            srcaddr6:
                type: raw
                description: (list or str) IPv6 source address objects.
            srcintf:
                type: raw
                description: (list or str) Source interface names.
            ssl-ssh-profile:
                type: str
                description: Deprecated, please rename it to ssl_ssh_profile. Name of an existing SSL SSH profile.
            status:
                type: str
                description: Enable/disable the active status of the policy.
                choices:
                    - 'disable'
                    - 'enable'
            tags:
                type: str
                description: Names of object-tags applied to address.
            transparent:
                type: str
                description: Enable to use the IP address of the client to connect to the server.
                choices:
                    - 'disable'
                    - 'enable'
            users:
                type: raw
                description: (list or str) Names of user objects.
            utm-status:
                type: str
                description: Deprecated, please rename it to utm_status. Enable the use of UTM profiles/sensors/lists.
                choices:
                    - 'disable'
                    - 'enable'
            uuid:
                type: str
                description: Universally Unique Identifier
            waf-profile:
                type: str
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
                type: str
                description: Deprecated, please rename it to webfilter_profile. Name of an existing Web filter profile.
            webproxy-forward-server:
                type: str
                description: Deprecated, please rename it to webproxy_forward_server. Name of web proxy forward server.
            webproxy-profile:
                type: str
                description: Deprecated, please rename it to webproxy_profile. Name of web proxy profile.
            cifs-profile:
                type: str
                description: Deprecated, please rename it to cifs_profile. Name of an existing CIFS profile.
            emailfilter-profile:
                type: str
                description: Deprecated, please rename it to emailfilter_profile. Name of an existing email filter profile.
            internet-service-custom-group:
                type: raw
                description: (list or str) Deprecated, please rename it to internet_service_custom_group. Custom Internet Service group name.
            internet-service-group:
                type: raw
                description: (list or str) Deprecated, please rename it to internet_service_group. Internet Service group name.
            session-ttl:
                type: raw
                description: (int or str) Deprecated, please rename it to session_ttl. TTL in seconds for sessions accepted by this policy
            ssh-filter-profile:
                type: str
                description: Deprecated, please rename it to ssh_filter_profile. Name of an existing SSH filter profile.
            ssh-policy-redirect:
                type: str
                description: Deprecated, please rename it to ssh_policy_redirect. Redirect SSH traffic to matching transparent proxy policy.
                choices:
                    - 'disable'
                    - 'enable'
            decrypted-traffic-mirror:
                type: str
                description: Deprecated, please rename it to decrypted_traffic_mirror. Decrypted traffic mirror.
            internet-service-name:
                type: raw
                description: (list or str) Deprecated, please rename it to internet_service_name. Internet Service name.
            file-filter-profile:
                type: str
                description: Deprecated, please rename it to file_filter_profile. Name of an existing file-filter profile.
            name:
                type: str
                description: Policy name.
            access-proxy:
                type: raw
                description: (list or str) Deprecated, please rename it to access_proxy. Access Proxy.
            device-ownership:
                type: str
                description: Deprecated, please rename it to device_ownership. When enabled, the ownership enforcement will be done at policy level.
                choices:
                    - 'disable'
                    - 'enable'
            videofilter-profile:
                type: str
                description: Deprecated, please rename it to videofilter_profile. Name of an existing VideoFilter profile.
            voip-profile:
                type: str
                description: Deprecated, please rename it to voip_profile. Name of an existing VoIP profile.
            ztna-ems-tag:
                type: raw
                description: (list or str) Deprecated, please rename it to ztna_ems_tag. ZTNA EMS Tag names.
            access-proxy6:
                type: raw
                description: (list or str) Deprecated, please rename it to access_proxy6. IPv6 access proxy.
            block-notification:
                type: str
                description: Deprecated, please rename it to block_notification. Enable/disable block notification.
                choices:
                    - 'disable'
                    - 'enable'
            dlp-profile:
                type: str
                description: Deprecated, please rename it to dlp_profile. Name of an existing DLP profile.
            sctp-filter-profile:
                type: str
                description: Deprecated, please rename it to sctp_filter_profile. Name of an existing SCTP filter profile.
            ztna-tags-match-logic:
                type: str
                description: Deprecated, please rename it to ztna_tags_match_logic. ZTNA tag matching logic.
                choices:
                    - 'or'
                    - 'and'
            casb-profile:
                type: str
                description: Deprecated, please rename it to casb_profile. Name of an existing CASB profile.
            detect-https-in-http-request:
                type: str
                description: Deprecated, please rename it to detect_https_in_http_request. Enable/disable detection of HTTPS in HTTP request.
                choices:
                    - 'disable'
                    - 'enable'
            diameter-filter-profile:
                type: str
                description: Deprecated, please rename it to diameter_filter_profile. Name of an existing Diameter filter profile.
            internet-service6:
                type: str
                description: Deprecated, please rename it to internet_service6. Enable/disable use of Internet Services IPv6 for this policy.
                choices:
                    - 'disable'
                    - 'enable'
            internet-service6-custom:
                type: raw
                description: (list) Deprecated, please rename it to internet_service6_custom. Custom Internet Service IPv6 name.
            internet-service6-custom-group:
                type: raw
                description: (list) Deprecated, please rename it to internet_service6_custom_group. Custom Internet Service IPv6 group name.
            internet-service6-group:
                type: raw
                description: (list) Deprecated, please rename it to internet_service6_group. Internet Service IPv6 group name.
            internet-service6-name:
                type: raw
                description: (list) Deprecated, please rename it to internet_service6_name. Internet Service IPv6 name.
            internet-service6-negate:
                type: str
                description: Deprecated, please rename it to internet_service6_negate. When enabled, Internet Services match against any internet servi...
                choices:
                    - 'disable'
                    - 'enable'
            ips-voip-filter:
                type: str
                description: Deprecated, please rename it to ips_voip_filter. Name of an existing VoIP
            virtual-patch-profile:
                type: str
                description: Deprecated, please rename it to virtual_patch_profile. Virtual patch profile.
            _policy_block:
                type: int
                description: Assigned policy block.
            dnsfilter-profile:
                type: raw
                description: (list) Deprecated, please rename it to dnsfilter_profile. Name of an existing DNS filter profile.
            log-http-transaction:
                type: str
                description: Deprecated, please rename it to log_http_transaction. Enable/disable HTTP transaction log.
                choices:
                    - 'disable'
                    - 'enable'
            ztna-proxy:
                type: raw
                description: (list) Deprecated, please rename it to ztna_proxy. IPv4 ZTNA traffic forward proxy.
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
    - name: Configure proxy policies.
      fortinet.fortimanager.fmgr_pkg_firewall_proxypolicy:
        bypass_validation: false
        adom: ansible
        pkg: ansible # package name
        state: present
        pkg_firewall_proxypolicy:
          action: accept # <value in [accept, deny, redirect]>
          comments: ansible-comment
          dstaddr: all
          dstintf: any
          policyid: 1
          schedule: always
          service: ALL
          srcaddr: all
          srcintf: any
          status: disable

- name: Gathering fortimanager facts
  hosts: fortimanagers
  gather_facts: false
  connection: httpapi
  vars:
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_httpapi_port: 443
  tasks:
    - name: Retrieve all the proxy policies
      fortinet.fortimanager.fmgr_fact:
        facts:
          selector: "pkg_firewall_proxypolicy"
          params:
            adom: "ansible"
            proxy-policy: "your_value"
            pkg: "ansible" # package name
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
        '/pm/config/adom/{adom}/pkg/{pkg}/firewall/proxy-policy'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/pkg/{pkg}/firewall/proxy-policy/{proxy-policy}'
    ]

    url_params = ['adom', 'pkg']
    module_primary_key = 'policyid'
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'pkg': {'required': True, 'type': 'str'},
        'pkg_firewall_proxypolicy': {
            'type': 'dict',
            'v_range': [['6.0.0', '']],
            'options': {
                'action': {'choices': ['accept', 'deny', 'redirect'], 'type': 'str'},
                'application-list': {'type': 'str'},
                'av-profile': {'type': 'str'},
                'comments': {'type': 'str'},
                'disclaimer': {'choices': ['disable', 'domain', 'policy', 'user'], 'type': 'str'},
                'dlp-sensor': {'type': 'str'},
                'dstaddr': {'type': 'raw'},
                'dstaddr-negate': {'choices': ['disable', 'enable'], 'type': 'str'},
                'dstaddr6': {'type': 'raw'},
                'dstintf': {'type': 'raw'},
                'global-label': {'type': 'str'},
                'groups': {'type': 'raw'},
                'http-tunnel-auth': {'choices': ['disable', 'enable'], 'type': 'str'},
                'icap-profile': {'type': 'str'},
                'internet-service': {'choices': ['disable', 'enable'], 'type': 'str'},
                'internet-service-custom': {'type': 'raw'},
                'internet-service-id': {'type': 'raw'},
                'internet-service-negate': {'choices': ['disable', 'enable'], 'type': 'str'},
                'ips-sensor': {'type': 'str'},
                'label': {'type': 'str'},
                'logtraffic': {'choices': ['disable', 'all', 'utm'], 'type': 'str'},
                'logtraffic-start': {'choices': ['disable', 'enable'], 'type': 'str'},
                'mms-profile': {'v_range': [['6.0.0', '7.2.0'], ['7.4.3', '']], 'type': 'str'},
                'policyid': {'required': True, 'type': 'int'},
                'poolname': {'type': 'raw'},
                'profile-group': {'type': 'str'},
                'profile-protocol-options': {'v_range': [['6.0.0', '7.2.2'], ['7.2.4', '7.2.4'], ['7.4.2', '']], 'type': 'str'},
                'profile-type': {'choices': ['single', 'group'], 'type': 'str'},
                'proxy': {
                    'choices': ['explicit-web', 'transparent-web', 'ftp', 'wanopt', 'ssh', 'ssh-tunnel', 'access-proxy', 'ztna-proxy'],
                    'type': 'str'
                },
                'redirect-url': {'type': 'str'},
                'replacemsg-override-group': {'type': 'str'},
                'scan-botnet-connections': {'v_range': [['6.0.0', '7.2.1']], 'choices': ['disable', 'block', 'monitor'], 'type': 'str'},
                'schedule': {'type': 'str'},
                'service': {'type': 'raw'},
                'service-negate': {'choices': ['disable', 'enable'], 'type': 'str'},
                'spamfilter-profile': {'v_range': [['6.0.0', '7.2.1']], 'type': 'str'},
                'srcaddr': {'type': 'raw'},
                'srcaddr-negate': {'choices': ['disable', 'enable'], 'type': 'str'},
                'srcaddr6': {'type': 'raw'},
                'srcintf': {'type': 'raw'},
                'ssl-ssh-profile': {'v_range': [['6.0.0', '7.2.2'], ['7.2.4', '7.2.4'], ['7.4.2', '']], 'type': 'str'},
                'status': {'choices': ['disable', 'enable'], 'type': 'str'},
                'tags': {'v_range': [['6.0.0', '6.4.14']], 'type': 'str'},
                'transparent': {'choices': ['disable', 'enable'], 'type': 'str'},
                'users': {'type': 'raw'},
                'utm-status': {'choices': ['disable', 'enable'], 'type': 'str'},
                'uuid': {'type': 'str'},
                'waf-profile': {'type': 'str'},
                'webcache': {'v_range': [['6.0.0', '7.2.0'], ['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'webcache-https': {'v_range': [['6.0.0', '7.2.0'], ['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'webfilter-profile': {'type': 'str'},
                'webproxy-forward-server': {'type': 'str'},
                'webproxy-profile': {'type': 'str'},
                'cifs-profile': {'v_range': [['6.2.0', '']], 'type': 'str'},
                'emailfilter-profile': {'v_range': [['6.2.0', '']], 'type': 'str'},
                'internet-service-custom-group': {'v_range': [['6.2.0', '']], 'type': 'raw'},
                'internet-service-group': {'v_range': [['6.2.0', '']], 'type': 'raw'},
                'session-ttl': {'v_range': [['6.2.0', '']], 'type': 'raw'},
                'ssh-filter-profile': {'v_range': [['6.2.0', '7.2.2'], ['7.2.4', '7.2.4'], ['7.4.2', '']], 'type': 'str'},
                'ssh-policy-redirect': {'v_range': [['6.2.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'decrypted-traffic-mirror': {'v_range': [['6.4.0', '7.2.2'], ['7.2.4', '7.2.4'], ['7.4.2', '']], 'type': 'str'},
                'internet-service-name': {'v_range': [['6.4.0', '7.2.2'], ['7.2.4', '7.2.4'], ['7.4.2', '']], 'type': 'raw'},
                'file-filter-profile': {'v_range': [['6.4.1', '7.2.2'], ['7.2.4', '7.2.4'], ['7.4.2', '']], 'type': 'str'},
                'name': {'v_range': [['6.4.2', '7.2.2'], ['7.2.4', '7.2.4'], ['7.4.2', '']], 'type': 'str'},
                'access-proxy': {'v_range': [['7.0.0', '7.2.2'], ['7.2.4', '7.2.4'], ['7.4.2', '']], 'type': 'raw'},
                'device-ownership': {'v_range': [['7.0.0', '7.2.2'], ['7.2.4', '7.2.4'], ['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'videofilter-profile': {'v_range': [['7.0.0', '7.2.2'], ['7.2.4', '7.2.4'], ['7.4.2', '']], 'type': 'str'},
                'voip-profile': {'v_range': [['7.0.0', '7.2.2'], ['7.4.3', '']], 'type': 'str'},
                'ztna-ems-tag': {'v_range': [['7.0.0', '7.2.2'], ['7.2.4', '7.2.4'], ['7.4.2', '']], 'type': 'raw'},
                'access-proxy6': {'v_range': [['7.0.1', '7.2.2'], ['7.2.4', '7.2.4'], ['7.4.2', '']], 'type': 'raw'},
                'block-notification': {
                    'v_range': [['7.0.3', '7.2.1'], ['7.2.4', '7.2.4'], ['7.4.2', '']],
                    'choices': ['disable', 'enable'],
                    'type': 'str'
                },
                'dlp-profile': {'v_range': [['7.2.0', '7.2.1'], ['7.2.4', '7.2.4'], ['7.4.2', '']], 'type': 'str'},
                'sctp-filter-profile': {'v_range': [['7.0.1', '7.2.2'], ['7.2.4', '7.2.4'], ['7.4.2', '']], 'type': 'str'},
                'ztna-tags-match-logic': {'v_range': [['7.0.2', '7.2.1'], ['7.2.4', '7.2.4'], ['7.4.2', '']], 'choices': ['or', 'and'], 'type': 'str'},
                'casb-profile': {'v_range': [['7.4.2', '']], 'type': 'str'},
                'detect-https-in-http-request': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'diameter-filter-profile': {'v_range': [['7.4.2', '']], 'type': 'str'},
                'internet-service6': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'internet-service6-custom': {'v_range': [['7.4.2', '']], 'type': 'raw'},
                'internet-service6-custom-group': {'v_range': [['7.4.2', '']], 'type': 'raw'},
                'internet-service6-group': {'v_range': [['7.4.2', '']], 'type': 'raw'},
                'internet-service6-name': {'v_range': [['7.4.2', '']], 'type': 'raw'},
                'internet-service6-negate': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ips-voip-filter': {'v_range': [['7.4.2', '']], 'type': 'str'},
                'virtual-patch-profile': {'v_range': [['7.4.2', '']], 'type': 'str'},
                '_policy_block': {'v_range': [['7.6.0', '']], 'type': 'int'},
                'dnsfilter-profile': {'v_range': [['7.6.0', '']], 'type': 'raw'},
                'log-http-transaction': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ztna-proxy': {'v_range': [['7.6.0', '']], 'type': 'raw'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('full crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'pkg_firewall_proxypolicy'),
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
