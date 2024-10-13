# cisco.intersight Ansible Collection Changelog

## Version 2.0.17
- Fixes #135 to support JSON Patch of existing resources with example port_policy_json_patch.yml playbook

## Version 2.0.16
- Fixes #133 to add support for Power Policies in Server Profiles

## Version 2.0.15
- Add CI workflow and workaround for ansible-test sanity failures

## Version 2.0.14
- Fixes #127 to avoid changes to existing users in local user policies

## Version 2.0.12
- Update README to follow the Ansible Certified Collections template

## Version 2.0.11
- Fix issue #125 to avoid exceptions when local user policy does not exist

## Version 2.0.10
- Fix issue #119 to avoid incorrect resources used on deletes or updates

## Version 2.0.9
- Fix issue #114 to support $count query param

## Version 2.0.8
- Fix issue #111 to allow User Policy updates

## Version 2.0.7
- Fix issue #101 to support IMM Server Policies.
- Update deploy_server_profiles playbook to support Unassign

## Version 2.0.6
- Updated Ansible Core requirement to >=2.14.0
- ansible-lint fixes for production profile

## Version 2.0.4
- Fix issue #99 to support NVMe boot devices in intersight_boot_order_policy

## Version 2.0.1

- Updated README with requirement for Python 3.6 or newer
- Added CHANGELOG.md
- Added tests/config.yml

## Version 2.0.0

- Initial version for Ansible Automation Platform
