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
module: purefa_pod
short_description:  Manage AC pods in Pure Storage FlashArrays
version_added: '1.0.0'
description:
- Manage AC pods in a Pure Storage FlashArray.
author:
- Pure Storage Ansible Team (@sdodsley) <pure-ansible-team@purestorage.com>
options:
  name:
    description:
    - The name of the pod.
    type: str
    required: true
  stretch:
    description:
    - The name of the array to stretch to/unstretch from. Must be synchromously replicated.
    - To unstretch an array use state I(absent)
    - You can only specify a remote array, ie you cannot unstretch a pod from the
      current array and then restretch back to the current array.
    - To restretch a pod you must perform this from the remaining array the pod
      resides on.
    type: str
  failover:
    description:
    - The name of the array given priority to stay online if arrays loose
      contact with eachother.
    - Oprions are either array in the cluster, or I(auto)
    type: list
    elements: str
  state:
    description:
    - Define whether the pod should exist or not.
    default: present
    choices: [ absent, present ]
    type: str
  eradicate:
    description:
    - Define whether to eradicate the pod on delete or leave in trash.
    type: bool
    default: false
  target:
    description:
    - Name of clone target pod.
    type: str
  mediator:
    description:
    - Name of the mediator to use for a pod
    type: str
    default: purestorage
  promote:
    description:
      - Promote/demote any pod not in a stretched relationship. .
      - Demoting a pod will render it read-only.
    required: false
    type: bool
  quiesce:
    description:
      - Quiesce/Skip quiesce when I(promote) is false and demoting an ActiveDR pod.
      - Quiesce will ensure all local data has been replicated before demotion.
      - Skipping quiesce looses all pending data to be replicated to the remote pod.
      - Can only demote the pod if it is in a Acrive DR replica link relationship.
      - This will default to True
    required: false
    type: bool
  undo:
    description:
      - Use the I(undo-remote) pod when I(promote) is true and promoting an ActiveDR pod.
      - This will default to True
    required: false
    type: bool
  quota:
    description:
      - Logical quota limit of the pod in K, M, G, T or P units, or bytes.
    type: str
    version_added: '1.18.0'
  ignore_usage:
    description:
    -  Flag used to override checks for quota management
       operations.
    - If set to true, pod usage is not checked against the
      quota_limits that are set.
    - If set to false, the actual logical bytes in use are prevented
      from exceeding the limits set on the pod.
    - Client operations might be impacted.
    - If the limit exceeds the quota, the operation is not allowed.
    default: false
    type: bool
    version_added: '1.18.0'
  throttle:
    description:
    - Allows pod creation to fail if array health is not optimal
    type: bool
    default: false
    version_added: '1.29.0'
  delete_contents:
    description:
    - This enables you to eradicate pods with contents.
    type: bool
    default: False
    version_added: '1.29.0'
extends_documentation_fragment:
- purestorage.flasharray.purestorage.fa
"""

EXAMPLES = r"""
- name: Create new pod named foo
  purestorage.flasharray.purefa_pod:
    name: foo
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: present

- name: Delete and eradicate pod named foo
  purestorage.flasharray.purefa_pod:
    name: foo
    eradicate: true
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: absent

