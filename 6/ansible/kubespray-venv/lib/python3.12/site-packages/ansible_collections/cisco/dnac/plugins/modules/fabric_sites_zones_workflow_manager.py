#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2022, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ("Abhishek Maheshwari, Madhan Sankaranarayanan")

DOCUMENTATION = r"""
---
module: fabric_sites_zones_workflow_manager
short_description: Manage fabric site(s)/zone(s) and update the authentication profile template in Cisco Catalyst Center.
description:
- Creating fabric site(s) for the SDA operation in Cisco Catalyst Center.
- Updating fabric site(s) for the SDA operation in Cisco Catalyst Center.
- Creating fabric zone(s) for the SDA operation in Cisco Catalyst Center.
- Updating fabric zone(s) for the SDA operation in Cisco Catalyst Center.
- Deletes fabric site(s) from Cisco Catalyst Center.
- Deletes fabric zone(s) from Cisco Catalyst Center.
- Configure the authentication profile template for fabric site/zone in Cisco Catalyst Center.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author: Abhishek Maheshwari (@abmahesh)
        Madhan Sankaranarayanan (@madhansansel)
options:
  config_verify:
    description: Set to True to verify the Cisco Catalyst Center configuration after applying the playbook configuration.
    type: bool
    default: False
  state:
    description: The desired state of Cisco Catalyst Center after the module execution.
    type: str
    choices: [ merged, deleted ]
    default: merged
  config:
    description: A list containing detailed configurations for creating, updating, or deleting fabric sites or zones
        in a Software-Defined Access (SDA) environment. It also includes specifications for updating the authentication
        profile template for these sites. Each element in the list represents a specific operation to be performed on
        the SDA infrastructure, such as the addition, modification, or removal of fabric sites/zones, and modifications
        to authentication profiles.
    type: list
    elements: dict
    required: True
    suboptions:
      fabric_sites:
        description: A dictionary containing detailed configurations for managing REST Endpoints that will receive Audit log
            and Events from the Cisco Catalyst Center Platform. This dictionary is essential for specifying attributes and
            parameters required for the lifecycle management of fabric sites, zones, and associated authentication profiles.
        type: dict
        suboptions:
          site_name:
            description: This name uniquely identifies the site for operations such as creating, updating, or deleting fabric
                sites or zones, as well as for updating the authentication profile template. This parameter is mandatory for
                any fabric site/zone management operation.
            type: str
            required: True
          site_type:
            description: Specifies the type of site to be managed within the SDA environment. The acceptable values are 'fabric_site'
                and 'fabric_zone'. The default value is 'fabric_site', indicating the configuration of a broader network area, whereas
                'fabric_zone' typically refers to a more specific segment within the site.
            type: str
            required: True
          authentication_profile:
            description: The authentication profile applied to the specified fabric. This profile determines the security posture and
                controls for network access within the site. Possible values include 'Closed Authentication', 'Low Impact',
                'No Authentication', and 'Open Authentication'. This setting is critical when creating or updating a fabric site or
                updating the authentication profile template.
            type: str
          is_pub_sub_enabled:
            description: A boolean flag that indicates whether the pub/sub mechanism is enabled for control nodes in the fabric site.
                This feature is relevant only when creating or updating fabric sites, not fabric zones. When set to True,
                pub/sub facilitates more efficient communication and control within the site. The default is True for fabric sites,
                and this setting is not applicable for fabric zones.
            type: bool
          update_authentication_profile:
            description: A dictionary containing the specific details required to update the authentication profile template associated
                with the fabric site. This includes advanced settings that fine-tune the authentication process and security controls
                within the site.
            type: dict
            suboptions:
              authentication_order:
                description: Specifies the primary method of authentication for the site. The available methods are 'dot1x' (IEEE 802.1X)
                    and 'mac' (MAC-based authentication). This setting determines the order in which authentication mechanisms are attempted.
                type: str
              dot1x_fallback_timeout:
                description: The timeout duration, in seconds, for falling back from 802.1X authentication. This value must be within the
                    range of 3 to 120 seconds. It defines the period a device waits before attempting an alternative authentication method
                    if 802.1X fails.
                type: int
              wake_on_lan:
                description: A boolean value indicating whether the Wake-on-LAN feature is enabled. Wake-on-LAN allows the network to
                    remotely wake up devices that are in a low-power state.
                type: bool
              number_of_hosts:
                description: Specifies the number of hosts allowed per port. The available options are 'Single' for one device per port or
                    'Unlimited' for multiple devices. This setting helps in controlling the network access and maintaining security.
                type: str
              enable_bpu_guard:
                description: A boolean setting that enables or disables BPDU Guard. BPDU Guard provides a security mechanism by disabling
                    a port when a BPDU (Bridge Protocol Data Unit) is received, protecting against potential network loops. This setting
                    defaults to true and is applicable only when the authentication profile is set to "Closed Authentication".
                type: bool


requirements:
- dnacentersdk >= 2.9.2
- python >= 3.9

notes:
  - To ensure the module operates correctly for scaled sets, which involve creating or updating fabric sites/zones and handling
    the updation of authentication profile template, please provide valid input in the playbook. If any failure is encountered,
    the module will and halt execution without proceeding to further operations.
  - When deleting fabric sites, make sure to provide the input to remove the fabric zones associated with them in the
    playbook. Fabric sites cannot be deleted until all underlying fabric zones have been removed.
  - SDK Method used are
    ccc_fabric_sites.FabricSitesZones.get_site
    ccc_fabric_sites.FabricSitesZones.get_fabric_sites
    ccc_fabric_sites.FabricSitesZones.get_fabric_zones
    ccc_fabric_sites.FabricSitesZones.add_fabric_site
    ccc_fabric_sites.FabricSitesZones.update_fabric_site
    ccc_fabric_sites.FabricSitesZones.add_fabric_zone
    ccc_fabric_sites.FabricSitesZones.update_fabric_zone
    ccc_fabric_sites.FabricSitesZones.get_authentication_profiles
    ccc_fabric_sites.FabricSitesZones.update_authentication_profile
    ccc_fabric_sites.FabricSitesZones.delete_fabric_site_by_id
    ccc_fabric_sites.FabricSitesZones.delete_fabric_zone_by_id

"""

EXAMPLES = r"""
- name: Create a fabric site for SDA with the specified name.
  cisco.dnac.fabric_sites_zones_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: merged
    config:
      - fabric sites:
          site_name: "Global/Test_SDA/Bld1"
          authentication_profile: "Closed Authentication"
          is_pub_sub_enabled: False

- name: Update a fabric site for SDA with the specified name.
  cisco.dnac.fabric_sites_zones_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: merged
    config:
      - fabric sites:
          site_name: "Global/Test_SDA/Bld1"
          authentication_profile: "Open Authentication"

- name: Update a fabric zone for SDA with the specified name.
  cisco.dnac.fabric_sites_zones_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: merged
    config:
      - fabric sites:
          site_name: "Global/Test_SDA/Bld1/Floor1"
          site_type: "fabric_zone"
          authentication_profile: "Closed Authentication"

- name: Update fabric zone for sda with given name.
  cisco.dnac.fabric_sites_zones_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: merged
    config:
      - fabric sites:
          site_name: "Global/Test_SDA/Bld1/Floor1"
          site_type: "fabric_zone"
          authentication_profile: "Open Authentication"

- name: Update/customise authentication profile template for fabric site/zone.
  cisco.dnac.fabric_sites_zones_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: merged
    config:
      - fabric_sites:
          site_name: "Global/Test_SDA/Bld1"
          site_type: "fabric_zone"
          authentication_profile: "Open Authentication"
          is_pub_sub_enabled: False
          update_authentication_profile:
            authentication_order: "dot1x"
            dot1x_fallback_timeout: 28
            wake_on_lan: False
            number_of_hosts: "Single"

- name: Deleting/removing fabric site from sda from Cisco Catalyst Center
  cisco.dnac.fabric_sites_zones_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: deleted
    config:
      - fabric_sites:
          site_name: "Global/Test_SDA/Bld1"

- name: Deleting/removing fabric zone from sda from Cisco Catalyst Center
  cisco.dnac.fabric_sites_zones_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: deleted
    config:
      - fabric_sites:
          site_name: "Global/Test_SDA/Bld1/Floor1"
          site_type: "fabric_zone"

"""

