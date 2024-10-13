#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2019, Simon Dodsley (simon@purestorage.com)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: purefa_dsrole
version_added: '1.0.0'
short_description: Configure FlashArray Directory Service Roles
description:
- Set or erase directory services role configurations.
author:
- Pure Storage Ansible Team (@sdodsley) <pure-ansible-team@purestorage.com>
options:
  state:
    description:
    - Create or delete directory service role
    type: str
    default: present
    choices: [ absent, present ]
  role:
    description:
    - The directory service role to work on
    type: str
    required: true
    choices: [ array_admin, ops_admin, readonly, storage_admin ]
  group_base:
    type: str
    description:
    - Specifies where the configured group is located in the directory
      tree. This field consists of Organizational Units (OUs) that combine
      with the base DN attribute and the configured group CNs to complete
      the full Distinguished Name of the groups. The group base should
      specify OU= for each OU and multiple OUs should be separated by commas.
      The order of OUs is important and should get larger in scope from left
      to right.
    - Each OU should not exceed 64 characters in length.
  group:
    type: str
    description:
    - Sets the common Name (CN) of the configured directory service group
      containing users for the FlashBlade. This name should be just the
      Common Name of the group without the CN= specifier.
    - Common Names should not exceed 64 characters in length.
extends_documentation_fragment:
- purestorage.flasharray.purestorage.fa
"""

EXAMPLES = r"""
- name: Delete exisitng array_admin directory service role
  purestorage.flasharray.purefa_dsrole:
    role: array_admin
    state: absent
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Create array_admin directory service role
  purestorage.flasharray.purefa_dsrole:
    role: array_admin
    group_base: "OU=PureGroups,OU=SANManagers"
    group: pureadmins
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Update ops_admin directory service role
  purestorage.flasharray.purefa_dsrole:
    role: ops_admin
    group_base: "OU=PureGroups"
    group: opsgroup
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
"""

RETURN = r"""
"""

MIN_DSROLE_API_VERSION = "2.30"

HAS_PYPURECLIENT = True
try:
    from pypureclient.flasharray import DirectoryServiceRole, FixedReference
except ImportError:
    HAS_PYPURECLIENT = False


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.purestorage.flasharray.plugins.module_utils.purefa import (
    get_array,
    purefa_argument_spec,
)
from ansible_collections.purestorage.flasharray.plugins.module_utils.version import (
    LooseVersion,
)


def update_role(module, array):
    """Update Directory Service Role"""
    changed = False
    role = list(
        array.get_directory_services_roles(names=[module.params["role"]]).items
    )[0]
    if (
        role.group_base != module.params["group_base"]
        or role.group != module.params["group"]
    ):
        changed = True
        if not module.check_mode:
            res = array.patch_directory_services_roles(
                names=[module.params["role"]],
                directory_service_roles=DirectoryServiceRole(
                    group_base=module.params["group_base"], group=module.params["group"]
                ),
            )
            if res.status_code != 200:
                module.fail_json(
                    msg="Update Directory Service Role {0} failed.Error: {1}".format(
                        module.params["role"], res.errors[0].message
                    )
                )
    module.exit_json(changed=changed)


def delete_role(module, array):
    """Delete Directory Service Role"""
    changed = True
    if not module.check_mode:
        res = array.delete_directory_services_roles(names=[module.params["role"]])
        if res.status_code != 200:
            module.fail_json(
                msg="Delete Directory Service Role {0} failed. Error: {1}".format(
                    module.params["role"], res.errors[0].message
                )
            )
    module.exit_json(changed=changed)


def create_role(module, array):
    """Create Directory Service Role"""
    changed = False
    if not module.params["group"] == "" or not module.params["group_base"] == "":
        changed = True
        if not module.check_mode:
            res = array.post_directory_services_roles(
                names=[module.params["role"]],
                directory_service_role=DirectoryServiceRole(
                    group_base=module.params["group_base"], group=module.params["group"]
                ),
            )
            if res.status_code != 200:
                module.fail_json(
                    msg="Create Directory Service Role {0} failed. Error: {1}".format(
                        module.params["role"],
                        res.errors[0].message,
                    )
                )
    module.exit_json(changed=changed)


def main():
    argument_spec = purefa_argument_spec()
    argument_spec.update(
        dict(
            role=dict(
                required=True,
                type="str",
                choices=["array_admin", "ops_admin", "readonly", "storage_admin"],
            ),
            state=dict(type="str", default="present", choices=["absent", "present"]),
            group_base=dict(type="str"),
            group=dict(type="str"),
        )
    )

    required_together = [["group", "group_base"]]

    module = AnsibleModule(
        argument_spec, required_together=required_together, supports_check_mode=True
    )

    if not HAS_PYPURECLIENT:
        module.fail_json(msg="pypureclient sdk is required for this module")

    state = module.params["state"]
    array = get_array(module)
    api_version = array.get_rest_version()
    if LooseVersion(MIN_DSROLE_API_VERSION) > LooseVersion(api_version):
        module.fail_json(
            msg="This module requires Purity//FA 6.6.3 and higher. "
            "For older Purity versions please use the ``purefa_dsrole_old`` module"
        )
    role_configured = False
    role = list(
        array.get_directory_services_roles(
            roles=[FixedReference(name=module.params["role"])]
        ).items
    )[0]
    if getattr(role, "group", None) is not None:
        role_configured = True

    if state == "absent" and role_configured:
        delete_role(module, array)
    elif role_configured and state == "present":
        update_role(module, array)
    elif not role_configured and state == "present":
        create_role(module, array)
    else:
        module.exit_json(changed=False)


if __name__ == "__main__":
    main()
