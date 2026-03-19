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
  image_id = "fd8e5jmcvep85j33nt0e"
}

resource "yandex_compute_instance" "vm-1" {
  name = "cis"

  resources {
    cores  = 2
    memory = 4
  }

  boot_disk {
    disk_id = yandex_compute_disk.boot-disk-1.id
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-1.id
    nat       = true
  }

  metadata = {
    user-data = <<EOF
#cloud-config
users:
  - name: ubuntu
    groups: sudo
    shell: /bin/bash
    sudo: 'ALL=(ALL) NOPASSWD:ALL'
    # SSH PUBLIC KEY
    ssh-authorized-keys:
      - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDWDDm3FFVvvV5rkecmGXAmOokKyD1JC6VnQv0T7RQgW9SQzamxFv+KzuxAsGRmDT+yTHUxRrBXIw+DDMJ77yTib1b64rOJOBEChErXvXxbkNY3ukSS+xB4aUcAUH6iq5dx/beqrvl/rz9jDY+6xDSaGQ5CMtYIc1qyO+jiMw0Npo8p5ghX+qiHQPFjpKISwb5k6z2vDvWkZQYb7d1oyZE1kceoKBST8pDB79JNE6+Uuy4KkkXbTBl13ovO0/LJRr/s2sr9N22PM5rK8HclduEyXRxHRDWiv9to+WsEzL36dzBj3oBGMxYqA2dzSG03zwFD/KDyFwuC9Ztypzy364Al
EOF
  }

  scheduling_policy {
    preemptible = true
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

output "external_ip_address_vm_1" {
  value = yandex_compute_instance.vm-1.network_interface.0.nat_ip_address
}

resource "local_file" "private_key" {
  content  = "[servers]\ncis ansible_host=${yandex_compute_instance.vm-1.network_interface.0.nat_ip_address} ansible_user=ubuntu"
  filename = "hosts"
}

resource "null_resource" "baz" {
  connection {
    type = "ssh"
    user = "ubuntu"
    #password = var.root_password
    # если ключ лежит по нестандартному пути, указываем путь к этому файлу.
    # генерируем командой ssh-keygen
    # private_key=""

    # Для Windows:
    # private_key = file("путь/до/файла/в/Windows") на швиндовс
    host = yandex_compute_instance.vm-1.network_interface.0.nat_ip_address
  }

  provisioner "remote-exec" {
    inline = [
      "sudo apt update",
      "sudo apt -y install python3",
    ]
  }
  triggers = {
    always_run = timestamp()
  }
}