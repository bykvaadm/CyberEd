terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
    local = {
      source  = "hashicorp/local"
      version = "~> 2.5"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  zone = "ru-central1-a"
}

resource "yandex_compute_disk" "boot-disk-1" {
  name     = "boot-disk-1"
  type     = "network-hdd"
  zone     = "ru-central1-a"
  size     = "20"
  image_id = "fd83j4siasgfq4pi1qif"
}
resource "yandex_compute_disk" "boot-disk-2" {
  name     = "boot-disk-2"
  type     = "network-hdd"
  zone     = "ru-central1-a"
  size     = "20"
  image_id = "fd83j4siasgfq4pi1qif"
}
resource "yandex_compute_disk" "boot-disk-3" {
  name     = "boot-disk-3"
  type     = "network-hdd"
  zone     = "ru-central1-a"
  size     = "20"
  image_id = "fd83j4siasgfq4pi1qif"
}
resource "yandex_compute_disk" "boot-disk-4" {
  name     = "boot-disk-4"
  type     = "network-hdd"
  zone     = "ru-central1-a"
  size     = "20"
  image_id = "fd83j4siasgfq4pi1qif"
}

resource "yandex_compute_instance" "vm-1" {
  name = "node-1"

  resources {
    cores  = 2
    memory = 2
  }

  boot_disk {
    disk_id = yandex_compute_disk.boot-disk-1.id
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-1.id
    nat       = true
  }

  scheduling_policy {
    preemptible = true
  }

  metadata = {
    user-data = "${file("meta.txt")}"
  }
}
resource "yandex_compute_instance" "vm-2" {
  name = "node-2"

  resources {
    cores  = 4
    memory = 8
  }

  boot_disk {
    disk_id = yandex_compute_disk.boot-disk-2.id
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-1.id
    nat       = true
  }

  scheduling_policy {
    preemptible = true
  }

  metadata = {
    user-data = "${file("meta.txt")}"
  }
}

resource "yandex_compute_instance" "vm-3" {
  name = "node-3"

  resources {
    cores  = 4
    memory = 8
  }

  boot_disk {
    disk_id = yandex_compute_disk.boot-disk-3.id
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-1.id
    nat       = true
  }

  scheduling_policy {
    preemptible = true
  }

  metadata = {
    user-data = "${file("meta.txt")}"
  }
}

resource "yandex_compute_instance" "vm-4" {
  name = "node-4"

  resources {
    cores  = 4
    memory = 8
  }

  boot_disk {
    disk_id = yandex_compute_disk.boot-disk-4.id
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-1.id
    nat       = true
  }

  scheduling_policy {
    preemptible = true
  }

  metadata = {
    user-data = "${file("meta.txt")}"
  }
}

resource "yandex_vpc_network" "network-1" {
  name = "network1"
}

resource "yandex_vpc_subnet" "subnet-1" {
  name           = "subnet1"
  zone           = "ru-central1-a"
  network_id     = yandex_vpc_network.network-1.id
  v4_cidr_blocks = ["192.168.10.0/24"]
}

output "internal_ip_address_vm_1" {
  value = yandex_compute_instance.vm-1.network_interface.0.ip_address
}

output "internal_ip_address_vm_2" {
  value = yandex_compute_instance.vm-2.network_interface.0.ip_address
}

output "internal_ip_address_vm_3" {
  value = yandex_compute_instance.vm-3.network_interface.0.ip_address
}

output "internal_ip_address_vm_4" {
  value = yandex_compute_instance.vm-3.network_interface.0.ip_address
}

output "external_ip_address_vm_1" {
  value = yandex_compute_instance.vm-1.network_interface.0.nat_ip_address
}

output "external_ip_address_vm_2" {
  value = yandex_compute_instance.vm-2.network_interface.0.nat_ip_address
}

output "external_ip_address_vm_3" {
  value = yandex_compute_instance.vm-3.network_interface.0.nat_ip_address
}

output "external_ip_address_vm_4" {
  value = yandex_compute_instance.vm-3.network_interface.0.nat_ip_address
}

resource "local_file" "hosts" {
  content  = <<-EOT
  all:
    hosts:
      node1:
        ansible_user: debian
        ansible_host: ${yandex_compute_instance.vm-1.network_interface.0.nat_ip_address}
        ip: ${yandex_compute_instance.vm-1.network_interface.0.ip_address}
        access_ip: ${yandex_compute_instance.vm-1.network_interface.0.ip_address}
      node2:
        ansible_user: debian
        ansible_host: ${yandex_compute_instance.vm-2.network_interface.0.nat_ip_address}
        ip: ${yandex_compute_instance.vm-2.network_interface.0.ip_address}
        access_ip: ${yandex_compute_instance.vm-2.network_interface.0.ip_address}
      node3:
        ansible_user: debian
        ansible_host: ${yandex_compute_instance.vm-3.network_interface.0.nat_ip_address}
        ip: ${yandex_compute_instance.vm-3.network_interface.0.ip_address}
        access_ip: ${yandex_compute_instance.vm-3.network_interface.0.ip_address}
      node4:
        ansible_user: debian
        ansible_host: ${yandex_compute_instance.vm-4.network_interface.0.nat_ip_address}
        ip: ${yandex_compute_instance.vm-4.network_interface.0.ip_address}
        access_ip: ${yandex_compute_instance.vm-4.network_interface.0.ip_address}
    children:
      kube_control_plane:
        hosts:
          node1:
      kube_node:
        hosts:
          node2:
          node3:
          node4:
      etcd:
        hosts:
          node1:
      k8s_cluster:
        children:
          kube_control_plane:
          kube_node:
      calico_rr:
        hosts: {}
  EOT
  filename = "../kubernetes/kubespray/inventory/mycluster/hosts.yaml"
}
