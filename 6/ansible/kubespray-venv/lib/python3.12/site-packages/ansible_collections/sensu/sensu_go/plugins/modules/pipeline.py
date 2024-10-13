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
API_VERSION = dict(v1="pipeline/v1", v2="core/v2")
HANDLER_TYPE = dict(handler="Handler", tcp_stream_handler="TCPStreamHandler", sumo_logic_metrics_handler="SumoLogicMetricsHandler")
MUTATOR_TYPE = dict(mutator="Mutator")
FILTER_TYPE = dict(event_filter="EventFilter")

DOCUMENTATION = '''
module: pipeline
author:
  - Domen Dobnikar (@domen_dobnikar)
short_description: Manage Sensu pipeline
description:
  - Create, update or delete a Sensu pipeline.
  - For more information, refer to the Sensu documentation at
    U(https://docs.sensu.io/sensu-go/latest/observability-pipeline/observe-process/pipelines/).
version_added: 1.14.0
extends_documentation_fragment:
  - sensu.sensu_go.auth
  - sensu.sensu_go.name
  - sensu.sensu_go.namespace
  - sensu.sensu_go.state
  - sensu.sensu_go.labels
seealso:
  - module: sensu.sensu_go.socket_handler
  - module: sensu.sensu_go.handler_info
  - module: sensu.sensu_go.pipe_handler
  - module: sensu.sensu_go.filter
  - module: sensu.sensu_go.filter_info
  - module: sensu.sensu_go.mutator
  - module: sensu.sensu_go.mutator_info
options:
  workflows:
    description:
      - Array of workflows (by names) to use when filtering, mutating, and handling observability events with a pipeline.
    type: list
    elements: dict
    suboptions:
      name:
        description:
          - Name of the Sensu pipeline workflow.
        type: str
        required: true
      filters:
        description:
          - Reference for the Sensu event filters to use when filtering events for the pipeline.
          - Each pipeline workflow can reference more than one event filter.
          - If a workflow has more than one filter, Sensu applies the filters in a series, starting with the filter that is listed first.
        type: list
        elements: dict
        suboptions:
          name:
            description:
              - Name of the Sensu event filter to use for the workflow.
              - You can use the built-in event filters, as well as your existing event filters, in pipeline workflows.
            type: str
            required: true
          type:
            description:
              - The sensuctl create resource type for the event filter.
              - Event filters should always be type EventFilter.
            type: str
            default: event_filter
            choices: [ event_filter ]
      mutator:
        description:
          - Reference for the Sensu mutator to use to mutate event data for the workflow.
          - Each pipeline workflow can reference only one mutator.
        type: dict
        suboptions:
          name:
            description:
              - Name of the Sensu mutator to use for the workflow.
              - You can use your existing mutators in pipeline workflows.
            type: str
            required: true
          type:
            description:
              - The sensuctl create resource type for the mutator.
              - Mutators should always be type Mutator.
            type: str
            default: mutator
            choices: [ mutator ]
      handler:
        description:
          - Reference for the Sensu handler to use for event processing in the workflow.
          - Each pipeline workflow must reference one handler.
          - Pipelines ignore any filters and mutators specified in handler definitions.
        type: dict
        required: true
        suboptions:
          name:
            description:
              - Name of the Sensu handler to use for the workflow.
              - You can use your existing handlers in pipeline workflows.
              - Pipelines ignore any filters and mutators specified in handler definitions.
            type: str
            required: true
          type:
            description:
              - The sensuctl create resource type for the handler.
            type: str
            required: true
            choices: [ handler, tcp_stream_handler, sumo_logic_metrics_handler ]
'''

EXAMPLES = '''
- name: Create a pipeline
  sensu.sensu_go.pipeline:
    name: this_pipeline
    workflows:
      - name: this-wf
        handler:
          name: this_handler
          type: tcp_stream_handler
        filters:
          - name: this_filter
          - name: this_filter_2
        mutator:
          name: this_mutator

- name: Delete pipeline
  sensu.sensu_go.pipeline:
    name: this_pipeline
    state: absent
'''

