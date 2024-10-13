from __future__ import absolute_import, division, print_function

__metaclass__ = type

try:
    import fusion as purefusion
except ImportError:
    pass

from ansible_collections.purestorage.fusion.plugins.module_utils.operations import (
    await_operation,
)


def delete_snapshot(fusion, snap, snapshots_api):
    patch = purefusion.SnapshotPatch(destroyed=purefusion.NullableBoolean(True))
    op = snapshots_api.update_snapshot(
        body=patch,
        tenant_name=snap.tenant.name,
        tenant_space_name=snap.tenant_space.name,
        snapshot_name=snap.name,
    )
    await_operation(fusion, op)
    op = snapshots_api.delete_snapshot(
        tenant_name=snap.tenant.name,
        tenant_space_name=snap.tenant_space.name,
        snapshot_name=snap.name,
    )
    await_operation(fusion, op)
