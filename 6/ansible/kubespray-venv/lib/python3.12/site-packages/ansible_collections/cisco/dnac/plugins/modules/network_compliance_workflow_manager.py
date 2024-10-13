#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to perform Network Compliance Operations on devices in Cisco Catalyst Center."""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ("Rugvedi Kapse, Madhan Sankaranarayanan")

DOCUMENTATION = r"""
---
module: network_compliance_workflow_manager
short_description: Network Compliance module for managing network compliance tasks on reachable device(s) in Cisco Catalyst Center.
description:
- Perform compliance checks or sync configurations on reachable devices using IP Address(s) or Site.
- API to perform full compliance checks or specific category checks on reachable device(s).
- API to sync device configuration on device(s).
version_added: "6.14.0"
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author: Rugvedi Kapse (@rukapse)
        Madhan Sankaranarayanan (@madhansansel)
options:
  config_verify:
    description: Set to True to verify the Cisco Catalyst Center config after applying the playbook config.
    type: bool
    default: False
  state:
    description: State of Cisco Catalyst Center after module completion.
    type: str
    choices: [ merged ]
    default: merged
  config:
    description: List of device details for running a compliance check or synchronizing device configuration.
    type: list
    elements: dict
    required: True
    suboptions:
      ip_address_list:
        description: List of IP addresses of devices to run a compliance check on or synchronize device configurations.
                     Either "ip_address_list" or "site_name" is required for module to execute.
                     If both "site_name" and "ip_address_list" are provided, operations are performed on devices that are present in both the
                     "ip_address_list" and the specified site.
                     (e.g. ["204.1.2.2", "204.1.2.5", "204.1.2.4"])
        type: list
        elements: str
      site_name:
        description: When "site_name" is specified, the module executes the operation on all the devices located within the specified site.
                     This is a string value that should represent the complete hierarchical path of the site.
                     Either "site_name" or "ip_address_list" is required for module to execute.
                     If both "site_name" and "ip_address_list" are provided, operations are performed on devices that are present in both the
                     "ip_address_list" and the specified site.
                     (e.g. "Global/USA/San Francisco/Building_2/floor_1")
        type: str
      run_compliance:
        description: Determines if a full compliance check should be triggered on the devices specified in the "ip_address_list" and/or "site_name".
                     if it is True then compliance will be triggered for all categories.
                     If it is False then compliance will be not be triggered even if run_compliance categories are provided.
                     Note - This operation cannot be performed on Access Points (APs) and if APs are provided, they will be skipped.
        type: bool
        default: True
      run_compliance_batch_size:
        description: Specifies the number of devices to be included in a single batch for compliance operations.
                     This parameter is crucial for optimizing performance during large-scale compliance checks.
                     By processing devices in manageable batches, the system can enhance the speed and efficiency of the operation,
                     reducing the overall time required and minimizing the risk of overloading system resources.
                     Adjusting this parameter allows for a balance between throughput and resource utilization, ensuring smooth and
                     effective compliance management.
                     Note - Having a higher value for run_compliance_batch_size may cause errors due to the increased load on the system.
        type: int
        default: 100
      run_compliance_categories:
        description: Specifying compliance categories allows you to trigger compliance checks only for the mentioned categories.
                     Category can have one or more values from among the options "INTENT", "RUNNING_CONFIG", "IMAGE", "PSIRT", "EOX", "NETWORK_SETTINGS".
                     Category "INTENT" is mapped to compliance types "NETWORK_SETTINGS", "NETWORK_PROFILE", "WORKFLOW", "FABRIC", "APPLICATION_VISIBILITY".
                     If "run_compliance" is False then compliance will be not be triggered even if "run_compliance_categories" are provided.
                     (e.g. ["INTENT", "RUNNING_CONFIG", "IMAGE", "PSIRT", "EOX", "NETWORK_SETTINGS"])
        type: list
        elements: str
      sync_device_config:
        description: Determines whether to synchronize the device configuration on the devices specified in the "ip_address_list" and/or "site_name".
                     Sync device configuration, primarily addresses the status of the `RUNNING_CONFIG`.
                     If set to True, and if `RUNNING_CONFIG` status is non-compliant this operation would commit device running configuration
                     to startup by issuing "write memory" to device.
                     Note - This operation cannot be performed on Access Points (APs) and if APs are provided, they will be skipped.
        type: bool
        default: False

requirements:
- dnacentersdk == 2.7.0
- python >= 3.9
notes:
  - SDK Methods used are
    compliance.Compliance.run_compliance
    compliance.Compliance.commit_device_configuration
    task.Task.get_task_by_id
    task.Task.get_task_tree
    compliance.Compliance.compliance_details_of_device

  - Paths used are
    post /dna/intent/api/v1/compliance/
    post /dna/intent/api/v1/network-device-config/write-memory
    get /dna/intent/api/v1/task/{taskId}
    get /dna/intent/api/v1/task/{taskId}/tree
    get /dna/intent/api/v1/compliance/${deviceUuid}/detail

"""

EXAMPLES = r"""
- name: Run Compliance check on device(s) using IP address list (run_compliance by default is True)
  cisco.dnac.network_compliance_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    config:
      - ip_address_list: ["204.1.2.2", "204.1.2.5", "204.1.2.4"]

- name: Run Compliance check on device(s) using IP address list
  cisco.dnac.network_compliance_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    config:
      - ip_address_list: ["204.1.2.2", "204.1.2.5", "204.1.2.4"]
        run_compliance: True

- name: Run Compliance check on device(s) using Site
  cisco.dnac.network_compliance_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    config:
      - site_name: "Global/USA/San Francisco/Building_1/floor_1"
        run_compliance: True

- name: Run Compliance check on device(s) using both IP address list and Site
  cisco.dnac.network_compliance_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    config:
      - ip_address_list: ["204.1.2.2", "204.1.2.5", "204.1.2.4"]
        site_name: "Global/USA/San Francisco/Building_1/floor_1"
        run_compliance: True

- name: Run Compliance check with specific categories on device(s) using IP address list
  cisco.dnac.network_compliance_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    config:
      - ip_address_list: ["204.1.2.2", "204.1.2.5", "204.1.2.4"]
        run_compliance: True
        run_compliance_categories: ["INTENT", "RUNNING_CONFIG", "IMAGE", "PSIRT"]

- name: Run Compliance check with specific categories on device(s) using Site
  cisco.dnac.network_compliance_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    config:
      - site_name: "Global/USA/San Francisco/Building_1/floor_1"
        run_compliance: True
        run_compliance_categories: ["INTENT", "RUNNING_CONFIG", "IMAGE", "PSIRT"]

- name: Run Compliance check with specific categories on device(s) using both IP address list and Site
  cisco.dnac.network_compliance_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    config:
      - ip_address_list: ["204.1.2.2", "204.1.2.5", "204.1.2.4"]
        site_name: "Global/USA/San Francisco/Building_1/floor_1"
        run_compliance: True
        run_compliance_categories: ["INTENT", "RUNNING_CONFIG", "IMAGE", "PSIRT"]

- name: Sync Device Configuration on device(s) using IP address list
  cisco.dnac.network_compliance_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    config:
      - site_name: "Global"
        sync_device_config: True
        run_compliance: False

- name: Sync Device Configuration on device(s) using Site
  cisco.dnac.network_compliance_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    config:
      - site_name: "Global/USA/San Francisco/Building_1/floor_1"
        sync_device_config: True
        run_compliance: False

- name: Sync Device Configuration on device(s) using both IP address list and Site
  cisco.dnac.network_compliance_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    config:
      - ip_address_list: ["204.1.2.2", "204.1.2.5", "204.1.2.4"]
        site_name: "Global/USA/San Francisco/Building_1/floor_1"
        sync_device_config: True
        run_compliance: False

- name: Run Compliance and Sync Device Configuration using both IP address list and Site
  cisco.dnac.network_compliance_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    config:
      - ip_address_list: ["204.1.2.2", "204.1.2.5", "204.1.2.4"]
        site_name: "Global/USA/San Francisco/Building_1/floor_1"
        run_compliance: True
        run_compliance_categories: ["INTENT", "RUNNING_CONFIG", "IMAGE", "PSIRT"]
        sync_device_config: True
"""

