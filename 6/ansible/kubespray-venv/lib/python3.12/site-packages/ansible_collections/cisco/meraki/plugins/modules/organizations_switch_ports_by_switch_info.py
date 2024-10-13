#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: organizations_switch_ports_by_switch_info
short_description: Information module for organizations _switch _ports _byswitch
description:
- Get all organizations _switch _ports _byswitch.
- List the switchports in an organization by switch.
version_added: '2.16.0'
extends_documentation_fragment:
  - cisco.meraki.module_info
  - cisco.meraki.module_info_pagination
author: Francisco Munoz (@fmunoz)
options:
  headers:
    description: Additional headers.
    type: dict
  organizationId:
    description:
    - OrganizationId path parameter. Organization ID.
    type: str
  perPage:
    description:
    - PerPage query parameter. The number of entries per page returned. Acceptable range is 3 - 50. Default is 50.
    type: int
  startingAfter:
    description:
    - >
      StartingAfter query parameter. A token used by the server to indicate the start of the page. Often this is a
      timestamp or an ID but it is not limited to those. This parameter should not be defined by client
      applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    type: str
  endingBefore:
    description:
    - >
      EndingBefore query parameter. A token used by the server to indicate the end of the page. Often this is a
      timestamp or an ID but it is not limited to those. This parameter should not be defined by client
      applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    type: str
  networkIds:
    description:
    - NetworkIds query parameter. Optional parameter to filter switchports by network.
    elements: str
    type: list
  portProfileIds:
    description:
    - PortProfileIds query parameter. Optional parameter to filter switchports belonging to the specified port profiles.
    elements: str
    type: list
  name:
    description:
    - >
      Name query parameter. Optional parameter to filter switchports belonging to switches by name. All returned
      switches will have a name that contains the search term or is an exact match.
    type: str
  mac:
    description:
    - >
      Mac query parameter. Optional parameter to filter switchports belonging to switches by MAC address. All
      returned switches will have a MAC address that contains the search term or is an exact match.
    type: str
  macs:
    description:
    - >
      Macs query parameter. Optional parameter to filter switchports by one or more MAC addresses belonging to
      devices. All switchports returned belong to MAC addresses of switches that are an exact match.
    elements: str
    type: list
  serial:
    description:
    - >
      Serial query parameter. Optional parameter to filter switchports belonging to switches by serial number. All
      returned switches will have a serial number that contains the search term or is an exact match.
    type: str
  serials:
    description:
    - >
      Serials query parameter. Optional parameter to filter switchports belonging to switches with one or more
      serial numbers. All switchports returned belong to serial numbers of switches that are an exact match.
    elements: str
    type: list
  configurationUpdatedAfter:
    description:
    - >
      ConfigurationUpdatedAfter query parameter. Optional parameter to filter results by switches where the
      configuration has been updated after the given timestamp.
    type: str
requirements:
- meraki >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco Meraki documentation for switch getOrganizationSwitchPortsBySwitch
  description: Complete reference of the getOrganizationSwitchPortsBySwitch API.
  link: https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-ports-by-switch
notes:
  - SDK Method used are
    switch.Switch.get_organization_switch_ports_by_switch,

  - Paths used are
    get /organizations/{organizationId}/switch/ports/bySwitch,
"""

EXAMPLES = r"""
- name: Get all organizations _switch _ports _byswitch
  cisco.meraki.organizations_switch_ports_by_switch_info:
    meraki_api_key: "{{meraki_api_key}}"
    meraki_base_url: "{{meraki_base_url}}"
    meraki_single_request_timeout: "{{meraki_single_request_timeout}}"
    meraki_certificate_path: "{{meraki_certificate_path}}"
    meraki_requests_proxy: "{{meraki_requests_proxy}}"
    meraki_wait_on_rate_limit: "{{meraki_wait_on_rate_limit}}"
    meraki_nginx_429_retry_wait_time: "{{meraki_nginx_429_retry_wait_time}}"
    meraki_action_batch_retry_wait_time: "{{meraki_action_batch_retry_wait_time}}"
    meraki_retry_4xx_error: "{{meraki_retry_4xx_error}}"
    meraki_retry_4xx_error_wait_time: "{{meraki_retry_4xx_error_wait_time}}"
    meraki_maximum_retries: "{{meraki_maximum_retries}}"
    meraki_output_log: "{{meraki_output_log}}"
    meraki_log_file_prefix: "{{meraki_log_file_prefix}}"
    meraki_log_path: "{{meraki_log_path}}"
    meraki_print_console: "{{meraki_print_console}}"
    meraki_suppress_logging: "{{meraki_suppress_logging}}"
    meraki_simulate: "{{meraki_simulate}}"
    meraki_be_geo_id: "{{meraki_be_geo_id}}"
    meraki_use_iterator_for_get_pages: "{{meraki_use_iterator_for_get_pages}}"
    meraki_inherit_logging_config: "{{meraki_inherit_logging_config}}"
    perPage: 0
    startingAfter: string
    endingBefore: string
    networkIds: []
    portProfileIds: []
    name: string
    mac: string
    macs: []
    serial: string
    serials: []
    configurationUpdatedAfter: string
    organizationId: string
    total_pages: -1
    direction: next
  register: result

"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "mac": "string",
        "model": "string",
        "name": "string",
        "network": {
          "id": "string",
          "name": "string"
        },
        "ports": [
          {
            "accessPolicyType": "string",
            "allowedVlans": "string",
            "enabled": true,
            "linkNegotiation": "string",
            "name": "string",
            "poeEnabled": true,
            "portId": "string",
            "rstpEnabled": true,
            "stickyMacAllowList": [
              "string"
            ],
            "stickyMacAllowListLimit": 0,
            "stpGuard": "string",
            "tags": [
              "string"
            ],
            "type": "string",
            "vlan": 0,
            "voiceVlan": 0
          }
        ],
        "serial": "string"
      }
    ]
"""