RETURN = '''
object:
  description: Object representing Sensu pipeline.
  returned: success
  type: dict
  sample:
    metadata:
      created_by: admin
      name: this_pipeline
      namespace: default
    workflows:
      - filters:
          - api_version: core/v2
            name: this_filter
            type: EventFilter
          - api_version: core/v2
            name: this_filter_2
            type: EventFilter
        handler:
          api_version: pipeline/v1
          name: this_handler
          type: TCPStreamHandler
        mutator:
          api_version: core/v2
          name: this_mutator
          type: Mutator
        name: this-wf
'''

from ansible.module_utils.basic import AnsibleModule

from ..module_utils import arguments, errors, utils


def do_differ(current, desired):
    return (
        utils.do_differ(current, desired, "pipelines")
    )


def handle_mutator_api_and_type(payload_mutator):
    payload_mutator["type"] = MUTATOR_TYPE[payload_mutator["type"]]
    payload_mutator["api_version"] = API_VERSION["v2"]


def handle_filter_api_and_type(payload_filters, workflow):
    filter_count = 0
    for filter in workflow["filters"]:
        payload_filters[filter_count]["type"] = FILTER_TYPE[filter["type"]]
        payload_filters[filter_count]["api_version"] = API_VERSION["v2"]
        filter_count += 1


def handle_handler_api_and_type(payload_handler):
    if payload_handler["type"] in ["tcp_stream_handler", "sumo_logic_metrics_handler"]:
        payload_handler["api_version"] = API_VERSION["v1"]
    else:
        payload_handler["api_version"] = API_VERSION["v2"]
    payload_handler["type"] = HANDLER_TYPE[payload_handler["type"]]


def handle_api_version_and_types(module, payload):
    payload_count = 0
    for workflow in module.params["workflows"]:
        # HANDLER
        handle_handler_api_and_type(payload["workflows"][payload_count]["handler"])

        # MUTATOR
        if workflow.get("mutator"):
            handle_mutator_api_and_type(payload["workflows"][payload_count]["mutator"])
        elif "mutator" in payload["workflows"][payload_count]:
            payload["workflows"][payload_count].pop("mutator")

        # FILTERS
        if workflow.get("filters"):
            handle_filter_api_and_type(
                payload["workflows"][payload_count]["filters"], workflow)
        elif "filters" in payload["workflows"][payload_count]:
            payload["workflows"][payload_count].pop("filters")
        payload_count += 1


def main():
    required_if = [
        ('state', 'present', ['workflows'])
    ]
    module = AnsibleModule(
        required_if=required_if,
        supports_check_mode=True,
        argument_spec=dict(
            arguments.get_spec(
                "auth", "name", "state", "namespace", "labels",
            ),
            workflows=dict(
                type="list",
                elements="dict",
                options=dict(
                    name=dict(
                        type="str",
                        required=True,
                    ),
                    filters=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            name=dict(
                                type="str",
                                required=True,
                            ),
                            type=dict(
                                type="str",
                                default="event_filter",
                                choices=[
                                    "event_filter",
                                ],
                            ),
                        ),
                    ),
                    mutator=dict(
                        type="dict",
                        options=dict(
                            name=dict(
                                type="str",
                                required=True,
                            ),
                            type=dict(
                                type="str",
                                default="mutator",
                                choices=[
                                    "mutator",
                                ],
                            ),
                        ),
                    ),
                    handler=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            name=dict(
                                type="str",
                                required=True,
                            ),
                            type=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "handler",
                                    "tcp_stream_handler",
                                    "sumo_logic_metrics_handler"
                                ],
                            ),
                        ),
                    ),
                ),
            ),
        ),
    )
    client = arguments.get_sensu_client(module.params['auth'])
    path = utils.build_core_v2_path(
        module.params['namespace'], 'pipelines', module.params['name'],
    )
    payload = arguments.get_mutation_payload(
        module.params, 'workflows'
    )
    if module.params["state"] == "present":
        handle_api_version_and_types(module, payload)
    try:
        changed, handler = utils.sync(
            module.params['state'], client, path, payload, module.check_mode,
            do_differ,
        )
        module.exit_json(changed=changed, object=handler)
    except errors.Error as e:
        module.fail_json(msg=str(e))


if __name__ == '__main__':
    main()
