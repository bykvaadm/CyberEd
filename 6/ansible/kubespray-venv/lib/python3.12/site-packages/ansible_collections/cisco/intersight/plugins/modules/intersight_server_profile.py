#!/usr/bin/python
# -*- coding: utf-8 -*-

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = r'''
---
module: intersight_server_profile
short_description: Server Profile configuration for Cisco Intersight
description:
  - Server Profile configuration for Cisco Intersight.
  - Used to configure Server Profiles with assigned servers and server policies.
  - For more information see L(Cisco Intersight,https://intersight.com/apidocs).
extends_documentation_fragment: intersight
options:
  state:
    description:
      - If C(present), will verify the resource is present and will create if needed.
      - If C(absent), will verify the resource is absent and will delete if needed.
    type: str
    choices: [present, absent]
    default: present
  organization:
    description:
      - The name of the Organization this resource is assigned to.
      - Profiles and Policies that are created within a Custom Organization are applicable only to devices in the same Organization.
    type: str
    default: default
  name:
    description:
      - The name assigned to the Server Profile.
      - The name must be between 1 and 62 alphanumeric characters, allowing special characters :-_.
    type: str
    required: true
  target_platform:
    description:
      - The platform for which the server profile is applicable.
      - Can either be a server that is operating in Standalone mode or which is attached to a Fabric Interconnect (FIAttached) managed by Intersight.
    type: str
    choices: [Standalone, FIAttached]
    default: Standalone
  tags:
    description:
      - List of tags in Key:<user-defined key> Value:<user-defined value> format.
    type: list
    elements: dict
    default: []
  description:
    description:
      - The user-defined description of the Server Profile.
      - Description can contain letters(a-z, A-Z), numbers(0-9), hyphen(-), period(.), colon(:), or an underscore(_).
    type: str
    aliases: [descr]
    default: ''
  assigned_server:
    description:
      - Managed Obect ID (MOID) of assigned server.
      - Option can be omitted if user wishes to assign server later.
    type: str
  bios_policy:
    description:
      - Name of BIOS Policy to associate with this profile.
    type: str
  boot_order_policy:
    description:
      - Name of Boot Order Policy to associate with this profile.
    type: str
  certificate_policy:
    description:
      - Name of Certificate Policy to associate with this profile.
    type: str
  drive_security_policy:
    description:
      - Name of Drive Security Policy to associate with this profile.
    type: str
  firmware_policy:
    description:
      - Name of Firmware Policy to associate with this profile.
    type: str
  imc_access_policy:
    description:
      - Name of IMC Access Policy to associate with this profile.
    type: str
  ipmi_over_lan_policy:
    description:
      - Name of IPMI over LAN Policy to associate with this profile.
    type: str
  lan_connectivity_policy:
    description:
      - Name of LAN Connectivity Policy to associate with this profile.
    type: str
  local_user_policy:
    description:
      - Name of Local User Policy to associate with this profile.
    type: str
  ntp_policy:
    description:
      - Name of NTP Policy to associate with this profile.
    type: str
  power_policy:
    description:
      - Name of Power Policy to associated with this profile.
    type: str
  san_connectivity_policy:
    description:
      - Name of SAN Connectivity Policy to associate with this profile.
    type: str
  serial_over_lan_policy:
    description:
      - Name of Serial over LAN Policy to associate with this profile.
    type: str
  snmp_policy:
    description:
      - Name of SNMP Policy to associate with this profile.
    type: str
  storage_policy:
    description:
      - Name of Storage Policy to associate with this profile.
    type: str
  syslog_policy:
    description:
      - Name of Syslog Policy to associate with this profile.
    type: str
  thermal_policy:
    description:
      - Name of Thermal Policy to associate with this profile.
    type: str
  virtual_kvm_policy:
    description:
      - Name of Virtual KVM Policy to associate with this profile.
    type: str
  virtual_media_policy:
    description:
      - Name of Virtual Media Policy to associate with this profile.
    type: str
author:
  - David Soper (@dsoper2)
  - Sid Nath (@SidNath21)
  - Tse Kai "Kevin" Chan (@BrightScale)
  - Soma Tummala (@SOMATUMMALA21)
'''

EXAMPLES = r'''
- name: Configure Server Profile
  cisco.intersight.intersight_server_profile:
    api_private_key: "{{ api_private_key }}"
    api_key_id: "{{ api_key_id }}"
    name: SP-Server1
    target_platform: FIAttached
    tags:
      - Key: Site
        Value: SJC02
    description: Profile for Server1
    assigned_server: 5e3b517d6176752d319a9999
    boot_order_policy: COS-Boot
    imc_access_policy: sjc02-d23-access
    lan_connectivity_policy: sjc02-d23-lan
    local_user_policy: guest-admin
    ntp_policy: lab-ntp
    storage_policy: storage
    virtual_media_policy: COS-VM

- name: Delete Server Profile
  cisco.intersight.intersight_server_profile:
    api_private_key: "{{ api_private_key }}"
    api_key_id: "{{ api_key_id }}"
    name: SP-Server1
    state: absent
'''

