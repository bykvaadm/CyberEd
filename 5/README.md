0. ДЗ находится тут: https://github.com/bykvaadm/secinfo-docker/tree/master/PartII
1. поднять 2 вм из текущего репозитория
2. далее сделать то, что описано в репозитории выше. При работе с тем репозиторием учитывать:
   - мы не работаем в vagrant, т.е. его не надо ставить, не надо выполнять vagrant up
   - все ip адреса которые указаны в лабе заменить на белые ip, полученные после выполнения п.1
   - vagrant ssh -> ssh debian@ip, где ip - также получен после выполнения п.1
   - провиженинга для терраформа нет, нужно сделать руками =)
   - для простоты доставки файлов на сервер проще всего поставить на них git и спуллить репозиторий из п0. на сервер

---

### Temp readme


      "sudo apt update",
      "sudo apt -y install ca-certificates curl git linux-headers-amd64 linux-image-amd64",
      "sudo install -m 0755 -d /etc/apt/keyrings",
      "sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc",
      "sudo chmod a+r /etc/apt/keyrings/docker.asc",
      "echo deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian   bookworm stable | sudo tee /etc/apt/sources.list.d/docker.list",
      "sudo apt update",
      "sudo apt -y install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin netcat-traditional make"

1. (victim) git clone https://github.com/bykvaadm/secinfo-docker.git
2. (victim) cd 
3. 