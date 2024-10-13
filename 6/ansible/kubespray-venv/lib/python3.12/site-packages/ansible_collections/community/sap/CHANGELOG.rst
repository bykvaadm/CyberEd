===========================
Community SAP Release Notes
===========================

.. contents:: Topics


v2.0.0
======

Release Summary
---------------

This release deprecates all modules and redirect them to community.sap_libs. The modules are removed in this release.
The modules are available in the community.sap_libs repository.

Major Changes
-------------

- all modules - everything is now a redirect to the new collection community.sap_libs

Deprecated Features
-------------------

- community.sap.hana_query - is deprecated in favor of community.sap_libs.sap_hdbsql
- community.sap.sap_company - is deprecated in favor of community.sap_libs.sap_company
- community.sap.sap_snote - is deprecated in favor of community.sap_libs.sap_snote
- community.sap.sap_task_list_execute - is deprecated in favor of community.sap_libs.sap_task_list_execute
- community.sap.sap_user - is deprecated in favor of community.sap_libs.sap_user
- community.sap.sapcar_extract - is deprecated in favor of community.sap_libs.sapcar_extract

v1.0.0
======

Release Summary
---------------

This is the first major release of the ``community.sap`` collection. This changelog contains all changes to the modules and plugins in this collection that have been made after the previous release.

Minor Changes
-------------

- sapcar_extract.py - more strict logic for filenames

New Modules
-----------

Identity
~~~~~~~~

- sap_company - This module will manage a company entities in a SAP S4HANA environment
- sap_user - This module will manage a user entities in a SAP S4/HANA environment

System
~~~~~~

- sap_snote - This module will upload and (de)implements C(SNOTES) in a SAP S4HANA environment.
- sap_system_facts - Gathers SAP facts in a host

v0.1.0
======

Release Summary
---------------

This is the minor release of the ``community.sap`` collection. It is the initial relase for the ``community.sap`` collection

New Modules
-----------

Database
~~~~~~~~

saphana
^^^^^^^

- hana_query - Execute SQL on HANA

Files
~~~~~

- sapcar_extract - Manages SAP SAPCAR archives

System
~~~~~~

- sap_task_list_execute - Perform SAP Task list execution