RETURN = r"""
#Case_1: Response when Run Compliance operation is performed successfully on device/s.
sample_response_1:
  description: A dictionary with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "status": "string",
      "changed": bool,
      "msg": "string"
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "data": dict,
      "version": "string"
    }

#Case_2: Response when Sync Device Configuration operation is performed successfully on device/s.
sample_response_2:
  description: A dictionary with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "status": "string",
      "changed": bool,
      "msg": "string"
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }

#Case_3: Response when Error Occurs in performing Run Compliance or Sync Device Configuration operation on device/s.
sample_response_3:
  description: A dictionary with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "changed": bool,
      "msg": "string"
    }
"""

import time
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts
)


class NetworkCompliance(DnacBase):
    """Class containing member attributes for network_compliance_workflow_manager module"""

    def __init__(self, module):
        """
        Initialize an instance of the class.
        Parameters:
          - module: The module associated with the class instance.
        Returns:
          The method does not return a value.
        """
        super().__init__(module)

    def validate_input(self):
        """
        Validate the fields provided in the playbook against a predefined specification
        to ensure they adhere to the expected structure and data types.
        Parameters:
            state (optional): A state parameter that can be used to customize validation
                              based on different conditions.
        Returns:
            object: An instance of the class with updated attributes:
              - self.msg: A message describing the validation result.
              - self.status: The status of the validation (either "success" or "failed").
              - self.validated_config: If successful, a validated version of the "config" parameter.
        Description:
            This method validates the fields provided in the playbook against a predefined specification.
            It checks if the required fields are present and if their data types match the expected types.
            If any parameter is found to be invalid, it logs an error message and sets the validation status to "failed".
            If the validation is successful, it logs a success message and returns an instance of the class
            with the validated configuration.
        """
        if not self.config:
            self.msg = "config not available in playbook for validation"
            self.status = "success"
            self.log(self.msg, "ERROR")
            return self

        temp_spec = {
            "ip_address_list": {"type": "list", "elements": "str", "required": False},
            "site_name": {"type": "str", "required": False},
            "run_compliance": {"type": "bool", "required": False, "default": True},
            "run_compliance_categories": {"type": "list", "elements": "str", "required": False},
            "run_compliance_batch_size": {"type": "int", "required": False, "default": 100},
            "sync_device_config": {"type": "bool", "required": False, "default": False},
        }

        # Validate device params
        valid_temp, invalid_params = validate_list_of_dicts(
            self.config, temp_spec
        )

        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(invalid_params)
            self.log(self.msg, "ERROR")
            self.status = "failed"
            return self

        self.validated_config = valid_temp

        self.msg = "Successfully validated playbook configuration parameters using 'validated_input': {0}".format(str(valid_temp))
        self.log(self.msg, "INFO")
        self.status = "success"

        return self

    def validate_ip4_address_list(self, ip_address_list):
        """
        Validates the list of IPv4 addresses provided in the playbook.
        Parameters:
            ip_address_list (list): A list of IPv4 addresses to be validated.
        Description:
            This method iterates through each IP address in the list and checks if it is a valid IPv4 address.
            If any address is found to be invalid, it logs an error message and fails.
            After validating all IP addresses, it logs a success message.
        """
        for ip in ip_address_list:
            if not self.is_valid_ipv4(ip):
                self.msg = "IP address: {0} is not valid".format(ip)
                self.log(self.msg, "ERROR")
                self.module.fail_json(self.msg)

        ip_address_list_str = ", ".join(ip_address_list)
        self.log("Successfully validated the IP address(es): {0}".format(ip_address_list_str), "DEBUG")

    def validate_run_compliance_paramters(self, mgmt_ip_to_instance_id_map, run_compliance, run_compliance_categories):
        """
        Validate and prepare parameters for running compliance checks.
        Parameters:
            - mgmt_ip_to_instance_id_map (dict): A dictionary mapping management IP addresses to device instance IDs.
            - run_compliance (bool or None): A boolean indicating whether to run compliance checks.
            - run_compliance_categories (list): A list of compliance categories to check.
        Returns:
        tuple: A tuple containing two dictionaries:
            - run_compliance_params: Parameters for running compliance checks.
        Notes:
            - This method prepares parameters for running compliance checks based on the provided inputs.
            - If invalid categories are provided in `run_compliance_categories`, a `ValueError` is raised.
            - If `run_compliance_categories` is provided and neither `run_compliance` nor `run_compliance_categories` is set, an error
              is logged and the method fails.
            - If `run_compliance` is set and `run_compliance_categories` is not, full compliance checks are triggered.
            - If both `run_compliance` and `run_compliance_categories` are set, compliance checks are triggered for specific categories.
        """
        # Initializing empty dicts/lists
        run_compliance_params = {}
        valid_categories = ["INTENT", "RUNNING_CONFIG", "IMAGE", "PSIRT", "EOX", "NETWORK_SETTINGS"]

        if run_compliance_categories:
            # Validate the categories provided
            if not all(category.upper() in valid_categories for category in run_compliance_categories):
                valid_categories_str = ", ".join(valid_categories)
                msg = "Invalid category provided. Valid categories are {0}.".format(valid_categories_str)
                self.log(msg, "ERROR")
                self.module.fail_json(msg)

            if run_compliance:
                # run_compliance_params
                run_compliance_params["deviceUuids"] = list(mgmt_ip_to_instance_id_map.values())
                run_compliance_params["triggerFull"] = False
                run_compliance_params["categories"] = run_compliance_categories

        if run_compliance:
            # run_compliance_params
            run_compliance_params["deviceUuids"] = list(mgmt_ip_to_instance_id_map.values())
            run_compliance_params["triggerFull"] = True

        # Check for devices with Compliance Status of "IN_PROGRESS" and update parameters accordingly
        if run_compliance_params:
            device_in_progress = set()

            response = self.get_compliance_report(run_compliance_params, mgmt_ip_to_instance_id_map)

            if not response:
                ip_address_list_str = ", ".join(list(mgmt_ip_to_instance_id_map.keys()))
                msg = (
                    "Error occurred when retrieving Compliance Report to identify if there are "
                    "devices with 'IN_PROGRESS' status. This is required on device(s): {0}"
                    .format(ip_address_list_str)
                )
                self.log(msg)
                self.module.fail_json(msg)

            # Iterate through the response to identify devices with 'IN_PROGRESS' status
            for device_ip, compliance_details_list in response.items():
                for compliance_type in compliance_details_list:
                    if compliance_type.get("status") == "IN_PROGRESS":
                        device_in_progress.add(compliance_type.get("deviceUuid"))

            self.log(
                "Number of devices with Compliance Status 'IN_PROGRESS': {0}. Device UUIDs: {1}".format(
                    len(device_in_progress), list(device_in_progress)), "DEBUG"
            )
            if device_in_progress:
                # Update run_compliance_params to exclude devices with 'IN_PROGRESS' status
                run_compliance_params["deviceUuids"] = [device_id for device_id in mgmt_ip_to_instance_id_map.values() if device_id not in device_in_progress]
                msg = "Excluding 'IN_PROGRESS' devices from compliance check. Updated run_compliance_params: {0}".format(run_compliance_params)
                self.log(msg, "DEBUG")

        return run_compliance_params

    def site_exists(self, site_name):
        """
        Checks the existence of a site in Cisco Catalyst Center.
        Parameters:
            site_name (str): The name of the site to be checked.
        Returns:
            tuple: A tuple containing two values:
                - site_exists (bool): Indicates whether the site exists (True) or not (False).
                - site_id (str or None): The ID of the site if it exists, or None if the site is not found.
        Description:
            This method queries Cisco Catalyst Center to determine if a site with the provided name exists.
            If the site is found, it sets "site_exists" to True and retrieves the site"s ID.
            If the site does not exist, "site_exists" is set to False, and "site_id" is None.
            If an exception occurs during the site lookup, an error message is logged, and the module fails.
        """
        site_exists = False
        site_id = None
        response = None

        # Attempt to retrieve site information from Catalyst Center
        try:
            response = self.dnac._exec(
                family="sites",
                function="get_site",
                op_modifies=True,
                params={"name": site_name},
            )
            self.log("Response received post 'get_site' API call: {0}".format(str(response)), "DEBUG")

            # Process the response if available
            if response:
                site = response.get("response")
                site_id = site[0].get("id")
                site_exists = True
            else:
                self.log("No response received from the 'get_site' API call.", "ERROR")

        except Exception as e:
            # Log an error message and fail if an exception occurs
            self.log("An error occurred while retrieving site details for Site '{0}' using 'get_site' API call: {1}".format(site_name, str(e)), "ERROR")

        if not site_exists:
            msg = "An error occurred while retrieving site details for Site '{0}'. Please verify that the site exists.".format(site_name)
            self.log(msg, "ERROR")
            self.module.fail_json(msg=msg)

        return (site_exists, site_id)

    def get_device_ids_from_ip(self, ip_address_list):
        """
        Retrieves the device IDs based on the provided list of IP addresses from Cisco Catalyst Center.
        Parameters:
            ip_address_list (list): A list of IP addresses of devices for which you want to retrieve the device IDs.
        Returns:
            dict: A dictionary mapping management IP addresses to their instance UUIDs.
        Description:
            This method queries Cisco Catalyst Center for device information using the provided IP addresses.
            For each IP address in the list, it attempts to fetch the device information using the "get_device_list" API.
            If the device is found and reachable, it extracts the device ID and maps it to the corresponding IP address.
            If any error occurs during the process, it logs an error message and continues to the next IP address.
        """
        mgmt_ip_to_instance_id_map = {}

        # Iterate through the provided list of IP addresses
        for device_ip in ip_address_list:
            try:
                # Query Cisco Catalyst Center for device information using the IP address
                response = self.dnac._exec(
                    family="devices",
                    function="get_device_list",
                    op_modifies=True,
                    params={"managementIpAddress": device_ip}
                )
                self.log("Response received post 'get_device_list' API call: {0}".format(str(response)), "DEBUG")

                # Check if a valid response is received
                if response.get("response"):
                    response = response.get("response")
                    if not response:
                        continue
                    for device_info in response:
                        if device_info["reachabilityStatus"] == "Reachable":
                            if device_info["family"] != "Unified AP":
                                device_id = device_info["id"]
                                mgmt_ip_to_instance_id_map[device_ip] = device_id
                            else:
                                msg = "Skipping device {0} as its family is {1}.".format(device_ip, device_info["family"])
                                self.log(msg, "INFO")
                        else:
                            msg = "Skipping device {0} as its status is {2}.".format(device_ip, device_info["reachabilityStatus"])
                            self.log(msg, "INFO")
                else:
                    # If unable to retrieve device information, log an error message
                    self.log("Unable to retrieve device information for {0}. Please ensure that the device exists and is reachable.".format(device_ip), "ERROR")

            except Exception as e:
                # Log an error message if any exception occurs during the process
                self.log("Error while fetching device ID for device: '{0}' from Cisco Catalyst Center: {1}".format(device_ip, str(e)), "ERROR")
        if not mgmt_ip_to_instance_id_map:
            ip_address_list_str = ", ".join(ip_address_list)
            self.msg = "No reachable devices found among the provided IP addresses: {0}".format(ip_address_list_str)
            self.update_result("ok", False, self.msg, "INFO")
            self.module.exit_json(**self.result)

        return mgmt_ip_to_instance_id_map

    def get_device_ids_from_site(self, site_name, site_id):
        """
        Retrieves the management IP addresses and their corresponding instance UUIDs of devices associated with a specific site in Cisco Catalyst Center.

        Parameters:
            site_name (str): The name of the site whose devices" information is to be retrieved.
            site_id (str): The unique identifier of the site.

        Returns:
            dict: A dictionary mapping management IP addresses to their instance UUIDs.

        Description:
            This method queries Cisco Catalyst Center to fetch the list of devices associated with the provided site.
            It then extracts the management IP addresses and their instance UUIDs from the response.
            Devices that are not reachable are logged as critical errors, and the function fails.
            If no reachable devices are found for the specified site, it logs an error message and fails.

        """
        mgmt_ip_to_instance_id_map = {}

        site_params = {
            "site_id": site_id,
        }

        # Attempt to retrieve device information associated with the site
        try:
            response = self.dnac._exec(
                family="sites",
                function="get_membership",
                op_modifies=True,
                params=site_params,
            )
            self.log("Response received post 'get_membership' API Call: {0} ".format(str(response)), "DEBUG")

            # Process the response if available
            if response:
                response = response["device"]
                # Iterate over the devices in the site membership
                for item in response:
                    if item["response"]:
                        for item_dict in item["response"]:
                            # Check if the device is reachable
                            if item_dict["reachabilityStatus"] == "Reachable":
                                if item_dict["family"] != "Unified AP":
                                    mgmt_ip_to_instance_id_map[item_dict["managementIpAddress"]] = item_dict["instanceUuid"]
                                else:
                                    msg = "Skipping device {0} in site {1} as its family is {2}".format(
                                        item_dict["managementIpAddress"], site_name, item_dict["family"])
                                    self.log(msg, "INFO")
                            else:
                                msg = "Skipping device {0} in site {1} as its status is {2}".format(
                                    item_dict["managementIpAddress"], site_name, item_dict["reachabilityStatus"])
                                self.log(msg, "WARNING")
            else:
                # If unable to retrieve device information, log an error message
                self.log("No response received from API call to get membership information for site. {0}".format(site_name), "ERROR")

        except Exception as e:
            # Log an error message if any exception occurs during the process
            self.log("Unable to fetch the device(s) associated to the site '{0}' due to {1}".format(site_name, str(e)), "ERROR")

        if not mgmt_ip_to_instance_id_map:
            self.msg = "Reachable devices not found at Site: {0}".format(site_name)
            self.update_result("ok", False, self.msg, "INFO")
            self.module.exit_json(**self.result)

        return mgmt_ip_to_instance_id_map

    def get_device_id_list(self, ip_address_list, site_name):
        """
        Get the list of unique device IDs for a specified list of management IP addresses or devices associated with a site
        in Cisco Catalyst Center.
        Parameters:
            ip_address_list (list): The management IP addresses of devices for which you want to retrieve the device IDs.
            site_name (str): The name of the site for which you want to retrieve the device IDs.
        Returns:
            dict: A dictionary mapping management IP addresses to device IDs for the specified devices.
        Description:
            This method queries Cisco Catalyst Center to retrieve the unique device IDs associated with devices having the
            specified IP addresses or belonging to the specified site.
        """
        # Initialize a dictionary to store management IP addresses and their corresponding device IDs
        mgmt_ip_to_instance_id_map = {}

        # Check if both site name and IP address list are provided
        if site_name:
            (site_exists, site_id) = self.site_exists(site_name)
            if site_exists:
                # Retrieve device IDs associated with devices in the site
                site_mgmt_ip_to_instance_id_map = self.get_device_ids_from_site(site_name, site_id)
                mgmt_ip_to_instance_id_map.update(site_mgmt_ip_to_instance_id_map)

        if ip_address_list:
            # Retrieve device IDs associated with devices having specified IP addresses
            iplist_mgmt_ip_to_instance_id_map = self.get_device_ids_from_ip(ip_address_list)
            mgmt_ip_to_instance_id_map.update(iplist_mgmt_ip_to_instance_id_map)

        return mgmt_ip_to_instance_id_map

    def is_sync_required(self, response, mgmt_ip_to_instance_id_map):
        """
        Determine if synchronization of device configurations is required.

        Args:
            response (dict): A dictionary containing modified responses for each device.
            mgmt_ip_to_instance_id_map (dict): A dictionary mapping management IP addresses to instance IDs.

        Returns:
            tuple: A tuple containing a boolean indicating whether synchronization is required
                   and a message explaining the result.

        Note:
            This method categorizes devices based on compliance status ("COMPLIANT", "NON_COMPLIANT", "OTHER")
            and checks if synchronization is necessary. If all devices are "COMPLIANT", synchronization is not
            required. If there are devices that are not "NON_COMPLIANT", synchronization is also not required.
        """
        task_name = "Sync Device Configuration"
        required = True
        msg = None

        # Validate if sync is required
        self.log("Compliance Report for {0} operation for device(s) {1} : {2}".format(
            task_name, list(mgmt_ip_to_instance_id_map.keys()), response), "INFO")

        # Categorize the devices based on status - "COMPLIANT", "NON_COMPLIANT", "OTHER"(status other than COMPLIANT and NON_COMPLIANT)
        categorized_devices = {"COMPLIANT": {}, "NON_COMPLIANT": {}, "OTHER": {}}
        for ip_address, compliance_type in response.items():
            status = compliance_type[0]["status"]
            if status == "NON_COMPLIANT":
                categorized_devices["NON_COMPLIANT"][ip_address] = compliance_type
            elif status == "COMPLIANT":
                categorized_devices["COMPLIANT"][ip_address] = compliance_type
            else:
                categorized_devices["OTHER"][ip_address] = compliance_type

        self.log("Device(s) Categorized based on Compliance status: {0}".format(categorized_devices), "INFO")

        # Validate if all devices are "COMPLIANT" - then sync not required
        if len(categorized_devices["COMPLIANT"]) + len(categorized_devices["OTHER"]) == len(mgmt_ip_to_instance_id_map):
            compliant_device_ips_str = ", ".join(list(mgmt_ip_to_instance_id_map.keys()))
            msg = (
                "Device(s) with IP address(es): {0} are already compliant with the RUNNING_CONFIG compliance type. "
                "Therefore, the task '{1}' is not required."
            ).format(compliant_device_ips_str, task_name)
            required = False

        return required, msg, categorized_devices

    def get_want(self, config):
        """
        Determines the desired state based on the provided configuration.
        Parameters:
            config (dict): The configuration specifying the desired state.
        Returns:
            dict: A dictionary containing the desired state parameters.
        Description:
            This method processes the provided configuration to determine the desired state. It validates the presence of
            either "ip_address_list" or "site_name" and constructs parameters for running compliance checks and syncing
            device configurations based on the provided configuration. It also logs the desired state for reference.
        """
        # Initialize parameters
        run_compliance_params = {}
        sync_device_config_params = {}
        compliance_detail_params_sync = {}
        compliance_details = {}

        # Store input parameters
        ip_address_list = config.get("ip_address_list")
        site_name = config.get("site_name")
        run_compliance = config.get("run_compliance")
        run_compliance_categories = config.get("run_compliance_categories")
        sync_device_config = config.get("sync_device_config")
        run_compliance_batch_size = config.get("run_compliance_batch_size")

        # Validate either ip_address_list OR site_name is present
        if not any([ip_address_list, site_name]):
            msg = "ip_address_list is {0} and site_name is {1}. Either the ip_address_list or the site_name must be provided.".format(
                ip_address_list, site_name)
            self.log(msg, "ERROR")
            self.module.fail_json(msg=msg)

        # Validate if a network compliance operation is present
        if not any([run_compliance, run_compliance_categories, sync_device_config]):
            msg = "No actions were requested. This network compliance module can perform the following tasks: Run Compliance Check or Sync Device Config."
            self.log(msg, "ERROR")
            self.module.fail_json(msg)
            return self

        # Validate valid ip_addresses
        if ip_address_list:
            self.validate_ip4_address_list(ip_address_list)
            # Remove Duplicates from list
            ip_address_list = list(set(ip_address_list))

        # Retrieve device ID list
        mgmt_ip_to_instance_id_map = self.get_device_id_list(ip_address_list, site_name)
        if not mgmt_ip_to_instance_id_map:
            # Log an error message if mgmt_ip_to_instance_id_map is empty
            ip_address_list_str = ", ".join(ip_address_list)
            msg = ("No device UUIDs were fetched for network compliance operations with the provided IP address(es): {0} "
                   "or site name: {1}. This could be due to Unreachable devices or access points (APs).").format(ip_address_list_str, site_name)
            self.log(msg, "ERROR")
            self.module.fail_json(msg)

        # Run Compliance Paramters
        run_compliance_params = self.validate_run_compliance_paramters(
            mgmt_ip_to_instance_id_map, run_compliance, run_compliance_categories)

        # Sync Device Configuration Parameters
        if sync_device_config:
            sync_device_config_params = {
                "deviceId": list(mgmt_ip_to_instance_id_map.values())
            }

            compliance_detail_params_sync = {
                "deviceUuids": list(mgmt_ip_to_instance_id_map.values()),
                "categories": ["RUNNING_CONFIG"]
            }

            # Validate if Sync Device Configuration is required on the device(s)
            response = self.get_compliance_report(compliance_detail_params_sync, mgmt_ip_to_instance_id_map)
            if not response:
                ip_address_list_str = ", ".join(list(mgmt_ip_to_instance_id_map.keys()))
                msg = "Error occurred when retrieving Compliance Report to identify if Sync Device Config Operation "
                msg += "is required on device(s): {0}".format(ip_address_list_str)
                self.log(msg)
                self.module.fail_json(msg)

            compliance_details = response
            sync_required, self.msg, categorized_devices = self.is_sync_required(response, mgmt_ip_to_instance_id_map)
            self.log("Is Sync Requied: {0} -- Message: {1}".format(sync_required, self.msg), "DEBUG")
            if not sync_required:
                self.update_result("ok", False, self.msg, "INFO")
                self.module.exit_json(**self.result)

            # Get the device IDs of devices in the "OTHER" category and "COMPLIANT" category
            other_device_ids = categorized_devices.get("OTHER", {}).keys()
            compliant_device_ids = categorized_devices.get("COMPLIANT", {}).keys()
            excluded_device_ids = set(other_device_ids) | set(compliant_device_ids)

            if excluded_device_ids:
                # Convert excluded_device_ids to their corresponding UUIDs
                excluded_device_uuids = [mgmt_ip_to_instance_id_map[ip] for ip in excluded_device_ids if ip in mgmt_ip_to_instance_id_map]

                # Exclude devices in the "OTHER" category from sync_device_config_params
                sync_device_config_params["deviceId"] = [
                    device_id for device_id in mgmt_ip_to_instance_id_map.values()
                    if device_id not in excluded_device_uuids
                ]
                excluded_device_ids_str = ", ".join(excluded_device_ids)
                msg = "Skipping these devices because their compliance status is not 'NON_COMPLIANT': {0}".format(excluded_device_ids_str)
                self.log(msg, "WARNING")
                self.log("Updated 'sync_device_config_params' parameters: {0}".format(sync_device_config_params), "DEBUG")

        # Construct the "want" dictionary containing the desired state parameters
        want = {}
        want = dict(
            ip_address_list=ip_address_list,
            site_name=site_name,
            mgmt_ip_to_instance_id_map=mgmt_ip_to_instance_id_map,
            run_compliance_params=run_compliance_params,
            run_compliance_batch_size=run_compliance_batch_size,
            sync_device_config_params=sync_device_config_params,
            compliance_detail_params_sync=compliance_detail_params_sync,
            compliance_details=compliance_details
        )
        self.want = want
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

        return self

    def get_compliance_report(self, run_compliance_params, mgmt_ip_to_instance_id_map):
        """
        Generate a compliance report for devices based on provided parameters.

        This function fetches the compliance details for a list of devices specified
        in the run_compliance_params. It maps the device UUIDs to their corresponding
        management IPs, and then retrieves the compliance details for each device.

        Args:
            run_compliance_params (dict): Parameters for running compliance checks.
                                          Expected to contain "deviceUuids" and optionally "categories".
            mgmt_ip_to_instance_id_map (dict): Mapping of device management IPs to device UUIDs.

        Returns:
            dict: A dictionary with device management IPs as keys and lists of compliance details as values.
        """
        # Initialize the lists/dicts
        final_response = {}
        device_list = []
        compliance_details_of_device_params = {}
        device_ip = None

        # Iterate through each device UUID in the run compliance parameters
        for device_uuid in run_compliance_params["deviceUuids"]:

            # Find the corresponding device IP for the given device UUID
            for ip, device_id in mgmt_ip_to_instance_id_map.items():
                if device_uuid == device_id:
                    device_ip = ip
                    break

            if device_ip is None:
                self.log("Device UUID: {0} not found in mgmt_ip_to_instance_id_map: {1}".format(device_uuid, mgmt_ip_to_instance_id_map), "DEBUG")
                continue

            # Add the device IP to the device list
            device_list.append(device_ip)

            # Initialize the response list for the device IP if not already present
            if device_ip not in final_response.keys():
                final_response[device_ip] = []

            # Check if categories are specified and fetch details for each category of the device
            if "categories" in run_compliance_params.keys():
                for category in run_compliance_params["categories"]:
                    compliance_details_of_device_params["category"] = category
                    compliance_details_of_device_params["device_uuid"] = device_uuid
                    compliance_details_of_device_params["diff_list"] = True

                    response = self.get_compliance_details_of_device(compliance_details_of_device_params, device_ip)
                    final_response[device_ip].extend(response)

            else:
                # Fetch compliance details for the device without specific category
                compliance_details_of_device_params["device_uuid"] = device_uuid
                compliance_details_of_device_params["diff_list"] = True
                response = self.get_compliance_details_of_device(compliance_details_of_device_params, device_ip)
                final_response[device_ip].extend(response)

        # If no compliance details were found, update the result with an error message
        if not final_response:
            device_list_str = ", ".join(device_list)
            self.msg = "No Compliance Details found for the devices: {0}".format(device_list_str)
            self.update_result("failed", False, self.msg, "ERROR")
            self.check_return_status()

        return final_response

    def get_compliance_details_of_device(self, compliance_details_of_device_params, device_ip):
        """
        Retrieve compliance details for a specific device.

        This function makes an API call to fetch compliance details for a given device
        using the specified parameters. It handles the API response and logs the
        necessary information.

        Args:
            compliance_details_of_device_params (dict): Parameters required for the compliance details API call.
            device_ip (str): The IP address of the device for which compliance details are being fetched.

        Returns:
            dict or None: The response from the compliance details API call if successful,
                          None if an error occurs or no response is received.
        """
        try:
            # Make the API call to fetch compliance details for the device
            response = self.dnac_apply["exec"](
                family="compliance",
                function="compliance_details_of_device",
                params=compliance_details_of_device_params,
                op_modifies=True
            )
            self.log("Response received post 'compliance_details_of_device' API call: {0}".format(str(response)), "DEBUG")

            if response:
                response = response["response"]
            else:
                self.log("No response received from the 'compliance_details_of_device' API call.", "ERROR")
            return response
        except Exception as e:
            # Handle any exceptions that occur during the API call
            self.msg = ("An error occurred while retrieving Compliance Details for device:{0} using 'compliance_details_of_device' API call"
                        ". Error: {1}".format(device_ip, str(e)))
            self.update_result("failed", False, self.msg, "ERROR")
            self.check_return_status()

    def run_compliance(self, run_compliance_params, batch_size):
        """
        Executes a compliance check operation in Cisco Catalyst Center.
        Parameters:
            run_compliance_params (dict): Parameters for running the compliance check.
            batch_size (int): The number of devices to include in each batch.
        Returns:
            batches_dict: A dictionary containing task IDs and parameters for each batch, or an empty dictionary if unsuccessful
        Description:
            This method initiates a compliance check operation in Cisco Catalyst Center by calling the "run_compliance" function
            from the "compliance" family of APIs. It passes the provided parameters and updates the result accordingly.
        """
        # Execute the compliance check operation
        device_uuids = run_compliance_params.get("deviceUuids")
        if not device_uuids:
            self.msg = "No device UUIDs were found for the execution of the compliance operation."
            self.update_result("ok", False, self.msg, "INFO")
            self.module.exit_json(**self.result)

        batches_dict = {}

        if len(device_uuids) > batch_size:
            batches = [device_uuids[i:i + batch_size] for i in range(0, len(device_uuids), batch_size)]
        else:
            batches = [device_uuids]
        self.log("Created {0} batch(es) for run compliance operation: {1}".format(len(batches), batches), "DEBUG")

        for idx, batch in enumerate(batches):
            self.log("Executing 'run_compliance' operation on batch: {0} - {1}".format(idx, batch), "DEBUG")
            batch_params = run_compliance_params.copy()
            batch_params["deviceUuids"] = batch
            self.log("Batch {0} Parameters: {1}".format(idx, batch_params), "DEBUG")

            try:
                response = self.dnac_apply["exec"](
                    family="compliance",
                    function="run_compliance",
                    params=batch_params,
                    op_modifies=True,
                )
                self.log("Response received post 'run_compliance' API call is {0}".format(str(response)), "DEBUG")

                if response:
                    self.result.update(dict(response=response["response"]))
                    task_id = response["response"].get("taskId")
                    self.log("Task Id for the 'run_compliance' task is {0}".format(task_id), "DEBUG")
                    if task_id:
                        batches_dict[idx] = {"task_id": task_id, "batch_params": batch_params}
                else:
                    self.log("No response received from the 'run_compliance' API call.", "ERROR")

            # Log and handle any exceptions that occur during the execution
            except Exception as e:
                msg = (
                    "An error occurred while executing the 'run_compliance' operation for parameters - {0}. "
                    "Error: {1}".format(batch_params, str(e))
                )
                self.log(msg, "CRITICAL")

        return batches_dict

    def sync_device_config(self, sync_device_config_params):
        """
        Synchronize the device configuration using the specified parameters.
        Parameters:
            - sync_device_config_params (dict): Parameters for synchronizing the device configuration.
        Returns:
            task_id (str): The ID of the task created for the synchronization operation.
        Note:
            This method initiates the synchronization of device configurations by making an API call to the Cisco Catalyst Center.
            It logs the response received from the API call and extracts the task ID from the response for further monitoring.
            If an error occurs during the API call, it will be caught and logged.
        """
        # Make an API call to synchronize device configuration
        try:
            response = self.dnac_apply["exec"](
                family="compliance",
                function="commit_device_configuration",
                params=sync_device_config_params,
                op_modifies=True,
            )
            self.log("Response received post 'commit_device_configuration' API call is {0}".format(str(response)), "DEBUG")

            if response:
                self.result.update(dict(response=response["response"]))
                self.log("Task Id for the 'commit_device_configuration' task  is {0}".format(response["response"].get("taskId")), "INFO")
                # Return the task ID
                return response["response"].get("taskId")
            else:
                self.log("No response received from the 'commit_device_configuration' API call.", "ERROR")
                return None

        # Log the error if an exception occurs during the API call
        except Exception as e:
            self.msg = (
                "Error occurred while synchronizing device configuration for parameters - {0}. "
                "Error: {1}".format(sync_device_config_params, str(e)))
            self.update_result("failed", False, self.msg, "ERROR")
            self.check_return_status()

    def get_task_status(self, task_id, task_name):
        """
        Retrieve the status of a task by its ID.
        Parameters:
            - task_id (str): The ID of the task whose status is to be retrieved.
            - task_name (str): The name of the task.
        Returns:
            response (dict): The response containing the status of the task.
        Note:
            This method makes an API call to retrieve the task status and logs the status information.
            If an error occurs during the API call, it will be caught and logged.
        """
        # Make an API call to retrieve the task tree
        try:
            response = self.dnac_apply["exec"](
                family="task",
                function="get_task_by_id",
                params=dict(task_id=task_id),
                op_modifies=True,
            )
            self.log("Response received post 'get_task_by_id' API Call for the Task {0} with Task id {1} "
                     "is {2}".format(task_name, str(task_id), str(response)), "DEBUG")

            if response:
                response = response["response"]
            else:
                self.log("No response received from the 'get_task_by_id' API call.", "CRITICAL")
            return response

        # Log the error if an exception occurs during the API call
        except Exception as e:
            self.msg = "Error occurred while retrieving 'get_task_by_id' for Task {0} with Task id {1}. Error: {2}".format(task_name, task_id, str(e))
            self.update_result("failed", False, self.msg, "ERROR")
            self.check_return_status()

    def get_task_tree(self, task_id, task_name):
        """
        Retrieve the tree of a task by its ID.
        Parameters:
            - task_id (str): The ID of the task whose status is to be retrieved.
            - task_name (str): The name of the task.
        Returns:
            response (dict): The response containing the status of the task.
        Note:
            This method makes an API call to retrieve the task status and logs the status information.
            If an error occurs during the API call, it will be caught and logged.
        """
        # Make an API call to retrieve the task status
        try:
            response = self.dnac_apply["exec"](
                family="task",
                function="get_task_tree",
                params=dict(task_id=task_id),
                op_modifies=True,
            )
            self.log("Response received post 'get_task_tree' API call for the Task {0} with Task id {1} "
                     "is {2}".format(task_name, str(task_id), str(response)), "DEBUG")
            if response:
                response = response["response"]
            else:
                self.log("No response received from the 'get_task_tree' API call.", "CRITICAL")
            return response

        # Log the error if an exception occurs during the API call
        except Exception as e:
            self.msg = "Error occurred while retrieving 'get_task_tree' for Task {0} with task id {1}: {2}".format(task_name, task_id, str(e))
            self.update_result("failed", False, self.msg, "ERROR")
            self.check_return_status()

    def update_result(self, status, changed, msg, log_level, data=None):
        """
        Update the result of the operation with the provided status, message, and log level.
        Parameters:
            - status (str): The status of the operation ("success" or "failed").
            - changed (bool): Indicates whether the operation caused changes.
            - msg (str): The message describing the result of the operation.
            - log_level (str): The log level at which the message should be logged ("INFO", "ERROR", "CRITICAL", etc.).
            - data (dict, optional): Additional data related to the operation result.
        Returns:
            self (object): An instance of the class.
        Note:
            - If the status is "failed", the "failed" key in the result dictionary will be set to True.
            - If data is provided, it will be included in the result dictionary.
        """
        # Update the result attributes with the provided values
        self.status = status
        self.result["status"] = status
        self.result["msg"] = msg
        self.result["changed"] = changed

        # Log the message at the specified log level
        self.log(msg, log_level)

        # If the status is "failed", set the "failed" key to True
        if status == "failed":
            self.result["failed"] = True

        # If additional data is provided, include it in the result dictionary
        if data:
            self.result["data"] = data

        return self

    def exit_while_loop(self, start_time, task_id, task_name, response):
        """
        Check if the elapsed time exceeds the specified timeout period and exit the while loop if it does.
        Parameters:
            - start_time (float): The time when the while loop started.
            - task_id (str): ID of the task being monitored.
            - task_name (str): Name of the task being monitored.
            - response (dict): Response received from the task status check.
        Returns:
            bool: True if the elapsed time exceeds the timeout period, False otherwise.
        """
        # If the elapsed time exceeds the timeout period
        if time.time() - start_time > self.params.get("dnac_api_task_timeout"):
            if response.get("data"):
                # If there is data in the response, include it in the error message
                self.msg = "Task {0} with task id {1} has not completed within the timeout period. Task Status: {2} ".format(
                    task_name, task_id, response.get("data"))
            else:
                # If there is no data in the response, generate a generic error message
                self.msg = "Task {0} with task id {1} has not completed within the timeout period.".format(
                    task_name, task_id)

            # Update the result with failure status and log the error message
            self.update_result("failed", False, self.msg, "ERROR")
            return True

        return False

    def handle_error(self, task_name, mgmt_ip_to_instance_id_map, failure_reason=None):
        """
        Handle error encountered during task execution.
        Parameters:
            - task_name (str): Name of the task being performed.
            - mgmt_ip_to_instance_id_map (dict): Mapping of management IP addresses to instance IDs.
            - failure_reason (str, optional): Reason for the failure, if available.
        Returns:
            self (object): An instance of the class used for interacting with Cisco Catalyst Center.
        """
        # If failure reason is provided, include it in the error message
        ip_address_list_str = ", ".join(list(mgmt_ip_to_instance_id_map.keys()))
        if failure_reason:
            self.msg = "An error occurred while performing {0} on device(s): {1}. The operation failed due to the following reason: {2}".format(
                task_name, ip_address_list_str, failure_reason)
        # If no failure reason is provided, generate a generic error message
        else:
            self.msg = "An error occurred while performing {0} on device(s): {1}".format(
                task_name, ip_address_list_str)

        # Update the result with failure status and log the error message
        self.update_result("failed", False, self.msg, "ERROR")

        return self

    def get_task_result(self, task_id, device_ids):
        """
        This function retrieves the status of compliance check tasks in Cisco Catalyst Center.
        Parameters:
            - task_id (str): The ID of the compliance check task.
            - device_ids (list): A list of device UUIDs involved in the compliance check task.
        Returns:
            dict: A dictionary containing the task ID as the key, and a dictionary with 'msg' and 'status' as the value.
        Description:
            This function continuously checks the status of a compliance check task until completion or timeout.
            It handles various scenarios such as task completion, task failure, or errors during execution.
            Upon successful completion, it logs the modified compliance response and updates the result accordingly.
            If the task does not complete within the timeout period, it returns a timeout status.
            If there is an error during task execution, it returns the error message and status.
            If the task fails, it returns the failure message and status.
        """
        task_name = "Run Compliance Check"
        start_time = time.time()

        while True:
            response = self.get_task_status(task_id, task_name)

            # Check if response returned
            if not response:
                msg = "Error retrieving Task status for {0} with Task Id: {1}".format(task_name, task_id)
                return {task_id: {"msg": msg, "status": None}}

            # Check if the elapsed time exceeds the timeout
            if time.time() - start_time > self.params.get("dnac_api_task_timeout"):
                msg = "Task {0} with task id {1} has not completed within the timeout period.".format(task_name, task_id)
                return {task_id: {"msg": msg, "status": "Timedout"}}

            # Handle error if task execution encounters an error
            if response.get("isError"):
                msg = "Task {0} with task id {1} has encountered an Error: {2}".format(task_name, task_id, response.get("failureReason"))
                return {task_id: {"msg": msg, "status": "Error"}}

            # Check if task completed successfully
            if not response.get("isError") and "success" in response.get("progress").lower():
                device_ids_str = ", ".join(device_ids)
                msg = "{0} has completed successfully on device(s): {1}".format(task_name, device_ids_str)
                return {task_id: {"msg": msg, "status": "Success"}}

            # Check if task failed
            if "failed" in response.get("progress").lower():
                device_ids_str = ", ".join(device_ids)
                msg = "Failed to {0} on the following device(s): {1}".format(task_name, device_ids_str)
                return {task_id: {"msg": msg, "status": "Failed"}}

    def get_batches_result(self, batches_dict):
        """
        Retrieves the results of compliance check tasks for a list of device batches.
        Parameters:
            batches_dict (dict): A dictionary where each key is a batch index and the value is a dictionary
                                 containing 'task_id' and 'batch_params'.
        Returns:
            list: A list of dictionaries where each dictionary contains the 'task_id', 'batch_params',
                  'task_status', and 'msg' for each batch.
        Description:
            This function iterates over the provided batches, retrieves the task status for each batch,
            and stores the result including task ID, batch parameters, task status, and message.
        """
        batches_result = []
        for idx, batch_info in batches_dict.items():
            task_id = batch_info["task_id"]
            device_ids = batch_info["batch_params"]["deviceUuids"]

            # Get task status for the current batch
            task_status = self.get_task_result(task_id, device_ids)
            self.log("The task status of batch: {0} with task id: {1} is {2}".format(idx, task_id, task_status), "INFO")

            # Extract message and status from the task status result
            msg = task_status[task_id]["msg"]
            status = task_status[task_id]["status"]

            # Store the result for the current batch
            batch_result = {
                "task_id": task_id,
                "batch_params": batch_info["batch_params"],
                "task_status": status,
                "msg": msg
            }

            # Append the current batch result to the batches_result list
            batches_result.append(batch_result)

        self.log("Collective result of all batches: {0}".format(batches_result), "DEBUG")
        return batches_result

    def validate_batch_result(self, batches_result, retried_batches=None):
        """
        Validates the results of compliance check tasks for device batches.
        Parameters:
            batches_status (list): A list of dictionaries where each dictionary contains 'task_id',
                                   'batch_params', 'task_status', and 'msg' for each batch.
        Returns:
            list: A list of device IDs that have successfully completed the compliance check.
        Description:
            This function iterates over the provided batches status, checks the task status for each batch,
            and collects the device IDs for batches that have completed successfully. For batches that failed,
            it re-runs the compliance check with a batch size of 1, validates the results recursively, and collects
            the successful device IDs.
        """
        if retried_batches is None:
            retried_batches = set()
        successful_devices = []

        # Iterate over each batch in the batches_status list
        for batch in batches_result:
            task_status = batch.get("task_status")
            batch_params = batch.get("batch_params")
            device_ids = tuple(batch_params.get("deviceUuids"))

            # Check if the task status is successful
            if task_status == "Success":
                successful_devices.extend(device_ids)
            else:
                # Check if the batch has already been retried with batch size of 1
                if device_ids in retried_batches:
                    device_ids_str = ", ".join(device_ids)
                    self.log(
                        "Batch for device(s) {0} has already been retried with batch size of 1 and failed. "
                        "Stopping recursion.".format(device_ids_str),
                        "ERROR"
                    )
                    continue

                self.log("Re-running compliance check for batch {0} with batch_result: {1} ".format(batch, batches_result), "WARNING")
                # Re-run the compliance check for the failed batch with batch size of 1
                retried_batches.add(device_ids)
                batches_dict = self.run_compliance(batch_params, batch_size=1)
                batches_result = self.get_batches_result(batches_dict)

                # Recursively validate the batch results and append the successful device IDs
                successful_devices.extend(self.validate_batch_result(batches_result, retried_batches=retried_batches))
        msg = ("The results of all batches have been validated, and the compliance checks "
               "were successfully executed on following devices: {0}".format(successful_devices))
        self.log(msg, "DEBUG")

        return successful_devices

    def get_compliance_task_status(self, batches_dict, mgmt_ip_to_instance_id_map):
        """
        Retrieves and processes compliance check task statuses for multiple batches.
        Parameters:
            batches_dict (dict): A dictionary containing information about each batch of compliance tasks.
            mgmt_ip_to_instance_id_map (dict): A dictionary mapping management IP addresses to instance IDs.
        Returns:
            self
        Description:
            This function processes the compliance check statuses for multiple batches of devices. It determines
            which devices were successful and which were unsuccessful. If any batches were successful, it logs
            the success message, updates the result, and retrieves compliance reports. If all batches failed,
            it logs the failure message and updates the result accordingly.
        """
        task_name = "Run Compliance Check"
        batches_result = self.get_batches_result(batches_dict)
        successful_devices = self.validate_batch_result(batches_result)
        successful_devices_str = ", ".join(successful_devices)
        self.log("{0} successful on device(s): {1}".format(task_name, successful_devices_str), "DEBUG")

        # Reverse the mgmt_ip_to_instance_id_map to map device IDs to IPs
        id_to_ip_map = {v: k for k, v in mgmt_ip_to_instance_id_map.items()}

        # Determine unsuccessful devices
        all_device_ids = [
            device_id
            for batch in batches_dict.values()
            for device_id in batch["batch_params"]["deviceUuids"]
        ]
        unsuccessful_devices = list(set(all_device_ids) - set(successful_devices))
        unsuccessful_ips = [id_to_ip_map[device_id] for device_id in unsuccessful_devices if device_id in id_to_ip_map]
        unsuccessful_ips_str = ", ".join(unsuccessful_ips)
        self.log("{0} unsuccessful on device(s): {1}".format(task_name, unsuccessful_ips_str), "DEBUG")

        if successful_devices:

            successful_ips = [id_to_ip_map[device_id] for device_id in successful_devices if device_id in id_to_ip_map]
            successful_ips_str = ", ".join(successful_ips)
            self.msg = "{0} has completed successfully on {1} device(s): {2}".format(task_name, len(successful_ips), successful_ips_str)

            if unsuccessful_ips:
                msg = "{0} was unsuccessful on {1} device(s): {2}".format(task_name, len(unsuccessful_ips), unsuccessful_ips_str)
                self.log(msg, "ERROR")
                self.msg += "and was unsuccessful on {0} device(s): {1}".format(len(unsuccessful_ips), unsuccessful_ips_str)

            successful_devices_params = self.want.get("run_compliance_params").copy()
            successful_devices_params["deviceUuids"] = successful_devices
            compliance_report = self.get_compliance_report(successful_devices_params, mgmt_ip_to_instance_id_map)
            self.log("Compliance Report: {0}".format(compliance_report), "INFO")
            self.update_result("success", True, self.msg, "INFO", compliance_report)
        else:
            self.msg = "Failed to {0} on the following device(s): {1}".format(task_name, unsuccessful_ips_str)
            self.update_result("failed", False, self.msg, "CRITICAL")

        return self

    def get_sync_config_task_status(self, task_id, mgmt_ip_to_instance_id_map):
        """
        This function manages the status of device configuration synchronization tasks in Cisco Catalyst Center.
        Parameters:
            - task_id: ID of the synchronization task
            - mgmt_ip_to_instance_id_map: Mapping of management IP addresses to instance IDs
        Returns:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            It validates if synchronization is required, categorizes devices based on compliance status, and checks task completion status.
            If all devices are already compliant, it logs a success message. If some devices have unexpected statuses, it logs an error.
            It continuously checks the task status until completion, updating the result accordingly.
        """
        task_name = "Sync Device Configuration"
        start_time = time.time()

        while True:
            success_devices = []
            failed_devices = []

            response = self.get_task_tree(task_id, task_name)

            # Check if response returned
            if not response:
                self.msg = "Error retrieving Task Tree for the task_name {0} task_id {1}".format(task_name, task_id)
                self.update_result("failed", False, self.msg, "ERROR")
                break

            # Check if the elapsed time exceeds the timeout
            if self.exit_while_loop(start_time, task_id, task_name, response):
                break

            # Handle error if task execution encounters an error
            if response[0].get("isError"):
                failure_reason = response[0].get("failureReason")
                self.handle_error(task_name, mgmt_ip_to_instance_id_map, failure_reason)
                break

            sync_device_config_params = self.want.get("sync_device_config_params")

            for item in response[1:]:
                progress = item["progress"]
                for device_id in sync_device_config_params["deviceId"]:
                    # Get IP from mgmt_ip_to_instance_id_map
                    ip = next((k for k, v in mgmt_ip_to_instance_id_map.items() if v == device_id), None)
                    if device_id in progress and "copy_Running_To_Startup=Success" in progress:
                        success_devices.append(ip)
                        self.log("{0} operation completed successfully on device: {1} with device UUID: {2}".format(task_name, ip, device_id), "DEBUG")
                    elif device_id in progress and "copy_Running_To_Startup=Failed" in progress:
                        self.log("{0} operation FAILED on device: {1} with device UUID: {2}".format(task_name, ip, device_id), "DEBUG")
                        failed_devices.append(ip)

            success_devices = set(success_devices)
            success_devices_str = ", ".join(success_devices)
            failed_devices = set(failed_devices)
            failed_devices_str = ", ".join(failed_devices)

            # Check conditions and print messages accordingly
            total_devices = len(sync_device_config_params["deviceId"])
            if len(success_devices) == total_devices:
                self.msg = "{0} has completed successfully on {1} device(s): {2}".format(task_name, len(success_devices), success_devices_str)
                self.update_result("success", True, self.msg, "INFO")
                break
            elif failed_devices and len(failed_devices) + len(success_devices) == total_devices:
                self.msg = "{0} task has failed on {1} device(s): {2} and succeeded on {3} device(s): {4}".format(
                    task_name, len(failed_devices), failed_devices_str, len(success_devices), success_devices_str)
                self.update_result("failed", True, self.msg, "CRITICAL")
                break
            elif len(failed_devices) == total_devices:
                self.msg = "{0} task has failed on {1} device(s): {2}".format(task_name, len(failed_devices), failed_devices_str)
                self.update_result("failed", False, self.msg, "CRITICAL")
                break

        return self

    def get_diff_merged(self):
        """
        This method is designed to Perform Network Compliance Actions in Cisco Catalyst Center.
        Parameters: None
        Returns:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            This method orchestrates compliance check operation and device configuration synchronization tasks specified in a playbook.
            It ensures all required tasks are present, executes them, and checks their status, facilitating smooth playbook execution.
        """
        # Action map for different network compliance operations
        action_map = {
            "run_compliance_params": (self.run_compliance, self.get_compliance_task_status),
            "sync_device_config_params": (self.sync_device_config, self.get_sync_config_task_status)
        }

        # Iterate through the action map and execute specified actions
        for action_param, (action_func, status_func) in action_map.items():

            # Execute the action and check its status
            if self.want.get(action_param):
                if action_param == "run_compliance_params":
                    self.log("Performing '{0}' operation...".format(action_func.__name__), "DEBUG")
                    batch_size = self.want.get("run_compliance_batch_size")
                    result_task_id = action_func(self.want.get(action_param), batch_size=batch_size)
                else:
                    self.log("Performing '{0}' operation...".format(action_func.__name__), "DEBUG")
                    result_task_id = action_func(self.want.get(action_param))

                if not result_task_id:
                    self.msg = "An error occurred while retrieving the task_id of the {0} operation.".format(action_func.__name__)
                    self.update_result("failed", False, self.msg, "CRITICAL")
                else:
                    status_func(result_task_id, self.want.get("mgmt_ip_to_instance_id_map")).check_return_status()

        return self

    def verify_diff_merged(self, config):
        """
        Verify the success of the "Sync Device Configuration" operation.
        Parameters:
            config (dict): A dictionary containing the configuration details.
        Returns:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            This method verifies the success of the "Sync Device Configuration" operation in the context of network compliance management.
            It checks if the configuration includes the option to synchronize device configurations (`sync_device_config`).
            If this option is present, the function proceeds to compare compliance details before and after executing the synchronization operation.
            It logs relevant information at each step and concludes by determining whether the synchronization was successful.
        """
        if config.get("sync_device_config"):
            # Get compliance details before running sync_device_config
            compliance_details_before = self.want.get("compliance_details")
            self.log("Compliance details before running sync_device_config: {0}".format(compliance_details_before), "INFO")

            # Get compliance details after running sync_device_config
            compliance_details_after = self.get_compliance_report(
                self.want.get("compliance_detail_params_sync"),
                self.want.get("mgmt_ip_to_instance_id_map")
            )
            if not compliance_details_after:
                self.msg = "Error occured when Retrieving Compliance Details after for verifying configuration."
                self.update("failed", False, self.msg, "ERROR")
                self.check_return_status()

            self.log("Compliance details after running sync_device_config: {0}.".format(compliance_details_after), "INFO")

            # Get the device IDs to check
            sync_device_ids = self.want.get("sync_device_config_params").get("deviceId", [])
            if not sync_device_ids:
                self.log(
                    "No device IDs found in sync_device_config_params, Sync Device Configuration "
                    "operation may not have been performed.",
                    "WARNING"
                )
                return self

            # Initialize the status lists
            all_statuses_before = []
            all_statuses_after = []

            # Iterate over the device IDs and check their compliance status
            for device_id in sync_device_ids:
                # Find the corresponding IP address from the mgmt_ip_to_instance_id_map
                ip_address = next((ip for ip, id in self.want.get("mgmt_ip_to_instance_id_map").items() if id == device_id), None)
                if ip_address:
                    # Get the status before
                    compliance_before = compliance_details_before.get(ip_address, [])
                    if compliance_before:
                        all_statuses_before.append(compliance_before[0]["status"])
                    # Get the status after
                    compliance_after = compliance_details_after.get(ip_address, [])
                    if compliance_after:
                        all_statuses_after.append(compliance_after[0]["status"])

            # Check if all statuses changed from "NON_COMPLIANT" to "COMPLIANT"
            if (
                all(all_status == "NON_COMPLIANT" for all_status in all_statuses_before) and
                all(all_status == "COMPLIANT" for all_status in all_statuses_after)
            ):
                self.log("Verified the success of the Sync Device Configuration operation.")
            else:
                self.log(
                    "Sync Device Configuration operation may have been unsuccessful "
                    "since not all devices have 'COMPLIANT' status after the operation.",
                    "WARNING"
                )
        else:
            self.log("Verification of configuration is not required for run compliance operation!", "INFO")
        return self


