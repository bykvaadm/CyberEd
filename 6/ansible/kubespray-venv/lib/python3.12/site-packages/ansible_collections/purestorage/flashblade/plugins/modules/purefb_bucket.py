#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2017, Simon Dodsley (simon@purestorage.com)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}


DOCUMENTATION = """
---
module: purefb_bucket
version_added: "1.0.0"
short_description:  Manage Object Store Buckets on a  Pure Storage FlashBlade.
description:
    - This module managess object store (s3) buckets on Pure Storage FlashBlade.
author: Pure Storage Ansible Team (@sdodsley) <pure-ansible-team@purestorage.com>
options:
  name:
    description:
      - Bucket Name.
    required: true
    type: str
  account:
    description:
      - Object Store Account for Bucket.
    required: true
    type: str
  versioning:
    description:
      - State of S3 bucket versioning
    required: false
    default: absent
    type: str
    choices: [ "enabled", "suspended", "absent" ]
  state:
    description:
      - Create, delete or modifies a bucket.
    required: false
    default: present
    type: str
    choices: [ "present", "absent" ]
  eradicate:
    description:
      - Define whether to eradicate the bucket on delete or leave in trash.
    required: false
    type: bool
    default: false
  mode:
    description:
      - The type of bucket to be created. Also referred to a VSO Mode.
      - Requires Purity//FB 3.3.3 or higher
      - I(multi-site-writable) type can only be used after feature is
        enabled by Pure Technical Support
    type: str
    choices: [ "classic", "multi-site-writable" ]
    version_added: '1.10.0'
  quota:
    description:
      - User quota in M, G, T or P units. This cannot be 0.
      - This value will override the object store account's default bucket quota.
    type: str
    version_added: '1.12.0'
  hard_limit:
    description:
     - Whether the I(quota) value is enforced or not.
     - If not provided the object store account default value will be used.
    type: bool
    version_added: '1.12.0'
  retention_lock:
    description:
     - Set retention lock level for the bucket
     - Once set to I(ratcheted) can only be lowered by Pure Technical Services
    type: str
    choices: [ "ratcheted", "unlocked" ]
    default: unlocked
    version_added: '1.12.0'
  retention_mode:
    description:
     - The retention mode used to apply locks on new objects if none is specified by the S3 client
     - I(safemode) is available if global Per-Bucket Safemode config is enabled
     - Use "" to clear
     - Once set to I(compliance) this can only be changed by contacting Pure Technical Services
    type: str
    choices: [ "compliance", "governance", "safemode", "" ]
    version_added: '1.12.0'
  object_lock_enabled:
    description:
     - If set to true, then S3 APIs relating to object lock may be used
    type: bool
    default: false
    version_added: '1.12.0'
  freeze_locked_objects:
    description:
     - If set to true, a locked object will be read-only and no new versions of
       the object may be created due to modifications
     - After enabling, can be disabled only by contacting Pure Technical Services
    type: bool
    default: false
    version_added: '1.12.0'
  default_retention:
    description:
     - The retention period, in days, used to apply locks on new objects if
       none is specified by the S3 client
     - Valid values between 1 and 365000
     - Use "" to clear
    type: str
    version_added: '1.12.0'
  block_new_public_policies:
    description:
    - If set to true, adding bucket policies that grant public access to a bucket is not allowed.
    type: bool
    version_added: '1.15.0'
  block_public_access:
    description:
    - If set to true, access to a bucket with a public policy is restricted to only authenticated
      users within the account that bucket belongs to.
    type: bool
    version_added: '1.15.0'
  eradication_mode:
    description:
    - The eradication mode of the bucket.
    type: str
    choices: [ "permission-based", "retention-based" ]
    version_added: '1.17.0'
  manual_eradication:
    description:
    - The manual eradication status of the bucket. If false, the bucket cannot be eradicated after
      it has been destroyed, unless it is empty. If true, the bucket can be eradicated.
    type: bool
    version_added: '1.17.0'
  eradication_delay:
    description:
    - Minimum eradication delay in days. Automatically eradicate destroyed buckets after
      the delay time passes unless automatic eradication is delayed due to other configuration values.
    - Valid values are integer days from 1 to 30. Default is 1.
    type: int
    version_added: '1.17.0'
extends_documentation_fragment:
- purestorage.flashblade.purestorage.fb
"""

