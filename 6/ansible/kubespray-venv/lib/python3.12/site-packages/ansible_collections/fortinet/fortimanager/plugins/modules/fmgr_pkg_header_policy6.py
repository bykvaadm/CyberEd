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
module: fmgr_pkg_header_policy6
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
    pkg:
        description: The parameter (pkg) in requested url.
        type: str
        required: true
    pkg_header_policy6:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            action:
                type: str
                description: Action.
                choices:
                    - 'deny'
                    - 'accept'
                    - 'ipsec'
                    - 'ssl-vpn'
            anti-replay:
                type: str
                description: Deprecated, please rename it to anti_replay. Anti replay.
                choices:
                    - 'disable'
                    - 'enable'
            app-category:
                type: raw
                description: (list or str) Deprecated, please rename it to app_category. App category.
            app-group:
                type: raw
                description: (list or str) Deprecated, please rename it to app_group. App group.
            application:
                type: raw
                description: (list) Application.
            application-charts:
                type: list
                elements: str
                description: Deprecated, please rename it to application_charts. Application charts.
                choices:
                    - 'top10-app'
                    - 'top10-p2p-user'
                    - 'top10-media-user'
            application-list:
                type: raw
                description: (list or str) Deprecated, please rename it to application_list. Application list.
            auto-asic-offload:
                type: str
                description: Deprecated, please rename it to auto_asic_offload. Auto asic offload.
                choices:
                    - 'disable'
                    - 'enable'
            av-profile:
                type: raw
                description: (list or str) Deprecated, please rename it to av_profile. Av profile.
            casi-profile:
                type: raw
                description: (list or str) Deprecated, please rename it to casi_profile. Casi profile.
            cifs-profile:
                type: raw
                description: (list or str) Deprecated, please rename it to cifs_profile. Cifs profile.
            comments:
                type: str
                description: Comments.
            custom-log-fields:
                type: raw
                description: (list or str) Deprecated, please rename it to custom_log_fields. Custom log fields.
            deep-inspection-options:
                type: raw
                description: (list or str) Deprecated, please rename it to deep_inspection_options. Deep inspection options.
            device-detection-portal:
                type: str
                description: Deprecated, please rename it to device_detection_portal. Device detection portal.
                choices:
                    - 'disable'
                    - 'enable'
            devices:
                type: raw
                description: (list or str) Devices.
            diffserv-forward:
                type: str
                description: Deprecated, please rename it to diffserv_forward. Diffserv forward.
                choices:
                    - 'disable'
                    - 'enable'
            diffserv-reverse:
                type: str
                description: Deprecated, please rename it to diffserv_reverse. Diffserv reverse.
                choices:
                    - 'disable'
                    - 'enable'
            diffservcode-forward:
                type: str
                description: Deprecated, please rename it to diffservcode_forward. Diffservcode forward.
            diffservcode-rev:
                type: str
                description: Deprecated, please rename it to diffservcode_rev. Diffservcode rev.
            dlp-sensor:
                type: raw
                description: (list or str) Deprecated, please rename it to dlp_sensor. Dlp sensor.
            dnsfilter-profile:
                type: raw
                description: (list or str) Deprecated, please rename it to dnsfilter_profile. Dnsfilter profile.
            dscp-match:
                type: str
                description: Deprecated, please rename it to dscp_match. Dscp match.
                choices:
                    - 'disable'
                    - 'enable'
            dscp-negate:
                type: str
                description: Deprecated, please rename it to dscp_negate. Dscp negate.
                choices:
                    - 'disable'
                    - 'enable'
            dscp-value:
                type: str
                description: Deprecated, please rename it to dscp_value. Dscp value.
            dsri:
                type: str
                description: Dsri.
                choices:
                    - 'disable'
                    - 'enable'
            dstaddr:
                type: raw
                description: (list or str) Dstaddr.
            dstaddr-negate:
                type: str
                description: Deprecated, please rename it to dstaddr_negate. Dstaddr negate.
                choices:
                    - 'disable'
                    - 'enable'
            dstintf:
                type: raw
                description: (list or str) Dstintf.
            dynamic-profile:
                type: str
                description: Deprecated, please rename it to dynamic_profile. Dynamic profile.
                choices:
                    - 'disable'
                    - 'enable'
            dynamic-profile-access:
                type: list
                elements: str
                description: Deprecated, please rename it to dynamic_profile_access. Dynamic profile access.
                choices:
                    - 'imap'
                    - 'smtp'
                    - 'pop3'
                    - 'http'
                    - 'ftp'
                    - 'im'
                    - 'nntp'
                    - 'imaps'
                    - 'smtps'
                    - 'pop3s'
                    - 'https'
                    - 'ftps'
            dynamic-profile-group:
                type: raw
                description: (list or str) Deprecated, please rename it to dynamic_profile_group. Dynamic profile group.
            email-collection-portal:
                type: str
                description: Deprecated, please rename it to email_collection_portal. Email collection portal.
                choices:
                    - 'disable'
                    - 'enable'
            emailfilter-profile:
                type: raw
                description: (list or str) Deprecated, please rename it to emailfilter_profile. Emailfilter profile.
            firewall-session-dirty:
                type: str
                description: Deprecated, please rename it to firewall_session_dirty. Firewall session dirty.
                choices:
                    - 'check-all'
                    - 'check-new'
            fixedport:
                type: str
                description: Fixedport.
                choices:
                    - 'disable'
                    - 'enable'
            fsae:
                type: str
                description: Fsae.
                choices:
                    - 'disable'
                    - 'enable'
            global-label:
                type: str
                description: Deprecated, please rename it to global_label. Global label.
            groups:
                type: raw
                description: (list or str) Groups.
            http-policy-redirect:
                type: str
                description: Deprecated, please rename it to http_policy_redirect. Http policy redirect.
                choices:
                    - 'disable'
                    - 'enable'
            icap-profile:
                type: raw
                description: (list or str) Deprecated, please rename it to icap_profile. Icap profile.
            identity-based:
                type: str
                description: Deprecated, please rename it to identity_based. Identity based.
                choices:
                    - 'disable'
                    - 'enable'
            identity-based-policy6:
                type: list
                elements: dict
                description: Deprecated, please rename it to identity_based_policy6. Identity based policy6.
                suboptions:
                    action:
                        type: str
                        description: Action.
                        choices:
                            - 'deny'
                            - 'accept'
                    application-list:
                        type: str
                        description: Deprecated, please rename it to application_list. Application list.
                    av-profile:
                        type: str
                        description: Deprecated, please rename it to av_profile. Av profile.
                    deep-inspection-options:
                        type: str
                        description: Deprecated, please rename it to deep_inspection_options. Deep inspection options.
                    devices:
                        type: str
                        description: Devices.
                    dlp-sensor:
                        type: str
                        description: Deprecated, please rename it to dlp_sensor. Dlp sensor.
                    endpoint-compliance:
                        type: str
                        description: Deprecated, please rename it to endpoint_compliance. Endpoint compliance.
                        choices:
                            - 'disable'
                            - 'enable'
                    groups:
                        type: str
                        description: Groups.
                    icap-profile:
                        type: str
                        description: Deprecated, please rename it to icap_profile. Icap profile.
                    id:
                        type: int
                        description: Id.
                    ips-sensor:
                        type: str
                        description: Deprecated, please rename it to ips_sensor. Ips sensor.
                    logtraffic:
                        type: str
                        description: Logtraffic.
                        choices:
                            - 'disable'
                            - 'enable'
                            - 'all'
                            - 'utm'
                    mms-profile:
                        type: str
                        description: Deprecated, please rename it to mms_profile. Mms profile.
                    per-ip-shaper:
                        type: str
                        description: Deprecated, please rename it to per_ip_shaper. Per ip shaper.
                    profile-group:
                        type: str
                        description: Deprecated, please rename it to profile_group. Profile group.
                    profile-protocol-options:
                        type: str
                        description: Deprecated, please rename it to profile_protocol_options. Profile protocol options.
                    profile-type:
                        type: str
                        description: Deprecated, please rename it to profile_type. Profile type.
                        choices:
                            - 'single'
                            - 'group'
                    replacemsg-group:
                        type: str
                        description: Deprecated, please rename it to replacemsg_group. Replacemsg group.
                    schedule:
                        type: str
                        description: Schedule.
                    send-deny-packet:
                        type: str
                        description: Deprecated, please rename it to send_deny_packet. Send deny packet.
                        choices:
                            - 'disable'
                            - 'enable'
                    service:
                        type: str
                        description: Service.
                    service-negate:
                        type: str
                        description: Deprecated, please rename it to service_negate. Service negate.
                        choices:
                            - 'disable'
                            - 'enable'
                    spamfilter-profile:
                        type: str
                        description: Deprecated, please rename it to spamfilter_profile. Spamfilter profile.
                    sslvpn-portal:
                        type: str
                        description: Deprecated, please rename it to sslvpn_portal. Sslvpn portal.
                    sslvpn-realm:
                        type: str
                        description: Deprecated, please rename it to sslvpn_realm. Sslvpn realm.
                    traffic-shaper:
                        type: str
                        description: Deprecated, please rename it to traffic_shaper. Traffic shaper.
                    traffic-shaper-reverse:
                        type: str
                        description: Deprecated, please rename it to traffic_shaper_reverse. Traffic shaper reverse.
                    utm-status:
                        type: str
                        description: Deprecated, please rename it to utm_status. Utm status.
                        choices:
                            - 'disable'
                            - 'enable'
                    voip-profile:
                        type: str
                        description: Deprecated, please rename it to voip_profile. Voip profile.
                    webfilter-profile:
                        type: str
                        description: Deprecated, please rename it to webfilter_profile. Webfilter profile.
            identity-from:
                type: str
                description: Deprecated, please rename it to identity_from. Identity from.
                choices:
                    - 'auth'
                    - 'device'
            inbound:
                type: str
                description: Inbound.
                choices:
                    - 'disable'
                    - 'enable'
            inspection-mode:
                type: str
                description: Deprecated, please rename it to inspection_mode. Inspection mode.
                choices:
                    - 'proxy'
                    - 'flow'
            ippool:
                type: str
                description: Ippool.
                choices:
                    - 'disable'
                    - 'enable'
            ips-sensor:
                type: raw
                description: (list or str) Deprecated, please rename it to ips_sensor. Ips sensor.
            label:
                type: str
                description: Label.
            logtraffic:
                type: str
                description: Logtraffic.
                choices:
                    - 'disable'
                    - 'enable'
                    - 'all'
                    - 'utm'
            logtraffic-start:
                type: str
                description: Deprecated, please rename it to logtraffic_start. Logtraffic start.
                choices:
                    - 'disable'
                    - 'enable'
            mms-profile:
                type: raw
                description: (list or str) Deprecated, please rename it to mms_profile. Mms profile.
            name:
                type: str
                description: Name.
            nat:
                type: str
                description: Nat.
                choices:
                    - 'disable'
                    - 'enable'
            natinbound:
                type: str
                description: Natinbound.
                choices:
                    - 'disable'
                    - 'enable'
            natoutbound:
                type: str
                description: Natoutbound.
                choices:
                    - 'disable'
                    - 'enable'
            np-accelation:
                type: str
                description: Deprecated, please rename it to np_accelation. Np accelation.
                choices:
                    - 'disable'
                    - 'enable'
            np-acceleration:
                type: str
                description: Deprecated, please rename it to np_acceleration. Np acceleration.
                choices:
                    - 'disable'
                    - 'enable'
            outbound:
                type: str
                description: Outbound.
                choices:
                    - 'disable'
                    - 'enable'
            per-ip-shaper:
                type: raw
                description: (list or str) Deprecated, please rename it to per_ip_shaper. Per ip shaper.
            policyid:
                type: int
                description: Policyid.
                required: true
            poolname:
                type: raw
                description: (list or str) Poolname.
            profile-group:
                type: raw
                description: (list or str) Deprecated, please rename it to profile_group. Profile group.
            profile-protocol-options:
                type: raw
                description: (list or str) Deprecated, please rename it to profile_protocol_options. Profile protocol options.
            profile-type:
                type: str
                description: Deprecated, please rename it to profile_type. Profile type.
                choices:
                    - 'single'
                    - 'group'
            replacemsg-group:
                type: raw
                description: (list or str) Deprecated, please rename it to replacemsg_group. Replacemsg group.
            replacemsg-override-group:
                type: raw
                description: (list or str) Deprecated, please rename it to replacemsg_override_group. Replacemsg override group.
            rsso:
                type: str
                description: Rsso.
                choices:
                    - 'disable'
                    - 'enable'
            schedule:
                type: raw
                description: (list or str) Schedule.
            send-deny-packet:
                type: str
                description: Deprecated, please rename it to send_deny_packet. Send deny packet.
                choices:
                    - 'disable'
                    - 'enable'
            service:
                type: raw
                description: (list or str) Service.
            service-negate:
                type: str
                description: Deprecated, please rename it to service_negate. Service negate.
                choices:
                    - 'disable'
                    - 'enable'
            session-ttl:
                type: raw
                description: (int or str) Deprecated, please rename it to session_ttl. Session ttl.
            spamfilter-profile:
                type: raw
                description: (list or str) Deprecated, please rename it to spamfilter_profile. Spamfilter profile.
            srcaddr:
                type: raw
                description: (list or str) Srcaddr.
            srcaddr-negate:
                type: str
                description: Deprecated, please rename it to srcaddr_negate. Srcaddr negate.
                choices:
                    - 'disable'
                    - 'enable'
            srcintf:
                type: raw
                description: (list or str) Srcintf.
            ssh-filter-profile:
                type: raw
                description: (list or str) Deprecated, please rename it to ssh_filter_profile. Ssh filter profile.
            ssh-policy-redirect:
                type: str
                description: Deprecated, please rename it to ssh_policy_redirect. Ssh policy redirect.
                choices:
                    - 'disable'
                    - 'enable'
            ssl-mirror:
                type: str
                description: Deprecated, please rename it to ssl_mirror. Ssl mirror.
                choices:
                    - 'disable'
                    - 'enable'
            ssl-mirror-intf:
                type: raw
                description: (list or str) Deprecated, please rename it to ssl_mirror_intf. Ssl mirror intf.
            ssl-ssh-profile:
                type: raw
                description: (list or str) Deprecated, please rename it to ssl_ssh_profile. Ssl ssh profile.
            sslvpn-auth:
                type: str
                description: Deprecated, please rename it to sslvpn_auth. Sslvpn auth.
                choices:
                    - 'any'
                    - 'local'
                    - 'radius'
                    - 'ldap'
                    - 'tacacs+'
            sslvpn-ccert:
                type: str
                description: Deprecated, please rename it to sslvpn_ccert. Sslvpn ccert.
                choices:
                    - 'disable'
                    - 'enable'
            sslvpn-cipher:
                type: str
                description: Deprecated, please rename it to sslvpn_cipher. Sslvpn cipher.
                choices:
                    - 'any'
                    - 'high'
                    - 'medium'
            status:
                type: str
                description: Status.
                choices:
                    - 'disable'
                    - 'enable'
            tags:
                type: raw
                description: (list or str) Tags.
            tcp-mss-receiver:
                type: int
                description: Deprecated, please rename it to tcp_mss_receiver. Tcp mss receiver.
            tcp-mss-sender:
                type: int
                description: Deprecated, please rename it to tcp_mss_sender. Tcp mss sender.
            tcp-session-without-syn:
                type: str
                description: Deprecated, please rename it to tcp_session_without_syn. Tcp session without syn.
                choices:
                    - 'all'
                    - 'data-only'
                    - 'disable'
            timeout-send-rst:
                type: str
                description: Deprecated, please rename it to timeout_send_rst. Timeout send rst.
                choices:
                    - 'disable'
                    - 'enable'
            tos:
                type: str
                description: Tos.
            tos-mask:
                type: str
                description: Deprecated, please rename it to tos_mask. Tos mask.
            tos-negate:
                type: str
                description: Deprecated, please rename it to tos_negate. Tos negate.
                choices:
                    - 'disable'
                    - 'enable'
            traffic-shaper:
                type: raw
                description: (list or str) Deprecated, please rename it to traffic_shaper. Traffic shaper.
            traffic-shaper-reverse:
                type: raw
                description: (list or str) Deprecated, please rename it to traffic_shaper_reverse. Traffic shaper reverse.
            url-category:
                type: raw
                description: (list or str) Deprecated, please rename it to url_category. Url category.
            users:
                type: raw
                description: (list or str) Users.
            utm-inspection-mode:
                type: str
                description: Deprecated, please rename it to utm_inspection_mode. Utm inspection mode.
                choices:
                    - 'proxy'
                    - 'flow'
            utm-status:
                type: str
                description: Deprecated, please rename it to utm_status. Utm status.
                choices:
                    - 'disable'
                    - 'enable'
            uuid:
                type: str
                description: Uuid.
            vlan-cos-fwd:
                type: int
                description: Deprecated, please rename it to vlan_cos_fwd. Vlan cos fwd.
            vlan-cos-rev:
                type: int
                description: Deprecated, please rename it to vlan_cos_rev. Vlan cos rev.
            vlan-filter:
                type: str
                description: Deprecated, please rename it to vlan_filter. Vlan filter.
            voip-profile:
                type: raw
                description: (list or str) Deprecated, please rename it to voip_profile. Voip profile.
            vpntunnel:
                type: raw
                description: (list or str) Vpntunnel.
            webfilter-profile:
                type: raw
                description: (list or str) Deprecated, please rename it to webfilter_profile. Webfilter profile.
            waf-profile:
                type: raw
                description: (list or str) Deprecated, please rename it to waf_profile. Waf profile.
            webcache:
                type: str
                description: Webcache.
                choices:
                    - 'disable'
                    - 'enable'
            webcache-https:
                type: str
                description: Deprecated, please rename it to webcache_https. Webcache https.
                choices:
                    - 'disable'
                    - 'enable'
            webproxy-forward-server:
                type: raw
                description: (list or str) Deprecated, please rename it to webproxy_forward_server. Webproxy forward server.
            webproxy-profile:
                type: raw
                description: (list or str) Deprecated, please rename it to webproxy_profile. Webproxy profile.
            fsso-groups:
                type: raw
                description: (list or str) Deprecated, please rename it to fsso_groups. Fsso groups.
            decrypted-traffic-mirror:
                type: raw
                description: (list or str) Deprecated, please rename it to decrypted_traffic_mirror. Decrypted traffic mirror.
            file-filter-profile:
                type: raw
                description: (list or str) Deprecated, please rename it to file_filter_profile. File filter profile.
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
    - name: Configure IPv6 header policies.
      fortinet.fortimanager.fmgr_pkg_header_policy6:
        bypass_validation: false
        pkg: ansible
        state: present
        pkg_header_policy6:
          action: accept # <value in [deny, accept, ipsec, ...]>
          comments: ansible-comment
          dstaddr: gall
          dstintf: any
          name: ansible-test2-header
          policyid: 1073741827 # must larger than 2^30(1074741824), since header/footer policy is a special policy
          schedule: galways
          service: gALL
          srcaddr: gall
          srcintf: any
          status: enable

