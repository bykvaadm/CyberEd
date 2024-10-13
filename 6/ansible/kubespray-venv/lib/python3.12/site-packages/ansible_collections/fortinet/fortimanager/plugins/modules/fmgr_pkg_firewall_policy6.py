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
module: fmgr_pkg_firewall_policy6
short_description: Configure IPv6 policies.
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
    pkg_firewall_policy6:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            action:
                type: str
                description: Policy action
                choices:
                    - 'deny'
                    - 'accept'
                    - 'ipsec'
                    - 'ssl-vpn'
            app-category:
                type: raw
                description: (list or str) Deprecated, please rename it to app_category. Application category ID list.
            application:
                type: raw
                description: (list) Application ID list.
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
            comments:
                type: str
                description: Comment.
            custom-log-fields:
                type: raw
                description: (list or str) Deprecated, please rename it to custom_log_fields. Log field index numbers to append custom log fields to lo...
            devices:
                type: raw
                description: (list or str) Names of devices or device groups that can be matched by the policy.
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
            dscp-match:
                type: str
                description: Deprecated, please rename it to dscp_match. Enable DSCP check.
                choices:
                    - 'disable'
                    - 'enable'
            dscp-negate:
                type: str
                description: Deprecated, please rename it to dscp_negate. Enable negated DSCP match.
                choices:
                    - 'disable'
                    - 'enable'
            dscp-value:
                type: str
                description: Deprecated, please rename it to dscp_value. DSCP value.
            dsri:
                type: str
                description: Enable DSRI to ignore HTTP server responses.
                choices:
                    - 'disable'
                    - 'enable'
            dstaddr:
                type: raw
                description: (list or str) Destination address and address group names.
            dstaddr-negate:
                type: str
                description: Deprecated, please rename it to dstaddr_negate. When enabled dstaddr specifies what the destination address must NOT be.
                choices:
                    - 'disable'
                    - 'enable'
            dstintf:
                type: raw
                description: (list or str) Outgoing
            firewall-session-dirty:
                type: str
                description: Deprecated, please rename it to firewall_session_dirty. How to handle sessions if the configuration of this firewall polic...
                choices:
                    - 'check-all'
                    - 'check-new'
            fixedport:
                type: str
                description: Enable to prevent source NAT from changing a sessions source port.
                choices:
                    - 'disable'
                    - 'enable'
            global-label:
                type: str
                description: Deprecated, please rename it to global_label. Label for the policy that appears when the GUI is in Global View mode.
            groups:
                type: raw
                description: (list or str) Names of user groups that can authenticate with this policy.
            icap-profile:
                type: str
                description: Deprecated, please rename it to icap_profile. Name of an existing ICAP profile.
            inbound:
                type: str
                description: Policy-based IPsec VPN
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
            label:
                type: str
                description: Label for the policy that appears when the GUI is in Section View mode.
            logtraffic:
                type: str
                description: Enable or disable logging.
                choices:
                    - 'disable'
                    - 'enable'
                    - 'all'
                    - 'utm'
            logtraffic-start:
                type: str
                description: Deprecated, please rename it to logtraffic_start. Record logs when a session starts and ends.
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
            natinbound:
                type: str
                description: Policy-based IPsec VPN
                choices:
                    - 'disable'
                    - 'enable'
            natoutbound:
                type: str
                description: Policy-based IPsec VPN
                choices:
                    - 'disable'
                    - 'enable'
            np-accelation:
                type: str
                description: Deprecated, please rename it to np_accelation. Enable/disable UTM Network Processor acceleration.
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
                description: Policy ID.
                required: true
            poolname:
                type: raw
                description: (list or str) IP Pool names.
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
            replacemsg-override-group:
                type: str
                description: Deprecated, please rename it to replacemsg_override_group. Override the default replacement message group for this policy.
            rsso:
                type: str
                description: Enable/disable RADIUS single sign-on
                choices:
                    - 'disable'
                    - 'enable'
            schedule:
                type: str
                description: Schedule name.
            send-deny-packet:
                type: str
                description: Deprecated, please rename it to send_deny_packet. Enable/disable return of deny-packet.
                choices:
                    - 'disable'
                    - 'enable'
            service:
                type: raw
                description: (list or str) Service and service group names.
            service-negate:
                type: str
                description: Deprecated, please rename it to service_negate. When enabled service specifies what the service must NOT be.
                choices:
                    - 'disable'
                    - 'enable'
            session-ttl:
                type: raw
                description: (int or str) Deprecated, please rename it to session_ttl. Session TTL in seconds for sessions accepted by this policy.
            spamfilter-profile:
                type: str
                description: Deprecated, please rename it to spamfilter_profile. Name of an existing Spam filter profile.
            srcaddr:
                type: raw
                description: (list or str) Source address and address group names.
            srcaddr-negate:
                type: str
                description: Deprecated, please rename it to srcaddr_negate. When enabled srcaddr specifies what the source address must NOT be.
                choices:
                    - 'disable'
                    - 'enable'
            srcintf:
                type: raw
                description: (list or str) Incoming
            ssl-mirror:
                type: str
                description: Deprecated, please rename it to ssl_mirror. Enable to copy decrypted SSL traffic to a FortiGate interface
                choices:
                    - 'disable'
                    - 'enable'
            ssl-mirror-intf:
                type: raw
                description: (list or str) Deprecated, please rename it to ssl_mirror_intf. SSL mirror interface name.
            ssl-ssh-profile:
                type: str
                description: Deprecated, please rename it to ssl_ssh_profile. Name of an existing SSL SSH profile.
            status:
                type: str
                description: Enable or disable this policy.
                choices:
                    - 'disable'
                    - 'enable'
            tags:
                type: str
                description: Names of object-tags applied to this policy.
            tcp-mss-receiver:
                type: int
                description: Deprecated, please rename it to tcp_mss_receiver. Receiver TCP maximum segment size
            tcp-mss-sender:
                type: int
                description: Deprecated, please rename it to tcp_mss_sender. Sender TCP maximum segment size
            tcp-session-without-syn:
                type: str
                description: Deprecated, please rename it to tcp_session_without_syn. Enable/disable creation of TCP session without SYN flag.
                choices:
                    - 'all'
                    - 'data-only'
                    - 'disable'
            timeout-send-rst:
                type: str
                description: Deprecated, please rename it to timeout_send_rst. Enable/disable sending RST packets when TCP sessions expire.
                choices:
                    - 'disable'
                    - 'enable'
            traffic-shaper:
                type: str
                description: Deprecated, please rename it to traffic_shaper. Reverse traffic shaper.
            traffic-shaper-reverse:
                type: str
                description: Deprecated, please rename it to traffic_shaper_reverse. Reverse traffic shaper.
            url-category:
                type: raw
                description: (list or str) Deprecated, please rename it to url_category. URL category ID list.
            users:
                type: raw
                description: (list or str) Names of individual users that can authenticate with this policy.
            utm-status:
                type: str
                description: Deprecated, please rename it to utm_status. Enable AV/web/ips protection profile.
                choices:
                    - 'disable'
                    - 'enable'
            uuid:
                type: str
                description: Universally Unique Identifier
            vlan-cos-fwd:
                type: int
                description: Deprecated, please rename it to vlan_cos_fwd. VLAN forward direction user priority
            vlan-cos-rev:
                type: int
                description: Deprecated, please rename it to vlan_cos_rev. VLAN reverse direction user priority
            voip-profile:
                type: str
                description: Deprecated, please rename it to voip_profile. Name of an existing VoIP profile.
            vpntunnel:
                type: str
                description: Policy-based IPsec VPN
            webfilter-profile:
                type: str
                description: Deprecated, please rename it to webfilter_profile. Name of an existing Web filter profile.
            anti-replay:
                type: str
                description: Deprecated, please rename it to anti_replay. Enable/disable anti-replay check.
                choices:
                    - 'disable'
                    - 'enable'
            app-group:
                type: raw
                description: (list or str) Deprecated, please rename it to app_group. Application group names.
            cifs-profile:
                type: str
                description: Deprecated, please rename it to cifs_profile. Name of an existing CIFS profile.
            dnsfilter-profile:
                type: str
                description: Deprecated, please rename it to dnsfilter_profile. Name of an existing DNS filter profile.
            emailfilter-profile:
                type: str
                description: Deprecated, please rename it to emailfilter_profile. Name of an existing email filter profile.
            http-policy-redirect:
                type: str
                description: Deprecated, please rename it to http_policy_redirect. Redirect HTTP
                choices:
                    - 'disable'
                    - 'enable'
            inspection-mode:
                type: str
                description: Deprecated, please rename it to inspection_mode. Policy inspection mode
                choices:
                    - 'proxy'
                    - 'flow'
            np-acceleration:
                type: str
                description: Deprecated, please rename it to np_acceleration. Enable/disable UTM Network Processor acceleration.
                choices:
                    - 'disable'
                    - 'enable'
            ssh-filter-profile:
                type: str
                description: Deprecated, please rename it to ssh_filter_profile. Name of an existing SSH filter profile.
            ssh-policy-redirect:
                type: str
                description: Deprecated, please rename it to ssh_policy_redirect. Redirect SSH traffic to matching transparent proxy policy.
                choices:
                    - 'disable'
                    - 'enable'
            tos:
                type: str
                description: ToS
            tos-mask:
                type: str
                description: Deprecated, please rename it to tos_mask. Non-zero bit positions are used for comparison while zero bit positions are ignored.
            tos-negate:
                type: str
                description: Deprecated, please rename it to tos_negate. Enable negated TOS match.
                choices:
                    - 'disable'
                    - 'enable'
            vlan-filter:
                type: str
                description: Deprecated, please rename it to vlan_filter. Set VLAN filters.
            waf-profile:
                type: str
                description: Deprecated, please rename it to waf_profile. Name of an existing Web application firewall profile.
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
            webproxy-forward-server:
                type: str
                description: Deprecated, please rename it to webproxy_forward_server. Web proxy forward server name.
            webproxy-profile:
                type: str
                description: Deprecated, please rename it to webproxy_profile. Webproxy profile name.
            casi-profile:
                type: str
                description: Deprecated, please rename it to casi_profile. CASI profile.
            fsso-groups:
                type: raw
                description: (list or str) Deprecated, please rename it to fsso_groups. Names of FSSO groups.
            decrypted-traffic-mirror:
                type: str
                description: Deprecated, please rename it to decrypted_traffic_mirror. Decrypted traffic mirror.
            cgn-log-server-grp:
                type: str
                description: Deprecated, please rename it to cgn_log_server_grp. NP log server group name
            policy-offload:
                type: str
                description: Deprecated, please rename it to policy_offload. Enable/disable offloading policy configuration to CP processors.
                choices:
                    - 'disable'
                    - 'enable'
            _policy_block:
                type: int
                description: Assigned policy block.
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
    - name: Configure IPv6 policies.
      fortinet.fortimanager.fmgr_pkg_firewall_policy6:
        bypass_validation: false
        adom: ansible
        pkg: ansible # package name
        state: present
        pkg_firewall_policy6:
          action: accept # <value in [deny, accept, ipsec, ...]>
          comments: ansible-comment
          dstaddr: all
          dstintf: any
          name: ansible-test-policy6
          nat: disable
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
    - name: Retrieve all the IPv6 policies
      fortinet.fortimanager.fmgr_fact:
        facts:
          selector: "pkg_firewall_policy6"
          params:
            adom: "ansible"
            pkg: "ansible" # package name
            policy6: "your_value"
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
        '/pm/config/adom/{adom}/pkg/{pkg}/firewall/policy6'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/pkg/{pkg}/firewall/policy6/{policy6}'
    ]

    url_params = ['adom', 'pkg']
    module_primary_key = 'policyid'
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'pkg': {'required': True, 'type': 'str'},
        'pkg_firewall_policy6': {
            'type': 'dict',
            'v_range': [['6.0.0', '']],
            'options': {
                'action': {'choices': ['deny', 'accept', 'ipsec', 'ssl-vpn'], 'type': 'str'},
                'app-category': {'type': 'raw'},
                'application': {'type': 'raw'},
                'application-list': {'type': 'str'},
                'auto-asic-offload': {'v_range': [['6.0.0', '7.2.0'], ['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'av-profile': {'type': 'str'},
                'comments': {'type': 'str'},
                'custom-log-fields': {'type': 'raw'},
                'devices': {'v_range': [['6.0.0', '7.2.1']], 'type': 'raw'},
                'diffserv-forward': {'choices': ['disable', 'enable'], 'type': 'str'},
                'diffserv-reverse': {'choices': ['disable', 'enable'], 'type': 'str'},
                'diffservcode-forward': {'type': 'str'},
                'diffservcode-rev': {'type': 'str'},
                'dlp-sensor': {'type': 'str'},
                'dscp-match': {'v_range': [['6.0.0', '7.2.1']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'dscp-negate': {'v_range': [['6.0.0', '7.2.1']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'dscp-value': {'v_range': [['6.0.0', '7.2.1']], 'type': 'str'},
                'dsri': {'choices': ['disable', 'enable'], 'type': 'str'},
                'dstaddr': {'type': 'raw'},
                'dstaddr-negate': {'choices': ['disable', 'enable'], 'type': 'str'},
                'dstintf': {'type': 'raw'},
                'firewall-session-dirty': {'choices': ['check-all', 'check-new'], 'type': 'str'},
                'fixedport': {'choices': ['disable', 'enable'], 'type': 'str'},
                'global-label': {'type': 'str'},
                'groups': {'type': 'raw'},
                'icap-profile': {'type': 'str'},
                'inbound': {'choices': ['disable', 'enable'], 'type': 'str'},
                'ippool': {'choices': ['disable', 'enable'], 'type': 'str'},
                'ips-sensor': {'type': 'str'},
                'label': {'type': 'str'},
                'logtraffic': {'choices': ['disable', 'enable', 'all', 'utm'], 'type': 'str'},
                'logtraffic-start': {'choices': ['disable', 'enable'], 'type': 'str'},
                'mms-profile': {'v_range': [['6.0.0', '7.2.0'], ['7.4.3', '']], 'type': 'str'},
                'name': {'type': 'str'},
                'nat': {'choices': ['disable', 'enable'], 'type': 'str'},
                'natinbound': {'choices': ['disable', 'enable'], 'type': 'str'},
                'natoutbound': {'choices': ['disable', 'enable'], 'type': 'str'},
                'np-accelation': {'v_range': [['6.0.0', '6.4.14']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'outbound': {'choices': ['disable', 'enable'], 'type': 'str'},
                'per-ip-shaper': {'type': 'str'},
                'policyid': {'required': True, 'type': 'int'},
                'poolname': {'type': 'raw'},
                'profile-group': {'type': 'str'},
                'profile-protocol-options': {'v_range': [['6.0.0', '7.2.1'], ['7.4.3', '']], 'type': 'str'},
                'profile-type': {'choices': ['single', 'group'], 'type': 'str'},
                'replacemsg-override-group': {'type': 'str'},
                'rsso': {'choices': ['disable', 'enable'], 'type': 'str'},
                'schedule': {'type': 'str'},
                'send-deny-packet': {'choices': ['disable', 'enable'], 'type': 'str'},
                'service': {'type': 'raw'},
                'service-negate': {'choices': ['disable', 'enable'], 'type': 'str'},
                'session-ttl': {'type': 'raw'},
                'spamfilter-profile': {'v_range': [['6.0.0', '7.2.1']], 'type': 'str'},
                'srcaddr': {'type': 'raw'},
                'srcaddr-negate': {'choices': ['disable', 'enable'], 'type': 'str'},
                'srcintf': {'type': 'raw'},
                'ssl-mirror': {'choices': ['disable', 'enable'], 'type': 'str'},
                'ssl-mirror-intf': {'type': 'raw'},
                'ssl-ssh-profile': {'v_range': [['6.0.0', '7.2.1'], ['7.4.3', '']], 'type': 'str'},
                'status': {'choices': ['disable', 'enable'], 'type': 'str'},
                'tags': {'v_range': [['6.0.0', '6.4.14']], 'type': 'str'},
                'tcp-mss-receiver': {'type': 'int'},
                'tcp-mss-sender': {'type': 'int'},
                'tcp-session-without-syn': {'choices': ['all', 'data-only', 'disable'], 'type': 'str'},
                'timeout-send-rst': {'choices': ['disable', 'enable'], 'type': 'str'},
                'traffic-shaper': {'type': 'str'},
                'traffic-shaper-reverse': {'type': 'str'},
                'url-category': {'type': 'raw'},
                'users': {'type': 'raw'},
                'utm-status': {'choices': ['disable', 'enable'], 'type': 'str'},
                'uuid': {'type': 'str'},
                'vlan-cos-fwd': {'type': 'int'},
                'vlan-cos-rev': {'type': 'int'},
                'voip-profile': {'type': 'str'},
                'vpntunnel': {'type': 'str'},
                'webfilter-profile': {'type': 'str'},
                'anti-replay': {'v_range': [['6.2.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'app-group': {'v_range': [['6.2.0', '']], 'type': 'raw'},
                'cifs-profile': {'v_range': [['6.2.0', '']], 'type': 'str'},
                'dnsfilter-profile': {'v_range': [['6.2.0', '']], 'type': 'str'},
                'emailfilter-profile': {'v_range': [['6.2.0', '']], 'type': 'str'},
                'http-policy-redirect': {'v_range': [['6.2.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'inspection-mode': {'v_range': [['6.2.0', '']], 'choices': ['proxy', 'flow'], 'type': 'str'},
                'np-acceleration': {'v_range': [['6.2.0', '7.2.0'], ['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ssh-filter-profile': {'v_range': [['6.2.0', '7.2.1'], ['7.4.3', '']], 'type': 'str'},
                'ssh-policy-redirect': {'v_range': [['6.2.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'tos': {'v_range': [['6.2.0', '']], 'type': 'str'},
                'tos-mask': {'v_range': [['6.2.0', '']], 'type': 'str'},
                'tos-negate': {'v_range': [['6.2.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'vlan-filter': {'v_range': [['6.2.0', '']], 'type': 'str'},
                'waf-profile': {'v_range': [['6.2.1', '']], 'type': 'str'},
                'webcache': {'v_range': [['6.2.1', '7.2.0'], ['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'webcache-https': {'v_range': [['6.2.1', '7.2.0'], ['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'webproxy-forward-server': {'v_range': [['6.2.1', '']], 'type': 'str'},
                'webproxy-profile': {'v_range': [['6.2.1', '']], 'type': 'str'},
                'casi-profile': {'v_range': [['6.2.0', '6.2.12']], 'type': 'str'},
                'fsso-groups': {'v_range': [['6.2.3', '']], 'type': 'raw'},
                'decrypted-traffic-mirror': {'v_range': [['6.4.0', '6.4.0']], 'type': 'str'},
                'cgn-log-server-grp': {'v_range': [['6.2.7', '6.2.12'], ['6.4.3', '']], 'type': 'str'},
                'policy-offload': {'v_range': [['6.2.7', '6.2.12'], ['6.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                '_policy_block': {'v_range': [['7.0.3', '']], 'type': 'int'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('full crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'pkg_firewall_policy6'),
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
