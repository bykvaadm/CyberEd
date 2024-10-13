#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ("Abinash Mishra, Madhan Sankaranarayanan")

DOCUMENTATION = r"""
---
module: provision_workflow_manager
short_description: Resource module for provision related functions
description:
- Manage operations related to wired and wireless provisioning
- API to re-provision provisioned devices
- API to un-provision provisioned devices
version_added: '6.6.0'
extends_documentation_fragment:
  - cisco.dnac.workflow_manager_params
author: Abinash Mishra (@abimishr)
        Madhan Sankaranarayanan (@madhansansel)
options:
  config_verify:
    description: Set to True to verify the Cisco Catalyst Center config after applying the playbook config.
    type: bool
    default: False
  state:
    description: The state of Cisco Catalyst Center after module completion.
    type: str
    choices: [ merged, deleted ]
    default: merged
  config:
    description:
    - List of details of device being managed.
    type: list
    elements: dict
    required: true
    suboptions:
        management_ip_address:
            description: Management Ip Address of the device.
            type: str
            required: true
        provisioning:
            description:
                - Specifies whether the user intends to perform site assignment only or full provisioning for a wired device.
                - Set to 'False' to carry out site assignment only.
                - Set to 'True' to proceed with provisioning to a site.
            type: bool
            required: false
            default: true
        site_name_hierarchy:
            description: Name of site where the device needs to be added.
            type: str
        managed_ap_locations:
            description:
                - Location of the sites allocated for the APs.
                - This is mandatory for provisioning of wireless devices.
            type: list
            elements: str
        dynamic_interfaces:
            description: Interface details of the controller
            type: list
            elements: dict
            suboptions:
                interface_ip_address:
                    description: Ip Address allocated to the interface
                    type: str
                interface_netmask_in_c_i_d_r:
                    description: Ip Address allocated to the interface
                    type: int
                interface_gateway:
                    description: Ip Address allocated to the interface
                    type: str
                lag_or_port_number:
                    description: Ip Address allocated to the interface
                    type: int
                vlan_id:
                    description: Ip Address allocated to the interface
                    type: int
                interface_name:
                    description: Ip Address allocated to the interface
                    type: str

requirements:
- dnacentersdk == 2.4.5
- python >= 3.9
notes:
  - SDK Methods used are
    sites.Sites.get_site,
    devices.Devices.get_network_device_by_ip,
    task.Task.get_task_by_id,
    sda.Sda.get_provisioned_wired_device,
    sda.Sda.re_provision_wired_device,
    sda.Sda.provision_wired_device,
    wireless.Wireless.provision

  - Paths used are
    get /dna/intent/api/v1/site
    get /dna/intent/api/v1/network-device/ip-address/{ipAddress}
    get /dna/intent/api/v1/task/{taskId}
    get /dna/intent/api/v1/business/sda/provision-device
    put /dna/intent/api/v1/business/sda/provision-device
    post /dna/intent/api/v1/business/sda/provision-device
    post /dna/intent/api/v1/wireless/provision

  - Added 'provisioning' option in v6.16.0
  - Added provisioning and reprovisioning of wireless devices in v6.16.0

"""

EXAMPLES = r"""
- name: Provision a wireless device to a site
  cisco.dnac.provision_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    state: merged
    config:
        - site_name_hierarchy: Global/USA/San Francisco/BGL_18
          management_ip_address: 204.192.3.40
          managed_ap_locations:
            - Global/USA/San Francisco/BGL_18/Test_Floor2
          dynamic_interfaces:
            - vlan_id: 1866
              interface_name: Vlan1866
              interface_ip_address: 204.192.6.200
              interface_gateway: 204.192.6.1

- name: Provision a wired device to a site
  cisco.dnac.provision_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    state: merged
    config:
        - site_name_hierarchy: Global/USA/San Francisco/BGL_18
          management_ip_address: 204.192.3.40

- name: Assign a wired device to a site
  cisco.dnac.provision_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    state: merged
    config:
        - site_name_hierarchy: Global/USA/San Francisco/BGL_18
          management_ip_address: 204.192.3.40
          provisioning: False

- name: Provision a wireless device to a site
  cisco.dnac.provision_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    state: merged
    config_verify: True
    config:
        - site_name_hierarchy: Global/USA/RTP/BLD11
          management_ip_address: 204.192.12.201
          managed_ap_locations:
            - Global/USA/RTP/BLD11/BLD11_FLOOR1

- name: Unprovision a device from a site
  cisco.dnac.provision_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    state: deleted
    config_verify: True
    config:
        - management_ip_address: 204.1.2.2

"""

