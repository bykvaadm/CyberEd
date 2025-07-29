1. cd ansible
2. install venv
   #python 3.10-3.13!!!!!!
    ```bash
    VENVDIR=kubespray-venv
    KUBESPRAYDIR=kubespray
    python3.12 -m venv $VENVDIR
    source $VENVDIR/bin/activate
    ```
3. git clone https://github.com/kubernetes-sigs/kubespray.git
4. cd $KUBESPRAYDIR && pip install -U -r requirements.txt
5. cd ../../ && terraform apply
6. cd ansible/$KUBESPRAYDIR && ../kubespray-venv/bin/ansible-playbook -i inventory/mycluster/hosts.yaml  --become --become-user=root cluster.yml
7. kubectl --insecure-skip-tls-verify get no
8. cd ../
9. git clone https://github.com/madhuakula/kubernetes-goat.git
10. cd kubernetes-goat
11. chmod +x setup-kubernetes-goat.sh
12. chmod +x access-kubernetes-goat.sh
13. install helm, kubectl;
14. ssh debian@89.169.159.219 sudo cat /etc/kubernetes/admin.conf > ~/.kube/config_TEMP
15. переименовать ~/.kube/config_TEMP в ~/.kube/config
16. ./setup-kubernetes-goat.sh
17. ./access-kubernetes-goat.sh

# scenarios
https://madhuakula.com/kubernetes-goat/docs/scenarios