- name: Gathering fortimanager facts
  hosts: fortimanagers
  gather_facts: false
  connection: httpapi
  vars:
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_httpapi_port: 443
  tasks:
    - name: Retrieve all the IPv6 header policies
      fortinet.fortimanager.fmgr_fact:
        facts:
          selector: "pkg_header_policy6"
          params:
            pkg: "ansible"
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
        '/pm/config/global/pkg/{pkg}/global/header/policy6'
    ]

    perobject_jrpc_urls = [
        '/pm/config/global/pkg/{pkg}/global/header/policy6/{policy6}'
    ]

    url_params = ['pkg']
    module_primary_key = 'policyid'
    module_arg_spec = {
        'pkg': {'required': True, 'type': 'str'},
        'pkg_header_policy6': {
            'type': 'dict',
            'v_range': [['6.0.0', '']],
            'options': {
                'action': {'choices': ['deny', 'accept', 'ipsec', 'ssl-vpn'], 'type': 'str'},
                'anti-replay': {'choices': ['disable', 'enable'], 'type': 'str'},
                'app-category': {'type': 'raw'},
                'app-group': {'type': 'raw'},
                'application': {'type': 'raw'},
                'application-charts': {'type': 'list', 'choices': ['top10-app', 'top10-p2p-user', 'top10-media-user'], 'elements': 'str'},
                'application-list': {'type': 'raw'},
                'auto-asic-offload': {'choices': ['disable', 'enable'], 'type': 'str'},
                'av-profile': {'type': 'raw'},
                'casi-profile': {'type': 'raw'},
                'cifs-profile': {'type': 'raw'},
                'comments': {'type': 'str'},
                'custom-log-fields': {'type': 'raw'},
                'deep-inspection-options': {'type': 'raw'},
                'device-detection-portal': {'choices': ['disable', 'enable'], 'type': 'str'},
                'devices': {'type': 'raw'},
                'diffserv-forward': {'choices': ['disable', 'enable'], 'type': 'str'},
                'diffserv-reverse': {'choices': ['disable', 'enable'], 'type': 'str'},
                'diffservcode-forward': {'type': 'str'},
                'diffservcode-rev': {'type': 'str'},
                'dlp-sensor': {'type': 'raw'},
                'dnsfilter-profile': {'type': 'raw'},
                'dscp-match': {'choices': ['disable', 'enable'], 'type': 'str'},
                'dscp-negate': {'choices': ['disable', 'enable'], 'type': 'str'},
                'dscp-value': {'type': 'str'},
                'dsri': {'choices': ['disable', 'enable'], 'type': 'str'},
                'dstaddr': {'type': 'raw'},
                'dstaddr-negate': {'choices': ['disable', 'enable'], 'type': 'str'},
                'dstintf': {'type': 'raw'},
                'dynamic-profile': {'choices': ['disable', 'enable'], 'type': 'str'},
                'dynamic-profile-access': {
                    'type': 'list',
                    'choices': ['imap', 'smtp', 'pop3', 'http', 'ftp', 'im', 'nntp', 'imaps', 'smtps', 'pop3s', 'https', 'ftps'],
                    'elements': 'str'
                },
                'dynamic-profile-group': {'type': 'raw'},
                'email-collection-portal': {'choices': ['disable', 'enable'], 'type': 'str'},
                'emailfilter-profile': {'type': 'raw'},
                'firewall-session-dirty': {'choices': ['check-all', 'check-new'], 'type': 'str'},
                'fixedport': {'choices': ['disable', 'enable'], 'type': 'str'},
                'fsae': {'choices': ['disable', 'enable'], 'type': 'str'},
                'global-label': {'type': 'str'},
                'groups': {'type': 'raw'},
                'http-policy-redirect': {'choices': ['disable', 'enable'], 'type': 'str'},
                'icap-profile': {'type': 'raw'},
                'identity-based': {'choices': ['disable', 'enable'], 'type': 'str'},
                'identity-based-policy6': {
                    'v_range': [['6.0.0', '6.2.0']],
                    'type': 'list',
                    'options': {
                        'action': {'v_range': [['6.0.0', '6.2.0']], 'choices': ['deny', 'accept'], 'type': 'str'},
                        'application-list': {'v_range': [['6.0.0', '6.2.0']], 'type': 'str'},
                        'av-profile': {'v_range': [['6.0.0', '6.2.0']], 'type': 'str'},
                        'deep-inspection-options': {'v_range': [['6.0.0', '6.2.0']], 'type': 'str'},
                        'devices': {'v_range': [['6.0.0', '6.2.0']], 'type': 'str'},
                        'dlp-sensor': {'v_range': [['6.0.0', '6.2.0']], 'type': 'str'},
                        'endpoint-compliance': {'v_range': [['6.0.0', '6.2.0']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'groups': {'v_range': [['6.0.0', '6.2.0']], 'type': 'str'},
                        'icap-profile': {'v_range': [['6.0.0', '6.2.0']], 'type': 'str'},
                        'id': {'v_range': [['6.0.0', '6.2.0']], 'type': 'int'},
                        'ips-sensor': {'v_range': [['6.0.0', '6.2.0']], 'type': 'str'},
                        'logtraffic': {'v_range': [['6.0.0', '6.2.0']], 'choices': ['disable', 'enable', 'all', 'utm'], 'type': 'str'},
                        'mms-profile': {'v_range': [['6.0.0', '6.2.0']], 'type': 'str'},
                        'per-ip-shaper': {'v_range': [['6.0.0', '6.2.0']], 'type': 'str'},
                        'profile-group': {'v_range': [['6.0.0', '6.2.0']], 'type': 'str'},
                        'profile-protocol-options': {'v_range': [['6.0.0', '6.2.0']], 'type': 'str'},
                        'profile-type': {'v_range': [['6.0.0', '6.2.0']], 'choices': ['single', 'group'], 'type': 'str'},
                        'replacemsg-group': {'v_range': [['6.0.0', '6.2.0']], 'type': 'str'},
                        'schedule': {'v_range': [['6.0.0', '6.2.0']], 'type': 'str'},
                        'send-deny-packet': {'v_range': [['6.0.0', '6.2.0']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'service': {'v_range': [['6.0.0', '6.2.0']], 'type': 'str'},
                        'service-negate': {'v_range': [['6.0.0', '6.2.0']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'spamfilter-profile': {'v_range': [['6.0.0', '6.2.0']], 'type': 'str'},
                        'sslvpn-portal': {'v_range': [['6.0.0', '6.2.0']], 'type': 'str'},
                        'sslvpn-realm': {'v_range': [['6.0.0', '6.2.0']], 'type': 'str'},
                        'traffic-shaper': {'v_range': [['6.0.0', '6.2.0']], 'type': 'str'},
                        'traffic-shaper-reverse': {'v_range': [['6.0.0', '6.2.0']], 'type': 'str'},
                        'utm-status': {'v_range': [['6.0.0', '6.2.0']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'voip-profile': {'v_range': [['6.0.0', '6.2.0']], 'type': 'str'},
                        'webfilter-profile': {'v_range': [['6.0.0', '6.2.0']], 'type': 'str'}
                    },
                    'elements': 'dict'
                },
                'identity-from': {'choices': ['auth', 'device'], 'type': 'str'},
                'inbound': {'choices': ['disable', 'enable'], 'type': 'str'},
                'inspection-mode': {'choices': ['proxy', 'flow'], 'type': 'str'},
                'ippool': {'choices': ['disable', 'enable'], 'type': 'str'},
                'ips-sensor': {'type': 'raw'},
                'label': {'type': 'str'},
                'logtraffic': {'choices': ['disable', 'enable', 'all', 'utm'], 'type': 'str'},
                'logtraffic-start': {'choices': ['disable', 'enable'], 'type': 'str'},
                'mms-profile': {'type': 'raw'},
                'name': {'type': 'str'},
                'nat': {'choices': ['disable', 'enable'], 'type': 'str'},
                'natinbound': {'choices': ['disable', 'enable'], 'type': 'str'},
                'natoutbound': {'choices': ['disable', 'enable'], 'type': 'str'},
                'np-accelation': {'choices': ['disable', 'enable'], 'type': 'str'},
                'np-acceleration': {'choices': ['disable', 'enable'], 'type': 'str'},
                'outbound': {'choices': ['disable', 'enable'], 'type': 'str'},
                'per-ip-shaper': {'type': 'raw'},
                'policyid': {'required': True, 'type': 'int'},
                'poolname': {'type': 'raw'},
                'profile-group': {'type': 'raw'},
                'profile-protocol-options': {'type': 'raw'},
                'profile-type': {'choices': ['single', 'group'], 'type': 'str'},
                'replacemsg-group': {'type': 'raw'},
                'replacemsg-override-group': {'type': 'raw'},
                'rsso': {'choices': ['disable', 'enable'], 'type': 'str'},
                'schedule': {'type': 'raw'},
                'send-deny-packet': {'choices': ['disable', 'enable'], 'type': 'str'},
                'service': {'type': 'raw'},
                'service-negate': {'choices': ['disable', 'enable'], 'type': 'str'},
                'session-ttl': {'type': 'raw'},
                'spamfilter-profile': {'type': 'raw'},
                'srcaddr': {'type': 'raw'},
                'srcaddr-negate': {'choices': ['disable', 'enable'], 'type': 'str'},
                'srcintf': {'type': 'raw'},
                'ssh-filter-profile': {'type': 'raw'},
                'ssh-policy-redirect': {'choices': ['disable', 'enable'], 'type': 'str'},
                'ssl-mirror': {'choices': ['disable', 'enable'], 'type': 'str'},
                'ssl-mirror-intf': {'type': 'raw'},
                'ssl-ssh-profile': {'type': 'raw'},
                'sslvpn-auth': {'choices': ['any', 'local', 'radius', 'ldap', 'tacacs+'], 'type': 'str'},
                'sslvpn-ccert': {'choices': ['disable', 'enable'], 'type': 'str'},
                'sslvpn-cipher': {'choices': ['any', 'high', 'medium'], 'type': 'str'},
                'status': {'choices': ['disable', 'enable'], 'type': 'str'},
                'tags': {'type': 'raw'},
                'tcp-mss-receiver': {'type': 'int'},
                'tcp-mss-sender': {'type': 'int'},
                'tcp-session-without-syn': {'choices': ['all', 'data-only', 'disable'], 'type': 'str'},
                'timeout-send-rst': {'choices': ['disable', 'enable'], 'type': 'str'},
                'tos': {'type': 'str'},
                'tos-mask': {'type': 'str'},
                'tos-negate': {'choices': ['disable', 'enable'], 'type': 'str'},
                'traffic-shaper': {'type': 'raw'},
                'traffic-shaper-reverse': {'type': 'raw'},
                'url-category': {'type': 'raw'},
                'users': {'type': 'raw'},
                'utm-inspection-mode': {'choices': ['proxy', 'flow'], 'type': 'str'},
                'utm-status': {'choices': ['disable', 'enable'], 'type': 'str'},
                'uuid': {'type': 'str'},
                'vlan-cos-fwd': {'type': 'int'},
                'vlan-cos-rev': {'type': 'int'},
                'vlan-filter': {'type': 'str'},
                'voip-profile': {'type': 'raw'},
                'vpntunnel': {'type': 'raw'},
                'webfilter-profile': {'type': 'raw'},
                'waf-profile': {'v_range': [['6.2.1', '']], 'type': 'raw'},
                'webcache': {'v_range': [['6.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'webcache-https': {'v_range': [['6.2.1', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'webproxy-forward-server': {'v_range': [['6.2.1', '']], 'type': 'raw'},
                'webproxy-profile': {'v_range': [['6.2.1', '']], 'type': 'raw'},
                'fsso-groups': {'v_range': [['6.2.3', '']], 'type': 'raw'},
                'decrypted-traffic-mirror': {'v_range': [['6.4.0', '']], 'type': 'raw'},
                'file-filter-profile': {'v_range': [['6.4.1', '']], 'type': 'raw'},
                'cgn-log-server-grp': {'v_range': [['6.2.7', '6.2.12'], ['6.4.3', '']], 'type': 'str'},
                'policy-offload': {'v_range': [['6.2.7', '6.2.12'], ['6.4.3', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                '_policy_block': {'v_range': [['7.2.2', '']], 'type': 'int'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('full crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = [
        {
            'attribute_path': ['pkg_header_policy6', 'policyid'],
            'lambda': 'int($) >= 1073741824',
            'fail_action': 'warn',
            'hint_message': 'policyid should be larger than 2^30, i.e. 1073741824, otherwise it will be ignored.'
        }
    ]

    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'pkg_header_policy6'),
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
