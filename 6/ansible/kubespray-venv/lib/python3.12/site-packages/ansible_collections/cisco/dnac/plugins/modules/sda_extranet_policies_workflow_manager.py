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
module: sda_extranet_policies_workflow_manager
short_description: SDA Extranet Policies Module provides functionality for managing SDA Extranet Policy in Cisco Catalyst Center.
description:
  - Manage extranet policy operations such as add/update/delete.
  - API to create a new extranet policy.
  - API to update an existing or edit an existing extranet policy.
  - API for deletion of an existing extranet policy using the policy name.
version_added: "6.17.0"
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
    choices: [ merged, deleted ]
    default: merged
  config:
    description: List of Extranet Policy Details for Creating, Updating, or Deleting Operations.
    type: list
    elements: dict
    required: True
    suboptions:
      extranet_policy_name:
        description: Name of the SDA Extranet Policy.
                     This parameter allows you to specify the desired name when creating a new extranet policy.
                     The same name can be used to update or delete the policy.
                     Note - This parameter is required when creating, updating or deleting extranet policy.
        type: str
      provider_virtual_network:
        description: Specifies the Provider Virtual Network containing shared services resources that subscribers need to access.
                     If a virtual network is already defined as a Provider, it cannot be assigned as a provider again.
                     Ensure the default route is present in the Global Routing Table if INFRA_VN is defined as the Provider.
                     For Subscriber Virtual Networks with multiple Providers having overlapping routes, traffic will be
                     load-balanced across those Provider Virtual Networks.
                     This parameter is required when creating or updating extranet policy.
        type: str
      subscriber_virtual_networks:
        description: Specifies a list of Subscriber Virtual Networks that require access to the Provider Virtual Network
                     containing shared services resources.
                     A Virtual Network previously defined as a Provider cannot be selected as a subscriber.
                     This parameter is required when creating or updating extranet policy.
        type: list
        elements: str
      fabric_sites:
        description: Specifies the Fabric Site(s) where this Extranet Policy will be applied.
                     The Provider Virtual Network must be added to a Fabric Site before applying the policy.
                     Fabric Site(s) connected to the same SD-Access Transit must have consistent Extranet Policies.
                     Selecting a Fabric Site connected to an SD-Access Transit will automatically select all other Sites connected to that Transit.
        type: list
        elements: str


requirements:
- dnacentersdk == 2.7.0
- python >= 3.9
notes:
  - SDK Methods used are
    sites.Sites.get_site
    sda.SDA.get_fabric_sites
    sda.SDA.get_extranet_policies
    sda.SDA.add_extranet_policy
    sda.SDA.update_extranet_policy
    sda.SDA.delete_extranet_policy_by_id
    task.Task.get_task_by_id

  - Paths used are
    get /dna/intent/api/v1/site
    get /dna/intent/api/v1/sda/fabricSites
    get /dna/intent/api/v1/sda/extranetPolicies
    post /dna/intent/api/v1/sda/extranetPolicies
    put /dna/intent/api/v1/sda/extranetPolicies
    delete dna/intent/api/v1/sda/extranetPolicies/${id}
    get /dna/intent/api/v1/task/{taskId}

"""

EXAMPLES = r"""
- name: Create Extranet Policy
  cisco.dnac.sda_extranet_policies_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: True
    state: merged
    config:
      - extranet_policy_name: "test_extranet_policy_1"
        provider_virtual_network: "VN_1"
        subscriber_virtual_networks: ["VN_2", "VN_3"]

- name: Create Extranet Policy with Fabric Site(s) specified
  cisco.dnac.sda_extranet_policies_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: True
    state: merged
    config:
      - extranet_policy_name: "test_extranet_policy_1"
        provider_virtual_network: "VN_1"
        subscriber_virtual_networks: ["VN_2", "VN_3"]
        fabric_sites: ["Global/Test_Extranet_Polcies/USA", "Global/Test_Extranet_Polcies/India"]

- name: Update existing Extranet Policy
  cisco.dnac.sda_extranet_policies_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: True
    state: merged
    config:
      - extranet_policy_name: "test_extranet_policy_1"
        provider_virtual_network: "VN_1"
        subscriber_virtual_networks: ["VN_2", "VN_4"]

- name: Update existing Extranet Policy with Fabric Site(s) specified
  cisco.dnac.sda_extranet_policies_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: True
    state: merged
    config:
      - extranet_policy_name: "test_extranet_policy_1"
        fabric_sites: ["Global/Test_Extranet_Polcies/USA", "Global/Test_Extranet_Polcies/India"]
        provider_virtual_network: "VN_1"
        subscriber_virtual_networks: ["VN_2", "VN_4"]

- name: Delete Extranet Policy
  cisco.dnac.sda_extranet_policies_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: True
    state: deleted
    config:
      - extranet_policy_name: "test_extranet_policy_1"
"""

RETURN = r"""
#Case_1: Response when task is successful
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

#Case_3: Response when Error Occurs
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


