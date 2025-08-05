# install VM's
```bash
# [cyberED/8]
git clone https://github.com/kubernetes-sigs/kubespray.git ansible/kubespray
cp -r ansible/kubespray/inventory/sample ansible/kubespray/inventory/mycluster
terraform init
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

Копируем себе конфиг с мастер ноды
```bash
export NODE_1=$(grep ansible_host inventory/mycluster/hosts.yaml | head -n1 | awk '{print $2}')
ssh debian@${NODE_1} sudo cat /etc/kubernetes/admin.conf > ~/.kube/config
# MAC
sed -i'' -e "s/127.0.0.1/${NODE_1}/g" ~/.kube/config
# Linux
sed -i "s/127.0.0.1/${NODE_1}/g" ~/.kube/config 
```
TEST
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

# install apps

```bash
# [cyberED/8/ansible/kubespray]
cd ../../helm
# [cyberED/8/helm]
## jenkins
helm repo add jenkins https://charts.jenkins.io
helm repo update
helm --kube-insecure-skip-tls-verify --namespace jenkins upgrade --install jenkins --create-namespace jenkins/jenkins -f jenkins_values.yaml
# etcd
helm --kube-insecure-skip-tls-verify --namespace etcd upgrade --install etcd \
  --set persistence.enabled="false" --set replicaCount="3" --set auth.rbac.create=false \
  --create-namespace oci://registry-1.docker.io/bitnamicharts/etcd -f etcd_values.yaml
sleep 15s  
kubectl --insecure-skip-tls-verify -n etcd edit statefulset.apps/etcd  
# Добавить после env ETCD_INITIAL_CLUSTER_STATE:
#       - env:
#         - name: ETCD_INITIAL_CLUSTER_STATE
#           value: new
          
# vault
sleep 70s
helm repo add hashicorp https://helm.releases.hashicorp.com
helm repo update
helm --kube-insecure-skip-tls-verify --namespace vault upgrade --install vault --create-namespace hashicorp/vault -f vault_values.yaml
kubectl --insecure-skip-tls-verify -n vault apply -f vault-security-policy.yaml
```

# prepare vault

```bash
kubectl --insecure-skip-tls-verify -n vault exec -ti vault-0 -- sh
vault operator init
```
OUTPUT
```text
Unseal Key 1: 7HWDOKVhN/sXJk5sxm85jUDtWbE7tc2L8+M9J/WapI3+
Unseal Key 2: VPHtAWPiSp1Pqcrtm4WhQV2h3I/HYRFEjQ05wTuIRD3I
Unseal Key 3: kjK8lyKOjhtOnNsS2VSdYKDM+HUq1qMIAhSlDZCvxtus
Unseal Key 4: hnxmiouNJ0wHnmYjWTfYHX7A8KC7wsmYUEWRrEYv62mR
Unseal Key 5: r4EKhfp7mp95bkHKKjcsFFeLRRgtH3GQOHNEKQZTOfs7

Initial Root Token: hvs.f6jiHnNdAs9SdctrG4PUf6Zx
```
unseal
```bash
vault operator unseal
# Unseal Key 1
vault operator unseal
# Unseal Key 2
vault operator unseal
# Unseal Key 3
```

Повторить еще 2 раза весь этот пункт для vault-1,vault-2 только не выполняя команду vault operator init

TEST
```bash
kubectl --insecure-skip-tls-verify -n vault get po
```
OUTPUT
```text
NAME                                   READY   STATUS    RESTARTS   AGE
vault-0                                1/1     Running   0          8m18s
vault-1                                1/1     Running   0          8m18s
vault-2                                1/1     Running   0          8m18s
vault-agent-injector-bdbbcb8cf-d9djn   1/1     Running   0          8m18s
```

# configure vault

```bash
kubectl --insecure-skip-tls-verify -n vault exec -ti vault-0 -- sh
vault login token=hvs.f6jiHnNdAs9SdctrG4PUf6Zx
vault secrets enable -path=kv kv
vault kv  enable-versioning kv/
vault auth enable approle
# Jenkins
### создадим политику
cat > ~/jenkins.hcl << EOF
path "auth/approle/login" {
  capabilities = [ "create", "read" ]
}

