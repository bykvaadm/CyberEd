#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_authentication_profiles
short_description: Resource module for Sda Authenticationprofiles
description:
- Manage operation update of the resource Sda Authenticationprofiles.
- Updates an authentication profile based on user input.
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  payload:
    description: Sda Authentication Profiles's payload.
    elements: dict
    suboptions:
      authenticationOrder:
        description: First authentication method.
        type: str
      authenticationProfileName:
        description: The default host authentication template (updating this field is
          not allowed).
        type: str
      dot1xToMabFallbackTimeout:
        description: 802.1x Timeout.
        type: int
      fabricId:
        description: ID of the fabric site/zone (updating this field is not allowed).
        type: str
      id:
        description: ID of the authentication profile (updating this field is not allowed).
        type: str
      numberOfHosts:
        description: Number of Hosts.
        type: str
      wakeOnLan:
        description: Wake on LAN.
        type: bool
    type: list
requirements:
- dnacentersdk >= 2.7.2
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for SDA UpdateAuthenticationProfile
  description: Complete reference of the UpdateAuthenticationProfile API.
  link: https://developer.cisco.com/docs/dna-center/#!update-authentication-profile
notes:
  - SDK Method used are
    sda.Sda.update_authentication_profile,

  - Paths used are
    put /dna/intent/api/v1/sda/authenticationProfiles,

"""

EXAMPLES = r"""
- name: Update all
  cisco.dnac.sda_authentication_profiles:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    payload:
    - authenticationOrder: string
      authenticationProfileName: string
      dot1xToMabFallbackTimeout: 0
      fabricId: string
      id: string
      numberOfHosts: string
      wakeOnLan: true

"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""