class SDAExtranetPolicies(DnacBase):
    """
    A class for managing Extranet Policies within the Cisco DNA Center using the SDA API.
    """
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
        Validates the input configuration parameters for the playbook.
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
        # Check if configuration is available
        if not self.config:
            self.status = "success"
            self.msg = "Configuration is not available in the playbook for validation"
            self.log(self.msg, "ERROR")
            return self

        # Expected schema for configuration parameters
        temp_spec = {
            "extranet_policy_name": {"type": "str", "required": True},
            "fabric_sites": {"type": "list", "elements": "str", "required": False},
            "provider_virtual_network": {"type": "str", "required": False},
            "subscriber_virtual_networks": {"type": "list", "elements": "str", "required": False},
        }

        # Validate params
        valid_temp, invalid_params = validate_list_of_dicts(
            self.config, temp_spec
        )

        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(invalid_params)
            self.update_result("failed", False, self.msg, "ERROR")
            return self

        # Set the validated configuration and update the result with success status
        self.validated_config = valid_temp
        self.msg = "Successfully validated playbook configuration parameters using 'validated_input': {0}".format(str(valid_temp))
        self.update_result("success", False, self.msg, "INFO")
        return self

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

    def get_fabric_ids_list(self, site_details):
        """
        Extracts a list of fabric IDs from the provided site details.
        Parameters:
            - site_details (dict): A dictionary containing site information. Each key-value pair
                                   represents a site, where the value is another dictionary that
                                   includes a 'fabric_id'.
        Returns:
            list: A list of fabric IDs extracted from the site details.
        Description:
            This method iterates over the values in the provided site_details dictionary, extracts
            the 'fabric_id' from each value, and appends it to a list. The resulting list of fabric IDs
            is then returned.
        """
        # Initialize an empty list to store fabric IDs
        fabric_ids_list = []

        # Iterate over each site's information in the site details
        for site_info in site_details.values():
            fabric_ids_list.append(site_info['fabric_id'])
        return fabric_ids_list

    def validate_merged_parameters(self, config):
        """
        Validate that the required parameters are present in the configuration for performing
        Add or Update Extranet Policy operations.
        Parameters:
            - config (dict): A dictionary containing the configuration parameters to be validated.
        Returns:
            None: This function does not return a value. It logs messages and raises exceptions
                  if required parameters are missing.
        Description:
            This method checks the provided configuration for the presence of the required parameters:
            'provider_virtual_network' and 'subscriber_virtual_networks'. If any of these parameters
            are missing, it logs an error message and raises an exception to halt execution. If all
            required parameters are present, it logs a success message indicating successful validation.
        """
        # Check for provider_virtual_network
        provider_virtual_network = config.get("provider_virtual_network")
        if provider_virtual_network is None:
            msg = ("Missing required parameter: 'provider_virtual_network'. "
                   "(extranet_policy_name, provider_virtual_network, and subscriber_virtual_networks) - "
                   "are the required parameters for performing Add or Update Extranet Policy operations.")
            self.log(msg, "ERROR")
            self.module.fail_json(msg)

        # Check for subscriber_virtual_networks
        subscriber_virtual_networks = config.get("subscriber_virtual_networks")
        if subscriber_virtual_networks is None:
            msg = (
                "Missing required parameter: 'subscriber_virtual_networks'. "
                "(extranet_policy_name, provider_virtual_network, and subscriber_virtual_networks) - "
                "are the required parameters for performing Add or Update Extranet Policy operations."
            )
            self.log(msg, "ERROR")
            self.module.fail_json(msg)

        self.log(
            "Successfully validated that the required parameters — (extranet_policy_name, "
            "provider_virtual_network, and subscriber_virtual_networks) are provided",
            "INFO"
        )

    def get_add_extranet_policy_params(self, config, site_details=None):
        """
        Generate parameters required for adding an Extranet Policy based on the provided configuration and site details.
        Parameters:
            - config (dict): A dictionary containing the configuration parameters.
            - site_details (dict, optional): A dictionary containing site details. Default is None.
        Returns:
            dict: A dictionary containing the parameters for adding an Extranet Policy.
        Description:
            This method constructs a dictionary of parameters required for adding an Extranet Policy.
            It includes the 'extranetPolicyName', 'providerVirtualNetworkName', and 'subscriberVirtualNetworkNames'
            from the configuration. If 'fabric_sites' are provided in the configuration and site details are available,
            it also includes the 'fabricIds' obtained from the site details.
        """
        # Initialize the parameters dictionary with basic required parameters
        add_extranet_policy_params = {
            "extranetPolicyName": config.get("extranet_policy_name"),
            "providerVirtualNetworkName": config.get("provider_virtual_network"),
            "subscriberVirtualNetworkNames": config.get("subscriber_virtual_networks")
        }

        # Check if 'fabric_sites' are provided and site details are available
        if config.get("fabric_sites") and site_details:
            add_extranet_policy_params["fabricIds"] = self.get_fabric_ids_list(site_details)

        return add_extranet_policy_params

    def get_update_extranet_policy_params(self, config, extranet_policy_id, site_details=None):
        """
        Generate parameters required for updating an Extranet Policy based on the provided configuration,
        policy ID, and site details.
        Parameters:
            config (dict): A dictionary containing the configuration parameters.
            extranet_policy_id (str): The ID of the Extranet Policy to be updated.
            site_details (dict, optional): A dictionary containing site details. Default is None.
        Returns:
            dict: A dictionary containing the parameters for updating an Extranet Policy.
        Description:
            This method constructs a dictionary of parameters required for updating an Extranet Policy.
            It includes the 'id' of the policy, 'extranetPolicyName', 'providerVirtualNetworkName', and
            'subscriberVirtualNetworkNames' from the configuration. If 'fabric_sites' are provided in the
            configuration and site details are available, it also includes the 'fabricIds' obtained from the
            site details.
        """
        # Initialize the parameters dictionary with basic required parameters
        update_extranet_policy_params = {
            "id": extranet_policy_id,
            "extranetPolicyName": config.get("extranet_policy_name"),
            "providerVirtualNetworkName": config.get("provider_virtual_network"),
            "subscriberVirtualNetworkNames": config.get("subscriber_virtual_networks")
        }

        # Check if 'fabric_sites' are provided and site details are available
        if config.get("fabric_sites") and site_details:
            update_extranet_policy_params["fabricIds"] = self.get_fabric_ids_list(site_details)

        return update_extranet_policy_params

    def get_delete_extranet_policy_params(self, extranet_policy_id):
        """
        Generate parameters required for deleting an Extranet Policy based on the provided policy ID.
        Parameters:
            extranet_policy_id (str): The unique identifier of the Extranet Policy to be deleted.
        Returns:
            dict: A dictionary containing the parameters for deleting an Extranet Policy.
        Description:
            This method constructs a dictionary of parameters required for deleting an Extranet Policy.
            It includes the 'id' of the policy, which is necessary for identifying the specific policy
            to be deleted.
        """
        # Create a dictionary with the extranet policy ID
        delete_extranet_policy_params = {
            "id": extranet_policy_id
        }

        return delete_extranet_policy_params

    def validate_site_exists(self, site_name):
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
            if response["response"]:
                site = response.get("response")
                site_id = site[0].get("id")
                site_exists = True
            else:
                self.log("No response received from the 'get_site' API call.", "WARNING")

        except Exception as e:
            # Log an error message and fail if an exception occurs
            self.log("An error occurred while retrieving site details for Site '{0}' using 'get_site' API call: {1}".format(site_name, str(e)), "ERROR")

        if not site_exists:
            self.msg = "An error occurred while retrieving site details for Site '{0}'. Please verify that the site exists.".format(site_name)
            self.update_result("failed", False, self.msg, "ERROR")
            self.check_return_status()

        return (site_exists, site_id)

    def get_site_details(self, fabric_sites):
        """
        Retrieve details for each site in the provided fabric sites list.
        Parameters:
            - fabric_sites (list): A list of site names to be validated and detailed.
        Returns:
            dict: A dictionary containing the details for each site, including existence and site ID.
        Description:
            This method takes a list of fabric sites and checks if each site exists using the validate_site_exists method.
            It constructs a dictionary where each key is a site name and the value is another dictionary containing
            'site_exists' (a boolean indicating if the site exists) and 'site_id' (the unique identifier of the site).
        """
        # Initialize an empty dictionary to store site details
        site_details = {}

        # Iterate over each site in the provided fabric sites list
        for site in fabric_sites:
            # Validate if the site exists and retrieve its ID
            (site_exists, site_id) = self.validate_site_exists(site)
            site_details[site] = {
                "site_exists": site_exists,
                "site_id": site_id,
            }

        return site_details

    def get_fabric_sites(self, site_name, site_id):
        """
        Retrieve the fabric ID for a given site using the SDA 'get_fabric_sites' API call.
        Parameters:
            - site_name (str): The name of the site.
            - site_id (str): The unique identifier of the site.
        Returns:
            str: The fabric ID if found, otherwise None.
        Description:
            This method calls the SDA 'get_fabric_sites' API to retrieve the fabric ID for a specified site. It logs the response,
            processes the response to extract the fabric ID, and handles any exceptions that occur during the API call.
        """
        try:
            # Call the SDA 'get_fabric_sites' API with the provided site ID
            response = self.dnac._exec(
                family="sda",
                function="get_fabric_sites",
                op_modifies=True,
                params={"siteId": site_id},
            )
            self.log("Response received post SDA - 'get_fabric_sites' API call: {0}".format(str(response)), "DEBUG")

            # Process the response if available
            if response["response"]:
                fabric_id = response.get("response")[0]["id"]
                return fabric_id
            else:
                self.log("No response received from the SDA - 'get_fabric_sites' API call.", "WARNING")
                return None
        except Exception as e:
            # Log an error message and fail if an exception occurs
            self.msg = (
                "An error occurred while retrieving fabric Site 'Id' for Site '{0}' using SDA - "
                "'get_fabric_sites' API call: {1}".format(site_name, str(e))
            )
            self.update_result("failed", False, self.msg, "ERROR")
            self.check_return_status()

    def get_fabric_sites_ids(self, site_details):
        """
        Retrieve and update fabric IDs for a list of sites.
        Parameters:
            - site_details (dict): A dictionary where each key is a site name and the value is another dictionary
              containing site information, including "site_id".
        Returns:
            dict: The updated dictionary with fabric IDs added to each site's information.
        Description:
            This method iterates through the provided `site_details` dictionary, retrieves the fabric ID for each site
            by calling the `get_fabric_sites` method, and logs the retrieved fabric IDs along with site details.
            It updates the `site_details` dictionary to include the fabric ID for each site and logs the updated
            information.
        """
        for site_name, site_info in site_details.items():
            site_id = site_info["site_id"]
            # Get the fabric ID using the site name and site ID
            fabric_id = self.get_fabric_sites(site_name, site_id)
            self.log("Fabric Id: {0} collected for the fabric_site: {1} with siteId: {2}".format(fabric_id, site_name, site_id))
            site_info["fabric_id"] = fabric_id
        self.log("Updated 'site_details' with the fabric_ids of each site.  {0}".format(site_details))
        return site_details

    def get_extranet_policies(self, extranet_policy_name):
        """
        Retrieve extranet policies for a given policy name using the SDA 'get_extranet_policies' API call.
        Parameters:
            - extranet_policy_name (str): The name of the extranet policy to retrieve.
        Returns:
            dict or None: The response dictionary containing policy details if found, otherwise None.
        Description:
            This method calls the SDA 'get_extranet_policies' API to retrieve details for the specified extranet
            policy name. It logs the response received from the API call and processes it. If the API call is successful
            and returns data, the first item in the response is returned. If no data is received or an exception occurs,
            appropriate warnings or error messages are logged.
        """
        try:
            # Execute the API call to get extranet policie
            response = self.dnac._exec(
                family="sda",
                function="get_extranet_policies",
                op_modifies=True,
                params={"extranetPolicyName": extranet_policy_name},
            )
            self.log("Response received post SDA - 'get_extranet_policies' API call: {0}".format(str(response)), "DEBUG")

            # Process the response if available
            if response.get("response"):
                response = response.get("response")[0]
                return response
            else:
                self.log("No response received from the SDA - 'get_extranet_policies' API call.", "WARNING")
                return None
        except Exception as e:
            # Log an error message and fail if an exception occurs
            self.msg = (
                "An error occurred while retrieving Extranet Policy Details: '{0}' using SDA - "
                "'get_extranet_policies' API call: {1}".format(extranet_policy_name, str(e))
            )
            self.update_result("failed", False, self.msg, "ERROR")
            self.check_return_status()

    def validate_extranet_policy_exists(self, config):
        """
        Check if an extranet policy exists and retrieve its details.
        Parameters:
            - config (dict): A dictionary containing configuration details, including the key "extranet_policy_name".
        Returns:
            tuple: A tuple containing:
                - bool: `True` if the extranet policy exists, otherwise `False`.
                - str or None: The ID of the extranet policy if it exists, otherwise `None`.
                - dict or None: The details of the extranet policy if it exists, otherwise `None`.
        Description:
            This method verifies the existence of an extranet policy based on the name provided in the `config` dictionary.
            It calls the `get_extranet_policies` method to retrieve policy details. If the policy is found, it sets
            `extranet_policy_exists` to `True` and extracts the policy ID and details. The method returns a tuple containing
            the existence status, policy ID, and policy details.
        """
        # Initialize variables to default values
        extranet_policy_exists = False
        extranet_policy_id = None

        extranet_policy_name = config.get("extranet_policy_name")
        extranet_policy_details = self.get_extranet_policies(extranet_policy_name)

        # Check if the policy details were retrieved successfully
        if extranet_policy_details:
            extranet_policy_exists = True
            extranet_policy_id = extranet_policy_details["id"]

        return (extranet_policy_exists, extranet_policy_id, extranet_policy_details)

    def compare_extranet_policies(self, extranet_policy_details, update_extranet_policy_params):
        """
        Compare the details of two extranet policies to check if they are equivalent.
        Parameters:
            - extranet_policy_details (dict): A dictionary containing the current details of the extranet policy.
            - update_extranet_policy_params (dict): A dictionary containing the updated policy parameters to compare against.
        Returns:
            bool: `True` if all values for the keys match between the two dictionaries, `False` otherwise.
        Description:
            This method compares the details of two extranet policies by iterating over each key in the `extranet_policy_details`
            dictionary and checking if the corresponding values in the `update_extranet_policy_params` dictionary match.
            Lists are compared regardless of order, while other values are compared directly. The method returns `True` if
            all values are equivalent, and `False` if any values differ.
        """
        # Iterate over each key in the extranet policy details and compare the details
        for key in extranet_policy_details:
            value1 = extranet_policy_details.get(key)
            value2 = update_extranet_policy_params.get(key)

            if isinstance(value1, list) and isinstance(value2, list):
                # Compare lists regardless of order
                if sorted(value1) != sorted(value2):
                    return False
            else:
                # Compare values directly
                if value1 != value2:
                    return False

        return True

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
        # Make an API call to retrieve the task status
        try:
            response = self.dnac_apply["exec"](
                family="task",
                function="get_task_by_id",
                params=dict(task_id=task_id),
                op_modifies=True,
            )
            self.log("Response received post 'get_task_by_id' API Call for the Task {0} with Task id {1} "
                     "is {2}".format(task_name, str(task_id), str(response)), "DEBUG")

            if response["response"]:
                response = response["response"]
            else:
                self.log("No response received from the 'get_task_by_id' API call.", "CRITICAL")
            return response

        # Log the error if an exception occurs during the API call
        except Exception as e:
            self.msg = "Error occurred while retrieving 'get_task_by_id' for Task {0} with Task id {1}. Error: {2}".format(task_name, task_id, str(e))
            self.update_result("failed", False, self.msg, "ERROR")
            self.check_return_status()

    def add_extranet_policy(self, add_extranet_policy_params):
        """
        Add a new extranet policy using the SDA 'add_extranet_policy' API call.
        Parameters:
            - add_extranet_policy_params (dict): A dictionary containing the parameters for the new extranet policy to be added.
        Returns:
            str or None: The task ID if the policy is added successfully, otherwise `None`.
        Description:
            This method sends a request to add a new extranet policy using the SDA 'add_extranet_policy' API. It logs the
            response from the API call and processes it to extract the task ID. If the policy is added successfully, the
            task ID is returned. If the API call does not return a response or an exception occurs, appropriate warnings or
            error messages are logged.
        """
        try:
            # Execute the API call to add a new extranet policy
            response = self.dnac._exec(
                family="sda",
                function="add_extranet_policy",
                op_modifies=True,
                params={"payload": [add_extranet_policy_params]},
            )
            self.log("Response received post SDA - 'add_extranet_policy' API call: {0}".format(str(response)), "DEBUG")

            # Process the response if available
            if response["response"]:
                self.result.update(dict(response=response["response"]))
                self.log("Task Id for the 'add_extranet_policy' task  is {0}".format(response["response"].get("taskId")), "INFO")
                # Return the task ID
                return response["response"].get("taskId")
            else:
                self.log("No response received from the SDA - 'add_extranet_policy' API call.", "WARNING")
                return None
        except Exception as e:
            # Log an error message and fail if an exception occurs
            self.msg = (
                "An error occurred while Adding Extranet Policy to the Cisco Catalyst Center. "
                "add_extranet_policy_params: {0}  Error: {1}".format(add_extranet_policy_params, str(e))
            )
            self.update_result("failed", False, self.msg, "ERROR")
            self.check_return_status()

    def get_add_extranet_policy_status(self, task_id):
        """
        Monitor the status of the 'Add Extranet Policy' task until completion or failure.
        Parameters:
            - task_id (str): The unique identifier of the task to monitor.
        Returns:
            self: The instance of the class, allowing for method chaining.
        Description:
            This method continuously polls the status of an ongoing task identified by `task_id`. It retrieves task status
            using `get_task_status` and handles various outcomes, including errors, timeouts, and successful completion.
            If the task encounters errors or fails, it logs appropriate error messages and updates the result. If the task
            completes successfully, it logs a success message and updates the result accordingly. The method will break
            out of the loop either on successful completion, encountering an error, or when a timeout condition is met.
        """
        task_name = "Add Extranet Policy"
        start_time = time.time()

        while True:
            response = self.get_task_status(task_id, task_name)

            # Check if response returned
            if not response:
                self.msg = "Error retrieving Task status for the task_name {0} task_id {1}".format(task_name, task_id)
                self.update_result("failed", False, self.msg, "ERROR")
                break

            # Check if the elapsed time exceeds the timeout
            if self.exit_while_loop(start_time, task_id, task_name, response):
                break

            # Handle error if task execution encounters an error
            if response.get("isError"):
                if response.get("failureReason"):
                    failure_reason = response.get("failureReason")
                    self.msg = (
                        "An error occurred while performing {0} task for add_extranet_policy_params: {1}. "
                        "The operation failed due to the following reason: {2}".format(
                            task_name, self.want.get("add_extranet_policy_params"), failure_reason
                        )
                    )
                    self.update_result("failed", False, self.msg, "ERROR")
                    break
                else:
                    self.msg = (
                        "An error occurred while performing {0} task for add_extranet_policy_params: {1}. "
                        .format(task_name, self.want.get("add_extranet_policy_params"))
                    )
                    self.update_result("failed", False, self.msg, "ERROR")
                    break

            # Check if task completed successfully
            if not response.get("isError") and response.get("progress") == "TASK_PROVISION":
                if "processcfs_complete=true" in response.get("data").lower():
                    extranet_policy_name = self.want.get("add_extranet_policy_params").get("extranetPolicyName")
                    self.msg = "Extranet Policy - '{0}' has been successfully added to the Cisco Catalyst Center.".format(extranet_policy_name)
                    self.update_result("success", True, self.msg, "INFO")
                    break
        return self

    def update_extranet_policy(self, update_extranet_policy_params):
        """
        Update an existing extranet policy using the SDA 'update_extranet_policy' API call.
        Parameters:
            - update_extranet_policy_params (dict): A dictionary containing the parameters for updating the extranet policy.
        Returns:
            str or None: The task ID if the update request is processed successfully, otherwise `None`.
        Description:
            This method sends a request to update an existing extranet policy using the SDA 'update_extranet_policy' API.
            It logs the response from the API call and processes it to extract the task ID. If the API call is successful and
            returns a response, the method updates the result with the response details and returns the task ID. If no response
            is received or if an exception occurs, appropriate warnings or error messages are logged.
        """
        try:
            # Execute the API call to update the extranet policy with the provided parameters
            response = self.dnac._exec(
                family="sda",
                function="update_extranet_policy",
                op_modifies=True,
                params={"payload": [update_extranet_policy_params]},
            )
            self.log("Response received post SDA - 'update_extranet_policy' API call: {0}".format(str(response)), "DEBUG")

            # Process the response if available
            if response["response"]:
                self.result.update(dict(response=response["response"]))
                self.log("Task Id for the 'update_extranet_policy' task  is {0}".format(response["response"].get("taskId")), "INFO")
                # Return the task ID
                return response["response"].get("taskId")
            else:
                self.log("No response received from the SDA - 'update_extranet_policy' API call.", "WARNING")
                return None
        except Exception as e:
            # Log an error message and fail if an exception occurs
            self.msg = (
                "An error occurred while Updating Extranet Policy. "
                "update_extranet_policy_params: {0}. Error - {1} ".format(update_extranet_policy_params, str(e))
            )
            self.update_result("failed", False, self.msg, "ERROR")
            self.check_return_status()

    def get_update_extranet_policy_status(self, task_id):
        """
        Monitor the status of the 'Update Extranet Policy' task until completion or failure.
        Parameters:
            - task_id (str): The unique identifier of the task to monitor.
        Returns:
            self: The instance of the class, allowing for method chaining.
        Description:
            This method continuously polls the status of an ongoing update task identified by `task_id`. It retrieves the
            task status using `get_task_status` and handles different outcomes such as errors, timeouts, and successful
            completion. The method logs appropriate messages based on the status of the task and updates the result with
            success or failure information. The method exits the loop upon encountering an error, exceeding the timeout,
            or successful completion of the task.
        """
        task_name = "Update Extranet Policy"
        start_time = time.time()

        while True:
            response = self.get_task_status(task_id, task_name)

            # Check if response returned
            if not response:
                self.msg = "Error retrieving Task status for the task_name {0} task_id {1}".format(task_name, task_id)
                self.update_result("failed", False, self.msg, "ERROR")
                break

            # Check if the elapsed time exceeds the timeout
            if self.exit_while_loop(start_time, task_id, task_name, response):
                break

            # Handle error if task execution encounters an error
            if response.get("isError"):
                if response.get("failureReason"):
                    failure_reason = response.get("failureReason")
                    self.msg = (
                        "An error occurred while performing {0} task for update_extranet_policy_params: {1}. "
                        "The operation failed due to the following reason: {2}".format(
                            task_name, self.want.get("update_extranet_policy_params"), failure_reason
                        )
                    )
                    self.update_result("failed", False, self.msg, "ERROR")
                    break
                else:
                    self.msg = (
                        "An error occurred while performing {0} task for update_extranet_policy_params: {1}. "
                        .format(task_name, self.want.get("update_extranet_policy_params"))
                    )
                    self.update_result("failed", False, self.msg, "ERROR")
                    break

            # Check if task completed successfully
            if not response.get("isError") and response.get("progress") == "TASK_MODIFY_PUT":
                if "processcfs_complete=true" in response.get("data").lower():
                    extranet_policy_name = self.want.get("update_extranet_policy_params").get("extranetPolicyName")
                    self.msg = "Extranet Policy - '{0}' has been successfully updated!".format(extranet_policy_name)
                    self.update_result("success", True, self.msg, "INFO")
                    break

        return self

    def delete_extranet_policy(self, delete_extranet_policy_params):
        """
        Delete an extranet policy using the SDA 'delete_extranet_policy_by_id' API call.
        Parameters:
            - delete_extranet_policy_params (dict): A dictionary containing the parameters for deleting the extranet policy,
              including the policy ID or other identifying details.
        Returns:
            str or None: The task ID if the delete request is processed successfully, otherwise `None`.
        Description:
            This method sends a request to delete an extranet policy using the SDA 'delete_extranet_policy_by_id' API.
            It logs the response from the API call and processes it to extract the task ID. If the API call is successful and
            returns a response, the method updates the result with the response details and returns the task ID. If no response
            is received or if an exception occurs, appropriate warnings or error messages are logged.
        """
        try:
            # Execute the API call to delete the extranet policy with the provided parameters
            response = self.dnac._exec(
                family="sda",
                function="delete_extranet_policy_by_id",
                op_modifies=True,
                params=delete_extranet_policy_params,
            )
            self.log("Response received post SDA - 'delete_extranet_policy_by_id' API call: {0}".format(str(response)), "DEBUG")

            # Process the response if available
            if response["response"]:
                self.result.update(dict(response=response["response"]))
                self.log("Task Id for the 'delete_extranet_policy_by_id' task  is {0}".format(response["response"].get("taskId")), "INFO")
                # Return the task ID
                return response["response"].get("taskId")
            else:
                self.log("No response received from the SDA - 'delete_extranet_policy_by_id' API call.", "WARNING")
                return None
        except Exception as e:
            # Log an error message and fail if an exception occurs
            self.msg = (
                "An error occurred while Deleting Extranet Policy. "
                "delete_extranet_policy_params: {0}. Error - {1} ".format(delete_extranet_policy_params, str(e))
            )
            self.update_result("failed", False, self.msg, "ERROR")
            self.check_return_status()

    def get_delete_extranet_policy_status(self, task_id):
        """
        Monitor the status of the 'Delete Extranet Policy' task until completion or failure.
        Parameters:
            - task_id (str): The unique identifier of the task to monitor.
        Returns:
            self: The instance of the class, allowing for method chaining.
        Description:
            This method continuously polls the status of an ongoing delete task identified by `task_id`. It uses the
            `get_task_status` method to check the task status and handles various outcomes, such as errors, timeouts,
            and successful completion. The method logs appropriate messages based on the task's status and updates the
            result with success or failure information. The monitoring loop exits upon encountering an error, exceeding
            the timeout, or successfully completing the task.
        """
        task_name = "Delete Extranet Policy"
        start_time = time.time()

        while True:
            response = self.get_task_status(task_id, task_name)

            # Check if response returned
            if not response:
                self.msg = "Error retrieving Task status for the task_name {0} task_id {1}".format(task_name, task_id)
                self.update_result("failed", False, self.msg, "ERROR")
                break

            # Check if the elapsed time exceeds the timeout
            if self.exit_while_loop(start_time, task_id, task_name, response):
                break

            # Handle error if task execution encounters an error
            if response.get("isError"):
                if response.get("failureReason"):
                    failure_reason = response.get("failureReason")
                    self.msg = (
                        "An error occurred while performing {0} task for delete_extranet_policy_params: {1}. "
                        "The operation failed due to the following reason: {2}".format(
                            task_name, self.want.get("delete_extranet_policy_params"), failure_reason
                        )
                    )
                    self.update_result("failed", False, self.msg, "ERROR")
                    break
                else:
                    self.msg = (
                        "An error occurred while performing {0} task for "
                        "delete_extranet_policy_params: {1}. ".format(
                            task_name, self.want.get("delete_extranet_policy_params")
                        )
                    )
                    self.update_result("failed", False, self.msg, "ERROR")
                    break

            # Check if task completed successfully
            if not response.get("isError") and response.get("progress") == "TASK_TERMINATE":
                if "processcfs_complete=true" in response.get("data").lower():
                    extranet_policy_name = self.want.get("extranet_policy_name")
                    self.msg = "Extranet Policy - '{0}' has been successfully deleted!".format(extranet_policy_name)
                    self.update_result("success", True, self.msg, "INFO")
                    break

        return self

    def get_have(self, config):
        """
        Retrieve the current state of the extranet policy based on the provided configuration.
        Parameters:
            - config (dict): Configuration dictionary containing site details.
        Returns:
            self: The instance of the class, allowing for method chaining.
        Description:
            This method checks if the extranet policy specified in the `config` exists. It uses the
            `validate_extranet_policy_exists` method to determine if the policy exists and to retrieve its details.
            The method logs the current state of the extranet policy and updates the instance attribute `have` with
            information about the existence, ID, and details of the extranet policy. It returns the instance for
            method chaining.
        """
        have = {}

        # check if given site exits, if exists store current site info
        (extranet_policy_exists, extranet_policy_id, extranet_policy_details) = self.validate_extranet_policy_exists(config)

        self.log("Current Extranet Policy details (have): {0}".format(str(extranet_policy_details)), "DEBUG")

        have["extranet_policy_exists"] = extranet_policy_exists
        have["extranet_policy_id"] = extranet_policy_id
        have["current_extranet_policy"] = extranet_policy_details

        self.have = have
        self.log("Current State (have): {0}".format(str(self.have)), "INFO")

        return self

    def get_want(self, config, state):
        """
        Generate the desired state parameters for API calls based on the provided configuration and state.
        Parameters:
            - config (dict): Configuration dictionary containing site and policy details.
            - state (str): Desired state, which can be 'merged' or 'delete'.
        Returns:
            self: The instance of the class, allowing for method chaining.
        Description:
            This method determines the parameters required for API calls based on the desired state and configuration.
            It checks if the extranet policy exists and sets the appropriate parameters for creating, updating, or deleting
            the policy. For the 'merged' state, it prepares parameters for updating the policy if it exists or creating
            it if it does not. For the 'delete' state, it prepares parameters for deleting the policy if it exists. The
            method logs the created parameters and updates the instance attribute `want` with these parameters. It returns
            the instance for method chaining.
        """
        # Initialize want
        want = {}
        site_details = {}

        self.log("Creating Parameters for API Calls with state: {0}".format(state))

        # Identify if policy already exists or needs to be created
        extranet_policy_name = config.get("extranet_policy_name")
        extranet_policy_exists = self.have.get("extranet_policy_exists")
        extranet_policy_id = self.have.get("extranet_policy_id")
        extranet_policy_details = self.have.get("current_extranet_policy")

        if state == "merged":
            self.validate_merged_parameters(config)
            fabric_sites = config.get("fabric_sites")
            if fabric_sites:
                self.log("Attempting to get the 'SiteId' for the provided fabric sites: {0}".format(fabric_sites), "DEBUG")
                site_details = self.get_site_details(fabric_sites)
                self.log("Attempting to get the fabric 'Id' for the provided fabric sites: {0}".format(fabric_sites), "DEBUG")
                site_details = self.get_fabric_sites_ids(site_details)

            if extranet_policy_exists:
                self.log(
                    "Extranet Policy - '{0}' exists in the Cisco Catalyst Center, "
                    "therefore setting 'update_extranet_policy_params'.".format(extranet_policy_name),
                    "DEBUG"
                )
                want = dict(update_extranet_policy_params=self.get_update_extranet_policy_params(config, extranet_policy_id, site_details))
                if self.compare_extranet_policies(extranet_policy_details, want["update_extranet_policy_params"]):
                    self.msg = (
                        "Extranet Policy - '{0}' is already same as the update requested, "
                        "and hence an update operation is not required.".format(extranet_policy_name)
                    )
                    self.update_result("ok", False, self.msg, "INFO")
                    self.check_return_status()
                    return self
            else:
                self.log(
                    "Extranet Policy - '{0}' does not exist in the Cisco Catalyst Center, "
                    "therefore setting 'add_extranet_policy_params'.".format(extranet_policy_name),
                    "DEBUG"
                )
                want = dict(add_extranet_policy_params=self.get_add_extranet_policy_params(config, site_details))
        else:
            if extranet_policy_exists:
                self.log(
                    "State is delete and Extranet Policy - '{0}' exists in the Cisco Catalyst Center, "
                    "therefore setting 'delete_extranet_policy_params'.".format(extranet_policy_name),
                    "DEBUG"
                )
                want = dict(extranet_policy_name=extranet_policy_name,
                            delete_extranet_policy_params=self.get_delete_extranet_policy_params(extranet_policy_id))
            else:
                self.msg = (
                    "Extranet Policy - '{0}' does not exist in the Cisco Catalyst Center and "
                    "hence delete operation not required.".format(extranet_policy_name)
                )
                self.update_result("ok", False, self.msg, "INFO")
                self.check_return_status()
                return self

        self.want = want
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")
        return self

    def get_diff_merged(self):
        """
        Executes actions based on the desired state parameters and checks their status.
        Parameters:
            - None
        Returns:
            self: The instance of the class, allowing for method chaining.
        Description:
            This method iterates through a map of action parameters to their corresponding functions for execution and status
            checking. For each action parameter present in the desired state (`want`), the associated action function is called
            to perform the action, and the corresponding status function is used to check the result. It ensures that all actions
            specified in the desired state are executed and their statuses are verified. The method returns the instance for method
            chaining.
        """
        action_map = {
            "add_extranet_policy_params": (self.add_extranet_policy, self.get_add_extranet_policy_status),
            "update_extranet_policy_params": (self.update_extranet_policy, self.get_update_extranet_policy_status),
        }

        for action_param, (action_func, status_func) in action_map.items():
            # Execute the action and check its status
            if self.want.get(action_param):
                result_task_id = action_func(self.want.get(action_param))
                status_func(result_task_id).check_return_status()
        return self

    def get_diff_deleted(self):
        """
        Executes deletion actions based on the desired state parameters and checks their status.
        Parameters:
            - None
        Returns:
            self: The instance of the class, allowing for method chaining.
        Description:
            This method iterates through a map of deletion action parameters to their corresponding functions for execution and
            status checking. For each deletion action parameter present in the desired state (`want`), the associated action
            function is called to perform the deletion, and the corresponding status function is used to check the result.
            It ensures that all deletion actions specified in the desired state are executed and their statuses are verified.
            The method returns the instance for method chaining.
        """
        action_map = {
            "delete_extranet_policy_params": (self.delete_extranet_policy, self.get_delete_extranet_policy_status)

        }
        for action_param, (action_func, status_func) in action_map.items():
            # Execute the action and check its status
            if self.want.get(action_param):
                result_task_id = action_func(self.want.get(action_param))
                status_func(result_task_id).check_return_status()
        return self

    def verify_diff_merged(self, config):
        """
        Verifies the results of the merged state operations by comparing the state before and after the operations.
        Parameters:
            - config (dict): Configuration dictionary containing site and policy details.
        Returns:
            self: The instance of the class, allowing for method chaining.
        Description:
            This method performs verification of operations related to the 'merged' state. It first retrieves the state before
            performing any operations and then compares it with the state after the operations. For add and update operations,
            it logs the states before and after the operations and verifies the success based on the presence or absence of
            the extranet policy and whether any changes were detected. It ensures that the operations have been performed as
            expected and logs appropriate messages based on the results.
        """
        pre_operation_state = self.have.copy()
        desired_state = self.want
        self.get_have(config)
        post_operation_state = self.have.copy()
        extranet_policy_name = config.get("extranet_policy_name")

        if desired_state.get("add_extranet_policy_params"):
            self.log("State before performing ADD Extranet Policy operation: {0}".format(str(pre_operation_state)), "INFO")
            self.log("Desired State: {}".format(str(desired_state)), "INFO")
            self.log("State after performing ADD Extranet Policy operation: {0}".format(str(post_operation_state)), "INFO")

            if post_operation_state["extranet_policy_exists"]:
                self.log("Verified the success of ADD Extranet Policy - '{0}' operation.".format(extranet_policy_name), "INFO")
            else:
                self.log(
                    "The ADD Extranet Policy - '{0}' operation may not have been successful "
                    "since the Extranet Policy does not exist in the Cisco Catalyst Center.".format(extranet_policy_name),
                    "WARNING"
                )

        if self.want.get("update_extranet_policy_params"):
            self.log("State before performing UPDATE Extranet Policy operation: {0}".format(str(pre_operation_state)), "INFO")
            self.log("Desired State: {}".format(str(desired_state)), "INFO")
            self.log("State after performing UPDATE Extranet Policy operation - '{0}'".format(str(post_operation_state)), "INFO")

            if not self.compare_extranet_policies(pre_operation_state["current_extranet_policy"], post_operation_state["current_extranet_policy"]):
                self.log("Verified the success of UPDATE Extranet Policy - '{0}' operation.".format(extranet_policy_name), "INFO")
            else:
                self.log(
                    "The UPDATE Extranet Policy - '{0}' operation may not have been performed or "
                    "may not have been successful because no change was detected in the Extranet Policy "
                    "in the Cisco Catalyst Center".format(extranet_policy_name),
                    "WARNING"
                )
        return self

    def verify_diff_deleted(self, config):
        """
        Verifies the results of the delete state operation by comparing the state before and after the delete operation.
        Parameters:
            - config (dict): Configuration dictionary containing site and policy details.
        Returns:
            self: The instance of the class, allowing for method chaining.
        Description:
            This method performs verification of the delete operation by comparing the state before and after the operation.
            It introduces a delay to allow the deletion to process and then retrieves the state. It checks if the extranet policy
            no longer exists and logs the result of the delete operation. It ensures that the delete operation was successful
            by verifying the absence of the extranet policy and logs appropriate messages based on the outcome.
        """
        pre_operation_state = self.have.copy()
        desired_state = self.want
        time.sleep(10)
        self.get_have(config)
        post_operation_state = self.have.copy()
        extranet_policy_name = config.get("extranet_policy_name")

        self.log("State before performing DELETE Extranet Policy operation: {0}".format(str(pre_operation_state)), "INFO")
        self.log("Desired State: {}".format(str(desired_state)), "INFO")
        self.log("State after performing DELETE Extranet Policy operation: {0}".format(str(post_operation_state)), "INFO")

        if not post_operation_state["extranet_policy_exists"]:
            self.log("Verified the success of DELETE Extranet Policy - '{0}' operation".format(extranet_policy_name), "INFO")
        else:
            self.log(
                "The DELETE Extranet Policy - '{0}' operation may not have been successful since "
                "the policy still exists in the Cisco Catalyst Center.".format(extranet_policy_name),
                "WARNING"
            )
        return self


