# 1. установка нужного софта

1. install git
2. install curl
3. install helm https://helm.sh/docs/intro/install/
4. install kubectl https://kubernetes.io/docs/tasks/tools/#kubectl
5. install uv https://docs.astral.sh/uv/getting-started/installation/
    ```bash
    # Linux/Macos
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
6. install python 3.10-3.13 (опционально, если питон нужной версии не уставновлен, скачается portable executable)
   ```bash
   uv python install 3.13
   ```

# 2. установка kubernetes

1. склонируйте репозиторий git c kebespray
    ```bash
    git clone https://github.com/kubernetes-sigs/kubespray.git
    ```
2. создадим virtual env с питоном версии 3.13
    ```bash
    uv venv --python 3.13
    ```
3. установим нужные зависимомсти
    ```bash
    uv pip install -r kubespray/requirements.txt
    ```
4. активируем виртуальную среду
    ```bash
    source .venv/bin/activate
    ```
5. вернитесь в лабораторную 6/7/8 для установки серверов терраформом
   ```bash
   cd -
   ```
6. установим kubernetes
    ```bash
    cd kubespray
    ../.venv/bin/ansible-playbook -i inventory/mycluster/hosts.yaml --become --become-user=root cluster.yml
    ```
7. копируем себе конфиг с мастер ноды
   ```bash
   export NODE_1=$(grep ansible_host ../kubernetes/kubespray/inventory/mycluster/hosts.yaml | head -n1 | awk '{print $2}')
   ssh debian@${NODE_1} sudo cat /etc/kubernetes/admin.conf > ~/.kube/config
   # MAC
   sed -i'' -e "s/127.0.0.1/${NODE_1}/g" ~/.kube/config
   # Linux
   sed -i "s/127.0.0.1/${NODE_1}/g" ~/.kube/config 
   ```
8. Проверка работоспособности
   ```bash
   kubectl --insecure-skip-tls-verify get no
   ```
   OUTPUT
   ```text
   NAME    STATUS   ROLES           AGE   VERSION
   node1   Ready    control-plane   14m   v1.31.1
   node2   Ready    <none>          13m   v1.31.1
   node3   Ready    <none>          13m   v1.31.1
   node4   Ready    <none>          13m   v1.31.1
   ```
9. продолжите выполнение лабы 6/7/8
