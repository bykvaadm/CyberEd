#!/usr/bin/python
# -*- coding: utf-8 -*-

# pylint: disable=invalid-name,use-dict-literal,too-many-branches,too-many-locals,line-too-long,wrong-import-position

"""This module creates, deletes or modifies metadata on Infinibox."""

# Copyright: (c) 2024, Infinidat <info@infinidat.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: infini_metadata
version_added: 2.13.0
short_description:  Create, Delete or Modify metadata on Infinibox
description:
    - This module creates, deletes or modifies metadata on Infinibox.
    - Deleting metadata by object, without specifying a key, is not implemented for any object_type (e.g. DELETE api/rest/metadata/system).
    - This would delete all metadata belonging to the object. Instead delete each key explicitely using its key name.
author: David Ohlemacher (@ohlemacher)
options:
  object_type:
    description:
      - Type of object
    type: str
    required: true
    choices: ["cluster", "fs", "fs-snap", "host", "pool", "system", "vol", "vol-snap"]
  object_name:
    description:
      - Name of the object. Not used if object_type is system
    type: str
    required: false
  key:
    description:
      - Name of the metadata key
    type: str
    required: true
  value:
    description:
      - Value of the metadata key
    type: str
    required: false
  state:
    description:
      - Creates/Modifies metadata when present or removes when absent.
    type: str
    required: false
    default: present
    choices: [ "stat", "present", "absent" ]

extends_documentation_fragment:
    - infinibox
"""

EXAMPLES = r"""
- name: Create new metadata key foo with value bar
  infini_metadata:
    name: foo
    key: bar
    state: present
    user: admin
    password: secret
    system: ibox001
- name: Stat metadata key named foo
  infini_metadata:
    name: foo
    state: stat
    user: admin
    password: secret
    system: ibox001
- name: Remove metadata keyn named foo
  infini_vol:
    name: foo_snap
    state: absent
    user: admin
    password: secret
    system: ibox001
