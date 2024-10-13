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
module: fmgr_system_npu_nputcam_tact
short_description: Target action of TCAM.
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
    system_npu_nputcam_tact:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            act:
                type: int
                description: Tcam tact act.
            act-v:
                type: str
                description: Deprecated, please rename it to act_v. Enable to set tact act.
                choices:
                    - 'disable'
                    - 'enable'
            fmtuv4-s:
                type: int
                description: Deprecated, please rename it to fmtuv4_s. Tcam tact fmtuv4-s.
            fmtuv4-s-v:
                type: str
                description: Deprecated, please rename it to fmtuv4_s_v. Enable to set tact fmtuv4-s.
                choices:
                    - 'disable'
                    - 'enable'
            fmtuv6-s:
                type: int
                description: Deprecated, please rename it to fmtuv6_s. Tcam tact fmtuv6-s.
            fmtuv6-s-v:
                type: str
                description: Deprecated, please rename it to fmtuv6_s_v. Enable to set tact fmtuv6-s.
                choices:
                    - 'disable'
                    - 'enable'
            lnkid:
                type: int
                description: Tcam tact lnkid.
            lnkid-v:
                type: str
                description: Deprecated, please rename it to lnkid_v. Enable to set tact lnkid.
                choices:
                    - 'disable'
                    - 'enable'
            mac-id:
                type: int
                description: Deprecated, please rename it to mac_id. Tcam tact mac-id.
            mac-id-v:
                type: str
                description: Deprecated, please rename it to mac_id_v. Enable to set tact mac-id.
                choices:
                    - 'disable'
                    - 'enable'
            mss-t:
                type: int
                description: Deprecated, please rename it to mss_t. Tcam tact mss.
            mss-t-v:
                type: str
                description: Deprecated, please rename it to mss_t_v. Enable to set tact mss.
                choices:
                    - 'disable'
                    - 'enable'
            mtuv4:
                type: int
                description: Tcam tact mtuv4.
            mtuv4-v:
                type: str
                description: Deprecated, please rename it to mtuv4_v. Enable to set tact mtuv4.
                choices:
                    - 'disable'
                    - 'enable'
            mtuv6:
                type: int
                description: Tcam tact mtuv6.
            mtuv6-v:
                type: str
                description: Deprecated, please rename it to mtuv6_v. Enable to set tact mtuv6.
                choices:
                    - 'disable'
                    - 'enable'
            slif-act:
                type: int
                description: Deprecated, please rename it to slif_act. Tcam tact slif-act.
            slif-act-v:
                type: str
                description: Deprecated, please rename it to slif_act_v. Enable to set tact slif-act.
                choices:
                    - 'disable'
                    - 'enable'
            sublnkid:
                type: int
                description: Tcam tact sublnkid.
            sublnkid-v:
                type: str
                description: Deprecated, please rename it to sublnkid_v. Enable to set tact sublnkid.
                choices:
                    - 'disable'
                    - 'enable'
            tgtv-act:
                type: int
                description: Deprecated, please rename it to tgtv_act. Tcam tact tgtv-act.
            tgtv-act-v:
                type: str
                description: Deprecated, please rename it to tgtv_act_v. Enable to set tact tgtv-act.
                choices:
                    - 'disable'
                    - 'enable'
            tlif-act:
                type: int
                description: Deprecated, please rename it to tlif_act. Tcam tact tlif-act.
            tlif-act-v:
                type: str
                description: Deprecated, please rename it to tlif_act_v. Enable to set tact tlif-act.
                choices:
                    - 'disable'
                    - 'enable'
            tpeid:
                type: int
                description: Tcam tact tpeid.
            tpeid-v:
                type: str
                description: Deprecated, please rename it to tpeid_v. Enable to set tact tpeid.
                choices:
                    - 'disable'
                    - 'enable'
            v6fe:
                type: int
                description: Tcam tact v6fe.
            v6fe-v:
                type: str
                description: Deprecated, please rename it to v6fe_v. Enable to set tact v6fe.
                choices:
                    - 'disable'
                    - 'enable'
            vep-en-v:
                type: str
                description: Deprecated, please rename it to vep_en_v. Enable to set tact vep-en.
                choices:
                    - 'disable'
                    - 'enable'
            vep-slid:
                type: int
                description: Deprecated, please rename it to vep_slid. Tcam tact vep_slid.
            vep-slid-v:
                type: str
                description: Deprecated, please rename it to vep_slid_v. Enable to set tact vep-slid.
                choices:
                    - 'disable'
                    - 'enable'
            vep_en:
                type: int
                description: Tcam tact vep_en.
            xlt-lif:
                type: int
                description: Deprecated, please rename it to xlt_lif. Tcam tact xlt-lif.
            xlt-lif-v:
                type: str
                description: Deprecated, please rename it to xlt_lif_v. Enable to set tact xlt-lif.
                choices:
                    - 'disable'
                    - 'enable'
            xlt-vid:
                type: int
                description: Deprecated, please rename it to xlt_vid. Tcam tact xlt-vid.
            xlt-vid-v:
                type: str
                description: Deprecated, please rename it to xlt_vid_v. Enable to set tact xlt-vid.
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
    - name: Target action of TCAM.
      fortinet.fortimanager.fmgr_system_npu_nputcam_tact:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        adom: <your own value>
        npu_tcam: <your own value>
        system_npu_nputcam_tact:
          act: <integer>
          act_v: <value in [disable, enable]>
          fmtuv4_s: <integer>
          fmtuv4_s_v: <value in [disable, enable]>
          fmtuv6_s: <integer>
          fmtuv6_s_v: <value in [disable, enable]>
          lnkid: <integer>
          lnkid_v: <value in [disable, enable]>
          mac_id: <integer>
          mac_id_v: <value in [disable, enable]>
          mss_t: <integer>
          mss_t_v: <value in [disable, enable]>
          mtuv4: <integer>
          mtuv4_v: <value in [disable, enable]>
          mtuv6: <integer>
          mtuv6_v: <value in [disable, enable]>
          slif_act: <integer>
          slif_act_v: <value in [disable, enable]>
          sublnkid: <integer>
          sublnkid_v: <value in [disable, enable]>
          tgtv_act: <integer>
          tgtv_act_v: <value in [disable, enable]>
          tlif_act: <integer>
          tlif_act_v: <value in [disable, enable]>
          tpeid: <integer>
          tpeid_v: <value in [disable, enable]>
          v6fe: <integer>
          v6fe_v: <value in [disable, enable]>
          vep_en_v: <value in [disable, enable]>
          vep_slid: <integer>
          vep_slid_v: <value in [disable, enable]>
          vep_en: <integer>
          xlt_lif: <integer>
          xlt_lif_v: <value in [disable, enable]>
          xlt_vid: <integer>
          xlt_vid_v: <value in [disable, enable]>
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
        '/pm/config/adom/{adom}/obj/system/npu/npu-tcam/{npu-tcam}/tact',
        '/pm/config/global/obj/system/npu/npu-tcam/{npu-tcam}/tact'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/system/npu/npu-tcam/{npu-tcam}/tact/{tact}',
        '/pm/config/global/obj/system/npu/npu-tcam/{npu-tcam}/tact/{tact}'
    ]

    url_params = ['adom', 'npu-tcam']
    module_primary_key = None
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'npu-tcam': {'type': 'str', 'api_name': 'npu_tcam'},
        'npu_tcam': {'type': 'str'},
        'system_npu_nputcam_tact': {
            'type': 'dict',
            'v_range': [['7.4.2', '']],
            'options': {
                'act': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'act-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'fmtuv4-s': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'fmtuv4-s-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'fmtuv6-s': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'fmtuv6-s-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'lnkid': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'lnkid-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'mac-id': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'mac-id-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'mss-t': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'mss-t-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'mtuv4': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'mtuv4-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'mtuv6': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'mtuv6-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'slif-act': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'slif-act-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'sublnkid': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'sublnkid-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'tgtv-act': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'tgtv-act-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'tlif-act': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'tlif-act-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'tpeid': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'tpeid-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'v6fe': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'v6fe-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'vep-en-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'vep-slid': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'vep-slid-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'vep_en': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'xlt-lif': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'xlt-lif-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                'xlt-vid': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'xlt-vid-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('partial crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'system_npu_nputcam_tact'),
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
