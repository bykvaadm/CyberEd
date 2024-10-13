#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2024, Akini Ross (@akinross) <akinross@cisco.com>

# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {"metadata_version": "1.1", "status": ["preview"], "supported_by": "community"}

DOCUMENTATION = r"""
---
module: ndo_l3_domain
short_description: Manage L3 Domains on Cisco Nexus Dashboard Orchestrator (NDO).
description:
- Manage L3 Domains on Cisco Nexus Dashboard Orchestrator (NDO).
- This module is only supported on ND v3.1 (NDO v4.3) and later.
author:
- Akini Ross (@akinross)
options:
  template:
    description:
    - The name of the template.
    - The template must be a fabric policy template.
    type: str
    required: true
  l3_domain:
    description:
    - The name of the L3 Domain.
    type: str
    aliases: [ name ]
  l3_domain_uuid:
    description:
    - The uuid of the L3 Domain.
    - This parameter is required when the O(l3_domain) needs to be updated.
    type: str
    aliases: [ uuid ]
  description:
    description:
    - The description of the L3 Domain.
    type: str
  pool:
    description:
    - The name of the VLAN Pool.
    - Providing an empty string will remove the pool from the L3 Domain.
    type: str
    aliases: [ vlan_pool ]
  state:
    description:
    - Use C(absent) for removing.
    - Use C(query) for listing an object or multiple objects.
    - Use C(present) for creating or updating.
    type: str
    choices: [ absent, query, present ]
    default: query
extends_documentation_fragment: cisco.mso.modules
"""

EXAMPLES = r"""
- name: Create a new L3 domain
  cisco.mso.ndo_l3_domain:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    template: ansible_tenant_template
    l3_domain: ansible_test_l3_domain
    pool: ansible_test_vlan_pool
    state: present

- name: Query a L3 domain with template_name
  cisco.mso.ndo_l3_domain:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    template: ansible_tenant_template
    l3_domain: ansible_test_l3_domain
    state: query
  register: query_one

- name: Query all L3 domains in the template
  cisco.mso.ndo_l3_domain:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    template: ansible_tenant_template
    state: query
  register: query_all

- name: Delete a vlan pool from a L3 domain
  cisco.mso.ndo_l3_domain:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    template: ansible_tenant_template
    l3_domain: ansible_test_l3_domain
    pool: ""
    state: present

- name: Delete a L3 domain
  cisco.mso.ndo_l3_domain:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    template: ansible_tenant_template
    l3_domain: ansible_test_l3_domain
    state: absent
"""

RETURN = r"""
"""


import copy
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.mso.plugins.module_utils.mso import MSOModule, mso_argument_spec
from ansible_collections.cisco.mso.plugins.module_utils.template import MSOTemplate, KVPair


def main():
    argument_spec = mso_argument_spec()
    argument_spec.update(
        template=dict(type="str", required=True),
        l3_domain=dict(type="str", aliases=["name"]),
        l3_domain_uuid=dict(type="str", aliases=["uuid"]),
        description=dict(type="str"),
        pool=dict(type="str", aliases=["vlan_pool"]),
        state=dict(type="str", default="query", choices=["absent", "query", "present"]),
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_if=[
            ["state", "absent", ["l3_domain"]],
            ["state", "present", ["l3_domain"]],
        ],
    )

    mso = MSOModule(module)

    template = module.params.get("template")
    l3_domain = module.params.get("l3_domain")
    l3_domain_uuid = module.params.get("l3_domain_uuid")
    pool = module.params.get("pool")
    description = module.params.get("description")
    state = module.params.get("state")

    ops = []
    match = None

    mso_template = MSOTemplate(mso, "fabric_policy", template)
    mso_template.validate_template("fabricPolicy")

    path = "/fabricPolicyTemplate/template/l3Domains"
    existing_l3_domains = mso_template.template.get("fabricPolicyTemplate", {}).get("template", {}).get("l3Domains", [])
    if l3_domain:
        object_description = "L3 Domain"
        if l3_domain_uuid:
            match = mso_template.get_object_by_uuid(object_description, existing_l3_domains, l3_domain_uuid)
        else:
            kv_list = [KVPair("name", l3_domain)]
            match = mso_template.get_object_by_key_value_pairs(object_description, existing_l3_domains, kv_list)
        if match:
            if match.details.get("pool"):
                match.details["pool"] = mso_template.get_vlan_pool_name(match.details.get("pool"))
            mso.existing = mso.previous = copy.deepcopy(match.details)
    else:
        mso.existing = mso.previous = existing_l3_domains

    if state == "present":

        mso.existing = {}

        if match:

            if l3_domain and match.details.get("name") != l3_domain:
                ops.append(dict(op="replace", path="{0}/{1}/name".format(path, match.index), value=l3_domain))
                match.details["name"] = l3_domain

            if description is not None and match.details.get("description") != description:
                ops.append(dict(op="replace", path="{0}/{1}/description".format(path, match.index), value=description))
                match.details["description"] = description

            if pool and match.details.get("pool") != pool:
                ops.append(dict(op="replace", path="{0}/{1}/pool".format(path, match.index), value=mso_template.get_vlan_pool_uuid(pool)))
                match.details["pool"] = pool
            elif pool == "" and match.details.get("pool"):
                ops.append(dict(op="remove", path="{0}/{1}/pool".format(path, match.index)))
                match.details.pop("pool")

            mso.sanitize(match.details)

        else:

            payload = {"name": l3_domain, "templateId": mso_template.template.get("templateId"), "schemaId": mso_template.template.get("schemaId")}
            if description:
                payload["description"] = description
            if pool:
                payload["pool"] = mso_template.get_vlan_pool_uuid(pool)

            ops.append(dict(op="add", path="{0}/-".format(path), value=copy.deepcopy(payload)))

            if pool:
                payload["pool"] = pool

            mso.sanitize(payload)

        mso.existing = mso.proposed

    elif state == "absent":
        if match:
            ops.append(dict(op="remove", path="{0}/{1}".format(path, match.index)))
        mso.existing = {}

    if not module.check_mode and ops:
        mso.request(mso_template.template_path, method="PATCH", data=ops)

    mso.exit_json()


if __name__ == "__main__":
    main()
