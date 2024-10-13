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
module: fmgr_system_npu_nputcam
short_description: Configure NPU TCAM policies.
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
    system_npu_nputcam:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            data:
                type: dict
                description: Data.
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
            dbg-dump:
                type: int
                description: Deprecated, please rename it to dbg_dump. Debug driver dump data/mask pdq.
            mask:
                type: dict
                description: Mask.
                suboptions:
                    df:
                        type: str
                        description: Tcam mask ip flag df.
                        choices:
                            - 'disable'
                            - 'enable'
                    dstip:
                        type: str
                        description: Tcam mask dst ipv4 address.
                    dstipv6:
                        type: str
                        description: Tcam mask dst ipv6 address.
                    dstmac:
                        type: str
                        description: Tcam mask dst macaddr.
                    dstport:
                        type: int
                        description: Tcam mask L4 dst port.
                    ethertype:
                        type: str
                        description: Tcam mask ethertype.
                    ext-tag:
                        type: str
                        description: Deprecated, please rename it to ext_tag. Tcam mask extension tag.
                        choices:
                            - 'disable'
                            - 'enable'
                    frag-off:
                        type: int
                        description: Deprecated, please rename it to frag_off. Tcam data ip flag fragment offset.
                    gen-buf-cnt:
                        type: int
                        description: Deprecated, please rename it to gen_buf_cnt. Tcam mask gen info buffer count.
                    gen-iv:
                        type: str
                        description: Deprecated, please rename it to gen_iv. Tcam mask gen info iv.
                        choices:
                            - 'invalid'
                            - 'valid'
                    gen-l3-flags:
                        type: int
                        description: Deprecated, please rename it to gen_l3_flags. Tcam mask gen info L3 flags.
                    gen-l4-flags:
                        type: int
                        description: Deprecated, please rename it to gen_l4_flags. Tcam mask gen info L4 flags.
                    gen-pkt-ctrl:
                        type: int
                        description: Deprecated, please rename it to gen_pkt_ctrl. Tcam mask gen info packet control.
                    gen-pri:
                        type: int
                        description: Deprecated, please rename it to gen_pri. Tcam mask gen info priority.
                    gen-pri-v:
                        type: str
                        description: Deprecated, please rename it to gen_pri_v. Tcam mask gen info priority valid.
                        choices:
                            - 'invalid'
                            - 'valid'
                    gen-tv:
                        type: str
                        description: Deprecated, please rename it to gen_tv. Tcam mask gen info tv.
                        choices:
                            - 'invalid'
                            - 'valid'
                    ihl:
                        type: int
                        description: Tcam mask ipv4 IHL.
                    ip4-id:
                        type: int
                        description: Deprecated, please rename it to ip4_id. Tcam mask ipv4 id.
                    ip6-fl:
                        type: int
                        description: Deprecated, please rename it to ip6_fl. Tcam mask ipv6 flow label.
                    ipver:
                        type: int
                        description: Tcam mask ip header version.
                    l4-wd10:
                        type: int
                        description: Deprecated, please rename it to l4_wd10. Tcam mask L4 word10.
                    l4-wd11:
                        type: int
                        description: Deprecated, please rename it to l4_wd11. Tcam mask L4 word11.
                    l4-wd8:
                        type: int
                        description: Deprecated, please rename it to l4_wd8. Tcam mask L4 word8.
                    l4-wd9:
                        type: int
                        description: Deprecated, please rename it to l4_wd9. Tcam mask L4 word9.
                    mf:
                        type: str
                        description: Tcam mask ip flag mf.
                        choices:
                            - 'disable'
                            - 'enable'
                    protocol:
                        type: int
                        description: Tcam mask ip protocol.
                    slink:
                        type: int
                        description: Tcam mask sublink.
                    smac-change:
                        type: str
                        description: Deprecated, please rename it to smac_change. Tcam mask source MAC change.
                        choices:
                            - 'disable'
                            - 'enable'
                    sp:
                        type: int
                        description: Tcam mask source port.
                    src-cfi:
                        type: str
                        description: Deprecated, please rename it to src_cfi. Tcam mask source cfi.
                        choices:
                            - 'disable'
                            - 'enable'
                    src-prio:
                        type: int
                        description: Deprecated, please rename it to src_prio. Tcam mask source priority.
                    src-updt:
                        type: str
                        description: Deprecated, please rename it to src_updt. Tcam mask source update.
                        choices:
                            - 'disable'
                            - 'enable'
                    srcip:
                        type: str
                        description: Tcam mask src ipv4 address.
                    srcipv6:
                        type: str
                        description: Tcam mask src ipv6 address.
                    srcmac:
                        type: str
                        description: Tcam mask src macaddr.
                    srcport:
                        type: int
                        description: Tcam mask L4 src port.
                    svid:
                        type: int
                        description: Tcam mask source vid.
                    tcp-ack:
                        type: str
                        description: Deprecated, please rename it to tcp_ack. Tcam mask tcp flag ack.
                        choices:
                            - 'disable'
                            - 'enable'
                    tcp-cwr:
                        type: str
                        description: Deprecated, please rename it to tcp_cwr. Tcam mask tcp flag cwr.
                        choices:
                            - 'disable'
                            - 'enable'
                    tcp-ece:
                        type: str
                        description: Deprecated, please rename it to tcp_ece. Tcam mask tcp flag ece.
                        choices:
                            - 'disable'
                            - 'enable'
                    tcp-fin:
                        type: str
                        description: Deprecated, please rename it to tcp_fin. Tcam mask tcp flag fin.
                        choices:
                            - 'disable'
                            - 'enable'
                    tcp-push:
                        type: str
                        description: Deprecated, please rename it to tcp_push. Tcam mask tcp flag push.
                        choices:
                            - 'disable'
                            - 'enable'
                    tcp-rst:
                        type: str
                        description: Deprecated, please rename it to tcp_rst. Tcam mask tcp flag rst.
                        choices:
                            - 'disable'
                            - 'enable'
                    tcp-syn:
                        type: str
                        description: Deprecated, please rename it to tcp_syn. Tcam mask tcp flag syn.
                        choices:
                            - 'disable'
                            - 'enable'
                    tcp-urg:
                        type: str
                        description: Deprecated, please rename it to tcp_urg. Tcam mask tcp flag urg.
                        choices:
                            - 'disable'
                            - 'enable'
                    tgt-cfi:
                        type: str
                        description: Deprecated, please rename it to tgt_cfi. Tcam mask target cfi.
                        choices:
                            - 'disable'
                            - 'enable'
                    tgt-prio:
                        type: int
                        description: Deprecated, please rename it to tgt_prio. Tcam mask target priority.
                    tgt-updt:
                        type: str
                        description: Deprecated, please rename it to tgt_updt. Tcam mask target port update.
                        choices:
                            - 'disable'
                            - 'enable'
                    tgt-v:
                        type: str
                        description: Deprecated, please rename it to tgt_v. Tcam mask target valid.
                        choices:
                            - 'invalid'
                            - 'valid'
                    tos:
                        type: int
                        description: Tcam mask ip tos.
                    tp:
                        type: int
                        description: Tcam mask target port.
                    ttl:
                        type: int
                        description: Tcam mask ip ttl.
                    tvid:
                        type: int
                        description: Tcam mask target vid.
                    vdid:
                        type: int
                        description: Tcam mask vdom id.
            mir-act:
                type: dict
                description: Deprecated, please rename it to mir_act. Mir act.
                suboptions:
                    vlif:
                        type: int
                        description: Tcam mirror action vlif.
            name:
                type: str
                description: NPU TCAM policies name.
                required: true
            oid:
                type: int
                description: NPU TCAM OID.
            pri-act:
                type: dict
                description: Deprecated, please rename it to pri_act. Pri act.
                suboptions:
                    priority:
                        type: int
                        description: Tcam priority action priority.
                    weight:
                        type: int
                        description: Tcam priority action weight.
            sact:
                type: dict
                description: Sact.
                suboptions:
                    act:
                        type: int
                        description: Tcam sact act.
                    act-v:
                        type: str
                        description: Deprecated, please rename it to act_v. Enable to set sact act.
                        choices:
                            - 'disable'
                            - 'enable'
                    bmproc:
                        type: int
                        description: Tcam sact bmproc.
                    bmproc-v:
                        type: str
                        description: Deprecated, please rename it to bmproc_v. Enable to set sact bmproc.
                        choices:
                            - 'disable'
                            - 'enable'
                    df-lif:
                        type: int
                        description: Deprecated, please rename it to df_lif. Tcam sact df-lif.
                    df-lif-v:
                        type: str
                        description: Deprecated, please rename it to df_lif_v. Enable to set sact df-lif.
                        choices:
                            - 'disable'
                            - 'enable'
                    dfr:
                        type: int
                        description: Tcam sact dfr.
                    dfr-v:
                        type: str
                        description: Deprecated, please rename it to dfr_v. Enable to set sact dfr.
                        choices:
                            - 'disable'
                            - 'enable'
                    dmac-skip:
                        type: int
                        description: Deprecated, please rename it to dmac_skip. Tcam sact dmac-skip.
                    dmac-skip-v:
                        type: str
                        description: Deprecated, please rename it to dmac_skip_v. Enable to set sact dmac-skip.
                        choices:
                            - 'disable'
                            - 'enable'
                    dosen:
                        type: int
                        description: Tcam sact dosen.
                    dosen-v:
                        type: str
                        description: Deprecated, please rename it to dosen_v. Enable to set sact dosen.
                        choices:
                            - 'disable'
                            - 'enable'
                    espff-proc:
                        type: int
                        description: Deprecated, please rename it to espff_proc. Tcam sact espff-proc.
                    espff-proc-v:
                        type: str
                        description: Deprecated, please rename it to espff_proc_v. Enable to set sact espff-proc.
                        choices:
                            - 'disable'
                            - 'enable'
                    etype-pid:
                        type: int
                        description: Deprecated, please rename it to etype_pid. Tcam sact etype-pid.
                    etype-pid-v:
                        type: str
                        description: Deprecated, please rename it to etype_pid_v. Enable to set sact etype-pid.
                        choices:
                            - 'disable'
                            - 'enable'
                    frag-proc:
                        type: int
                        description: Deprecated, please rename it to frag_proc. Tcam sact frag-proc.
                    frag-proc-v:
                        type: str
                        description: Deprecated, please rename it to frag_proc_v. Enable to set sact frag-proc.
                        choices:
                            - 'disable'
                            - 'enable'
                    fwd:
                        type: int
                        description: Tcam sact fwd.
                    fwd-lif:
                        type: int
                        description: Deprecated, please rename it to fwd_lif. Tcam sact fwd-lif.
                    fwd-lif-v:
                        type: str
                        description: Deprecated, please rename it to fwd_lif_v. Enable to set sact fwd-lif.
                        choices:
                            - 'disable'
                            - 'enable'
                    fwd-tvid:
                        type: int
                        description: Deprecated, please rename it to fwd_tvid. Tcam sact fwd-tvid.
                    fwd-tvid-v:
                        type: str
                        description: Deprecated, please rename it to fwd_tvid_v. Enable to set sact fwd-vid.
                        choices:
                            - 'disable'
                            - 'enable'
                    fwd-v:
                        type: str
                        description: Deprecated, please rename it to fwd_v. Enable to set sact fwd.
                        choices:
                            - 'disable'
                            - 'enable'
                    icpen:
                        type: int
                        description: Tcam sact icpen.
                    icpen-v:
                        type: str
                        description: Deprecated, please rename it to icpen_v. Enable to set sact icpen.
                        choices:
                            - 'disable'
                            - 'enable'
                    igmp-mld-snp:
                        type: int
                        description: Deprecated, please rename it to igmp_mld_snp. Tcam sact igmp-mld-snp.
                    igmp-mld-snp-v:
                        type: str
                        description: Deprecated, please rename it to igmp_mld_snp_v. Enable to set sact igmp-mld-snp.
                        choices:
                            - 'disable'
                            - 'enable'
                    learn:
                        type: int
                        description: Tcam sact learn.
                    learn-v:
                        type: str
                        description: Deprecated, please rename it to learn_v. Enable to set sact learn.
                        choices:
                            - 'disable'
                            - 'enable'
                    m-srh-ctrl:
                        type: int
                        description: Deprecated, please rename it to m_srh_ctrl. Tcam sact m-srh-ctrl.
                    m-srh-ctrl-v:
                        type: str
                        description: Deprecated, please rename it to m_srh_ctrl_v. Enable to set sact m-srh-ctrl.
                        choices:
                            - 'disable'
                            - 'enable'
                    mac-id:
                        type: int
                        description: Deprecated, please rename it to mac_id. Tcam sact mac-id.
                    mac-id-v:
                        type: str
                        description: Deprecated, please rename it to mac_id_v. Enable to set sact mac-id.
                        choices:
                            - 'disable'
                            - 'enable'
                    mss:
                        type: int
                        description: Tcam sact mss.
                    mss-v:
                        type: str
                        description: Deprecated, please rename it to mss_v. Enable to set sact mss.
                        choices:
                            - 'disable'
                            - 'enable'
                    pleen:
                        type: int
                        description: Tcam sact pleen.
                    pleen-v:
                        type: str
                        description: Deprecated, please rename it to pleen_v. Enable to set sact pleen.
                        choices:
                            - 'disable'
                            - 'enable'
                    prio-pid:
                        type: int
                        description: Deprecated, please rename it to prio_pid. Tcam sact prio-pid.
                    prio-pid-v:
                        type: str
                        description: Deprecated, please rename it to prio_pid_v. Enable to set sact prio-pid.
                        choices:
                            - 'disable'
                            - 'enable'
                    promis:
                        type: int
                        description: Tcam sact promis.
                    promis-v:
                        type: str
                        description: Deprecated, please rename it to promis_v. Enable to set sact promis.
                        choices:
                            - 'disable'
                            - 'enable'
                    rfsh:
                        type: int
                        description: Tcam sact rfsh.
                    rfsh-v:
                        type: str
                        description: Deprecated, please rename it to rfsh_v. Enable to set sact rfsh.
                        choices:
                            - 'disable'
                            - 'enable'
                    smac-skip:
                        type: int
                        description: Deprecated, please rename it to smac_skip. Tcam sact smac-skip.
                    smac-skip-v:
                        type: str
                        description: Deprecated, please rename it to smac_skip_v. Enable to set sact smac-skip.
                        choices:
                            - 'disable'
                            - 'enable'
                    tp-smchk-v:
                        type: str
                        description: Deprecated, please rename it to tp_smchk_v. Enable to set sact tp mode.
                        choices:
                            - 'disable'
                            - 'enable'
                    tp_smchk:
                        type: int
                        description: Tcam sact tp mode.
                    tpe-id:
                        type: int
                        description: Deprecated, please rename it to tpe_id. Tcam sact tpe-id.
                    tpe-id-v:
                        type: str
                        description: Deprecated, please rename it to tpe_id_v. Enable to set sact tpe-id.
                        choices:
                            - 'disable'
                            - 'enable'
                    vdm:
                        type: int
                        description: Tcam sact vdm.
                    vdm-v:
                        type: str
                        description: Deprecated, please rename it to vdm_v. Enable to set sact vdm.
                        choices:
                            - 'disable'
                            - 'enable'
                    vdom-id:
                        type: int
                        description: Deprecated, please rename it to vdom_id. Tcam sact vdom-id.
                    vdom-id-v:
                        type: str
                        description: Deprecated, please rename it to vdom_id_v. Enable to set sact vdom-id.
                        choices:
                            - 'disable'
                            - 'enable'
                    x-mode:
                        type: int
                        description: Deprecated, please rename it to x_mode. Tcam sact x-mode.
                    x-mode-v:
                        type: str
                        description: Deprecated, please rename it to x_mode_v. Enable to set sact x-mode.
                        choices:
                            - 'disable'
                            - 'enable'
            tact:
                type: dict
                description: Tact.
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
            type:
                type: str
                description: TCAM policy type.
                choices:
                    - 'L2_src_tc'
                    - 'L2_tgt_tc'
                    - 'L2_src_mir'
                    - 'L2_tgt_mir'
                    - 'L2_src_act'
                    - 'L2_tgt_act'
                    - 'IPv4_src_tc'
                    - 'IPv4_tgt_tc'
                    - 'IPv4_src_mir'
                    - 'IPv4_tgt_mir'
                    - 'IPv4_src_act'
                    - 'IPv4_tgt_act'
                    - 'IPv6_src_tc'
                    - 'IPv6_tgt_tc'
                    - 'IPv6_src_mir'
                    - 'IPv6_tgt_mir'
                    - 'IPv6_src_act'
                    - 'IPv6_tgt_act'
            vid:
                type: int
                description: NPU TCAM VID.
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
    - name: Configure NPU TCAM policies.
      fortinet.fortimanager.fmgr_system_npu_nputcam:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: present # <value in [present, absent]>
        system_npu_nputcam:
          data:
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
          dbg_dump: <integer>
          mask:
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
          mir_act:
            vlif: <integer>
          name: <string>
          oid: <integer>
          pri_act:
            priority: <integer>
            weight: <integer>
          sact:
            act: <integer>
            act_v: <value in [disable, enable]>
            bmproc: <integer>
            bmproc_v: <value in [disable, enable]>
            df_lif: <integer>
            df_lif_v: <value in [disable, enable]>
            dfr: <integer>
            dfr_v: <value in [disable, enable]>
            dmac_skip: <integer>
            dmac_skip_v: <value in [disable, enable]>
            dosen: <integer>
            dosen_v: <value in [disable, enable]>
            espff_proc: <integer>
            espff_proc_v: <value in [disable, enable]>
            etype_pid: <integer>
            etype_pid_v: <value in [disable, enable]>
            frag_proc: <integer>
            frag_proc_v: <value in [disable, enable]>
            fwd: <integer>
            fwd_lif: <integer>
            fwd_lif_v: <value in [disable, enable]>
            fwd_tvid: <integer>
            fwd_tvid_v: <value in [disable, enable]>
            fwd_v: <value in [disable, enable]>
            icpen: <integer>
            icpen_v: <value in [disable, enable]>
            igmp_mld_snp: <integer>
            igmp_mld_snp_v: <value in [disable, enable]>
            learn: <integer>
            learn_v: <value in [disable, enable]>
            m_srh_ctrl: <integer>
            m_srh_ctrl_v: <value in [disable, enable]>
            mac_id: <integer>
            mac_id_v: <value in [disable, enable]>
            mss: <integer>
            mss_v: <value in [disable, enable]>
            pleen: <integer>
            pleen_v: <value in [disable, enable]>
            prio_pid: <integer>
            prio_pid_v: <value in [disable, enable]>
            promis: <integer>
            promis_v: <value in [disable, enable]>
            rfsh: <integer>
            rfsh_v: <value in [disable, enable]>
            smac_skip: <integer>
            smac_skip_v: <value in [disable, enable]>
            tp_smchk_v: <value in [disable, enable]>
            tp_smchk: <integer>
            tpe_id: <integer>
            tpe_id_v: <value in [disable, enable]>
            vdm: <integer>
            vdm_v: <value in [disable, enable]>
            vdom_id: <integer>
            vdom_id_v: <value in [disable, enable]>
            x_mode: <integer>
            x_mode_v: <value in [disable, enable]>
          tact:
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
          type: <value in [L2_src_tc, L2_tgt_tc, L2_src_mir, ...]>
          vid: <integer>
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
        '/pm/config/adom/{adom}/obj/system/npu/npu-tcam',
        '/pm/config/global/obj/system/npu/npu-tcam'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/system/npu/npu-tcam/{npu-tcam}',
        '/pm/config/global/obj/system/npu/npu-tcam/{npu-tcam}'
    ]

    url_params = ['adom']
    module_primary_key = 'name'
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'system_npu_nputcam': {
            'type': 'dict',
            'v_range': [['7.4.2', '']],
            'options': {
                'data': {
                    'v_range': [['7.4.2', '']],
                    'type': 'dict',
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
                },
                'dbg-dump': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'mask': {
                    'v_range': [['7.4.2', '']],
                    'type': 'dict',
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
                },
                'mir-act': {'v_range': [['7.4.2', '']], 'type': 'dict', 'options': {'vlif': {'v_range': [['7.4.2', '']], 'type': 'int'}}},
                'name': {'v_range': [['7.4.2', '']], 'required': True, 'type': 'str'},
                'oid': {'v_range': [['7.4.2', '']], 'type': 'int'},
                'pri-act': {
                    'v_range': [['7.4.2', '']],
                    'type': 'dict',
                    'options': {'priority': {'v_range': [['7.4.2', '']], 'type': 'int'}, 'weight': {'v_range': [['7.4.2', '']], 'type': 'int'}}
                },
                'sact': {
                    'v_range': [['7.4.2', '']],
                    'type': 'dict',
                    'options': {
                        'act': {'v_range': [['7.4.2', '']], 'type': 'int'},
                        'act-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'bmproc': {'v_range': [['7.4.2', '']], 'type': 'int'},
                        'bmproc-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'df-lif': {'v_range': [['7.4.2', '']], 'type': 'int'},
                        'df-lif-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'dfr': {'v_range': [['7.4.2', '']], 'type': 'int'},
                        'dfr-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'dmac-skip': {'v_range': [['7.4.2', '']], 'type': 'int'},
                        'dmac-skip-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'dosen': {'v_range': [['7.4.2', '']], 'type': 'int'},
                        'dosen-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'espff-proc': {'v_range': [['7.4.2', '']], 'type': 'int'},
                        'espff-proc-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'etype-pid': {'v_range': [['7.4.2', '']], 'type': 'int'},
                        'etype-pid-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'frag-proc': {'v_range': [['7.4.2', '']], 'type': 'int'},
                        'frag-proc-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'fwd': {'v_range': [['7.4.2', '']], 'type': 'int'},
                        'fwd-lif': {'v_range': [['7.4.2', '']], 'type': 'int'},
                        'fwd-lif-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'fwd-tvid': {'v_range': [['7.4.2', '']], 'type': 'int'},
                        'fwd-tvid-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'fwd-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'icpen': {'v_range': [['7.4.2', '']], 'type': 'int'},
                        'icpen-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'igmp-mld-snp': {'v_range': [['7.4.2', '']], 'type': 'int'},
                        'igmp-mld-snp-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'learn': {'v_range': [['7.4.2', '']], 'type': 'int'},
                        'learn-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'm-srh-ctrl': {'v_range': [['7.4.2', '']], 'type': 'int'},
                        'm-srh-ctrl-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'mac-id': {'v_range': [['7.4.2', '']], 'type': 'int'},
                        'mac-id-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'mss': {'v_range': [['7.4.2', '']], 'type': 'int'},
                        'mss-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'pleen': {'v_range': [['7.4.2', '']], 'type': 'int'},
                        'pleen-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'prio-pid': {'v_range': [['7.4.2', '']], 'type': 'int'},
                        'prio-pid-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'promis': {'v_range': [['7.4.2', '']], 'type': 'int'},
                        'promis-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'rfsh': {'v_range': [['7.4.2', '']], 'type': 'int'},
                        'rfsh-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'smac-skip': {'v_range': [['7.4.2', '']], 'type': 'int'},
                        'smac-skip-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'tp-smchk-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'tp_smchk': {'v_range': [['7.4.2', '']], 'type': 'int'},
                        'tpe-id': {'v_range': [['7.4.2', '']], 'type': 'int'},
                        'tpe-id-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'vdm': {'v_range': [['7.4.2', '']], 'type': 'int'},
                        'vdm-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'vdom-id': {'v_range': [['7.4.2', '']], 'type': 'int'},
                        'vdom-id-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'},
                        'x-mode': {'v_range': [['7.4.2', '']], 'type': 'int'},
                        'x-mode-v': {'v_range': [['7.4.2', '']], 'choices': ['disable', 'enable'], 'type': 'str'}
                    }
                },
                'tact': {
                    'v_range': [['7.4.2', '']],
                    'type': 'dict',
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
                },
                'type': {
                    'v_range': [['7.4.2', '']],
                    'choices': [
                        'L2_src_tc', 'L2_tgt_tc', 'L2_src_mir', 'L2_tgt_mir', 'L2_src_act', 'L2_tgt_act', 'IPv4_src_tc', 'IPv4_tgt_tc', 'IPv4_src_mir',
                        'IPv4_tgt_mir', 'IPv4_src_act', 'IPv4_tgt_act', 'IPv6_src_tc', 'IPv6_tgt_tc', 'IPv6_src_mir', 'IPv6_tgt_mir', 'IPv6_src_act',
                        'IPv6_tgt_act'
                    ],
                    'type': 'str'
                },
                'vid': {'v_range': [['7.4.2', '']], 'type': 'int'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('full crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'system_npu_nputcam'),
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