"""

# RETURN = r''' # '''

import json

from ansible.module_utils.basic import AnsibleModule, missing_required_lib

from ansible_collections.infinidat.infinibox.plugins.module_utils.infinibox import (
    HAS_INFINISDK,
    api_wrapper,
    get_cluster,
    get_filesystem,
    get_host,
    get_pool,
    get_system,
    get_volume,
    infinibox_argument_spec,
)

HAS_INFINISDK = True
try:
    from infinisdk.core.exceptions import APICommandFailed
except ImportError:
    HAS_INFINISDK = False

HAS_CAPACITY = False


@api_wrapper
def get_metadata_vol(module, disable_fail):
    """ Get metadata about a volume """
    system = get_system(module)
    object_type = module.params["object_type"]
    object_name = module.params["object_name"]
    key = module.params["key"]
    metadata = None

    vol = get_volume(module, system)
    if vol:
        path = f"metadata/{vol.id}/{key}"
        try:
            metadata = system.api.get(path=path)
        except APICommandFailed:
            if not disable_fail:
                module.fail_json(
                    f"Cannot find {object_type} metadata key. "
                    f"Volume {object_name} key {key} not found"
                )
    elif not disable_fail:
        msg = f"Volume with object name {object_name} not found. Cannot stat its metadata."
        module.fail_json(msg=msg)

    return metadata


@api_wrapper
def get_metadata_fs(module, disable_fail):
    """ Get metadata about a fs """
    system = get_system(module)
    object_type = module.params["object_type"]
    object_name = module.params["object_name"]
    key = module.params["key"]
    metadata = None

    fs = get_filesystem(module, system)
    if fs:
        path = f"metadata/{fs.id}/{key}"
        try:
            metadata = system.api.get(path=path)
        except APICommandFailed:
            if not disable_fail:
                module.fail_json(
                    f"Cannot find {object_type} metadata key. "
                    f"File system {object_name} key {key} not found"
                )
    elif not disable_fail:
        msg = f"File system named {object_name} not found. Cannot stat its metadata."
        module.fail_json(msg=msg)

    return metadata


@api_wrapper
def get_metadata_host(module, disable_fail):
    """ Get metadata about a host """
    system = get_system(module)
    object_type = module.params["object_type"]
    object_name = module.params["object_name"]
    key = module.params["key"]
    metadata = None

    host = get_host(module, system)
    if host:
        path = f"metadata/{host.id}/{key}"
        try:
            metadata = system.api.get(path=path)
        except APICommandFailed:
            if not disable_fail:
                module.fail_json(
                    f"Cannot find {object_type} metadata key. "
                    f"Host {object_name} key {key} not found"
                )
    elif not disable_fail:
        msg = f"Host named {object_name} not found. Cannot stat its metadata."
        module.fail_json(msg=msg)

    return metadata


@api_wrapper
def get_metadata_cluster(module, disable_fail):
    """ Get metadata about a cluster """
    system = get_system(module)
    object_type = module.params["object_type"]
    object_name = module.params["object_name"]
    key = module.params["key"]
    metadata = None

    cluster = get_cluster(module, system)
    if cluster:
        path = f"metadata/{cluster.id}/{key}"
        try:
            metadata = system.api.get(path=path)
        except APICommandFailed:
            if not disable_fail:
                module.fail_json(
                    f"Cannot find {object_type} metadata key. "
                    f"Cluster {object_name} key {key} not found"
                )
    elif not disable_fail:
        msg = f"Cluster named {object_name} not found. Cannot stat its metadata."
        module.fail_json(msg=msg)

    return metadata


@api_wrapper
def get_metadata_fssnap(module, disable_fail):
    """ Get metadata about a fs snapshot """
    system = get_system(module)
    object_type = module.params["object_type"]
    object_name = module.params["object_name"]
    key = module.params["key"]
    metadata = None

    fssnap = get_filesystem(module, system)
    if fssnap:
        path = f"metadata/{fssnap.id}/{key}"
        try:
            metadata = system.api.get(path=path)
        except APICommandFailed:
            if not disable_fail:
                module.fail_json(
                    f"Cannot find {object_type} metadata key. "
                    f"File system snapshot {object_name} key {key} not found"
                )
    elif not disable_fail:
        msg = f"File system snapshot named {object_name} not found. Cannot stat its metadata."
        module.fail_json(msg=msg)

    return metadata


@api_wrapper
def get_metadata_pool(module, disable_fail):
    """ Get metadata about a pool """
    system = get_system(module)
    object_type = module.params["object_type"]
    object_name = module.params["object_name"]
    key = module.params["key"]
    metadata = None

    pool = get_pool(module, system)
    if pool:
        path = f"metadata/{pool.id}/{key}"
        try:
            metadata = system.api.get(path=path)
        except APICommandFailed:
            if not disable_fail:
                module.fail_json(
                    f"Cannot find {object_type} metadata key. "
                    f"Pool {object_name} key {key} not found"
                )
    elif not disable_fail:
        msg = f"Pool named {object_name} not found. Cannot stat its metadata."
        module.fail_json(msg=msg)

    return metadata


@api_wrapper
def get_metadata_volsnap(module, disable_fail):
    """ Get metadata for a volume snapshot """
    system = get_system(module)
    object_type = module.params["object_type"]
    object_name = module.params["object_name"]
    key = module.params["key"]
    metadata = None

    volsnap = get_volume(module, system)
    if volsnap:
        path = f"metadata/{volsnap.id}/{key}"
        try:
            metadata = system.api.get(path=path)
        except APICommandFailed:
            if not disable_fail:
                module.fail_json(
                    f"Cannot find {object_type} metadata key. "
                    f"Volume snapshot {object_name} key {key} not found"
                )
    elif not disable_fail:
        msg = f"Volume snapshot named {object_name} not found. Cannot stat its metadata."
        module.fail_json(msg=msg)

    return metadata


@api_wrapper
def get_metadata(module, disable_fail=False):
    """
    Find and return metadata
    Use disable_fail when we are looking for metadata
    and it may or may not exist and neither case is an error.
    """
    system = get_system(module)
    object_type = module.params["object_type"]
    object_name = module.params["object_name"]
    key = module.params["key"]

    if object_type == "system":
        path = f"metadata/{object_type}?key={key}"
        metadata = system.api.get(path=path)
    elif object_type == "fs":
        metadata = get_metadata_fs(module, disable_fail)
    elif object_type == "vol":
        metadata = get_metadata_vol(module, disable_fail)
    elif object_type == "host":
        metadata = get_metadata_host(module, disable_fail)
    elif object_type == "cluster":
        metadata = get_metadata_cluster(module, disable_fail)
    elif object_type == "fs-snap":
        metadata = get_metadata_fs(module, disable_fail)
    elif object_type == "pool":
        metadata = get_metadata_pool(module, disable_fail)
    elif object_type == "vol-snap":
        metadata = get_metadata_volsnap(module, disable_fail)

    else:
        msg = f"Metadata for {object_type} not supported. Cannot stat."
        module.fail_json(msg=msg)

    if metadata:
        result = metadata.get_result()
        if not disable_fail and not result:
            msg = f"Metadata for {object_type} with key {key} not found. Cannot stat."
            module.fail_json(msg=msg)
        return result

    if disable_fail:
        return None

    msg = f"Metadata for {object_type} named {object_name} not found. Cannot stat."
    module.fail_json(msg=msg)
    return None  # Quiet pylint


@api_wrapper
def put_metadata(module):  # pylint: disable=too-many-statements
    """Create metadata key with a value.  The changed variable is found elsewhere."""
    system = get_system(module)

    object_type = module.params["object_type"]
    key = module.params["key"]
    value = module.params["value"]

    # Could check metadata value size < 32k

    if object_type == "system":
        path = "metadata/system"
    elif object_type == "vol":
        vol = get_volume(module, system)
        if not vol:
            object_name = module.params["object_name"]
            msg = f"Volume {object_name} not found. Cannot add metadata key {key}."
            module.fail_json(msg=msg)
        path = f"metadata/{vol.id}"
    elif object_type == "fs":
        fs = get_filesystem(module, system)
        if not fs:
            object_name = module.params["object_name"]
            msg = f"File system {object_name} not found. Cannot add metadata key {key}."
            module.fail_json(msg=msg)
        path = f"metadata/{fs.id}"
    elif object_type == "host":
        host = get_host(module, system)
        if not host:
            object_name = module.params["object_name"]
            msg = f"Cluster {object_name} not found. Cannot add metadata key {key}."
            module.fail_json(msg=msg)
        path = f"metadata/{host.id}"
    elif object_type == "cluster":
        cluster = get_cluster(module, system)
        if not cluster:
            object_name = module.params["object_name"]
            msg = f"Cluster {object_name} not found. Cannot add metadata key {key}."
            module.fail_json(msg=msg)
        path = f"metadata/{cluster.id}"
    elif object_type == "fs-snap":
        fssnap = get_filesystem(module, system)
        if not fssnap:
            object_name = module.params["object_name"]
            msg = f"File system snapshot {object_name} not found. Cannot add metadata key {key}."
            module.fail_json(msg=msg)
        path = f"metadata/{fssnap.id}"
    elif object_type == "pool":
        pool = get_pool(module, system)
        if not pool:
            object_name = module.params["object_name"]
            msg = f"Pool {object_name} not found. Cannot add metadata key {key}."
            module.fail_json(msg=msg)
        path = f"metadata/{pool.id}"
    elif object_type == "vol-snap":
        volsnap = get_volume(module, system)
        if not volsnap:
            object_name = module.params["object_name"]
            msg = f"Volume snapshot {object_name} not found. Cannot add metadata key {key}."
            module.fail_json(msg=msg)
        path = f"metadata/{volsnap.id}"

    # Create json data
    data = {
        key: value
    }

    # Put
    system.api.put(path=path, data=data)
    # Variable 'changed' not returned by design


@api_wrapper
def delete_metadata(module):  # pylint: disable=too-many-return-statements
    """
    Remove metadata key.
    Not implemented by design: Deleting all of the system's metadata
    using 'DELETE api/rest/metadata/system'.
    """
    system = get_system(module)
    changed = False
    object_type = module.params["object_type"]
    key = module.params["key"]
    if object_type == "system":
        path = f"metadata/system/{key}"
    elif object_type == "vol":
        vol = get_volume(module, system)
        if not vol:
            changed = False
            return changed  # No vol therefore no metadata to delete
        path = f"metadata/{vol.id}/{key}"
    elif object_type == "fs":
        fs = get_filesystem(module, system)
        if not fs:
            changed = False
            return changed  # No fs therefore no metadata to delete
        path = f"metadata/{fs.id}/{key}"
    elif object_type == "host":
        host = get_host(module, system)
        if not host:
            changed = False
            return changed  # No host therefore no metadata to delete
        path = f"metadata/{host.id}/{key}"
    elif object_type == "cluster":
        cluster = get_cluster(module, system)
        if not cluster:
            changed = False
            return changed  # No cluster therefore no metadata to delete
        path = f"metadata/{cluster.id}/{key}"
    elif object_type == "fs-snap":
        fssnap = get_filesystem(module, system)
        if not fssnap:
            changed = False
            return changed  # No fssnap therefore no metadata to delete
        path = f"metadata/{fssnap.id}/{key}"
    elif object_type == "pool":
        pool = get_pool(module, system)
        if not pool:
            changed = False
            return changed  # No pool therefore no metadata to delete
        path = f"metadata/{pool.id}/{key}"
    elif object_type == "vol-snap":
        volsnap = get_volume(module, system)
        if not volsnap:
            changed = False
            return changed  # No volsnap therefore no metadata to delete
        path = f"metadata/{volsnap.id}/{key}"
    else:
        module.fail_json(f"Object type {object_type} not supported")

    try:
        system.api.delete(path=path)
        changed = True
    except APICommandFailed as err:
        if err.status_code != 404:
            raise
    return changed


def handle_stat(module):
    """Return metadata stat"""
    object_type = module.params["object_type"]
    key = module.params["key"]
    metadata = get_metadata(module)
    if object_type == "system":
        metadata_id = metadata[0]["id"]
        object_id = metadata[0]["object_id"]
        value = metadata[0]["value"]
    else:
        metadata_id = metadata["id"]
        object_id = metadata["object_id"]
        value = metadata["value"]

    result = {
        "msg": "Metadata found",
        "changed": False,
        "object_type": object_type,
        "key": key,
        "id": metadata_id,
        "object_id": object_id,
        "value": value,
    }
    module.exit_json(**result)


def handle_present(module):
    """Make metadata present"""
    changed = False
    msg = "Metadata unchanged"
    if not module.check_mode:
        old_metadata = get_metadata(module, disable_fail=True)
        put_metadata(module)
        new_metadata = get_metadata(module)
        changed = new_metadata != old_metadata
        if changed:
            msg = "Metadata changed"
        else:
            msg = "Metadata unchanged since the value is the same as the existing metadata"
    module.exit_json(changed=changed, msg=msg)


def handle_absent(module):
    """Make metadata absent"""
    msg = "Metadata unchanged"
    changed = False
    if not module.check_mode:
        changed = delete_metadata(module)
        if changed:
            msg = "Metadata removed"
        else:
            msg = "Metadata did not exist so no removal was necessary"
    module.exit_json(changed=changed, msg=msg)


def execute_state(module):
    """Determine which state function to execute and do so"""
    state = module.params["state"]
    try:
        if state == "stat":
            handle_stat(module)
        elif state == "present":
            handle_present(module)
        elif state == "absent":
            handle_absent(module)
        else:
            module.fail_json(msg=f"Internal handler error. Invalid state: {state}")
    finally:
        system = get_system(module)
        system.logout()


def check_options(module):
    """Verify module options are sane"""
    state = module.params["state"]
    object_type = module.params["object_type"]
    object_name = module.params["object_name"]

    # Check object_type
    object_types = [
        "cluster",
        "fs",
        "fs-snap",
        "host",
        "pool",
        "system",
        "vol",
        "vol-snap",
    ]
    if object_type not in object_types:
        module.fail_json(
            f"Cannot create {object_type} metadata. Object type must be one of {object_types}"
        )

    # Check object_name
    if object_type == "system":
        if object_name:
            module.fail_json("An object_name for object_type system must not be provided.")
    else:
        if not object_name:
            module.fail_json(
                f"The name of the {object_type} must be provided as object_name."
            )

    key = module.params["key"]
    if not key:
        module.fail_json(f"Cannot create a {object_type} metadata key without providing a key name")

    if state == "stat":
        pass
    elif state == "present":
        # Check value
        key = module.params["key"]
        value = module.params["value"]
        if not value:
            module.fail_json(
                f"Cannot create a {object_type} metadata key {key} without providing a value"
            )
        # Check system object_type
        if object_type == "system":
            if key == "ui-dataset-default-provisioning":
                values = ["THICK", "THIN"]
                if value not in values:
                    module.fail_json(
                        f"Cannot create {object_type} metadata for key {key}. "
                        f"Value must be one of {values}. Invalid value: {value}."
                    )

            # Convert bool string to bool
            if key in [
                "ui-dataset-base2-units",
                "ui-feedback-dialog",
                "ui-feedback-form",
            ]:
                try:
                    module.params["value"] = json.loads(value.lower())
                except json.decoder.JSONDecodeError:
                    module.fail_json(
                        f"Cannot create {object_type} metadata for key {key}. "
                        f"Value must be able to be decoded as a boolean. Invalid value: {value}."
                    )

            # Convert integer string to int
            if key in [
                "ui-bulk-volume-zero-padding",
                "ui-table-export-limit"
            ]:
                try:
                    module.params["value"] = json.loads(value.lower())
                except json.decoder.JSONDecodeError:
                    module.fail_json(
                        f"Cannot create {object_type} metadata for key {key}. "
                        f"Value must be of type integer. Invalid value: {value}."
                    )

    elif state == "absent":
        pass
    else:
        module.fail_json(f"Invalid state '{state}' provided")


def main():
    """ Main """
    argument_spec = infinibox_argument_spec()

    argument_spec.update(
        {
            "object_type": {"required": True, "choices": ["cluster", "fs", "fs-snap", "host", "pool", "system", "vol", "vol-snap"]},
            "object_name": {"required": False, "default": None},
            "key": {"required": True, "no_log": False},
            "value": {"required": False, "default": None},
            "state": {"default": "present", "choices": ["stat", "present", "absent"]},
        }
    )

    module = AnsibleModule(argument_spec, supports_check_mode=True)

    if not HAS_INFINISDK:
        module.fail_json(msg=missing_required_lib("infinisdk"))

    check_options(module)
    execute_state(module)


if __name__ == "__main__":
    main()
