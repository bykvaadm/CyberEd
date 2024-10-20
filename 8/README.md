# install VM's
```bash
# [cyberED/8]
git clone https://github.com/kubernetes-sigs/kubespray.git ansible/kubespray
cp -r ansible/kubespray/inventory/sample ansible/kubespray/inventory/mycluster
terraform apply
```

# prepare environment

use strongly python 3.10-3.12!!!!!!

```bash
# [cyberED/8]
python3.12 -m venv ansible/kubespray-venv
source ansible/kubespray-venv/bin/activate
cd ansible/kubespray
# [cyberED/8/ansible/kubespray]
pip install -U -r requirements.txt 
```

install additional requirements if you don't have ones:
- helm
- kubectl

# install kubernetes   

```bash
# [cyberED/8/ansible/kubespray]
../kubespray-venv/bin/ansible-playbook -i inventory/mycluster/hosts.yaml --become --become-user=root cluster.yml
```

ssh to node-1, copy /etc/kubernetes/kubeadmin.conf to localhost ~/.kube/config

# install apps

```bash
# [cyberED/8/ansible/kubespray]
cd ../../helm
# [cyberED/8/helm]
## jenkins
helm repo add jenkins https://charts.jenkins.io
helm repo update
helm --kube-insecure-skip-tls-verify --namespace jenkins upgrade --install jenkins --create-namespace jenkins
#### kubectl --insecure-skip-tls-verify --namespace jenkins port-forward svc/jenkins 8080:8080
kubectl --insecure-skip-tls-verify exec --namespace jenkins -it svc/jenkins -c jenkins -- /bin/cat /run/secrets/additional/chart-admin-password && echo
# etcd
helm --kube-insecure-skip-tls-verify --namespace etcd upgrade --install etcd \
    --set persistence.enabled="false" --set replicaCount="3" --set auth.rbac.create=false \
    --create-namespace oci://registry-1.docker.io/bitnamicharts/etcd
# vault
helm repo add hashicorp https://helm.releases.hashicorp.com
helm --kube-insecure-skip-tls-verify --namespace vault upgrade --install vault --create-namespace vault
```





# uninstall vault

vault:
helm --kube-insecure-skip-tls-verify --namespace vault uninstall vault
kubectl --insecure-skip-tls-verify delete MutatingWebhookConfiguration consul-consul-connect-injector
