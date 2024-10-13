# This code is part of Ansible, but is an independent component.
# This particular file snippet, and this file snippet only, is BSD licensed.
# Modules you write using this snippet, which is embedded dynamically by Ansible
# still belong to the author of the module, and may assign their own license
# to the complete work.
#
# (c) 2020-2021 Fortinet, Inc
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright notice,
#      this list of conditions and the following disclaimer in the documentation
#      and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE
# USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
from __future__ import absolute_import, division, print_function

__metaclass__ = type
from ansible.module_utils.basic import _load_params
import datetime
import re

from ansible.module_utils.six import raise_from

try:
    import yaml
except ImportError as imp_exc:
    YAML_IMPORT_ERROR = imp_exc
else:
    YAML_IMPORT_ERROR = None


def check_galaxy_version(schema):
    params = _load_params()
    if not params:
        return
    params_keys = list(params.keys())
    if "method" in params_keys and "method" not in schema:
        error_message = "Legacy playbook detected, please revise the playbook or install latest legacy"
        error_message += " fortimanager galaxy collection: #ansible-galaxy collection install -f fortinet.fortimanager:1.0.5"
        raise Exception(error_message)


def get_bypass(params):
    bypass = params.get("bypass_validation", False)
    if isinstance(bypass, bool):
        return bypass
    elif isinstance(bypass, str):
        return bypass.lower() in ["true", "y", "yes", "t", "1", "on"]
    elif isinstance(bypass, int):
        return bypass != 0
    return True


def check_parameter_bypass(schema, module_level2_name):
    schema = modify_argument_spec(schema)
    params = _load_params()
    if not params:
        return schema
    is_bypass = get_bypass(params)  # This params are raw data, need to decide bypass manually.
    if is_bypass:
        top_level_schema = dict()
        for key in schema:
            if key != module_level2_name:
                top_level_schema[key] = schema[key]
            elif (
                not params[module_level2_name]
                or isinstance(params[module_level2_name], dict)
            ):
                top_level_schema[module_level2_name] = {"type": "dict"}
            elif isinstance(params[module_level2_name], list):
                top_level_schema[module_level2_name] = {"type": "list"}
        return top_level_schema
    return schema


def modify_argument_spec(schema):
    if not isinstance(schema, dict):
        return schema
    new_schema = {}
    rename_arg = {"message": "fmgr_message",
                  "syslog-facility": "fmgr_syslog_facility",
                  "80211d": "d80211d",
                  "80211k": "d80211k",
                  "80211v": "d80211v",
                  "80211mc": "d80211mc"}
    for param_name in schema:
        if param_name != "v_range" and param_name != "api_name":
            new_content = modify_argument_spec(schema[param_name])
            aliase_name = _get_modified_name(param_name)
            if param_name in rename_arg:
                new_content["removed_in_version"] = "3.0.0"
                new_content["removed_from_collection"] = "fortinet.fortimanager"
                new_content["aliases"] = [rename_arg[param_name]]
            elif aliase_name != param_name:
                new_content["removed_in_version"] = "3.0.0"
                new_content["removed_from_collection"] = "fortinet.fortimanager"
                if aliase_name not in new_schema and "api_name" not in schema[param_name]:
                    new_content["aliases"] = [aliase_name]
            new_schema[param_name] = new_content
    return new_schema


def _get_modified_name(variable_name):
    modified_name = variable_name
    for special_char in ["-", " ", ".", "(", "+"]:
        modified_name = modified_name.replace(special_char, "_")
    return modified_name


def remove_aliases(user_params, metadata, bypass_valid=False):
    if not user_params:
        return user_params
    if isinstance(user_params, str) or isinstance(user_params, int):
        return user_params
    if isinstance(user_params, list):
        new_params = []
        for item in user_params:
            new_params.append(remove_aliases(item, metadata, bypass_valid))
        return new_params
    replace_key = {"fmgr_message": "message",
                   "fmgr_syslog_facility": "syslog-facility",
                   "d80211d": "80211d",
                   "d80211k": "80211k",
                   "d80211v": "80211v",
                   "d80211mc": "80211mc"}
    new_params = {}
    considered_keys = set()
    for param_name, param_data in metadata.items():
        ansible_format_param_name = _get_modified_name(param_name)
        considered_keys.add(param_name)
        considered_keys.add(ansible_format_param_name)
        user_data = user_params.get(param_name, None)
        if user_data is None:
            user_data = user_params.get(ansible_format_param_name, None)
        if user_data is None:
            continue
        fmg_api_param_name = replace_key.get(param_name, param_name)
        if "options" in param_data:
            new_params[fmg_api_param_name] = remove_aliases(user_data, param_data["options"], bypass_valid)
        else:
            new_params[fmg_api_param_name] = user_data
    if bypass_valid:
        for param_name, param_data in user_params.items():
            if param_name not in considered_keys:
                new_params[param_name] = param_data
    return new_params


