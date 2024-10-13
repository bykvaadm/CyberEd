Objective:
This playbook creates FC host, multiple volumes, zones on Flashsystem Cluster and performs mapping of all volumes to host.

Prerequisite:
- IBM Spectrum Virtualize and Brocade ansible collection plugins must be installed
- For more information on Brocade switch ansible collection, please refer to https://github.com/brocade/ansible/blob/master/README.rst

These playbooks maps multiple volumes of cluster to fc host
- It uses spectrum virtualize ansible modules as well as brocade ansible modules to create zone

There are total 2 files used for this use-case

1. multiple_vol_creation_zone_map_vars
	This file has all the variables required for playbooks
	- cluster_*   	  : Parameters starting with cluster contain cluster details where user wants to create volume, hosst etc
	- brocade_switch_*  : Parameters starting with brocade_switch contain brocade switch details
	- application_host_*: Parameters starting with application_host contain application host details which is performing read/write of data
      - volume_details    : Parameters starting with volume contain volume details which will be mapped to host
	- portset_*	   : Parameters starting with portset contain portset details required for creating fc host

2. multi_volume_create_host_mapping_zone_multipath
	- This playbook fetches the list of SCSI_HOST WWPN's associated with given fcioportid from specV cluster
	- Creates zone with the name given and add specV ports fetched and host WWPN's given
	- Creates multiple volumes based on volume details provided
	- Maps the multiple volumes to Host to form multiple paths

Authors: Ajinkya Nanavati (ananava1@in.ibm.com)
         Mohit Chitlange  (mochitla@in.ibm.com)