EXAMPLES = """
- name: Create new bucket named foo in account bar
  purestorage.flashblade.purefb_bucket:
    name: foo
    account: bar
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Delete bucket named foo in account bar
  purestorage.flashblade.purefb_bucket:
    name: foo
    account: bar
    state: absent
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Change bucket versioning state
  purestorage.flashblade.purefb_bucket:
    name: foo
    account: bar
    versioning: enabled
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Recover deleted bucket named foo in account bar
  purestorage.flashblade.purefb_bucket:
    name: foo
    account: bar
    state: present
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Eradicate bucket named foo in account bar
  purestorage.flashblade.purefb_bucket:
    name: foo
    account: bar
    state: absent
    eradicate: true
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641
"""

RETURN = """
"""

HAS_PURITY_FB = True
try:
    from purity_fb import Bucket, Reference, BucketPatch, BucketPost
except ImportError:
    HAS_PURITY_FB = False

HAS_PYPURECLIENT = True
try:
    from pypureclient import flashblade
except ImportError:
    HAS_PYPURECLIENT = False

from ansible.module_utils.basic import AnsibleModule, human_to_bytes
from ansible_collections.purestorage.flashblade.plugins.module_utils.purefb import (
    get_blade,
    get_system,
    purefb_argument_spec,
)


SEC_PER_DAY = 86400000
MIN_REQUIRED_API_VERSION = "1.5"
VERSIONING_VERSION = "1.9"
VSO_VERSION = "2.5"
QUOTA_VERSION = "2.8"
MODE_VERSION = "2.12"
WORM_VERSION = "2.13"


def get_s3acc(module, blade):
    """Return Object Store Account or None"""
    s3acc = None
    accts = blade.object_store_accounts.list_object_store_accounts()
    for acct in range(0, len(accts.items)):
        if accts.items[acct].name == module.params["account"]:
            s3acc = accts.items[acct]
    return s3acc


def get_bucket(module, blade):
    """Return Bucket or None"""
    s3bucket = None
    buckets = blade.buckets.list_buckets()
    for bucket in range(0, len(buckets.items)):
        if buckets.items[bucket].name == module.params["name"]:
            s3bucket = buckets.items[bucket]
    return s3bucket


