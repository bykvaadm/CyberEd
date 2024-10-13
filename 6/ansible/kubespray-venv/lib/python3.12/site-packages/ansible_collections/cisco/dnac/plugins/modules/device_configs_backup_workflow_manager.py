#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ("Abinash Mishra, Madhan Sankaranarayanan")

DOCUMENTATION = r"""
---
module: device_configs_backup_workflow_manager
short_description: Resource module for device_configs_backup functions
description:
- Manage operation related to taking the backup of running config, static config and vlan.dat.bat
version_added: '6.14.0'
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
    choices: [ merged ]
    default: merged
  config:
    description:
      - List of details regarding the device configuration backups being taken
      - Alteast one of the paramters mentioned in the suboptions must be passed in config
    type: list
    elements: dict
    required: true
    suboptions:
      hostname:
        description: Hostname of the device as displayed on the inventory GUI of Cisco Catalyst Center
        type: str
      management_ip_address:
        description: IP address of the device as displayed on the inventory GUI of Cisco Catalyst Center
        type: str
      site:
        description: Name of the site to which the device is assigned
        type: str
      mac_address:
        description: Mac address of the device as displayed on the inventory GUI of Cisco Catalyst Center
        type: str
      serial_number:
        description: Serial number of the device as displayed on the inventory GUI of Cisco Catalyst Center
        type: str
      family:
        description: Family of the device(s) as displayed on the inventory GUI of Cisco Catalyst Center
        type: str
      type:
        description: Specifies the type of the device(s) from the family, like Cisco Catalyst 9300 Switch or Cisco Catalyst 9500 Switch
        type: str
      series:
        description: Specifies the series of the device(s) from the type, like Cisco Catalyst 9300 Series Switches
        type: str
      collection_status:
        description: Specifies the collection status of the device(s) on the GUI of Cisco Catalyst Center
        type: str
      file_path:
        description:
            - Location of the path or folder where the configs need to be exported in local system.
            - If the file_path is not provided, the backup file(s) will be stored in a directory named
              "tmp" in the same directory as the playbook.
        type: str
        default: tmp
      file_password:
        description:
            - Optional file password for zipping and unzipping the config file.
            - Minimum password length is 8 and it should contain atleast one lower case letter, one uppercase
              letter, one digit and one special characters from -=\\\\\\\\;,./~!@$%^&*()_+{}[]|:?"
        type: str
requirements:
  - dnacentersdk == 2.6.10
  - python >= 3.5
notes:
  - SDK Methods used are devices.Devices.get_device_list,
    configuration_archive.ConfigurationsArchive.export_device_configurations,
    task.Task.get_task_by_id
  - Paths used are get /dna/intent/api/v1/network-device
    post dna/intent/api/v1/network-device-archive/cleartext
    get /dna/intent/api/v1/task/${taskId}

"""

EXAMPLES = r"""
- name: Take backup of a 9300 wired device
  cisco.dnac.device_configs_backup_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    dnac_log_level: "{{dnac_log_level}}"
    state: merged
    config:
        - hostname: NY-BN-9500.cisco.local
          management_ip_address: 205.1.1.4
          serial_number: F2AKI0082J
          family: Switches and Hubs
          type: Cisco Catalyst 9300 Switch
          series: Cisco Catalyst 9300 Series Switches
          collection_status: Managed
          file_path: /home/admin/madhan_ansible/collections/ansible_collections/cisco/dnac/playbooks/new_tmp

- name: Take backup of a 9300 wired device associated with site
  cisco.dnac.device_configs_backup_workflow_manager:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    dnac_log_level: "{{dnac_log_level}}"
    state: merged
    config:
        - site: Global/USA/New York/BLDNYC

"""

