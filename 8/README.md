# подготовка лабораторной среды 
1. подготовьте среду kubernetes (см. инструкцию в папке "kubernetes")
    ```bash
    cd ../kubernetes
    ```
2. terraform init
3. terraform apply
4. вернитесь в инструкцию kubernetes (ПУНКТ 2.6) для запуска ansible и установке kubernetes на сервера
    ```bash
    cd ../kubernetes
    ```

# install apps

```bash
## jenkins
helm repo add jenkins https://charts.jenkins.io
helm repo update
helm --kube-insecure-skip-tls-verify --namespace jenkins upgrade --install jenkins --create-namespace jenkins/jenkins -f helm/jenkins_values.yaml
# etcd
helm --kube-insecure-skip-tls-verify --namespace etcd upgrade --install etcd \
  --set persistence.enabled="false" --set replicaCount="3" --set auth.rbac.create=false \
  --create-namespace oci://registry-1.docker.io/bitnamicharts/etcd -f helm/etcd_values.yaml
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
helm --kube-insecure-skip-tls-verify --namespace vault upgrade --install vault --create-namespace hashicorp/vault -f helm/vault_values.yaml
kubectl --insecure-skip-tls-verify -n vault apply -f helm/vault-security-policy.yaml
```

# prepare vault

```bash
kubectl --insecure-skip-tls-verify -n vault exec -ti vault-0 -- sh
vault operator init
```
OUTPUT
```text
Unseal Key 1: 9O8HuGSKQLI+oqWbGSfzz+up7drM0UrcNh2q6KRT0gmi
Unseal Key 2: ePrknQICGArB8pk4GA6RVhDAX6FjMjvm3Xg6KwVAF/ci
Unseal Key 3: 8z4zrpgGm1l+0ZQgLxoRHQgjfuAfUf4VJ7YE6ZrPXJ80
Unseal Key 4: J6+TQuGYfDlea4P/9v+vVwTjRDT2QboDdeszasSqqhXC
Unseal Key 5: Pn5iqFdFGX1VTjr5VbDIAm68QWBpzQLysvP3DeOi4gx8

Initial Root Token: hvs.pythjDn2XEhvnLweVKP5VnXW

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
vault login token=hvs.pythjDn2XEhvnLweVKP5VnXW
vault auth enable approle
vault secrets enable -path=kv kv
vault kv enable-versioning kv/

# создадим секреты
vault kv put -mount=kv thp/logstash-kube keystore=ololo redis=azaza truststore=purumpurum

# создадим политику
cat > ~/jenkins.hcl << EOF
path "auth/approle/login" {
  capabilities = [ "create", "read" ]
}

path "kv/data/thp/*" {
  capabilities = [ "read", "update" ]
}
EOF
vault policy write jenkins ~/jenkins.hcl

# создаём роль jenkins и связать с политикой jenkins
vault write auth/approle/role/jenkins policies=jenkins
```

Прочитаем данные для последующей авторизации, сначала role id (грубо говоря логин)
```bash
vault read auth/approle/role/jenkins/role-id
```
OUTPUT
```text
Key        Value
---        -----
role_id    81eda87a-ac1b-d937-089a-94734f91139c
```

прочитаем secret id (грубо говоря пароль)
```bash
vault write -f auth/approle/role/jenkins/secret-id
```
OUTPUT
```text
Key                   Value
---                   -----
secret_id             86cc0273-bc66-5ab2-f4c2-388558ed874a
...
```

# jenkins job

получаем пароль от jenkins
```bash
kubectl --insecure-skip-tls-verify exec --namespace jenkins -it svc/jenkins -c jenkins -- /bin/cat /run/secrets/additional/chart-admin-password && echo
# kubectl --insecure-skip-tls-verify -n jenkins logs -f jenkins-0 -c init
```
OUTPUT
```text
bwhWH5CxiMe9jP4uFTD1rM
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
10. сохраняем себе id/name (они одинаковые) // 3115eae8-f7bd-4af2-a6b8-0f2f2e229c58
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