- name: Set failover array for pod named foo
  purestorage.flasharray.purefa_pod:
    name: foo
    failover:
    - array1
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Set mediator for pod named foo
  purestorage.flasharray.purefa_pod:
    name: foo
    mediator: bar
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Stretch a pod named foo to array2
  purestorage.flasharray.purefa_pod:
    name: foo
    stretch: array2
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Unstretch a pod named foo from array2
  purestorage.flasharray.purefa_pod:
    name: foo
    stretch: array2
    state: absent
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Create clone of pod foo named bar
  purestorage.flasharray.purefa_pod:
    name: foo
    target: bar
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: present
"""

RETURN = r"""
"""

HAS_PURESTORAGE = True
try:
    from pypureclient.flasharray import PodPost, PodPatch, Reference
except ImportError:
    HAS_PURESTORAGE = False

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.purestorage.flasharray.plugins.module_utils.purefa import (
    get_array,
    purefa_argument_spec,
)
from ansible_collections.purestorage.flasharray.plugins.module_utils.common import (
    human_to_bytes,
)
from ansible_collections.purestorage.flasharray.plugins.module_utils.version import (
    LooseVersion,
)

POD_QUOTA_VERSION = "2.23"
THROTTLE_VERSION = "2.31"


def get_pod(module, array):
    """Return Pod or None"""
    try:
        return list(
            array.get_pods(
                names=[module.params["name"]], filter="destroyed='False'"
            ).items
        )[0]
    except Exception:
        return None


def get_undo_pod(module, array):
    """Return Undo Pod or None"""
    try:
        return list(
            array.get_pods(names=[module.params["name"] + ".undo-demote.*"]).items
        )
    except Exception:
        return None


def get_target(module, array):
    try:
        return list(
            array.get_pods(
                names=[module.params["target"]], filter="destroyed='False'"
            ).items
        )[0]
    except Exception:
        return None


def get_destroyed_pod(module, array):
    """Return Destroyed Volume or None"""
    try:
        return bool(
            list(
                array.get_pods(
                    names=[module.params["name"]], filter="destroyed='True'"
                ).items
            )[0]
        )
    except Exception:
        return False


def get_destroyed_target(module, array):
    """Return Destroyed Volume or None"""
    try:
        return bool(
            list(
                array.get_pods(
                    names=[module.params["target"]], filter="destroyed='False'"
                ).items
            )[0]
        )
    except Exception:
        return False


def check_arrays(module, array):
    """Check if array name provided are sync-replicated"""
    good_arrays = []
    good_arrays.append(list(array.get_arrays().items)[0].name)
    connected_arrays = list(array.get_array_connections().items)
    for arr in range(0, len(connected_arrays)):
        if connected_arrays[arr].type == "sync-replication":
            good_arrays.append(connected_arrays[arr].name)
    if module.params["failover"] is not None:
        if module.params["failover"] == ["auto"]:
            failover_array = []
        else:
            failover_array = module.params["failover"]
        if failover_array != []:
            for arr in range(0, len(failover_array)):
                if failover_array[arr] not in good_arrays:
                    module.fail_json(
                        msg="Failover array {0} is not valid.".format(
                            failover_array[arr]
                        )
                    )
    if module.params["stretch"] is not None:
        if module.params["stretch"] not in good_arrays:
            module.fail_json(
                msg="Stretch: Array {0} is not connected.".format(
                    module.params["stretch"]
                )
            )
    return None


def create_pod(module, array):
    """Create Pod"""
    api_version = array.get_rest_version()
    changed = True
    if module.params["target"]:
        module.fail_json(msg="Cannot clone non-existant pod.")
    if not module.check_mode:
        if module.params["failover"]:
            failovers = []
            for fo_array in range(0, len(module.params["failover"])):
                failovers.append(Reference(name=module.params["failover"][fo_array]))
            if LooseVersion(THROTTLE_VERSION) > LooseVersion(api_version):
                res = array.post_pods(
                    names=[module.params["name"]],
                    pod=PodPost(failover_preferences=failovers),
                )
            else:
                res = array.post_pods(
                    names=[module.params["name"]],
                    pod=PodPost(failover_preferences=failovers),
                    allow_throttle=module.params["throttle"],
                )
        else:
            if LooseVersion(THROTTLE_VERSION) > LooseVersion(api_version):
                res = array.post_pods(
                    names=[module.params["name"]],
                    pod=PodPost(),
                )
            else:
                res = array.post_pods(
                    names=[module.params["name"]],
                    pod=PodPost(),
                    allow_throttle=module.params["throttle"],
                )
        if res.status_code != 200:
            module.fail_json(
                msg="Pod {0} creation failed. Error: {1}".format(
                    module.params["name"], res.errors[0].message
                )
            )
        if module.params["mediator"] != "purestorage":
            res = array.patch_pods(
                names=[module.params["name"]],
                pod=PodPatch(mediator=module.params["mediator"]),
            )
            if res.status_code != 200:
                module.warn(
                    "Failed to communicate with mediator {0}, using default value.".format(
                        module.params["mediator"]
                    )
                )
        if module.params["stretch"]:
            current_array = list(array.get_arrays().items)[0].name
            if module.params["stretch"] != current_array:
                res = array.post_pods_arrays(
                    group_names=[module.params["name"]],
                    member_names=[module.params["stretch"]],
                )
                if res.status_code != 200:
                    module.fail_json(
                        msg="Failed to stretch pod {0} to array {1}. Error: {2}".format(
                            module.params["name"],
                            module.params["stretch"],
                            res.errors[0].message,
                        )
                    )
        if module.params["quota"] and LooseVersion(POD_QUOTA_VERSION) <= LooseVersion(
            api_version
        ):
            res = array.patch_pods(
                names=[module.params["name"]],
                pod=PodPatch(quota_limit=human_to_bytes(module.params["quota"])),
            )
            if res.status_code != 200:
                module.fail_json(
                    msg="Failed to apply quota to pod {0}. Error: {1}".format(
                        module.params["name"], res.errors[0].message
                    )
                )
    module.exit_json(changed=changed)


def clone_pod(module, array):
    """Create Pod Clone"""
    api_version = array.get_rest_version()
    changed = False
    if get_target(module, array) is None:
        if not get_destroyed_target(module, array):
            changed = True
            if not module.check_mode:
                if LooseVersion(THROTTLE_VERSION) > LooseVersion(api_version):
                    res = array.post_pods(
                        pod=PodPost(source=Reference(name=module.params["name"])),
                        names=[module.params["target"]],
                    )
                else:
                    res = array.post_pods(
                        pod=PodPost(source=Reference(name=module.params["name"])),
                        names=[module.params["target"]],
                        allow_throttle=module.params["throttle"],
                    )
            if res.status_code != 200:
                module.fail_json(
                    msg="Clone pod {0} to pod {1} failed. Error: {2}".format(
                        module.params["name"],
                        module.params["target"],
                        res.errors[0].message,
                    )
                )
        else:
            module.fail_json(
                msg="Target pod {0} already exists but deleted.".format(
                    module.params["target"]
                )
            )

    module.exit_json(changed=changed)


def update_pod(module, array):
    """Update Pod configuration"""
    api_version = array.get_rest_version()
    changed = False
    current_config = list(array.get_pods(names=[module.params["name"]]).items)[0]
    if module.params["failover"]:
        current_failover = current_config.failover_preference
        if current_failover == [] or sorted(module.params["failover"]) != sorted(
            current_failover
        ):
            changed = True
            if not module.check_mode:
                if module.params["failover"] == ["auto"]:
                    if current_failover != []:
                        res = array.patch_pods(
                            names=[module.params["name"]],
                            pod=PodPatch(failover_preferences=[]),
                        )
                        if res.status_code != 200:
                            module.fail_json(
                                msg="Failed to clear failover preference for pod {0}. Error: {1}".format(
                                    module.params["name"],
                                    res.errors[0].message,
                                )
                            )
                else:
                    failovers = []
                    for fo_array in range(0, len(module.params["failover"])):
                        failovers.append(Reference(module.params["failover"][fo_array]))
                    res = array.patch_pods(
                        names=[module.params["name"]],
                        pod=PodPatch(failover_preferences=failovers),
                    )
                if res.status_code != 200:
                    module.fail_json(
                        msg="Failed to set failover preference for pod {0}. Error: {1}".format(
                            module.params["name"],
                            res.errors[0].message,
                        )
                    )
    if current_config.mediator != module.params["mediator"]:
        changed = True
        if not module.check_mode:
            res = array.patch_pods(
                names=[module.params["name"]],
                pod=PodPatch(mediator=module.params["mediator"]),
            )
            if res.status_code != 200:
                module.warn(
                    "Failed to communicate with mediator {0}. Setting unchanged.i Error: {1}".format(
                        module.params["mediator"],
                        res.errors[0].message,
                    )
                )
    if module.params["promote"] is not None:
        if current_config.array_count > 1:
            module.fail_json(
                msg="Promotion/Demotion not permitted. Pod {0} is stretched".format(
                    module.params["name"]
                )
            )
        else:
            changed = True
            if not module.check_mode:
                if (
                    current_config.promotion_status == "demoted"
                    and module.params["promote"]
                ):
                    if module.params["undo"] is None:
                        module.params["undo"] = True
                    if current_config.promotion_status == "quiescing":
                        module.fail_json(
                            msg="Cannot promote pod {0} as it is still quiesing".format(
                                module.params["name"]
                            )
                        )
                    elif module.params["undo"]:
                        undo_pod = get_undo_pod(module, array)
                        if len(undo_pod) == 1:
                            res = array.patch_pods(
                                names=[module.params["name"]],
                                promote_from=undo_pod[0].name,
                            )
                        else:
                            res = array.patch_pods(
                                names=[module.params["name"]],
                                promote_from=undo_pod[-1].name,
                            )
                            module.warn(
                                "undo-demote pod(s) remaining for {0}. Consider eradicating.".format(
                                    module.params["name"]
                                )
                            )
                    else:
                        res = array.patch_pods(
                            names=[module.params["name"]],
                            pod=PodPatch(requested_promotion_state="promoted"),
                        )
                    if res.status_code != 200:
                        module.fail_json(
                            msg="Failed to promote pod {0}. Error: {1}".format(
                                module.params["name"], res.erroros[0].message
                            )
                        )
                elif (
                    current_config.promotion_status != "demoted"
                    and not module.params["promote"]
                ):
                    if get_undo_pod(module, array):
                        module.fail_json(
                            msg="Cannot demote pod {0} due to associated undo-demote "
                            "pod not being eradicated".format(module.params["name"])
                        )
                    if module.params["quiesce"] is None:
                        module.params["quiesce"] = True
                    if current_config["link_target_count"] == 0:
                        res = array.patch_pods(
                            names=[module.params["name"]],
                            pod=PodPatch(requested_promotion_state="demoted"),
                        )
                    elif not module.params["quiesce"]:
                        res = array.patch_pods(
                            names=[module.params["name"]],
                            pod=PodPatch(requested_promotion_state="demoted"),
                            skip_quiesce=True,
                        )
                    else:
                        res = array.patch_pods(
                            names=[module.params["name"]],
                            pod=PodPatch(requested_promotion_state="demoted"),
                            quiesce=True,
                        )
                if res.status_code != 200:
                    module.fail_json(
                        msg="Failed to demote pod {0}. Error: {1}".format(
                            module.params["name"], res.errors[0].message
                        )
                    )
    if module.params["quota"] and LooseVersion(POD_QUOTA_VERSION) <= LooseVersion(
        api_version
    ):
        quota = human_to_bytes(module.params["quota"])
        if current_config.quota_limit != quota:
            changed = True
            if not module.check_mode:
                res = array.patch_pods(
                    names=[module.params["name"]],
                    pod=PodPatch(
                        quota_limit=quota, ignore_usage=module.params["ignore_usage"]
                    ),
                )
                if res.status_code != 200:
                    module.fail_json(
                        msg="Failed to update quota on pod {0}. Error: {1}".format(
                            module.params["name"], res.errors[0].message
                        )
                    )

    module.exit_json(changed=changed)


def stretch_pod(module, array):
    """Stretch/unstretch Pod configuration"""
    changed = False
    current_config = list(array.get_pods(names=[module.params["name"]]).items)[0]
    if module.params["stretch"]:
        current_arrays = []
        for arr in range(0, len(current_config.arrays)):
            current_arrays.append(current_config.arrays[arr]["name"])
        if (
            module.params["stretch"] not in current_arrays
            and module.params["state"] == "present"
        ):
            changed = True
            if not module.check_mode:
                res = array.post_pods_arrays(
                    group_names=[module.params["name"]],
                    member_names=[module.params["stretch"]],
                )
                if res.status_code != 200:
                    module.fail_json(
                        msg="Failed to stretch pod {0} to array {1}. Error: {2}".format(
                            module.params["name"],
                            module.params["stretch"],
                            res.errors[0].message,
                        )
                    )

        if (
            module.params["stretch"] in current_arrays
            and module.params["state"] == "absent"
        ):
            changed = True
            if not module.check_mode:
                try:
                    array.delete_pods_arrays(
                        group_names=[module.params["name"]],
                        member_names=[module.params["stretch"]],
                    )
                except Exception:
                    module.fail_json(
                        msg="Failed to unstretch pod {0} from array {1}.".format(
                            module.params["name"], module.params["stretch"]
                        )
                    )

    module.exit_json(changed=changed)


def delete_pod(module, array):
    """Delete Pod"""
    changed = True
    if not module.check_mode:
        res = array.patch_pods(
            names=[module.params["name"]], pod=PodPatch(destroyed=True)
        )
        if res.status_code != 200:
            module.fail_json(
                msg="Delete pod {0} failed. Error: {1}".format(
                    module.params["name"], res.errors[0].message
                )
            )
        if module.params["eradicate"]:
            res = array.delete_pods(
                names=[module.params["name"]],
                eradicate_contents=module.params["delete_contents"],
            )
            if res.status_code != 200:
                module.fail_json(
                    msg="Eradicate pod {0} failed. Error: {1}".format(
                        module.params["name"], res.errors[0].message
                    )
                )
    module.exit_json(changed=changed)


def eradicate_pod(module, array):
    """Eradicate Deleted Pod"""
    if module.params["eradicate"]:
        changed = True
        if not module.check_mode:
            res = array.delete_pods(
                names=[module.params["name"]],
                eradicate_contents=module.params["delete_contents"],
            )
            if res.status_code != 200:
                module.fail_json(
                    msg="Eradication of pod {0} failed. Error: {1}".format(
                        module.params["name"], res.errors[0].message
                    )
                )
    module.exit_json(changed=changed)


def recover_pod(module, array):
    """Recover Deleted Pod"""
    changed = True
    if not module.check_mode:
        res = array.patch_pods(
            names=[module.params["name"]], pod=PodPatch(destroyed=False)
        )
        if res.status_code != 200:
            module.fail_json(
                msg="Recovery of pod {0} failed. Error: {1}".format(
                    module.params["name"], res.errors[0].message
                )
            )
    module.exit_json(changed=changed)


def main():
    argument_spec = purefa_argument_spec()
    argument_spec.update(
        dict(
            name=dict(type="str", required=True),
            stretch=dict(type="str"),
            target=dict(type="str"),
            mediator=dict(type="str", default="purestorage"),
            failover=dict(type="list", elements="str"),
            promote=dict(type="bool"),
            undo=dict(type="bool"),
            quiesce=dict(type="bool"),
            eradicate=dict(type="bool", default=False),
            state=dict(type="str", default="present", choices=["absent", "present"]),
            quota=dict(type="str"),
            ignore_usage=dict(type="bool", default=False),
            throttle=dict(type="bool", default=False),
            delete_contents=dict(type="bool", default=False),
        )
    )

    mutually_exclusive = [
        ["stretch", "failover"],
        ["stretch", "eradicate"],
        ["stretch", "mediator"],
        ["target", "mediator"],
        ["target", "stretch"],
        ["target", "failover"],
        ["target", "eradicate"],
    ]

    module = AnsibleModule(
        argument_spec, mutually_exclusive=mutually_exclusive, supports_check_mode=True
    )

    state = module.params["state"]
    array = get_array(module)

    api_version = array.get_rest_version()
    pod = get_pod(module, array)
    destroyed = ""
    if not pod:
        destroyed = get_destroyed_pod(module, array)
    if module.params["failover"] or module.params["failover"] != "auto":
        check_arrays(module, array)

    if state == "present" and not pod:
        create_pod(module, array)
    elif pod and module.params["stretch"]:
        stretch_pod(module, array)
    elif state == "present" and pod and module.params["target"]:
        clone_pod(module, array)
    elif state == "present" and pod and module.params["target"]:
        clone_pod(module, array)
    elif state == "present" and pod:
        update_pod(module, array)
    elif state == "absent" and pod and not module.params["stretch"]:
        delete_pod(module, array)
    elif state == "present" and destroyed:
        recover_pod(module, array)
    elif state == "absent" and destroyed:
        eradicate_pod(module, array)
    elif state == "absent" and not pod:
        module.exit_json(changed=False)


if __name__ == "__main__":
    main()