RETURN = r'''
api_repsonse:
  description: The API response output returned by the specified resource.
  returned: always
  type: dict
  sample:
    "api_response": {
        "AssignedServer": {
            "Moid": "5e3b517d6176752d319a0881",
            "ObjectType": "compute.Blade",
        },
        "Name": "SP-IMM-6454-D23-1-1",
        "ObjectType": "server.Profile",
        "Tags": [
            {
                "Key": "Site",
                "Value": "SJC02"
            }
        ],
        "TargetPlatform": "FIAttached",
        "Type": "instance"
    }
'''


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.intersight.plugins.module_utils.intersight import IntersightModule, intersight_argument_spec


def post_profile_to_policy(intersight, moid, resource_path, policy_name):
    options = {
        'http_method': 'get',
        'resource_path': resource_path,
        'query_params': {
            '$filter': "Name eq '" + policy_name + "'",
        },
    }
    response = intersight.call_api(**options)
    if response.get('Results'):
        # get expected policy moid from 1st list element
        expected_policy_moid = response['Results'][0]['Moid']
        actual_policy_moid = ''
        # check any current profiles and delete if needed
        options = {
            'http_method': 'get',
            'resource_path': resource_path,
            'query_params': {
                '$filter': "Profiles/any(t: t/Moid eq '" + moid + "')",
            },
        }
        response = intersight.call_api(**options)
        if response.get('Results'):
            # get actual moid from 1st list element
            actual_policy_moid = response['Results'][0]['Moid']
            if actual_policy_moid != expected_policy_moid:
                if not intersight.module.check_mode:
                    # delete the actual policy
                    options = {
                        'http_method': 'delete',
                        'resource_path': resource_path + '/' + actual_policy_moid + '/Profiles',
                        'moid': moid,
                    }
                    intersight.call_api(**options)
                actual_policy_moid = ''
        if not actual_policy_moid:
            if not intersight.module.check_mode:
                # post profile to the expected policy
                options = {
                    'http_method': 'post',
                    'resource_path': resource_path + '/' + expected_policy_moid + '/Profiles',
                    'body': [
                        {
                            'ObjectType': 'server.Profile',
                            'Moid': moid,
                        }
                    ]
                }
                intersight.call_api(**options)
            intersight.result['changed'] = True


