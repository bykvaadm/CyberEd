#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: planned_access_points
short_description: Resource module for Planned Access Points
description:
- Manage operations create, update and delete of the resource Planned Access Points.
- >
   Allows creation of a new planned access point on an existing floor map including its planned radio and antenna
   details. Use the Get variant of this API to fetch any existing planned access points for the floor. The payload to
   create a planned access point is in the same format, albeit a single object instead of a list, of that API.
- >
   Allow to delete a planned access point from an existing floor map including its planned radio and antenna details.
   Use the Get variant of this API to fetch the existing planned access points for the floor. The instanceUUID listed
   in each of the planned access point attributes acts as the path param input to this API to delete that specific
   instance.
- >
   Allows updating a planned access point on an existing floor map including its planned radio and antenna details.
   Use the Get variant of this API to fetch the existing planned access points for the floor. The payload to update a
   planned access point is in the same format, albeit a single object instead of a list, of that API.
version_added: '6.0.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  attributes:
    description: Planned Access Points's attributes.
    suboptions:
      createDate:
        description: Planned Access Points's createDate.
        type: int
      domain:
        description: Planned Access Points's domain.
        type: str
      heirarchyName:
        description: Planned Access Points's heirarchyName.
        type: str
      id:
        description: Planned Access Points's id.
        type: float
      instanceUuid:
        description: Planned Access Points's instanceUuid.
        type: str
      macaddress:
        description: Planned Access Points's macaddress.
        type: str
      name:
        description: Planned Access Points's name.
        type: str
      source:
        description: Planned Access Points's source.
        type: str
      typeString:
        description: Planned Access Points's typeString.
        type: str
    type: dict
  floorId:
    description: FloorId path parameter. The instance UUID of the floor hierarchy element.
    type: str
  isSensor:
    description: IsSensor flag.
    type: bool
  location:
    description: Planned Access Points's location.
    suboptions:
      altitude:
        description: Planned Access Points's altitude.
        type: float
      lattitude:
        description: Planned Access Points's lattitude.
        type: float
      longtitude:
        description: Planned Access Points's longtitude.
        type: float
    type: dict
  plannedAccessPointUuid:
    description: PlannedAccessPointUuid path parameter. The instance UUID of the planned
      access point to delete.
    type: str
  position:
    description: Planned Access Points's position.
    suboptions:
      x:
        description: Planned Access Points's x.
        type: float
      y:
        description: Planned Access Points's y.
        type: float
      z:
        description: Planned Access Points's z.
        type: float
    type: dict
  radioCount:
    description: Planned Access Points's radioCount.
    type: int
  radios:
    description: Planned Access Points's radios.
    elements: dict
    suboptions:
      antenna:
        description: Planned Access Points's antenna.
        suboptions:
          azimuthAngle:
            description: Planned Access Points's azimuthAngle.
            type: float
          elevationAngle:
            description: Planned Access Points's elevationAngle.
            type: float
          gain:
            description: Planned Access Points's gain.
            type: float
          mode:
            description: Planned Access Points's mode.
            type: str
          name:
            description: Planned Access Points's name.
            type: str
          type:
            description: Planned Access Points's type.
            type: str
        type: dict
      attributes:
        description: Planned Access Points's attributes.
        suboptions:
          channel:
            description: Planned Access Points's channel.
            type: float
          channelString:
            description: Planned Access Points's channelString.
            type: str
          id:
            description: Planned Access Points's id.
            type: float
          ifMode:
            description: Planned Access Points's ifMode.
            type: str
          ifTypeString:
            description: Planned Access Points's ifTypeString.
            type: str
          ifTypeSubband:
            description: Planned Access Points's ifTypeSubband.
            type: str
          instanceUuid:
            description: Planned Access Points's instanceUuid.
            type: str
          slotId:
            description: Planned Access Points's slotId.
            type: float
        type: dict
      isSensor:
        description: IsSensor flag.
        type: bool
    type: list
requirements:
- dnacentersdk >= 2.7.2
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Devices CreatePlannedAccessPointForFloor
  description: Complete reference of the CreatePlannedAccessPointForFloor API.
  link: https://developer.cisco.com/docs/dna-center/#!create-planned-access-point-for-floor
- name: Cisco DNA Center documentation for Devices DeletePlannedAccessPointForFloor
  description: Complete reference of the DeletePlannedAccessPointForFloor API.
  link: https://developer.cisco.com/docs/dna-center/#!delete-planned-access-point-for-floor
- name: Cisco DNA Center documentation for Devices UpdatePlannedAccessPointForFloor
  description: Complete reference of the UpdatePlannedAccessPointForFloor API.
  link: https://developer.cisco.com/docs/dna-center/#!update-planned-access-point-for-floor
notes:
  - SDK Method used are
    devices.Devices.create_planned_access_point_for_floor,
    devices.Devices.delete_planned_access_point_for_floor,
    devices.Devices.update_planned_access_point_for_floor,

  - Paths used are
    post /dna/intent/api/v1/floors/{floorId}/planned-access-points,
    delete /dna/intent/api/v1/floors/{floorId}/planned-access-points/{plannedAccessPointUuid},
    put /dna/intent/api/v1/floors/{floorId}/planned-access-points,

"""

EXAMPLES = r"""
- name: Update all
  cisco.dnac.planned_access_points:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    attributes:
      createDate: 0
      domain: string
      heirarchyName: string
      id: 0
      instanceUuid: string
      macaddress: string
      name: string
      source: string
      typeString: string
    floorId: string
    isSensor: true
    location:
      altitude: 0
      lattitude: 0
      longtitude: 0
    position:
      x: 0
      y: 0
      z: 0
    radioCount: 0
    radios:
    - antenna:
        azimuthAngle: 0
        elevationAngle: 0
        gain: 0
        mode: string
        name: string
        type: string
      attributes:
        channel: 0
        channelString: string
        id: 0
        ifMode: string
        ifTypeString: string
        ifTypeSubband: string
        instanceUuid: string
        slotId: 0
      isSensor: true

- name: Create
  cisco.dnac.planned_access_points:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    attributes:
      createDate: 0
      domain: string
      heirarchyName: string
      id: 0
      instanceUuid: string
      macaddress: string
      name: string
      source: string
      typeString: string
    floorId: string
    isSensor: true
    location:
      altitude: 0
      lattitude: 0
      longtitude: 0
    position:
      x: 0
      y: 0
      z: 0
    radioCount: 0
    radios:
    - antenna:
        azimuthAngle: 0
        elevationAngle: 0
        gain: 0
        mode: string
        name: string
        type: string
      attributes:
        channel: 0
        channelString: string
        id: 0
        ifMode: string
        ifTypeString: string
        ifTypeSubband: string
        instanceUuid: string
        slotId: 0
      isSensor: true

- name: Delete by id
  cisco.dnac.planned_access_points:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    floorId: string
    plannedAccessPointUuid: string

"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""