class NAPIManager(object):
    jrpc_urls = None
    perobject_jrpc_urls = None
    module_primary_key = None
    url_params = None
    module = None
    conn = None
    module_name = None
    module_level2_name = None
    top_level_schema_name = None
    module_arg_spec = None

    def __init__(self, jrpc_urls, perobject_jrpc_urls, module_primary_key,
                 url_params, module, conn, top_level_schema_name=None):
        self.jrpc_urls = jrpc_urls
        self.perobject_jrpc_urls = perobject_jrpc_urls
        self.module_primary_key = module_primary_key
        self.url_params = url_params
        self.module = module
        self.conn = conn
        self.process_workspace_lock()
        self.module_name = self.module._name
        self.module_level2_name = self.module_name.split(".")[-1][5:]
        self.top_level_schema_name = top_level_schema_name
        self._set_connection_options()
        self.system_status = self.get_system_status()
        self.version_check_warnings = list()
        self._nr_exported_playbooks = 0
        self._nr_valid_selectors = 0
        self.metadata = {}

        if YAML_IMPORT_ERROR:
            raise_from(
                Exception("YAML must be installed to use this plugin"),
                YAML_IMPORT_ERROR,
            )

    def _set_connection_options(self):
        for key in ['access_token', 'enable_log', 'forticloud_access_token']:
            if key in self.module.params:
                self.conn.set_customer_option(key, self.module.params[key])

    def process_workspace_lock(self):
        self.conn.process_workspace_locking(self.module.params)

    def is_force_update(self):
        return (
            "proposed_method" in self.module.params
            and self.module.params["proposed_method"]
        )

    def get_propose_method(self, default_method):
        if (
            "proposed_method" in self.module.params
            and self.module.params["proposed_method"]
        ):
            return self.module.params["proposed_method"]
        return default_method

    def get_params_in_url(self, s):
        '''Find contents in {}'''
        pattern = r'\{(.*?)\}'
        result = re.findall(pattern, s)
        return result

    def _version_matched(self, v_ranges):
        if not v_ranges or not self.system_status:
            # if system version is not determined, give up version checking
            return True, None

        sys_version_value = (
            int(self.system_status["Major"]) * 10000
            + int(self.system_status["Minor"]) * 100
            + int(self.system_status["Patch"])
        )
        b_match = False
        for vr in v_ranges:
            min_v = vr[0].split(".")
            min_vn = (
                int(min_v[0]) * 10000
                + int(min_v[1]) * 100
                + int(min_v[2])
            )
            if min_vn > sys_version_value:
                break
            if vr[1] == "":  # Empty string means no max version
                b_match = True
                break
            max_v = vr[1].split(".")
            max_vn = (
                int(max_v[0]) * 10000
                + int(max_v[1]) * 100
                + int(max_v[2])
            )
            if max_vn >= sys_version_value:
                b_match = True
                break
        if b_match:
            return True, None
        supported_v = []
        for vr in v_ranges:
            if vr[1] == "":
                vr_s = ">= %s" % (vr[0])
            else:
                vr_s = "%s-%s" % (vr[0], (vr[1]))
            supported_v.append(vr_s)
        return (
            False,
            "Current FortiManager version %s.%s.%s do not support this feature. Supported version range: %s."
            % (self.system_status["Major"], self.system_status["Minor"], self.system_status["Patch"], supported_v),
        )

    def _get_basic_url(self, is_perobject):
        url_libs = [""]
        if is_perobject:
            url_libs = self.perobject_jrpc_urls
        else:
            url_libs = self.jrpc_urls
        the_url = None
        if "adom" in self.url_params and not url_libs[0].endswith("{adom}"):
            adom = self.module.params["adom"]
            if adom == "global":
                for url in url_libs:
                    if "/global/" in url and "/adom/{adom}" not in url:
                        the_url = url
                        break
                if not the_url:
                    self.module.fail_json(msg="No global url for the request, please use other adom.")
            else:
                for url in url_libs:
                    if "/adom/{adom}" in url:
                        the_url = url
                        break
                if not the_url:
                    self.module.fail_json(msg="No url for the requested adom:%s, please use other adom." % (adom))
        else:
            the_url = url_libs[0]
        if not the_url:
            self.module.fail_json(msg="Can't find target url, please check param: adom")
        return self._get_replaced_url(the_url)

    def _get_replaced_url(self, url_template):
        target_url = url_template
        for param in self.url_params:
            token_hint = "{%s}" % (param)
            token = ""
            modified_name = _get_modified_name(param)
            modified_token = self.module.params.get(modified_name, None)
            previous_token = self.module.params.get(param, None)
            if modified_token is not None:
                token = modified_token
            elif previous_token is not None:
                token = previous_token
            else:
                self.module.fail_json(msg="Missing input param: %s" % (modified_name))
            target_url = target_url.replace(token_hint, "%s" % (token))
        return target_url

    def _get_base_perobject_url(self, mvalue):
        url_getting = self._get_basic_url(True)
        if not url_getting.endswith("}"):
            # in case of non-regular per-object url, such as scope member.
            return url_getting
        last_token = url_getting.split("/")[-1]
        return url_getting.replace(last_token, str(mvalue))

    def get_object(self, mvalue):
        url_getting = self._get_base_perobject_url(mvalue)
        params = [{"url": url_getting}]
        response = self.conn.send_request("get", params)
        return response

    def update_object(self, mvalue):
        url_updating = self._get_base_perobject_url(mvalue)
        bypass_valid = self.module.params.get("bypass_validation", False) is True
        raw_attributes = remove_aliases(self.module.params, self.metadata, bypass_valid)
        raw_attributes = raw_attributes.get(self.module_level2_name, {})
        params = {
            "url": url_updating,
            self.top_level_schema_name: raw_attributes,
        }
        if self.module.check_mode:
            self.do_check_exit(True)
        response = self.conn.send_request(self.get_propose_method("update"), [params])
        return response

    def create_object(self):
        url_creating = self._get_basic_url(False)
        bypass_valid = self.module.params.get("bypass_validation", False) is True
        raw_attributes = remove_aliases(self.module.params, self.metadata, bypass_valid)
        raw_attributes = raw_attributes.get(self.module_level2_name, {})
        params = {
            "url": url_creating,
            self.top_level_schema_name: raw_attributes,
        }
        if self.module.check_mode:
            self.do_check_exit(True)
        return self.conn.send_request(self.get_propose_method("set"), [params])

    def delete_object(self, mvalue):
        url_deleting = self._get_base_perobject_url(mvalue)
        params = [{"url": url_deleting}]
        if self.module.check_mode:
            self.do_check_exit(True)
        return self.conn.send_request("delete", params)

    def get_system_status(self):
        params = [{"url": "/cli/global/system/status"}]
        response = self.conn.send_request("get", params)
        if response[0] == 0:
            if "data" not in response[1]:
                raise AssertionError("Error when getting system status")
            return response[1]["data"]
        return None

    def is_same_subnet(self, object_remote, object_present):
        if isinstance(object_remote, list) and len(object_remote) != 2:
            return False
        tokens = object_present.split("/")
        if len(tokens) != 2:
            return False
        try:
            subnet_number = int(tokens[1])
            if subnet_number < 0 or subnet_number > 32:
                return False
            remote_subnet_number = sum(bin(int(x)).count("1") for x in object_remote[1].split("."))
            if object_remote[0] == tokens[0] and remote_subnet_number == subnet_number:
                return True
        except Exception as e:
            return False
        return False

    def is_object_difference(self, remote_obj, local_obj):
        for key in local_obj:
            local_value = local_obj[key]
            if local_value is None:
                continue
            remote_value = remote_obj.get(key, None)
            if remote_value is None:
                return True
            if isinstance(local_value, list):
                try:
                    if isinstance(remote_value, list):
                        if str(sorted(remote_value)) == str(sorted(local_value)):
                            continue
                    # Won't update if remote = 'var' and local = ['var']
                    elif len(local_value) == 1:
                        if str(remote_value) == str(local_value[0]):
                            continue
                except Exception as e:
                    return True
                return True
            elif isinstance(local_value, dict):
                if not isinstance(remote_value, dict):
                    return True
                elif self.is_object_difference(remote_value, local_value):
                    return True
            else:  # local_value is not list or dict, maybe int, float or str
                value_string = str(local_value)
                if isinstance(remote_value, list):  # e.g., subnet
                    if self.is_same_subnet(remote_value, value_string):
                        continue
                    # Won't update if remote = ['var'] and local = 'var'
                    elif len(remote_value) != 1 or str(remote_value[0]) != value_string:
                        return True
                elif str(remote_value) != value_string:
                    return True
        return False

    def _update_required(self, robject):
        object_remote = robject["data"] if "data" in robject else {}
        bypass_valid = self.module.params.get("bypass_validation", False)
        object_present = remove_aliases(self.module.params, self.metadata, bypass_valid)
        object_present = object_present.get(self.module_level2_name, {})
        return self.is_object_difference(object_remote, object_present)

    def _process_with_mkey(self, mvalue):
        if self.module.params["state"] == "present":
            rc, robject = self.get_object(mvalue)
            if rc == 0:
                if self.is_force_update() or self._update_required(robject):
                    return self.update_object(mvalue)
                else:
                    return_msg = "Your FortiManager is already up to date and does not need to be updated. "
                    return_msg += "To force update, please add argument proposed_method:update"
                    if self.module.check_mode:
                        self.do_check_exit(False, message=return_msg)
                    self.module.exit_json(message=return_msg)
            else:
                return self.create_object()
        elif self.module.params["state"] == "absent":
            # in case the `GET` method returns nothing... see module `fmgr_antivirus_mmschecksum`
            return self.delete_object(mvalue)

    def _process_without_mkey(self):
        if self.module.params["state"] == "absent":
            self.module.fail_json(msg="This module doesn't not support state:absent yet.")
        return self.create_object()

    def process_generic(self, method, param):
        response = self.conn.send_request(method, param)
        self.do_exit(response)

    def process_exec(self, argument_specs=None):
        self.metadata = argument_specs
        params = self.module.params
        module_name = self.module_level2_name
        track = [module_name]
        bypass_valid = params.get("bypass_validation", False)
        if not bypass_valid:
            self.check_versioning_mismatch(track, argument_specs.get(module_name, None), params.get(module_name, None))
        adom_value = params.get("adom", None)
        target_url = self._get_target_url(adom_value, self.jrpc_urls)
        target_url = self._get_replaced_url(target_url)
        api_params = {"url": target_url}
        if module_name in params:
            params = remove_aliases(params, argument_specs, bypass_valid)
            api_params[self.top_level_schema_name] = params[module_name]
        if self.module.check_mode:
            self.do_check_exit(True)
        response = self.conn.send_request("exec", [api_params])
        self.do_exit(response)

    def process_task(self, metadata, task_type):
        params = self.module.params
        selector = params[task_type]["selector"]
        param_url_id = "params" if task_type == "facts" else "self"
        specified_url_param = params[task_type][param_url_id]
        specified_url_param = specified_url_param if specified_url_param else {}
        param_target = params[task_type].get("target", {})
        param_target = param_target if param_target else {}
        mkey = metadata[selector].get("mkey", None)
        if mkey and not mkey.startswith("complex:") and mkey not in param_target:
            modified_mkey = _get_modified_name(mkey)
            if modified_mkey in param_target:
                param_target[mkey] = param_target[modified_mkey]
                del param_target[modified_mkey]
            else:
                self.module.fail_json(msg="Must give the primary key/value in target: %s!" % (mkey))
        vrange = metadata[selector].get("v_range", None)
        matched, checking_message = self._version_matched(vrange)
        if not matched:
            self.version_check_warnings.append("selector:%s %s" % (selector, checking_message))
        # Get target URL
        param_map = {}
        specified_params = set()
        for param_name in metadata[selector]["params"]:
            modified_name = _get_modified_name(param_name)
            if modified_name in specified_url_param:
                param_map[param_name] = modified_name
                specified_params.add(param_name)
            elif param_name in specified_url_param:
                param_map[param_name] = param_name
                specified_params.add(param_name)
        url_with_specified_param = []
        unique_url_params = []
        for possible_url in metadata[selector]["urls"]:
            url_params = set(self.get_params_in_url(possible_url))
            if "adom" in metadata[selector]["params"]:
                url_params.add("adom")
            if specified_params == url_params:
                url_with_specified_param.append(possible_url)
            if url_params not in unique_url_params:
                unique_url_params.append(url_params)
        if len(url_with_specified_param) == 0:
            error_message = 'Expect required params: '
            for i, url_params in enumerate(unique_url_params):
                if i:
                    error_message += ', or '
                error_message += '%s' % ([_get_modified_name(key) for key in url_params])
            self.module.fail_json(msg=error_message)
        adom_value = specified_url_param.get("adom", None)
        target_url = self._get_target_url(adom_value, url_with_specified_param)
        for param in param_map:
            token_hint = "{%s}" % (param)
            user_param_name = param_map[param]
            token = "%s" % (specified_url_param[user_param_name]) if specified_url_param[user_param_name] else ""
            target_url = target_url.replace(token_hint, token)
        # Send data
        request_type = {"clone": "clone", "rename": "update",
                        "move": "move", "facts": "get"}
        api_params = {"url": target_url}
        if task_type in ["clone", "rename"]:
            api_params["data"] = param_target
        elif task_type == "move":
            api_params["option"] = params[task_type]["action"]
            api_params["target"] = param_target
        elif task_type == "facts":
            fact_params = params["facts"]
            for key in ["filter", "sortings", "fields", "option"]:
                if fact_params.get(key, None):
                    api_params[key] = fact_params[key]
            if fact_params.get("extra_params", None):
                for key in fact_params["extra_params"]:
                    api_params[key] = fact_params["extra_params"][key]
        if self.module.check_mode:
            if task_type in ["clone", "rename", "move"]:
                self.do_check_exit(True)
        response = self.conn.send_request(request_type[task_type], [api_params])
        self.do_exit(response, changed=(task_type != "facts"))

    def __fix_remote_object_internal(self, robject, module_schema, log):
        if not isinstance(robject, dict):
            return True
        need_bypass = False
        keys_to_delete = list()
        for key in robject:
            value = robject[key]
            # keys are internal in FMG devices.
            if key not in module_schema:
                keys_to_delete.append(key)
                continue
            # key is found
            attr_schema = module_schema[key]
            attr_type = attr_schema["type"]
            if attr_type in ["str", "int"]:
                # Do immediate fix.
                if isinstance(value, list):
                    if len(value) == 1:
                        robject[key] = value[0]
                        log.write("\tfix list-to-atomic key:%s\n" % (key))
                    else:
                        need_bypass = True
                elif isinstance(value, dict):
                    need_bypass = True
                if not value or value == "null":
                    log.write("\tdelete empty key:%s\n" % (key))
                    keys_to_delete.append(key)
            elif attr_type == "dict":
                if "options" in attr_schema and isinstance(value, dict):
                    need_bypass |= self.__fix_remote_object_internal(
                        value, attr_schema["options"], log
                    )
                else:
                    need_bypass = True
                if not value or value == "null":
                    log.write("\tdelete empty key:%s\n" % (key))
                    keys_to_delete.append(key)
            elif attr_type == "list":
                if "options" in attr_schema and isinstance(value, list):
                    for sub_value in value:
                        need_bypass |= self.__fix_remote_object_internal(
                            sub_value, attr_schema["options"], log
                        )
                else:
                    need_bypass = True
                if (
                    isinstance(value, list)
                    and not len(value)
                    or value == "null"
                    or not value
                ):
                    log.write("\tdelete empty key:%s\n" % (key))
                    keys_to_delete.append(key)
            else:
                continue
        for key in keys_to_delete:
            log.write("\tdelete unrecognized key:%s\n" % (key))
            del robject[key]
        return need_bypass

    def __append_whiteblank_per_line(self, blob, num_of_blank):
        ret = " " * num_of_blank
        ret += blob.replace("\n", "\n%s" % (" " * num_of_blank))
        return ret

    def _generate_playbook(self, counter, export_path, selector, robject, state_present,
                           need_bypass, url_params, params_schema, log):
        prefix_text = """- name: Exported Playbook
  hosts: fortimanagers
  connection: httpapi
  collections:
    - fortinet.fortimanager
  vars:
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_httpapi_port: 443
  tasks:
"""
        with open("%s/%s_%s.yml" % (export_path, selector, counter), "w") as f:
            f.write(prefix_text)
            f.write("  - name: exported config for %s\n" % (selector))
            f.write("    fmgr_%s:\n" % (selector))
            if need_bypass:
                f.write("      bypass_validation: true\n")
            if state_present:
                f.write("      state: present\n")
            for url_param_key in params_schema:
                if url_param_key not in url_params:
                    continue
                url_param_value = url_params[url_param_key]
                f.write("      %s: %s\n" % (url_param_key, url_param_value))
            f.write("      %s:\n" % (selector))
            f.write(self.__append_whiteblank_per_line(yaml.dump(robject), 8))
        log.write(
            "\texported playbook: %s/%s_%s.yml\n" % (export_path, selector, counter)
        )
        self._nr_exported_playbooks += 1

    def _process_export_response(self, selector, response, schema_invt, log,
                                 export_path, url_params, params_schema):
        response_code = response[0]
        response_data = response[1]
        if response_code != 0 or "data" not in response_data:
            log.write("\tno configuration data found\n")
            return
        if selector not in schema_invt:
            log.write("\trequested object has no corresponding ansible module\n")
            return
        state_present = schema_invt[selector]["stated"]
        module_schema = schema_invt[selector]["options"]
        remote_objects = response_data["data"]
        counter = 0
        if isinstance(remote_objects, list):
            for remote_object in remote_objects:
                need_bypass = self.__fix_remote_object_internal(remote_object, module_schema, log)
                self._generate_playbook(counter, export_path, selector, remote_object,
                                        state_present, need_bypass, url_params, params_schema, log)
                counter += 1
        elif isinstance(remote_objects, dict):
            need_bypass = self.__fix_remote_object_internal(remote_objects, module_schema, log)
            self._generate_playbook(counter, export_path, selector, remote_objects, state_present,
                                    need_bypass, url_params, params_schema, log)
            counter += 1
        if not counter:
            self._nr_valid_selectors += 1

    def _process_export_per_selector(self, selector, schema, param, log, export_path, process, schema_invt):
        # make urls from schema and parameters provided.
        url = None
        export_urls = schema["urls"]
        if "adom" in param and not export_urls[0].endswith("{adom}"):
            if param["adom"] == "global":
                for _url in export_urls:
                    if "/global/" in _url and "/adom/{adom}/" not in _url:
                        url = _url
                        break
            else:
                for _url in export_urls:
                    if "/adom/{adom}/" in _url:
                        url = _url
                        break
        if not url:
            url = export_urls[0]
        _param_applied = list()
        for _param_key in param:
            _param_value = param[_param_key]
            if _param_key == "adom" and _param_value.lower() == "global":
                continue
            token_hint = "/%s/{%s}" % (_param_key, _param_key)
            token = "/%s/%s" % (_param_key, _param_value)
            if token_hint in url:
                _param_applied.append(_param_key)
            url = url.replace(token_hint, token)
        for _param_key in param:
            if _param_key in _param_applied:
                continue
            if _param_key == "adom" and _param_value.lower() == "global":
                continue
            token_hint = "{%s}" % (_param_key)
            token = param[_param_key]
            url = url.replace(token_hint, token)
        tokens = url.split("/")
        if tokens[-1].startswith("{") and tokens[-1].endswith("}"):
            new_url = ""
            for token in tokens[:-1]:
                new_url += "/%s" % (token)
            new_url = new_url.replace("//", "/")
            url = new_url
        unresolved_parameter = False
        tokens = url.split("/")
        for token in tokens:
            if token.startswith("{") and token.endswith("}"):
                unresolved_parameter = True
                break
        log.write("[%s]exporting: %s\n" % (process, selector))
        log.write("\turl: %s\n" % (url))
        if unresolved_parameter:
            log.write("\t unknown parameter, skipped!\n")
            return
        response = self.conn.send_request("get", [{"url": url}])
        self._process_export_response(selector, response, schema_invt, log, export_path, param, schema["params"])

    def process_export(self, metadata):
        from ansible_collections.fortinet.fortimanager.plugins.module_utils.exported_schema import (
            schemas as exported_schema_inventory,
        )
        params = self.module.params
        export_selectors = params["export_playbooks"]["selector"]
        export_path = "./"
        if params["export_playbooks"].get("path", None):
            export_path = params["export_playbooks"]["path"]
        log = open("%s/export.log" % (export_path), "w")
        log.write("Export time: %s\n" % (str(datetime.datetime.now())))
        # Check required parameter.
        for selector in export_selectors:
            if selector == "all":
                continue
            export_meta = metadata[selector]
            export_meta_param = export_meta["params"]
            export_meta_urls = export_meta["urls"]
            if (
                not params["export_playbooks"]["params"]
                or selector not in params["export_playbooks"]["params"]
            ):
                self.module.fail_json("parameter export_playbooks->params needs entry:%s" % (selector))
            if not len(export_meta_urls):
                raise AssertionError("Invalid schema.")
            # extracted required parameter.
            url_tokens = export_meta_urls[0].split("/")
            required_params = list()
            for _param in export_meta_param:
                if "{%s}" % (_param) == url_tokens[-1]:
                    continue
                required_params.append(_param)
            for _param in required_params:
                if _param not in params["export_playbooks"]["params"][selector]:
                    self.module.fail_json(
                        "required parameters for selector %s: %s"
                        % (selector, required_params)
                    )
        # Check required parameter for selector: all
        if "all" in export_selectors:
            if (
                "all" not in params["export_playbooks"]["params"]
                or "adom" not in params["export_playbooks"]["params"]["all"]
            ):
                self.module.fail_json("required parameters for selector %s: %s" % ("all", ["adom"]))
        # process specific selector and 'all'
        selectors_to_process = dict()
        for selector in export_selectors:
            if selector == "all":
                continue
            selectors_to_process[selector] = (metadata[selector], self.module.params["export_playbooks"]["params"][selector])
        if "all" in export_selectors:
            for selector in metadata:
                chosen = True
                if not len(metadata[selector]["urls"]):
                    raise AssertionError("Invalid Schema.")
                url_tokens = metadata[selector]["urls"][0].split("/")
                for _param in metadata[selector]["params"]:
                    if _param == "adom":
                        continue
                    elif "{%s}" % (_param) != url_tokens[-1]:
                        chosen = False
                        break
                if not chosen or selector in selectors_to_process:
                    continue
                selectors_to_process[selector] = (
                    metadata[selector],
                    self.module.params["export_playbooks"]["params"]["all"],
                )
        process_counter = 1
        number_selectors = len(selectors_to_process)
        for selector in selectors_to_process:
            self._process_export_per_selector(
                selector,
                selectors_to_process[selector][0],
                selectors_to_process[selector][1],
                log,
                export_path,
                "%s/%s" % (process_counter, number_selectors),
                exported_schema_inventory,
            )
            process_counter += 1
        self.module.exit_json(
            number_of_selectors=number_selectors,
            number_of_valid_selectors=self._nr_valid_selectors,
            number_of_exported_playbooks=self._nr_exported_playbooks,
            system_infomation=self.system_status,
        )

    def _get_target_url(self, adom_value, url_list):
        target_url = None
        if adom_value is not None and not url_list[0].endswith("{adom}"):
            if adom_value == "global":
                for url in url_list:
                    if "/global/" in url and "/adom/{adom}" not in url:
                        target_url = url
                        break
            elif adom_value:
                for url in url_list:
                    if "/adom/{adom}" in url:
                        target_url = url
                        break
            else:
                # adom = "", choose default URL which is for all domains
                for url in url_list:
                    if "/global/" not in url and "/adom/{adom}" not in url:
                        target_url = url
                        break
        else:
            target_url = url_list[0]
        if not target_url:
            self.module.fail_json(msg="Please check the value of params: adom")
        return target_url

    def process_object_member(self, argument_specs=None):
        self.metadata = argument_specs
        module_name = self.module_level2_name
        params = self.module.params
        track = [module_name]
        bypass_valid = self.module.params.get("bypass_validation", False)
        if not bypass_valid:
            self.check_versioning_mismatch(track, argument_specs.get(module_name, None), params.get(module_name, None))
        member_url = self._get_basic_url(False)
        parent_url, separator, task_type = member_url.rpartition("/")
        response = (-1, {})
        object_present = remove_aliases(self.module.params, self.metadata, bypass_valid)
        object_present = object_present.get(self.module_level2_name, {})
        if self.module.params["state"] == "present":
            params = [{"url": parent_url}]
            rc, object_remote = self.conn.send_request("get", params)
            if rc == 0:
                object_remote = object_remote.get("data", {})
                object_remote = object_remote.get(task_type, {})
                require_update = True
                if not bypass_valid:
                    if isinstance(object_remote, list):
                        if len(object_remote) > 1:
                            require_update = True
                        else:
                            object_remote = object_remote[0]
                    try:
                        require_update = self.is_object_difference(object_remote, object_present)
                    except Exception as e:
                        pass
                if self.is_force_update() or require_update:
                    response = self.update_object("")
                else:
                    return_msg = "Your FortiManager is already up to date and does not need to be updated. "
                    return_msg += "To force update, please add argument proposed_method:update"
                    self.module.exit_json(message=return_msg)
            else:
                resource_name = parent_url.split("/")[-1]
                parent_module, separator, task_name = module_name.rpartition("_")
                parent_module = "fmgr_" + parent_module
                rename_parent_module = {"fmgr_pm_devprof": "fmgr_pm_devprof_pkg",
                                        "fmgr_pm_wanprof": "fmgr_pm_wanprof_pkg"}
                if parent_module in rename_parent_module:
                    parent_module = rename_parent_module[parent_module]
                self.module.fail_json(msg="The resource %s does not exist. Please try to use the module %s first." %
                                      (resource_name, parent_module))
        elif self.module.params["state"] == "absent":
            params = [{"url": member_url, self.top_level_schema_name: object_present}]
            if self.module.check_mode:
                self.do_check_exit(True)
            response = self.conn.send_request("delete", params)
        self.do_exit(response)

    def process_curd(self, argument_specs=None):
        self.metadata = argument_specs
        module_name = self.module_level2_name
        params = self.module.params
        track = [module_name]
        if not params.get("bypass_validation", False):
            self.check_versioning_mismatch(track, argument_specs.get(module_name, None), params.get(module_name, None))
        if self.module_primary_key and isinstance(params.get(module_name, None), dict):
            mvalue = ""
            if self.module_primary_key.startswith("complex:"):
                mvalue_exec_string = self.module_primary_key[len("complex:"):]
                mvalue_exec_string = mvalue_exec_string.replace("{{module}}", "self.module.params[self.module_level2_name]")
                mvalue = eval(mvalue_exec_string)
            else:
                modified_main_key = _get_modified_name(self.module_primary_key)
                if modified_main_key in params[module_name]:
                    mvalue = params[module_name][modified_main_key]
                elif self.module_primary_key in params[module_name]:
                    mvalue = params[module_name][self.module_primary_key]
            self.do_exit(self._process_with_mkey(mvalue))
        else:
            self.do_exit(self._process_without_mkey())

    def process_partial_curd(self, argument_specs=None):
        self.metadata = argument_specs
        module_name = self.module_level2_name
        params = self.module.params
        track = [module_name]
        bypass_valid = params.get("bypass_validation", False)
        if not bypass_valid:
            self.check_versioning_mismatch(track, argument_specs.get(module_name, None), params.get(module_name, None))
        adom_value = params.get("adom", None)
        target_url = self._get_target_url(adom_value, self.jrpc_urls)
        target_url = self._get_replaced_url(target_url)
        target_url = target_url.rstrip("/")
        api_params = {"url": target_url}
        # Try to get and compare, and skip update if same.
        try:
            rc, robject = self.conn.send_request("get", [api_params])
            if rc == 0 and not (self.is_force_update() or self._update_required(robject)):
                return_msg = "Your FortiManager is already up to date and does not need to be updated. "
                return_msg += "To force update, please add argument proposed_method:update"
                if self.module.check_mode:
                    self.do_check_exit(False, message=return_msg)
                self.module.exit_json(message=return_msg)
        except Exception as e:
            pass
        if module_name in params:
            params = remove_aliases(params, argument_specs, bypass_valid)
            api_params[self.top_level_schema_name] = params[module_name]
        if self.module.check_mode:
            self.do_check_exit(True)
        response = self.conn.send_request(self.get_propose_method("set"), [api_params])
        self.do_exit(response)

    def check_versioning_mismatch(self, track, schema, params):
        if not params or not schema:
            return
        param_type = schema["type"] if "type" in schema else None
        v_range = schema["v_range"] if "v_range" in schema else None
        matched, checking_message = self._version_matched(v_range)
        if not matched:
            param_path = track[0]
            for _param in track[1:]:
                param_path += "-->%s" % (_param)
            self.version_check_warnings.append("param: %s %s" % (param_path, checking_message))
        if param_type == "dict" and "options" in schema:
            if not isinstance(params, dict):
                raise AssertionError()
            for sub_param_key in params:
                sub_param = params[sub_param_key]
                if sub_param_key in schema["options"]:
                    sub_schema = schema["options"][sub_param_key]
                    track.append(sub_param_key)
                    self.check_versioning_mismatch(track, sub_schema, sub_param)
                    del track[-1]
        elif param_type == "list" and "options" in schema:
            if not isinstance(params, list):
                raise AssertionError()
            for grouped_param in params:
                if not isinstance(grouped_param, dict):
                    raise AssertionError()
                for sub_param_key in grouped_param:
                    sub_param = grouped_param[sub_param_key]
                    if sub_param_key in schema["options"]:
                        sub_schema = schema["options"][sub_param_key]
                        track.append(sub_param_key)
                        self.check_versioning_mismatch(track, sub_schema, sub_param)
                        del track[-1]

    def validate_parameters(self, pvb):
        for blob in pvb:
            attribute_path = blob["attribute_path"]
            pointer = self.module.params
            ignored = False
            for attr in attribute_path:
                if attr not in pointer:
                    # If the parameter is not given, ignore that.
                    ignored = True
                    break
                pointer = pointer[attr]
            if ignored:
                continue
            lambda_expr = blob["lambda"]
            lambda_expr = lambda_expr.replace("$", str(pointer))
            eval_result = eval(lambda_expr)
            if not eval_result:
                if "fail_action" not in blob or blob["fail_action"] == "warn":
                    self.module.warn(blob["hint_message"])
                else:
                    # assert blob['fail_action'] == 'quit':
                    self.module.fail_json(msg=blob["hint_message"])

    def do_final_exit(self, rc, result, changed=True):
        # XXX: as with https://github.com/fortinet/ansible-fortimanager-generic.
        # the failing conditions priority: failed_when > rc_failed > rc_succeeded.
        failed = rc != 0
        if changed:
            changed = rc == 0

        if "response_code" in result:
            if "rc_failed" in self.module.params and self.module.params["rc_failed"]:
                for rc_code in self.module.params["rc_failed"]:
                    if str(result["response_code"]) == str(rc_code):
                        failed = True
                        result["result_code_overriding"] = "rc code:%s is overridden to failure" % (rc_code)
            elif "rc_succeeded" in self.module.params and self.module.params["rc_succeeded"]:
                for rc_code in self.module.params["rc_succeeded"]:
                    if str(result["response_code"]) == str(rc_code):
                        failed = False
                        result["result_code_overriding"] = "rc code:%s is overridden to success" % (rc_code)
        if self.system_status:
            result["system_information"] = self.system_status
        if len(self.version_check_warnings):
            version_check_warning = {}
            version_check_warning["mismatches"] = self.version_check_warnings
            if self.system_status:
                version_check_warning["system_version"] = "v%s.%s.%s" % (
                    self.system_status["Major"],
                    self.system_status["Minor"],
                    self.system_status["Patch"],
                )
            self.module.warn(
                "Some parameters in the playbook may not be supported by the current FortiManager version. "
                "To see which parameters are not available, check version_check_warning in the output. "
                "This message is only a suggestion. Please ignore this warning if you think your configurations are correct."
            )
            self.module.exit_json(rc=rc, meta=result, version_check_warning=version_check_warning, failed=failed, changed=changed)
        else:
            self.module.exit_json(rc=rc, meta=result, failed=failed, changed=changed)

    def do_check_exit(self, changed, message=""):
        result = {}
        if message:
            message = "Using check mode. " + message
        else:
            message = "Using check mode."
        if self.system_status:
            result["system_information"] = self.system_status
        if len(self.version_check_warnings):
            version_check_warning = {}
            version_check_warning["mismatches"] = self.version_check_warnings
            if self.system_status:
                version_check_warning["system_version"] = "v%s.%s.%s" % (
                    self.system_status["Major"],
                    self.system_status["Minor"],
                    self.system_status["Patch"],
                )
            self.module.warn(
                "Some parameters in the playbook may not be supported by the current FortiManager version. "
                "To see which parameters are not available, check version_check_warning in the output. "
                "This message is only a suggestion. Please ignore this warning if you think your configurations are correct."
            )
            self.module.exit_json(meta=result, version_check_warning=version_check_warning, changed=changed, message=message)
        else:
            self.module.exit_json(meta=result, changed=changed, message=message)

    def do_exit(self, response, changed=True):
        rc, response_data = response
        result = {"response_data": list(), "response_message": ""}
        if "data" in response_data:
            result["response_data"] = response_data["data"]
        if "status" in response_data:
            if "code" in response_data["status"]:
                result["response_code"] = response_data["status"]["code"]
            if "message" in response_data["status"]:
                result["response_message"] = response_data["status"]["message"]
        if "url" in response_data:
            result["request_url"] = response_data["url"]
            # Fix for fmgr_sys_hitcount
            if response_data["url"] == "/sys/hitcount":
                if isinstance(result["response_data"], list) and len(result["response_data"]) == 0:
                    result["response_data"] = dict()
                if "taskid" in response_data and isinstance(result["response_data"], dict) \
                        and "task" not in result["response_data"]:
                    result["response_data"]["task"] = response_data["taskid"]
        self.do_final_exit(rc, result, changed=changed)
