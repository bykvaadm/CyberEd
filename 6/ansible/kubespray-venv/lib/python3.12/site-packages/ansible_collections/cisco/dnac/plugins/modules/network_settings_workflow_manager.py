#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to perform operations on global pool, reserve pool and network in Cisco Catalyst Center."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ['Muthu Rakesh, Madhan Sankaranarayanan']

DOCUMENTATION = r"""
---
module: network_settings_workflow_manager
short_description: Resource module for IP Address pools and network functions
description:
- Manage operations on Global Pool, Reserve Pool, Network resources.
- API to create/update/delete global pool.
- API to reserve/update/delete an ip subpool from the global pool.
- API to update network settings for DHCP, Syslog, SNMP, NTP, Network AAA, Client and Endpoint AAA,
  and/or DNS center server settings.
version_added: '6.6.0'
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author: Muthu Rakesh (@MUTHU-RAKESH-27)
        Madhan Sankaranarayanan (@madhansansel)
options:
  config_verify:
    description: Set to True to verify the Cisco Catalyst Center after applying the playbook config.
    type: bool
    default: False
  state:
    description: The state of Cisco Catalyst Center after module completion.
    type: str
    choices: [ merged, deleted ]
    default: merged
  config:
    description:
    - List of details of global pool, reserved pool, network being managed.
    type: list
    elements: dict
    required: true
    suboptions:
      global_pool_details:
        description: Manages IPv4 and IPv6 IP pools in the global level.
        type: dict
        suboptions:
          settings:
            description: Global Pool's settings.
            type: dict
            suboptions:
              ip_pool:
                description: Contains a list of global IP pool configurations.
                elements: dict
                type: list
                suboptions:
                  name:
                    description:
                    - Specifies the name assigned to the Global IP Pool.
                    - Required for the operations in the Global IP Pool.
                    - Length should be less than or equal to 100.
                    - Only letters, numbers and -_./ characters are allowed.
                    type: str
                  pool_type:
                    description: >
                      Includes both the Generic Ip Pool and Tunnel Ip Pool.
                      Generic - Used for general purpose within the network such as device
                                management or communication between the network devices.
                      Tunnel - Designated for the tunnel interfaces to encapsulate packets
                               within the network protocol. It is used in VPN connections,
                               GRE tunnels, or other types of overlay networks.
                    default: Generic
                    choices: [Generic, Tunnel]
                    type: str
                  ip_address_space:
                    description: IP address space either IPv4 or IPv6.
                    type: str
                  cidr:
                    description: >
                      Defines the IP pool's Classless Inter-Domain Routing block,
                      enabling systematic IP address distribution within a network.
                    type: str
                  gateway:
                    description: Serves as an entry or exit point for data traffic between networks.
                    type: str
                  dhcp_server_ips:
                    description: >
                      The DHCP server IPs responsible for automatically assigning IP addresses
                      and network configuration parameters to devices on a local network.
                    elements: str
                    type: list
                  dns_server_ips:
                    description: Responsible for translating domain names into corresponding IP addresses.
                    elements: str
                    type: list
                  prev_name:
                    description: >
                      The former identifier for the global pool. It should be used
                      exclusively when you need to update the global pool's name.
                    type: str

      reserve_pool_details:
        description: Reserved IP subpool details from the global pool.
        type: dict
        suboptions:
          site_name:
            description: >
              The name of the site provided as a path parameter, used
              to specify where the IP sub-pool will be reserved.
            type: str
          name:
            description:
            - Name of the reserve IP subpool.
            - Required for the operations in the Reserve IP Pool.
            - Length should be less than or equal to 100.
            - Only letters, numbers and -_./ characters are allowed.
            type: str
          pool_type:
            description: Type of the reserve ip sub pool.
                Generic - Used for general purpose within the network such as device
                          management or communication between the network devices.
                LAN - Used for the devices and the resources within the Local Area Network
                      such as device connectivity, internal communication, or services.
                Management - Used for the management purposes such as device management interfaces,
                             management access, or other administrative functions.
                Service - Used for the network services and application such as DNS (Domain Name System),
                          DHCP (Dynamic Host Configuration Protocol), NTP (Network Time Protocol).
                WAN - Used for the devices and resources with the Wide Area Network such as remote
                      sites interconnection with other network or services hosted within WAN.
            default: Generic
            choices: [Generic, LAN, Management, Service, WAN]
            type: str
          ipv6_address_space:
            description: >
              Determines whether both IPv6 and IPv4 inputs are required.
              If set to false, only IPv4 inputs are required.
              If set to true, both IPv6 and IPv4 inputs are required.
            type: bool
          ipv4_global_pool:
            description:
            - IP v4 Global pool address with cidr, example 175.175.0.0/16.
            - If both 'ipv6_global_pool' and 'ipv4_global_pool_name' are provided, the 'ipv4_global_pool' will be given priority.
            type: str
          ipv4_global_pool_name:
            description:
            - Specifies the name to be associated with the IPv4 Global IP Pool.
            - If both 'ipv4_global_pool' and 'ipv4_global_pool_name' are provided, the 'ipv4_global_pool' will be given priority.
            type: str
            version_added: 6.14.0
          ipv4_subnet:
            description: Indicates the IPv4 subnet address, for example, "175.175.0.0".
            type: str
          ipv4_prefix:
            description: ip4 prefix length is enabled or ipv4 total Host input is enabled
            type: bool
          ipv4_prefix_length:
            description: The ipv4 prefix length is required when ipv4_prefix value is true.
            type: int
          ipv4_total_host:
            description: The total number of hosts for IPv4, required when the 'ipv4_prefix' is set to false.
            type: int
          ipv4_gateway:
            description: Provides the gateway's IPv4 address, for example, "175.175.0.1".
            type: str
            version_added: 4.0.0
          ipv4_dhcp_servers:
            description: Specifies the IPv4 addresses for DHCP servers, for example, "1.1.1.1".
            elements: str
            type: list
          ipv4_dns_servers:
            description: Specifies the IPv4 addresses for DNS servers, for example, "4.4.4.4".
            elements: str
            type: list
          ipv6_dhcp_servers:
            description: >
              Specifies the IPv6 addresses for DHCP servers in the format.
              For example, "2001:0db8:0123:4567:89ab:cdef:0001:0001".
            elements: str
            type: list
          ipv6_dns_servers:
            description: >
              Specifies the IPv6 addresses for DNS servers.
              For example, "2001:0db8:0123:4567:89ab:cdef:0002:0002".
            elements: str
            type: list
          ipv6_gateway:
            description: >
              Provides the gateway's IPv6 address.
              For example, "2001:0db8:0123:4567:89ab:cdef:0003:0003".
            type: str
          ipv6_global_pool:
            description:
            - The ipv6_global_pool is a required when the ipv6_address_space is set to true.
            - It specifies the global IPv6 address pool using CIDR notation, such as "2001:db8:85a3::/64".
            - In cases where both ipv6_global_pool and ipv6_global_pool_name are specified, ipv6_global_pool will take precedence.
            type: str
          ipv6_global_pool_name:
            description:
            - Specifies the name assigned to the Ip v6 Global IP Pool.
            - If both 'ipv6_global_pool' and 'ipv6_global_pool_name' are provided, the 'ipv6_global_pool' will be given priority.
            type: str
            version_added: 6.14.0
          ipv6_subnet:
            description: IPv6 Subnet address, example 2001:db8:85a3:0:100.
            type: str
          ipv6_prefix:
            description: >
              Determines whether to enable the 'ipv6_prefix_length' or 'ipv6_total_host' input field.
              If IPv6 prefix value is true, the IPv6 prefix length input field is required,
              If it is false ipv6 total Host input is required.
            type: bool
          ipv6_prefix_length:
            description: Specifies the IPv6 prefix length. Required when 'ipv6_prefix' is set to true.
            type: int
          ipv6_total_host:
            description:
            - Specifies the total number of IPv6 hosts. Required when 'ipv6_prefix' is set to false.
            - Must specify a number of IPv6 IP addresses that is less than 256.
            type: int
          prev_name:
            description: The former name associated with the reserved IP sub-pool.
            type: str
          slaac_support:
            description: >
              Allows devices on IPv6 networks to self-configure their
              IP addresses autonomously, eliminating the need for manual setup.
            type: bool
      network_management_details:
        description: Set default network settings for the site
        type: list
        elements: dict
        suboptions:
          site_name:
            description: >
              The name of the site provided as a path parameter, used
              to specify where the IP sub-pool will be reserved. (eg Global/Chennai/Trill)
            type: str
          settings:
            description: Network management details settings.
            type: dict
            suboptions:
              network_aaa:
                description: Manages AAA (Authentication Authorization Accounting) for network devices.
                suboptions:
                  server_type:
                    description: Server type for managing AAA for network devices.
                    choices: [AAA, ISE]
                    type: str
                  protocol:
                    description: Protocol for AAA or ISE server.
                    choices: [RADIUS, TACACS]
                    default: RADIUS
                    type: str
                  pan_address:
                    description:
                    - PAN IP address for the ISE server.
                    - For example, 1.1.1.1.
                    type: str
                    version_added: 6.14.0
                  primary_server_address:
                    description:
                    - Primary IP address for the ISE/AAA server.
                    - For example, 1.1.1.2.
                    type: str
                    version_added: 6.14.0
                  secondary_server_address:
                    description:
                    - Secondary IP address for the AAA server.
                    - For example, 1.1.1.3.
                    type: str
                    version_added: 6.14.0
                  shared_secret:
                    description:
                    - Shared secret for ISE Server.
                    - Length of the shared secret should be atleast 4 characters.
                    type: str
                type: dict
              client_and_endpoint_aaa:
                description: Manages AAA (Authentication Authorization Accounting) for clients and endpoints.
                suboptions:
                  server_type:
                    description:
                    - Server type for managing AAA for client and endpoints.
                    choices: [AAA, ISE]
                    type: str
                  protocol:
                    description: Protocol for AAA or ISE server.
                    choices: [RADIUS, TACACS]
                    default: RADIUS
                    type: str
                  pan_address:
                    description:
                    - PAN IP address for the ISE server.
                    - For example, 1.1.1.1.
                    type: str
                    version_added: 6.14.0
                  primary_server_address:
                    description:
                    - Primary IP address for the ISE/AAA server.
                    - For example, 1.1.1.2.
                    type: str
                    version_added: 6.14.0
                  secondary_server_address:
                    description:
                    - Secondary IP address for the AAA server.
                    - For example, 1.1.1.3.
                    type: str
                    version_added: 6.14.0
                  shared_secret:
                    description:
                    - Shared secret for ISE Server.
                    - Length of the shared secret should be atleast 4 characters.
                    type: str
                type: dict
              dhcp_server:
                description: DHCP Server IP address (eg 1.1.1.4).
                elements: str
                type: list
              dns_server:
                description: DNS server details of the network under a specific site.
                suboptions:
                  domain_name:
                    description: Domain Name of DHCP (eg; cisco.com, cisco.net).
                    type: str
                  primary_ip_address:
                    description: Primary IP Address for DHCP (eg 2.2.2.2).
                    type: str
                  secondary_ip_address:
                    description: Secondary IP Address for DHCP (eg 3.3.3.3).
                    type: str
                type: dict
              ntp_server:
                description: IP address for NTP server under a specific site (eg 1.1.1.2).
                elements: str
                type: list
              timezone:
                description: Time zone of a specific site. (eg Africa/Abidjan/GMT).
                type: str
              message_of_the_day:
                description: Banner details under a specific site.
                suboptions:
                  banner_message:
                    description: Message for the banner (eg; Good day).
                    type: str
                  retain_existing_banner:
                    description: Retain existing banner message.
                    type: bool
                type: dict
              netflow_collector:
                description: Netflow collector details under a specific site.
                suboptions:
                  ip_address:
                    description: IP Address for NetFlow collector (eg 3.3.3.1).
                    type: str
                  port:
                    description: Port for NetFlow Collector (eg; 443).
                    type: int
                type: dict
              snmp_server:
                description: Snmp Server details under a specific site.
                suboptions:
                  configure_dnac_ip:
                    description: Configuration Cisco Catalyst Center IP for SNMP Server (eg true).
                    type: bool
                  ip_addresses:
                    description: IP Address for SNMP Server (eg 4.4.4.1).
                    elements: str
                    type: list
                type: dict
              syslog_server:
                description: syslog Server details under a specific site.
                suboptions:
                  configure_dnac_ip:
                    description: Configuration Cisco Catalyst Center IP for syslog server (eg true).
                    type: bool
                  ip_addresses:
                    description: IP Address for syslog server (eg 4.4.4.4).
                    elements: str
                    type: list
                type: dict
requirements:
- dnacentersdk >= 2.7.2
- python >= 3.9
notes:
  - SDK Method used are
    network_settings.NetworkSettings.create_global_pool,
    network_settings.NetworkSettings.delete_global_ip_pool,
    network_settings.NetworkSettings.update_global_pool,
    network_settings.NetworkSettings.release_reserve_ip_subpool,
    network_settings.NetworkSettings.reserve_ip_subpool,
    network_settings.NetworkSettings.update_reserve_ip_subpool,
    network_settings.NetworkSettings.update_network_v2,

  - Paths used are
    post /dna/intent/api/v1/global-pool,
    delete /dna/intent/api/v1/global-pool/{id},
    put /dna/intent/api/v1/global-pool,
    post /dna/intent/api/v1/reserve-ip-subpool/{siteId},
    delete /dna/intent/api/v1/reserve-ip-subpool/{id},
    put /dna/intent/api/v1/reserve-ip-subpool/{siteId},
    put /dna/intent/api/v2/network/{siteId},

"""

