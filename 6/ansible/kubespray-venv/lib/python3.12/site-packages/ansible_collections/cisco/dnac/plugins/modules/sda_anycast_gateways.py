#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_anycast_gateways
short_description: Resource module for Sda Anycastgateways
description:
- Manage operations create, update and delete of the resource Sda Anycastgateways.
- Adds anycast gateways based on user input.
- Deletes an anycast gateway based on id.
- Updates anycast gateways based on user input.
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. ID of the anycast gateway to be deleted.
    type: str
  payload:
    description: Sda Anycast Gateways's payload.
    elements: dict
    suboptions:
      fabricId:
        description: ID of the fabric containing this anycast gateway. Updating anycast
          gateways on fabric zones is not allowed--instead, update the corresponding
          anycast gateway on the fabric site and the updates will be applied on all
          applicable fabric zones (updating this field is not allowed).
        type: str
      id:
        description: ID of the anycast gateway (updating this field is not allowed).
        type: str
      ipPoolName:
        description: Name of the IP pool associated with the anycast gateway (updating
          this field is not allowed).
        type: str
      isCriticalPool:
        description: Enable/disable critical VLAN (not applicable to INFRA_VN; updating
          this field is not allowed).
        type: bool
      isIntraSubnetRoutingEnabled:
        description: Enable/disable Intra-Subnet Routing (not applicable to INFRA_VN;
          updating this field is not allowed).
        type: bool
      isIpDirectedBroadcast:
        description: Enable/disable IP-directed broadcast (not applicable to INFRA_VN).
        type: bool
      isLayer2FloodingEnabled:
        description: Enable/disable layer 2 flooding (not applicable to INFRA_VN).
        type: bool
      isMultipleIpToMacAddresses:
        description: Enable/disable multiple IP-to-MAC Addresses (Wireless Bridged-Network
          Virtual Machine; not applicable to INFRA_VN).
        type: bool
      isSupplicantBasedExtendedNodeOnboarding:
        description: Enable/disable Supplicant-Based Extended Node Onboarding (applicable
          only to INFRA_VN; required when poolType is EXTENDED_NODE).
        type: bool
      isWirelessPool:
        description: Enable/disable fabric-enabled wireless (not applicable to INFRA_VN).
        type: bool
      poolType:
        description: The pool type of the anycast gateway (applicable only to INFRA_VN;
          updating this field is not allowed).
        type: str
      securityGroupName:
        description: Name of the associated Security Group (not applicable to INFRA_VN).
        type: str
      tcpMssAdjustment:
        description: TCP maximum segment size adjustment.
        type: int
      trafficType:
        description: The type of traffic the anycast gateway serves.
        type: str
      virtualNetworkName:
        description: Name of the layer 3 virtual network associated with the anycast
          gateway (updating this field is not allowed).
        type: str
      vlanId:
        description: ID of the VLAN of the anycast gateway (updating this field is not
          allowed).
        type: int
      vlanName:
        description: Name of the VLAN of the anycast gateway (updating this field is
          not allowed).
        type: str
    type: list
requirements:
- dnacentersdk >= 2.7.2
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for SDA AddAnycastGateways
  description: Complete reference of the AddAnycastGateways API.
  link: https://developer.cisco.com/docs/dna-center/#!add-anycast-gateways
- name: Cisco DNA Center documentation for SDA DeleteAnycastGatewayById
  description: Complete reference of the DeleteAnycastGatewayById API.
  link: https://developer.cisco.com/docs/dna-center/#!delete-anycast-gateway-by-id
- name: Cisco DNA Center documentation for SDA UpdateAnycastGateways
  description: Complete reference of the UpdateAnycastGateways API.
  link: https://developer.cisco.com/docs/dna-center/#!update-anycast-gateways
notes:
  - SDK Method used are
    sda.Sda.add_anycast_gateways,
    sda.Sda.delete_anycast_gateway_by_id,
    sda.Sda.update_anycast_gateways,

  - Paths used are
    post /dna/intent/api/v1/sda/anycastGateways,
    delete /dna/intent/api/v1/sda/anycastGateways/{id},
    put /dna/intent/api/v1/sda/anycastGateways,

"""

EXAMPLES = r"""
- name: Update all
  cisco.dnac.sda_anycast_gateways:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    payload:
    - fabricId: string
      id: string
      ipPoolName: string
      isCriticalPool: true
      isIntraSubnetRoutingEnabled: true
      isIpDirectedBroadcast: true
      isLayer2FloodingEnabled: true
      isMultipleIpToMacAddresses: true
      isSupplicantBasedExtendedNodeOnboarding: true
      isWirelessPool: true
      poolType: string
      securityGroupName: string
      tcpMssAdjustment: 0
      trafficType: string
      virtualNetworkName: string
      vlanId: 0
      vlanName: string

- name: Create
  cisco.dnac.sda_anycastGateways:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    payload:
    - autoGenerateVlanName: true
      fabricId: string
      ipPoolName: string
      isCriticalPool: true
      isIntraSubnetRoutingEnabled: true
      isIpDirectedBroadcast: true
      isLayer2FloodingEnabled: true
      isMultipleIpToMacAddresses: true
      isSupplicantBasedExtendedNodeOnboarding: true
      isWirelessPool: true
      poolType: string
      securityGroupName: string
      tcpMssAdjustment: 0
      trafficType: string
      virtualNetworkName: string
      vlanId: 0
      vlanName: string

- name: Delete by id
  cisco.dnac.sda_anycastGateways:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    id: string

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
