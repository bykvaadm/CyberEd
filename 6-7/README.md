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
4. git clone https://github.com/kubernetes-sigs/kubespray.git
4. cd kubespray
5. ./kubespray-venv/bin/ansible-playbook -i inventory/mycluster/hosts.yaml  --become --become-user=root cluster.yml
6. cd ../
7. git clone https://github.com/madhuakula/kubernetes-goat.git
8. cd kubernetes-goat
9. chmod +x setup-kubernetes-goat.sh
10. chmod +x access-kubernetes-goat.sh
11. ./setup-kubernetes-goat.sh
12. ./access-kubernetes-goat.sh

# scenarios
https://madhuakula.com/kubernetes-goat/docs/scenarios