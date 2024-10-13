# Community Hetzner Robot Collection Release Notes

**Topics**

- <a href="#v1-9-3">v1\.9\.3</a>
    - <a href="#release-summary">Release Summary</a>
    - <a href="#bugfixes">Bugfixes</a>
- <a href="#v1-9-2">v1\.9\.2</a>
    - <a href="#release-summary-1">Release Summary</a>
    - <a href="#bugfixes-1">Bugfixes</a>
- <a href="#v1-9-1">v1\.9\.1</a>
    - <a href="#release-summary-2">Release Summary</a>
    - <a href="#security-fixes">Security Fixes</a>
- <a href="#v1-9-0">v1\.9\.0</a>
    - <a href="#release-summary-3">Release Summary</a>
    - <a href="#minor-changes">Minor Changes</a>
    - <a href="#deprecated-features">Deprecated Features</a>
- <a href="#v1-8-2">v1\.8\.2</a>
    - <a href="#release-summary-4">Release Summary</a>
    - <a href="#bugfixes-2">Bugfixes</a>
- <a href="#v1-8-1">v1\.8\.1</a>
    - <a href="#release-summary-5">Release Summary</a>
    - <a href="#known-issues">Known Issues</a>
- <a href="#v1-8-0">v1\.8\.0</a>
    - <a href="#release-summary-6">Release Summary</a>
    - <a href="#major-changes">Major Changes</a>
    - <a href="#minor-changes-1">Minor Changes</a>
- <a href="#v1-7-0">v1\.7\.0</a>
    - <a href="#release-summary-7">Release Summary</a>
    - <a href="#new-modules">New Modules</a>
- <a href="#v1-6-0">v1\.6\.0</a>
    - <a href="#release-summary-8">Release Summary</a>
    - <a href="#minor-changes-2">Minor Changes</a>
- <a href="#v1-5-2">v1\.5\.2</a>
    - <a href="#release-summary-9">Release Summary</a>
    - <a href="#minor-changes-3">Minor Changes</a>
- <a href="#v1-5-1">v1\.5\.1</a>
    - <a href="#release-summary-10">Release Summary</a>
- <a href="#v1-5-0">v1\.5\.0</a>
    - <a href="#release-summary-11">Release Summary</a>
    - <a href="#minor-changes-4">Minor Changes</a>
- <a href="#v1-4-0">v1\.4\.0</a>
    - <a href="#release-summary-12">Release Summary</a>
    - <a href="#minor-changes-5">Minor Changes</a>
- <a href="#v1-3-1">v1\.3\.1</a>
    - <a href="#release-summary-13">Release Summary</a>
    - <a href="#bugfixes-3">Bugfixes</a>
- <a href="#v1-3-0">v1\.3\.0</a>
    - <a href="#release-summary-14">Release Summary</a>
    - <a href="#minor-changes-6">Minor Changes</a>
    - <a href="#bugfixes-4">Bugfixes</a>
- <a href="#v1-2-3">v1\.2\.3</a>
    - <a href="#release-summary-15">Release Summary</a>
- <a href="#v1-2-2">v1\.2\.2</a>
    - <a href="#release-summary-16">Release Summary</a>
    - <a href="#bugfixes-5">Bugfixes</a>
- <a href="#v1-2-1">v1\.2\.1</a>
    - <a href="#release-summary-17">Release Summary</a>
    - <a href="#minor-changes-7">Minor Changes</a>
- <a href="#v1-2-0">v1\.2\.0</a>
    - <a href="#release-summary-18">Release Summary</a>
    - <a href="#minor-changes-8">Minor Changes</a>
    - <a href="#new-modules-1">New Modules</a>
- <a href="#v1-1-1">v1\.1\.1</a>
    - <a href="#release-summary-19">Release Summary</a>
    - <a href="#bugfixes-6">Bugfixes</a>
- <a href="#v1-1-0">v1\.1\.0</a>
    - <a href="#release-summary-20">Release Summary</a>
    - <a href="#new-plugins">New Plugins</a>
        - <a href="#inventory">Inventory</a>
- <a href="#v1-0-0">v1\.0\.0</a>
    - <a href="#release-summary-21">Release Summary</a>
    - <a href="#breaking-changes--porting-guide">Breaking Changes / Porting Guide</a>

<a id="v1-9-3"></a>
## v1\.9\.3

<a id="release-summary"></a>
### Release Summary

Bugfix release\.

<a id="bugfixes"></a>
### Bugfixes