def create_bucket(module, blade):
    """Create bucket"""
    changed = True
    bladev2 = get_system(module)
    if not module.check_mode:
        try:
            api_version = blade.api_version.list_versions().versions
            if VSO_VERSION in api_version:
                account_defaults = list(
                    bladev2.get_object_store_accounts(
                        names=[module.params["account"]]
                    ).items
                )[0]
                if QUOTA_VERSION in api_version:
                    if not module.params["hard_limit"]:
                        module.params["hard_limit"] = (
                            account_defaults.hard_limit_enabled
                        )
                    if module.params["quota"]:
                        quota = str(human_to_bytes(module.params["quota"]))
                    else:
                        if not account_defaults.quota_limit:
                            quota = ""
                        else:
                            quota = str(account_defaults.quota_limit)
                    if not module.params["retention_mode"]:
                        module.params["retention_mode"] = ""
                    if not module.params["default_retention"]:
                        module.params["default_retention"] = ""
                    else:
                        module.params["default_retention"] = str(
                            int(module.params["default_retention"]) * 86400000
                        )
                    if module.params["object_lock_enabled"]:
                        bucket = flashblade.BucketPost(
                            account=flashblade.Reference(name=module.params["account"]),
                            bucket_type=module.params["mode"],
                            hard_limit_enabled=module.params["hard_limit"],
                            quota_limit=quota,
                        )
                    else:
                        bucket = flashblade.BucketPost(
                            account=flashblade.Reference(name=module.params["account"]),
                            bucket_type=module.params["mode"],
                            hard_limit_enabled=module.params["hard_limit"],
                            quota_limit=quota,
                        )
                else:
                    bucket = flashblade.BucketPost(
                        account=flashblade.Reference(name=module.params["account"]),
                        bucket_type=module.params["mode"],
                    )
                res = bladev2.post_buckets(names=[module.params["name"]], bucket=bucket)
                if res.status_code != 200:
                    module.fail_json(
                        msg="Object Store Bucket {0} creation failed. Error: {1}".format(
                            module.params["name"],
                            res.errors[0].message,
                        )
                    )
                if QUOTA_VERSION in api_version:
                    bucket = flashblade.BucketPatch(
                        retention_lock=module.params["retention_lock"],
                        object_lock_config=flashblade.ObjectLockConfigRequestBody(
                            default_retention_mode=module.params["retention_mode"],
                            enabled=module.params["object_lock_enabled"],
                            freeze_locked_objects=module.params[
                                "freeze_locked_objects"
                            ],
                            default_retention=module.params["default_retention"],
                        ),
                        versioning=module.params["versioning"],
                    )
                else:
                    bucket = flashblade.BucketPatch(
                        retention_lock=module.params["retention_lock"],
                        versioning=module.params["versioning"],
                    )
                res = bladev2.patch_buckets(
                    names=[module.params["name"]], bucket=bucket
                )
                if res.status_code != 200:
                    module.fail_json(
                        msg="Object Store Bucket {0} creation update failed. Error: {1}".format(
                            module.params["name"],
                            res.errors[0].message,
                        )
                    )
            else:
                attr = BucketPost()
                attr.account = Reference(name=module.params["account"])
                blade.buckets.create_buckets(names=[module.params["name"]], bucket=attr)
                if module.params["versioning"] != "absent":
                    try:
                        blade.buckets.update_buckets(
                            names=[module.params["name"]],
                            bucket=BucketPatch(versioning=module.params["versioning"]),
                        )
                    except Exception:
                        module.fail_json(
                            msg="Object Store Bucket {0} Created but versioning state failed".format(
                                module.params["name"]
                            )
                        )
        except Exception:
            blade.buckets.update_buckets(
                names=[module.params["name"]], bucket=BucketPatch(destroyed=True)
            )
            blade.buckets.delete_buckets(names=[module.params["name"]])
            module.fail_json(
                msg="Object Store Bucket {0}: Creation failed".format(
                    module.params["name"]
                )
            )
        if MODE_VERSION in api_version:
            if not module.params["block_new_public_policies"]:
                module.params["block_new_public_policies"] = False
            if not module.params["block_public_access"]:
                module.params["block_public_access"] = False
            pac = BucketPatch(
                public_access_config=flashblade.PublicAccessConfig(
                    block_new_public_policies=module.params[
                        "block_new_public_policies"
                    ],
                    block_public_access=module.params["block_public_access"],
                )
            )
            res = bladev2.patch_buckets(bucket=pac, names=[module.params["name"]])
            if res.status_code != 200:
                module.warn(
                    msg="Failed to set Public Access config correctly for bucket {0}. "
                    "Error: {1}".format(module.params["name"], res.errors[0].message)
                )
        if WORM_VERSION in api_version and module.params["eradication_mode"]:
            if not module.params["eradication_delay"]:
                module.params["eradication_delay"] = SEC_PER_DAY
            else:
                module.params["eradication_delay"] = (
                    module.params["eradication_delay"] * SEC_PER_DAY
                )
            if not module.params["manual_eradication"]:
                module.params["manual_eradication"] = "disabled"
            else:
                module.params["manual_eradication"] = "enabled"
            worm = BucketPatch(
                eradication_config=flashblade.BucketEradicationConfig(
                    manual_eradication=module.params["manual_eradication"],
                    eradication_mode=module.params["eradication_mode"],
                    eradication_delay=module.params["eradication_delay"],
                )
            )
            res = bladev2.patch_buckets(bucket=worm, names=[module.params["name"]])
            if res.status_code != 200:
                module.warn(
                    msg="Failed to set Bucket Eradication config correctly for bucket {0}. "
                    "Error: {1}".format(module.params["name"], res.errors[0].message)
                )
    module.exit_json(changed=changed)


def delete_bucket(module, blade):
    """Delete Bucket"""
    changed = True
    if not module.check_mode:
        try:
            api_version = blade.api_version.list_versions().versions
            if VERSIONING_VERSION in api_version:
                blade.buckets.update_buckets(
                    names=[module.params["name"]], bucket=BucketPatch(destroyed=True)
                )
            else:
                blade.buckets.update_buckets(
                    names=[module.params["name"]], destroyed=Bucket(destroyed=True)
                )
            if module.params["eradicate"]:
                try:
                    blade.buckets.delete_buckets(names=[module.params["name"]])
                except Exception:
                    module.fail_json(
                        msg="Object Store Bucket {0}: Eradication failed".format(
                            module.params["name"]
                        )
                    )
        except Exception:
            module.fail_json(
                msg="Object Store Bucket {0}: Deletion failed".format(
                    module.params["name"]
                )
            )
    module.exit_json(changed=changed)


def recover_bucket(module, blade):
    """Recover Bucket"""
    changed = True
    if not module.check_mode:
        try:
            api_version = blade.api_version.list_versions().versions
            if VERSIONING_VERSION in api_version:
                blade.buckets.update_buckets(
                    names=[module.params["name"]], bucket=BucketPatch(destroyed=False)
                )
            else:
                blade.buckets.update_buckets(
                    names=[module.params["name"]], destroyed=Bucket(destroyed=False)
                )
        except Exception:
            module.fail_json(
                msg="Object Store Bucket {0}: Recovery failed".format(
                    module.params["name"]
                )
            )
    module.exit_json(changed=changed)


