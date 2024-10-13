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
module: fmgr_hotspot20_hsprofile
short_description: Configure hotspot profile.
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
    hotspot20_hsprofile:
        description: The top level parameters set.
        required: false
        type: dict
        suboptions:
            3gpp-plmn:
                type: str
                description: Deprecated, please rename it to 3gpp_plmn. 3GPP PLMN name.
            access-network-asra:
                type: str
                description: Deprecated, please rename it to access_network_asra. Enable/disable additional step required for access
                choices:
                    - 'disable'
                    - 'enable'
            access-network-esr:
                type: str
                description: Deprecated, please rename it to access_network_esr. Enable/disable emergency services reachable
                choices:
                    - 'disable'
                    - 'enable'
            access-network-internet:
                type: str
                description: Deprecated, please rename it to access_network_internet. Enable/disable connectivity to the Internet.
                choices:
                    - 'disable'
                    - 'enable'
            access-network-type:
                type: str
                description: Deprecated, please rename it to access_network_type. Access network type.
                choices:
                    - 'private-network'
                    - 'private-network-with-guest-access'
                    - 'chargeable-public-network'
                    - 'free-public-network'
                    - 'personal-device-network'
                    - 'emergency-services-only-network'
                    - 'test-or-experimental'
                    - 'wildcard'
            access-network-uesa:
                type: str
                description: Deprecated, please rename it to access_network_uesa. Enable/disable unauthenticated emergency service accessible
                choices:
                    - 'disable'
                    - 'enable'
            anqp-domain-id:
                type: int
                description: Deprecated, please rename it to anqp_domain_id. ANQP Domain ID
            bss-transition:
                type: str
                description: Deprecated, please rename it to bss_transition. Enable/disable basic service set
                choices:
                    - 'disable'
                    - 'enable'
            conn-cap:
                type: str
                description: Deprecated, please rename it to conn_cap. Connection capability name.
            deauth-request-timeout:
                type: int
                description: Deprecated, please rename it to deauth_request_timeout. Deauthentication request timeout
            dgaf:
                type: str
                description: Enable/disable downstream group-addressed forwarding
                choices:
                    - 'disable'
                    - 'enable'
            domain-name:
                type: str
                description: Deprecated, please rename it to domain_name. Domain name.
            gas-comeback-delay:
                type: int
                description: Deprecated, please rename it to gas_comeback_delay. GAS comeback delay
            gas-fragmentation-limit:
                type: int
                description: Deprecated, please rename it to gas_fragmentation_limit. GAS fragmentation limit
            hessid:
                type: str
                description: Homogeneous extended service set identifier
            ip-addr-type:
                type: str
                description: Deprecated, please rename it to ip_addr_type. IP address type name.
            l2tif:
                type: str
                description: Enable/disable Layer 2 traffic inspection and filtering.
                choices:
                    - 'disable'
                    - 'enable'
            nai-realm:
                type: str
                description: Deprecated, please rename it to nai_realm. NAI realm list name.
            name:
                type: str
                description: Hotspot profile name.
                required: true
            network-auth:
                type: str
                description: Deprecated, please rename it to network_auth. Network authentication name.
            oper-friendly-name:
                type: str
                description: Deprecated, please rename it to oper_friendly_name. Operator friendly name.
            osu-provider:
                type: raw
                description: (list or str) Deprecated, please rename it to osu_provider. Manually selected list of OSU provider
            osu-ssid:
                type: str
                description: Deprecated, please rename it to osu_ssid. Online sign up
            pame-bi:
                type: str
                description: Deprecated, please rename it to pame_bi. Enable/disable Pre-Association Message Exchange BSSID Independent
                choices:
                    - 'disable'
                    - 'enable'
            proxy-arp:
                type: str
                description: Deprecated, please rename it to proxy_arp. Enable/disable Proxy ARP.
                choices:
                    - 'disable'
                    - 'enable'
            qos-map:
                type: str
                description: Deprecated, please rename it to qos_map. QoS MAP set ID.
            roaming-consortium:
                type: str
                description: Deprecated, please rename it to roaming_consortium. Roaming consortium list name.
            venue-group:
                type: str
                description: Deprecated, please rename it to venue_group. Venue group.
                choices:
                    - 'unspecified'
                    - 'assembly'
                    - 'business'
                    - 'educational'
                    - 'factory'
                    - 'institutional'
                    - 'mercantile'
                    - 'residential'
                    - 'storage'
                    - 'utility'
                    - 'vehicular'
                    - 'outdoor'
            venue-name:
                type: str
                description: Deprecated, please rename it to venue_name. Venue name.
            venue-type:
                type: str
                description: Deprecated, please rename it to venue_type. Venue type.
                choices:
                    - 'unspecified'
                    - 'arena'
                    - 'stadium'
                    - 'passenger-terminal'
                    - 'amphitheater'
                    - 'amusement-park'
                    - 'place-of-worship'
                    - 'convention-center'
                    - 'library'
                    - 'museum'
                    - 'restaurant'
                    - 'theater'
                    - 'bar'
                    - 'coffee-shop'
                    - 'zoo-or-aquarium'
                    - 'emergency-center'
                    - 'doctor-office'
                    - 'bank'
                    - 'fire-station'
                    - 'police-station'
                    - 'post-office'
                    - 'professional-office'
                    - 'research-facility'
                    - 'attorney-office'
                    - 'primary-school'
                    - 'secondary-school'
                    - 'university-or-college'
                    - 'factory'
                    - 'hospital'
                    - 'long-term-care-facility'
                    - 'rehab-center'
                    - 'group-home'
                    - 'prison-or-jail'
                    - 'retail-store'
                    - 'grocery-market'
                    - 'auto-service-station'
                    - 'shopping-mall'
                    - 'gas-station'
                    - 'private'
                    - 'hotel-or-motel'
                    - 'dormitory'
                    - 'boarding-house'
                    - 'automobile'
                    - 'airplane'
                    - 'bus'
                    - 'ferry'
                    - 'ship-or-boat'
                    - 'train'
                    - 'motor-bike'
                    - 'muni-mesh-network'
                    - 'city-park'
                    - 'rest-area'
                    - 'traffic-control'
                    - 'bus-stop'
                    - 'kiosk'
            wan-metrics:
                type: str
                description: Deprecated, please rename it to wan_metrics. WAN metric name.
            wnm-sleep-mode:
                type: str
                description: Deprecated, please rename it to wnm_sleep_mode. Enable/disable wireless network management
                choices:
                    - 'disable'
                    - 'enable'
            advice-of-charge:
                type: str
                description: Deprecated, please rename it to advice_of_charge. Advice of charge.
            oper-icon:
                type: str
                description: Deprecated, please rename it to oper_icon. Operator icon.
            osu-provider-nai:
                type: str
                description: Deprecated, please rename it to osu_provider_nai. OSU Provider NAI.
            release:
                type: int
                description: Hotspot 2.
            terms-and-conditions:
                type: str
                description: Deprecated, please rename it to terms_and_conditions. Terms and conditions.
            venue-url:
                type: str
                description: Deprecated, please rename it to venue_url. Venue name.
            wba-charging-currency:
                type: str
                description: Deprecated, please rename it to wba_charging_currency. Three letter currency code.
            wba-charging-rate:
                type: int
                description: Deprecated, please rename it to wba_charging_rate. Number of currency units per kilobyte.
            wba-data-clearing-provider:
                type: str
                description: Deprecated, please rename it to wba_data_clearing_provider. WBA ID of data clearing provider.
            wba-financial-clearing-provider:
                type: str
                description: Deprecated, please rename it to wba_financial_clearing_provider. WBA ID of financial clearing provider.
            wba-open-roaming:
                type: str
                description: Deprecated, please rename it to wba_open_roaming. Enable/disable WBA open roaming support.
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
    - name: Configure hotspot profile.
      fortinet.fortimanager.fmgr_hotspot20_hsprofile:
        # bypass_validation: false
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        # rc_succeeded: [0, -2, -3, ...]
        # rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: present # <value in [present, absent]>
        hotspot20_hsprofile:
          3gpp_plmn: <string>
          access_network_asra: <value in [disable, enable]>
          access_network_esr: <value in [disable, enable]>
          access_network_internet: <value in [disable, enable]>
          access_network_type: <value in [private-network, private-network-with-guest-access, chargeable-public-network, ...]>
          access_network_uesa: <value in [disable, enable]>
          anqp_domain_id: <integer>
          bss_transition: <value in [disable, enable]>
          conn_cap: <string>
          deauth_request_timeout: <integer>
          dgaf: <value in [disable, enable]>
          domain_name: <string>
          gas_comeback_delay: <integer>
          gas_fragmentation_limit: <integer>
          hessid: <string>
          ip_addr_type: <string>
          l2tif: <value in [disable, enable]>
          nai_realm: <string>
          name: <string>
          network_auth: <string>
          oper_friendly_name: <string>
          osu_provider: <list or string>
          osu_ssid: <string>
          pame_bi: <value in [disable, enable]>
          proxy_arp: <value in [disable, enable]>
          qos_map: <string>
          roaming_consortium: <string>
          venue_group: <value in [unspecified, assembly, business, ...]>
          venue_name: <string>
          venue_type: <value in [unspecified, arena, stadium, ...]>
          wan_metrics: <string>
          wnm_sleep_mode: <value in [disable, enable]>
          advice_of_charge: <string>
          oper_icon: <string>
          osu_provider_nai: <string>
          release: <integer>
          terms_and_conditions: <string>
          venue_url: <string>
          wba_charging_currency: <string>
          wba_charging_rate: <integer>
          wba_data_clearing_provider: <string>
          wba_financial_clearing_provider: <string>
          wba_open_roaming: <value in [disable, enable]>
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
        '/pm/config/adom/{adom}/obj/wireless-controller/hotspot20/hs-profile',
        '/pm/config/global/obj/wireless-controller/hotspot20/hs-profile'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/wireless-controller/hotspot20/hs-profile/{hs-profile}',
        '/pm/config/global/obj/wireless-controller/hotspot20/hs-profile/{hs-profile}'
    ]

    url_params = ['adom']
    module_primary_key = 'name'
    module_arg_spec = {
        'adom': {'required': True, 'type': 'str'},
        'hotspot20_hsprofile': {
            'type': 'dict',
            'v_range': [['6.0.0', '']],
            'options': {
                '3gpp-plmn': {'type': 'str'},
                'access-network-asra': {'choices': ['disable', 'enable'], 'type': 'str'},
                'access-network-esr': {'choices': ['disable', 'enable'], 'type': 'str'},
                'access-network-internet': {'choices': ['disable', 'enable'], 'type': 'str'},
                'access-network-type': {
                    'choices': [
                        'private-network', 'private-network-with-guest-access', 'chargeable-public-network', 'free-public-network',
                        'personal-device-network', 'emergency-services-only-network', 'test-or-experimental', 'wildcard'
                    ],
                    'type': 'str'
                },
                'access-network-uesa': {'choices': ['disable', 'enable'], 'type': 'str'},
                'anqp-domain-id': {'type': 'int'},
                'bss-transition': {'choices': ['disable', 'enable'], 'type': 'str'},
                'conn-cap': {'type': 'str'},
                'deauth-request-timeout': {'type': 'int'},
                'dgaf': {'choices': ['disable', 'enable'], 'type': 'str'},
                'domain-name': {'type': 'str'},
                'gas-comeback-delay': {'type': 'int'},
                'gas-fragmentation-limit': {'type': 'int'},
                'hessid': {'type': 'str'},
                'ip-addr-type': {'type': 'str'},
                'l2tif': {'choices': ['disable', 'enable'], 'type': 'str'},
                'nai-realm': {'type': 'str'},
                'name': {'required': True, 'type': 'str'},
                'network-auth': {'type': 'str'},
                'oper-friendly-name': {'type': 'str'},
                'osu-provider': {'type': 'raw'},
                'osu-ssid': {'type': 'str'},
                'pame-bi': {'choices': ['disable', 'enable'], 'type': 'str'},
                'proxy-arp': {'choices': ['disable', 'enable'], 'type': 'str'},
                'qos-map': {'type': 'str'},
                'roaming-consortium': {'type': 'str'},
                'venue-group': {
                    'choices': [
                        'unspecified', 'assembly', 'business', 'educational', 'factory', 'institutional', 'mercantile', 'residential', 'storage',
                        'utility', 'vehicular', 'outdoor'
                    ],
                    'type': 'str'
                },
                'venue-name': {'type': 'str'},
                'venue-type': {
                    'choices': [
                        'unspecified', 'arena', 'stadium', 'passenger-terminal', 'amphitheater', 'amusement-park', 'place-of-worship',
                        'convention-center', 'library', 'museum', 'restaurant', 'theater', 'bar', 'coffee-shop', 'zoo-or-aquarium', 'emergency-center',
                        'doctor-office', 'bank', 'fire-station', 'police-station', 'post-office', 'professional-office', 'research-facility',
                        'attorney-office', 'primary-school', 'secondary-school', 'university-or-college', 'factory', 'hospital',
                        'long-term-care-facility', 'rehab-center', 'group-home', 'prison-or-jail', 'retail-store', 'grocery-market',
                        'auto-service-station', 'shopping-mall', 'gas-station', 'private', 'hotel-or-motel', 'dormitory', 'boarding-house', 'automobile',
                        'airplane', 'bus', 'ferry', 'ship-or-boat', 'train', 'motor-bike', 'muni-mesh-network', 'city-park', 'rest-area',
                        'traffic-control', 'bus-stop', 'kiosk'
                    ],
                    'type': 'str'
                },
                'wan-metrics': {'type': 'str'},
                'wnm-sleep-mode': {'choices': ['disable', 'enable'], 'type': 'str'},
                'advice-of-charge': {'v_range': [['7.0.2', '']], 'type': 'str'},
                'oper-icon': {'v_range': [['7.0.2', '']], 'type': 'str'},
                'osu-provider-nai': {'v_range': [['7.0.2', '']], 'type': 'str'},
                'release': {'v_range': [['7.0.2', '']], 'type': 'int'},
                'terms-and-conditions': {'v_range': [['7.0.2', '']], 'type': 'str'},
                'venue-url': {'v_range': [['7.0.2', '']], 'type': 'str'},
                'wba-charging-currency': {'v_range': [['7.6.0', '']], 'type': 'str'},
                'wba-charging-rate': {'v_range': [['7.6.0', '']], 'type': 'int'},
                'wba-data-clearing-provider': {'v_range': [['7.6.0', '']], 'type': 'str'},
                'wba-financial-clearing-provider': {'v_range': [['7.6.0', '']], 'type': 'str'},
                'wba-open-roaming': {'v_range': [['7.6.0', '']], 'choices': ['disable', 'enable'], 'type': 'str'}
            }

        }
    }

    module_option_spec = get_module_arg_spec('full crud')
    module_arg_spec.update(module_option_spec)
    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'hotspot20_hsprofile'),
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
