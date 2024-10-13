# -*- coding: utf-8 -*-
# Copyright: (c) 2019, XLAB Steampunk <steampunk@xlab.si>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
  name: backends
  author: Tadej Borovsak (@tadeboro)
  version_added: 1.13.2
  short_description: Format websocket connection for backends hosts from inventory.
  description:
    - Socket connection format function.
    - Filter backends hosts from ansible inventory groups.
    - The return value is a list of websocket connection addresses.
  positional: _input
  options:
    _input:
      description: Inventory host variables (hostvars).
      type: dict
      required: true
    groups:
      description: List of ansible inventory groups.
      type: list
      required: true
'''

EXAMPLES = '''
  - name: Filter backends from ansible inventory and format a list of websocket connection addresses
    ansible.builtin.debug:
      msg: "{{ hostvars | sensu.sensu_go.backends(groups) }}"
'''

RETURN = '''
  _value:
    description: List of websocket connection addresses.
    type: list
'''


def _format_backend(vars):
    if "api_key_file" in vars:
        protocol = "wss"
    else:
        protocol = "ws"
    return "{0}://{1}:{2}".format(protocol, vars["inventory_hostname"], 8081)


def backends(hostvars, groups):
    return [
        _format_backend(hostvars[name]) for name in groups.get("backends", [])
    ]


class FilterModule(object):
    def filters(self):
        return dict(
            backends=backends,
        )