def update_bucket(module, blade, bucket):
    """Update Bucket"""
    changed = False
    change_pac = False
    change_worm = False
    bladev2 = get_system(module)
    bucket_detail = list(bladev2.get_buckets(names=[module.params["name"]]).items)[0]
    api_version = blade.api_version.list_versions().versions
    if VSO_VERSION in api_version:
        if module.params["mode"] and bucket_detail.bucket_type != module.params["mode"]:
            module.warn("Changing bucket type is not permitted.")
        if QUOTA_VERSION in api_version:
            if (
                bucket_detail.retention_lock == "ratcheted"
                and getattr(
                    bucket_detail.object_lock_config, "default_retention_mode", None
                )
                == "compliance"
                and module.params["retention_mode"] != "compliance"
            ):
                module.warn(
                    "Changing retention_mode can only be performed by Pure Technical Support."
                )
        if not module.params["object_lock_enabled"] and getattr(
            bucket_detail.object_lock_config, "enabled", False
        ):
            module.warn("Object lock cannot be disabled.")
        if not module.params["freeze_locked_objects"] and getattr(
            bucket_detail.object_lock_config, "freeze_locked_objects", False
        ):
            module.warn("Freeze locked onjects cannot be disabled.")
        if getattr(bucket_detail.object_lock_config, "default_retention", 0) > 1:
            if (
                bucket_detail.object_lock_config.default_retention / 86400000
                > int(module.params["default_retention"])
                and bucket_detail.retention_lock == "ratcheted"
            ):
                module.warn(
                    "Default retention can only be reduced by Pure Technical Support."
                )

    if VERSIONING_VERSION in api_version:
        if bucket.versioning != "none":
            if module.params["versioning"] == "absent":
                versioning = "suspended"
            else:
                versioning = module.params["versioning"]
            if bucket.versioning != versioning:
                changed = True
                if not module.check_mode:
                    try:
                        blade.buckets.update_buckets(
                            names=[module.params["name"]],
                            bucket=BucketPatch(versioning=versioning),
                        )
                        changed = True
                    except Exception:
                        module.fail_json(
                            msg="Object Store Bucket {0}: Versioning change failed".format(
                                module.params["name"]
                            )
                        )
        elif module.params["versioning"] != "absent":
            changed = True
            if not module.check_mode:
                try:
                    blade.buckets.update_buckets(
                        names=[module.params["name"]],
                        bucket=BucketPatch(versioning=module.params["versioning"]),
                    )
                    changed = True
                except Exception:
                    module.fail_json(
                        msg="Object Store Bucket {0}: Versioning change failed".format(
                            module.params["name"]
                        )
                    )
    if MODE_VERSION in api_version:
        current_pac = {
            "block_new_public_policies": bucket_detail.public_access_config.block_new_public_policies,
            "block_public_access": bucket_detail.public_access_config.block_public_access,
        }
        if module.params["block_new_public_policies"] is None:
            new_public_policies = current_pac["block_new_public_policies"]
        else:
            new_public_policies = module.params["block_new_public_policies"]
        if module.params["block_public_access"] is None:
            new_public_access = current_pac["block_public_access"]
        else:
            new_public_access = module.params["block_public_access"]
        new_pac = {
            "block_new_public_policies": new_public_policies,
            "block_public_access": new_public_access,
        }
        if current_pac != new_pac:
            change_pac = True
            pac = BucketPatch(
                public_access_config=flashblade.PublicAccessConfig(
                    block_new_public_policies=new_pac.block_new_public_policies,
                    block_public_access=new_pac.block_public_access,
                )
            )
        if change_pac and not module.check_mode:
            res = bladev2.patch_buckets(bucket=pac, names=[module.params["name"]])
            if res.status_code != 200:
                module.fail_json(
                    msg="Failed to update Public Access config correctly for bucket {0}. "
                    "Error: {1}".format(module.params["name"], res.errors[0].message)
                )
    if WORM_VERSION in api_version:
        current_worm = {
            "eradication_delay": bucket_detail.eradication_config.eradication_delay,
            "manual_eradication": bucket_detail.eradication_config.manual_eradication,
            "eradication_mode": bucket_detail.eradication_config.eradication_mode,
        }
        if module.params["eradication_delay"] is None:
            new_delay = current_worm["eradication_delay"]
        else:
            new_delay = module.params["eradication_delay"] * SEC_PER_DAY
        if module.params["manual_eradication"] is None:
            new_manual = current_worm["manual_eradication"]
        else:
            if module.params["manual_eradication"]:
                new_manual = "enabled"
            else:
                new_manual = "disabled"
        if (
            module.params["eradication_mode"]
            and module.params["eradication_mode"] != current_worm["eradication_mode"]
        ):
            new_mode = module.params["eradication_mode"]
        else:
            new_mode = current_worm["eradication_mode"]
        new_worm = {
            "eradication_delay": new_delay,
            "manual_eradication": new_manual,
            "eradication_mode": new_mode,
        }
        if current_worm != new_worm:
            change_worm = True
            worm = BucketPatch(
                public_access_config=flashblade.BucketEradicationConfig(
                    eradication_delay=new_worm.eradication_delay,
                    manual_eradication=new_worm.manual_eradication,
                    eradication_mode=new_worm.eradication_mode,
                )
            )
        if change_worm and not module.check_mode:
            res = bladev2.patch_buckets(bucket=worm, names=[module.params["name"]])
            if res.status_code != 200:
                module.fail_json(
                    msg="Failed to update Eradication config correctly for bucket {0}. "
                    "Error: {1}".format(module.params["name"], res.errors[0].message)
                )
    module.exit_json(changed=(changed or change_pac or change_worm))


