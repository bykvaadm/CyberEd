# -*- coding: utf-8 -*-

# Copyright (c) 2023, Felix Fontein <felix@fontein.de>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
name: lookup
author: Felix Fontein (@felixfontein)
short_description: Look up DNS records
version_added: 2.6.0
requirements:
    - dnspython >= 1.15.0 (maybe older versions also work)
    - ipaddress (on Python 2.7 when using O(server))
description:
    - Look up DNS records.
options:
    _terms:
        description:
            - Domain name(s) to query.
        type: list
        elements: str
        required: true
    type:
        description:
            - The record type to retrieve.
        type: str
        default: A
        choices:
            - A
            - ALL
            - AAAA
            - CAA
            - CNAME
            - DNAME
            - DNSKEY
            - DS
            - HINFO
            - LOC
            - MX
            - NAPTR
            - NS
            - NSEC
            - NSEC3
            - NSEC3PARAM
            - PTR
            - RP
            - RRSIG
            - SOA
            - SPF
            - SRV
            - SSHFP
            - TLSA
            - TXT
    query_retry:
        description:
            - Number of retries for DNS query timeouts.
        type: int
        default: 3
    query_timeout:
        description:
            - Timeout per DNS query in seconds.
        type: float
        default: 10
    server:
        description:
            - The DNS server(s) to use to look up the result. Must be a list of one or more IP addresses.
            - By default, the system's standard resolver is used.
        type: list
        elements: str
    servfail_retries:
        description:
            - How often to retry on SERVFAIL errors.
        type: int
        default: 0
    nxdomain_handling:
        description:
            - How to handle NXDOMAIN errors. These appear if an unknown domain name is queried.
            - V(empty) (default) returns an empty result for that domain name.
              This means that for the corresponding domain name, nothing is added to RV(_result).
            - V(fail) makes the lookup fail.
            - V(message) adds the string V(NXDOMAIN) to RV(_result).
        type: str
        choices:
            - empty
            - fail
            - message
        default: empty
notes:
    - Note that when using this lookup plugin with V(lookup(\)), and the result is a one-element list,
      Ansible simply returns the one element not as a list. Since this behavior is surprising and
      can cause problems, it is better to use V(query(\)) instead of V(lookup(\)). See the examples
      and also R(Forcing lookups to return lists, query) in the Ansible documentation.
    - All domain names are assumed to be absolute. The resolver's configured search list is not used.
'''

EXAMPLES = """
- name: Look up A (IPv4) records for example.org
  ansible.builtin.debug:
    msg: "{{ query('community.dns.lookup', 'example.org.') }}"

- name: Look up AAAA (IPv6) records for example.org
  ansible.builtin.debug:
    msg: "{{ query('community.dns.lookup', 'example.org.', type='AAAA' ) }}"
"""

RETURN = """
_result:
    description:
        - The records of type O(type) for all queried DNS names.
        - If multiple DNS names are queried in O(_terms), the resulting lists have been concatenated.
    type: list
    elements: str
    sample:
        - 127.0.0.1
"""

from ansible.errors import AnsibleLookupError
from ansible.plugins.lookup import LookupBase
from ansible.module_utils.common.text.converters import to_text

from ansible_collections.community.dns.plugins.module_utils.ips import (
    is_ip_address,
)

from ansible_collections.community.dns.plugins.module_utils.dnspython_records import (
    NAME_TO_RDTYPE,
)

from ansible_collections.community.dns.plugins.module_utils.resolver import (
    SimpleResolver,
)

from ansible_collections.community.dns.plugins.plugin_utils.ips import (
    assert_requirements_present as assert_requirements_present_ipaddress,
)

from ansible_collections.community.dns.plugins.plugin_utils.resolver import (
    assert_requirements_present as assert_requirements_present_dnspython,
    guarded_run,
)

try:
    import dns.resolver
except ImportError:
    # handled by assert_requirements_present_dnspython
    pass


class LookupModule(LookupBase):
    @staticmethod
    def _resolve(resolver, name, rdtype, server_addresses, nxdomain_handling):
        def callback():
            try:
                rrset = resolver.resolve(
                    name,
                    rdtype=rdtype,
                    server_addresses=server_addresses,
                    nxdomain_is_empty=nxdomain_handling == 'empty',
                )
                if not rrset:
                    return []
                return [to_text(data) for data in rrset]
            except dns.resolver.NXDOMAIN:
                if nxdomain_handling == 'message':
                    return ['NXDOMAIN']
                raise AnsibleLookupError('Got NXDOMAIN when querying {name}'.format(name=name))

        return guarded_run(
            callback,
            error_class=AnsibleLookupError,
            server=name,
        )

    def run(self, terms, variables=None, **kwargs):
        assert_requirements_present_dnspython('community.dns.lookup', 'lookup')

        self.set_options(var_options=variables, direct=kwargs)

        resolver = SimpleResolver(
            timeout=self.get_option('query_timeout'),
            timeout_retries=self.get_option('query_retry'),
            servfail_retries=self.get_option('servfail_retries'),
        )

        rdtype = NAME_TO_RDTYPE[self.get_option('type')]

        nxdomain_handling = self.get_option('nxdomain_handling')

        server_addresses = None
        if self.get_option('server'):
            server_addresses = []
            assert_requirements_present_ipaddress('community.dns.lookup', 'lookup')
            for server in self.get_option('server'):
                if is_ip_address(server):
                    server_addresses.append(server)
                    continue
                else:
                    server_addresses.extend(guarded_run(
                        lambda: resolver.resolve_addresses(server),
                        error_class=AnsibleLookupError,
                        server=server,
                    ))

        result = []
        for name in terms:
            result.extend(self._resolve(resolver, name, rdtype, server_addresses, nxdomain_handling))
        return result