RETURN = r"""
# Case_1: Successful creation/updation/deletion of provision
response_1:
  description: A dictionary with details of provision is returned
  returned: always
  type: dict
  sample: >
    {
      "response":
      {
        "response": String,
        "version": String
        },
      "msg": String
    }

# Case_2: Error while creating a provision
response_2:
  description: A list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: list
  sample: >
    {
      "response": [],
      "msg": String
    }

# Case_3: Already exists and requires no update
response_3:
  description: A dictionary with the exisiting details as returned by the Cisco Cisco Catalyst Center  Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": String,
      "msg": String
    }
"""
import time
import re
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts
)


class Provision(DnacBase):

    """
    Class containing member attributes for provision workflow module
    """
    def __init__(self, module):
        super().__init__(module)

    def validate_input(self, state=None):

        """
        Validate the fields provided in the playbook.
        Checks the configuration provided in the playbook against a predefined specification
        to ensure it adheres to the expected structure and data types.
        Args:
            self: The instance of the class containing the 'config' attribute to be validated.
        Returns:
            The method returns an instance of the class with updated attributes:
                - self.msg: A message describing the validation result.
                - self.status: The status of the validation (either 'success' or 'failed').
                - self.validated_config: If successful, a validated version of the
                  'config' parameter.
        Example:
            To use this method, create an instance of the class and call 'validate_input' on it.
            If the validation succeeds, 'self.status' will be 'success' and
            'self.validated_config' will contain the validated configuration. If it fails,
            'self.status' will be 'failed', and 'self.msg' will describe the validation issues.
        """

        if not self.config:
            self.msg = "config not available in playbook for validation"
            self.status = "success"
            return self

        provision_spec = {
            "management_ip_address": {'type': 'str', 'required': True},
            "site_name_hierarchy": {'type': 'str', 'required': False},
            "managed_ap_locations": {'type': 'list', 'required': False,
                                     'elements': 'str'},
            "dynamic_interfaces": {'type': 'list', 'required': False,
                                   'elements': 'dict'},
            "provisioning": {'type': 'bool', 'required': False, "default": True}
        }
        if state == "merged":
            provision_spec["site_name_hierarchy"] = {'type': 'str', 'required': True}

        # Validate provision params
        valid_provision, invalid_params = validate_list_of_dicts(
            self.config, provision_spec
        )
        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(
                "\n".join(invalid_params))
            self.log(str(self.msg), "ERROR")
            self.status = "failed"
            return self

        self.validated_config = valid_provision
        self.msg = "Successfully validated playbook configuration parameters using 'validate_input': {0}".format(str(valid_provision))
        self.log(str(self.msg), "INFO")
        self.status = "success"
        return self

    def get_dev_type(self):
        """
        Fetches the type of device (wired/wireless)

        Parameters:
          - self: The instance of the class containing the 'config' attribute
                  to be validated.
        Returns:
          The method returns an instance of the class with updated attributes:
          - device_type: A string indicating the type of the
                       device (wired/wireless).
        Example:
          Post creation of the validated input, we use this method to get the
          type of the device.
        """
        try:
            dev_response = self.dnac_apply['exec'](
                family="devices",
                function='get_network_device_by_ip',
                params={"ip_address": self.validated_config[0]["management_ip_address"]},
                op_modifies=True
            )
        except Exception as e:
            self.log(str(e), "ERROR")
            self.module.fail_json(msg=str(e))

        self.log("The device response from 'get_network_device_by_ip' API is {0}".format(str(dev_response)), "DEBUG")
        dev_dict = dev_response.get("response")
        device_family = dev_dict["family"]

        if device_family == "Wireless Controller":
            device_type = "wireless"
        elif device_family in ["Switches and Hubs", "Routers"]:
            device_type = "wired"
        else:
            device_type = None
        self.log("The device type is {0}".format(device_type), "INFO")
        return device_type

    def get_device_id(self):
        """
        Fetches the UUID of the device added in the inventory

        Parameters:
          - self: The instance of the class containing the 'config' attribute
                  to be validated.
        Returns:
          The method returns the serial number of the device as a string. If it fails, it returns None.
        Example:
          After creating the validated input, this method retrieves the
          UUID of the device.
        """

        dev_response = self.dnac_apply['exec'](
            family="devices",
            function='get_network_device_by_ip',
            params={"ip_address": self.validated_config[0]["management_ip_address"]},
            op_modifies=True
        )

        self.log("The device response from 'get_network_device_by_ip' API is {0}".format(str(dev_response)), "DEBUG")
        dev_dict = dev_response.get("response")
        device_id = dev_dict.get("id")

        self.log("Device ID of the device with IP address {0} is {1}".format(self.validated_config[0]["management_ip_address"], device_id), "INFO")
        return device_id

    def get_serial_number(self):
        """
        Fetches the serial number of the device

        Parameters:
          - self: The instance of the class containing the 'config' attribute
                  to be validated.
        Returns:
          The method returns the serial number of the device as a string. If it fails, it returns None.
        Example:
          After creating the validated input, this method retrieves the
          serial number of the device.
        """

        try:
            response = self.dnac_apply['exec'](
                family="devices",
                function='get_network_device_by_ip',
                params={"ip_address": self.validated_config[0]["management_ip_address"]},
                op_modifies=True
            )

        except Exception as e:
            self.log("An error occurred while fetching the serial number: {0}".format(str(e)), "ERROR")
            return None

        if not (response or response.get("response")):
            self.log("No response received from 'get_network_device_by_ip' API or it's invalid.", "ERROR")
            return None

        self.log("The device response from 'get_network_device_by_ip' API is {0}".format(str(response)), "DEBUG")
        dev_dict = response.get("response")
        serial_number = dev_dict.get("serialNumber")

        if not serial_number:
            self.log("Serial number not found in the response.", "ERROR")
            return None

        self.log("Serial Number of the device is {0}".format(str(serial_number)), "INFO")

        return serial_number

    def get_task_status(self, task_id=None):
        """
        Fetches the status of the task once any provision API is called

        Parameters:
          - self: The instance of the class containing the 'config' attribute
                  to be validated.
          - task_id: Task_id of the provisioning task.
        Returns:
          The method returns the status of the task_id used to track provisioning.
          Returns True if task is not failed otheriwse returns False.
        Example:
          Post creation of the provision task, this method fetheches the task
          status.

        """
        result = False
        params = {"task_id": task_id}
        while True:
            response = self.dnac_apply['exec'](
                family="task",
                function='get_task_by_id',
                params=params,
                op_modifies=True
            )
            self.log("Response collected from 'get_task_by_id' API is {0}".format(str(response)), "DEBUG")
            response = response.response
            self.log("Task status for the task id {0} is {1}".format(str(task_id), str(response.get("progress"))), "INFO")
            if response.get('isError') or re.search(
                'failed', response.get('progress'), flags=re.IGNORECASE
            ):
                msg = 'Provision task with id {0} has not completed - Reason: {1}'.format(
                    task_id, response.get("failureReason"))
                self.module.fail_json(msg=msg)
                return False

            if response.get('progress') in ["TASK_PROVISION", "TASK_MODIFY_PUT"] and response.get("isError") is False:
                result = True
                break

            time.sleep(3)
        self.result.update(dict(provision_task=response))
        return result

    def get_execution_status_site(self, execution_id=None):
        """
        Fetches the status of the BAPI once site assignment API is called

        Parameters:
          - self: The instance of the class containing the 'config' attribute
                  to be validated.
          - execution_id: execution_id of the BAPI API.
        Returns:
          The method returns the status of the BAPI used to track site assignment.
          Returns True if the status is not failed, otheriwse returns False.
        Example:
          Post creation of the provision task, this method fetheches the task
          status.

        """
        result = False
        params = {"execution_id": execution_id}
        while True:
            response = self.dnac_apply['exec'](
                family="task",
                function="get_business_api_execution_details",
                params=params,
                op_modifies=True
            )
            self.log("Response collected from 'get_business_api_execution_details' API is {0}".format(str(response)), "DEBUG")
            self.log("Execution status for the execution id {0} is {1}".format(str(execution_id), str(response.get("status"))), "INFO")
            if response.get('bapiError') or response.get("status") == "FAILURE":
                msg = 'Assigning to site execution with id {0} has not completed - Reason: {1}'.format(
                    execution_id, response.get("bapiError"))
                self.module.fail_json(msg=msg)
                return False

            if response.get('status') == 'SUCCESS':
                result = True
                break

            time.sleep(3)
        self.result.update(dict(assignment_task=response))
        return result

    def get_execution_status_wireless(self, execution_id=None):
        """
        Fetches the status of the BAPI once site wireless provision API is called

        Parameters:
          - self: The instance of the class containing the 'config' attribute
                  to be validated.
          - execution_id: execution_id of the BAPI API.
        Returns:
          The method returns the status of the BAPI used to track wireless provisioning.
          Returns True if the status is not failed, otheriwse returns False.
        Example:
          Post creation of the provision task, this method fetheches the task
          status.

        """
        result = False
        params = {"execution_id": execution_id}
        while True:
            response = self.dnac_apply['exec'](
                family="task",
                function="get_business_api_execution_details",
                params=params,
                op_modifies=True
            )
            self.log("Response collected from 'get_business_api_execution_details' API is {0}".format(str(response)), "DEBUG")
            self.log("Execution status for the execution id {0} is {1}".format(str(execution_id), str(response.get("status"))), "INFO")
            if response.get('bapiError') or response.get("status") == "FAILURE":
                if response.get("bapiError") == "Device was already provisioned , please use provision update API to reprovision the device":
                    msg = "Performing reprovisioning of wireless device"
                    result = True
                    self.perform_wireless_reprovision()
                    break
                msg = 'Wireless provisioning execution with id {0} has not completed - Reason: {1}'.format(
                    execution_id, response.get("bapiError"))
                self.module.fail_json(msg=msg)
                return False

            if response.get('status') == 'SUCCESS':
                result = True
                break

            time.sleep(3)
        self.result.update(dict(assignment_task=response))
        return result

    def get_site_type(self, site_name_hierarchy=None):
        """
        Fetches the type of site

        Parameters:
          - self: The instance of the class containing the 'config' attribute
                  to be validated.
          - site_name_hierarchy: Name of the site collected from the input.
        Returns:
          - site_type: A string indicating the type of the site (area/building/floor).
        Example:
          Post creation of the validated input, this method gets the
          type of the site.
        """

        try:
            response = self.dnac_apply['exec'](
                family="sites",
                function='get_site',
                params={"name": site_name_hierarchy},
                op_modifies=True
            )
        except Exception:
            self.log("Exception occurred as \
                site '{0}' was not found".format(site_name_hierarchy), "CRITICAL")
            self.module.fail_json(msg="Site not found", response=[])

        if response:
            self.log("Received site details\
                for '{0}': {1}".format(site_name_hierarchy, str(response)), "DEBUG")
            site = response.get("response")
            site_additional_info = site[0].get("additionalInfo")
            for item in site_additional_info:
                if item["nameSpace"] == "Location":
                    site_type = item.get("attributes").get("type")
                    self.log("Site type for site name '{1}' : {0}".format(site_type, site_name_hierarchy), "INFO")

        return site_type

    def get_site_details(self, site_name_hierarchy=None):
        """
        Fetches the id and existance of the site

        Parameters:
          - self: The instance of the class containing the 'config' attribute
                  to be validated.
          - site_name_hierarchy: Name of the site collected from the input.
        Returns:
          - site_id: A string indicating the id of the site.
          - site_exits: A boolean value indicating the existance of the site.
        Example:
          Post creation of the validated input, this method gets the
          id of the site.
        """

        site_exists = False
        site_id = None
        try:
            response = self.dnac_apply['exec'](
                family="sites",
                function='get_site',
                params={"name": site_name_hierarchy},
                op_modifies=True
            )
        except Exception:
            self.log("Exception occurred as \
                site '{0}' was not found".format(self.want.get("site_name")), "CRITICAL")
            self.module.fail_json(msg="Site not found", response=[])

        if response:
            self.log("Received site details\
                for '{0}': {1}".format(site_name_hierarchy, str(response)), "DEBUG")
            site = response.get("response")
            site_additional_info = site[0].get("additionalInfo")
            if len(site) == 1:
                site_id = site[0].get("id")
                site_exists = True
                self.log("Site Name: {1}, Site ID: {0}".format(site_id, site_name_hierarchy), "INFO")

        return (site_exists, site_id)

    def is_device_assigned_to_site(self, uuid):
        """
        Checks if a device, specified by its UUID, is assigned to any site.

        Parameters:
          - self: The instance of the class containing the 'config' attribute
                  to be validated.
          - uuid (str): The UUID of the device to check for site assignment.
        Returns:
          - boolean:  True if the device is assigned to a site, False otherwise.

        """

        self.log("Checking site assignment for device with UUID: {0}".format(uuid), "INFO")
        try:
            site_response = self.dnac_apply['exec'](
                family="devices",
                function='get_device_detail',
                params={"search_by": uuid ,
                        "identifier": "uuid"},
                op_modifies=True
            )
            self.log("Response collected from the API 'get_device_detail' {0}".format(site_response))
            site_response = site_response.get("response")
            if site_response.get("location"):
                return True
            else:
                return False
        except Exception as e:
            msg = "Failed to find device with UUID {0} due to: {1}".format(uuid, e)
            self.log(msg, "CRITICAL")
            self.module.fail_json(msg=msg)

    def get_site_assign(self):
        """
        Fetches the details of devices assigned to a site

        Parameters:
          - self: The instance of the class containing the 'config' attribute
                  to be validated.
        Returns:
          - boolean: True if any device is associated with the site, False if no device is associated with site

        Example:
          Post creation of the validated input, this method tells whether devices are associated with a site.
        """

        site_name_hierarchy = self.validated_config[0].get("site_name_hierarchy")
        site_exists, site_id = self.get_site_details(site_name_hierarchy=site_name_hierarchy)
        serial_number = self.get_serial_number()
        if site_exists:
            site_response = self.dnac_apply['exec'](
                family="sites",
                function='get_membership',
                params={"site_id": site_id,
                        "serial_number": serial_number},
                op_modifies=True
            )
            self.log("Response collected from the 'get_memership' API is {0}".format(site_response), "DEBUG")
            device_list = site_response.get("device")
            if len(device_list) > 0:
                if all(device.get("response") == [] for device in device_list):
                    return False
                else:
                    return True
            else:
                return False
        return False

    def get_wired_params(self):
        """
        Prepares the payload for provisioning of the wired devices

        Parameters:
          - self: The instance of the class containing the 'config' attribute
                  to be validated.
        Returns:
          The method returns an instance of the class with updated attributes:
          - wired_params: A dictionary containing all the values indicating
                          management IP address of the device and the hierarchy
                          of the site.
        Example:
          Post creation of the validated input, it fetches the required
          paramters and stores it for further processing and calling the
          parameters in other APIs.
        """

        site_name = self.validated_config[0].get("site_name_hierarchy")

        (site_exits, site_id) = self.get_site_details(site_name_hierarchy=site_name)

        if site_exits is False:
            msg = "Site {0} doesn't exist".format(site_name)
            self.log(msg, "CRITICAL")
            self.module.fail_json(msg=msg)

        if self.validated_config[0].get("provisioning") is True:
            wired_params = {
                "deviceManagementIpAddress": self.validated_config[0]["management_ip_address"],
                "siteNameHierarchy": site_name
            }
        else:
            wired_params = {
                "device": [
                    {
                        "ip": self.validated_config[0]["management_ip_address"]
                    }
                ],
                "site_id": site_id
            }

        self.log("Parameters collected for the provisioning of wired device:{0}".format(wired_params), "INFO")
        return wired_params

    def get_wireless_params(self):
        """
        Prepares the payload for provisioning of the wireless devices

        Parameters:
          - self: The instance of the class containing the 'config' attribute
                  to be validated.
        Returns:
          The method returns an instance of the class with updated attributes:
          - wireless_params: A list of dictionary containing all the values indicating
                          management IP address of the device, hierarchy
                          of the site, AP Location of the wireless controller and details
                          of the interface
        Example:
          Post creation of the validated input, it fetches the required
          paramters and stores it for further processing and calling the
          parameters in other APIs.
        """

        wireless_params = [
            {
                "site": self.validated_config[0].get("site_name_hierarchy"),
                "managedAPLocations": self.validated_config[0].get("managed_ap_locations"),
            }
        ]

        if not (wireless_params[0].get("managedAPLocations") and isinstance(wireless_params[0].get("managedAPLocations"), list)):
            msg = "Missing Managed AP Locations: Please specify the intended location(s) for the wireless device \
                within the site hierarchy."
            self.log(msg, "CRITICAL")
            self.module.fail_json(msg=msg, response=[])

        for ap_loc in self.validated_config[0].get("managed_ap_locations"):
            if self.get_site_type(site_name_hierarchy=ap_loc) != "floor":
                self.log("Managed AP Location must be a floor", "CRITICAL")
                self.module.fail_json(msg="Managed AP Location must be a floor", response=[])

        wireless_params[0]["dynamicInterfaces"] = []
        if self.validated_config[0].get("dynamic_interfaces"):
            for interface in self.validated_config[0].get("dynamic_interfaces"):
                interface_dict = {
                    "interfaceIPAddress": interface.get("interface_ip_address"),
                    "interfaceNetmaskInCIDR": interface.get("interface_netmask_in_c_i_d_r"),
                    "interfaceGateway": interface.get("interface_gateway"),
                    "lagOrPortNumber": interface.get("lag_or_port_number"),
                    "vlanId": interface.get("vlan_id"),
                    "interfaceName": interface.get("interface_name")
                }
                wireless_params[0]["dynamicInterfaces"].append(interface_dict)
        response = self.dnac_apply['exec'](
            family="devices",
            function='get_network_device_by_ip',
            params={"ip_address": self.validated_config[0]["management_ip_address"]},
            op_modifies=True
        )

        self.log("Response collected from 'get_network_device_by_ip' is:{0}".format(str(response)), "DEBUG")
        wireless_params[0]["deviceName"] = response.get("response").get("hostname")
        self.log("Parameters collected for the provisioning of wireless device:{0}".format(wireless_params), "INFO")
        return wireless_params

    def get_want(self):
        """
        Get all provision related informantion from the playbook
        Args:
            self: The instance of the class containing the 'config' attribute to be validated.
            config: validated config passed from the playbook
        Returns:
            The method returns an instance of the class with updated attributes:
                - self.want: A dictionary of paramters obtained from the playbook
                - self.msg: A message indicating all the paramters from the playbook are
                collected
                - self.status: Success
        Example:
            It stores all the paramters passed from the playbook for further processing
            before calling the APIs
        """

        self.want = {}
        self.want["device_type"] = self.get_dev_type()
        if self.want["device_type"] == "wired":
            self.want["prov_params"] = self.get_wired_params()
        elif self.want["device_type"] == "wireless":
            self.want["prov_params"] = self.get_wireless_params()
        else:
            self.log("Passed devices are neither wired or wireless devices", "WARNING")

        self.msg = "Successfully collected all parameters from playbook " + \
            "for comparison"
        self.log(self.msg, "INFO")
        self.status = "success"
        return self

    def perform_wireless_reprovision(self):
        """
        This method performs the reprovisioning of a wireless device. Since, we don't have any
        APIs to get provisioned wireless devices, so we are reprovisioning based on the failure
        condition of the device
        Parameters:
            - self: The instance of the class containing the 'config' attribute
                  to be validated.
        Returns:
            object: An instance of the class with updated results and status
            based on the processing of differences.
        Example:
            If wireless device is already provisioned, this method calls the provision update
            API and handles it accordingly
        """

        try:
            headers_payload = {"__persistbapioutput": "true"}
            response = self.dnac_apply['exec'](
                family="wireless",
                function="provision_update",
                op_modifies=True,
                params={"payload": self.want.get("prov_params"),
                        "headers": headers_payload}
            )
            self.log("Wireless provisioning response collected from 'provision_update' API is: {0}".format(str(response)), "DEBUG")
            execution_id = response.get("executionId")
            self.get_execution_status_wireless(execution_id=execution_id)
            self.result["changed"] = True
            self.result['msg'] = "Wireless device with IP address {0} got re-provisioned successfully".format(self.validated_config[0]["management_ip_address"])
            self.result['diff'] = self.validated_config
            self.result['response'] = execution_id
            self.log(self.result['msg'], "INFO")
            return self
        except Exception as e:
            self.log("Parameters are {0}".format(self.want))
            self.msg = "Error in wireless re-provisioning of {0} due to {1}".format(self.validated_config[0]["management_ip_address"], e)
            self.log(self.msg, "ERROR")
            self.status = "failed"
            return self

    def get_diff_merged(self):
        """
        Add to provision database
        Args:
            self: An instance of a class used for interacting with Cisco Catalyst Center.
        Returns:
            object: An instance of the class with updated results and status
            based on the processing of differences.
        Description:
            The function processes the differences and, depending on the
            changes required, it may add, update,or resynchronize devices in
            Cisco Catalyst Center. The updated results and status are stored in the
            class instance for further use.
        """

        device_type = self.want.get("device_type")
        if device_type == "wired":
            try:
                status_response = self.dnac_apply['exec'](
                    family="sda",
                    function="get_provisioned_wired_device",
                    op_modifies=True,
                    params={
                        "device_management_ip_address": self.validated_config[0]["management_ip_address"]
                    },
                )
            except Exception:
                status_response = {}
            self.log("Wired device's status Response collected from 'get_provisioned_wired_device' API is:{0}".format(str(status_response)), "DEBUG")
            status = status_response.get("status")
            self.log("The provisioned status of the wired device is {0}".format(status), "INFO")

            if status == "success":
                try:
                    response = self.dnac_apply['exec'](
                        family="sda",
                        function="re_provision_wired_device",
                        op_modifies=True,
                        params=self.want["prov_params"],
                    )
                    self.log("Reprovisioning response collected from 're_provision_wired_device' API is: {0}".format(response), "DEBUG")
                    task_id = response.get("taskId")
                    self.get_task_status(task_id=task_id)
                    self.result["changed"] = True
                    self.result['msg'] = "Re-Provision done Successfully"
                    self.result['diff'] = self.validated_config
                    self.result['response'] = task_id
                    self.log(self.result['msg'], "INFO")
                    return self

                except Exception as e:
                    self.msg = "Error in re-provisioning due to {0}".format(str(e))
                    self.log(self.msg, "ERROR")
                    self.status = "failed"
                    return self
            else:
                if self.validated_config[0].get("provisioning") is True:
                    try:
                        response = self.dnac_apply['exec'](
                            family="sda",
                            function="provision_wired_device",
                            op_modifies=True,
                            params=self.want["prov_params"],
                        )
                        self.log("Provisioning response collected from 'provision_wired_device' API is: {0}".format(response), "DEBUG")
                    except Exception as e:
                        self.msg = "Error in provisioning due to {0}".format(str(e))
                        self.log(self.msg, "ERROR")
                        self.status = "failed"
                        return self

                else:
                    uuid = self.get_device_id()
                    if self.is_device_assigned_to_site(uuid) is True:
                        self.result["changed"] = False
                        self.result['msg'] = "Device is already assigned to the desired site"
                        self.result['diff'] = self.want
                        self.result['response'] = self.want.get("prov_params").get("site_id")
                        self.log(self.result['msg'], "INFO")
                        return self

                    try:
                        response = self.dnac_apply['exec'](
                            family="sites",
                            function="assign_devices_to_site",
                            op_modifies=True,
                            params={
                                "site_id": self.want.get("prov_params").get("site_id"),
                                "payload": self.want.get("prov_params")
                            },
                        )
                        self.log("Assignment response collected from 'assign_devices_to_site' API is: {0}".format(response), "DEBUG")
                        execution_id = response.get("executionId")
                        assignment_info = self.get_execution_status_site(execution_id=execution_id)
                        self.result["changed"] = True
                        self.result['msg'] = "Site assignment done successfully"
                        self.result['diff'] = self.validated_config
                        self.result['response'] = execution_id
                        self.log(self.result['msg'], "INFO")
                        return self
                    except Exception as e:
                        self.msg = "Error in site assignment due to {0}".format(str(e))
                        self.log(self.msg, "ERROR")
                        self.status = "failed"
                        return self

        elif device_type == "wireless":
            try:
                response = self.dnac_apply['exec'](
                    family="wireless",
                    function="provision",
                    op_modifies=True,
                    params={"payload": self.want.get("prov_params")}
                )
                self.log("Wireless provisioning response collected from 'provision' API is: {0}".format(str(response)), "DEBUG")
                execution_id = response.get("executionId")
                self.get_execution_status_wireless(execution_id=execution_id)
                self.result["changed"] = True
                self.result['msg'] = "Wireless device with IP {0} got provisioned successfully".format(self.validated_config[0]["management_ip_address"])
                self.result['diff'] = self.validated_config
                self.result['response'] = execution_id
                self.log(self.result['msg'], "INFO")
                return self
            except Exception as e:
                self.log("Parameters are {0}".format(self.want))
                self.msg = "Error in wireless provisioning of {0} due to {1}".format(self.validated_config[0]["management_ip_address"], e)
                self.log(self.msg, "ERROR")
                self.status = "failed"
                return self

        else:
            self.result['msg'] = "Passed device is neither wired nor wireless"
            self.log(self.result['msg'], "ERROR")
            self.result['response'] = self.want.get("prov_params")
            return self

        task_id = response.get("taskId")
        self.get_task_status(task_id=task_id)
        self.result["changed"] = True
        self.result['msg'] = "Provision done Successfully"
        self.result['diff'] = self.validated_config
        self.result['response'] = task_id
        self.log(self.result['msg'], "INFO")
        return self

    def get_diff_deleted(self):
        """
        Delete from provision database
        Args:
            self: An instance of a class used for interacting with Cisco Catalyst Center
        Returns:
            self: An instance of the class with updated results and status based on
            the deletion operation.
        Description:
            This function is responsible for removing devices from the Cisco Catalyst Center PnP GUI and
            raise Exception if any error occured.
        """

        device_type = self.want.get("device_type")

        if device_type != "wired":
            self.result['msg'] = "APIs are not supported for the device"
            self.log(self.result['msg'], "CRITICAL")
            return self

        try:
            status_response = self.dnac_apply['exec'](
                family="sda",
                function="get_provisioned_wired_device",
                op_modifies=True,
                params={
                    "device_management_ip_address": self.validated_config[0]["management_ip_address"]
                },
            )

        except Exception:
            status_response = {}
        self.log("Wired device's status Response collected from 'get_provisioned_wired_device' API is:{0}".format(str(status_response)), "DEBUG")
        status = status_response.get("status")
        self.log("The provisioned status of the wired device is {0}".format(status), "INFO")

        if status != "success":
            self.result['msg'] = "Device associated with the passed IP address is not provisioned"
            self.log(self.result['msg'], "CRITICAL")
            self.result['response'] = self.want["prov_params"]
            return self

        response = self.dnac_apply['exec'](
            family="sda",
            function="delete_provisioned_wired_device",
            op_modifies=True,
            params={
                "device_management_ip_address": self.validated_config[0]["management_ip_address"]
            },
        )
        self.log("Response collected from the 'delete_provisioned_wired_device' API is : {0}".format(str(response)), "DEBUG")

        task_id = response.get("taskId")
        deletion_info = self.get_task_status(task_id=task_id)
        self.result["changed"] = True
        self.result['msg'] = "Deletion done Successfully"
        self.result['diff'] = self.validated_config
        self.result['response'] = task_id
        self.log(self.result['msg'], "INFO")
        return self

    def verify_diff_merged(self):
        """
        Verify the merged status(Creation/Updation) of Discovery in Cisco Catalyst Center.
        Args:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - config (dict): The configuration details to be verified.
        Return:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            This method checks the merged status of a configuration in Cisco Catalyst Center by
            retrieving the current state (have) and desired state (want) of the configuration,
            logs the states, and validates whether the specified device(s) exists in the DNA
            Center configuration's Inventory Database in the provisioned state.
        """

        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")
        # Code to validate Cisco Catalyst Center config for merged state

        device_type = self.want.get("device_type")
        provisioning = self.validated_config[0].get("provisioning")
        site_name_hierarchy = self.validated_config[0].get("site_name_hierarchy")
        uuid = self.get_device_id()
        if provisioning is False:
            if self.is_device_assigned_to_site(uuid) is True:
                self.log("Requested device is already added to the site {0}".format(site_name_hierarchy), "INFO")
            else:
                self.log("Requested device is not added to the site {0}".format(site_name_hierarchy), "INFO")
            return self

        if device_type == "wired":
            try:
                status_response = self.dnac_apply['exec'](
                    family="sda",
                    function="get_provisioned_wired_device",
                    op_modifies=True,
                    params={
                        "device_management_ip_address": self.validated_config[0]["management_ip_address"]
                    },
                )
            except Exception:
                status_response = {}
            self.log("Wired device's status Response collected from 'get_provisioned_wired_device' API is:{0}".format(str(status_response)), "DEBUG")
            status = status_response.get("status")
            self.log("The provisioned status of the wired device is {0}".format(status), "INFO")

            if status == "success":
                self.log("Requested wired device is alread provisioned", "INFO")

            else:
                self.log("Requested wired device is not provisioned", "INFO")

        else:
            self.log("Currently we don't have any API in the Cisco Catalyst Center to fetch the provisioning details of wireless devices")
        self.status = "success"

        return self

    def verify_diff_deleted(self):
        """
        Verify the deletion status of Discovery in Cisco Catalyst Center.
        Args:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - config (dict): The configuration details to be verified.
        Return:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            This method checks the deletion status of a configuration in Cisco Catalyst Center.
            It validates whether the specified discovery(s) exists in the Cisco Catalyst Center configuration's
            Inventory Database in the provisioned state.
        """

        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")
        # Code to validate Cisco Catalyst Center config for merged state

        device_type = self.want.get("device_type")
        if device_type == "wired":
            try:
                status_response = self.dnac_apply['exec'](
                    family="sda",
                    function="get_provisioned_wired_device",
                    op_modifies=True,
                    params={
                        "device_management_ip_address": self.validated_config[0]["management_ip_address"]
                    },
                )
            except Exception:
                status_response = {}
            self.log("Wired device's status Response collected from 'get_provisioned_wired_device' API is:{0}".format(str(status_response)), "DEBUG")
            status = status_response.get("status")
            self.log("The provisioned status of the wired device is {0}".format(status), "INFO")

            if status == "success":
                self.log("Requested wired device is in provisioned state and is not unprovisioned", "INFO")

            else:
                self.log("Requested wired device is unprovisioned", "INFO")

        else:
            self.log("Currently we don't have any API in the Cisco Catalyst Center to fetch the provisioning details of wireless devices")
        self.status = "success"

        return self