def eradicate_bucket(module, blade):
    """Eradicate Bucket"""
    changed = True
    if not module.check_mode:
        try:
            blade.buckets.delete_buckets(names=[module.params["name"]])
        except Exception:
            module.fail_json(
                msg="Object Store Bucket {0}: Eradication failed".format(
                    module.params["name"]
                )
            )
    module.exit_json(changed=changed)


def main():
    argument_spec = purefb_argument_spec()
    argument_spec.update(
        dict(
            name=dict(required=True),
            account=dict(required=True),
            eradicate=dict(default="false", type="bool"),
            mode=dict(
                type="str",
                choices=["classic", "multi-site-writable"],
            ),
            retention_mode=dict(
                type="str", choices=["compliance", "governance", "safemode", ""]
            ),
            default_retention=dict(type="str"),
            retention_lock=dict(
                type="str", choices=["ratcheted", "unlocked"], default="unlocked"
            ),
            hard_limit=dict(type="bool"),
            block_new_public_policies=dict(type="bool"),
            block_public_access=dict(type="bool"),
            object_lock_enabled=dict(type="bool", default=False),
            freeze_locked_objects=dict(type="bool", default=False),
            quota=dict(type="str"),
            versioning=dict(
                default="absent", choices=["enabled", "suspended", "absent"]
            ),
            state=dict(default="present", choices=["present", "absent"]),
            eradication_delay=dict(type="int"),
            eradication_mode=dict(
                type="str", choices=["permission-based", "retention-based"]
            ),
            manual_eradication=dict(type="bool"),
        )
    )

    module = AnsibleModule(argument_spec, supports_check_mode=True)

    if not HAS_PURITY_FB:
        module.fail_json(msg="purity_fb sdk is required for this module")
    if module.params["mode"]:
        if not HAS_PYPURECLIENT:
            module.fail_json(msg="py-pure-client sdk is required to support VSO mode")

    if (
        module.params["eradication_delay"]
        and not 30 >= module.params["eradication_delay"] >= 1
    ):
        module.fail_json(msg="Eradication Delay must be between 1 and 30 days.")

    state = module.params["state"]
    blade = get_blade(module)
    api_version = blade.api_version.list_versions().versions
    if MIN_REQUIRED_API_VERSION not in api_version:
        module.fail_json(msg="Purity//FB must be upgraded to support this module.")

    # From REST 2.12 classic is no longer the default mode
    if MODE_VERSION in api_version:
        if not module.params["mode"]:
            module.params["mode"] = "multi-site-writable"
    elif not module.params["mode"]:
        module.params["mode"] = "classic"
    bucket = get_bucket(module, blade)
    if not get_s3acc(module, blade):
        module.fail_json(
            msg="Object Store Account {0} does not exist.".format(
                module.params["account"]
            )
        )

    if module.params["eradicate"] and state == "present":
        module.warn("Eradicate flag ignored without state=absent")

    if state == "present" and not bucket:
        create_bucket(module, blade)
    elif state == "present" and bucket and bucket.destroyed:
        recover_bucket(module, blade)
    elif state == "absent" and bucket and not bucket.destroyed:
        delete_bucket(module, blade)
    elif state == "present" and bucket:
        update_bucket(module, blade, bucket)
    elif (
        state == "absent" and bucket and bucket.destroyed and module.params["eradicate"]
    ):
        eradicate_bucket(module, blade)
    elif state == "absent" and not bucket:
        module.exit_json(changed=False)

    module.exit_json(changed=False)


if __name__ == "__main__":
    main()