def main():
    """ main entry point for module execution
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
                    'state': {'default': 'merged', 'choices': ['merged', 'deleted']}
                    }

    # Initialize the Ansible module with the provided argument specifications
    module = AnsibleModule(argument_spec=element_spec,
                           supports_check_mode=False)

    # Initialize the NetworkCompliance object with the module
    ccc_sda_extranet_policies = SDAExtranetPolicies(module)

    # Get the state parameter from the provided parameters
    state = ccc_sda_extranet_policies.params.get("state")

    # Check if the state is valid
    if state not in ccc_sda_extranet_policies.supported_states:
        ccc_sda_extranet_policies.status = "invalid"
        ccc_sda_extranet_policies.msg = "State {0} is invalid".format(state)
        ccc_sda_extranet_policies.check_return_status()

    # Validate the input parameters and check the return status
    ccc_sda_extranet_policies.validate_input().check_return_status()

    # Get the config_verify parameter from the provided parameters
    config_verify = ccc_sda_extranet_policies.params.get("config_verify")

    # Iterate over the validated configuration parameters
    for config in ccc_sda_extranet_policies.validated_config:
        ccc_sda_extranet_policies.reset_values()
        ccc_sda_extranet_policies.get_have(config).check_return_status()
        ccc_sda_extranet_policies.get_want(config, state).check_return_status()
        ccc_sda_extranet_policies.get_diff_state_apply[state]().check_return_status()
        if config_verify:
            ccc_sda_extranet_policies.verify_diff_state_apply[state](config).check_return_status()

    module.exit_json(**ccc_sda_extranet_policies.result)


if __name__ == '__main__':
    main()
