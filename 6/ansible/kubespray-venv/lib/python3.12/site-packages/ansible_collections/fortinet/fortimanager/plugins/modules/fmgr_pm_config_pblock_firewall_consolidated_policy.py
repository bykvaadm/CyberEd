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
module: fmgr_pm_config_pblock_firewall_consolidated_policy
short_description: Configure consolidated IPv4/IPv6 policies.
description:
    - This module is able to configure a FortiManager device.
    - Examples include all parameters and values which need to be adjusted to data sources before usage.

version_added: "2.2.0"
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
    pm_config_pblock_firewall_consolidated_policy:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            _policy_block:
                type: int
                description: Assigned policy block.
            action:
                type: str
                description: Policy action
                choices:
                    - 'deny'
                    - 'accept'
                    - 'ipsec'
            app-category:
                type: raw
                description: (list) Deprecated, please rename it to app_category. App category.
            app-group:
                type: raw
                description: (list) Deprecated, please rename it to app_group. App group.
            application:
                type: raw
                description: (list) Application.
            application-list:
                type: str
                description: Deprecated, please rename it to application_list. Name of an existing Application list.
            auto-asic-offload:
                type: str
                description: Deprecated, please rename it to auto_asic_offload. Enable/disable policy traffic ASIC offloading.
                choices:
                    - 'disable'
                    - 'enable'
            av-profile:
                type: str
                description: Deprecated, please rename it to av_profile. Name of an existing Antivirus profile.
            captive-portal-exempt:
                type: str
                description: Deprecated, please rename it to captive_portal_exempt. Enable exemption of some users from the captive portal.
                choices:
                    - 'disable'
                    - 'enable'
            cifs-profile:
                type: str
                description: Deprecated, please rename it to cifs_profile. Name of an existing CIFS profile.
            comments:
                type: str
                description: Comment.
            diffserv-forward:
                type: str
                description: Deprecated, please rename it to diffserv_forward. Enable to change packets DiffServ values to the specified diffservcode-f...
                choices:
                    - 'disable'
                    - 'enable'
            diffserv-reverse:
                type: str
                description: Deprecated, please rename it to diffserv_reverse. Enable to change packets reverse
                choices:
                    - 'disable'
                    - 'enable'
            diffservcode-forward:
                type: str
                description: Deprecated, please rename it to diffservcode_forward. Change packets DiffServ to this value.
            diffservcode-rev:
                type: str
                description: Deprecated, please rename it to diffservcode_rev. Change packets reverse
            dlp-sensor:
                type: str
                description: Deprecated, please rename it to dlp_sensor. Name of an existing DLP sensor.
            dnsfilter-profile:
                type: str
                description: Deprecated, please rename it to dnsfilter_profile. Name of an existing DNS filter profile.
            dstaddr-negate:
                type: str
                description: Deprecated, please rename it to dstaddr_negate. When enabled dstaddr specifies what the destination address must NOT be.
                choices:
                    - 'disable'
                    - 'enable'
            dstaddr4:
                type: raw
                description: (list) Destination IPv4 address name and address group names.
            dstaddr6:
                type: raw
                description: (list) Destination IPv6 address name and address group names.
            dstintf:
                type: raw
                description: (list) Outgoing
            emailfilter-profile:
                type: str
                description: Deprecated, please rename it to emailfilter_profile. Name of an existing email filter profile.
            fixedport:
                type: str
                description: Enable to prevent source NAT from changing a sessions source port.
                choices:
                    - 'disable'
                    - 'enable'
            fsso-groups:
                type: raw
                description: (list) Deprecated, please rename it to fsso_groups. Names of FSSO groups.
            global-label:
                type: str
                description: Deprecated, please rename it to global_label. Label for the policy that appears when the GUI is in Global View mode.
            groups:
                type: raw
                description: (list) Names of user groups that can authenticate with this policy.
            http-policy-redirect:
                type: str
                description: Deprecated, please rename it to http_policy_redirect. Redirect HTTP
                choices:
                    - 'disable'
                    - 'enable'
            icap-profile:
                type: str
                description: Deprecated, please rename it to icap_profile. Name of an existing ICAP profile.
            inbound:
                type: str
                description: Policy-based IPsec VPN
                choices:
                    - 'disable'
                    - 'enable'
            inspection-mode:
                type: str
                description: Deprecated, please rename it to inspection_mode. Policy inspection mode
                choices:
                    - 'proxy'
                    - 'flow'
            internet-service:
                type: str
                description: Deprecated, please rename it to internet_service. Enable/disable use of Internet Services for this policy.
                choices:
                    - 'disable'
                    - 'enable'
            internet-service-custom:
                type: raw
                description: (list) Deprecated, please rename it to internet_service_custom. Custom Internet Service name.
            internet-service-custom-group:
                type: raw
                description: (list) Deprecated, please rename it to internet_service_custom_group. Custom Internet Service group name.
            internet-service-group:
                type: raw
                description: (list) Deprecated, please rename it to internet_service_group. Internet Service group name.
            internet-service-id:
                type: raw
                description: (list) Deprecated, please rename it to internet_service_id. Internet Service ID.
            internet-service-negate:
                type: str
                description: Deprecated, please rename it to internet_service_negate. When enabled internet-service specifies what the service must NOT be.
                choices:
                    - 'disable'
                    - 'enable'
            internet-service-src:
                type: str
                description: Deprecated, please rename it to internet_service_src. Enable/disable use of Internet Services in source for this policy.
                choices:
                    - 'disable'
                    - 'enable'
            internet-service-src-custom:
                type: raw
                description: (list) Deprecated, please rename it to internet_service_src_custom. Custom Internet Service source name.
            internet-service-src-custom-group:
                type: raw
                description: (list) Deprecated, please rename it to internet_service_src_custom_group. Custom Internet Service source group name.
            internet-service-src-group:
                type: raw
                description: (list) Deprecated, please rename it to internet_service_src_group. Internet Service source group name.
            internet-service-src-id:
                type: raw
                description: (list) Deprecated, please rename it to internet_service_src_id. Internet Service source ID.
            internet-service-src-negate:
                type: str
                description: Deprecated, please rename it to internet_service_src_negate. When enabled internet-service-src specifies what the service ...
                choices:
                    - 'disable'
                    - 'enable'
            ippool:
                type: str
                description: Enable to use IP Pools for source NAT.
                choices:
                    - 'disable'
                    - 'enable'
            ips-sensor:
                type: str
                description: Deprecated, please rename it to ips_sensor. Name of an existing IPS sensor.
            logtraffic:
                type: str
                description: Enable or disable logging.
                choices:
                    - 'disable'
                    - 'all'
                    - 'utm'
            logtraffic-start:
                type: str
                description: Deprecated, please rename it to logtraffic_start. Record logs when a session starts.
                choices:
                    - 'disable'
                    - 'enable'
            mms-profile:
                type: str
                description: Deprecated, please rename it to mms_profile. Name of an existing MMS profile.
            name:
                type: str
                description: Policy name.
            nat:
                type: str
                description: Enable/disable source NAT.
                choices:
                    - 'disable'
                    - 'enable'
            outbound:
                type: str
                description: Policy-based IPsec VPN
                choices:
                    - 'disable'
                    - 'enable'
            per-ip-shaper:
                type: str
                description: Deprecated, please rename it to per_ip_shaper. Per-IP traffic shaper.
            policyid:
                type: int
                description: Policy ID
                required: true
            poolname4:
                type: raw
                description: (list) IPv4 pool names.
            poolname6:
                type: raw
                description: (list) IPv6 pool names.
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
            schedule:
                type: str
                description: Schedule name.
            service:
                type: raw
                description: (list) Service and service group names.
            service-negate:
                type: str
                description: Deprecated, please rename it to service_negate. When enabled service specifies what the service must NOT be.
                choices:
                    - 'disable'
                    - 'enable'
            session-ttl:
                type: int
                description: Deprecated, please rename it to session_ttl. TTL in seconds for sessions accepted by this policy
            srcaddr-negate:
                type: str
                description: Deprecated, please rename it to srcaddr_negate. When enabled srcaddr specifies what the source address must NOT be.
                choices:
                    - 'disable'
                    - 'enable'
            srcaddr4:
                type: raw
                description: (list) Source IPv4 address name and address group names.
            srcaddr6:
                type: raw
                description: (list) Source IPv6 address name and address group names.
            srcintf:
                type: raw
                description: (list) Incoming
            ssh-filter-profile:
                type: str
                description: Deprecated, please rename it to ssh_filter_profile. Name of an existing SSH filter profile.
            ssh-policy-redirect:
                type: str
                description: Deprecated, please rename it to ssh_policy_redirect. Redirect SSH traffic to matching transparent proxy policy.
                choices:
                    - 'disable'
                    - 'enable'
            ssl-ssh-profile:
                type: str
                description: Deprecated, please rename it to ssl_ssh_profile. Name of an existing SSL SSH profile.
            status:
                type: str
                description: Enable or disable this policy.
                choices:
                    - 'disable'
                    - 'enable'
            tcp-mss-receiver:
                type: int
                description: Deprecated, please rename it to tcp_mss_receiver. Receiver TCP maximum segment size
            tcp-mss-sender:
                type: int
                description: Deprecated, please rename it to tcp_mss_sender. Sender TCP maximum segment size
            traffic-shaper:
                type: str
                description: Deprecated, please rename it to traffic_shaper. Traffic shaper.
            traffic-shaper-reverse:
                type: str
                description: Deprecated, please rename it to traffic_shaper_reverse. Reverse traffic shaper.
            url-category:
                type: raw
                description: (list) Deprecated, please rename it to url_category. Url category.
            users:
                type: raw
                description: (list) Names of individual users that can authenticate with this policy.
            utm-status:
                type: str
                description: Deprecated, please rename it to utm_status. Enable to add one or more security profiles
                choices:
                    - 'disable'
                    - 'enable'
            uuid:
                type: str
                description: Universally Unique Identifier
            voip-profile:
                type: str
                description: Deprecated, please rename it to voip_profile. Name of an existing VoIP profile.
            vpntunnel:
                type: str
                description: Policy-based IPsec VPN
            waf-profile:
                type: str
                description: Deprecated, please rename it to waf_profile. Name of an existing Web application firewall profile.
            wanopt:
                type: str
                description: Enable/disable WAN optimization.
                choices:
                    - 'disable'
                    - 'enable'
            wanopt-detection:
                type: str
                description: Deprecated, please rename it to wanopt_detection. WAN optimization auto-detection mode.
                choices:
                    - 'active'
                    - 'passive'
                    - 'off'
            wanopt-passive-opt:
                type: str
                description: Deprecated, please rename it to wanopt_passive_opt. WAN optimization passive mode options.
                choices:
                    - 'default'
                    - 'transparent'
                    - 'non-transparent'
            wanopt-peer:
                type: str
                description: Deprecated, please rename it to wanopt_peer. WAN optimization peer.
            wanopt-profile:
                type: str
                description: Deprecated, please rename it to wanopt_profile. WAN optimization profile.
            webcache:
                type: str
                description: Enable/disable web cache.
                choices:
                    - 'disable'
                    - 'enable'
            webcache-https:
                type: str
                description: Deprecated, please rename it to webcache_https. Enable/disable web cache for HTTPS.
                choices:
                    - 'disable'
                    - 'enable'
            webfilter-profile:
                type: str
                description: Deprecated, please rename it to webfilter_profile. Name of an existing Web filter profile.
            webproxy-forward-server:
                type: str
                description: Deprecated, please rename it to webproxy_forward_server. Webproxy forward server name.
            webproxy-profile:
                type: str
                description: Deprecated, please rename it to webproxy_profile. Webproxy profile name.
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
    - name: Configure consolidated IPv4/IPv6 policies.
      fortinet.fortimanager.fmgr_pm_config_pblock_firewall_consolidated_policy:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        adom: <your own value>
        pblock: <your own value>
        state: present # <value in [present, absent]>
        pm_config_pblock_firewall_consolidated_policy:
          _policy_block: <integer>
          action: <value in [deny, accept, ipsec]>
          app_category: <list or string>
          app_group: <list or string>
          application: <list or integer>
          application_list: <string>
          auto_asic_offload: <value in [disable, enable]>
          av_profile: <string>
          captive_portal_exempt: <value in [disable, enable]>
          cifs_profile: <string>
          comments: <string>
          diffserv_forward: <value in [disable, enable]>
          diffserv_reverse: <value in [disable, enable]>
          diffservcode_forward: <string>
          diffservcode_rev: <string>
          dlp_sensor: <string>
          dnsfilter_profile: <string>
          dstaddr_negate: <value in [disable, enable]>
          dstaddr4: <list or string>
          dstaddr6: <list or string>
          dstintf: <list or string>
          emailfilter_profile: <string>
          fixedport: <value in [disable, enable]>
          fsso_groups: <list or string>
          global_label: <string>
          groups: <list or string>
          http_policy_redirect: <value in [disable, enable]>
          icap_profile: <string>
          inbound: <value in [disable, enable]>
          inspection_mode: <value in [proxy, flow]>
          internet_service: <value in [disable, enable]>
          internet_service_custom: <list or string>
          internet_service_custom_group: <list or string>
          internet_service_group: <list or string>
          internet_service_id: <list or string>
          internet_service_negate: <value in [disable, enable]>
          internet_service_src: <value in [disable, enable]>
          internet_service_src_custom: <list or string>
          internet_service_src_custom_group: <list or string>
          internet_service_src_group: <list or string>
          internet_service_src_id: <list or string>
          internet_service_src_negate: <value in [disable, enable]>
          ippool: <value in [disable, enable]>
          ips_sensor: <string>
          logtraffic: <value in [disable, all, utm]>
          logtraffic_start: <value in [disable, enable]>
          mms_profile: <string>
          name: <string>
          nat: <value in [disable, enable]>
          outbound: <value in [disable, enable]>
          per_ip_shaper: <string>
          policyid: <integer>
          poolname4: <list or string>
          poolname6: <list or string>
          profile_group: <string>
          profile_protocol_options: <string>
          profile_type: <value in [single, group]>
          schedule: <string>
          service: <list or string>
          service_negate: <value in [disable, enable]>
          session_ttl: <integer>
          srcaddr_negate: <value in [disable, enable]>
          srcaddr4: <list or string>
          srcaddr6: <list or string>
          srcintf: <list or string>
          ssh_filter_profile: <string>
          ssh_policy_redirect: <value in [disable, enable]>
          ssl_ssh_profile: <string>
          status: <value in [disable, enable]>
          tcp_mss_receiver: <integer>
          tcp_mss_sender: <integer>
          traffic_shaper: <string>
          traffic_shaper_reverse: <string>
          url_category: <list or string>
          users: <list or string>
          utm_status: <value in [disable, enable]>
          uuid: <string>
          voip_profile: <string>
          vpntunnel: <string>
          waf_profile: <string>
          wanopt: <value in [disable, enable]>
          wanopt_detection: <value in [active, passive, off]>
          wanopt_passive_opt: <value in [default, transparent, non-transparent]>
          wanopt_peer: <string>
          wanopt_profile: <string>
          webcache: <value in [disable, enable]>
          webcache_https: <value in [disable, enable]>
          webfilter_profile: <string>
          webproxy_forward_server: <string>
          webproxy_profile: <string>
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
        '/pm/config/adom/{adom}/pblock/{pblock}/firewall/consolidated/policy'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/pblock/{pblock}/firewall/consolidated/policy/{policy}'
    ]

    url_params = ['adom', 'pblock']
    module_primary_key = 'policyid'
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'pblock': {'required': True, 'type': 'str'},
        'pm_config_pblock_firewall_consolidated_policy': {
            'type': 'dict',
            'v_range': [['7.0.3', '']],
            'options': {
                '_policy_block': {'v_range': [['7.0.3', '']], 'type': 'int'},
                'action': {'v_range': [['7.0.3', '']], 'choices': ['deny', 'accept', 'ipsec'], 'type': 'str'},
                'app-category': {'v_range': [['7.0.3', '7.4.2']], 'type': 'raw'},
                'app-group': {'v_range': [['7.0.3', '7.4.2']], 'type': 'raw'},
                'application': {'v_range': [['7.0.3', '7.4.2']], 'type': 'raw'},
                'application-list': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'auto-asic-offload': {'v_range': [['7.0.3', '7.2.0'], ['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'av-profile': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'captive-portal-exempt': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'cifs-profile': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'comments': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'diffserv-forward': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'diffserv-reverse': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'diffservcode-forward': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'diffservcode-rev': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'dlp-sensor': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'dnsfilter-profile': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'dstaddr-negate': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'dstaddr4': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'dstaddr6': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'dstintf': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'emailfilter-profile': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'fixedport': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'fsso-groups': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'global-label': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'groups': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'http-policy-redirect': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'icap-profile': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'inbound': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'inspection-mode': {'v_range': [['7.0.3', '']], 'choices': ['proxy', 'flow'], 'type': 'str'},
                'internet-service': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'internet-service-custom': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'internet-service-custom-group': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'internet-service-group': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'internet-service-id': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'internet-service-negate': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'internet-service-src': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'internet-service-src-custom': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'internet-service-src-custom-group': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'internet-service-src-group': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'internet-service-src-id': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'internet-service-src-negate': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ippool': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ips-sensor': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'logtraffic': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'all', 'utm'], 'type': 'str'},
                'logtraffic-start': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'mms-profile': {'v_range': [['7.0.3', '7.2.0'], ['7.4.3', '']], 'type': 'str'},
                'name': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'nat': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'outbound': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'per-ip-shaper': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'policyid': {'v_range': [['7.0.3', '']], 'required': True, 'type': 'int'},
                'poolname4': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'poolname6': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'profile-group': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'profile-protocol-options': {'v_range': [['7.0.3', '7.2.0'], ['7.4.3', '']], 'type': 'str'},
                'profile-type': {'v_range': [['7.0.3', '']], 'choices': ['single', 'group'], 'type': 'str'},
                'schedule': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'service': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'service-negate': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'session-ttl': {'v_range': [['7.0.3', '']], 'type': 'int'},
                'srcaddr-negate': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'srcaddr4': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'srcaddr6': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'srcintf': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'ssh-filter-profile': {'v_range': [['7.0.3', '7.2.0'], ['7.4.3', '']], 'type': 'str'},
                'ssh-policy-redirect': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ssl-ssh-profile': {'v_range': [['7.0.3', '7.2.0'], ['7.4.3', '']], 'type': 'str'},
                'status': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'tcp-mss-receiver': {'v_range': [['7.0.3', '']], 'type': 'int'},
                'tcp-mss-sender': {'v_range': [['7.0.3', '']], 'type': 'int'},
                'traffic-shaper': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'traffic-shaper-reverse': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'url-category': {'v_range': [['7.0.3', '7.4.2']], 'type': 'raw'},
                'users': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'utm-status': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'uuid': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'voip-profile': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'vpntunnel': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'waf-profile': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'wanopt': {'v_range': [['7.0.3', '7.2.0'], ['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'wanopt-detection': {'v_range': [['7.0.3', '7.2.0'], ['7.4.3', '']], 'choices': ['active', 'passive', 'off'], 'type': 'str'},
                'wanopt-passive-opt': {
                    'v_range': [['7.0.3', '7.2.0'], ['7.4.3', '']],
                    'choices': ['default', 'transparent', 'non-transparent'],
                    'type': 'str'
                },
                'wanopt-peer': {'v_range': [['7.0.3', '7.2.0'], ['7.4.3', '']], 'type': 'str'},
                'wanopt-profile': {'v_range': [['7.0.3', '7.2.0'], ['7.4.3', '']], 'type': 'str'},
                'webcache': {'v_range': [['7.0.3', '7.2.0'], ['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'webcache-https': {'v_range': [['7.0.3', '7.2.0'], ['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'webfilter-profile': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'webproxy-forward-server': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'webproxy-profile': {'v_range': [['7.0.3', '']], 'type': 'str'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('full crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'pm_config_pblock_firewall_consolidated_policy'),
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
