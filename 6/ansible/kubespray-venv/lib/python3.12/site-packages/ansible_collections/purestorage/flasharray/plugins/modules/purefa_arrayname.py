#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2018, Simon Dodsley (simon@purestorage.com)
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
module: purefa_arrayname
version_added: '1.0.0'
short_description: Configure Pure Storage FlashArray array name
description:
- Configure name of array for Pure Storage FlashArrays.
- Ideal for Day 0 initial configuration.
author:
- Pure Storage Ansible Team (@sdodsley) <pure-ansible-team@purestorage.com>
options:
  state:
    description:
    - Set the array name
    type: str
    default: present
    choices: [ present ]
  name:
    description:
    - Name of the array. Must conform to correct naming schema.
    type: str
    required: true
extends_documentation_fragment:
- purestorage.flasharray.purestorage.fa
"""

EXAMPLES = r"""
- name: Set new array name
  purestorage.flasharray.purefa_arrayname:
    name: new-array-name
    state: present
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
"""

RETURN = r"""
"""

HAS_PURESTORAGE = True
try:
    from pypureclient.flasharray import Arrays
except ImportError:
    HAS_PURESTORAGE = False


import re
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.purestorage.flasharray.plugins.module_utils.purefa import (
    get_array,
    purefa_argument_spec,
)


def update_name(module, array):
    """Change aray name"""
    changed = True
    if not module.check_mode:
        res = array.patch_arrays(array=Arrays(name=module.params["name"]))
        if res.status_code != 200:
            module.fail_json(
                msg="Failed to change array name to {0}. Error: {1}".format(
                    module.params["name"], res.errors[0].message
                )
            )

    module.exit_json(changed=changed)


def main():
    argument_spec = purefa_argument_spec()
    argument_spec.update(
        dict(
            name=dict(type="str", required=True),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec, supports_check_mode=True)

    if not HAS_PURESTORAGE:
        module.fail_json(msg="py-pure-client sdk is required for this module")

    array = get_array(module)
    pattern = re.compile("^[a-zA-Z0-9]([a-zA-Z0-9-]{0,54}[a-zA-Z0-9])?$")
    if not pattern.match(module.params["name"]):
        module.fail_json(
            msg="Array name {0} does not conform to array name rules".format(
                module.params["name"]
            )
        )
    if module.params["name"] != list(array.get_arrays().items)[0].name:
        update_name(module, array)

    module.exit_json(changed=False)


if __name__ == "__main__":
    main()
