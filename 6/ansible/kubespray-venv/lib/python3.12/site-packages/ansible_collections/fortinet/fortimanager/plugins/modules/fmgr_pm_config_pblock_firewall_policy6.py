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
module: fmgr_pm_config_pblock_firewall_policy6
short_description: Configure IPv6 policies.
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
    pm_config_pblock_firewall_policy6:
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
                    - 'ssl-vpn'
            anti-replay:
                type: str
                description: Deprecated, please rename it to anti_replay. Enable/disable anti-replay check.
                choices:
                    - 'disable'
                    - 'enable'
            app-category:
                type: raw
                description: (list) Deprecated, please rename it to app_category. Application category ID list.
            app-group:
                type: raw
                description: (list) Deprecated, please rename it to app_group. Application group names.
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
            cgn-log-server-grp:
                type: str
                description: Deprecated, please rename it to cgn_log_server_grp. Cgn log server grp.
            cifs-profile:
                type: str
                description: Deprecated, please rename it to cifs_profile. Name of an existing CIFS profile.
            comments:
                type: str
                description: Comment.
            custom-log-fields:
                type: raw
                description: (list) Deprecated, please rename it to custom_log_fields. Log field index numbers to append custom log fields to log messa...
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
            dsri:
                type: str
                description: Enable DSRI to ignore HTTP server responses.
                choices:
                    - 'disable'
                    - 'enable'
            dstaddr:
                type: raw
                description: (list) Destination address and address group names.
            dstaddr-negate:
                type: str
                description: Deprecated, please rename it to dstaddr_negate. When enabled dstaddr specifies what the destination address must NOT be.
                choices:
                    - 'disable'
                    - 'enable'
            dstintf:
                type: raw
                description: (list) Outgoing
            emailfilter-profile:
                type: str
                description: Deprecated, please rename it to emailfilter_profile. Name of an existing email filter profile.
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
            np-acceleration:
                type: str
                description: Deprecated, please rename it to np_acceleration. Enable/disable UTM Network Processor acceleration.
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
            policy-offload:
                type: str
                description: Deprecated, please rename it to policy_offload. Policy offload.
                choices:
                    - 'disable'
                    - 'enable'
            policyid:
                type: int
                description: Policy ID
                required: true
            poolname:
                type: raw
                description: (list) IP Pool names.
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
                description: (list) Service and service group names.
            service-negate:
                type: str
                description: Deprecated, please rename it to service_negate. When enabled service specifies what the service must NOT be.
                choices:
                    - 'disable'
                    - 'enable'
            session-ttl:
                type: str
                description: Deprecated, please rename it to session_ttl. Session TTL in seconds for sessions accepted by this policy.
            srcaddr:
                type: raw
                description: (list) Source address and address group names.
            srcaddr-negate:
                type: str
                description: Deprecated, please rename it to srcaddr_negate. When enabled srcaddr specifies what the source address must NOT be.
                choices:
                    - 'disable'
                    - 'enable'
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
            ssl-mirror:
                type: str
                description: Deprecated, please rename it to ssl_mirror. Enable to copy decrypted SSL traffic to a FortiGate interface
                choices:
                    - 'disable'
                    - 'enable'
            ssl-mirror-intf:
                type: raw
                description: (list) Deprecated, please rename it to ssl_mirror_intf. SSL mirror interface name.
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
            traffic-shaper:
                type: str
                description: Deprecated, please rename it to traffic_shaper. Reverse traffic shaper.
            traffic-shaper-reverse:
                type: str
                description: Deprecated, please rename it to traffic_shaper_reverse. Reverse traffic shaper.
            url-category:
                type: raw
                description: (list) Deprecated, please rename it to url_category. URL category ID list.
            users:
                type: raw
                description: (list) Names of individual users that can authenticate with this policy.
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
            vlan-filter:
                type: str
                description: Deprecated, please rename it to vlan_filter. Set VLAN filters.
            voip-profile:
                type: str
                description: Deprecated, please rename it to voip_profile. Name of an existing VoIP profile.
            vpntunnel:
                type: str
                description: Policy-based IPsec VPN
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
            webfilter-profile:
                type: str
                description: Deprecated, please rename it to webfilter_profile. Name of an existing Web filter profile.
            webproxy-forward-server:
                type: str
                description: Deprecated, please rename it to webproxy_forward_server. Web proxy forward server name.
            webproxy-profile:
                type: str
                description: Deprecated, please rename it to webproxy_profile. Webproxy profile name.
            dscp-negate:
                type: str
                description: Deprecated, please rename it to dscp_negate. Enable negated DSCP match.
                choices:
                    - 'disable'
                    - 'enable'
            devices:
                type: raw
                description: (list) Names of devices or device groups that can be matched by the policy.
            dscp-value:
                type: str
                description: Deprecated, please rename it to dscp_value. DSCP value.
            spamfilter-profile:
                type: str
                description: Deprecated, please rename it to spamfilter_profile. Name of an existing Spam filter profile.
            dscp-match:
                type: str
                description: Deprecated, please rename it to dscp_match. Enable DSCP check.
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
    - name: Configure IPv6 policies.
      fortinet.fortimanager.fmgr_pm_config_pblock_firewall_policy6:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        adom: <your own value>
        pblock: <your own value>
        state: present # <value in [present, absent]>
        pm_config_pblock_firewall_policy6:
          _policy_block: <integer>
          action: <value in [deny, accept, ipsec, ...]>
          anti_replay: <value in [disable, enable]>
          app_category: <list or string>
          app_group: <list or string>
          application: <list or integer>
          application_list: <string>
          auto_asic_offload: <value in [disable, enable]>
          av_profile: <string>
          cgn_log_server_grp: <string>
          cifs_profile: <string>
          comments: <string>
          custom_log_fields: <list or string>
          diffserv_forward: <value in [disable, enable]>
          diffserv_reverse: <value in [disable, enable]>
          diffservcode_forward: <string>
          diffservcode_rev: <string>
          dlp_sensor: <string>
          dnsfilter_profile: <string>
          dsri: <value in [disable, enable]>
          dstaddr: <list or string>
          dstaddr_negate: <value in [disable, enable]>
          dstintf: <list or string>
          emailfilter_profile: <string>
          firewall_session_dirty: <value in [check-all, check-new]>
          fixedport: <value in [disable, enable]>
          fsso_groups: <list or string>
          global_label: <string>
          groups: <list or string>
          http_policy_redirect: <value in [disable, enable]>
          icap_profile: <string>
          inbound: <value in [disable, enable]>
          inspection_mode: <value in [proxy, flow]>
          ippool: <value in [disable, enable]>
          ips_sensor: <string>
          label: <string>
          logtraffic: <value in [disable, enable, all, ...]>
          logtraffic_start: <value in [disable, enable]>
          mms_profile: <string>
          name: <string>
          nat: <value in [disable, enable]>
          natinbound: <value in [disable, enable]>
          natoutbound: <value in [disable, enable]>
          np_acceleration: <value in [disable, enable]>
          outbound: <value in [disable, enable]>
          per_ip_shaper: <string>
          policy_offload: <value in [disable, enable]>
          policyid: <integer>
          poolname: <list or string>
          profile_group: <string>
          profile_protocol_options: <string>
          profile_type: <value in [single, group]>
          replacemsg_override_group: <string>
          rsso: <value in [disable, enable]>
          schedule: <string>
          send_deny_packet: <value in [disable, enable]>
          service: <list or string>
          service_negate: <value in [disable, enable]>
          session_ttl: <string>
          srcaddr: <list or string>
          srcaddr_negate: <value in [disable, enable]>
          srcintf: <list or string>
          ssh_filter_profile: <string>
          ssh_policy_redirect: <value in [disable, enable]>
          ssl_mirror: <value in [disable, enable]>
          ssl_mirror_intf: <list or string>
          ssl_ssh_profile: <string>
          status: <value in [disable, enable]>
          tcp_mss_receiver: <integer>
          tcp_mss_sender: <integer>
          tcp_session_without_syn: <value in [all, data-only, disable]>
          timeout_send_rst: <value in [disable, enable]>
          tos: <string>
          tos_mask: <string>
          tos_negate: <value in [disable, enable]>
          traffic_shaper: <string>
          traffic_shaper_reverse: <string>
          url_category: <list or string>
          users: <list or string>
          utm_status: <value in [disable, enable]>
          uuid: <string>
          vlan_cos_fwd: <integer>
          vlan_cos_rev: <integer>
          vlan_filter: <string>
          voip_profile: <string>
          vpntunnel: <string>
          waf_profile: <string>
          webcache: <value in [disable, enable]>
          webcache_https: <value in [disable, enable]>
          webfilter_profile: <string>
          webproxy_forward_server: <string>
          webproxy_profile: <string>
          dscp_negate: <value in [disable, enable]>
          devices: <list or string>
          dscp_value: <string>
          spamfilter_profile: <string>
          dscp_match: <value in [disable, enable]>
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
        '/pm/config/adom/{adom}/pblock/{pblock}/firewall/policy6'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/pblock/{pblock}/firewall/policy6/{policy6}'
    ]

    url_params = ['adom', 'pblock']
    module_primary_key = 'policyid'
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'pblock': {'required': True, 'type': 'str'},
        'pm_config_pblock_firewall_policy6': {
            'type': 'dict',
            'v_range': [['7.0.3', '']],
            'options': {
                '_policy_block': {'v_range': [['7.0.3', '']], 'type': 'int'},
                'action': {'v_range': [['7.0.3', '']], 'choices': ['deny', 'accept', 'ipsec', 'ssl-vpn'], 'type': 'str'},
                'anti-replay': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'app-category': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'app-group': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'application': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'application-list': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'auto-asic-offload': {'v_range': [['7.0.3', '7.2.0'], ['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'av-profile': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'cgn-log-server-grp': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'cifs-profile': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'comments': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'custom-log-fields': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'diffserv-forward': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'diffserv-reverse': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'diffservcode-forward': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'diffservcode-rev': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'dlp-sensor': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'dnsfilter-profile': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'dsri': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'dstaddr': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'dstaddr-negate': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'dstintf': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'emailfilter-profile': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'firewall-session-dirty': {'v_range': [['7.0.3', '']], 'choices': ['check-all', 'check-new'], 'type': 'str'},
                'fixedport': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'fsso-groups': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'global-label': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'groups': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'http-policy-redirect': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'icap-profile': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'inbound': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'inspection-mode': {'v_range': [['7.0.3', '']], 'choices': ['proxy', 'flow'], 'type': 'str'},
                'ippool': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ips-sensor': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'label': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'logtraffic': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable', 'all', 'utm'], 'type': 'str'},
                'logtraffic-start': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'mms-profile': {'v_range': [['7.0.3', '7.2.0'], ['7.4.3', '']], 'type': 'str'},
                'name': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'nat': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'natinbound': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'natoutbound': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'np-acceleration': {'v_range': [['7.0.3', '7.2.0'], ['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'outbound': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'per-ip-shaper': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'policy-offload': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'policyid': {'v_range': [['7.0.3', '']], 'required': True, 'type': 'int'},
                'poolname': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'profile-group': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'profile-protocol-options': {'v_range': [['7.0.3', '7.2.1'], ['7.4.3', '']], 'type': 'str'},
                'profile-type': {'v_range': [['7.0.3', '']], 'choices': ['single', 'group'], 'type': 'str'},
                'replacemsg-override-group': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'rsso': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'schedule': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'send-deny-packet': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'service': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'service-negate': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'session-ttl': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'srcaddr': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'srcaddr-negate': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'srcintf': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'ssh-filter-profile': {'v_range': [['7.0.3', '7.2.1'], ['7.4.3', '']], 'type': 'str'},
                'ssh-policy-redirect': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ssl-mirror': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'ssl-mirror-intf': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'ssl-ssh-profile': {'v_range': [['7.0.3', '7.2.1'], ['7.4.3', '']], 'type': 'str'},
                'status': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'tcp-mss-receiver': {'v_range': [['7.0.3', '']], 'type': 'int'},
                'tcp-mss-sender': {'v_range': [['7.0.3', '']], 'type': 'int'},
                'tcp-session-without-syn': {'v_range': [['7.0.3', '']], 'choices': ['all', 'data-only', 'disable'], 'type': 'str'},
                'timeout-send-rst': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'tos': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'tos-mask': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'tos-negate': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'traffic-shaper': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'traffic-shaper-reverse': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'url-category': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'users': {'v_range': [['7.0.3', '']], 'type': 'raw'},
                'utm-status': {'v_range': [['7.0.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'uuid': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'vlan-cos-fwd': {'v_range': [['7.0.3', '']], 'type': 'int'},
                'vlan-cos-rev': {'v_range': [['7.0.3', '']], 'type': 'int'},
                'vlan-filter': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'voip-profile': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'vpntunnel': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'waf-profile': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'webcache': {'v_range': [['7.0.3', '7.2.0'], ['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'webcache-https': {'v_range': [['7.0.3', '7.2.0'], ['7.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'webfilter-profile': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'webproxy-forward-server': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'webproxy-profile': {'v_range': [['7.0.3', '']], 'type': 'str'},
                'dscp-negate': {'v_range': [['7.0.3', '7.2.1']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'devices': {'v_range': [['7.0.3', '7.2.1']], 'type': 'raw'},
                'dscp-value': {'v_range': [['7.0.3', '7.2.1']], 'type': 'str'},
                'spamfilter-profile': {'v_range': [['7.0.3', '7.2.1']], 'type': 'str'},
                'dscp-match': {'v_range': [['7.0.3', '7.2.1']], 'choices': ['disable', 'enable'], 'type': 'str'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('full crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'pm_config_pblock_firewall_policy6'),
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
