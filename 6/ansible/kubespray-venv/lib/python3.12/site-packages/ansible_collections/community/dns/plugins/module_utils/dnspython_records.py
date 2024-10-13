# -*- coding: utf-8 -*-

# Copyright (c) 2015, Jan-Piet Mens <jpmens(at)gmail.com>
# Copyright (c) 2017 Ansible Project
# Copyright (c) 2022, Felix Fontein <felix@fontein.de>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


import base64

from ansible.module_utils.common.text.converters import to_bytes, to_native, to_text
from ansible.module_utils.six import binary_type

NAME_TO_RDTYPE = {}
RDTYPE_TO_NAME = {}
RDTYPE_TO_FIELDS = {}

try:
    import dns.name
    import dns.rdata
    import dns.rdatatype

    # The following data has been borrowed from community.general's dig lookup plugin.
    #
    # Note: adding support for RRSIG is hard work. :)
    for name, rdtype, fields in [
        ('A', dns.rdatatype.A, ['address']),
        ('AAAA', dns.rdatatype.AAAA, ['address']),
        ('CAA', dns.rdatatype.CAA, ['flags', 'tag', 'value']),
        ('CNAME', dns.rdatatype.CNAME, ['target']),
        ('DNAME', dns.rdatatype.DNAME, ['target']),
        ('DNSKEY', dns.rdatatype.DNSKEY, ['flags', 'algorithm', 'protocol', 'key']),
        ('DS', dns.rdatatype.DS, ['algorithm', 'digest_type', 'key_tag', 'digest']),
        ('HINFO', dns.rdatatype.HINFO, ['cpu', 'os']),
        ('LOC', dns.rdatatype.LOC, ['latitude', 'longitude', 'altitude', 'size', 'horizontal_precision', 'vertical_precision']),
        ('MX', dns.rdatatype.MX, ['preference', 'exchange']),
        ('NAPTR', dns.rdatatype.NAPTR, ['order', 'preference', 'flags', 'service', 'regexp', 'replacement']),
        ('NS', dns.rdatatype.NS, ['target']),
        ('NSEC', dns.rdatatype.NSEC, ['next', 'windows']),
        ('NSEC3', dns.rdatatype.NSEC3, ['algorithm', 'flags', 'iterations', 'salt', 'next', 'windows']),
        ('NSEC3PARAM', dns.rdatatype.NSEC3PARAM, ['algorithm', 'flags', 'iterations', 'salt']),
        ('PTR', dns.rdatatype.PTR, ['target']),
        ('RP', dns.rdatatype.RP, ['mbox', 'txt']),
        ('RRSIG', dns.rdatatype.RRSIG, ['type_covered', 'algorithm', 'labels', 'original_ttl', 'expiration', 'inception', 'key_tag', 'signer', 'signature']),
        ('SOA', dns.rdatatype.SOA, ['mname', 'rname', 'serial', 'refresh', 'retry', 'expire', 'minimum']),
        ('SPF', dns.rdatatype.SPF, ['strings']),
        ('SRV', dns.rdatatype.SRV, ['priority', 'weight', 'port', 'target']),
        ('SSHFP', dns.rdatatype.SSHFP, ['algorithm', 'fp_type', 'fingerprint']),
        ('TLSA', dns.rdatatype.TLSA, ['usage', 'selector', 'mtype', 'cert']),
        ('TXT', dns.rdatatype.TXT, ['strings']),
    ]:
        NAME_TO_RDTYPE[name] = rdtype
        RDTYPE_TO_NAME[rdtype] = name
        RDTYPE_TO_FIELDS[rdtype] = fields

except ImportError:
    pass  # has to be handled on application level


def convert_rdata_to_dict(rdata, to_unicode=True, add_synthetic=True):
    '''
    Convert a DNSPython record data object to a Python dictionary.

    Code borrowed from community.general's dig looup plugin.

    If ``to_unicode=True``, all strings will be converted to Unicode/UTF-8 strings.

    If ``add_synthetic=True``, for some record types additional fields are added.
    For TXT and SPF records, ``value`` contains the concatenated strings, for example.
    '''
    result = {}

    fields = RDTYPE_TO_FIELDS.get(rdata.rdtype)
    if fields is None:
        raise ValueError('Unsupported record type {rdtype}'.format(rdtype=rdata.rdtype))
    for f in fields:
        val = rdata.__getattribute__(f)

        if isinstance(val, dns.name.Name):
            val = dns.name.Name.to_text(val)

        if rdata.rdtype == dns.rdatatype.DS and f == 'digest':
            val = dns.rdata._hexify(rdata.digest).replace(' ', '')
        if rdata.rdtype == dns.rdatatype.DNSKEY and f == 'algorithm':
            val = int(val)
        if rdata.rdtype == dns.rdatatype.DNSKEY and f == 'key':
            val = dns.rdata._base64ify(rdata.key).replace(' ', '')
        if rdata.rdtype == dns.rdatatype.NSEC3 and f == 'next':
            val = to_native(base64.b32encode(rdata.next).translate(dns.rdtypes.ANY.NSEC3.b32_normal_to_hex).lower())
        if rdata.rdtype in (dns.rdatatype.NSEC, dns.rdatatype.NSEC3) and f == 'windows':
            try:
                val = dns.rdtypes.util.Bitmap(rdata.windows).to_text().lstrip(' ')
            except AttributeError:
                # dnspython < 2.0.0
                val = []
                for window, bitmap in rdata.windows:
                    for i, byte in enumerate(bitmap):
                        for j in range(8):
                            if (byte >> (7 - j)) & 1 != 0:
                                val.append(dns.rdatatype.to_text(window * 256 + i * 8 + j))
                val = ' '.join(val).lstrip(' ')
        if rdata.rdtype in (dns.rdatatype.NSEC3, dns.rdatatype.NSEC3PARAM) and f == 'salt':
            val = dns.rdata._hexify(rdata.salt).replace(' ', '')
        if rdata.rdtype == dns.rdatatype.RRSIG and f == 'type_covered':
            val = RDTYPE_TO_NAME.get(rdata.type_covered) or str(val)
        if rdata.rdtype == dns.rdatatype.RRSIG and f == 'algorithm':
            val = int(val)
        if rdata.rdtype == dns.rdatatype.RRSIG and f == 'signature':
            val = dns.rdata._base64ify(rdata.signature).replace(' ', '')
        if rdata.rdtype == dns.rdatatype.SSHFP and f == 'fingerprint':
            val = dns.rdata._hexify(rdata.fingerprint).replace(' ', '')
        if rdata.rdtype == dns.rdatatype.TLSA and f == 'cert':
            val = dns.rdata._hexify(rdata.cert).replace(' ', '')

        if isinstance(val, (list, tuple)):
            if to_unicode:
                val = [to_text(v) if isinstance(v, binary_type) else v for v in val]
            else:
                val = list(val)
        elif to_unicode and isinstance(val, binary_type):
            val = to_text(val)

        result[f] = val

    if add_synthetic:
        if rdata.rdtype in (dns.rdatatype.TXT, dns.rdatatype.SPF):
            if to_unicode:
                result['value'] = u''.join([to_text(str) for str in rdata.strings])
            else:
                result['value'] = b''.join([to_bytes(str) for str in rdata.strings])
    return result
