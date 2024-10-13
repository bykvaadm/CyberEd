1. terraform apply
2. cd ansible
3. install venv
   #python 3.10-3.12!!!!!!
    ```bash
    VENVDIR=kubespray-venv
    KUBESPRAYDIR=kubespray
    python3.12 -m venv $VENVDIR
    source $VENVDIR/bin/activate
    cd $KUBESPRAYDIR
    pip install -U -r requirements.txt 
    ```
3. cd kubespray
4. ../kubespray-venv/bin/ansible-playbook -i inventory/mycluster/hosts.yaml  --become --become-user=root cluster.yml
5. cd ../kubernetes-goat
6. ./setup-kubernetes-goat.sh
7. ./access-kubernetes-goat.sh
