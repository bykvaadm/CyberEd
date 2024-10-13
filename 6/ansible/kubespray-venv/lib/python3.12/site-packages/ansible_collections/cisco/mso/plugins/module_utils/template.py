# -*- coding: utf-8 -*-

# Copyright: (c) 2022, Akini Ross (@akinross) <akinross@cisco.com>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.cisco.mso.plugins.module_utils.constants import TEMPLATE_TYPES
from collections import namedtuple

KVPair = namedtuple("KVPair", "key value")
Item = namedtuple("Item", "index details")
SearchQuery = namedtuple("SearchQuery", "key kv_pairs")


class MSOTemplate:
    def __init__(self, mso_module, template_type=None, template_name=None, template_id=None):
        self.mso = mso_module
        self.templates_path = "templates"
        self.summaries_path = "{0}/summaries".format(self.templates_path)
        self.template = {}
        self.template_path = ""
        self.template_name = template_name
        self.template_id = template_id

        if template_id:
            # Checking if the template with id exists to avoid error: MSO Error 400: Template ID 665da24b95400f375928f195 invalid
            template_summary = self.mso.get_obj(self.summaries_path, templateId=self.template_id)
            if template_summary:
                self.template_path = "{0}/{1}".format(self.templates_path, self.template_id)
                self.template = self.mso.query_obj(self.template_path)
            else:
                self.mso.fail_json(
                    msg="Provided template id '{0}' does not exist. Existing templates: {1}".format(
                        self.template_id,
                        [
                            "Template '{0}' with id '{1}'".format(template.get("templateName"), template.get("templateId"))
                            for template in self.mso.query_objs(self.summaries_path)
                        ],
                    )
                )
        elif template_name:
            if not template_type:
                self.mso.fail_json(msg="Template type must be provided when using template name.")
            template_summary = self.mso.get_obj(
                self.summaries_path, templateName=self.template_name, templateType=TEMPLATE_TYPES[template_type]["template_type"]
            )
            if template_summary:
                self.template_path = "{0}/{1}".format(self.templates_path, template_summary.get("templateId"))
                self.template = self.mso.query_obj(self.template_path)
        elif template_type:
            self.template = self.mso.query_objs(self.summaries_path, templateType=TEMPLATE_TYPES[template_type]["template_type"])
        else:
            self.template = self.mso.query_objs(self.summaries_path)

        # Remove unwanted keys from existing object for better output and diff compares
        if isinstance(self.template, dict):
            for key in ["_updateVersion", "version"]:
                self.template.pop(key, None)

    @staticmethod
    def get_object_from_list(search_list, kv_list):
        """
        Get the first matched object from a list of mso object dictionaries.
        :param search_list: Objects to search through -> List.
        :param kv_list: Key/value pairs that should match in the object. -> List[KVPair(Str, Str)]
        :return: The index and details of the object. -> Item (Named Tuple)
                 Values of provided keys of all existing objects. -> List
        """

        def kv_match(kvs, item):
            return all((item.get(kv.key) == kv.value for kv in kvs))

        match = next((Item(index, item) for index, item in enumerate(search_list) if kv_match(kv_list, item)), None)
        existing = [item.get(kv.key) for item in search_list for kv in kv_list]
        return match, existing

    def validate_template(self, template_type):
        """
        Validate that attributes are set to a value that is not equal None.
        :return: None
        """
        if not self.template or not isinstance(self.template, dict):
            self.mso.fail_json(msg="Template '{0}' not found.".format(self.template_name))
        if self.template.get("templateType") != template_type:
            self.mso.fail_json(msg="Template type must be '{0}'.".format(template_type))

    def get_object_by_key_value_pairs(self, object_description, search_list, kv_list, fail_module=False):
        """
        Get the object from a list of mso object dictionaries by name.
        :param object_description: Description of the object to search for -> Str
        :param search_list: Objects to search through -> List.
        :param kv_list: Key/value pairs that should match in the object. -> List[KVPair(Str, Str)]
        :param fail_module: When match is not found fail the ansible module. -> Bool
        :return: The object. -> Dict | None
        """
        match, existing = self.get_object_from_list(search_list, kv_list)
        if not match and fail_module:
            msg = "Provided {0} with '{1}' not matching existing object(s): {2}".format(object_description, kv_list, ", ".join(existing))
            self.mso.fail_json(msg=msg)
        return match

    def get_object_by_uuid(self, object_description, search_list, uuid, fail_module=False):
        """
        Get the object from a list of mso object dictionaries by uuid.
        :param object_description: Description of the object to search for -> Str
        :param search_list: Objects to search through -> List.
        :param uuid: UUID of the object to search for -> Str
        :param fail_module: When match is not found fail the ansible module. -> Bool
        :return: The object. -> Dict | None
        """
        kv_list = [KVPair("uuid", uuid)]
        return self.get_object_by_key_value_pairs(object_description, search_list, kv_list, fail_module)

    def get_vlan_pool_uuid(self, vlan_pool_name):
        """
        Get the UUID of a VLAN pool by name.
        :param vlan_pool_name: Name of the VLAN pool to search for -> Str
        :return: UUID of the VLAN pool. -> Str
        """
        existing_vlan_pools = self.template.get("fabricPolicyTemplate", {}).get("template", {}).get("vlanPools", [])
        kv_list = [KVPair("name", vlan_pool_name)]
        match = self.get_object_by_key_value_pairs("VLAN Pool", existing_vlan_pools, kv_list, fail_module=True)
        return match.details.get("uuid")

    def get_vlan_pool_name(self, vlan_pool_uuid):
        """
        Get the UUID of a VLAN pool by name.
        :param vlan_pool_name: Name of the VLAN pool to search for -> Str
        :return: UUID of the VLAN pool. -> Str
        """
        existing_vlan_pools = self.template.get("fabricPolicyTemplate", {}).get("template", {}).get("vlanPools", [])
        kv_list = [KVPair("uuid", vlan_pool_uuid)]
        match = self.get_object_by_key_value_pairs("VLAN Pool", existing_vlan_pools, kv_list, fail_module=True)
        return match.details.get("name")
