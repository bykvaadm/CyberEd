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
module: pipeline_info
author:
  - Domen Dobnikar (@domen_dobnikar)
short_description: List available Sensu pipelines.
description:
  - Retrieve information about Sensu Go pipelines.
  - For more information, refer to the Sensu documentation at
    U(https://docs.sensu.io/sensu-go/latest/observability-pipeline/observe-process/pipelines/).
version_added: 1.14.0
extends_documentation_fragment:
  - sensu.sensu_go.requirements
  - sensu.sensu_go.auth
  - sensu.sensu_go.namespace

seealso:
  - module: sensu.sensu_go.socket_handler
  - module: sensu.sensu_go.handler_info
  - module: sensu.sensu_go.pipe_handler
  - module: sensu.sensu_go.filter
  - module: sensu.sensu_go.filter_info
  - module: sensu.sensu_go.mutator
  - module: sensu.sensu_go.mutator_info
options:
  name:
    description:
      - Name of a specific pipeline.
    type: str
'''

EXAMPLES = '''
- name: List all Sensu pipelines
  sensu.sensu_go.pipeline_info:
  register: result

- name: List the selected Sensu pipeline
  sensu.sensu_go.pipeline_info:
    name: my_pipeline
  register: result
'''

RETURN = """
objects:
  description: List of Sensu pipelines.
  returned: success
  type: list
  elements: dict
  sample:
    - metadata:
        created_by: admin
        name: this_pipeline
        namespace: default
      workflows: null
    - metadata:
        created_by: admin
        name: this_pipeline_1
        namespace: default
      workflows:
      - handler:
          api_version: core/v2
          name: best_handler_1
          type: Handler
        name: best_workflow_1
    - metadata:
        created_by: admin
        name: this_pipeline_2
        namespace: default
      workflows:
      - handler:
          api_version: core/v2
          name: best_handler_2
          type: Handler
        name: best_workflow_1
"""

from ansible.module_utils.basic import AnsibleModule

from ..module_utils import arguments, errors, utils


def main():
    module = AnsibleModule(
        supports_check_mode=True,
        argument_spec=dict(
            arguments.get_spec("auth", "namespace"),
            name=dict(),  # Name is not required in info modules.
        ),
    )

    client = arguments.get_sensu_client(module.params["auth"])
    path = utils.build_core_v2_path(
        module.params["namespace"], "pipelines", module.params["name"],
    )
    try:
        handlers = utils.prepare_result_list(utils.get(client, path))
    except errors.Error as e:
        module.fail_json(msg=str(e))

    module.exit_json(changed=False, objects=handlers)


if __name__ == '__main__':
    main()
