#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_anycast_gateways_count_info
short_description: Information module for Sda Anycastgateways Count
description:
- Get all Sda Anycastgateways Count.
- Returns the count of anycast gateways that match the provided query parameters.
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
    - FabricId query parameter. Only count anycast gateways within this fabric.
    type: str
  virtualNetworkName:
    description:
    - VirtualNetworkName query parameter. Only count anycast gateways associated with this virtual network.
    type: str
  ipPoolName:
    description:
    - IpPoolName query parameter. Only count anycast gateways associated with this IP pool.
    type: str
  vlanName:
    description:
    - VlanName query parameter. Only count anycast gateways associated with this VLAN name.
    type: str
  vlanId:
    description:
    - VlanId query parameter. Only count anycast gateways associated with this VLAN ID.
    type: int
requirements:
- dnacentersdk >= 2.7.2
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for SDA GetAnycastGatewayCount
  description: Complete reference of the GetAnycastGatewayCount API.
  link: https://developer.cisco.com/docs/dna-center/#!get-anycast-gateway-count
notes:
  - SDK Method used are
    sda.Sda.get_anycast_gateway_count,

  - Paths used are
    get /dna/intent/api/v1/sda/anycastGateways/count,

"""

EXAMPLES = r"""
- name: Get all Sda Anycastgateways Count
  cisco.dnac.sda_anycast_gateways_count_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    fabricId: string
    virtualNetworkName: string
    ipPoolName: string
    vlanName: string
    vlanId: 0
  register: result

"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "count": 0
      },
      "version": "string"
    }
"""
