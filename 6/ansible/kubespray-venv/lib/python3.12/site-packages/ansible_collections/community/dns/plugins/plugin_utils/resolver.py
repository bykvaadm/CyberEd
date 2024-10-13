# -*- coding: utf-8 -*-

# Copyright (c) 2023, Felix Fontein <felix@fontein.de>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.errors import AnsibleError
from ansible.module_utils.basic import missing_required_lib
from ansible.module_utils.common.text.converters import to_native
from ansible.module_utils.six import raise_from

from ansible_collections.community.dns.plugins.module_utils.resolver import (
    ResolverError,
)

try:
    import dns  # pylint: disable=unused-import
    import dns.exception  # pylint: disable=unused-import
    import dns.name  # pylint: disable=unused-import
    import dns.message  # pylint: disable=unused-import
    import dns.query  # pylint: disable=unused-import
    import dns.rcode  # pylint: disable=unused-import
    import dns.rdatatype  # pylint: disable=unused-import
    import dns.resolver  # pylint: disable=unused-import
except ImportError as exc:
    DNSPYTHON_IMPORTERROR = exc
else:
    DNSPYTHON_IMPORTERROR = None


def guarded_run(runner, error_class=AnsibleError, server=None):
    suffix = ' for {0}'.format(server) if server is not None else ''
    try:
        return runner()
    except ResolverError as e:
        raise_from(error_class('Unexpected resolving error{0}: {1}'.format(suffix, to_native(e))), e)
    except dns.exception.DNSException as e:
        raise_from(error_class('Unexpected DNS error{0}: {1}'.format(suffix, to_native(e))), e)


def assert_requirements_present(plugin_name, plugin_type):
    if DNSPYTHON_IMPORTERROR is not None:
        msg = 'The {fqcn} {type} plugin is missing requirements: {msg}'.format(
            msg=missing_required_lib('dnspython'), fqcn=plugin_name, type=plugin_type
        )
        raise_from(AnsibleError(msg), DNSPYTHON_IMPORTERROR)