def main():

    """
    main entry point for module execution
    """

    element_spec = {'dnac_host': {'required': True, 'type': 'str'},
                    'dnac_port': {'type': 'str', 'default': '443'},
                    'dnac_username': {'type': 'str', 'default': 'admin', 'aliases': ['user']},
                    'dnac_password': {'type': 'str', 'no_log': True},
                    'dnac_verify': {'type': 'bool', 'default': 'True'},
                    'dnac_version': {'type': 'str', 'default': '2.2.3.3'},
                    'dnac_debug': {'type': 'bool', 'default': False},
                    'dnac_log': {'type': 'bool', 'default': False},
                    "dnac_log_level": {"type": 'str', "default": 'WARNING'},
                    "dnac_log_file_path": {"type": 'str', "default": 'dnac.log'},
                    "dnac_log_append": {"type": 'bool', "default": True},
                    "config_verify": {"type": 'bool', "default": False},
                    'dnac_api_task_timeout': {'type': 'int', "default": 1200},
                    'dnac_task_poll_interval': {'type': 'int', "default": 2},
                    'validate_response_schema': {'type': 'bool', 'default': True},
                    'config': {'required': True, 'type': 'list', 'elements': 'dict'},
                    'state': {'default': 'merged', 'choices': ['merged', 'deleted']}
                    }
    module = AnsibleModule(argument_spec=element_spec,
                           supports_check_mode=False)
    ccc_provision = Provision(module)
    config_verify = ccc_provision.params.get("config_verify")

    state = ccc_provision.params.get("state")
    if state not in ccc_provision.supported_states:
        ccc_provision.status = "invalid"
        ccc_provision.msg = "State {0} is invalid".format(state)
        ccc_provision.check_return_status()

    ccc_provision.validate_input(state=state).check_return_status()

    for config in ccc_provision.validated_config:
        ccc_provision.reset_values()
        ccc_provision.get_want().check_return_status()
        ccc_provision.get_diff_state_apply[state]().check_return_status()
        if config_verify:
            ccc_provision.verify_diff_state_apply[state]().check_return_status()

    module.exit_json(**ccc_provision.result)


if __name__ == '__main__':
    main()
