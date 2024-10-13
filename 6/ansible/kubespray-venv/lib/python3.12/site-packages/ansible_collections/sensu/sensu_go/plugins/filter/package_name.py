# -*- coding: utf-8 -*-
# Copyright: (c) 2020, XLAB Steampunk <steampunk@xlab.si>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
  name: package_name
  author: Tadej Borovsak (@tadeboro)
  version_added: 1.13.2
  short_description: Format package name
  description:
    - Package name format function.
    - The return value is a string respresenting package name and build version.
  positional: _input
  options:
    _input:
      description: Package type.
      choices: [ apt, yum ]
      type: string
      required: true
    name:
      description: Package name.
      type: string
      required: true
    version:
      description: Package version.
      type: string
      required: true
    build:
      description: Package build.
      type: string
      required: true
'''

EXAMPLES = '''
  - name: Install apt component
    apt:
      name: "{{ 'apt' | sensu.sensu_go.package_name(name, version, build) }}"

  - name: Install yum component
    yum:
      name: "{{ 'yum' | sensu.sensu_go.package_name(name, version, build) }}"
'''

RETURN = '''
  _value:
    description: Package name, version and build as a formatted string.
    type: string
'''


def _apt_package_name(name, version, build):
    if version == "latest":
        return name
    if build == "latest":
        return "{0}={1}-*".format(name, version)
    return "{0}={1}-{2}".format(name, version, build)


def _yum_package_name(name, version, build):
    if version == "latest":
        return name
    if build == "latest":
        return "{0}-{1}".format(name, version)
    return "{0}-{1}-{2}".format(name, version, build)


KIND_HANDLERS = dict(
    apt=_apt_package_name,
    yum=_yum_package_name,
)


def package_name(kind, name, version, build):
    return KIND_HANDLERS[kind](name, version, build)


class FilterModule(object):
    def filters(self):
        return dict(
            package_name=package_name,
        )