* boot \- use PHP array form encoding when sending multiple <code>authorized\_key</code> \([https\://github\.com/ansible\-collections/community\.hrobot/issues/112](https\://github\.com/ansible\-collections/community\.hrobot/issues/112)\, [https\://github\.com/ansible\-collections/community\.hrobot/pull/113](https\://github\.com/ansible\-collections/community\.hrobot/pull/113)\)\.

<a id="v1-9-2"></a>
## v1\.9\.2

<a id="release-summary-1"></a>
### Release Summary

Bugfix release\.

<a id="bugfixes-1"></a>
### Bugfixes

* inventory plugins \- add unsafe wrapper to avoid marking strings that do not contain <code>\{</code> or <code>\}</code> as unsafe\, to work around a bug in AWX \([https\://github\.com/ansible\-collections/community\.hrobot/pull/102](https\://github\.com/ansible\-collections/community\.hrobot/pull/102)\)\.

<a id="v1-9-1"></a>
## v1\.9\.1

<a id="release-summary-2"></a>
### Release Summary

Bugfix release\.

<a id="security-fixes"></a>
### Security Fixes

* robot inventory plugin \- make sure all data received from the Hetzner robot service server is marked as unsafe\, so remote code execution by obtaining texts that can be evaluated as templates is not possible \([https\://www\.die\-welt\.net/2024/03/remote\-code\-execution\-in\-ansible\-dynamic\-inventory\-plugins/](https\://www\.die\-welt\.net/2024/03/remote\-code\-execution\-in\-ansible\-dynamic\-inventory\-plugins/)\, [https\://github\.com/ansible\-collections/community\.hrobot/pull/99](https\://github\.com/ansible\-collections/community\.hrobot/pull/99)\)\.

<a id="v1-9-0"></a>
## v1\.9\.0

<a id="release-summary-3"></a>
### Release Summary

Feature and maintenance release\.

<a id="minor-changes"></a>
### Minor Changes

* robot inventory plugin \- the <code>filters</code> option has been renamed to <code>simple\_filters</code>\. The old name still works until community\.hrobot 2\.0\.0\. Then it will change to allow more complex filtering with the <code>community\.library\_inventory\_filtering\_v1</code> collection\'s functionality \([https\://github\.com/ansible\-collections/community\.hrobot/pull/94](https\://github\.com/ansible\-collections/community\.hrobot/pull/94)\)\.

<a id="deprecated-features"></a>
### Deprecated Features

* robot inventory plugin \- the <code>filters</code> option has been renamed to <code>simple\_filters</code>\. The old name will stop working in community\.hrobot 2\.0\.0 \([https\://github\.com/ansible\-collections/community\.hrobot/pull/94](https\://github\.com/ansible\-collections/community\.hrobot/pull/94)\)\.

<a id="v1-8-2"></a>
## v1\.8\.2

<a id="release-summary-4"></a>
### Release Summary

Maintenance release with updated documentation\.

<a id="bugfixes-2"></a>
### Bugfixes

* Show more information \(if available\) from error messages \([https\://github\.com/ansible\-collections/community\.hrobot/pull/89](https\://github\.com/ansible\-collections/community\.hrobot/pull/89)\)\.

<a id="v1-8-1"></a>
## v1\.8\.1

<a id="release-summary-5"></a>
### Release Summary

Maintenance release with updated documentation\.

From this version on\, community\.hrobot is using the new [Ansible semantic markup](https\://docs\.ansible\.com/ansible/devel/dev\_guide/developing\_modules\_documenting\.html\#semantic\-markup\-within\-module\-documentation)
in its documentation\. If you look at documentation with the ansible\-doc CLI tool
from ansible\-core before 2\.15\, please note that it does not render the markup
correctly\. You should be still able to read it in most cases\, but you need
ansible\-core 2\.15 or later to see it as it is intended\. Alternatively you can
look at [the devel docsite](https\://docs\.ansible\.com/ansible/devel/collections/community/hrobot/)
for the rendered HTML version of the documentation of the latest release\.

<a id="known-issues"></a>
### Known Issues

* Ansible markup will show up in raw form on ansible\-doc text output for ansible\-core before 2\.15\. If you have trouble deciphering the documentation markup\, please upgrade to ansible\-core 2\.15 \(or newer\)\, or read the HTML documentation on [https\://docs\.ansible\.com/ansible/devel/collections/community/hrobot/](https\://docs\.ansible\.com/ansible/devel/collections/community/hrobot/)\.

<a id="v1-8-0"></a>
## v1\.8\.0

<a id="release-summary-6"></a>
### Release Summary

Feature release for the Hetzner firewall changes\.

<a id="major-changes"></a>
### Major Changes

* firewall \- Hetzner added output rules support to the firewall\. This change unfortunately means that using old versions of the firewall module will always set the output rule list to empty\, thus disallowing the server to send out packets \([https\://github\.com/ansible\-collections/community\.hrobot/issues/75](https\://github\.com/ansible\-collections/community\.hrobot/issues/75)\, [https\://github\.com/ansible\-collections/community\.hrobot/pull/76](https\://github\.com/ansible\-collections/community\.hrobot/pull/76)\)\.

<a id="minor-changes-1"></a>
### Minor Changes

* firewall\, firewall\_info \- add <code>filter\_ipv6</code> and <code>rules\.output</code> output to support the new IPv6 filtering and output rules features \([https\://github\.com/ansible\-collections/community\.hrobot/issues/75](https\://github\.com/ansible\-collections/community\.hrobot/issues/75)\, [https\://github\.com/ansible\-collections/community\.hrobot/pull/76](https\://github\.com/ansible\-collections/community\.hrobot/pull/76)\)\.
* firewall\, firewall\_info \- add <code>server\_number</code> option that can be used instead of <code>server\_ip</code> to identify the server\. Hetzner deprecated configuring the firewall by <code>server\_ip</code>\, so using <code>server\_ip</code> will stop at some point in the future \([https\://github\.com/ansible\-collections/community\.hrobot/pull/77](https\://github\.com/ansible\-collections/community\.hrobot/pull/77)\)\.

<a id="v1-7-0"></a>
## v1\.7\.0

<a id="release-summary-7"></a>
### Release Summary

Feature release\.

<a id="new-modules"></a>
### New Modules

* community\.hrobot\.v\_switch \- Manage Hetzner\'s vSwitch

<a id="v1-6-0"></a>
## v1\.6\.0

<a id="release-summary-8"></a>
### Release Summary

Feature release with improved documentation\.

<a id="minor-changes-2"></a>
### Minor Changes

* Added a <code>community\.hrobot\.robot</code> module defaults group / action group\. Use with <code>group/community\.hrobot\.robot</code> to provide options for all Hetzner Robot modules \([https\://github\.com/ansible\-collections/community\.hrobot/pull/65](https\://github\.com/ansible\-collections/community\.hrobot/pull/65)\)\.

<a id="v1-5-2"></a>
## v1\.5\.2

<a id="release-summary-9"></a>
### Release Summary

Maintenance release with a documentation improvement\.

<a id="minor-changes-3"></a>
### Minor Changes

* The collection repository conforms to the [REUSE specification](https\://reuse\.software/spec/) except for the changelog fragments \([https\://github\.com/ansible\-collections/community\.hrobot/pull/60](https\://github\.com/ansible\-collections/community\.hrobot/pull/60)\)\.

<a id="v1-5-1"></a>
## v1\.5\.1

<a id="release-summary-10"></a>
### Release Summary

Maintenance release with small documentation fixes\.

<a id="v1-5-0"></a>
## v1\.5\.0

<a id="release-summary-11"></a>
### Release Summary

Maintenance release changing the way licenses are declared\. No functional changes\.

<a id="minor-changes-4"></a>
### Minor Changes

* All software licenses are now in the <code>LICENSES/</code> directory of the collection root\. Moreover\, <code>SPDX\-License\-Identifier\:</code> is used to declare the applicable license for every file that is not automatically generated \([https\://github\.com/ansible\-collections/community\.hrobot/pull/52](https\://github\.com/ansible\-collections/community\.hrobot/pull/52)\)\.

<a id="v1-4-0"></a>
## v1\.4\.0

<a id="release-summary-12"></a>
### Release Summary

Feature release\.

<a id="minor-changes-5"></a>
### Minor Changes

* robot inventory plugin \- allow to template <code>hetzner\_user</code> and <code>hetzner\_password</code> \([https\://github\.com/ansible\-collections/community\.hrobot/pull/49](https\://github\.com/ansible\-collections/community\.hrobot/pull/49)\)\.

<a id="v1-3-1"></a>
## v1\.3\.1

<a id="release-summary-13"></a>
### Release Summary

Maintenance release\.

<a id="bugfixes-3"></a>
### Bugfixes

* Include <code>simplified\_bsd\.txt</code> license file for the <code>robot</code> and <code>failover</code> module utils\.

<a id="v1-3-0"></a>
## v1\.3\.0

<a id="release-summary-14"></a>
### Release Summary

Feature and bugfix release\.

<a id="minor-changes-6"></a>
### Minor Changes

* Prepare collection for inclusion in an Execution Environment by declaring its dependencies \([https\://github\.com/ansible\-collections/community\.hrobot/pull/45](https\://github\.com/ansible\-collections/community\.hrobot/pull/45)\)\.

<a id="bugfixes-4"></a>
### Bugfixes

* robot inventory plugin \- do not crash if a server neither has name or primary IP set\. Instead\, fall back to using the server\'s number as the name\. This can happen if unnamed rack reservations show up in your server list \([https\://github\.com/ansible\-collections/community\.hrobot/issues/40](https\://github\.com/ansible\-collections/community\.hrobot/issues/40)\, [https\://github\.com/ansible\-collections/community\.hrobot/pull/47](https\://github\.com/ansible\-collections/community\.hrobot/pull/47)\)\.

<a id="v1-2-3"></a>
## v1\.2\.3

<a id="release-summary-15"></a>
### Release Summary

Docs update release\.

<a id="v1-2-2"></a>
## v1\.2\.2

<a id="release-summary-16"></a>
### Release Summary

Bugfix release\.

<a id="bugfixes-5"></a>
### Bugfixes

* boot \- fix incorrect handling of SSH authorized keys \([https\://github\.com/ansible\-collections/community\.hrobot/issues/32](https\://github\.com/ansible\-collections/community\.hrobot/issues/32)\, [https\://github\.com/ansible\-collections/community\.hrobot/pull/33](https\://github\.com/ansible\-collections/community\.hrobot/pull/33)\)\.

<a id="v1-2-1"></a>
## v1\.2\.1

<a id="release-summary-17"></a>
### Release Summary

Maintenance release\.

<a id="minor-changes-7"></a>
### Minor Changes

* Generic module HTTP support code \- fix usage of <code>fetch\_url</code> with changes in latest ansible\-core <code>devel</code> branch \([https\://github\.com/ansible\-collections/community\.hrobot/pull/30](https\://github\.com/ansible\-collections/community\.hrobot/pull/30)\)\.

<a id="v1-2-0"></a>
## v1\.2\.0

<a id="release-summary-18"></a>
### Release Summary

Feature release with multiple new modules\.

<a id="minor-changes-8"></a>
### Minor Changes

* Avoid internal ansible\-core module\_utils in favor of equivalent public API available since at least Ansible 2\.9 \([https\://github\.com/ansible\-collections/community\.hrobot/pull/18](https\://github\.com/ansible\-collections/community\.hrobot/pull/18)\)\.
* firewall \- rename option <code>whitelist\_hos</code> to <code>allowlist\_hos</code>\, keep old name as alias \([https\://github\.com/ansible\-collections/community\.hrobot/pull/15](https\://github\.com/ansible\-collections/community\.hrobot/pull/15)\)\.
* firewall\, firewall\_info \- add return value <code>allowlist\_hos</code>\, which contains the same value as <code>whitelist\_hos</code>\. The old name <code>whitelist\_hos</code> will be removed eventually \([https\://github\.com/ansible\-collections/community\.hrobot/pull/15](https\://github\.com/ansible\-collections/community\.hrobot/pull/15)\)\.
* robot module utils \- add <code>allow\_empty\_result</code> parameter to <code>plugin\_open\_url\_json</code> and <code>fetch\_url\_json</code> \([https\://github\.com/ansible\-collections/community\.hrobot/pull/16](https\://github\.com/ansible\-collections/community\.hrobot/pull/16)\)\.

<a id="new-modules-1"></a>
### New Modules

* community\.hrobot\.boot \- Set boot configuration
* community\.hrobot\.reset \- Reset a dedicated server
* community\.hrobot\.reverse\_dns \- Set or remove reverse DNS entry for IP
* community\.hrobot\.server \- Update server information
* community\.hrobot\.server\_info \- Query information on one or more servers
* community\.hrobot\.ssh\_key \- Add\, remove or update SSH key
* community\.hrobot\.ssh\_key\_info \- Query information on SSH keys

<a id="v1-1-1"></a>
## v1\.1\.1

<a id="release-summary-19"></a>
### Release Summary

Bugfix release which reduces the number of HTTPS queries for the modules and plugins\.

<a id="bugfixes-6"></a>
### Bugfixes

* robot \- force HTTP basic authentication to reduce number of HTTPS requests \([https\://github\.com/ansible\-collections/community\.hrobot/pull/9](https\://github\.com/ansible\-collections/community\.hrobot/pull/9)\)\.

<a id="v1-1-0"></a>
## v1\.1\.0

<a id="release-summary-20"></a>
### Release Summary

Release with a new inventory plugin\.

<a id="new-plugins"></a>
### New Plugins

<a id="inventory"></a>
#### Inventory

* community\.hrobot\.robot \- Hetzner Robot inventory source

<a id="v1-0-0"></a>
## v1\.0\.0

<a id="release-summary-21"></a>
### Release Summary

The <code>community\.hrobot</code> continues the work on the Hetzner Robot modules from their state in <code>community\.general</code> 1\.2\.0\. The changes listed here are thus relative to the modules <code>community\.general\.hetzner\_\*</code>\.

<a id="breaking-changes--porting-guide"></a>
### Breaking Changes / Porting Guide

* firewall \- now requires the [ipaddress](https\://pypi\.org/project/ipaddress/) library \([https\://github\.com/ansible\-collections/community\.hrobot/pull/2](https\://github\.com/ansible\-collections/community\.hrobot/pull/2)\)\.
