1. cd ansible
2. install venv
   #python 3.10-3.13!!!!!!
    ```bash
    VENVDIR=kubespray-venv
    KUBESPRAYDIR=kubespray
    python3.12 -m venv $VENVDIR
    source $VENVDIR/bin/activate
    ```
3. cd ansible && git clone https://github.com/kubernetes-sigs/kubespray.git
4. cd $KUBESPRAYDIR && pip install -U -r requirements.txt
5. cd ../../ && terraform apply
6. cd ansible/$KUBESPRAYDIR && ../kubespray-venv/bin/ansible-playbook -i inventory/mycluster/hosts.yaml  --become --become-user=root cluster.yml
7. cd ../
8. git clone https://github.com/madhuakula/kubernetes-goat.git
9. cd kubernetes-goat
10. chmod +x setup-kubernetes-goat.sh
11. chmod +x access-kubernetes-goat.sh
12. ./setup-kubernetes-goat.sh
13. ./access-kubernetes-goat.sh

# scenarios
https://madhuakula.com/kubernetes-goat/docs/scenarios