EXAMPLES = r"""
- name: Create global pool
  cisco.dnac.network_settings_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    dnac_log_level: "{{ dnac_log_level }}"
    state: merged
    config_verify: True
    config:
    - global_pool_details:
        settings:
          ip_pool:
          - name: string
            pool_type: Generic
            ip_address_space: string
            cidr: string
            gateway: string
            dhcp_server_ips: list
            dns_server_ips: list

- name: Create reserve an ip pool
  cisco.dnac.network_settings_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    dnac_log_level: "{{ dnac_log_level }}"
    state: merged
    config_verify: True
    config:
    - reserve_pool_details:
      - site_name: string
        name: string
        pool_type: LAN
        ipv6_address_space: True
        ipv4_global_pool: string
        ipv4_prefix: True
        ipv4_prefix_length: 9
        ipv4_subnet: string
        ipv6_prefix: True
        ipv6_prefix_length: 64
        ipv6_global_pool: string
        ipv6_subnet: string
        slaac_support: True

- name: Create reserve an ip pool using global pool name
  cisco.dnac.network_settings_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    dnac_log_level: "{{ dnac_log_level }}"
    state: merged
    config_verify: True
    config:
    - reserve_pool_details:
      - name: string
        site_name: string
        pool_type: LAN
        ipv6_address_space: True
        ipv4_global_pool_name: string
        ipv4_prefix: True
        ipv4_prefix_length: 9
        ipv4_subnet: string
        ipv6_prefix: True
        ipv6_prefix_length: 64
        ipv6_global_pool_name: string
        ipv6_subnet: string
        slaac_support: True

- name: Delete reserved pool
  cisco.dnac.network_settings_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    dnac_log_level: "{{ dnac_log_level }}"
    state: deleted
    config_verify: True
    config:
    - reserve_pool_details:
      - site_name: string
        name: string

- name: Manage the network functions
  cisco.dnac.network_settings_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    dnac_log_level: "{{ dnac_log_level }}"
    state: merged
    config_verify: True
    config:
    - network_management_details:
      - site_name: string
        settings:
          dhcp_server: list
          dns_server:
            domain_name: string
            primary_ip_address: string
            secondary_ip_address: string
          ntp_server: list
          timezone: string
          message_of_the_day:
            banner_message: string
            retain_existing_banner: bool
          netflow_collector:
            ip_address: string
            port: 443
          snmp_server:
            configure_dnac_ip: True
            ip_addresses: list
          syslog_server:
            configure_dnac_ip: True
            ip_addresses: list

- name: Adding the network_aaa and client_and_endpoint_aaa AAA server
  cisco.dnac.network_settings_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    dnac_log_level: "{{ dnac_log_level }}"
    state: merged
    config_verify: True
    config:
    - network_management_details:
      - site_name: string
        settings:
          network_aaa:
            server_type: AAA
            primary_server_address: string
            secondary_server_address: string
            protocol: string
          client_and_endpoint_aaa:
            server_type: AAA
            primary_server_address: string
            secondary_server_address: string
            protocol: string

- name: Adding the network_aaa and client_and_endpoint_aaa ISE server
  cisco.dnac.network_settings_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    dnac_log_level: "{{ dnac_log_level }}"
    state: merged
    config_verify: True
    config:
    - network_management_details:
      - site_name: string
        settings:
          network_aaa:
            server_type: ISE
            pan_address: string
            primary_server_address: string
            protocol: string
          client_and_endpoint_aaa:
            server_type: ISE
            pan_address: string
            primary_server_address: string
            protocol: string
"""

RETURN = r"""
# Case_1: Successful creation/updation/deletion of global pool
response_1:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "executionId": "string",
      "executionStatusUrl": "string",
      "message": "string"
    }

# Case_2: Successful creation/updation/deletion of reserve pool
response_2:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "executionId": "string",
      "executionStatusUrl": "string",
      "message": "string"
    }

# Case_3: Successful creation/updation of network
response_3:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "executionId": "string",
      "executionStatusUrl": "string",
      "message": "string"
    }
"""

import copy
import re
import time
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts,
    get_dict_result,
    dnac_compare_equality,
)