path "kv/data/thp/*" {
  capabilities = [ "read", "update" ]
}
EOF
vault policy write jenkins ~/jenkins.hcl
### создать роль jenkins и связать с политикой
vault write auth/approle/role/jenkins policies=jenkins
```

прочитать role id
```bash
vault read auth/approle/role/jenkins/role-id
```
OUTPUT
```text
Key        Value
---        -----
role_id    e6a4a672-bd27-7ebd-e61f-a6bab052f04f
```

прочитать secret id
```bash
vault write -f auth/approle/role/jenkins/secret-id
```
OUTPUT
```text
Key                   Value
---                   -----
secret_id             aa169070-0137-faba-9cd8-6c3d0b9cacb6
secret_id_accessor    9b07aba2-5007-a758-b0b2-e9605e25bf2d
secret_id_num_uses    0
secret_id_ttl         0s
```

создадим секреты
```bash
vault kv put -mount=kv thp/logstash-kube keystore=ololo redis=azaza truststore=purumpurum
```

# jenkins job

получаем пароль от jenkins
```bash
kubectl --insecure-skip-tls-verify exec --namespace jenkins -it svc/jenkins -c jenkins -- /bin/cat /run/secrets/additional/chart-admin-password && echo
# kubectl --insecure-skip-tls-verify -n jenkins logs -f jenkins-0 -c init
```
OUTPUT
```text
3cdGI9a6cdaSnL7qH2PlhC
```
пробрасываем порт
```bash
kubectl --insecure-skip-tls-verify --namespace jenkins port-forward svc/jenkins 8080:8080
```
открываем в браузере 127.0.0.1:8080 и вводим admin и пароль полученный ранее

1. Manage Jenkins
2. plugins
3. Available Plugins
4. HashiCorp Vault
5. устанавливаем, ставим галку restart
6. заново пробрасываем порт
7. http://127.0.0.1:8080/manage/credentials/store/system/domain/_/newCredentials
8. выбираем Vault app role credential
9. заполняем role_id, secret_id жмем create 
10. сохраняем себе id/name (они одинаковые) // 8cc5136e-1526-41e0-a057-204fe0863712
11. dashboard -> new item
12. имя - vault, тип - pipeline -> ok
13. скрипт:
```text
node {
    // define the secrets and the env variables
    // engine version can be defined on secret, job, folder or global.
    // the default is engine version 2 unless otherwise specified globally.
    def secrets = [
        [path: 'kv/thp/logstash-kube', engineVersion: 2, secretValues: [
            [envVar: 'keystore', vaultKey: 'keystore'],
            [envVar: 'redis', vaultKey: 'redis'],
            [envVar: 'truststore', vaultKey: 'truststore']
            ]]
    ]

    // optional configuration, if you do not provide this the next higher configuration
    // (e.g. folder or global) will be used
    def configuration = [vaultUrl: 'http://vault-ui.vault.svc.cluster.local:8200',
                         vaultCredentialId: '8cc5136e-1526-41e0-a057-204fe0863712',
                         skipSslVerification: 'true',
                         engineVersion: 2]
    
    // inside this block your credentials will be available as env variables
    withVault([configuration: configuration, vaultSecrets: secrets]) {
        sh '''
        echo $truststore >> fucking_file
        echo $keystore >> fucking_file
        echo $redis >> fucking_file
        cat fucking_file
        '''
    }
}
```

# uninstall vault

vault:
helm --kube-insecure-skip-tls-verify --namespace vault uninstall vault
kubectl --insecure-skip-tls-verify delete MutatingWebhookConfiguration consul-consul-connect-injector
