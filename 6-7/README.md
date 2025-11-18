# Requrements
1. install helm https://helm.sh/docs/intro/install/
2. install kubectl https://kubernetes.io/docs/tasks/tools/#kubectl
3. install python 3.10-3.13

# Steps to install LAB
1. cd ansible
2. setup venv (python 3.10-3.13!!!!!!)
    ```bash
    VENVDIR=kubespray-venv
    KUBESPRAYDIR=kubespray
    python3.13 -m venv $VENVDIR
    source $VENVDIR/bin/activate
    ```
3. [OPTIONAL] git clone https://github.com/kubernetes-sigs/kubespray.git
4. cd $KUBESPRAYDIR && python3.13 -m pip install -U -r requirements.txt
5. cd ../../ && terraform apply
6. cd ansible/$KUBESPRAYDIR && ../kubespray-venv/bin/ansible-playbook -i inventory/mycluster/hosts.yaml  --become --become-user=root cluster.yml
7. cd ../
8. [OPTIONAL] git clone https://github.com/madhuakula/kubernetes-goat.git
9. cd kubernetes-goat
10. [OPTIONAL] chmod +x setup-kubernetes-goat.sh && chmod +x access-kubernetes-goat.sh
11. HOST=$(grep ansible_host ../kubespray/inventory/mycluster/hosts.yaml | awk '{print $2}' |head -n1)
12. ssh debian@$HOST sudo 2>/dev/null cat /etc/kubernetes/admin.conf>~/.kube/cybered
13. sed -i '' '"s/127.0.0.1/$HOST/g" ~/.kube/cybered
14. kubectl --insecure-skip-tls-verify --kubeconfig ~/.kube/cybered get no
15. ./setup-kubernetes-goat.sh --insecure --kubeconfig ~/.kube/cybered
16. ./access-kubernetes-goat.sh

# scenarios
https://madhuakula.com/kubernetes-goat/docs/scenarios