class NetworkSettings(DnacBase):
    """Class containing member attributes for network_settings_workflow_manager module"""

    def __init__(self, module):
        super().__init__(module)
        self.result["response"] = [
            {"globalPool": {"response": {}, "msg": {}}},
            {"reservePool": {"response": {}, "msg": {}}},
            {"network": {"response": {}, "msg": {}}}
        ]
        self.global_pool_obj_params = self.get_obj_params("GlobalPool")
        self.reserve_pool_obj_params = self.get_obj_params("ReservePool")
        self.network_obj_params = self.get_obj_params("Network")
        self.all_reserved_pool_details = {}

    def validate_input(self):
        """
        Checks if the configuration parameters provided in the playbook
        meet the expected structure and data types,
        as defined in the 'temp_spec' dictionary.

        Parameters:
            None

        Returns:
            self

        """

        if not self.config:
            self.msg = "config not available in playbook for validation"
            self.status = "success"
            return self

        # temp_spec is the specification for the expected structure of configuration parameters
        temp_spec = {
            "global_pool_details": {
                "type": 'dict',
                "settings": {
                    "type": 'dict',
                    "ip_pool": {
                        "type": 'list',
                        "elements": 'dict',
                        "ip_address_space": {"type": 'string'},
                        "dhcp_server_ips": {"type": 'list'},
                        "dns_server_ips": {"type": 'list'},
                        "gateway": {"type": 'string'},
                        "cidr": {"type": 'string'},
                        "name": {"type": 'string'},
                        "prev_name": {"type": 'string'},
                        "pool_type": {"type": 'string', "choices": ["Generic", "Tunnel"]},
                    }
                }
            },
            "reserve_pool_details": {
                "type": 'list',
                "elements": 'dict',
                "name": {"type": 'string'},
                "prev_name": {"type": 'string'},
                "ipv6_address_space": {"type": 'bool'},
                "ipv4_global_pool": {"type": 'string'},
                "ipv4_prefix": {"type": 'bool'},
                "ipv4_prefix_length": {"type": 'string'},
                "ipv4_subnet": {"type": 'string'},
                "ipv4_gateway": {"type": 'string'},
                "ipv4_dhcp_servers": {"type": 'list'},
                "ipv4_dns_servers": {"type": 'list'},
                "ipv6_global_pool": {"type": 'string'},
                "ipv6_prefix": {"type": 'bool'},
                "ipv6_prefix_length": {"type": 'integer'},
                "ipv6_subnet": {"type": 'string'},
                "ipv6_gateway": {"type": 'string'},
                "ipv6_dhcp_servers": {"type": 'list'},
                "ipv6_dns_servers": {"type": 'list'},
                "ipv4_total_host": {"type": 'integer'},
                "ipv6_total_host": {"type": 'integer'},
                "slaac_support": {"type": 'bool'},
                "site_name": {"type": 'string'},
                "pool_type": {
                    "type": 'string',
                    "choices": ["Generic", "LAN", "Management", "Service", "WAN"]
                },
            },
            "network_management_details": {
                "type": 'list',
                "elements": 'dict',
                "settings": {
                    "type": 'dict',
                    "dhcp_server": {"type": 'list'},
                    "dns_server": {
                        "type": 'dict',
                        "domain_name": {"type": 'string'},
                        "primary_ip_address": {"type": 'string'},
                        "secondary_ip_address": {"type": 'string'}
                    },
                    "syslog_server": {
                        "type": 'dict',
                        "ip_addresses": {"type": 'list'},
                        "configure_dnac_ip": {"type": 'bool'}
                    },
                    "snmp_server": {
                        "type": 'dict',
                        "ip_addresses": {"type": 'list'},
                        "configure_dnac_ip": {"type": 'bool'}
                    },
                    "netflow_collector": {
                        "type": 'dict',
                        "ip_address": {"type": 'string'},
                        "port": {"type": 'integer'},
                    },
                    "timezone": {"type": 'string'},
                    "ntp_server": {"type": 'list'},
                    "message_of_the_day": {
                        "type": 'dict',
                        "banner_message": {"type": 'string'},
                        "retain_existing_banner": {"type": 'bool'},
                    },
                    "network_aaa": {
                        "type": 'dict',
                        "server_type": {"type": 'string', "choices": ["ISE", "AAA"]},
                        "pan_address": {"type": 'string'},
                        "primary_server_address": {"type": 'string'},
                        "secondary_server_address": {"type": 'string'},
                        "protocol": {"type": 'string', "choices": ["RADIUS", "TACACS"]},
                        "shared_secret": {"type": 'string'}
                    },
                    "client_and_endpoint_aaa": {
                        "type": 'dict',
                        "server_type": {"type": 'string', "choices": ["ISE", "AAA"]},
                        "pan_address": {"type": 'string'},
                        "primary_server_address": {"type": 'string'},
                        "secondary_server_address": {"type": 'string'},
                        "protocol": {"type": 'string', "choices": ["RADIUS", "TACACS"]},
                        "shared_secret": {"type": 'string'}
                    }
                },
                "site_name": {"type": 'string'},
            }
        }

        # Validate playbook params against the specification (temp_spec)
        valid_temp, invalid_params = validate_list_of_dicts(self.config, temp_spec)
        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format("\n".join(invalid_params))
            self.status = "failed"
            return self

        self.validated_config = valid_temp
        self.log("Successfully validated playbook config params: {0}".format(valid_temp), "INFO")
        self.msg = "Successfully validated input from the playbook"
        self.status = "success"
        return self

    def requires_update(self, have, want, obj_params):
        """
        Check if the template config given requires update by comparing
        current information wih the requested information.

        This method compares the current global pool, reserve pool,
        or network details from Cisco Catalyst Center with the user-provided details
        from the playbook, using a specified schema for comparison.

        Parameters:
            have (dict) - Current information from the Cisco Catalyst Center
                          (global pool, reserve pool, network details)
            want (dict) - Users provided information from the playbook
            obj_params (list of tuples) - A list of parameter mappings specifying which
                                          Cisco Catalyst Center parameters (dnac_param) correspond to
                                          the user-provided parameters (ansible_param).

        Returns:
            bool - True if any parameter specified in obj_params differs between
            current_obj and requested_obj, indicating that an update is required.
            False if all specified parameters are equal.

        """

        current_obj = have
        requested_obj = want
        self.log("Current State (have): {0}".format(current_obj), "DEBUG")
        self.log("Desired State (want): {0}".format(requested_obj), "DEBUG")

        return any(not dnac_compare_equality(current_obj.get(dnac_param),
                                             requested_obj.get(ansible_param))
                   for (dnac_param, ansible_param) in obj_params)

    def get_obj_params(self, get_object):
        """
        Get the required comparison obj_params value

        Parameters:
            get_object (str) - identifier for the required obj_params

        Returns:
            obj_params (list) - obj_params value for comparison.
        """

        try:
            if get_object == "GlobalPool":
                obj_params = [
                    ("ipPoolName", "ipPoolName"),
                    ("IpAddressSpace", "IpAddressSpace"),
                    ("dhcpServerIps", "dhcpServerIps"),
                    ("dnsServerIps", "dnsServerIps"),
                    ("gateway", "gateway"),
                ]
            elif get_object == "ReservePool":
                obj_params = [
                    ("name", "name"),
                    ("type", "type"),
                    ("ipv6AddressSpace", "ipv6AddressSpace"),
                    ("ipv4GateWay", "ipv4GateWay"),
                    ("ipv4DhcpServers", "ipv4DhcpServers"),
                    ("ipv4DnsServers", "ipv4DnsServers"),
                    ("ipv6GateWay", "ipv6GateWay"),
                    ("ipv6DhcpServers", "ipv6DhcpServers"),
                    ("ipv6DnsServers", "ipv6DnsServers"),
                    ("ipv4TotalHost", "ipv4TotalHost"),
                    ("slaacSupport", "slaacSupport")
                ]
            elif get_object == "Network":
                obj_params = [
                    ("settings", "settings"),
                    ("site_name", "site_name")
                ]
            else:
                raise ValueError("Received an unexpected value for 'get_object': {0}"
                                 .format(get_object))
        except Exception as msg:
            self.log("Received exception: {0}".format(msg), "CRITICAL")

        return obj_params

    def get_site_id(self, site_name):
        """
        Get the site id from the site name.
        Use check_return_status() to check for failure

        Parameters:
            site_name (str) - Site name

        Returns:
            str or None - The Site Id if found, or None if not found or error
        """

        try:
            response = self.dnac._exec(
                family="sites",
                function='get_site',
                op_modifies=True,
                params={"name": site_name},
            )
            self.log("Received API response from 'get_site': {0}".format(response), "DEBUG")
            if not response:
                self.log("Failed to retrieve the site ID for the site name: {0}"
                         .format(site_name), "ERROR")
                return None

            _id = response.get("response")[0].get("id")
            self.log("Site ID for site name '{0}': {1}".format(site_name, _id), "DEBUG")
        except Exception as msg:
            self.log("Exception occurred while retrieving site_id from the site_name: {0}"
                     .format(msg), "CRITICAL")
            return None

        return _id

    def get_global_pool_params(self, pool_info):
        """
        Process Global Pool params from playbook data for Global Pool config in Cisco Catalyst Center

        Parameters:
            pool_info (dict) - Playbook data containing information about the global pool

        Returns:
            dict or None - Processed Global Pool data in a format suitable
            for Cisco Catalyst Center configuration, or None if pool_info is empty.
        """

        if not pool_info:
            self.log("Global Pool is empty", "INFO")
            return None

        self.log("Global Pool Details: {0}".format(pool_info), "DEBUG")
        global_pool = {
            "dhcpServerIps": pool_info.get("dhcpServerIps"),
            "dnsServerIps": pool_info.get("dnsServerIps"),
            "ipPoolCidr": pool_info.get("ipPoolCidr"),
            "ipPoolName": pool_info.get("ipPoolName"),
            "type": pool_info.get("ipPoolType").capitalize()
        }
        self.log("Formated global pool details: {0}".format(global_pool), "DEBUG")
        # global_ippool = global_pool.get("settings").get("ippool")[0]
        if pool_info.get("ipv6") is False:
            global_pool.update({"IpAddressSpace": "IPv4"})
        else:
            global_pool.update({"IpAddressSpace": "IPv6"})

        self.log("ip_address_space: {0}".format(global_pool.get("IpAddressSpace")), "DEBUG")
        if not pool_info["gateways"]:
            global_pool.update({"gateway": ""})
        else:
            global_pool.update({"gateway": pool_info.get("gateways")[0]})

        return global_pool

    def get_reserve_pool_params(self, pool_info):
        """
        Process Reserved Pool parameters from playbook data
        for Reserved Pool configuration in Cisco Catalyst Center

        Parameters:
            pool_info (dict) - Playbook data containing information about the reserved pool

        Returns:
            reserve_pool (dict) - Processed Reserved pool data
            in the format suitable for the Cisco Catalyst Center config
        """

        reserve_pool = {
            "name": pool_info.get("groupName"),
            "site_id": pool_info.get("siteId"),
        }
        pool_info_ippools = pool_info.get("ipPools")
        pool_info_length = len(pool_info_ippools)

        # If the reserved pool has only IPv4, pool_info_length will be 1.
        # If the reserved pool has both IPv4 and IPv6, pool_info_length will be 2.
        if pool_info_length == 1:
            reserve_pool.update({
                "ipv4DhcpServers": pool_info_ippools[0].get("dhcpServerIps"),
                "ipv4DnsServers": pool_info_ippools[0].get("dnsServerIps"),
                "ipv6AddressSpace": "False"
            })
            if pool_info_ippools[0].get("gateways") != []:
                reserve_pool.update({"ipv4GateWay": pool_info_ippools[0].get("gateways")[0]})
            else:
                reserve_pool.update({"ipv4GateWay": ""})
            reserve_pool.update({"ipv6AddressSpace": "False"})
        else:

            # If the ipv6 flag is set in the second element, ipv4_index will be 0 and ipv6_index will be 1.
            # If the ipv6 flag is set in the first element, ipv4_index will be 1 and ipv6_index will be 0.
            if not pool_info_ippools[0].get("ipv6"):
                ipv4_index = 0
                ipv6_index = 1
            else:
                ipv4_index = 1
                ipv6_index = 0

            reserve_pool.update({
                "ipv4DhcpServers": pool_info_ippools[ipv4_index].get("dhcpServerIps"),
                "ipv4DnsServers": pool_info_ippools[ipv4_index].get("dnsServerIps"),
                "ipv6AddressSpace": "True",
                "ipv6Prefix": "True",
                "ipv6DnsServers": pool_info_ippools[ipv6_index].get("dnsServerIps"),
                "ipv6DhcpServers": pool_info_ippools[ipv6_index].get("dhcpServerIps")
            })
            if pool_info_ippools[ipv4_index].get("gateways") != []:
                reserve_pool.update({"ipv4GateWay":
                                    pool_info_ippools[ipv4_index].get("gateways")[0]})
            else:
                reserve_pool.update({"ipv4GateWay": None})

            if pool_info_ippools[ipv6_index].get("gateways") != []:
                reserve_pool.update({
                    "ipv6GateWay": pool_info_ippools[ipv6_index].get("gateways")[0]
                })
            else:
                reserve_pool.update({"ipv6GateWay": ""})

            ippools_info = pool_info_ippools[ipv6_index].get("context")
            slaac_support_info = get_dict_result(ippools_info, "contextKey", "slaacSupport")
            if slaac_support_info is None or slaac_support_info.get("contextValue") == "false":
                reserve_pool.update({"slaacSupport": False})
            else:
                reserve_pool.update({"slaacSupport": True})

        self.log("Formatted reserve pool details: {0}".format(reserve_pool), "DEBUG")
        return reserve_pool

    def get_network_params(self, site_id):
        """
        Process the Network parameters from the playbook
        for Network configuration in Cisco Catalyst Center

        Parameters:
            site_id (str) - The Site ID for which network parameters are requested

        Returns:
            dict or None: Processed Network data in a format
            suitable for Cisco Catalyst Center configuration, or None
            if the response is not a dictionary or there was an error.
        """

        response = self.dnac._exec(
            family="network_settings",
            function='get_network_v2',
            op_modifies=True,
            params={"site_id": site_id}
        )
        self.log("Received API response from 'get_network_v2': {0}".format(response), "DEBUG")
        if not isinstance(response, dict):
            self.log("Failed to retrieve the network details - "
                     "Response is not a dictionary", "ERROR")
            return None

        # Extract various network-related details from the response
        all_network_details = response.get("response")
        dhcp_details = get_dict_result(all_network_details, "key", "dhcp.server")
        dns_details = get_dict_result(all_network_details, "key", "dns.server")
        snmp_details = get_dict_result(all_network_details, "key", "snmp.trap.receiver")
        syslog_details = get_dict_result(all_network_details, "key", "syslog.server")
        netflow_details = get_dict_result(all_network_details, "key", "netflow.collector")
        ntpserver_details = get_dict_result(all_network_details, "key", "ntp.server")
        timezone_details = get_dict_result(all_network_details, "key", "timezone.site")
        messageoftheday_details = get_dict_result(all_network_details, "key", "device.banner")
        network_aaa = get_dict_result(all_network_details, "key", "aaa.network.server.1")
        network_aaa2 = get_dict_result(all_network_details, "key", "aaa.network.server.2")
        network_aaa_pan = get_dict_result(all_network_details, "key", "aaa.server.pan.network")
        client_and_endpoint_aaa = get_dict_result(all_network_details, "key", "aaa.endpoint.server.1")
        client_and_endpoint_aaa2 = get_dict_result(all_network_details,
                                                   "key",
                                                   "aaa.endpoint.server.2")
        client_and_endpoint_aaa_pan = get_dict_result(all_network_details,
                                                      "key",
                                                      "aaa.server.pan.endpoint")

        # Prepare the network details for Cisco Catalyst Center configuration
        network_details = {
            "settings": {
                "snmpServer": {
                    "configureDnacIP": snmp_details.get("value")[0].get("configureDnacIP"),
                    "ipAddresses": snmp_details.get("value")[0].get("ipAddresses"),
                },
                "syslogServer": {
                    "configureDnacIP": syslog_details.get("value")[0].get("configureDnacIP"),
                    "ipAddresses": syslog_details.get("value")[0].get("ipAddresses"),
                },
                "timezone": timezone_details.get("value")[0],
            }
        }
        network_settings = network_details.get("settings")
        if dhcp_details and dhcp_details.get("value") != []:
            network_settings.update({"dhcpServer": dhcp_details.get("value")})
        else:
            network_settings.update({"dhcpServer": [""]})

        if dns_details is not None:
            network_settings.update({
                "dnsServer": {
                    "domainName": dns_details.get("value")[0].get("domainName"),
                    "primaryIpAddress": dns_details.get("value")[0].get("primaryIpAddress"),
                    "secondaryIpAddress": dns_details.get("value")[0].get("secondaryIpAddress")
                }
            })

        if ntpserver_details and ntpserver_details.get("value") != []:
            network_settings.update({"ntpServer": ntpserver_details.get("value")})
        else:
            network_settings.update({"ntpServer": [""]})

        netflow_collector_values = netflow_details.get("value")[0]
        ip_address = netflow_collector_values.get("ipAddress")
        port = netflow_collector_values.get("port")
        if port is None:
            port = "null"

        network_settings.update({
            "netflowcollector": {
                "ipAddress": ip_address,
                "port": port,
            }
        })

        if messageoftheday_details is not None:
            network_settings.update({
                "messageOfTheday": {
                    "bannerMessage": messageoftheday_details.get("value")[0].get("bannerMessage"),
                }
            })
            retain_existing_banner = messageoftheday_details.get("value")[0] \
                .get("retainExistingBanner")
            if retain_existing_banner is True:
                network_settings.get("messageOfTheday").update({
                    "retainExistingBanner": "true"
                })
            else:
                network_settings.get("messageOfTheday").update({
                    "retainExistingBanner": "false"
                })

        if network_aaa and network_aaa_pan:
            aaa_pan_value = network_aaa_pan.get("value")[0]
            aaa_value = network_aaa.get("value")[0]
            if aaa_pan_value == "None":
                network_settings.update({
                    "network_aaa": {
                        "network": aaa_value.get("ipAddress"),
                        "protocol": aaa_value.get("protocol"),
                        "ipAddress": network_aaa2.get("value")[0].get("ipAddress"),
                        "servers": "AAA"
                    }
                })
            else:
                network_settings.update({
                    "network_aaa": {
                        "network": aaa_pan_value,
                        "protocol": aaa_value.get("protocol"),
                        "ipAddress": aaa_value.get("ipAddress"),
                        "servers": "ISE"
                    }
                })

        if client_and_endpoint_aaa and client_and_endpoint_aaa_pan:
            aaa_pan_value = client_and_endpoint_aaa_pan.get("value")[0]
            aaa_value = client_and_endpoint_aaa.get("value")[0]
            if aaa_pan_value == "None":
                network_settings.update({
                    "clientAndEndpoint_aaa": {
                        "network": aaa_value.get("ipAddress"),
                        "protocol": aaa_value.get("protocol"),
                        "ipAddress": client_and_endpoint_aaa2.get("value")[0].get("ipAddress"),
                        "servers": "AAA"
                    }
                })
            else:
                network_settings.update({
                    "clientAndEndpoint_aaa": {
                        "network": aaa_pan_value,
                        "protocol": aaa_value.get("protocol"),
                        "ipAddress": aaa_value.get("ipAddress"),
                        "servers": "ISE"
                    }
                })

        network_settings_snmp = network_settings.get("snmpServer")
        if not network_settings_snmp.get("ipAddresses"):
            network_settings_snmp.update({"ipAddresses": []})

        network_settings_syslog = network_settings.get("syslogServer")
        if not network_settings_syslog.get("ipAddresses"):
            network_settings_syslog.update({"ipAddresses": []})

        self.log("Formatted playbook network details: {0}".format(network_details), "DEBUG")
        return network_details

    def get_reserved_ip_subpool(self, site_id):
        """
        Retrieve all the reserved IP subpool details from the Cisco Catalyst Center.

        Parameters:
            site_id (str) - The Site ID for which reserved pool details are requested.
            self (object) - The current object details.

        Returns:
            self (object) - The current object with updated desired Fabric Transits information.
        """

        value = 1
        self.all_reserved_pool_details.update({site_id: []})
        start_time = time.time()
        while True:
            response = self.dnac._exec(
                family="network_settings",
                function="get_reserve_ip_subpool",
                op_modifies=True,
                params={
                    "site_id": site_id,
                    "offset": value
                }
            )
            if not isinstance(response, dict):
                self.msg = "Error in getting reserve pool - Response is not a dictionary"
                self.log(self.msg, "CRITICAL")
                self.status = "exited"
                return self.check_return_status()

            reserve_pool_details = response.get("response")
            if not reserve_pool_details:
                self.log("No subpools are reserved in the site with ID - '{0}'."
                         .format(site_id), "DEBUG")
                return self

            self.all_reserved_pool_details.get(site_id).extend(reserve_pool_details)
            value += 25
            end_time = time.time()
            if (end_time - start_time) >= self.max_timeout:
                self.msg = (
                    "Max timeout of {0} sec has reached for the API 'get_reserved_ip_subpool' status."
                    .format(self.max_timeout)
                )
                self.status = "failed"
                break

        return self

    def global_pool_exists(self, name):
        """
        Check if the Global Pool with the given name exists

        Parameters:
            name (str) - The name of the Global Pool to check for existence

        Returns:
            dict - A dictionary containing information about the Global Pool's existence:
            - 'exists' (bool): True if the Global Pool exists, False otherwise.
            - 'id' (str or None): The ID of the Global Pool if it exists, or None if it doesn't.
            - 'details' (dict or None): Details of the Global Pool if it exists, else None.
        """

        global_pool = {
            "exists": False,
            "details": None,
            "id": None
        }
        value = 1
        while True:
            response = self.dnac._exec(
                family="network_settings",
                function="get_global_pool",
                params={"offset": value}
            )
            if not isinstance(response, dict):
                self.msg = "Failed to retrieve the global pool details - Response is not a dictionary"
                self.log(self.msg, "CRITICAL")
                self.status = "failed"
                return self.check_return_status()

            all_global_pool_details = response.get("response")
            if not all_global_pool_details:
                self.log("Global pool '{0}' does not exist".format(name), "INFO")
                return global_pool

            global_pool_details = get_dict_result(all_global_pool_details, "ipPoolName", name)
            if global_pool_details:
                self.log("Global pool found with name '{0}': {1}".format(name, global_pool_details), "INFO")
                global_pool.update({"exists": True})
                global_pool.update({"id": global_pool_details.get("id")})
                global_pool["details"] = self.get_global_pool_params(global_pool_details)
                break

            value += 25

        self.log("Formatted global pool details: {0}".format(global_pool), "DEBUG")
        return global_pool

    def reserve_pool_exists(self, name, site_name):
        """
        Check if the Reserved pool with the given name exists in a specific site
        Use check_return_status() to check for failure

        Parameters:
            name (str) - The name of the Reserved pool to check for existence.
            site_name (str) - The name of the site where the Reserved pool is located.

        Returns:
            dict - A dictionary containing information about the Reserved pool's existence:
            - 'exists' (bool): True if the Reserved pool exists in the specified site, else False.
            - 'id' (str or None): The ID of the Reserved pool if it exists, or None if it doesn't.
            - 'details' (dict or None): Details of the Reserved pool if it exists, or else None.
        """

        reserve_pool = {
            "exists": False,
            "details": None,
            "id": None,
            "success": True
        }
        site_id = self.get_site_id(site_name)
        self.log("Site ID for the site name {0}: {1}".format(site_name, site_id), "DEBUG")
        if not site_id:
            reserve_pool.update({"success": False})
            self.msg = "Failed to get the site id from the site name {0}".format(site_name)
            self.status = "failed"
            return reserve_pool

        if not self.all_reserved_pool_details.get(site_id):
            self.get_reserved_ip_subpool(site_id)

        if not self.all_reserved_pool_details.get(site_id):
            self.log("Reserved pool {0} does not exist in the site {1}"
                     .format(name, site_name), "DEBUG")
            return reserve_pool

        reserve_pool_details = get_dict_result(self.all_reserved_pool_details.get(site_id), "groupName", name)
        if reserve_pool_details:
            self.log("Reserve pool found with name '{0}' in the site '{1}': {2}"
                     .format(name, site_name, reserve_pool_details), "INFO")
            reserve_pool.update({"exists": True})
            reserve_pool.update({"id": reserve_pool_details.get("id")})
            reserve_pool.update({"details": self.get_reserve_pool_params(reserve_pool_details)})

        self.log("Reserved pool details: {0}".format(reserve_pool.get("details")), "DEBUG")
        self.log("Reserved pool id: {0}".format(reserve_pool.get("id")), "DEBUG")
        return reserve_pool

    def get_have_global_pool(self, global_pool_details):
        """
        Get the current Global Pool information from
        Cisco Catalyst Center based on the provided playbook details.
        check this API using check_return_status.

        Parameters:
            global_pool_details (dict) - Playbook details containing Global Pool configuration.

        Returns:
            self - The current object with updated information.
        """

        global_pool_settings = global_pool_details.get("settings")
        if global_pool_settings is None:
            self.msg = "settings in global_pool_details is missing in the playbook"
            self.status = "failed"
            return self

        global_pool_ippool = global_pool_settings.get("ip_pool")
        if global_pool_ippool is None:
            self.msg = "ip_pool in global_pool_details is missing in the playbook"
            self.status = "failed"
            return self

        global_pool = []
        global_pool_index = 0
        for pool_details in global_pool_ippool:
            name = pool_details.get("name")
            if name is None:
                self.msg = "Missing required parameter 'name' in global_pool_details"
                self.status = "failed"
                return self

            name_length = len(name)
            if name_length > 100:
                self.msg = "The length of the'name' in global_pool_details should be less or equal to 100."
                self.status = "failed"
                return self

            if " " in name:
                self.msg = "The 'name' in global_pool_details should not contain any spaces."
                self.status = "failed"
                return self

            pattern = r'^[\w\-./]+$'
            if not re.match(pattern, name):
                self.msg = "The 'name' in global_pool_details should contain only letters, numbers and -_./ characters."
                self.status = "failed"
                return self

            # If the Global Pool doesn't exist and a previous name is provided
            # Else try using the previous name
            global_pool.append(self.global_pool_exists(name))
            self.log("Global pool details of '{0}': {1}".format(name, global_pool[global_pool_index]), "DEBUG")
            prev_name = pool_details.get("prev_name")
            if global_pool[global_pool_index].get("exists") is False and \
                    prev_name is not None:
                global_pool.pop()
                global_pool.append(self.global_pool_exists(prev_name))
                if global_pool[global_pool_index].get("exists") is False:
                    self.msg = "Prev name {0} doesn't exist in global_pool_details".format(prev_name)
                    self.status = "failed"
                    return self

                global_pool[global_pool_index].update({"prev_name": name})
            global_pool_index += 1

        self.log("Global pool details: {0}".format(global_pool), "DEBUG")
        self.have.update({"globalPool": global_pool})
        self.msg = "Collecting the global pool details from the Cisco Catalyst Center"
        self.status = "success"
        return self

    def get_have_reserve_pool(self, reserve_pool_details):
        """
        Get the current Reserved Pool information from Cisco Catalyst Center
        based on the provided playbook details.
        Check this API using check_return_status

        Parameters:
            reserve_pool_details (list of dict) - Playbook details containing Reserved Pool configuration.

        Returns:
            self - The current object with updated information.
        """

        reserve_pool = []
        reserve_pool_index = 0
        for item in reserve_pool_details:
            name = item.get("name")
            if name is None:
                self.msg = "Missing required parameter 'name' in reserve_pool_details."
                self.status = "failed"
                return self

            name_length = len(name)
            if name_length > 100:
                self.msg = "The length of the 'name' in reserve_pool_details should be less or equal to 100."
                self.status = "failed"
                return self

            if " " in name:
                self.msg = "The 'name' in reserve_pool_details should not contain any spaces."
                self.status = "failed"
                return self

            pattern = r'^[\w\-./]+$'
            if not re.match(pattern, name):
                self.msg = "The 'name' in reserve_pool_details should contain only letters, numbers and -_./ characters."
                self.status = "failed"
                return self

            site_name = item.get("site_name")
            self.log("Site Name: {0}".format(site_name), "DEBUG")
            if site_name is None:
                self.msg = "Missing parameter 'site_name' in reserve_pool_details"
                self.status = "failed"
                return self

            # Check if the Reserved Pool exists in Cisco Catalyst Center
            # based on the provided name and site name
            reserve_pool.append(self.reserve_pool_exists(name, site_name))
            if not reserve_pool[reserve_pool_index].get("success"):
                return self.check_return_status()
            self.log("Reserved pool details for '{0}': {1}".format(name, reserve_pool[reserve_pool_index]), "DEBUG")

            # If the Reserved Pool doesn't exist and a previous name is provided
            # Else try using the previous name
            prev_name = item.get("prev_name")
            if reserve_pool[reserve_pool_index].get("exists") is False and \
                    prev_name is not None:
                reserve_pool.pop()
                reserve_pool.append(self.reserve_pool_exists(prev_name, site_name))
                if not reserve_pool[reserve_pool_index].get("success"):
                    return self.check_return_status()

                # If the previous name doesn't exist in Cisco Catalyst Center, return with error
                if reserve_pool[reserve_pool_index].get("exists") is False:
                    self.msg = "Prev name {0} doesn't exist in reserve_pool_details".format(prev_name)
                    self.status = "failed"
                    return self

            self.log("Reserved pool exists: {0}".format(reserve_pool[reserve_pool_index].get("exists")), "DEBUG")
            self.log("Reserved pool: {0}".format(reserve_pool[reserve_pool_index].get("details")), "DEBUG")

            # If reserve pool exist, convert ipv6AddressSpace to the required format (boolean)
            if reserve_pool[reserve_pool_index].get("exists"):
                reserve_pool_info = reserve_pool[reserve_pool_index].get("details")
                if reserve_pool_info.get("ipv6AddressSpace") == "False":
                    reserve_pool_info.update({"ipv6AddressSpace": False})
                else:
                    reserve_pool_info.update({"ipv6AddressSpace": True})

            reserve_pool_index += 1

        self.log("Reserved pool details: {0}".format(reserve_pool), "DEBUG")
        self.have.update({"reservePool": reserve_pool})
        self.msg = "Collected the reserve pool details from the Cisco Catalyst Center"
        self.status = "success"
        return self

    def get_have_network(self, network_details):
        """
        Get the current Network details from Cisco Catalyst
        Center based on the provided playbook details.

        Parameters:
            network_details (dict) - Playbook details containing Network Management configuration.

        Returns:
            self - The current object with updated Network information.
        """
        all_network_management_details = []
        for item in network_details:
            network = {}
            site_name = item.get("site_name")
            if site_name is None:
                site_name = "Global"
                item.update({"site_name": site_name})

            site_id = self.get_site_id(site_name)
            if site_id is None:
                self.msg = "The site with the name '{0}' is not available in the Catalyst Center".format(site_name)
                self.status = "failed"
                return self

            network["site_id"] = site_id
            network["net_details"] = self.get_network_params(site_id)
            self.log("Network details from the Catalyst Center for site '{0}': {1}".format(site_name, network), "DEBUG")
            all_network_management_details.append(network)

        self.have.update({"network": all_network_management_details})
        self.msg = "Collecting the network details from the Cisco Catalyst Center"
        self.status = "success"
        return self

    def get_have(self, config):
        """
        Get the current Global Pool Reserved Pool and Network details from Cisco Catalyst Center

        Parameters:
            config (dict) - Playbook details containing Global Pool,
            Reserved Pool, and Network Management configuration.

        Returns:
            self - The current object with updated Global Pool,
            Reserved Pool, and Network information.
        """

        global_pool_details = config.get("global_pool_details")
        if global_pool_details is not None:
            self.get_have_global_pool(global_pool_details).check_return_status()

        reserve_pool_details = config.get("reserve_pool_details")
        if reserve_pool_details is not None:
            self.get_have_reserve_pool(reserve_pool_details).check_return_status()

        network_details = config.get("network_management_details")
        if network_details is not None:
            self.get_have_network(network_details).check_return_status()

        self.log("Current State (have): {0}".format(self.have), "INFO")
        self.msg = "Successfully retrieved the details from the Cisco Catalyst Center"
        self.status = "success"
        return self

    def get_global_pool_cidr(self, global_pool_cidr, global_pool_name):
        """
        Get the Ipv4 or Ipv6 global pool cidr from the global pool name.

        Parameters:
            global_pool_cidr (dict) - Global pool cidr value of the current item.
            global_pool_name (dict) - Global pool name of the current item.

        Returns:
            global_pool_cidr (str) - Global pool cidr value of the current item.
        """

        if global_pool_cidr:
            return global_pool_cidr

        if not global_pool_name:
            self.msg = "Missing parameter 'Global Pool CIDR' or 'Global Pool name' is required under reserve_pool_details."
            self.status = "failed"
            return self.check_return_status()

        value = 1
        while True:
            response = self.dnac._exec(
                family="network_settings",
                function="get_global_pool",
                params={"offset": value}
            )
            value += 25
            if not isinstance(response, dict):
                self.msg = "Failed to retrieve the global pool details - Response is not a dictionary"
                self.log(self.msg, "CRITICAL")
                self.status = "failed"
                return self.check_return_status()

            all_global_pool_details = response.get("response")
            if not all_global_pool_details:
                self.log("Invalid global_pool_name '{0}' under reserve_pool_details".format(global_pool_name), "ERROR")
                self.msg = "No information found for the global pool named '{0}'".format(global_pool_name)
                self.status = "failed"
                return self.check_return_status()

            global_pool_details = get_dict_result(all_global_pool_details, "ipPoolName", global_pool_name)
            if global_pool_details:
                global_pool_cidr = global_pool_details.get("ipPoolCidr")
                self.log("Global pool found with name '{0}': {1}".format(global_pool_name, global_pool_details), "INFO")
                break

        self.log("Global Pool '{0}' cidr: {1}".format(global_pool_name, global_pool_cidr), "INFO")
        return global_pool_cidr

    def get_want_global_pool(self, global_ippool):
        """
        Get all the Global Pool information from playbook
        Set the status and the msg before returning from the API
        Check the return value of the API with check_return_status()

        Parameters:
            global_ippool (dict) - Playbook global pool details containing IpAddressSpace,
            DHCP server IPs, DNS server IPs, IP pool name, IP pool CIDR, gateway, and type.

        Returns:
            self - The current object with updated desired Global Pool information.
        """

        # Initialize the desired Global Pool configuration
        want_global = {
            "settings": {
                "ippool": []
            }
        }
        want_ippool = want_global.get("settings").get("ippool")
        global_pool_index = 0
        for pool_details in global_ippool:
            pool_values = {
                "dhcpServerIps": pool_details.get("dhcp_server_ips"),
                "dnsServerIps": pool_details.get("dns_server_ips"),
                "ipPoolName": pool_details.get("name"),
                "ipPoolCidr": pool_details.get("cidr"),
                "gateway": pool_details.get("gateway"),
                "type": pool_details.get("pool_type"),
            }
            ip_address_space = pool_details.get("ip_address_space")
            if not ip_address_space:
                self.msg = "Missing required parameter 'ip_address_space' under global_pool_details."
                self.status = "failed"
                return self

            ip_address_space_list = ["IPv4", "IPv6"]
            if ip_address_space not in ip_address_space_list:
                self.msg = "The 'ip_address_space' under global_pool_details should be in the list: {0}" \
                           .format(ip_address_space_list)
                self.status = "failed"
                return self

            pool_values.update({"IpAddressSpace": ip_address_space})

            # Converting to the required format based on the existing Global Pool
            if not self.have.get("globalPool")[global_pool_index].get("exists"):
                if pool_values.get("dhcpServerIps") is None:
                    pool_values.update({"dhcpServerIps": []})
                if pool_values.get("dnsServerIps") is None:
                    pool_values.update({"dnsServerIps": []})
                if pool_values.get("IpAddressSpace") is None:
                    pool_values.update({"IpAddressSpace": ""})
                if pool_values.get("gateway") is None:
                    pool_values.update({"gateway": ""})
                if pool_values.get("type") is None:
                    pool_values.update({"type": "Generic"})
            else:
                have_ippool = self.have.get("globalPool")[global_pool_index].get("details")

                # Copy existing Global Pool information if the desired configuration is not provided
                pool_values.update({
                    "IpAddressSpace": have_ippool.get("IpAddressSpace"),
                    "type": have_ippool.get("type"),
                    "ipPoolCidr": have_ippool.get("ipPoolCidr"),
                    "id": self.have.get("globalPool")[global_pool_index].get("id")
                })
                for key in ["dhcpServerIps", "dnsServerIps", "gateway"]:
                    if pool_values.get(key) is None and have_ippool.get(key) is not None:
                        pool_values[key] = have_ippool[key]
            want_ippool.append(pool_values)
            global_pool_index += 1

        self.log("Global pool playbook details: {0}".format(want_global), "DEBUG")
        self.want.update({"wantGlobal": want_global})
        self.msg = "Collecting the global pool details from the playbook"
        self.status = "success"
        return self

    def get_want_reserve_pool(self, reserve_pool):
        """
        Get all the Reserved Pool information from playbook
        Set the status and the msg before returning from the API
        Check the return value of the API with check_return_status()

        Parameters:
            reserve_pool (dict) - Playbook reserved pool
            details containing various properties.

        Returns:
            self - The current object with updated desired Reserved Pool information.
        """

        want_reserve = []
        reserve_pool_index = 0
        for item in reserve_pool:
            pool_values = {
                "name": item.get("name"),
                "type": item.get("pool_type"),
                "ipv6AddressSpace": item.get("ipv6_address_space"),
                "ipv4GlobalPool": self.get_global_pool_cidr(item.get("ipv4_global_pool"),
                                                            item.get("ipv4_global_pool_name")),
                "ipv4Prefix": item.get("ipv4_prefix"),
                "ipv4PrefixLength": item.get("ipv4_prefix_length"),
                "ipv4GateWay": item.get("ipv4_gateway"),
                "ipv4DhcpServers": item.get("ipv4_dhcp_servers"),
                "ipv4DnsServers": item.get("ipv4_dns_servers"),
                "ipv4Subnet": item.get("ipv4_subnet"),
                "ipv6Prefix": item.get("ipv6_prefix"),
                "ipv6PrefixLength": item.get("ipv6_prefix_length"),
                "ipv6GateWay": item.get("ipv6_gateway"),
                "ipv6DhcpServers": item.get("ipv6_dhcp_servers"),
                "ipv6Subnet": item.get("ipv6_subnet"),
                "ipv6DnsServers": item.get("ipv6_dns_servers"),
                "ipv4TotalHost": item.get("ipv4_total_host"),
                "ipv6TotalHost": item.get("ipv6_total_host"),
                "slaacSupport": item.get("slaac_support")
            }
            # Check for missing required parameters in the playbook
            if pool_values.get("ipv6AddressSpace") is True:
                pool_values.update({
                    "ipv6GlobalPool": self.get_global_pool_cidr(item.get("ipv6_global_pool"),
                                                                item.get("ipv6_global_pool_name"))})

            if not pool_values.get("name"):
                self.msg = "Missing required parameter 'name' in reserve_pool_details '{0}' element" \
                           .format(reserve_pool_index + 1)
                self.status = "failed"
                return self

            if pool_values.get("ipv4Prefix") is True:
                if pool_values.get("ipv4Subnet") is None and \
                        pool_values.get("ipv4TotalHost") is None:
                    self.msg = "Failed to add IPv4 in reserve_pool_details '{0}'. ".format(reserve_pool_index + 1) + \
                               "Required parameters 'ipv4_subnet' or 'ipv4_total_host' are missing."
                    self.status = "failed"
                    return self

            if pool_values.get("ipv6Prefix") is True:
                if pool_values.get("ipv6Subnet") is None and \
                        pool_values.get("ipv6TotalHost") is None:
                    self.msg = "Failed to add IPv6 in reserve_pool_details '{0}'. ".format(reserve_pool_index + 1) + \
                               "Required parameters 'ipv6_subnet' or 'ipv6_total_host' are missing."
                    self.status = "failed"
                    return self

            self.log("Reserved IP pool playbook details: {0}".format(pool_values), "DEBUG")

            # If there are no existing Reserved Pool details, validate and set defaults
            if not self.have.get("reservePool")[reserve_pool_index].get("details"):
                if not pool_values.get("ipv4GlobalPool"):
                    self.msg = "missing parameter 'ipv4GlobalPool' in reserve_pool_details '{0}' element" \
                               .format(reserve_pool_index + 1)
                    self.status = "failed"
                    return self

                if not pool_values.get("ipv4PrefixLength"):
                    self.msg = "missing parameter 'ipv4_prefix_length' in reserve_pool_details '{0}' element" \
                               .format(reserve_pool_index + 1)
                    self.status = "failed"
                    return self

                if pool_values.get("type") is None:
                    pool_values.update({"type": "Generic"})
                if pool_values.get("ipv4DhcpServers") is None:
                    pool_values.update({"ipv4DhcpServers": []})
                if pool_values.get("ipv4DnsServers") is None:
                    pool_values.update({"ipv4DnsServers": []})
                if pool_values.get("ipv6AddressSpace") is None:
                    pool_values.update({"ipv6AddressSpace": False})
                if pool_values.get("slaacSupport") is None:
                    pool_values.update({"slaacSupport": True})
                if pool_values.get("ipv4TotalHost") is None:
                    del pool_values['ipv4TotalHost']
                if pool_values.get("ipv6AddressSpace") is True:
                    pool_values.update({"ipv6Prefix": True})
                else:
                    del pool_values['ipv6Prefix']

            else:
                keys_to_delete = ['type', 'ipv4GlobalPool', 'ipv4Prefix', 'ipv4PrefixLength',
                                  'ipv4TotalHost', 'ipv4Subnet', 'slaacSupport']
                for key in keys_to_delete:
                    if key in pool_values:
                        del pool_values[key]

                copy_pool_values = copy.deepcopy(pool_values)
                for item in copy_pool_values:
                    if pool_values.get(item) is None:
                        del pool_values[item]

            if not pool_values.get("ipv6AddressSpace"):
                keys_to_check = ['ipv6PrefixLength', 'ipv6GateWay', 'ipv6DhcpServers',
                                 'ipv6DnsServers', 'ipv6TotalHost', 'ipv6Subnet']
                for key in keys_to_check:
                    if key in pool_values:
                        del pool_values[key]

            want_reserve.append(pool_values)
            reserve_pool_index += 1

        self.want.update({"wantReserve": want_reserve})
        self.log("Reserved Pool details: {0}".format(want_reserve), "INFO")
        self.msg = "Collected the reserved pool details from the playbook"
        self.status = "success"
        return self

    def get_want_network(self, network_management_details):
        """
        Get all the Network related information from playbook
        Set the status and the msg before returning from the API
        Check the return value of the API with check_return_status()

        Parameters:
            network_management_details (dict) - Playbook network
            details containing various network settings.

        Returns:
            self - The current object with updated desired Network-related information.
        """
        all_network_management_details = []
        network_management_index = 0
        for item in network_management_details:
            item = item.get("settings")
            want_network = {
                "settings": {
                    "dhcpServer": {},
                    "dnsServer": {},
                    "snmpServer": {},
                    "syslogServer": {},
                    "netflowcollector": {},
                    "ntpServer": {},
                    "timezone": "",
                    "messageOfTheday": {},
                    "network_aaa": {},
                    "clientAndEndpoint_aaa": {}
                }
            }
            want_network_settings = want_network.get("settings")
            self.log("Current state (have): {0}".format(self.have), "DEBUG")
            if item.get("dhcp_server") is not None:
                want_network_settings.update({
                    "dhcpServer": item.get("dhcp_server")
                })
            else:
                del want_network_settings["dhcpServer"]

            if item.get("ntp_server") is not None:
                want_network_settings.update({
                    "ntpServer": item.get("ntp_server")
                })
            else:
                del want_network_settings["ntpServer"]

            have_timezone = self.have.get("network")[network_management_index].get("net_details").get("settings").get("timezone")
            if item.get("timezone") is not None:
                want_network_settings["timezone"] = \
                    item.get("timezone")
            elif have_timezone is not None:
                want_network_settings["timezone"] = have_timezone
            else:
                want_network_settings["timezone"] = "GMT"

            dns_server = item.get("dns_server")
            if dns_server is not None:
                if dns_server.get("domain_name") is not None:
                    want_network_settings.get("dnsServer").update({
                        "domainName":
                        dns_server.get("domain_name")
                    })

                if dns_server.get("primary_ip_address") is not None:
                    want_network_settings.get("dnsServer").update({
                        "primaryIpAddress":
                        dns_server.get("primary_ip_address")
                    })

                if dns_server.get("secondary_ip_address") is not None:
                    want_network_settings.get("dnsServer").update({
                        "secondaryIpAddress":
                        dns_server.get("secondary_ip_address")
                    })
            else:
                del want_network_settings["dnsServer"]

            snmp_server = item.get("snmp_server")
            if snmp_server is not None:
                if snmp_server.get("configure_dnac_ip") is not None:
                    want_network_settings.get("snmpServer").update({
                        "configureDnacIP": snmp_server.get("configure_dnac_ip")
                    })
                if snmp_server.get("ip_addresses") is not None:
                    want_network_settings.get("snmpServer").update({
                        "ipAddresses": snmp_server.get("ip_addresses")
                    })
            else:
                del want_network_settings["snmpServer"]

            syslog_server = item.get("syslog_server")
            if syslog_server is not None:
                if syslog_server.get("configure_dnac_ip") is not None:
                    want_network_settings.get("syslogServer").update({
                        "configureDnacIP": syslog_server.get("configure_dnac_ip")
                    })
                if syslog_server.get("ip_addresses") is not None:
                    want_network_settings.get("syslogServer").update({
                        "ipAddresses": syslog_server.get("ip_addresses")
                    })
            else:
                del want_network_settings["syslogServer"]

            netflow_collector = item.get("netflow_collector")
            if netflow_collector is not None:
                if netflow_collector.get("ip_address") is not None:
                    want_network_settings.get("netflowcollector").update({
                        "ipAddress":
                        netflow_collector.get("ip_address")
                    })
                if netflow_collector.get("port") is not None:
                    want_network_settings.get("netflowcollector").update({
                        "port":
                        netflow_collector.get("port")
                    })
            else:
                del want_network_settings["netflowcollector"]

            message_of_the_day = item.get("message_of_the_day")
            if message_of_the_day is not None:
                if message_of_the_day.get("banner_message") is not None:
                    want_network_settings.get("messageOfTheday").update({
                        "bannerMessage":
                        message_of_the_day.get("banner_message")
                    })
                retain_existing_banner = message_of_the_day.get("retain_existing_banner")
                if retain_existing_banner is not None:
                    if retain_existing_banner is True:
                        want_network_settings.get("messageOfTheday").update({
                            "retainExistingBanner": "true"
                        })
                    else:
                        want_network_settings.get("messageOfTheday").update({
                            "retainExistingBanner": "false"
                        })
            else:
                del want_network_settings["messageOfTheday"]

            server_types = ["AAA", "ISE"]
            protocol_types = ["RADIUS", "TACACS"]
            network_aaa = item.get("network_aaa")
            if network_aaa:
                server_type = network_aaa.get("server_type")
                if server_type:
                    want_network_settings.get("network_aaa").update({
                        "servers": server_type
                    })
                else:
                    self.msg = "The 'server_type' is required under network_aaa."
                    self.status = "failed"
                    return self

                if server_type not in server_types:
                    self.msg = "The 'server_type' in the network_aaa should be in {0}".format(server_types)
                    self.status = "failed"
                    return self

                primary_server_address = network_aaa.get("primary_server_address")
                if primary_server_address:
                    want_network_settings.get("network_aaa").update({
                        "network": primary_server_address
                    })
                else:
                    self.msg = "Missing required parameter 'primary_server_address' in network_aaa."
                    self.status = "failed"
                    return self

                if server_type == "ISE":
                    pan_address = network_aaa.get("pan_address")
                    if pan_address:
                        want_network_settings.get("network_aaa").update({
                            "ipAddress": pan_address
                        })
                    else:
                        self.msg = "Missing required parameter 'pan_address' for ISE server in network_aaa."
                        self.status = "failed"
                        return self
                else:
                    secondary_server_address = network_aaa.get("secondary_server_address")
                    if secondary_server_address:
                        want_network_settings.get("network_aaa").update({
                            "ipAddress": secondary_server_address
                        })

                protocol = network_aaa.get("protocol")
                if protocol:
                    want_network_settings.get("network_aaa").update({
                        "protocol": protocol
                    })
                else:
                    want_network_settings.get("network_aaa").update({
                        "protocol": "RADIUS"
                    })

                if protocol not in protocol_types:
                    self.msg = "The 'protocol' in the network_aaa should be in {0}".format(protocol_types)
                    self.status = "failed"
                    return self

                shared_secret = network_aaa.get("shared_secret")
                if shared_secret is not None:
                    if len(shared_secret) < 4:
                        self.msg = (
                            "The 'shared_secret' length in 'network_aaa' should be greater than or equal to 4."
                        )
                        self.status = "failed"
                        return self

                    want_network_settings.get("network_aaa").update({
                        "sharedSecret": shared_secret
                    })
            else:
                del want_network_settings["network_aaa"]

            client_and_endpoint_aaa = item.get("client_and_endpoint_aaa")
            if client_and_endpoint_aaa:
                server_type = client_and_endpoint_aaa.get("server_type")
                if server_type:
                    want_network_settings.get("clientAndEndpoint_aaa").update({
                        "servers": server_type
                    })
                else:
                    self.msg = "The 'server_type' is required under client_and_endpoint_aaa."
                    self.status = "failed"
                    return self

                if server_type not in server_types:
                    self.msg = "The 'server_type' in the client_and_endpoint_aaa should be in {0}".format(server_types)
                    self.status = "failed"
                    return self

                primary_server_address = client_and_endpoint_aaa.get("primary_server_address")
                if primary_server_address:
                    want_network_settings.get("clientAndEndpoint_aaa").update({
                        "network": primary_server_address
                    })
                else:
                    self.msg = "Missing required parameter 'primary_server_address' in client_and_endpoint_aaa."
                    self.status = "failed"
                    return self

                if server_type == "ISE":
                    pan_address = client_and_endpoint_aaa.get("pan_address")
                    if pan_address:
                        want_network_settings.get("clientAndEndpoint_aaa").update({
                            "ipAddress": pan_address
                        })
                    else:
                        self.msg = "Missing required parameter 'pan_address' for ISE server in client_and_endpoint_aaa."
                        self.status = "failed"
                        return self
                else:
                    secondary_server_address = client_and_endpoint_aaa.get("secondary_server_address")
                    if secondary_server_address:
                        want_network_settings.get("clientAndEndpoint_aaa").update({
                            "ipAddress": secondary_server_address
                        })

                protocol = client_and_endpoint_aaa.get("protocol")
                if protocol:
                    want_network_settings.get("clientAndEndpoint_aaa").update({
                        "protocol": protocol
                    })
                else:
                    want_network_settings.get("clientAndEndpoint_aaa").update({
                        "protocol": "RADIUS"
                    })

                if protocol not in protocol_types:
                    self.msg = "The 'protocol' in the client_and_endpoint_aaa should be in {0}".format(protocol_types)
                    self.status = "failed"
                    return self

                shared_secret = client_and_endpoint_aaa.get("shared_secret")
                if shared_secret is not None:
                    if len(shared_secret) < 4:
                        self.msg = (
                            "The 'shared_secret' length in 'client_and_endpoint_aaa' should be greater than or equal to 4."
                        )
                        self.status = "failed"
                        return self

                    want_network_settings.get("clientAndEndpoint_aaa").update({
                        "sharedSecret": shared_secret
                    })
            else:
                del want_network_settings["clientAndEndpoint_aaa"]

            network_aaa = want_network_settings.get("network_aaa")
            client_and_endpoint_aaa = want_network_settings.get("clientAndEndpoint_aaa")
            if network_aaa and client_and_endpoint_aaa and \
                    network_aaa.get("sharedSecret") and \
                    client_and_endpoint_aaa.get("sharedSecret") and \
                    network_aaa.get("sharedSecret") != client_and_endpoint_aaa.get("sharedSecret"):
                self.msg = "The 'shared_secret' of 'network_aaa' and 'client_and_endpoint_aaa' should be same."
                self.status = "failed"
                return self

            all_network_management_details.append(want_network)
            network_management_index += 1

        self.log("Network playbook details: {0}".format(all_network_management_details), "DEBUG")
        self.want.update({"wantNetwork": all_network_management_details})
        self.msg = "Collected the network details from the playbook"
        self.status = "success"
        return self

    def get_want(self, config):
        """
        Get all the Global Pool Reserved Pool and Network related information from playbook

        Parameters:
            config (list of dict) - Playbook details

        Returns:
            None
        """

        if config.get("global_pool_details"):
            global_ippool = config.get("global_pool_details").get("settings").get("ip_pool")
            self.get_want_global_pool(global_ippool).check_return_status()

        if config.get("reserve_pool_details"):
            reserve_pool = config.get("reserve_pool_details")
            self.get_want_reserve_pool(reserve_pool).check_return_status()

        if config.get("network_management_details"):
            network_management_details = config.get("network_management_details")
            self.get_want_network(network_management_details).check_return_status()

        self.log("Desired State (want): {0}".format(self.want), "INFO")
        self.msg = "Successfully retrieved details from the playbook"
        self.status = "success"
        return self

    def update_global_pool(self, global_pool):
        """
        Update/Create Global Pool in Cisco Catalyst Center with fields provided in playbook

        Parameters:
            global_pool (list of dict) - Global Pool playbook details

        Returns:
            None
        """

        create_global_pool = []
        update_global_pool = []
        global_pool_index = 0
        result_global_pool = self.result.get("response")[0].get("globalPool")
        want_global_pool = self.want.get("wantGlobal").get("settings").get("ippool")
        self.log("Global pool playbook details: {0}".format(global_pool), "DEBUG")
        for item in self.have.get("globalPool"):
            result_global_pool.get("msg") \
                .update({want_global_pool[global_pool_index].get("ipPoolName"): {}})
            if item.get("exists") is True:
                update_global_pool.append(want_global_pool[global_pool_index])
            else:
                create_global_pool.append(want_global_pool[global_pool_index])

            global_pool_index += 1

        # Check create_global_pool; if yes, create the global pool
        if create_global_pool:
            self.log("Global pool(s) details to be created: {0}".format(create_global_pool), "INFO")
            pool_params = {
                "settings": {
                    "ippool": copy.deepcopy(create_global_pool)
                }
            }
            response = self.dnac._exec(
                family="network_settings",
                function="create_global_pool",
                op_modifies=True,
                params=pool_params,
            )
            self.check_execution_response_status(response, "create_global_pool").check_return_status()
            self.log("Successfully created global pool successfully.", "INFO")
            for item in pool_params.get("settings").get("ippool"):
                name = item.get("ipPoolName")
                self.log("Global pool '{0}' created successfully.".format(name), "INFO")
                result_global_pool.get("response").update({"created": pool_params})
                result_global_pool.get("msg").update({name: "Global Pool Created Successfully"})

        if update_global_pool:
            final_update_global_pool = []
            # Pool exists, check update is required
            for item in update_global_pool:
                name = item.get("ipPoolName")
                for pool_value in self.have.get("globalPool"):
                    if pool_value.get("exists") and (pool_value.get("details").get("ipPoolName") == name or pool_value.get("prev_name") == name):
                        if not self.requires_update(pool_value.get("details"), item, self.global_pool_obj_params):
                            self.log("Global pool '{0}' doesn't require an update".format(name), "INFO")
                            result_global_pool.get("msg").update({name: "Global pool doesn't require an update"})
                        elif item not in final_update_global_pool:
                            final_update_global_pool.append(item)

            if final_update_global_pool:
                self.log("Global pool requires update", "INFO")

                # Pool(s) needs update
                pool_params = {
                    "settings": {
                        "ippool": copy.deepcopy(final_update_global_pool)
                    }
                }
                self.log("Desired State for global pool (want): {0}".format(pool_params), "DEBUG")
                keys_to_remove = ["IpAddressSpace", "ipPoolCidr", "type"]
                for item in pool_params["settings"]["ippool"]:
                    for key in keys_to_remove:
                        del item[key]

                self.log("Desired global pool details (want): {0}".format(pool_params), "DEBUG")
                response = self.dnac._exec(
                    family="network_settings",
                    function="update_global_pool",
                    op_modifies=True,
                    params=pool_params,
                )

                self.check_execution_response_status(response, "update_global_pool").check_return_status()
                for item in pool_params.get("settings").get("ippool"):
                    name = item.get("ipPoolName")
                    self.log("Global pool '{0}' Updated successfully.".format(name), "INFO")
                    result_global_pool.get("response").update({"globalPool Details": pool_params})
                    result_global_pool.get("msg").update({name: "Global Pool Updated Successfully"})

        self.log("Global pool configuration operations completed successfully.", "INFO")
        return

    def update_reserve_pool(self, reserve_pool):
        """
        Update or Create a Reserve Pool in Cisco Catalyst Center based on the provided configuration.
        This method checks if a reserve pool with the specified name exists in Cisco Catalyst Center.
        If it exists and requires an update, it updates the pool. If not, it creates a new pool.

        Parameters:
            reserve_pool (list of dict) - Playbook details containing Reserve Pool information.

        Returns:
            None
        """

        reserve_pool_index = -1
        for item in reserve_pool:
            reserve_pool_index += 1
            name = item.get("name")
            result_reserve_pool = self.result.get("response")[1].get("reservePool")
            self.log("Current reserved pool '{0}' details in Catalyst Center: {1}"
                     .format(name, self.have.get("reservePool")[reserve_pool_index].get("details")), "DEBUG")
            self.log("Desired reserved pool '{0}' details in Catalyst Center: {1}"
                     .format(name, self.want.get("wantReserve")[reserve_pool_index]), "DEBUG")

            # Check pool exist, if not create and return
            self.log("IPv4 reserved pool '{0}': {1}"
                     .format(name, self.want.get("wantReserve")[reserve_pool_index].get("ipv4GlobalPool")), "DEBUG")
            site_name = item.get("site_name")
            reserve_params = self.want.get("wantReserve")[reserve_pool_index]
            site_id = self.get_site_id(site_name)
            reserve_params.update({"site_id": site_id})
            if not self.have.get("reservePool")[reserve_pool_index].get("exists"):
                self.log("Desired reserved pool '{0}' details (want): {1}"
                         .format(name, reserve_params), "DEBUG")
                response = self.dnac._exec(
                    family="network_settings",
                    function="reserve_ip_subpool",
                    op_modifies=True,
                    params=reserve_params,
                )
                self.check_execution_response_status(response, "reserve_ip_subpool").check_return_status()
                self.log("Successfully created IP subpool reservation '{0}'.".format(name), "INFO")
                result_reserve_pool.get("response") \
                    .update({name: self.want.get("wantReserve")[reserve_pool_index]})
                result_reserve_pool.get("msg") \
                    .update({name: "Ip Subpool Reservation Created Successfully"})
                continue

            # Check update is required
            if not self.requires_update(self.have.get("reservePool")[reserve_pool_index].get("details"),
                                        self.want.get("wantReserve")[reserve_pool_index],
                                        self.reserve_pool_obj_params):
                self.log("Reserved ip subpool '{0}' doesn't require an update".format(name), "INFO")
                result_reserve_pool.get("msg") \
                    .update({name: "Reserved ip subpool doesn't require an update"})
                continue

            self.log("Reserved ip pool '{0}' requires an update".format(name), "DEBUG")

            # Pool Exists
            self.log("Current reserved ip pool '{0}' details in Catalyst Center: {1}"
                     .format(name, self.have.get("reservePool")), "DEBUG")
            self.log("Desired reserved ip pool '{0}' details: {1}"
                     .format(name, self.want.get("wantReserve")), "DEBUG")
            reserve_params.update({"id": self.have.get("reservePool")[reserve_pool_index].get("id")})
            response = self.dnac._exec(
                family="network_settings",
                function="update_reserve_ip_subpool",
                op_modifies=True,
                params=reserve_params,
            )
            self.check_execution_response_status(response, "update_reserve_ip_subpool").check_return_status()
            self.log("Reserved ip subpool '{0}' updated successfully.".format(name), "INFO")
            result_reserve_pool.get("response") \
                .update({name: reserve_params})
            result_reserve_pool.get("response").get(name) \
                .update({"Id": self.have.get("reservePool")[reserve_pool_index].get("id")})
            result_reserve_pool.get("msg") \
                .update({name: "Reserved Ip Subpool updated successfully."})

        self.log("Updated reserved IP subpool successfully", "INFO")
        return

    def update_network(self, network_management):
        """
        Update or create a network configuration in Cisco Catalyst
        Center based on the provided playbook details.

        Parameters:
            network_management (list of dict) - Playbook details containing Network Management information.

        Returns:
            None
        """
        network_management_index = 0
        for item in network_management:
            site_name = item.get("site_name")
            result_network = self.result.get("response")[2].get("network")
            result_network.get("response").update({site_name: {}})
            have_network_details = self.have.get("network")[network_management_index].get("net_details")
            want_network_details = self.want.get("wantNetwork")[network_management_index]
            network_aaa = want_network_details.get("settings").get("network_aaa")
            client_and_endpoint_aaa = want_network_details.get("settings").get("clientAndEndpoint_aaa")

            # Check update is required or not
            if not (network_aaa.get("sharedSecret") or
                    client_and_endpoint_aaa.get("sharedSecret") or
                    self.requires_update(have_network_details, want_network_details, self.network_obj_params)):

                self.log("Network in site '{0}' doesn't require an update.".format(site_name), "INFO")
                result_network.get("response").get(site_name).update({
                    "Cisco Catalyst Center params": self.have.get("network")[network_management_index]
                    .get("net_details").get("settings")
                })
                result_network.get("msg").update({site_name: "Network doesn't require an update"})
                continue

            self.log("Network in site '{0}' requires update.".format(site_name), "INFO")
            self.log("Current State of network in Catalyst Center: {0}"
                     .format(self.have.get("network")), "DEBUG")
            self.log("Desired State of network: {0}".format(self.want.get("wantNetwork")), "DEBUG")

            net_params = copy.deepcopy(self.want.get("wantNetwork")[network_management_index])
            net_params.update({"site_id": self.have.get("network")[network_management_index].get("site_id")})
            try:
                response = self.dnac._exec(
                    family="network_settings",
                    function='update_network_v2',
                    op_modifies=True,
                    params=net_params,
                )
            except Exception as msg:
                if "[400] Bad Request" in str(msg):
                    self.msg = (
                        "Received Bad Request [400] from the Catalyst Center. "
                        "Please provide valid input or check the server IPs under the network_management_details."
                    )

                self.log(str(msg), "ERROR")
                self.status = "failed"
                return self

            self.log("Received API response of 'update_network_v2': {0}".format(response), "DEBUG")
            validation_string = "desired common settings operation successful"
            self.check_task_response_status(response, validation_string, "update_network_v2").check_return_status()
            self.log("Network under the site '{0}' has been changed successfully".format(site_name), "INFO")
            result_network.get("msg") \
                .update({site_name: "Network Updated successfully"})
            result_network.get("response").get(site_name) \
                .update({"Network Details": self.want.get("wantNetwork")[network_management_index].get("settings")})
            network_management_index += 1

        return

    def get_diff_merged(self, config):
        """
        Update or create Global Pool, Reserve Pool, and
        Network configurations in Cisco Catalyst Center based on the playbook details

        Parameters:
            config (list of dict) - Playbook details containing
            Global Pool, Reserve Pool, and Network Management information.

        Returns:
            self
        """

        global_pool = config.get("global_pool_details")
        if global_pool is not None:
            self.update_global_pool(global_pool)

        reserve_pool = config.get("reserve_pool_details")
        if reserve_pool is not None:
            self.update_reserve_pool(reserve_pool)

        network_management = config.get("network_management_details")
        if network_management is not None:
            self.update_network(network_management)

        return self

    def delete_reserve_pool(self, reserve_pool_details):
        """
        Delete a Reserve Pool by name in Cisco Catalyst Center

        Parameters:
            reserve_pool_details (list of dict) - Reserverd pool playbook details.

        Returns:
            self
        """

        reserve_pool_index = -1
        for item in reserve_pool_details:
            reserve_pool_index += 1
            name = item.get("name")
            reserve_pool_exists = self.have.get("reservePool")[reserve_pool_index].get("exists")
            result_reserve_pool = self.result.get("response")[1].get("reservePool")

            if not reserve_pool_exists:
                result_reserve_pool.get("msg").update({name: "Reserve Pool not found"})
                self.log("Reserved Ip Subpool '{0}' not found".format(name), "INFO")
                continue

            self.log("Reserved IP pool scheduled for deletion: {0}"
                     .format(self.have.get("reservePool")[reserve_pool_index].get("name")), "INFO")
            _id = self.have.get("reservePool")[reserve_pool_index].get("id")
            self.log("Reserved pool '{0}' id: {1}".format(name, _id), "DEBUG")
            response = self.dnac._exec(
                family="network_settings",
                function="release_reserve_ip_subpool",
                op_modifies=True,
                params={"id": _id},
            )
            self.check_execution_response_status(response, "release_reserve_ip_subpool").check_return_status()
            executionid = response.get("executionId")
            result_reserve_pool = self.result.get("response")[1].get("reservePool")
            result_reserve_pool.get("response").update({name: {}})
            result_reserve_pool.get("response").get(name) \
                .update({"Execution Id": executionid})
            result_reserve_pool.get("msg") \
                .update({name: "Ip subpool reservation released successfully"})

        self.msg = "Reserved pool(s) released successfully"
        self.status = "success"
        return self

    def delete_global_pool(self, global_pool_details):
        """
        Delete a Global Pool by name in Cisco Catalyst Center

        Parameters:
            global_pool_details (dict) - Global pool details of the playbook

        Returns:
            self
        """

        result_global_pool = self.result.get("response")[0].get("globalPool")
        global_pool_index = 0
        for item in self.have.get("globalPool"):
            global_pool_exists = item.get("exists")
            name = global_pool_details.get("settings").get("ip_pool")[global_pool_index].get("name")
            global_pool_index += 1
            if not global_pool_exists:
                result_global_pool.get("msg").update({name: "Global Pool not found"})
                self.log("Global pool '{0}' not found".format(name), "INFO")
                continue

            id = item.get("id")
            response = self.dnac._exec(
                family="network_settings",
                function="delete_global_ip_pool",
                op_modifies=True,
                params={"id": id},
            )

            # Check the execution status
            self.check_execution_response_status(response, "delete_global_ip_pool").check_return_status()
            executionid = response.get("executionId")

            # Update result information
            result_global_pool = self.result.get("response")[0].get("globalPool")
            result_global_pool.get("response").update({name: {}})
            result_global_pool.get("response").get(name).update({"Execution Id": executionid})
            result_global_pool.get("msg").update({name: "Global pool deleted successfully"})

        self.msg = "Global pools deleted successfully"
        self.status = "success"
        return self

    def get_diff_deleted(self, config):
        """
        Delete Reserve Pool and Global Pool in Cisco Catalyst Center based on playbook details.

        Parameters:
            config (list of dict) - Playbook details

        Returns:
            self
        """

        reserve_pool_details = config.get("reserve_pool_details")
        if reserve_pool_details is not None:
            self.delete_reserve_pool(reserve_pool_details).check_return_status()

        global_pool_details = config.get("global_pool_details")
        if global_pool_details is not None:
            self.delete_global_pool(global_pool_details).check_return_status()

        return self

    def verify_diff_merged(self, config):
        """
        Validating the Cisco Catalyst Center configuration with the playbook details
        when state is merged (Create/Update).

        Parameters:
            config (dict) - Playbook details containing Global Pool,
            Reserved Pool, and Network Management configuration.

        Returns:
            self
        """

        self.all_reserved_pool_details = {}
        self.get_have(config)
        self.log("Current State (have): {0}".format(self.have), "INFO")
        self.log("Requested State (want): {0}".format(self.want), "INFO")
        if config.get("global_pool_details") is not None:
            global_pool_index = 0
            self.log("Desired State of global pool (want): {0}"
                     .format(self.want.get("wantGlobal")), "DEBUG")
            self.log("Current State of global pool (have): {0}"
                     .format(self.have.get("globalPool")), "DEBUG")
            for item in self.want.get("wantGlobal").get("settings").get("ippool"):
                global_pool_details = self.have.get("globalPool")[global_pool_index].get("details")
                if not global_pool_details:
                    self.msg = "The global pool is not created with the config: {0}".format(item)
                    self.status = "failed"
                    return self

                if self.requires_update(global_pool_details, item, self.global_pool_obj_params):
                    self.msg = "Global Pool Config is not applied to the Cisco Catalyst Center"
                    self.status = "failed"
                    return self

                global_pool_index += 1

            self.log("Successfully validated global pool(s).", "INFO")
            self.result.get("response")[0].get("globalPool").update({"Validation": "Success"})

        if config.get("reserve_pool_details") is not None:
            reserve_pool_index = 0
            self.log("Desired State for reserve pool (want): {0}"
                     .format(self.want.get("wantReserve")), "DEBUG")
            self.log("Current State for reserve pool (have): {0}"
                     .format(self.have.get("reservePool")), "DEBUG")
            for item in self.want.get("wantReserve"):
                reserve_pool_details = self.have.get("reservePool")[reserve_pool_index].get("details")
                if not reserve_pool_details:
                    self.msg = "The reserve pool is not created with the config: {0}".format(item)
                    self.status = "failed"
                    return self

                if self.requires_update(reserve_pool_details, item, self.reserve_pool_obj_params):
                    self.msg = "Reserved Pool Config is not applied to the Cisco Catalyst Center"
                    self.status = "failed"
                    return self

                reserve_pool_index += 1

            self.log("Successfully validated the reserved pool(s)", "INFO")
            self.result.get("response")[1].get("reservePool").update({"Validation": "Success"})

        network_management_details = config.get("network_management_details")
        if network_management_details is not None:
            network_management_index = 0
            for item in network_management_details:
                if self.requires_update(self.have.get("network")[network_management_index].get("net_details"),
                                        self.want.get("wantNetwork")[network_management_index], self.network_obj_params):
                    self.msg = "Network Functions Config is not applied to the Cisco Catalyst Center"
                    self.status = "failed"
                    return self

                self.log("Successfully validated the network functions '{0}'."
                         .format(item.get("site_name")), "INFO")
                network_management_index += 1

            self.result.get("response")[2].get("network").update({"Validation": "Success"})

        self.msg = "Successfully validated the Global Pool, Reserve Pool and the Network Functions."
        self.status = "success"
        return self

    def verify_diff_deleted(self, config):
        """
        Validating the Cisco Catalyst Center configuration with the playbook details
        when state is deleted (delete).

        Parameters:
            config (dict) - Playbook details containing Global Pool,
            Reserved Pool, and Network Management configuration.

        Returns:
            self
        """

        self.all_reserved_pool_details = {}
        self.get_have(config)
        self.log("Current State (have): {0}".format(self.have), "INFO")
        self.log("Desired State (want): {0}".format(self.want), "INFO")
        if config.get("global_pool_details") is not None:
            global_pool_index = 0
            global_pool_details = self.have.get("globalPool")
            for item in global_pool_details:
                global_pool_exists = item.get("exists")
                name = config.get("global_pool_details").get("settings") \
                             .get("ip_pool")[global_pool_index].get("name")
                if global_pool_exists:
                    self.msg = "Global Pool Config '{0}' is not applied to the Cisco Catalyst Center" \
                               .format(name)
                    self.status = "failed"
                    return self

                self.log("Successfully validated absence of Global Pool '{0}'.".format(name), "INFO")
                global_pool_index += 1
            self.result.get("response")[0].get("globalPool").update({"Validation": "Success"})

        if config.get("reserve_pool_details") is not None:
            reserve_pool_index = 0
            reserve_pool_details = self.have.get("reservePool")
            for item in reserve_pool_details:
                reserve_pool_exists = item.get("exists")
                name = config.get("reserve_pool_details")[reserve_pool_index].get("name")
                if reserve_pool_exists:
                    self.msg = "Reserved Pool Config '{0}' is not applied to the Catalyst Center" \
                               .format(name)
                    self.status = "failed"
                    return self

                self.log("Successfully validated the absence of Reserve Pool '{0}'.".format(name), "INFO")
                self.result.get("response")[1].get("reservePool").update({"Validation": "Success"})

        self.msg = "Successfully validated the absence of Global Pool/Reserve Pool"
        self.status = "success"
        return self

    def reset_values(self):
        """
        Reset all neccessary attributes to default values

        Parameters:
            None

        Returns:
            None
        """

        self.have.clear()
        self.want.clear()
        return


