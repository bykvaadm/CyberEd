#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: license_device_license_summary_info
short_description: Information module for License Device License Summary
description:
- Get all License Device License Summary.
- Show license summary of devices.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  page_number:
    description:
    - Page_number query parameter. Page number of response.
    type: float
  order:
    description:
    - Order query parameter. Sorting order.
    type: str
  sort_by:
    description:
    - Sort_by query parameter. Sort result by field.
    type: str
  dna_level:
    description:
    - Dna_level query parameter. Device Cisco DNA license level. The valid values are Advantage, Essentials.
    type: str
  device_type:
    description:
    - Device_type query parameter. Type of device. The valid values are Routers, Switches and Hubs, Wireless Controller.
    type: str
  limit:
    description:
    - Limit query parameter.
    type: float
  registration_status:
    description:
    - >
      Registration_status query parameter. Smart license registration status of device. The valid values are
      Unknown, NA, Unregistered, Registered, Registration_expired, Reservation_in_progress, Registered_slr,
      Registered_plr, Registered_satellite.
    type: str
  virtual_account_name:
    description:
    - Virtual_account_name query parameter. Name of virtual account.
    type: str
  smart_account_id:
    description:
    - Smart_account_id query parameter. Id of smart account.
    type: str
  device_uuid:
    description:
    - Device_uuid query parameter. Id of device.
    type: str
requirements:
- dnacentersdk >= 2.7.2
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Licenses DeviceLicenseSummary
  description: Complete reference of the DeviceLicenseSummary API.
  link: https://developer.cisco.com/docs/dna-center/#!device-license-summary
notes:
  - SDK Method used are
    licenses.Licenses.device_license_summary,

  - Paths used are
    get /dna/intent/api/v1/licenses/device/summary,

"""

EXAMPLES = r"""
- name: Get all License Device License Summary
  cisco.dnac.license_device_license_summary_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    page_number: 0
    order: string
    sort_by: string
    dna_level: string
    device_type: string
    limit: 0
    registration_status: string
    virtual_account_name: string
    smart_account_id: string
    device_uuid: string
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
          "authorization_status": "string",
          "last_updated_time": "string",
          "is_performance_allowed": true,
          "sle_auth_code": "string",
          "throughput_level": "string",
          "hsec_status": "string",
          "device_uuid": "string",
          "site": "string",
          "total_access_point_count": 0,
          "model": "string",
          "is_wireless_capable": true,
          "registration_status": "string",
          "sle_state": "string",
          "performance_license": "string",
          "license_mode": "string",
          "is_license_expired": true,
          "software_version": "string",
          "reservation_status": "string",
          "is_wireless": true,
          "network_license": "string",
          "evaluation_license_expiry": "string",
          "wireless_capable_network_license": "string",
          "device_name": "string",
          "device_type": "string",
          "dna_level": "string",
          "virtual_account_name": "string",
          "last_successful_rum_usage_upload_time": "string",
          "ip_address": "string",
          "wireless_capable_dna_license": "string",
          "mac_address": "string",
          "customer_tag1": "string",
          "customer_tag2": "string",
          "customer_tag3": "string",
          "customer_tag4": "string",
          "smart_account_name": "string"
        }
      ],
      "version": "string"
    }
"""
