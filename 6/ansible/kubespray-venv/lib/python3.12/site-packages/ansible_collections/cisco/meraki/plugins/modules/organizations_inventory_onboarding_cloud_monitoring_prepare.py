#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: organizations_inventory_onboarding_cloud_monitoring_prepare
short_description: Resource module for organizations _inventory _onboarding _cloudmonitoring _prepare
description:
- Manage operation create of the resource organizations _inventory _onboarding _cloudmonitoring _prepare.
- >
   Initiates or updates an import session. An import ID will be generated and used when you are ready to commit the
   import.
version_added: '2.16.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  devices:
    description: A set of devices to import (or update).
    elements: dict
    suboptions:
      sudi:
        description: Device SUDI certificate.
        type: str
      tunnel:
        description: TLS Related Parameters.
        suboptions:
          certificateName:
            description: Name of the configured TLS certificate.
            type: str
          localInterface:
            description: Number of the vlan expected to be used to connect to the cloud.
            type: int
          loopbackNumber:
            description: Number of the configured Loopback Interface used for TLS overlay.
            type: int
          name:
            description: Name of the configured TLS tunnel.
            type: str
        type: dict
      user:
        description: User parameters.
        suboptions:
          username:
            description: The name of the device user for Meraki monitoring.
            type: str
        type: dict
      vty:
        description: VTY Related Parameters.
        suboptions:
          accessList:
            description: AccessList details.
            suboptions:
              vtyIn:
                description: VTY in ACL.
                suboptions:
                  name:
                    description: Name.
                    type: str
                type: dict
              vtyOut:
                description: VTY out ACL.
                suboptions:
                  name:
                    description: Name.
                    type: str
                type: dict
            type: dict
          authentication:
            description: VTY AAA authentication.
            suboptions:
              group:
                description: Group Details.
                suboptions:
                  name:
                    description: Group Name.
                    type: str
                type: dict
            type: dict
          authorization:
            description: VTY AAA authorization.
            suboptions:
              group:
                description: Group Details.
                suboptions:
                  name:
                    description: Group Name.
                    type: str
                type: dict
            type: dict
          endLineNumber:
            description: Ending line VTY number.
            type: int
          rotaryNumber:
            description: SSH rotary number.
            type: int
          startLineNumber:
            description: Starting line VTY number.
            type: int
        type: dict
    type: list
  organizationId:
    description: OrganizationId path parameter. Organization ID.
    type: str
requirements:
- meraki >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco Meraki documentation for organizations createOrganizationInventoryOnboardingCloudMonitoringPrepare
  description: Complete reference of the createOrganizationInventoryOnboardingCloudMonitoringPrepare API.
  link: https://developer.cisco.com/meraki/api-v1/#!create-organization-inventory-onboarding-cloud-monitoring-prepare
notes:
  - SDK Method used are
    organizations.Organizations.create_organization_inventory_onboarding_cloud_monitoring_prepare,

  - Paths used are
    post /organizations/{organizationId}/inventory/onboarding/cloudMonitoring/prepare,
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.organizations_inventory_onboarding_cloud_monitoring_prepare:
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
    devices:
    - sudi: "-----BEGIN CERTIFICATE-----\n        MIIDyTCCArGgAwIBAgIKBBNXOVCGU1YztjANBgkqhkiG9w0BAQsFADAnMQ4wDAYD\n\
        \        VQQKEwVDaXNjbzEVMBMGA1UEAxMMQUNUMiBTVURJIENBMB4XDTIxMDUzMTEzNTUx\n  \
        \      NVoXDTI5MDUxNDIwMjU0MVowbTEpMCcGA1UEBRMgUElEOkM5MjAwTC0yNFAtNEcg\n    \
        \    U046SkFFMjUyMjBSMksxDjAMBgNVBAoTBUNpc2NvMRgwFgYDVQQLEw9BQ1QtMiBM\n      \
        \  aXRlIFNVREkxFjAUBgNVBAMTDUM5MjAwTC0yNFAtNEcwggEiMA0GCSqGSIb3DQEB\n        AQUAA4IBDwAwggEKAoIBAQDaUPxW76g...
        \        TR1TuP36bHh13X3vtGiDsCD88Ci2TZIqd/EDkkc7v9ipUUYVVH+YDrPt2Aukb1PH\n  \
        \      D6K0R+KhgEzRo5x54TlU6oWvjUpwNZUwwdhMWIQaUVkMyZBYNy0jGPLO8jwZhyBg\n    \
        \    1Fneybr9pwedGbLrAaz+gdEikB8B4a/fvPjVfL5Ngb4QRjFqWuE+X3nLc0kHedep\n      \
        \  6nfgpUNXMlStVm5nIXKP6OjmzfCHPYh9L2Ehs1TrSk1ser9Ofx0ZMVL/jBZR2EIj\n        OZ8tH6KlX2/B2pbSPIO6kD5c4UA8Cf1...
        \        VR0PAQH/BAQDAgXgMAwGA1UdEwEB/wQCMAAwHwYDVR0jBBgwFoAUSNjx8cJw1Vu7\n  \
        \      fHMJk6+4uDAD+H8wTQYDVR0RBEYwRKBCBgkrBgEEAQkVAgOgNRMzQ2hpcElEPVVV\n    \
        \    VUNNaElGcUVFMklFUUVBQWNBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUE9MB0GA1Ud\n      \
        \  DgQWBBRdhMkFD/z5hokaQeLbaRsp4hkvbzANBgkqhkiG9w0BAQsFAAOCAQEAMtuh\n        YpBz4xEZ7YdJsLpw67Q0TTJGnTBRpzA...
        \        OwmH/iZ+tDfYQ3W3ElWTW93871DkuW4WQIfbnoHg/F7bF0DKYVkD3rpZjyz3NhzH\n  \
        \      d7cjTdJXQ85bTAOXDuxKH3qewrXxxOGXgh3I6NUq0UwMTWh84lND7Jl+ZAQkYNS2\n    \
        \    iHanTZFQBk3ML0NUb7fKDYGRTZRqwQ/upIO4S6LV1cxH/6V0qbMy3sCSHZoMLrW3\n      \
        \  0m3M6yKpe5+VZzHZwmWdUf3Ot+zKjhveK5/YNsMIASdvtvymxUizq2Hr1hvR/kPc\n        p1vuyWxipU8JfzOh/A==\n\
        \        -----END CERTIFICATE-----\n        "
      tunnel:
        certificateName: DeviceSUDI
        localInterface: 1
        loopbackNumber: 1000
        name: MERAKI
      user:
        username: Meraki
      vty:
        accessList:
          vtyIn:
            name: MERAKI_IN
          vtyOut:
            name: MERAKI_OUT
        authentication:
          group:
            name: ''
        authorization:
          group:
            name: MERAKI
        endLineNumber: 17
        rotaryNumber: 50
        startLineNumber: 16
    organizationId: string

"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: list
  sample: >
    [
      {
        "configParams": {
          "cloudStaticIp": "string",
          "tunnel": {
            "host": "string",
            "mode": "string",
            "name": "string",
            "port": "string",
            "rootCertificate": {
              "content": "string",
              "name": "string"
            }
          },
          "user": {
            "publicKey": "string",
            "secret": {
              "hash": "string"
            },
            "username": "string"
          }
        },
        "deviceId": "string",
        "message": "string",
        "status": "string",
        "udi": "string"
      }
    ]
"""
