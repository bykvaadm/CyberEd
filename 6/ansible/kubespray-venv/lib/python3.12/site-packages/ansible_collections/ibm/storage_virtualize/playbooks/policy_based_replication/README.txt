Objective:
  - Set up mTLS and configure Policy Based Replication.

Prerequisite:
  - IBM storage Virtualize ansible collection plugins must be installed.
  - Partnership(FC/IP) must be present between the clusters.
  - Host must be present on primary cluster.

These playbooks set up mTLS and configure Policy Based Replication between a primary cluster and the secondary cluster.
  - It uses storage virtualize ansible modules.
  - This playbook is designed to set up mTLS on both the site and configure Policy Based Replication between source cluster to destination cluster. This is designed in a way that it creates Data Reduction Pool, links them, creates provision policy and replication policy. 
  - These playbooks also creates multiple Volumes with specified prefix along with volume group and maps all of them to the specified host.

There are total 4 files used for this use-case.
  1. main.yml:
     This is the main file to be executed as below:
     ansible-playbook main.yml -i PBR_variable.yml
     main.yml leverages other files for PBR configuration. It executes 2 playbooks like "Create_mTLS.yml" and "Create_mdiskgrp_drp_proviPolicy.yml" and later on this the playbook creates volume group and associated volumes with volume_prefix name specified in inventroy file "PBR_variable.yml". It also maps all the volumes to specified host.
     After first execution of this playbook for next execution we can add volumes on existing/new volume group with existing replication policy and provision policy. It mapped this newly added volumes to the existing host object.

  2. PBR_variable.yml:
     This file has all the variables required for playbooks.
      - users_data: Parameters contain primary cluster details from where user wants to replicate data as well as secondary cluster details to where volume will be replicated to.
      - host_name: It is the host name to which all the volumes should be mapped after creation. It assumes host is already created on primary clusters.
      - volume*: Parameters starting volume contain details for volume such as name prefix for volume and size for the volumes to be created.It also has a volumegroup name.
      - number_of_volumes: It is the number of volumes to be created between clusters.
      - log_path: It specifies the log path of playbook. If not specified then logs will generate at default path "/tmp/ansiblePB.debug".

  3. Create_mTLS.yml:
     This playbook sets mTLS (Mutual Transport Layer Security) which includes ceritficate generation on individual cluster, export it to remote location, creates certificate truststore which contains the certificate bundle. This operation is to be performed on both (primary and secondary) sites.

  4. Create_mdiskgrp_drp_proviPolicy.yml:
      This playbook checks the drive status and drive count. Based on this drive info, it creates mdiskgrp, and data reduction pool with specified level. It links pools of both the sites. Then, it creates provisioning policy and replication policy.

Authors: Akshada Thorat  (akshada.thorat@ibm.com)
         Sandip Rajbanshi (sandip.rajbanshi@ibm.com)
         Lavanya C R (lavanya.c.r1@ibm.com)