def main():
    """main entry point for module execution"""

    # Define the specification for module arguments
    element_spec = {
        "dnac_host": {"type": 'str', "required": True},
        "dnac_port": {"type": 'str', "default": '443'},
        "dnac_username": {"type": 'str', "default": 'admin', "aliases": ['user']},
        "dnac_password": {"type": 'str', "no_log": True},
        "dnac_verify": {"type": 'bool', "default": 'True'},
        "dnac_version": {"type": 'str', "default": '2.2.3.3'},
        "dnac_debug": {"type": 'bool', "default": False},
        "dnac_log": {"type": 'bool', "default": False},
        "dnac_log_level": {"type": 'str', "default": 'WARNING'},
        "dnac_log_file_path": {"type": 'str', "default": 'dnac.log'},
        "dnac_log_append": {"type": 'bool', "default": True},
        "config_verify": {"type": 'bool', "default": False},
        "dnac_api_task_timeout": {"type": 'int', "default": 1200},
        "dnac_task_poll_interval": {"type": 'int', "default": 2},
        "config": {"type": 'list', "required": True, "elements": 'dict'},
        "state": {"default": 'merged', "choices": ['merged', 'deleted']},
        "validate_response_schema": {"type": 'bool', "default": True},
    }

    # Create an AnsibleModule object with argument specifications
    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=False)
    ccc_network = NetworkSettings(module)
    state = ccc_network.params.get("state")
    config_verify = ccc_network.params.get("config_verify")
    if state not in ccc_network.supported_states:
        ccc_network.status = "invalid"
        ccc_network.msg = "State {0} is invalid".format(state)
        ccc_network.check_return_status()

    ccc_network.validate_input().check_return_status()

    for config in ccc_network.config:
        ccc_network.reset_values()
        ccc_network.get_have(config).check_return_status()
        if state != "deleted":
            ccc_network.get_want(config).check_return_status()
        ccc_network.get_diff_state_apply[state](config).check_return_status()
        if config_verify:
            ccc_network.verify_diff_state_apply[state](config).check_return_status()

    module.exit_json(**ccc_network.result)


if __name__ == "__main__":
    main()
