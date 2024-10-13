#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2019, XLAB Steampunk <steampunk@xlab.si>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["stableinterface"],
    "supported_by": "certified",
}

DOCUMENTATION = '''
module: datastore
author:
  - Manca Bizjak (@mancabizjak)
  - Tadej Borovsak (@tadeboro)
short_description: Manage Sensu external datastore providers
description:
  - Add or remove external datastore provider.
  - For more information, refer to the Sensu documentation at
    U(https://docs.sensu.io/sensu-go/latest/reference/datastore/).
version_added: 1.1.0
extends_documentation_fragment:
  - sensu.sensu_go.requirements
  - sensu.sensu_go.auth
  - sensu.sensu_go.name
  - sensu.sensu_go.state
seealso:
  - module: sensu.sensu_go.datastore_info
options:
  dsn:
    description:
      - Attribute that specifies the data source names as a URL or
        PostgreSQL connection string. See the PostgreSQL docs for more
        information about connection strings.
    type: str
  pool_size:
    description:
      - The maximum number of connections to hold in the PostgreSQL connection
        pool.
    type: int
  max_conn_lifetime:
    description:
      - Maximum time a connection can persist before being destroyed.
    type: str
  max_idle_conns:
    description:
      - Maximum number of number of idle connections to retain.
    type: int
    default: 2
  batch_workers:
    description:
      - Number of Goroutines sending data to PostgreSQL, as specified in the PostgreSQL configuration.
      - Set to current PostgreSQL pool size as default.
    type: int
  batch_buffer:
    description:
      - Maximum number of requests to buffer in memory.
    type: int
    default: 0
  batch_size:
    description:
      - Number of requests in each PostgreSQL write transaction, as specified in the PostgreSQL configuration.
    type: int
    default: 1
  enable_round_robin:
    description:
      - Enables round robin scheduling on PostgreSQL.
      - Any existing round robin scheduling will stop and migrate to PostgreSQL as entities check in with keepalives.
      - Sensu will gradually delete the existing etcd scheduler state as keepalives on the etcd scheduler keys expire over time.
    type: bool
    default: false
  strict:
    description:
      - When the PostgresConfig resource is created, configuration validation will include connecting to the PostgreSQL database
        and executing a query to confirm whether the connected user has permission to create database tables.
      - Sensu-backend will try to connect to PostgreSQL indefinitely at 5-second intervals instead of reverting to etcd after 3 attempts.
      - We recommend setting strict to true in most cases. If the connection fails or the user does not have permission to
        create database tables, resource configuration will fail and the configuration will not be persisted.
        This extended configuration is useful for debugging when you are not sure whether the configuration
        is correct or the database is working properly.
    type: bool
    default: false
notes:
  - Currently, only one external datastore can be active at a time. The module
    will fail to perform its operation if this would break that invariant.
'''

EXAMPLES = '''
- name: Add external datastore
  sensu.sensu_go.datastore:
    name: my-postgres
    dsn: postgresql://user:secret@host:port/dbname

- name: Remove external datastore
  sensu.sensu_go.datastore:
    name: my-postgres
    state: absent

- name: Add external datastore with pool_size and max_conn_lifetime specified
  sensu.sensu_go.datastore:
    name: my-postgres
    dsn: postgresql://user:secret@host:port/dbname
    pool_size: 1
    max_conn_lifetime: "5m30s"
'''

RETURN = '''
object:
  description: Object representing external datastore provider.
  returned: success
  type: dict
  sample:
    metadata:
      name: my-postgres
    batch_buffer: 0
    batch_size: 1
    batch_workers: 0
    dsn: "postgresql://user:secret@host:port/dbname"
    max_conn_lifetime: 5m
    max_idle_conns: 2
    pool_size: 20
    strict: true
    enable_round_robin: true
'''

from ansible.module_utils.basic import AnsibleModule

from ..module_utils import arguments, errors, utils

API_GROUP = "enterprise"
API_VERSION = "store/v1"


def _get(client, path):
    return utils.convert_v1_to_v2_response(utils.get(client, path))


def sync(state, client, list_path, resource_path, payload, check_mode):
    datastore = _get(client, resource_path)

    # When we are deleting stores, we do not care if there is more than one
    # datastore present. We just make sure the currently manipulated store is
    # gone. This makes our module useful in "let us clean up the mess"
    # scenarios.
    if state == "absent" and datastore is None:
        return False, None

    if state == "absent":
        if not check_mode:
            utils.delete(client, resource_path)
        return True, None

    # If the store exists, update it and ignore the fact that there might be
    # more than one present.
    if datastore:
        if utils.do_differ(datastore, payload["spec"]):
            if check_mode:
                return True, payload["spec"]
            utils.put(client, resource_path, payload)
            return True, _get(client, resource_path)
        return False, datastore

    # When adding a new datastore, we first make sure there is no other
    # datastore present because we do not want to be the ones who brought
    # backends into an inconsistent state.
    if utils.get(client, list_path):
        raise errors.Error("Some other external datastore is already active.")

    if check_mode:
        return True, payload["spec"]
    utils.put(client, resource_path, payload)
    return True, _get(client, resource_path)


def main():
    required_if = [
        ("state", "present", ["dsn"])
    ]
    module = AnsibleModule(
        required_if=required_if,
        supports_check_mode=True,
        argument_spec=dict(
            arguments.get_spec("auth", "name", "state"),
            dsn=dict(),
            pool_size=dict(
                type="int",
                default=0,
            ),
            max_conn_lifetime=dict(
                type="str",
            ),
            max_idle_conns=dict(
                type="int",
                default=2,
            ),
            batch_workers=dict(
                type="int",
            ),
            batch_buffer=dict(
                type="int",
                default=0,
            ),
            batch_size=dict(
                type="int",
                default=1,
            ),
            enable_round_robin=dict(
                type="bool",
                default=False,
            ),
            strict=dict(
                type="bool",
                default=False,
            ),
        ),
    )
    client = arguments.get_sensu_client(module.params["auth"])
    list_path = utils.build_url_path(API_GROUP, API_VERSION, None, "provider")
    resource_path = utils.build_url_path(
        API_GROUP, API_VERSION, None, "provider", module.params["name"],
    )
    payload = dict(
        type="PostgresConfig",
        api_version=API_VERSION,
        metadata=dict(name=module.params["name"]),
        spec=arguments.get_spec_payload(module.params, "dsn", "pool_size", "max_conn_lifetime", "max_idle_conns", "batch_workers",
                                        "batch_buffer", "batch_size", "enable_round_robin", "strict"),
    )
    try:
        changed, datastore = sync(
            module.params["state"], client, list_path, resource_path, payload,
            module.check_mode,
        )
        module.exit_json(changed=changed, object=datastore)
    except errors.Error as e:
        module.fail_json(msg=str(e))


if __name__ == '__main__':
    main()
