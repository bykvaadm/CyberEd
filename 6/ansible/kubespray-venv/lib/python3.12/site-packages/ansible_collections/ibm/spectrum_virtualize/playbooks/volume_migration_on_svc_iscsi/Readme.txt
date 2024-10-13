Objective:
Migrate volume from one Flash System to another Flash System in application transparent manner with target host as ISCSI.

Prerequisite:
- IBM Spectrum Virtualize ansible collection plugins must be installed

These playbooks migrate a volume from a source cluster to the destination cluster.
These playbooks are designed to migrate volume mapped to Fibre Channel (FC) host or ISCSI host from source cluster to ISCSI host on destination cluster.

There are total 3 files used for this use-case.
  1. vol_migration_vars:
     This file has all the variables required for playbooks
	- src_cluster_*        : Parameters starting with src_cluster contain source cluster details from where user wants to migrate volume
	- src_cluster_*        : Parameters starting with src_cluster contain source cluster details from where user wants to migrate volume
	- dest_cluster*        : Parameters starting with dest_cluster contain destination cluster details to where volume will be migrated
	- application_host_*   : Parameters starting with application_host contain application host details which is performing read/write of data
	- application_iscsi_ip : This contains in detail information for ip to be given to node with detail information as follows
	- node_name: Node name of cluster
        - portset: portset name to be used
        - ip_address: <ip address>
        - subnet_prefix: <prefix>
        - gateway: <gateway>
        - port: <port_id>
     	- src_vol_name         : This suggest volume name of source cluster which is to be migrated
	- dest_vol_name        : This create volume name at destination cluster
	- rel_name             : This is name of relationship to be created between source and destination cluster
  2. initiate_migration_for_given_volume:
     - This playbook initiates the migration
     - Most importantly, it also starts data copy from source cluster to destination cluster
  Note:
     User should not run playbook create_zone_map_volume_and_rescan until relationship is in consistent_syncronized state
  3. create_host_map_volume_and_rescan
     - Execute this playbook once the relationship created by above playbook is in consistent_syncronized state
	 - create iscsi host on flashsystem from iqn defined in variable application_host_iqn from variable file
	 - configuring ip on each node for iscsi host connectivity
	 - establish iscsi session from host to flashsystem nodes
     - Maps the volume to the Host and starts scsi rescan on the host
     - Switch replication direction of a migration relationship once host is mapped
     - Again rescan the volume on the host to get the updated path details
     - Delete source volume and migration relationship which was created
     - Again rescan the multipath and expect migrated volume has the only path from destiantion cluster

 Authors: Ajinkya Nanavati (ananava1@in.ibm.com)
          Mohit Chitlange  (mochitla@in.ibm.com)
          Devendra Mahajan (demahaj1@in.ibm.com)
