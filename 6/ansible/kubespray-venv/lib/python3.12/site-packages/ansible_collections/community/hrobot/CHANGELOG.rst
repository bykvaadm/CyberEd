================================================
Community Hetzner Robot Collection Release Notes
================================================

.. contents:: Topics

v1.9.3
======

Release Summary
---------------

Bugfix release.

Bugfixes
--------

- boot - use PHP array form encoding when sending multiple ``authorized_key`` (https://github.com/ansible-collections/community.hrobot/issues/112, https://github.com/ansible-collections/community.hrobot/pull/113).

v1.9.2
======

Release Summary
---------------

Bugfix release.

Bugfixes
--------

- inventory plugins - add unsafe wrapper to avoid marking strings that do not contain ``{`` or ``}`` as unsafe, to work around a bug in AWX (https://github.com/ansible-collections/community.hrobot/pull/102).

v1.9.1
======

Release Summary
---------------

Bugfix release.

Security Fixes
--------------

- robot inventory plugin - make sure all data received from the Hetzner robot service server is marked as unsafe, so remote code execution by obtaining texts that can be evaluated as templates is not possible (https://www.die-welt.net/2024/03/remote-code-execution-in-ansible-dynamic-inventory-plugins/, https://github.com/ansible-collections/community.hrobot/pull/99).

v1.9.0
======

Release Summary
---------------

Feature and maintenance release.

Minor Changes
-------------

- robot inventory plugin - the ``filters`` option has been renamed to ``simple_filters``. The old name still works until community.hrobot 2.0.0. Then it will change to allow more complex filtering with the ``community.library_inventory_filtering_v1`` collection's functionality (https://github.com/ansible-collections/community.hrobot/pull/94).

Deprecated Features
-------------------

- robot inventory plugin - the ``filters`` option has been renamed to ``simple_filters``. The old name will stop working in community.hrobot 2.0.0 (https://github.com/ansible-collections/community.hrobot/pull/94).

v1.8.2
======

Release Summary
---------------

Maintenance release with updated documentation.

Bugfixes
--------

- Show more information (if available) from error messages (https://github.com/ansible-collections/community.hrobot/pull/89).

v1.8.1
======

Release Summary
---------------

Maintenance release with updated documentation.

From this version on, community.hrobot is using the new `Ansible semantic markup
<https://docs.ansible.com/ansible/devel/dev_guide/developing_modules_documenting.html#semantic-markup-within-module-documentation>`__
in its documentation. If you look at documentation with the ansible-doc CLI tool
from ansible-core before 2.15, please note that it does not render the markup
correctly. You should be still able to read it in most cases, but you need
ansible-core 2.15 or later to see it as it is intended. Alternatively you can
look at `the devel docsite <https://docs.ansible.com/ansible/devel/collections/community/hrobot/>`__
for the rendered HTML version of the documentation of the latest release.

Known Issues
------------

- Ansible markup will show up in raw form on ansible-doc text output for ansible-core before 2.15. If you have trouble deciphering the documentation markup, please upgrade to ansible-core 2.15 (or newer), or read the HTML documentation on https://docs.ansible.com/ansible/devel/collections/community/hrobot/.

v1.8.0
======

Release Summary
---------------

Feature release for the Hetzner firewall changes.

Major Changes
-------------

- firewall - Hetzner added output rules support to the firewall. This change unfortunately means that using old versions of the firewall module will always set the output rule list to empty, thus disallowing the server to send out packets (https://github.com/ansible-collections/community.hrobot/issues/75, https://github.com/ansible-collections/community.hrobot/pull/76).

Minor Changes
-------------

- firewall, firewall_info - add ``filter_ipv6`` and ``rules.output`` output to support the new IPv6 filtering and output rules features (https://github.com/ansible-collections/community.hrobot/issues/75, https://github.com/ansible-collections/community.hrobot/pull/76).
- firewall, firewall_info - add ``server_number`` option that can be used instead of ``server_ip`` to identify the server. Hetzner deprecated configuring the firewall by ``server_ip``, so using ``server_ip`` will stop at some point in the future (https://github.com/ansible-collections/community.hrobot/pull/77).

v1.7.0
======

Release Summary
---------------

Feature release.

New Modules
-----------

- community.hrobot.v_switch - Manage Hetzner's vSwitch

v1.6.0
======

Release Summary
---------------

Feature release with improved documentation.

Minor Changes
-------------

- Added a ``community.hrobot.robot`` module defaults group / action group. Use with ``group/community.hrobot.robot`` to provide options for all Hetzner Robot modules (https://github.com/ansible-collections/community.hrobot/pull/65).

v1.5.2
======

Release Summary
---------------

Maintenance release with a documentation improvement.

Minor Changes
-------------

- The collection repository conforms to the `REUSE specification <https://reuse.software/spec/>`__ except for the changelog fragments (https://github.com/ansible-collections/community.hrobot/pull/60).

v1.5.1
======

Release Summary
---------------

Maintenance release with small documentation fixes.

v1.5.0
======

Release Summary
---------------

Maintenance release changing the way licenses are declared. No functional changes.

Minor Changes
-------------

- All software licenses are now in the ``LICENSES/`` directory of the collection root. Moreover, ``SPDX-License-Identifier:`` is used to declare the applicable license for every file that is not automatically generated (https://github.com/ansible-collections/community.hrobot/pull/52).

v1.4.0
======

Release Summary
---------------

Feature release.

Minor Changes
-------------

- robot inventory plugin - allow to template ``hetzner_user`` and ``hetzner_password`` (https://github.com/ansible-collections/community.hrobot/pull/49).

v1.3.1
======

Release Summary
---------------

Maintenance release.

Bugfixes
--------

- Include ``simplified_bsd.txt`` license file for the ``robot`` and ``failover`` module utils.

v1.3.0
======

Release Summary
---------------

Feature and bugfix release.

Minor Changes
-------------

- Prepare collection for inclusion in an Execution Environment by declaring its dependencies (https://github.com/ansible-collections/community.hrobot/pull/45).

Bugfixes
--------

- robot inventory plugin - do not crash if a server neither has name or primary IP set. Instead, fall back to using the server's number as the name. This can happen if unnamed rack reservations show up in your server list (https://github.com/ansible-collections/community.hrobot/issues/40, https://github.com/ansible-collections/community.hrobot/pull/47).

v1.2.3
======

Release Summary
---------------

Docs update release.

v1.2.2
======

Release Summary
---------------

Bugfix release.

Bugfixes
--------

- boot - fix incorrect handling of SSH authorized keys (https://github.com/ansible-collections/community.hrobot/issues/32, https://github.com/ansible-collections/community.hrobot/pull/33).

v1.2.1
======

Release Summary
---------------

Maintenance release.

Minor Changes
-------------

- Generic module HTTP support code - fix usage of ``fetch_url`` with changes in latest ansible-core ``devel`` branch (https://github.com/ansible-collections/community.hrobot/pull/30).

v1.2.0
======

Release Summary
---------------

Feature release with multiple new modules.

Minor Changes
-------------

- Avoid internal ansible-core module_utils in favor of equivalent public API available since at least Ansible 2.9 (https://github.com/ansible-collections/community.hrobot/pull/18).
- firewall - rename option ``whitelist_hos`` to ``allowlist_hos``, keep old name as alias (https://github.com/ansible-collections/community.hrobot/pull/15).
- firewall, firewall_info - add return value ``allowlist_hos``, which contains the same value as ``whitelist_hos``. The old name ``whitelist_hos`` will be removed eventually (https://github.com/ansible-collections/community.hrobot/pull/15).
- robot module utils - add ``allow_empty_result`` parameter to ``plugin_open_url_json`` and ``fetch_url_json`` (https://github.com/ansible-collections/community.hrobot/pull/16).

New Modules
-----------

- community.hrobot.boot - Set boot configuration
- community.hrobot.reset - Reset a dedicated server
- community.hrobot.reverse_dns - Set or remove reverse DNS entry for IP
- community.hrobot.server - Update server information
- community.hrobot.server_info - Query information on one or more servers
- community.hrobot.ssh_key - Add, remove or update SSH key
- community.hrobot.ssh_key_info - Query information on SSH keys

v1.1.1
======

Release Summary
---------------

Bugfix release which reduces the number of HTTPS queries for the modules and plugins.

Bugfixes
--------

- robot - force HTTP basic authentication to reduce number of HTTPS requests (https://github.com/ansible-collections/community.hrobot/pull/9).

v1.1.0
======

Release Summary
---------------

Release with a new inventory plugin.

New Plugins
-----------

Inventory
~~~~~~~~~

- community.hrobot.robot - Hetzner Robot inventory source

v1.0.0
======

Release Summary
---------------

The ``community.hrobot`` continues the work on the Hetzner Robot modules from their state in ``community.general`` 1.2.0. The changes listed here are thus relative to the modules ``community.general.hetzner_*``.

Breaking Changes / Porting Guide
--------------------------------

- firewall - now requires the `ipaddress <https://pypi.org/project/ipaddress/>`_ library (https://github.com/ansible-collections/community.hrobot/pull/2).