RETURN = r"""
# Case_1: Successful creation and exportation of device configs
response_1:
  description: A dictionary with  with the response returned by the Cisco Catalyst Center Python SDK
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

# Case_2: Error while taking a device_configs_backup
response_2:
  description: A string with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: list
  sample: >
    {
      "response": [],
      "msg": String
    }
"""
# common approach when a module relies on optional dependencies that are not available during the validation process.
try:
    import pyzipper
    HAS_PYZIPPER = True
except ImportError:
    HAS_PYZIPPER = False
    pyzipper = None

try:
    import pathlib
    HAS_PATHLIB = True
except ImportError:
    HAS_PATHLIB = False
    pathlib = None

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts
)
from io import BytesIO
import random
import string
import re
import time


class Device_configs_backup(DnacBase):

    """
    Class containing member attributes for device_configs_backup workflow_manager module
    """
    def __init__(self, module):
        super().__init__(module)

    def validate_input(self):
        """
        Validate the fields provided in the playbook.  Checks the
        configuration provided in the playbook against a predefined
        specification to ensure it adheres to the expected structure
        and data types.

        Parameters:
          - self: The instance of the class containing the 'config' attribute
                  to be validated.
        Returns:
          The method returns an instance of the class with updated attributes:
          - self.msg: A message describing the validation result.
          - self.status: The status of the validation (either 'success' or 'failed').
          - self.validated_config: If successful, a validated version of the
                                   'config' parameter.
        Example:
          To use this method, create an instance of the class and call
          'validate_input' on it.If the validation succeeds, 'self.status'
          will be 'success'and 'self.validated_config' will contain the
          validated configuration. If it fails, 'self.status' will be
          'failed', and 'self.msg' will describe the validation issues.
        """
        if HAS_PYZIPPER is False:
            msg = "Pyzipper is not installed. Please install it using 'pip install pyzipper' command"
            self.log(msg, "CRITICAL")
            self.module.fail_json(msg=msg)

        if HAS_PATHLIB is False:
            msg = "Pathlib is not installed. Please install it using 'pip install pathlib' command"
            self.log(msg, "CRITICAL")
            self.module.fail_json(msg=msg)

        if not self.config:
            self.msg = "config not available in playbook for validattion"
            self.status = "success"
            return self

        device_configs_backup_spec = {
            'hostname': {'type': 'str', 'required': False},
            'site': {'type': 'str', 'required': False},
            'management_ip_address': {'type': 'str', 'required': False},
            'mac_address': {'type': 'str', 'required': False},
            'serial_number': {'type': 'str', 'required': False},
            'family': {'type': 'str', 'required': False},
            'type': {'type': 'str', 'required': False},
            'series': {'type': 'str', 'required': False},
            'collection_status': {'type': 'str', 'required': False},
            'file_path': {'type': 'str', 'required': False, 'default': 'tmp'},
            'file_password': {'type': 'str', 'required': False}
        }
        # Validate device_configs_backup params
        valid_device_configs_backup, invalid_params = validate_list_of_dicts(
            self.config, device_configs_backup_spec
        )
        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(
                "\n".join(invalid_params))
            self.log(str(self.msg), "ERROR")
            self.status = "failed"
            return self

        self.validated_config = valid_device_configs_backup
        self.msg = "Successfully validated playbook configuration parameters using 'validate_input': {0}".format(str(valid_device_configs_backup))
        self.status = "success"
        return self

    def validate_ipv4_address(self):
        """
        Validates the management ip adress passed by the user
        """

        ip_address = self.validated_config[0].get("management_ip_address")

        if ip_address:
            if self.is_valid_ipv4(ip_address) is False:
                msg = "IP address {0} is not valid".format(ip_address)
                self.log(msg, "CRITICAL")
                self.module.fail_json(msg=msg)

        self.log("Validated IP address collected for config collection is {0}".format(ip_address), "INFO")

    def get_site_details(self, site_name_hierarchy):
        """
        Fetches the existance status of the site

        Parameters:
          - self: The instance of the class containing the 'config' attribute
                  to be validated.
          - site_name_hierarchy: Name of the site collected from the input.
        Returns:
          - site_exits: A boolean value indicating the existance of the site.
        Example:
            Post creation of the validated input, this method checks whther the site
            exists in the Cisco Catalyst Center or not
        """

        site_exists = False
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
            if len(site) == 1:
                site_exists = True
                self.log("Site Name: {0} exists in the Cisco Catalyst Center".format(site_name_hierarchy), "INFO")

        return site_exists

    def get_have(self):
        """
        Get the current device_configs_backup details
        Args:
            self: The instance of the class containing the 'config' attribute to be validated.
        Returns:
            The method returns an instance of the class with updated attributes:
                - self.
        Example:
            Stored paramters are used to call the APIs to store the validated configs
        """

        have = {}
        have = self.validated_config[0]
        self.have = have
        self.log("Parameters collected from get have api are {0}".format(self.have), "INFO")
        return self

    def get_device_ids_list(self):
        """
        Fetches the list of device ids from various paramters passed in the playbook
        Args:
            self: The instance of the class containing the 'config' attribute to be validated.
        Returns:
            device_ids: The list of device ids based on the parameters passed by the user
        Example:
            Stored paramters like management ip address/ family can be used to fetch the device ids
            list
        """

        device_params = self.validated_config[0]
        if device_params.get("file_password"):
            if len(device_params) - 1 == 0:
                msg = "Please provide atleast one device parameter as mentioned in the documentation to fetch device configs"
                self.log(msg, "CRITICAL")
                self.module.fail_json(msg=msg)

        response = self.dnac_apply['exec'](
            family="devices",
            function='get_device_list',
            params=device_params,
            op_modifies=True
        )
        self.log("Response collected from the API 'get_device_list' is {0}".format(str(response)), "DEBUG")
        device_list = response.get("response")
        self.log("Length of the device list fetched from the API 'get_device_list' is {0}".format(str(device_list)), "INFO")
        original_valid_device_count = len(device_list)
        if original_valid_device_count == 0:
            msg = "No devices found in the inventory matching the given parameters."
            self.log(msg, "CRITICAL")
            self.module.fail_json(msg=msg)

        valid_devices = []
        for device in device_list:
            ip_address = device.get("managementIpAddress")
            if device.get("collectionStatus") != "Managed":
                msg = "Device backup of device with IP address {0} \
                    is not possible due to collection status not being in Managed state".format(ip_address)
                self.log(msg, "WARNING")

            elif device.get("family") == "Unified AP":
                msg = "Device backup of device with IP address {0} \
                    is not possible due to device being an Unified AP".format(ip_address)
                self.log(msg, "WARNING")

            elif device.get("reachabilityStatus") != "Reachable":
                msg = "Device backup of device with IP address {0} \
                    is not possible due to device being not reachable".format(ip_address)
                self.log(msg, "WARNING")
            else:
                valid_devices.append(device)

        if not valid_devices:
            msg = "No device IDs were collected because the devices are either Unified APs \
                not in the Managed state, or not reachable."
            self.log(msg, "CRITICAL")
            self.module.fail_json(msg=msg)

        device_ids = [id.get("id") for id in valid_devices]
        valid_device_count = len(device_ids)
        self.log("Collected device IDs: {0}".format(device_ids), "INFO")
        self.log("Backup of {0} devices out of {1} devices is possible".format(valid_device_count, original_valid_device_count), "INFO")
        return device_ids

    def get_devices_by_site_and_params(self):
        """
        Retrieves a list of device IDs that match the given site and other parameters.
        Args:
            self: The instance of the class containing the 'config' attribute to be validated.
        Returns:
            device_in_site: List of device IDs that match the criteria and are located at the specified site.
        Example:
            Uses stored parameters like management IP address/family to fetch device IDs at the given site.
        """

        site = self.validated_config[0].get("site")
        device_ids = self.get_device_ids_list()
        devices_in_site = []

        for dev_id in device_ids:
            device_details_response = self.dnac_apply['exec'](
                family="devices",
                function='get_device_detail',
                params={"search_by": dev_id,
                        "identifier": "uuid"},
                op_modifies=True
            )
            self.log("Response collected from the API 'get_device_detail' {0}".format(device_details_response), "DEBUG")
            device_details = device_details_response.get("response")
            if device_details.get("location") == site:
                devices_in_site.append(dev_id)

        if not devices_in_site:
            msg = "No devices found in the given site {0}".format(site)
            self.log(msg, "CRITICAL")
            self.module.fail_json(msg=msg)

        return devices_in_site

    def get_device_ids_by_site(self):
        """
        Retrieves the list of device IDs at the specified site., when only site is passed as the parameter
        Args:
            self: The instance of the class containing the 'config' attribute to be validated.
        Returns:
            device_ids: The list of device ids present at the site passed by the user
        Example:
            Uses site as parameter to fetch the device IDs at the given site.
        """
        site = self.validated_config[0].get("site")
        response = self.dnac_apply['exec'](
            family="devices",
            function='get_device_list',
            op_modifies=True
        )
        self.log("Response collected from the API 'get_device_list' is {0}".format(str(response)), "DEBUG")
        device_list = response.get("response")
        self.log("Length of the device list fetched from the API 'get_device_list' is {0}".format(str(device_list)), "INFO")
        if len(device_list) == 0:
            msg = "No devices found in the inventory"
            self.log(msg, "CRITICAL")
            self.module.fail_json(msg=msg)

        device_ids = []
        for device in device_list:
            if device.get("site") == site:
                device_ids.append(device)

        self.log("Device IDs collected:{0}".format(device_ids), "INFO")
        return device_ids

    def password_generator(self):
        """
        Creates a password that matches Cisco Catalyst Center's requirements
        Min password length is 8 and it should contain atleast one lower case letter,
        one uppercase letter, one digit and one special characters from -=\\\\;,./~!@#$%^&*()_+{}[]|:?
        """

        punctuation = "-=;,.~!@#$%^&*()_+{}[]|:?"
        password_chars = punctuation + string.ascii_letters + string.digits
        password_list = [
            random.choice(punctuation),
            random.choice(string.ascii_uppercase),
            random.choice(string.ascii_lowercase),
            random.choice(string.digits),
            random.choice(password_chars),
            random.choice(password_chars),
            random.choice(password_chars),
            random.choice(password_chars),
        ]
        password = []
        while password_list:
            password.append(
                password_list.pop(random.randint(0, len(password_list) - 1))
            )
        password = "".join(password)

        self.log("File password is generated using the password generator API", "INFO")
        return password

    def validate_password(self, password=None):
        """
        Validates the user-defined password for Cisco catalyst Center's requirements
        Min password length is 8 and it should contain atleast one lower case letter,
        one uppercase letter, one digit and one special characters from -=\\\\;,./~!@#$%^&*()_+{}[]|:?
        """

        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[-=\\;,./~!@#$%^&*()_+{}[\]|:?\"]).{8,}$"
        self.log("User defined password is {0}".format(password), "DEBUG")
        if re.match(pattern, password):
            return True
        else:
            return False

    def get_want(self):
        """
        Get all device_configs_backup related informantion from the playbook and preprare it to call
        the API to export the device configurations.
        Args:
            self: The instance of the class containing the 'config' attribute to be validated.
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
        device_params = self.validated_config[0]
        site = device_params.get("site")
        filtered_keys = {}
        for key, value in device_params.items():
            if key not in ['file_path', 'file_password']:
                filtered_keys[key] = value

        if device_params.get("site") and self.get_site_details(site):
            if len(filtered_keys) > 1:
                self.want["deviceId"] = self.get_devices_by_site_and_params()
            else:
                self.want["deviceId"] = self.get_device_ids_by_site()
        else:
            self.want["deviceId"] = self.get_device_ids_list()

        self.log("Device IDs passed is {0}".format(self.want["deviceId"]), "INFO")

        if device_params.get("file_password"):
            password = device_params.get("file_password")
            if self.validate_password(password=password) is True:
                self.want["password"] = password

            else:
                msg = "Invalid input as Invalid password. Min password length is 8 and it should contain" + \
                    "atleast one lower case letter, one uppercase letter, one digit and one special characters" + \
                    "from -=\\\\\\\\;,./~!@#$%^&*()_+{}[]|:?"
                self.log(msg, "CRITICAL")
                self.module.fail_json(msg=msg)

        else:
            self.want["password"] = self.password_generator()

        self.msg = "Successfully collected all parameters from playbook " + \
            "for exceution"
        self.status = "success"
        self.log(self.msg, "INFO")
        return self

    def get_device_config(self):
        """
        Cisco Catalyst Center creates a ZIP file by calling the export API
        """

        response = self.dnac_apply['exec'](
            family="configuration_archive",
            function='export_device_configurations',
            params=self.want,
            op_modifies=True
        )
        response = response.get("response")

        self.log("Response collected from 'export_device_configurations' API is {0}".format(str(response)), "DEBUG")
        if response.get("errorCode"):
            msg = response.get("message")
            self.log(msg, "CRITICAL")
            self.module.fail_json(msg=msg)

        task_id = response.get("taskId")
        self.log("Task Id of the task is {0}".format(task_id), "INFO")
        return task_id

    def get_task_status(self, task_id=None):
        """
        Monitor the status of a task of creation of dicovery in the Cisco Catalyst Center.
        It checks the task status periodically until the task is no longer 'In Progress'
        or other states. If the task encounters an error or fails, it immediately fails the
        module and returns False.

        Parameters:
          - task_id: The ID of the task to monitor.

        Returns:
          - result: True if the task completed successfully, False otherwise.
                    With True it also returns additionalStatusURL
        """

        result = False
        params = dict(task_id=task_id)
        while True:
            response = self.dnac_apply['exec'](
                family="task",
                function='get_task_by_id',
                params=params,
                op_modifies=True,
            )
            response = response.response

            self.log("Response collected from 'get task by id' is {0}".format(response), "DEBUG")
            if response.get('isError') or re.search(
                'failed', response.get('progress'), flags=re.IGNORECASE
            ):
                msg = 'Device backup task with id {0} has not completed - Reason: {1}'.format(
                    task_id, response.get("failureReason"))
                self.log(msg, "CRITICAL")
                self.module.fail_json(msg=msg)
                return False

            self.log("Task status for the task id (before checking status) {0} is {1}".format(str(task_id), str(response)), "INFO")
            progress = response.get('progress')
            self.log("Progress of the task is {0}".format(str(progress)), "DEBUG")

            if progress == "Device configuration Successfully exported as password protected ZIP.":
                result = True
                additionalStatusURL = response.get("additionalStatusURL")
                self.log("The backup process is completed", "INFO")
                self.result.update(dict(backup_task=response))
                return (result, additionalStatusURL)

            self.log("The progress status is {0}, continue to check the status after 3 seconds. Putting into sleep for 3 seconds".format(progress), "INFO")
            time.sleep(3)

    def download_file(self, additionalStatusURL=None):
        """
        Downloading file and store locally
        Using unzip path settings for directory
        Paremetrs:
            self:  The instance of the class containing the 'config' attribute to be validated.
            additionalStatusURL: This paramter is used to fetch the file id

        Returns:
            - result: True if the file downloaded and uzipped, else False
        """

        self.log("Downloading: {0}".format(additionalStatusURL), "INFO")
        file_id = additionalStatusURL.split("/")[-1]

        try:
            response = self.dnac._exec(
                family="file",
                function='download_a_file_by_fileid',
                op_modifies=True,
                params={"file_id": file_id},
            )
            self.log("Received API response from 'download_a_file_by_fileid': {0}".format(str(response)), "DEBUG")
        except Exception as e:
            self.log("File couldn't be downloaded: {0}".format(e), "INFO")
            return False

        if isinstance(response, dict) and response.get("errorCode"):
            self.log(response.get("message"), "CRITICAL")
            self.module.fail_json(msg=response.get("message"))

        zip_data = BytesIO(response.data)
        self.log("ZIP data collected is {0}".format(zip_data), "INFO")

        pathlib.Path(self.have.get("file_path")).mkdir(parents=True, exist_ok=True)
        self.log("Unzipping file after completion of download", "INFO")

        try:
            with pyzipper.AESZipFile(zip_data, 'r') as f:
                f.pwd = bytes(self.want.get("password"), encoding="utf-8")
                f.extractall(path=str(self.have.get("file_path")))
        except Exception as e:
            self.log("Error in unzipping: {0}".format(e), "CRITICAL")
            return False

        self.log("Unzipping complete", "INFO")
        return True

    def get_diff_merged(self):
        """
        Add to device_configs_backup database
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

        if self.have.get('management_ip_address'):
            self.validate_ipv4_address()

        task_id = self.get_device_config()
        result, additionalStatusURL = self.get_task_status(task_id=task_id)

        if result is True:
            download_status = self.download_file(additionalStatusURL=additionalStatusURL)
            if download_status is True:
                self.result['response'] = task_id
                self.result['msg'] = "Device configs got downloaded"
                self.log(self.result['msg'], "INFO")
                self.result['changed'] = True
                return self
        return self

    def verify_diff_merged(self):
        """
        Verify the merged status(Creation/Updation) of Discovery in Cisco Catalyst Center.
        Args:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Return:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            This method checks the merged status of a configuration in Cisco Catalyst Center by
            retrieving the current state (have) and desired state (want) of the configuration,
            logs the states, and validates whether the specified device(s) exists in the DNA
            Center configuration's Discovery Database.
        """

        self.log("Current State (have): {0}".format(str(self.have)), "INFO")
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")
        # Code to validate Cisco Catalyst Center config for merged state
        window_seconds = 10
        current_time = time.time()
        window_start_time = current_time - window_seconds
        files_modified_within_window = [
            f.name for f in pathlib.Path(self.have.get("file_path")).iterdir()
            if f.stat().st_mtime > window_start_time
        ]

        if len(files_modified_within_window) > 0:
            self.log("Backup has been taken in the following files {0}".format(str(files_modified_within_window)), "INFO")
        else:
            self.log("Backup has not been taken, please check", "WARNING")

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
                    'state': {'default': 'merged', 'choices': ['merged']}
                    }
    module = AnsibleModule(argument_spec=element_spec,
                           supports_check_mode=False)
    ccc_device_configs_backup = Device_configs_backup(module)

    state = ccc_device_configs_backup.params.get("state")
    if state not in ccc_device_configs_backup.supported_states:
        ccc_device_configs_backup.status = "invalid"
        ccc_device_configs_backup.msg = "State {0} is invalid".format(state)
        ccc_device_configs_backup.check_return_status()

    config_verify = ccc_device_configs_backup.params.get("config_verify")
    ccc_device_configs_backup.validate_input().check_return_status()

    for config in ccc_device_configs_backup.validated_config:
        ccc_device_configs_backup.reset_values()
        ccc_device_configs_backup.get_have().check_return_status()
        ccc_device_configs_backup.get_want().check_return_status()
        ccc_device_configs_backup.get_diff_state_apply[state]().check_return_status()
        if config_verify:
            ccc_device_configs_backup.verify_diff_state_apply[state]().check_return_status()

    module.exit_json(**ccc_device_configs_backup.result)


if __name__ == '__main__':
    main()
