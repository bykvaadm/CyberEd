#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: networks_appliance_static_routes
short_description: Resource module for networks _appliance _static _routes
description:
- Manage operations create, update and delete of the resource networks _appliance _static _routes.
- Add a static route for an MX or teleworker network.
- Delete a static route from an MX or teleworker network.
- Update a static route for an MX or teleworker network.
version_added: '2.16.0'
extends_documentation_fragment:
  - cisco.meraki.module
author: Francisco Munoz (@fmunoz)
options:
  enabled:
    description: The enabled state of the static route.
    type: bool
  fixedIpAssignments:
    description: The DHCP fixed IP assignments on the static route. This should be an
      object that contains mappings from MAC addresses to objects that themselves each
      contain "ip" and "name" string fields. See the sample request/response for more
      details.
    type: dict
  gatewayIp:
    description: The gateway IP (next hop) of the static route.
    type: str
  gatewayVlanId:
    description: The gateway IP (next hop) VLAN ID of the static route.
    type: str
  name:
    description: The name of the new static route.
    type: str
  networkId:
    description: NetworkId path parameter. Network ID.
    type: str
  reservedIpRanges:
    description: The DHCP reserved IP ranges on the static route.
    elements: dict
    suboptions:
      comment:
        description: A text comment for the reserved range.
        type: str
      end:
        description: The last IP in the reserved range.
        type: str
      start:
        description: The first IP in the reserved range.
        type: str
    type: list
  staticRouteId:
    description: StaticRouteId path parameter. Static route ID.
    type: str
  subnet:
    description: The subnet of the static route.
    type: str
requirements:
- meraki >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco Meraki documentation for appliance createNetworkApplianceStaticRoute
  description: Complete reference of the createNetworkApplianceStaticRoute API.
  link: https://developer.cisco.com/meraki/api-v1/#!create-network-appliance-static-route
- name: Cisco Meraki documentation for appliance deleteNetworkApplianceStaticRoute
  description: Complete reference of the deleteNetworkApplianceStaticRoute API.
  link: https://developer.cisco.com/meraki/api-v1/#!delete-network-appliance-static-route
- name: Cisco Meraki documentation for appliance updateNetworkApplianceStaticRoute
  description: Complete reference of the updateNetworkApplianceStaticRoute API.
  link: https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-static-route
notes:
  - SDK Method used are
    appliance.Appliance.create_network_appliance_static_route,
    appliance.Appliance.delete_network_appliance_static_route,
    appliance.Appliance.update_network_appliance_static_route,

  - Paths used are
    post /networks/{networkId}/appliance/staticRoutes,
    delete /networks/{networkId}/appliance/staticRoutes/{staticRouteId},
    put /networks/{networkId}/appliance/staticRoutes/{staticRouteId},
"""

EXAMPLES = r"""
- name: Create
  cisco.meraki.networks_appliance_static_routes:
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
    meraki_caller: "{{meraki_caller}}"
    meraki_use_iterator_for_get_pages: "{{meraki_use_iterator_for_get_pages}}"
    meraki_inherit_logging_config: "{{meraki_inherit_logging_config}}"
    state: present
    gatewayIp: 1.2.3.5
    name: My route
    networkId: string
    subnet: 192.168.1.0/24

- name: Update by id
  cisco.meraki.networks_appliance_static_routes:
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
    meraki_caller: "{{meraki_caller}}"
    meraki_use_iterator_for_get_pages: "{{meraki_use_iterator_for_get_pages}}"
    meraki_inherit_logging_config: "{{meraki_inherit_logging_config}}"
    state: present
    fixedIpAssignments:
      22:33:44:55:66:77:
        ip: 1.2.3.4
        name: Some client name
    name: My route
    networkId: string
    reservedIpRanges:
    - comment: A reserved IP range
      end: 192.168.1.1
      start: 192.168.1.0
    staticRouteId: string
    subnet: 192.168.1.0/24

- name: Delete by id
  cisco.meraki.networks_appliance_static_routes:
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
    meraki_caller: "{{meraki_caller}}"
    meraki_use_iterator_for_get_pages: "{{meraki_use_iterator_for_get_pages}}"
    meraki_inherit_logging_config: "{{meraki_inherit_logging_config}}"
    state: absent
    networkId: string
    staticRouteId: string

"""
RETURN = r"""
meraki_response:
  description: A dictionary or list with the response returned by the Cisco Meraki Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