RETURN = r"""

dnac_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
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

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts,
)
import time


class FabricSitesZones(DnacBase):
    """Class containing member attributes for fabric sites and zones workflow manager module"""

    def __init__(self, module):
        super().__init__(module)
        self.supported_states = ["merged", "deleted"]
        self.create_site, self.update_site, self.no_update_site = [], [], []
        self.create_zone, self.update_zone, self.no_update_zone = [], [], []
        self.update_auth_profile, self.no_update_profile = [], []
        self.delete_site, self.delete_zone, self.absent_site, self.absent_zone = [], [], [], []

    def validate_input(self):
        """
        Validate the fields provided in the playbook.
        Checks the configuration provided in the playbook against a predefined specification
        to ensure it adheres to the expected structure and data types.
        Parameters:
            self: The instance of the class containing the 'config' attribute to be validated.
        Returns:
            The method returns an instance of the class with updated attributes:
                - self.msg: A message describing the validation result.
                - self.status: The status of the validation (either 'success' or 'failed').
                - self.validated_config: If successful, a validated version of the 'config' parameter.
        Example:
            To use this method, create an instance of the class and call 'validate_input' on it.
            If the validation succeeds, 'self.status' will be 'success' and 'self.validated_config'
            will contain the validated configuration. If it fails, 'self.status' will be 'failed', and
            'self.msg' will describe the validation issues.
        """

        temp_spec = {
            'fabric_sites': {
                'type': 'list',
                'elements': 'dict',
                'site_name': {'type': 'str'},
                'site_type': {'type': 'str', 'default': 'fabric_site'},
                'authentication_profile': {'type': 'str'},
                'is_pub_sub_enabled': {'type': 'bool', 'default': False},
                'update_authentication_profile': {
                    'elements': 'dict',
                    'site_name_hierarchy': {'type': 'str'},
                    'authentication_profile': {'type': 'str'},
                    'authentication_order': {'type': 'str'},
                    'dot1x_fallback_timeout': {'type': 'int'},
                    'wake_on_lan': {'type': 'bool'},
                    'number_of_hosts': {'type': 'str'},
                    'enable_bpu_guard': {'type': 'bool'}
                }
            },
        }

        if not self.config:
            self.status = "failed"
            self.msg = "The playbook configuration is empty or missing."
            self.log(self.msg, "ERROR")
            return self

        # Validate device params
        valid_temp, invalid_params = validate_list_of_dicts(
            self.config, temp_spec
        )

        if invalid_params:
            self.msg = "The playbook contains invalid parameters: {0}".format(invalid_params)
            self.log(self.msg, "ERROR")
            self.status = "failed"
            return self

        self.validated_config = valid_temp
        self.msg = "Successfully validated playbook configuration parameters using 'validate_input': {0}".format(str(valid_temp))
        self.log(self.msg, "INFO")
        self.status = "success"

        return self

    def get_site_id(self, site_name):
        """
        Retrieves the site ID for a given site name from the Cisco Catalyst Center.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            site_name (str): The complete name of site for which the site ID need to be retrieved.
        Returns:
            str: A site ID corresponding to the provided site name.
        Description:
            This function invokes an API to fetch the details of given site from the Cisco Catalyst Center. If the
            site is found, its site ID is extracted.
            The function logs messages for successful API responses, missing site, and any errors
            encountered during the process. The final site ID is returned.
        """

        try:
            response = self.dnac._exec(
                family="sites",
                function='get_site',
                op_modifies=True,
                params={"name": site_name},
            )
            self.log("Received API response from 'get_site': {0}".format(str(response)), "DEBUG")
            response = response.get('response')

            if not response or not response[0].get("id"):
                self.status = "failed"
                self.msg = "No site with the name '{0}' found in Cisco Catalyst Center.".format(site_name)
                self.log(self.msg, "ERROR")
                self.check_return_status()
            site_id = response[0].get("id")

        except Exception as e:
            self.status = "failed"
            self.msg = """Error while getting the details of Site with given name '{0}' present in
                    Cisco Catalyst Center: {1}""".format(site_name, str(e))
            self.log(self.msg, "ERROR")
            self.check_return_status()

        return site_id

    def get_fabric_site_detail(self, site_name, site_id):
        """
        Retrieves the detailed information of a fabric site from the Cisco Catalyst Center.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            site_name (str): The complete name of the site for which the details need to be retrieved.
            site_id (str): The unique identifier of the site in the Cisco Catalyst Center.
        Returns:
            dict or None: A dictionary containing the details of the fabric site if found.
                        Returns None if the site is not a fabric site or if an error occurs.
        Description:
            This function fetches the fabric site details from Cisco Catalyst Center using the provided site ID.
            It logs the API response and returns the site details if the site is a fabric site. If the site is not
            found or is not a fabric site, it returns None. In case of an error, it logs the issue, sets the status
            to "failed", and handles the failure.
        """

        try:
            response = self.dnac._exec(
                family="sda",
                function='get_fabric_sites',
                op_modifies=True,
                params={"site_id": site_id},
            )
            response = response.get("response")
            self.log("Received API response from 'get_fabric_sites' for the site '{0}': {1}".format(site_name, str(response)), "DEBUG")

            if not response:
                self.log("Given site '{0}' is not a fabric site in Cisco Catalyst Center.".format(site_name), "INFO")
                return None

            return response[0]
        except Exception as e:
            self.status = "failed"
            self.msg = """Error while getting the details of Site with given name '{0}' present in
                    Cisco Catalyst Center: {1}""".format(site_name, str(e))
            self.log(self.msg, "ERROR")
            self.check_return_status()

        return None

    def get_fabric_zone_detail(self, site_name, site_id):
        """
        Retrieves the detailed information of a fabric zone from the Cisco Catalyst Center.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            site_name (str): The complete name of the site for which the fabric zone details need to be retrieved.
            site_id (str): The unique identifier of the site in the Cisco Catalyst Center.
        Returns:
            dict or None: A dictionary containing the details of the fabric zone if found,
                        or None if the site is not a fabric zone or an error occurs.
        Description:
            This function fetches the fabric zone details from Cisco Catalyst Center using the provided site ID.
            It logs the API response and returns the details if the site is a fabric zone. If the site is not
            recognized as a fabric zone, it returns None. In case of an error, it logs the issue, sets the status
            to "failed", and handles the failure appropriately.
        """

        try:
            response = self.dnac._exec(
                family="sda",
                function='get_fabric_zones',
                op_modifies=True,
                params={"site_id": site_id},
            )
            response = response.get("response")
            self.log("Received API response from 'get_fabric_zones' for the site '{0}': {1}".format(site_name, str(response)), "DEBUG")

            if not response:
                self.log("Given site '{0}' is not a fabric zone in Cisco Catalyst Center.".format(site_name), "INFO")
                return None

            return response[0]

        except Exception as e:
            self.status = "failed"
            self.msg = """Error while getting the details of fabric zone '{0}' present in
                    Cisco Catalyst Center: {1}""".format(site_name, str(e))
            self.log(self.msg, "ERROR")
            self.check_return_status()

        return None

    def get_have(self, config):
        """
        Retrieves the current state of fabric sites and zones from the Cisco Catalyst Center based on the given configuration.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (dict): A configuration dictionary containing details about the fabric sites and zones.
                        The key "fabric_sites" should contain a list of dictionaries.
        Returns:
            self (object): The instance of the class with the updated `have` attribute containing the current state
                of fabric sites and zones.
        Description:
            This function processes the provided configuration to determine the current state of fabric sites
            and zones in the Cisco Catalyst Center. It iterates over the "fabric_sites" list in the configuration,
            extracting the site name and type. For each site, it retrieves the corresponding site or zone ID
            and details using the `get_site_id`, `get_fabric_site_detail`, and `get_fabric_zone_detail` methods.
            The `have` attribute of the instance is updated with this dictionary, representing the current state
            of the system. The function logs the final state and returns the instance for further use.
        """

        have = {
            "fabric_sites_ids": [],
            "fabric_zone_ids": []
        }
        fabric_sites = config.get("fabric_sites", [])

        for site in fabric_sites:
            site_name = site.get("site_name")
            site_type = site.get("site_type", "fabric_site")
            site_id = self.get_site_id(site_name)

            if site_type == "fabric_site":
                site_detail = self.get_fabric_site_detail(site_name, site_id)
                if site_detail:
                    self.log("Site detail for fabric site {0} collected successfully.".format(site_name), "DEBUG")
                    have["fabric_sites_ids"].append(site_detail.get("siteId"))
            else:
                zone_detail = self.get_fabric_zone_detail(site_name, site_id)
                if zone_detail:
                    self.log("Site detail for fabric zone {0} collected successfully.".format(site_name), "DEBUG")
                    have["fabric_zone_ids"].append(zone_detail.get("siteId"))

        self.have = have
        self.log("Current State (have): {0}".format(str(have)), "INFO")

        return self

    def get_want(self, config):
        """
        Collects and validates the desired state configuration for fabric sites and zones from the given playbook configuration.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (dict): A dictionary containing the configuration for the desired state of fabric sites and zones.
                        It should include a key "fabric_sites" with a list of dictionaries.
        Returns:
            self (object): The instance of the class with the updated `want` attribute containing the validated desired state
                of fabric sites and zones and updating authentication profile template.
        Description:
            This function processes the provided playbook configuration to determine the desired state of fabric sites
            and zones in the Cisco Catalyst Center.
            The validated site information is stored in the `want` dictionary under the key "fabric_sites".
            The `want` attribute of the instance is updated with this dictionary, representing the desired state
            of the system. The function returns the instance for further processing or method chaining.
        """

        want = {}
        fabric_sites = config.get("fabric_sites")

        if not fabric_sites:
            self.status = "failed"
            self.msg = (
                "No input provided in the playbook for fabric site/zone operation or updating the "
                "authentication profile template in Cisco Catalysyt Center."
            )
            self.log(self.msg, "ERROR")
            self.result["response"] = self.msg
            return self

        if fabric_sites:
            fabric_site_info = []

            for site in fabric_sites:
                site_name = site.get("site_name")
                site_type = site.get("site_type", "fabric_site")

                if not site_name:
                    self.status = "failed"
                    self.msg = (
                        "Required parameter 'site_name' is missing. It must be provided in the playbook for fabric site/zone "
                        "operations in Cisco Catalyst Center."
                    )
                    self.log(self.msg, "ERROR")
                    self.result["response"] = self.msg
                    return self

                if site_type not in ["fabric_site", "fabric_zone"]:
                    self.status = "failed"
                    self.msg = (
                        "Invalid site_type '{0}' provided. Please use 'fabric_site' or 'fabric_zone' for fabric site/zone operations"
                        " in Cisco Catalyst Center."
                    ).format(site_type)
                    self.log(self.msg, "ERROR")
                    return self

                fabric_site_info.append(site)

            want["fabric_sites"] = fabric_site_info

        self.want = want
        self.msg = "Successfully collected all parameters from the playbook for creating/updating the fabric sites/zones."
        self.status = "success"
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

        return self

    def create_fabric_site(self, site):
        """
        Creates a fabric site in the Cisco Catalyst Center using the provided site configuration.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            site (dict): A dictionary containing the details of the fabric site to be created.
        Returns:
            self (object): The instance of the class with updated status and result attributes reflecting the outcome
                of the fabric site creation operation.
        Description:
            This function creates a fabric site in the Cisco Catalyst Center based on the configuration provided
            in the `site` dictionary.
            The function constructs the payload for the API request, which includes the site ID, authentication profile,
            and an optional flag for PubSub enablement. The payload is then sent to the `add_fabric_site` API endpoint.
            After the API call, the function monitors the status of the task using the `get_task_details` method.
            If the task encounters an error, the function logs the error and sets the status to "failed". If the task completes
            successfully and contains the necessary data, the status is set to "success", and the site is marked as created.
        """

        try:
            fabric_site_payload = []
            site_name = site.get("site_name")
            auth_profile = site.get("authentication_profile")
            if not auth_profile:
                self.status = "failed"
                self.msg = (
                    "Required parameter 'authentication_profile'is missing needed for creation of fabric sites in Cisco Catalyst Center. "
                    "Please provide one of the following authentication_profile ['Closed Authentication', 'Low Impact'"
                    ", 'No Authentication', 'Open Authentication'] in the playbook."
                )
                self.log(self.msg, "ERROR")
                self.result["response"] = self.msg
                return self

            site_payload = {
                "siteId": self.get_site_id(site_name),
                "authenticationProfileName": site.get("authentication_profile"),
                "isPubSubEnabled": site.get("is_pub_sub_enabled", False)
            }
            fabric_site_payload.append(site_payload)
            self.log("Requested payload for creating fabric site '{0}' is:  {1}".format(site_name, str(site_payload)), "INFO")

            response = self.dnac._exec(
                family="sda",
                function='add_fabric_site',
                op_modifies=True,
                params={'payload': fabric_site_payload}
            )
            self.log("Received API response from 'add_fabric_site' for the site {0}: {1}".format(site_name, str(response)), "DEBUG")
            response = response.get("response")

            if not response:
                self.status = "failed"
                self.msg = "No response received from 'add_fabric_site' API, task ID not retrieved."
                self.log(self.msg, "ERROR")
                return self

            task_id = response.get("taskId")

            while True:
                task_details = self.get_task_details(task_id)

                if task_details.get("isError"):
                    self.status = "failed"
                    failure_reason = task_details.get("failureReason")
                    if failure_reason:
                        self.msg = "Failed to create the Fabric site '{0}' due to {1}.".format(site_name, failure_reason)
                    else:
                        self.msg = "Failed to create the Fabric site '{0}'.".format(site_name)
                    self.log(self.msg, "ERROR")
                    self.result['response'] = self.msg
                    break
                elif task_details.get("endTime") and "workflow_id" in task_details.get("data"):
                    self.status = "success"
                    self.create_site.append(site_name)
                    self.log("Fabric site '{0}' created successfully in the Cisco Catalyst Center".format(site_name), "INFO")
                    break

                time.sleep(1)

        except Exception as e:
            self.status = "failed"
            self.msg = "An exception occured while creating the fabric site '{0}' in Cisco Catalyst Center: {1}".format(site_name, str(e))
            self.log(self.msg, "ERROR")

        return self

    def fabric_site_needs_update(self, site, site_in_ccc):
        """
        Determines if a fabric site in Cisco Catalyst Center needs to be updated based on the provided configuration.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            site (dict): A dictionary containing the desired configuration of the fabric site.
            site_in_ccc (dict): A dictionary containing the current configuration of the fabric site as
                                present in the Cisco Catalyst Center.
        Returns:
            bool: True if the fabric site requires an update, False otherwise.
        Description:
            This function compares the desired configuration (`site`) of a fabric site with its current
            configuration (`site_in_ccc`) in the Cisco Catalyst Center.
            The function returns True, indicating that the fabric site needs to be updated. Otherwise, it returns False,
            indicating no update is needed.
        """

        auth_profile = site.get("authentication_profile")
        if auth_profile and auth_profile != site_in_ccc.get("authenticationProfileName"):
            return True

        is_pub_sub_enabled = site.get("is_pub_sub_enabled")
        if is_pub_sub_enabled is not None and is_pub_sub_enabled != site_in_ccc.get("isPubSubEnabled"):
            return True

        return False

    def update_fabric_site(self, site, site_in_ccc):
        """
        Updates a fabric site in the Cisco Catalyst Center based on the provided configuration and current state.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            site (dict): A dictionary containing the desired configuration for the fabric site.
            site_in_ccc (dict): A dictionary containing the current configuration of the fabric site
                                in the Cisco Catalyst Center.
        Returns:
            self (object): The instance of the class with updated status and result attributes reflecting the outcome
                of the fabric site update operation.
        Description:
            This method updates a fabric site in the Cisco Catalyst Center. The constructed payload includes the site ID,
            authentication profile name, and PubSub enablement status and payload is sent to the `update_fabric_site`
            API endpoint.
            After initiating the update, the method tracks the status of the update task using `get_task_details`.
            It checks for task errors or successful completion, updating the status and logging messages accordingly.
            If the task fails, an appropriate error message is logged, and the status is set to "failed".
        """

        try:
            update_site_params = []
            site_name = site.get("site_name")

            if site.get("is_pub_sub_enabled") is None:
                pub_sub_enable = site_in_ccc.get("isPubSubEnabled")
            else:
                pub_sub_enable = site.get("is_pub_sub_enabled")

            if not site.get("authentication_profile"):
                auth_profile = site_in_ccc.get("authenticationProfileName")
            else:
                auth_profile = site.get("authentication_profile")

            site_payload = {
                "id": site_in_ccc.get("id"),
                "siteId": site_in_ccc.get("siteId"),
                "authenticationProfileName": auth_profile,
                "isPubSubEnabled": pub_sub_enable
            }
            update_site_params.append(site_payload)
            self.log("Requested payload for updating fabric site '{0}' is:  {1}".format(site_name, str(site_payload)), "INFO")

            response = self.dnac._exec(
                family="sda",
                function='update_fabric_site',
                op_modifies=True,
                params={'payload': update_site_params}
            )
            self.log("Received API response from 'update_fabric_site' for the site {0}: {1}".format(site_name, str(response)), "DEBUG")
            response = response.get("response")

            if not response:
                self.status = "failed"
                self.msg = "Unable to fetch the task Id for the updation of fabric site as the 'update_fabric_site' response is empty."
                self.log(self.msg, "ERROR")
                return self

            task_id = response.get("taskId")

            while True:
                task_details = self.get_task_details(task_id)
                if task_details.get("isError"):
                    self.status = "failed"
                    failure_reason = task_details.get("failureReason")
                    if failure_reason:
                        self.msg = "Unable to update the Fabric site '{0}' because of {1}.".format(site_name, failure_reason)
                    else:
                        self.msg = "Unable to update the Fabric site '{0}'.".format(site_name)
                    self.log(self.msg, "ERROR")
                    self.result['response'] = self.msg
                    break
                elif task_details.get("endTime") and "workflow_id" in task_details.get("data"):
                    self.status = "success"
                    self.update_site.append(site_name)
                    self.log("Fabric site '{0}' updated successfully in the Cisco Catalyst Center".format(site_name), "INFO")
                    break
                time.sleep(1)
        except Exception as e:
            self.status = "failed"
            self.msg = "An exception occured while updating the fabric site '{0}' in Cisco Catalyst Center: {1}".format(site_name, str(e))
            self.log(self.msg, "ERROR")

        return self

    def create_fabric_zone(self, zone):
        """
        Creates a fabric zone in the Cisco Catalyst Center based on the provided configuration.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            zone (dict): A dictionary containing the desired configuration for the fabric zone.
        Returns:
            self (object): The instance of the class with updated status and result attributes reflecting the outcome
                of the fabric zone creation operation.
        Description:
            This method creates a fabric zone in the Cisco Catalyst Center and  sends the payload to the add_fabric_zone
            API endpoint. The method logs the requested payload and the API response.
            After initiating the creation, the method monitors the task's status using `get_task_details`.
            It checks for task errors or successful completion. If the task fails, an appropriate error message
            is logged, and the status is set to "failed". If the task succeeds, the status is set to "success",
            and the site name is added to the list of successfully created zones.
            The function returns the class instance (`self`) with the updated attributes.
        """

        try:
            fabric_zone_payload = []
            site_name = zone.get("site_name")

            zone_payload = {
                "siteId": self.get_site_id(site_name),
                "authenticationProfileName": zone.get("authentication_profile"),
            }
            fabric_zone_payload.append(zone_payload)
            self.log("Requested payload for creating fabric zone '{0}' is:  {1}".format(site_name, zone_payload), "INFO")

            response = self.dnac._exec(
                family="sda",
                function='add_fabric_zone',
                op_modifies=True,
                params={'payload': fabric_zone_payload}
            )
            self.log("Received API response from 'add_fabric_zone' for the site {0}: {1}".format(site_name, str(response)), "DEBUG")
            response = response.get("response")

            if not response:
                self.status = "failed"
                self.msg = "Unable to fetch the task Id for the creation of fabric zone as the 'add_fabric_zone' response is empty."
                self.log(self.msg, "ERROR")
                return self

            task_id = response.get("taskId")

            while True:
                task_details = self.get_task_details(task_id)

                if task_details.get("isError"):
                    self.status = "failed"
                    failure_reason = task_details.get("failureReason")
                    if failure_reason:
                        self.msg = "Unable to create the Fabric zone '{0}' because of {1}.".format(site_name, failure_reason)
                    else:
                        self.msg = "Unable to create the Fabric zone '{0}'.".format(site_name)
                    self.log(self.msg, "ERROR")
                    self.result['response'] = self.msg
                    break
                elif task_details.get("endTime") and "workflow_id" in task_details.get("data"):
                    self.status = "success"
                    self.create_zone.append(site_name)
                    self.log("Fabric zone '{0}' created successfully in the Cisco Catalyst Center.".format(site_name), "INFO")
                    break
                time.sleep(1)
        except Exception as e:
            self.status = "failed"
            self.msg = "An exception occured while creating the fabric zone '{0}' in Cisco Catalyst Center: {1}".format(site_name, str(e))
            self.log(self.msg, "ERROR")

        return self

    def update_fabric_zone(self, zone, zone_in_ccc):
        """
        Updates an existing fabric zone in the Cisco Catalyst Center with the provided configuration.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            zone (dict): A dictionary containing the desired updates for the fabric zone.
            zone_in_ccc (dict): A dictionary containing the current configuration of the fabric zone
                                in the Cisco Catalyst Center.
        Returns:
            self (object): The instance of the class with updated status and result attributes reflecting the outcome
                of the fabric zone update operation.
        Description:
            This method updates the configuration of a fabric zone in the Cisco Catalyst Center.
            The constructed payload is sent to the `update_fabric_zone` API endpoint. The method logs the
            requested payload and the API response.
            After initiating the update, the method monitors the task's status using `get_task_details`. It checks
            for task errors or successful completion.
            The function returns the class instance (`self`) with the updated attributes.
        """

        try:
            update_zone_params = []
            site_name = zone.get("site_name")

            zone_payload = {
                "id": zone_in_ccc.get("id"),
                "siteId": zone_in_ccc.get("siteId"),
                "authenticationProfileName": zone.get("authentication_profile") or zone_in_ccc.get("authenticationProfileName")
            }
            update_zone_params.append(zone_payload)
            self.log("Requested payload for updating fabric zone '{0}' is:  {1}".format(site_name, zone_payload), "INFO")

            response = self.dnac._exec(
                family="sda",
                function='update_fabric_zone',
                op_modifies=True,
                params={'payload': update_zone_params}
            )
            self.log("Received API response from 'update_fabric_zone' for the site {0}: {1}".format(site_name, str(response)), "DEBUG")
            response = response.get("response")

            if not response:
                self.status = "failed"
                self.msg = "Unable to fetch the task Id for the updation of fabric zone as the 'update_fabric_zone' response is empty."
                self.log(self.msg, "ERROR")
                return self

            task_id = response.get("taskId")

            while True:
                task_details = self.get_task_details(task_id)

                if task_details.get("isError"):
                    self.status = "failed"
                    failure_reason = task_details.get("failureReason")
                    if failure_reason:
                        self.msg = "Unable to update the Fabric zone '{0}' because of {1}.".format(site_name, failure_reason)
                    else:
                        self.msg = "Unable to update the Fabric zone '{0}'.".format(site_name)
                    self.log(self.msg, "ERROR")
                    self.result['response'] = self.msg
                    break
                elif task_details.get("endTime") and "workflow_id" in task_details.get("data"):
                    self.status = "success"
                    self.log("Fabric zone '{0}' updated successfully in the Cisco Catalyst Center".format(site_name), "INFO")
                    self.update_zone.append(site_name)
                    break
                time.sleep(1)
        except Exception as e:
            self.status = "failed"
            self.msg = "An exception occured while updating the fabric zone '{0}' in Cisco Catalyst Center: {1}".format(site_name, str(e))
            self.log(self.msg, "ERROR")

        return self

    def validate_auth_profile_parameters(self, auth_profile_dict):
        """
        Validates the parameters provided for updating the authentication profile template.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            auth_profile_dict (dict): A dictionary containing the parameters for the authentication profile.
        Returns:
            self (objetc): The instance of the class with updated status and result attributes if invalid parameters are found.
        Description:
            This method checks the validity of the provided parameters for the authentication profile template. It validates
            the "authentication_order" to ensure it is either "dot1x" or "mac". For "dot1x_fallback_timeout", it ensures the
            value is an integer within the range of 3 to 120. The "number_of_hosts" must be either "Single" or "Unlimited".
            If any invalid parameters are found, they are added to the `invalid_auth_profile_list`. Corresponding error messages
            are logged, and the status is set to "failed". The method also logs warnings for any exceptions encountered during
            the validation process.
        """

        invalid_auth_profile_list = []
        auth_order = auth_profile_dict.get("authentication_order")
        if auth_order and auth_order not in ["dot1x", "mac"]:
            invalid_auth_profile_list.append("authentication_order")
            msg = (
                "Invalid authentication_order '{0}'given in the playbook for the updation of authentication profile template. "
                "Please provide one of the following authentication_order ['dot1x', 'mac'] in the playbook."
            ).format(auth_order)
            self.log(msg, "ERROR")

        fall_timeout = auth_profile_dict.get("dot1x_fallback_timeout")
        if fall_timeout:
            try:
                timeout = int(fall_timeout)
                if timeout not in range(3, 121):
                    invalid_auth_profile_list.append("dot1x_fallback_timeout")
                    msg = (
                        "Invalid 'dot1x_fallback_timeout' '{0}' given in the playbook. "
                        "Please provide a value in the range [3, 120]."
                    ).format(timeout)
                    self.log(msg, "ERROR")
            except Exception as e:
                invalid_auth_profile_list.append("dot1x_fallback_timeout")
                msg = (
                    "Invalid 'dot1x_fallback_timeout' string '{0}' given in the playbook, unable to convert it into the integer. "
                    "Please provide a value in the range [3, 120]."
                ).format(fall_timeout)
                self.log(msg, "WARNING")

        number_of_hosts = auth_profile_dict.get("number_of_hosts")
        if number_of_hosts and number_of_hosts.title() not in ["Single", "Unlimited"]:
            invalid_auth_profile_list.append("number_of_hosts")
            msg = (
                "Invalid number_of_hosts '{0}'given in the playbook for the updation of authentication profile template. "
                "Please provide one of the following: ['Single', 'Unlimited']."
            ).format(auth_order)
            self.log(msg, "ERROR")

        if invalid_auth_profile_list:
            self.status = "failed"
            self.msg = (
                "Invalid parameters found: {0}. "
                "Unable to update the authentication profile template."
            ).format(invalid_auth_profile_list)
            self.log(self.msg, "ERROR")
            self.result["response"] = self.msg

        return self

    def get_authentication_profile(self, fabric_id, auth_profile, site_name):
        """
        Retrieves the details of an authentication profile for a given fabric and site from the Cisco Catalyst Center.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            fabric_id (str): The ID of the fabric to which the authentication profile belongs.
            auth_profile (str): The name of the authentication profile to retrieve.
            site_name (str): The name of the site associated with the authentication profile.
        Returns:
            dict or None: A dictionary containing the details of the authentication profile if found, or None if no profile is associated
                        with the site or if an error occurs.
        Description:
            This method sends a request to the Cisco Catalyst Center to fetch the authentication profile details based on the provided
            `fabric_id` and `auth_profile` name. The `site_name` is used for logging purposes to provide context in the logs.
            If the response contains authentication profile details, these details are returned. If no profile is found or if an error
            occurs during the request, the method logs an appropriate message and returns `None`.
        """

        try:
            profile_details = None
            response = self.dnac._exec(
                family="sda",
                function='get_authentication_profiles',
                op_modifies=True,
                params={
                    "fabric_id": fabric_id,
                    "authentication_profile_name": auth_profile
                }
            )
            response = response.get("response")
            self.log("Received API response from 'get_authentication_profiles' for the site '{0}': {1}".format(site_name, str(response)), "DEBUG")

            if not response:
                self.log("No Authentication profile asssociated to this site '{0}' in Cisco Catalyst Center.".format(site_name), "INFO")
                return profile_details

            profile_details = response[0]
            return profile_details
        except Exception as e:
            self.status = "failed"
            self.msg = (
                "Error while getting the details of authentication profiles for the site '{0}' present in "
                "Cisco Catalyst Center: {1}"
            ).format(site_name, str(e))
            self.log(self.msg, "ERROR")
            self.check_return_status()

        return None

    def auth_profile_needs_update(self, auth_profile_dict, auth_profile_in_ccc):
        """
        Determines if the authentication profile requires an update by comparing it with the existing profile in Cisco Catalyst Center.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            auth_profile_dict (dict): A dictionary containing the desired authentication profile settings to compare.
            auth_profile_in_ccc (dict): A dictionary containing the current authentication profile settings from Cisco Catalyst Center.
        Returns:
            bool: Returns `True` if any of the settings in `auth_profile_dict` differ from those in `auth_profile_in_ccc` and an update
                is needed. Returns `False` if the settings match and no update is required.
        Description:
            This method compares the provided authentication profile settings (`auth_profile_dict`) with the current settings retrieved from
            the Cisco Catalyst Center (`auth_profile_in_ccc`). It considers the possibility of an additional setting "enable_bpu_guard" if
            the current profile is "Closed Authentication".
            It iterates through a mapping of profile settings and checks if any of the settings require an update. If any discrepancies are
            found, the method returns `True`. If all settings match, it returns `False`.
        """

        profile_key_mapping = {
            "authentication_order": "authenticationOrder",
            "dot1x_fallback_timeout": "dot1xToMabFallbackTimeout",
            "wake_on_lan": "wakeOnLan",
            "number_of_hosts": "numberOfHosts"
        }
        if auth_profile_in_ccc.get("authenticationProfileName") == "Closed Authentication":
            profile_key_mapping["enable_bpu_guard"] = "isBpduGuardEnabled"

        for key, ccc_key in profile_key_mapping.items():
            desired_value = auth_profile_dict.get(key)

            if desired_value is None:
                continue

            current_value = auth_profile_in_ccc.get(ccc_key)

            if key == "dot1x_fallback_timeout":
                desired_value = int(desired_value)
                current_value = int(current_value)

            if desired_value != current_value:
                return True

        return False

    def collect_authentication_params(self, auth_profile_dict, auth_profile_in_ccc):
        """
        Collects and prepares the updated authentication profile parameters based on the provided dictionary and the current profile in
        Cisco Catalyst Center.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            auth_profile_dict (dict): A dictionary containing the desired authentication profile settings.
            auth_profile_in_ccc (dict): A dictionary containing the current authentication profile settings from Cisco Catalyst Center.
        Returns:
            list: A list containing a single dictionary with the updated authentication profile parameters.
        Description:
            This method prepares the updated parameters for an authentication profile by combining desired settings from `auth_profile_dict` with
            the current settings from `auth_profile_in_ccc`.
            It creates a dictionary with the ID, fabric ID, profile name, and updated settings for authentication order, dot1x fallback timeout,
            number of hosts, and Wake-on-LAN. If the profile is "Closed Authentication," it also includes the BPDU guard setting.
            The method returns a list containing the updated parameters in a dictionary, which can be used for further processing or API requests.
        """

        updated_params = []
        profile_name = auth_profile_in_ccc.get("authenticationProfileName")
        authentications_params_dict = {
            "id": auth_profile_in_ccc.get("id"),
            "fabricId": auth_profile_in_ccc.get("fabricId"),
            "authenticationProfileName": profile_name,
            "authenticationOrder": auth_profile_dict.get("authentication_order") or auth_profile_in_ccc.get("authenticationOrder"),
            "dot1xToMabFallbackTimeout": int(auth_profile_dict.get("dot1x_fallback_timeout")) or auth_profile_in_ccc.get("dot1xToMabFallbackTimeout"),
            "numberOfHosts": auth_profile_dict.get("number_of_hosts") or auth_profile_in_ccc.get("numberOfHosts"),
        }

        if auth_profile_dict.get("wake_on_lan") is None:
            authentications_params_dict["wakeOnLan"] = auth_profile_in_ccc.get("wakeOnLan")
        else:
            authentications_params_dict["wakeOnLan"] = auth_profile_dict.get("wake_on_lan")

        if profile_name == "Closed Authentication":
            if auth_profile_dict.get("enable_bpu_guard") is None:
                auth_profile_dict["isBpduGuardEnabled"] = auth_profile_in_ccc.get("isBpduGuardEnabled", True)
            else:
                auth_profile_dict["isBpduGuardEnabled"] = auth_profile_dict.get("enable_bpu_guard")

        updated_params.append(authentications_params_dict)

        return updated_params

    def update_authentication_profile_template(self, profile_update_params, site_name):
        """
        Updates the authentication profile template for a specified site in Cisco Catalyst Center.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            profile_update_params (dict): A dictionary containing the parameters to update the authentication profile.
            site_name (str): The name of the site where the authentication profile is being updated.
        Returns:
            self (object): Returns the current instance of the class with updated status and message attributes.
        Description:
            This method sends a request to update the authentication profile template for the specified site using the
            provided parameters. It first logs the requested payload and sends it to the API for processing.
            It then monitors the task status by polling until the update is complete. If the update is successful,
            it logs a success message and appends the site name to the list of updated profiles. If an error occurs or
            the task fails, it logs an error message and updates the status to "failed".
        """

        try:
            self.log("Requested payload for updating authentication profile for site {0}: {1}".format(site_name, profile_update_params), "INFO")
            response = self.dnac._exec(
                family="sda",
                function='update_authentication_profile',
                op_modifies=True,
                params={'payload': profile_update_params}
            )
            self.log("Received API response from 'update_authentication_profile'for site {0}: {1}".format(site_name, str(response)), "DEBUG")
            response = response.get("response")

            if not response:
                self.status = "failed"
                self.msg = "Unable to fetch the task Id for the updation of authentication profile for site '{0}'.".format(site_name)
                self.log(self.msg, "ERROR")
                return self

            task_id = response.get("taskId")

            if not task_id:
                self.status = "failed"
                self.msg = "No task ID returned for the update request of the authentication profile for site '{0}'.".format(site_name)
                self.log(self.msg, "ERROR")
                self.result["response"] = self.msg
                return self

            while True:
                task_details = self.get_task_details(task_id)

                if task_details.get("isError"):
                    self.status = "failed"
                    failure_reason = task_details.get("failureReason")
                    if failure_reason:
                        self.msg = "Unable to update the authentication profile for site '{0}' because of {1}.".format(site_name, failure_reason)
                    else:
                        self.msg = "Unable to update the authentication profile for site '{0}'.".format(site_name)
                    self.log(self.msg, "ERROR")
                    self.result['response'] = self.msg
                    break

                if task_details.get("endTime") and "workflow_id" in task_details.get("data"):
                    self.status = "success"
                    self.update_auth_profile.append(site_name)
                    self.log("Authentication profile for the site '{0}' updated successfully in the Cisco Catalyst Center".format(site_name), "INFO")
                    break

                time.sleep(1)
        except Exception as e:
            self.status = "failed"
            self.msg = "An exception occured while updating the authentication profile for site '{0}' in Cisco Catalyst Center: {1}".format(site_name, str(e))
            self.log(self.msg, "ERROR")

        return self

    def delete_fabric_site_zone(self, fabric_id, site_name, site_type):
        """
        Deletes a fabric site or fabric zone from Cisco Catalyst Center.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            fabric_id (str): The ID of the fabric site or fabric zone to be deleted.
            site_name (str): The name of the fabric site or fabric zone to be deleted.
            site_type (str): The type of the entity to be deleted. Should be either "fabric_site" or "fabric_zone".
        Returns:
            self (object): Returns the current instance of the class with updated status and message attributes.
        Description:
            This method sends a request to delete a fabric site or fabric zone based on the provided `fabric_id` and `site_type`.
            It determines the appropriate API function to call based on the `site_type`, either "delete_fabric_site_by_id" or
            "delete_fabric_zone_by_id". It returns the class instance for further processing or chaining.
        """

        try:
            if site_type == "fabric_site":
                api_name = "delete_fabric_site_by_id"
                type_name = "fabric site"
            else:
                api_name = "delete_fabric_zone_by_id"
                type_name = "fabric zone"

            response = self.dnac._exec(
                family="sda",
                function=api_name,
                op_modifies=True,
                params={"id": fabric_id},
            )
            self.log("Received API response from '{0}' for the site {1}: {2}".format(api_name, site_name, str(response)), "DEBUG")
            response = response.get("response")

            if not response:
                self.status = "failed"
                self.msg = "Unable to fetch the task Id for the deletion of {0}: '{1}'.".format(type_name, site_name)
                self.log(self.msg, "ERROR")
                return self

            task_id = response.get("taskId")

            if not task_id:
                self.status = "failed"
                self.msg = "No task ID returned for the update request of the deletion of fabric site/zone '{0}'.".format(site_name)
                self.log(self.msg, "ERROR")
                self.result["response"] = self.msg
                return self

            while True:
                task_details = self.get_task_details(task_id)

                if task_details.get("isError"):
                    self.status = "failed"
                    failure_reason = task_details.get("failureReason")
                    if failure_reason:
                        self.msg = "Unable to delete {0} '{1}' because of {2}.".format(type_name, site_name, failure_reason)
                    else:
                        self.msg = "Unable to delete {0} '{1}'.".format(type_name, site_name)
                    self.log(self.msg, "ERROR")
                    self.result['response'] = self.msg
                    break

                if task_details.get("endTime") and "workflow_id" in task_details.get("data"):
                    self.status = "success"
                    if site_type == "fabric_site":
                        self.delete_site.append(site_name)
                    else:
                        self.delete_zone.append(site_name)
                    self.log("{0} '{1}' deleted successfully from the Cisco Catalyst Center".format(type_name.title(), site_name), "INFO")
                    break

                time.sleep(1)
        except Exception as e:
            self.status = "failed"
            self.msg = "Exception occurred while deleting {0} '{1}' due to: {2}".format(type_name, site_name, str(e))
            self.log(self.msg, "ERROR")

        return self

    def update_site_zones_profile_messages(self):
        """
        Updates and logs messages based on the status of fabric sites, fabric zones, and authentication profile templates.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Returns:
            self (object): Returns the current instance of the class with updated `result` and `msg` attributes.
        Description:
            This method aggregates status messages related to the creation, update, or deletion of fabric sites, fabric zones,
            and authentication profile templates.
            It checks various instance variables (`create_site`, `update_site`, `no_update_site`, `create_zone`, `update_zone`,
            `no_update_zone`, `update_auth_profile`, `no_update_profile`, `delete_site`, `absent_site`, `delete_zone`, `absent_zone`)
            to determine the status and generates corresponding messages.
            The method also updates the `result["response"]` attribute with the concatenated status messages.
        """

        self.result["changed"] = False
        result_msg_list = []

        if self.create_site:
            create_site_msg = "Fabric site(s) '{0}' created successfully in Cisco Catalyst Center.".format(self.create_site)
            result_msg_list.append(create_site_msg)

        if self.update_site:
            update_site_msg = "Fabric site(s) '{0}' updated successfully in Cisco Catalyst Center.".format(self.update_site)
            result_msg_list.append(update_site_msg)

        if self.no_update_site:
            no_update_site_msg = "Fabric site(s) '{0}' need no update in Cisco Catalyst Center.".format(self.no_update_site)
            result_msg_list.append(no_update_site_msg)

        if self.create_zone:
            create_zone_msg = "Fabric zone(s) '{0}' created successfully in Cisco Catalyst Center.".format(self.create_zone)
            result_msg_list.append(create_zone_msg)

        if self.update_zone:
            update_zone_msg = "Fabric zone(s) '{0}' updated successfully in Cisco Catalyst Center.".format(self.update_zone)
            result_msg_list.append(update_zone_msg)

        if self.no_update_zone:
            no_update_zone_msg = "Fabric zone(s) '{0}' need no update in Cisco Catalyst Center.".format(self.no_update_zone)
            result_msg_list.append(no_update_zone_msg)

        if self.update_auth_profile:
            update_auth_msg = """Authentication profile template for site(s) '{0}' updated successfully in Cisco Catalyst
                        Center.""".format(self.update_auth_profile)
            result_msg_list.append(update_auth_msg)

        if self.no_update_profile:
            no_update_auth_msg = "Authentication profile template for site(s) '{0}' need no update in Cisco Catalyst Center.".format(self.no_update_profile)
            result_msg_list.append(no_update_auth_msg)

        if self.delete_site:
            delete_site_msg = "Fabric site(s) '{0}' deleted successfully from the Cisco Catalyst Center.".format(self.delete_site)
            result_msg_list.append(delete_site_msg)

        if self.absent_site:
            absent_site_msg = "Unable to delete fabric site(s) '{0}' as they are not present in Cisco Catalyst Center.".format(self.absent_site)
            result_msg_list.append(absent_site_msg)

        if self.delete_zone:
            delete_zone_msg = "Fabric zone(s) '{0}' deleted successfully from the Cisco Catalyst Center.".format(self.delete_zone)
            result_msg_list.append(delete_zone_msg)

        if self.absent_zone:
            absent_zone_msg = "Unable to delete fabric zone(s) '{0}' as they are not present in Cisco Catalyst Center.".format(self.absent_zone)
            result_msg_list.append(absent_zone_msg)

        if self.create_site or self.update_site or self.create_zone or self.update_zone or self.delete_site or self.update_auth_profile:
            self.result["changed"] = True

        self.msg = " ".join(result_msg_list)
        self.log(self.msg, "INFO")
        self.result["response"] = self.msg

        return self

    def get_diff_merged(self, config):
        """
        Creates, updates, or deletes fabric sites and zones based on the provided configuration, and manages
        authentication profile updates.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (dict): A dictionary containing the configuration for fabric sites and zones and updating
                    authentication profile template.
        Returns:
            self (object): Returns the current instance of the class with updated attributes based on the operations performed.
        Description:
            This method processes the provided configuration to manage fabric sites and zones in Cisco Catalyst Center.
            1. Fabric Sites
                - If 'fabric_sites' is present in the configuration, it iterates over the list of sites.
                - Checks if the site needs to be created or updated based on its type ("fabric_site" or "fabric_zone").
                - Creates or updates the site as necessary. If the site does not need any updates, it logs this information.
            2. Authentication Profile
                - If an `update_authentication_profile` parameter is provided, it validates and updates the authentication
                    profile template associated with the site.
                - Ensures that the authentication profile is valid and performs updates if needed.
                - If no update is necessary or if the profile is not present, it logs the appropriate messages.
        """

        # Create/Update Fabric sites/zones in Cisco Catalyst Center
        fabric_sites = self.want.get('fabric_sites')

        for site in fabric_sites:
            site_name = site.get("site_name")
            site_type = site.get("site_type", "fabric_site")
            site_id = self.get_site_id(site_name)
            auth_profile = site.get("authentication_profile")

            if auth_profile and auth_profile not in ["Closed Authentication", "Low Impact", "No Authentication", "Open Authentication"]:
                self.status = "failed"
                self.msg = (
                    "Invalid authentication_profile '{0}'given in the playbook for the creation of fabric site. "
                    "Please provide one of the following authentication_profile ['Closed Authentication', 'Low Impact'"
                    ", 'No Authentication', 'Open Authentication'] in the playbook."
                ).format(auth_profile)
                self.log(self.msg, "ERROR")
                self.result["response"] = self.msg
                return self

            if site_type == "fabric_site":
                # Check whether site is already fabric or not.
                if site_id not in self.have.get("fabric_sites_ids"):
                    # Create the fabric site in Cisco Catalyst Center
                    self.create_fabric_site(site).check_return_status()
                else:
                    # Check whether fabric site needs any update or not
                    site_in_ccc = self.get_fabric_site_detail(site_name, site_id)
                    require_update = self.fabric_site_needs_update(site, site_in_ccc)
                    if require_update:
                        self.update_fabric_site(site, site_in_ccc).check_return_status()
                    else:
                        self.status = "success"
                        self.no_update_site.append(site_name)
                        self.log("Fabric site '{0}' already present and doesnot need any update in the Cisco Catalyst Center.".format(site_name), "INFO")
            else:
                # Check whether site zone is already fabric or not.
                if site_id not in self.have.get("fabric_zone_ids"):
                    # Create the fabric site in Cisco Catalyst Center
                    self.create_fabric_zone(site).check_return_status()
                else:
                    # Check whether fabric site needs any update or not
                    zone_in_ccc = self.get_fabric_zone_detail(site_name, site_id)
                    if auth_profile and auth_profile != zone_in_ccc.get("authenticationProfileName"):
                        self.update_fabric_zone(site, zone_in_ccc).check_return_status()
                    else:
                        self.status = "success"
                        self.no_update_zone.append(site_name)
                        self.log("Fabric zone '{0}' already present and doesnot need any update in the Cisco Catalyst Center.".format(site_name), "INFO")

            # Updating/customising the default parameters for authentication profile template
            if site.get("update_authentication_profile"):
                if not auth_profile:
                    self.status = "failed"
                    self.msg = (
                        "Required parameter 'authentication_profile' is missing needed for updation of Authentication Profile template. "
                        "Please provide one of the following authentication_profile ['Closed Authentication', 'Low Impact'"
                        ", 'Open Authentication'] in the playbook."
                    )
                    self.log(self.msg, "ERROR")
                    self.result["response"] = self.msg
                    return self

                if auth_profile == "No Authentication":
                    self.status = "success"
                    msg = (
                        "Unable to update 'authentication_profile' for the site '{0}' as for the profile template 'No Authentication' updating "
                        "authentication_profile is not supported. Please provide one of the following authentication_profile ['Closed Authentication'"
                        ", 'Low Impact', 'Open Authentication'] in the playbook."
                    ).format(site_name)
                    self.log(msg, "INFO")
                    self.no_update_profile.append(site_name)
                    return self

                # With the given site id collect the fabric site/zone id
                if site_type == "fabric_site":
                    site_detail = self.get_fabric_site_detail(site_name, site_id)
                    fabric_id = site_detail.get("id")
                else:
                    zone_detail = self.get_fabric_zone_detail(site_name, site_id)
                    fabric_id = zone_detail.get("id")

                # Validate the playbook input parameter for updating the authentication profile
                auth_profile_dict = site.get("update_authentication_profile")
                self.validate_auth_profile_parameters(auth_profile_dict).check_return_status()
                validate_msg = (
                    "All the given parameter(s) '{0}' in the playbook for the updation of authentication "
                    " profile in SDA fabric site/zone are validated successfully."
                ).format(auth_profile_dict)
                self.log(validate_msg, "INFO")
                auth_profile_in_ccc = self.get_authentication_profile(fabric_id, auth_profile, site_name)

                if not auth_profile_in_ccc:
                    self.status = "success"
                    msg = (
                        "There is no authentication template profile associated to the site '{0}' "
                        "in the Cisco Catalyst Center so unable to update the profile parameters."
                    ).format(site_name)
                    self.log(self.msg, "INFO")
                    self.no_update_profile.append(site_name)
                    return self

                profile_needs_update = self.auth_profile_needs_update(auth_profile_dict, auth_profile_in_ccc)
                if not profile_needs_update:
                    self.status = "success"
                    msg = (
                        "Authentication profile for the site '{0}' does not need any update in the "
                        "Cisco Catalyst Center."
                    ).format(site_name)
                    self.log(msg, "INFO")
                    self.no_update_profile.append(site_name)
                    return self

                # Collect the authentication profile parameters for the update operation
                profile_update_params = self.collect_authentication_params(auth_profile_dict, auth_profile_in_ccc)
                self.update_authentication_profile_template(profile_update_params, site_name).check_return_status()

        return self

    def get_diff_deleted(self, config):
        """
        Deletes fabric sites and zones from the Cisco Catalyst Center based on the provided configuration.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (dict): A dictionary containing the configuration for fabric sites and zones. It may include:
                - 'fabric_sites' - List of dictionaries, where each dictionary represents a fabric site or zone.
                    - 'site_name' - The name of the site or zone to be deleted.
                    - 'site_type'- Type of the site or zone, either "fabric_site" or "fabric_zone". Defaults to "fabric_site".
        Returns:
            self (object): Returns the current instance of the class with updated attributes based on the deletion operations performed.
        Description:
            This method processes the provided configuration to manage the deletion of fabric sites and zones in Cisco Catalyst Center.
            - For Fabric Sites
                - Verifies if the site exists in Cisco Catalyst Center.
                - Deletes the site if it exists; otherwise, logs a message indicating the site is not present.
            - For Fabric Zones
                - Verifies if the zone exists in Cisco Catalyst Center.
                - Deletes the zone if it exists; otherwise, logs a message indicating the zone is not present.
        """

        # Delete Fabric sites/zones from the Cisco Catalyst Center
        if not config.get('fabric_sites'):
            self.status = "failed"
            self.msg = "Unable to delete any fabric site/zone or authentication profile template as input is not given in the playbook."
            self.log(self.msg, "ERROR")
            self.result["response"] = self.msg
            return self

        fabric_sites = self.want.get('fabric_sites')

        for site in fabric_sites:
            site_name = site.get("site_name")
            site_type = site.get("site_type", "fabric_site")
            if not site_name:
                self.status = "failed"
                self.msg = "Unable to delete fabric site/zone as required parameter 'site_name' is not given in the playbook."
                self.log(self.msg, "ERROR")
                self.result["response"] = self.msg
                return self

            site_id = self.get_site_id(site_name)

            if site_type == "fabric_site":
                # Check whether fabric site is present in Cisco Catalyst Center.
                if site_id in self.have.get("fabric_sites_ids"):
                    site_detail = self.get_fabric_site_detail(site_name, site_id)
                    fabric_id = site_detail.get("id")
                    # Delete the fabric site from the Cisco Catalyst Center
                    self.delete_fabric_site_zone(fabric_id, site_name, site_type).check_return_status()
                else:
                    self.status = "success"
                    self.absent_site.append(site_name)
                    self.log("Unable to delete fabric site '{0}' as it is not present in the Cisco Catalyst Center.".format(site_name), "INFO")
            else:
                # Check whether fabric zone is present in Cisco Catalyst Center.
                if site_id in self.have.get("fabric_zone_ids"):
                    site_detail = self.get_fabric_zone_detail(site_name, site_id, )
                    fabric_id = site_detail.get("id")
                    # Delete the fabric zone from the Cisco Catalyst Center
                    self.delete_fabric_site_zone(fabric_id, site_name, site_type).check_return_status()
                else:
                    self.status = "success"
                    self.absent_zone.append(site_name)
                    self.log("Unable to delete fabric zone '{0}' as it is not present in the Cisco Catalyst Center.".format(site_name), "INFO")

        return self

    def verify_diff_merged(self, config):
        """
        Verify the addition/update status of fabric site/zones in Cisco Catalyst Center.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (dict): The configuration details to be verified.
        Returns:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            This method verifies whether the specified configurations have been successfully added/updated
            in Cisco Catalyst Center as desired.
        """

        self.get_have(config)
        self.log("Current State (have): {0}".format(str(self.have)), "INFO")
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

        if config.get('fabric_sites'):
            fabric_sites = self.want.get('fabric_sites')
            verify_site_list, verify_auth_list = [], []
            site_name_list, auth_name_list = [], []
            auth_flag = False

            for site in fabric_sites:
                site_name = site.get("site_name")
                site_type = site.get("site_type", "fabric_site")
                site_id = self.get_site_id(site_name)

                if site_type == "fabric_site":
                    if site_id not in self.have.get("fabric_sites_ids"):
                        verify_site_list.append(site_name)
                    else:
                        site_name_list.append(site_name)
                else:
                    if site_id not in self.have.get("fabric_zone_ids"):
                        verify_site_list.append(site_name)
                    else:
                        site_name_list.append(site_name)

                #  Verifying updating/customising the default parameters for authentication profile template
                if site.get("update_authentication_profile"):
                    auth_flag = True
                    # With the given site id collect the fabric site/zone id
                    if site_type == "fabric_site":
                        site_detail = self.get_fabric_site_detail(site_name, site_id)
                        fabric_id = site_detail.get("id")
                        auth_name_list.append(site_name)
                    else:
                        zone_detail = self.get_fabric_zone_detail(site_name, site_id)
                        fabric_id = zone_detail.get("id")
                        auth_name_list.append(site_name)

                    if not fabric_id:
                        verify_auth_list.append(site_name)

            if not verify_site_list:
                self.status = "success"
                msg = (
                    "Requested fabric site(s)/zone(s) '{0}' have been successfully added/updated to the Cisco Catalyst Center "
                    "and their addition/updation has been verified."
                ).format(site_name_list)
                self.log(msg, "INFO")
            else:
                msg = (
                    "Playbook's input does not match with Cisco Catalyst Center, indicating that the fabric site(s) '{0}' "
                    " addition/updation task may not have executed successfully."
                ).format(verify_site_list)
                self.log(msg, "INFO")

            if not auth_flag:
                return self

            if not verify_auth_list:
                self.status = "success"
                msg = (
                    "Authentication template profile for the site(s) '{0}' have been successfully updated to the Cisco Catalyst Center "
                    "and their updation has been verified."
                ).format(auth_name_list)
                self.log(msg, "INFO")
            else:
                msg = (
                    "Playbook's input does not match with Cisco Catalyst Center, indicating that the Authentication template "
                    "profile for the site(s) '{0}' updation task may not have executed successfully."
                ).format(verify_auth_list)
                self.log(msg, "INFO")

        return self

    def verify_diff_deleted(self, config):
        """
        Verify the deletion status of fabric sites/zones fromt the Cisco Catalyst Center.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (dict): The configuration details to be verified.
        Returns:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            This method checks the deletion status of a configuration in Cisco Catalyst Center.
            It validates whether the specified fabric site/zone deleted from Cisco Catalyst Center.
        """

        self.get_have(config)
        self.log("Current State (have): {0}".format(str(self.have)), "INFO")
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

        fabric_sites = self.want.get('fabric_sites')
        verify_site_list, site_name_list = [], []

        for site in fabric_sites:
            site_name = site.get("site_name")
            site_type = site.get("site_type", "fabric_site")
            site_id = self.get_site_id(site_name)

            if site_type == "fabric_site":
                # Check whether fabric site is present in Cisco Catalyst Center.
                if site_id in self.have.get("fabric_sites_ids"):
                    verify_site_list.append(site_name)
                else:
                    site_name_list.append(site_name)
            else:
                # Check whether fabric zone is present in Cisco Catalyst Center.
                if site_id in self.have.get("fabric_zone_ids"):
                    verify_site_list.append(site_name)
                else:
                    site_name_list.append(site_name)

        if not verify_site_list:
            self.status = "success"
            msg = (
                "Requested fabric site(s)/zones(s) '{0}' have been successfully deleted from the Cisco Catalyst "
                "Center and their deletion has been verified."
            ).format(site_name_list)
            self.log(msg, "INFO")
        else:
            msg = (
                "Playbook's input does not match with Cisco Catalyst Center, indicating that fabric site(s)/zones(s)"
                " '{0}' deletion task may not have executed successfully."
            ).format(verify_site_list)

        return self


def main():
    """ main entry point for module execution
    """

    element_spec = {'dnac_host': {'required': True, 'type': 'str'},
                    'dnac_port': {'type': 'str', 'default': '443'},
                    'dnac_username': {'type': 'str', 'default': 'admin', 'aliases': ['user']},
                    'dnac_password': {'type': 'str', 'no_log': True},
                    'dnac_verify': {'type': 'bool', 'default': 'True'},
                    'dnac_version': {'type': 'str', 'default': '2.2.3.3'},
                    'dnac_debug': {'type': 'bool', 'default': False},
                    'dnac_log_level': {'type': 'str', 'default': 'WARNING'},
                    "dnac_log_file_path": {"type": 'str', "default": 'dnac.log'},
                    "dnac_log_append": {"type": 'bool', "default": True},
                    'dnac_log': {'type': 'bool', 'default': False},
                    'validate_response_schema': {'type': 'bool', 'default': True},
                    'config_verify': {'type': 'bool', "default": False},
                    'dnac_api_task_timeout': {'type': 'int', "default": 1200},
                    'dnac_task_poll_interval': {'type': 'int', "default": 2},
                    'config': {'required': True, 'type': 'list', 'elements': 'dict'},
                    'state': {'default': 'merged', 'choices': ['merged', 'deleted']}
                    }

    module = AnsibleModule(argument_spec=element_spec,
                           supports_check_mode=False)

    ccc_fabric_sites = FabricSitesZones(module)
    state = ccc_fabric_sites.params.get("state")

    if state not in ccc_fabric_sites.supported_states:
        ccc_fabric_sites.status = "invalid"
        ccc_fabric_sites.msg = "State {0} is invalid".format(state)
        ccc_fabric_sites.check_return_status()

    ccc_fabric_sites.validate_input().check_return_status()
    config_verify = ccc_fabric_sites.params.get("config_verify")

    for config in ccc_fabric_sites.validated_config:
        ccc_fabric_sites.reset_values()
        ccc_fabric_sites.get_want(config).check_return_status()
        ccc_fabric_sites.get_have(config).check_return_status()
        ccc_fabric_sites.get_diff_state_apply[state](config).check_return_status()
        if config_verify:
            ccc_fabric_sites.verify_diff_state_apply[state](config).check_return_status()

    # Invoke the API to check the status and log the output of each site/zone and authentication profile update on console.
    ccc_fabric_sites.update_site_zones_profile_messages().check_return_status()

    module.exit_json(**ccc_fabric_sites.result)


if __name__ == '__main__':
    main()
