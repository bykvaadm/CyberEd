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

resource "yandex_compute_instance" "vm-1" {
  name = "nginx-1"

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
  name = "nginx-2"

  resources {
    cores  = 2
    memory = 2
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
  name = "nginx-3"

  resources {
    cores  = 2
    memory = 2
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

output "external_ip_address_vm_1" {
  value = yandex_compute_instance.vm-1.network_interface.0.nat_ip_address
}

output "external_ip_address_vm_2" {
  value = yandex_compute_instance.vm-2.network_interface.0.nat_ip_address
}

output "external_ip_address_vm_3" {
  value = yandex_compute_instance.vm-3.network_interface.0.nat_ip_address
}

resource "local_file" "hosts" {
  content  = "[nginx]\nnginx-1 ansible_host=${yandex_compute_instance.vm-1.network_interface.0.nat_ip_address} ansible_user=debian\nnginx-2 ansible_host=${yandex_compute_instance.vm-2.network_interface.0.nat_ip_address} ansible_user=debian\nnginx-3 ansible_host=${yandex_compute_instance.vm-3.network_interface.0.nat_ip_address} ansible_user=debian"
  filename = "ansible/hosts"
}

#resource "null_resource" "baz" {
#  connection {
#    type = "ssh"
#    user = "debian"
#    #password = var.root_password
#    host = yandex_compute_instance.vm-1.network_interface.0.nat_ip_address
#  }
#
#  provisioner "remote-exec" {
#    inline = [
#      "sudo apt update",
#      "sudo apt -y install ca-certificates curl git",
#      "sudo install -m 0755 -d /etc/apt/keyrings",
#      "sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc",
#      "sudo chmod a+r /etc/apt/keyrings/docker.asc",
#      "echo deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian   bookworm stable | sudo tee /etc/apt/sources.list.d/docker.list",
#      "sudo apt update",
#      "sudo apt -y install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin"
#    ]
#  }
#  triggers = {
#    always_run = timestamp()
#  }
#}