def main():
    argument_spec = intersight_argument_spec.copy()
    argument_spec.update(
        state=dict(type='str', choices=['present', 'absent'], default='present'),
        organization=dict(type='str', default='default'),
        name=dict(type='str', required=True),
        target_platform=dict(type='str', choices=['Standalone', 'FIAttached'], default='Standalone'),
        tags=dict(type='list', elements='dict', default=[]),
        description=dict(type='str', aliases=['descr'], default=''),
        assigned_server=dict(type='str'),
        bios_policy=dict(type='str'),
        boot_order_policy=dict(type='str'),
        certificate_policy=dict(type='str'),
        drive_security_policy=dict(type='str'),
        firmware_policy=dict(type='str'),
        imc_access_policy=dict(type='str'),
        ipmi_over_lan_policy=dict(type='str'),
        lan_connectivity_policy=dict(type='str'),
        local_user_policy=dict(type='str'),
        ntp_policy=dict(type='str'),
        power_policy=dict(type='str'),
        san_connectivity_policy=dict(type='str'),
        serial_over_lan_policy=dict(type='str'),
        snmp_policy=dict(type='str'),
        storage_policy=dict(type='str'),
        syslog_policy=dict(type='str'),
        thermal_policy=dict(type='str'),
        virtual_kvm_policy=dict(type='str'),
        virtual_media_policy=dict(type='str'),
    )

    module = AnsibleModule(
        argument_spec,
        supports_check_mode=True,
    )

    intersight = IntersightModule(module)
    intersight.result['api_response'] = {}
    intersight.result['trace_id'] = ''
    #
    # Argument spec above, resource path, and API body should be the only code changed in this module
    #
    resource_path = '/server/Profiles'
    # Define API body used in compares or create
    intersight.api_body = {
        'Organization': {
            'Name': intersight.module.params['organization'],
        },
        'Name': intersight.module.params['name'],
        'Tags': intersight.module.params['tags'],
        'Description': intersight.module.params['description'],
    }
    intersight.result['api_response'] = {}
    # Get assigned server information (if defined)
    if intersight.module.params['assigned_server']:
        intersight.get_resource(
            resource_path='/compute/PhysicalSummaries',
            query_params={
                '$filter': "Moid eq '" + intersight.module.params['assigned_server'] + "'",
            }
        )
        source_object_type = None
        if intersight.result['api_response'].get('SourceObjectType'):
            source_object_type = intersight.result['api_response']['SourceObjectType']
        intersight.api_body['AssignedServer'] = {
            'Moid': intersight.module.params['assigned_server'],
            'ObjectType': source_object_type,
        }
    if intersight.module.params['target_platform'] == 'FIAttached':
        intersight.api_body['TargetPlatform'] = intersight.module.params['target_platform']

    # Configure the profile
    moid = intersight.configure_policy_or_profile(resource_path=resource_path)

    if moid and intersight.module.params['bios_policy']:
        post_profile_to_policy(intersight, moid, resource_path='/bios/Policies', policy_name=intersight.module.params['bios_policy'])
    if moid and intersight.module.params['boot_order_policy']:
        post_profile_to_policy(intersight, moid, resource_path='/boot/PrecisionPolicies', policy_name=intersight.module.params['boot_order_policy'])
    if moid and intersight.module.params['certificate_policy']:
        post_profile_to_policy(intersight, moid, resource_path='/certificatemanagement/Policies', policy_name=intersight.module.params['certificate_policy'])
    if moid and intersight.module.params['drive_security_policy']:
        post_profile_to_policy(intersight, moid, resource_path='/storage/DriveSecurityPolicies', policy_name=intersight.module.params['drive_security_policy'])
    if moid and intersight.module.params['firmware_policy']:
        post_profile_to_policy(intersight, moid, resource_path='/firmware/Policies', policy_name=intersight.module.params['firmware_policy'])
    if moid and intersight.module.params['imc_access_policy']:
        post_profile_to_policy(intersight, moid, resource_path='/access/Policies', policy_name=intersight.module.params['imc_access_policy'])
    if moid and intersight.module.params['ipmi_over_lan_policy']:
        post_profile_to_policy(intersight, moid, resource_path='/ipmioverlan/Policies', policy_name=intersight.module.params['ipmi_over_lan_policy'])
    if moid and intersight.module.params['lan_connectivity_policy']:
        post_profile_to_policy(intersight, moid, resource_path='/vnic/LanConnectivityPolicies', policy_name=intersight.module.params['lan_connectivity_policy'])
    if moid and intersight.module.params['local_user_policy']:
        post_profile_to_policy(intersight, moid, resource_path='/iam/EndPointUserPolicies', policy_name=intersight.module.params['local_user_policy'])
    if moid and intersight.module.params['ntp_policy']:
        post_profile_to_policy(intersight, moid, resource_path='/ntp/Policies', policy_name=intersight.module.params['ntp_policy'])
    if moid and intersight.module.params['power_policy']:
        post_profile_to_policy(intersight, moid, resource_path='/power/Policies', policy_name=intersight.module.params['power_policy'])
    if moid and intersight.module.params['san_connectivity_policy']:
        post_profile_to_policy(intersight, moid, resource_path='/vnic/SanConnectivityPolicies', policy_name=intersight.module.params['san_connectivity_policy'])
    if moid and intersight.module.params['serial_over_lan_policy']:
        post_profile_to_policy(intersight, moid, resource_path='/sol/Policies', policy_name=intersight.module.params['serial_over_lan_policy'])
    if moid and intersight.module.params['snmp_policy']:
        post_profile_to_policy(intersight, moid, resource_path='/snmp/Policies', policy_name=intersight.module.params['snmp_policy'])
    if moid and intersight.module.params['storage_policy']:
        post_profile_to_policy(intersight, moid, resource_path='/storage/StoragePolicies', policy_name=intersight.module.params['storage_policy'])
    if moid and intersight.module.params['syslog_policy']:
        post_profile_to_policy(intersight, moid, resource_path='/syslog/Policies', policy_name=intersight.module.params['syslog_policy'])
    if moid and intersight.module.params['thermal_policy']:
        post_profile_to_policy(intersight, moid, resource_path='/thermal/Policies', policy_name=intersight.module.params['thermal_policy'])
    if moid and intersight.module.params['virtual_kvm_policy']:
        post_profile_to_policy(intersight, moid, resource_path='/kvm/Policies', policy_name=intersight.module.params['virtual_kvm_policy'])
    if moid and intersight.module.params['virtual_media_policy']:
        post_profile_to_policy(intersight, moid, resource_path='/vmedia/Policies', policy_name=intersight.module.params['virtual_media_policy'])

    module.exit_json(**intersight.result)


if __name__ == '__main__':
    main()
