#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device
short_description: Resource module for Network Device
description:
- Manage operations create, update and delete of the resource Network Device.
- Adds the device with given credential.
- Deletes the network device for the given Id.
- >
   Update the credentials, management IP address of a given device or a set of devices in Catalyst Center and trigger
   an inventory sync.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  cleanConfig:
    description: CleanConfig query parameter.
    type: bool
    version_added: 4.0.0
  cliTransport:
    description: CLI transport. Supported values telnet, ssh2.
    type: str
  computeDevice:
    description: Compute Device or not. Options are TRUE / FALSE.
    type: bool
  enablePassword:
    description: CLI enable password of the device.
    type: str
  extendedDiscoveryInfo:
    description: This field holds that info as whether to add device with canned data
      or not. Supported values DISCOVER_WITH_CANNED_DATA.
    type: str
  httpPassword:
    description: HTTP password of the device.
    type: str
  httpPort:
    description: HTTP port of the device.
    type: str
  httpSecure:
    description: Flag to select HTTP / HTTPS protocol. Options are TRUE / FALSE. TRUE
      for HTTPS and FALSE for HTTP.
    type: bool
  httpUserName:
    description: HTTP Username of the device.
    type: str
  id:
    description: Id path parameter. Device ID.
    type: str
  ipAddress:
    description: IP Address of the device.
    elements: str
    type: list
  merakiOrgId:
    description: Selected meraki organization for which the devices needs to be imported.
    elements: str
    type: list
  netconfPort:
    description: Netconf Port of the device.
    type: str
  password:
    description: CLI Password of the device.
    type: str
  serialNumber:
    description: Serial Number of the Device.
    type: str
  snmpAuthPassphrase:
    description: SNMPV3 auth passphrase of the device.
    type: str
  snmpAuthProtocol:
    description: SNMPV3 auth protocol. Supported values sha, md5.
    type: str
  snmpMode:
    description: SNMPV3 mode. Supported values noAuthnoPriv, authNoPriv, authPriv.
    type: str
  snmpPrivPassphrase:
    description: SNMPV3 priv passphrase.
    type: str
  snmpPrivProtocol:
    description: SNMPV3 priv protocol. Supported values AES128.
    type: str
  snmpROCommunity:
    description: SNMP Read Community of the device.
    type: str
  snmpRWCommunity:
    description: SNMP Write Community of the device.
    type: str
  snmpRetry:
    description: SNMP retry count. Max value supported is 3. Default is Global SNMP
      retry (if exists) or 3.
    type: int
  snmpTimeout:
    description: SNMP timeout in seconds. Max value supported is 300. Default is Global
      SNMP timeout (if exists) or 5.
    type: int
  snmpUserName:
    description: SNMPV3 user name of the device.
    type: str
  snmpVersion:
    description: SNMP version. Values supported v2, v3. Default is v2.
    type: str
  type:
    description: Type of device being added.
    type: str
  updateMgmtIPaddressList:
    description: Network Device's updateMgmtIPaddressList.
    elements: dict
    suboptions:
      existMgmtIpAddress:
        description: ExistMgmtIpAddress IP Address of the device.
        type: str
      newMgmtIpAddress:
        description: New IP Address to be Updated.
        type: str
    type: list
  userName:
    description: CLI user name of the device.
    type: str
requirements:
- dnacentersdk >= 2.7.2
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Devices AddDevice2
  description: Complete reference of the AddDevice2 API.
  link: https://developer.cisco.com/docs/dna-center/#!add-device
- name: Cisco DNA Center documentation for Devices DeleteDeviceById
  description: Complete reference of the DeleteDeviceById API.
  link: https://developer.cisco.com/docs/dna-center/#!delete-device-by-id
- name: Cisco DNA Center documentation for Devices UpdateDeviceDetails
  description: Complete reference of the UpdateDeviceDetails API.
  link: https://developer.cisco.com/docs/dna-center/#!update-device-details
notes:
  - SDK Method used are
    devices.Devices.add_device,
    devices.Devices.delete_device_by_id,
    devices.Devices.sync_devices,

  - Paths used are
    post /dna/intent/api/v1/network-device,
    delete /dna/intent/api/v1/network-device/{id},
    put /dna/intent/api/v1/network-device,

  - Removed 'managementIpAddress' options in v4.3.0.
"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.network_device:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    cliTransport: string
    computeDevice: true
    enablePassword: string
    extendedDiscoveryInfo: string
    httpPassword: string
    httpPort: string
    httpSecure: true
    httpUserName: string
    ipAddress:
    - string
    merakiOrgId:
    - string
    netconfPort: string
    password: string
    serialNumber: string
    snmpAuthPassphrase: string
    snmpAuthProtocol: string
    snmpMode: string
    snmpPrivPassphrase: string
    snmpPrivProtocol: string
    snmpROCommunity: string
    snmpRWCommunity: string
    snmpRetry: 0
    snmpTimeout: 0
    snmpUserName: string
    snmpVersion: string
    type: string
    userName: string

- name: Update all
  cisco.dnac.network_device:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    cliTransport: string
    computeDevice: true
    enablePassword: string
    extendedDiscoveryInfo: string
    httpPassword: string
    httpPort: string
    httpSecure: true
    httpUserName: string
    ipAddress:
    - string
    merakiOrgId:
    - string
    netconfPort: string
    password: string
    serialNumber: string
    snmpAuthPassphrase: string
    snmpAuthProtocol: string
    snmpMode: string
    snmpPrivPassphrase: string
    snmpPrivProtocol: string
    snmpROCommunity: string
    snmpRWCommunity: string
    snmpRetry: 0
    snmpTimeout: 0
    snmpUserName: string
    snmpVersion: string
    type: string
    updateMgmtIPaddressList:
    - existMgmtIpAddress: string
      newMgmtIpAddress: string
    userName: string

- name: Delete by id
  cisco.dnac.network_device:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    cleanConfig: true
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
