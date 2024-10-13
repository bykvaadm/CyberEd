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
module: fmgr_system_npu_nputcam_data
short_description: Data fields of TCAM.
description:
    - This module is able to configure a FortiManager device.
    - Examples include all parameters and values which need to be adjusted to data sources before usage.

version_added: "2.4.0"
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
    adom:
        description: The parameter (adom) in requested url.
        type: str
        required: true
    npu-tcam:
        description: Deprecated, please use "npu_tcam"
        type: str
    npu_tcam:
        description: The parameter (npu-tcam) in requested url.
        type: str
    system_npu_nputcam_data:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            df:
                type: str
                description: Tcam data ip flag df.
                choices:
                    - 'disable'
                    - 'enable'
            dstip:
                type: str
                description: Tcam data dst ipv4 address.
            dstipv6:
                type: str
                description: Tcam data dst ipv6 address.
            dstmac:
                type: str
                description: Tcam data dst macaddr.
            dstport:
                type: int
                description: Tcam data L4 dst port.
            ethertype:
                type: str
                description: Tcam data ethertype.
            ext-tag:
                type: str
                description: Deprecated, please rename it to ext_tag. Tcam data extension tag.
                choices:
                    - 'disable'
                    - 'enable'
            frag-off:
                type: int
                description: Deprecated, please rename it to frag_off. Tcam data ip flag fragment offset.
            gen-buf-cnt:
                type: int
                description: Deprecated, please rename it to gen_buf_cnt. Tcam data gen info buffer count.
            gen-iv:
                type: str
                description: Deprecated, please rename it to gen_iv. Tcam data gen info iv.
                choices:
                    - 'invalid'
                    - 'valid'
            gen-l3-flags:
                type: int
                description: Deprecated, please rename it to gen_l3_flags. Tcam data gen info L3 flags.
            gen-l4-flags:
                type: int
                description: Deprecated, please rename it to gen_l4_flags. Tcam data gen info L4 flags.
            gen-pkt-ctrl:
                type: int
                description: Deprecated, please rename it to gen_pkt_ctrl. Tcam data gen info packet control.
            gen-pri:
                type: int
                description: Deprecated, please rename it to gen_pri. Tcam data gen info priority.
            gen-pri-v:
                type: str
                description: Deprecated, please rename it to gen_pri_v. Tcam data gen info priority valid.
                choices:
                    - 'invalid'
                    - 'valid'
            gen-tv:
                type: str
                description: Deprecated, please rename it to gen_tv. Tcam data gen info tv.
                choices:
                    - 'invalid'
                    - 'valid'
            ihl:
                type: int
                description: Tcam data ipv4 IHL.
            ip4-id:
                type: int
                description: Deprecated, please rename it to ip4_id. Tcam data ipv4 id.
            ip6-fl:
                type: int
                description: Deprecated, please rename it to ip6_fl. Tcam data ipv6 flow label.
            ipver:
                type: int
                description: Tcam data ip header version.
            l4-wd10:
                type: int
                description: Deprecated, please rename it to l4_wd10. Tcam data L4 word10.
            l4-wd11:
                type: int
                description: Deprecated, please rename it to l4_wd11. Tcam data L4 word11.
            l4-wd8:
                type: int
                description: Deprecated, please rename it to l4_wd8. Tcam data L4 word8.
            l4-wd9:
                type: int
                description: Deprecated, please rename it to l4_wd9. Tcam data L4 word9.
            mf:
                type: str
                description: Tcam data ip flag mf.
                choices:
                    - 'disable'
                    - 'enable'
            protocol:
                type: int
                description: Tcam data ip protocol.
            slink:
                type: int
                description: Tcam data sublink.
            smac-change:
                type: str
                description: Deprecated, please rename it to smac_change. Tcam data source MAC change.
                choices:
                    - 'disable'
                    - 'enable'
            sp:
                type: int
                description: Tcam data source port.
            src-cfi:
                type: str
                description: Deprecated, please rename it to src_cfi. Tcam data source cfi.
                choices:
                    - 'disable'
                    - 'enable'
            src-prio:
                type: int
                description: Deprecated, please rename it to src_prio. Tcam data source priority.
            src-updt:
                type: str
                description: Deprecated, please rename it to src_updt. Tcam data source update.
                choices:
                    - 'disable'
                    - 'enable'
            srcip:
                type: str
                description: Tcam data src ipv4 address.
            srcipv6:
                type: str
                description: Tcam data src ipv6 address.
            srcmac:
                type: str
                description: Tcam data src macaddr.
            srcport:
                type: int
                description: Tcam data L4 src port.
            svid:
                type: int
                description: Tcam data source vid.
            tcp-ack:
                type: str
                description: Deprecated, please rename it to tcp_ack. Tcam data tcp flag ack.
                choices:
                    - 'disable'
                    - 'enable'
            tcp-cwr:
                type: str
                description: Deprecated, please rename it to tcp_cwr. Tcam data tcp flag cwr.
                choices:
                    - 'disable'
                    - 'enable'
            tcp-ece:
                type: str
                description: Deprecated, please rename it to tcp_ece. Tcam data tcp flag ece.
                choices:
                    - 'disable'
                    - 'enable'
            tcp-fin:
                type: str
                description: Deprecated, please rename it to tcp_fin. Tcam data tcp flag fin.
                choices:
                    - 'disable'
                    - 'enable'
            tcp-push:
                type: str
                description: Deprecated, please rename it to tcp_push. Tcam data tcp flag push.
                choices:
                    - 'disable'
                    - 'enable'
            tcp-rst:
                type: str
                description: Deprecated, please rename it to tcp_rst. Tcam data tcp flag rst.
                choices:
                    - 'disable'
                    - 'enable'
            tcp-syn:
                type: str
                description: Deprecated, please rename it to tcp_syn. Tcam data tcp flag syn.
                choices:
                    - 'disable'
                    - 'enable'
            tcp-urg:
                type: str
                description: Deprecated, please rename it to tcp_urg. Tcam data tcp flag urg.
                choices:
                    - 'disable'
                    - 'enable'
            tgt-cfi:
                type: str
                description: Deprecated, please rename it to tgt_cfi. Tcam data target cfi.
                choices:
                    - 'disable'
                    - 'enable'
            tgt-prio:
                type: int
                description: Deprecated, please rename it to tgt_prio. Tcam data target priority.
            tgt-updt:
                type: str
                description: Deprecated, please rename it to tgt_updt. Tcam data target port update.
                choices:
                    - 'disable'
                    - 'enable'
            tgt-v:
                type: str
                description: Deprecated, please rename it to tgt_v. Tcam data target valid.
                choices:
                    - 'invalid'
                    - 'valid'
            tos:
                type: int
                description: Tcam data ip tos.
            tp:
                type: int
                description: Tcam data target port.
            ttl:
                type: int
                description: Tcam data ip ttl.
            tvid:
                type: int
                description: Tcam data target vid.
            vdid:
                type: int
                description: Tcam data vdom id.
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
    - name: Data fields of TCAM.
      fortinet.fortimanager.fmgr_system_npu_nputcam_data:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        adom: <your own value>
        npu_tcam: <your own value>
        system_npu_nputcam_data:
          df: <value in [disable, enable]>
          dstip: <string>
          dstipv6: <string>
          dstmac: <string>
          dstport: <integer>
          ethertype: <string>
          ext_tag: <value in [disable, enable]>
          frag_off: <integer>
          gen_buf_cnt: <integer>
          gen_iv: <value in [invalid, valid]>
          gen_l3_flags: <integer>
          gen_l4_flags: <integer>
          gen_pkt_ctrl: <integer>
          gen_pri: <integer>
          gen_pri_v: <value in [invalid, valid]>
          gen_tv: <value in [invalid, valid]>
          ihl: <integer>
          ip4_id: <integer>
          ip6_fl: <integer>
          ipver: <integer>
          l4_wd10: <integer>
          l4_wd11: <integer>
          l4_wd8: <integer>
          l4_wd9: <integer>
          mf: <value in [disable, enable]>
          protocol: <integer>
          slink: <integer>
          smac_change: <value in [disable, enable]>
          sp: <integer>
          src_cfi: <value in [disable, enable]>
          src_prio: <integer>
          src_updt: <value in [disable, enable]>
          srcip: <string>
          srcipv6: <string>
          srcmac: <string>
          srcport: <integer>
          svid: <integer>
          tcp_ack: <value in [disable, enable]>
          tcp_cwr: <value in [disable, enable]>
          tcp_ece: <value in [disable, enable]>
          tcp_fin: <value in [disable, enable]>
          tcp_push: <value in [disable, enable]>
          tcp_rst: <value in [disable, enable]>
          tcp_syn: <value in [disable, enable]>
          tcp_urg: <value in [disable, enable]>
          tgt_cfi: <value in [disable, enable]>
          tgt_prio: <integer>
          tgt_updt: <value in [disable, enable]>
          tgt_v: <value in [invalid, valid]>
          tos: <integer>
          tp: <integer>
          ttl: <integer>
          tvid: <integer>
          vdid: <integer>
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
        '/pm/config/adom/{adom}/obj/system/npu/npu-tcam/{npu-tcam}/data',
        '/pm/config/global/obj/system/npu/npu-tcam/{npu-tcam}/data'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/system/npu/npu-tcam/{npu-tcam}/data/{data}',
        '/pm/config/global/obj/system/npu/npu-tcam/{npu-tcam}/data/{data}'
    ]

    url_params = ['adom', 'npu-tcam']
    module_primary_key = None
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'npu-tcam': {'type': 'str', 'api_name': 'npu_tcam'},
        'npu_tcam': {'type': 'str'},
        'system_npu_nputcam_data': {
            'type': 'dict',
            'v_range': [['7.4.2', '']],
            'options': {
                'df': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'dstip': {'v_range': [['7.4.2', '']], 'type': 'str'},
                'dstipv6': {'v_range': [['7.4.2', '']], 'type': 'str'},
                'dstmac': {'v_range': [['7.4.2', '']], 'type': 'str'},
                'dstport': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'ethertype': {'v_range': [['7.4.2', '']], 'type': 'str'},
                'ext-tag': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'frag-off': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'gen-buf-cnt': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'gen-iv': {'v_range': [['7.4.2', '']], 'choices': ['invalid', 'valid'], 'type': 'str'},
                'gen-l3-flags': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'gen-l4-flags': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'gen-pkt-ctrl': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'gen-pri': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'gen-pri-v': {'v_range': [['7.4.2', '']], 'choices': ['invalid', 'valid'], 'type': 'str'},
                'gen-tv': {'v_range': [['7.4.2', '']], 'choices': ['invalid', 'valid'], 'type': 'str'},
                'ihl': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'ip4-id': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'ip6-fl': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'ipver': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'l4-wd10': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'l4-wd11': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'l4-wd8': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'l4-wd9': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'mf': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'protocol': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'slink': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'smac-change': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'sp': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'src-cfi': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'src-prio': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'src-updt': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'srcip': {'v_range': [['7.4.2', '']], 'type': 'str'},
                'srcipv6': {'v_range': [['7.4.2', '']], 'type': 'str'},
                'srcmac': {'v_range': [['7.4.2', '']], 'type': 'str'},
                'srcport': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'svid': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'tcp-ack': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'tcp-cwr': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'tcp-ece': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'tcp-fin': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'tcp-push': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'tcp-rst': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'tcp-syn': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'tcp-urg': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'tgt-cfi': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'tgt-prio': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'tgt-updt': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'tgt-v': {'v_range': [['7.4.2', '']], 'choices': ['invalid', 'valid'], 'type': 'str'},
                'tos': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'tp': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'ttl': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'tvid': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'vdid': {'v_range': [['7.4.2', '']], 'type': 'int'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('partial crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'system_npu_nputcam_data'),
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
