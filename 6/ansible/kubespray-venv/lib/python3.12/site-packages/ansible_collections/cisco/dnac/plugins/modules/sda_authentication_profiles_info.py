#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_authentication_profiles_info
short_description: Information module for Sda Authenticationprofiles
description:
- Get all Sda Authenticationprofiles.
- Returns a list of authentication profiles that match the provided query parameters.
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  fabricId:
    description:
    - FabricId query parameter. ID of the fabric whose authentication profiles are to be returned.
    type: str
  authenticationProfileName:
    description:
    - >
      AuthenticationProfileName query parameter. Return only the authentication profiles with this specified name.
      Note that 'No Authentication' is not a valid option for this parameter.
    type: str
requirements:
- dnacentersdk >= 2.7.2
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for SDA GetAuthenticationProfiles
  description: Complete reference of the GetAuthenticationProfiles API.
  link: https://developer.cisco.com/docs/dna-center/#!get-authentication-profiles
notes:
  - SDK Method used are
    sda.Sda.get_authentication_profiles,

  - Paths used are
    get /dna/intent/api/v1/sda/authenticationProfiles,

"""

EXAMPLES = r"""
- name: Get all Sda Authenticationprofiles
  cisco.dnac.sda_authentication_profiles_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    fabricId: string
    authenticationProfileName: string
  register: result

"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "id": "string",
          "fabricId": "string",
          "authenticationProfileName": "string",
          "authenticationOrder": "string",
          "dot1xToMabFallbackTimeout": 0,
          "wakeOnLan": true,
          "numberOfHosts": "string"
        }
      ],
      "version": "string"
    }
"""