def main():
    """
    main entry point for module execution
    """

    # Define the specification for the module"s arguments
    element_spec = {"dnac_host": {"required": True, "type": "str"},
                    "dnac_port": {"type": "str", "default": "443"},
                    "dnac_username": {"type": "str", "default": "admin", "aliases": ["user"]},
                    "dnac_password": {"type": "str", "no_log": True},
                    "dnac_verify": {"type": "bool", "default": "True"},
                    "dnac_version": {"type": "str", "default": "2.2.3.3"},
                    "dnac_debug": {"type": "bool", "default": False},
                    "dnac_log_level": {"type": "str", "default": "WARNING"},
                    "dnac_log_file_path": {"type": "str", "default": "dnac.log"},
                    "dnac_log_append": {"type": "bool", "default": True},
                    "dnac_log": {"type": "bool", "default": False},
                    "validate_response_schema": {"type": "bool", "default": True},
                    "config_verify": {"type": "bool", "default": False},
                    "dnac_api_task_timeout": {"type": "int", "default": 1200},
                    "dnac_task_poll_interval": {"type": "int", "default": 2},
                    "config": {"required": True, "type": "list", "elements": "dict"},
                    "state": {"default": "merged", "choices": ["merged"]}
                    }

    # Initialize the Ansible module with the provided argument specifications
    module = AnsibleModule(argument_spec=element_spec,
                           supports_check_mode=False)

    # Initialize the NetworkCompliance object with the module
    ccc_network_compliance = NetworkCompliance(module)

    # Get the state parameter from the provided parameters
    state = ccc_network_compliance.params.get("state")

    # Check if the state is valid
    if state not in ccc_network_compliance.supported_states:
        ccc_network_compliance.status = "invalid"
        ccc_network_compliance.msg = "State {0} is invalid".format(state)
        ccc_network_compliance.check_return_status()

    # Validate the input parameters and check the return status
    ccc_network_compliance.validate_input().check_return_status()

    # Get the config_verify parameter from the provided parameters
    config_verify = ccc_network_compliance.params.get("config_verify")

    # Iterate over the validated configuration parameters
    for config in ccc_network_compliance.validated_config:
        ccc_network_compliance.get_want(config).check_return_status()
        ccc_network_compliance.get_diff_state_apply[state]().check_return_status()
        if config_verify:
            ccc_network_compliance.verify_diff_state_apply[state](config).check_return_status()

    # Exit with the result obtained from the NetworkCompliance object
    module.exit_json(**ccc_network_compliance.result)


if __name__ == "__main__":
    main()
