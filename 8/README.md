# Лабораторная 8 — Vault + GitLab CI в Kubernetes

Строим безопасный CI/CD: **GitLab CE** в Kubernetes (официальный чарт `gitlab/gitlab`) получает
секреты из **Vault** по **JWT/OIDC (ID tokens)**. Vault работает в HA на **Raft**.

**Почему JWT, а не `secrets:vault`:** keyword `secrets:vault` — это Premium/Ultimate. В Community
Edition делаем «ручную» аутентификацию: `id_tokens` (доступен на всех тарифах) выдаёт короткоживущий
JWT, а `vault` CLI в джобе меняет его на Vault-токен и читает kv. Лицензия не нужна.

```
GitLab CI job ──(JWT, id_tokens)──▶ Vault (jwt auth) ──▶ kv/thp/logstash-kube
        ▲                                  │
   раннер в k8s                     ключи проверки JWT берутся
   (сабчарт gitlab-runner)          из GitLab /oauth/discovery/keys
```

---

# быстрый путь: install.sh

Когда kubernetes уже поднят (шаг ниже), весь стенд ставится одной командой:

```bash
./install.sh
```

Скрипт идемпотентен (можно перезапускать) и делает всё, что расписано дальше руками:
Vault на raft (init / raft join / unseal) → PostgreSQL + Redis → GitLab →
Vault UI через Envoy → kv-секрет и jwt-роль в Vault. В конце печатает адреса, пароль root
и root-токен Vault. Unseal-ключи кладёт в `vault-init.json` (chmod 600).

```bash
./install.sh --reset-vault   # снести и переинициализировать ТОЛЬКО Vault (GitLab не трогает)
./install.sh --uninstall     # снести всё
```

> `--reset-vault` нужен, если потерян `vault-init.json`: в нём **единственная** копия unseal-ключей
> и root-токена, Vault их у себя не хранит. Восстановить нельзя (`rekey` и `generate-root` сами
> требуют unseal-ключи) — но и не жалко: всё содержимое Vault создаёт этот же скрипт, а raft лежит
> в `emptyDir`.

Дальше — то же самое **по шагам, руками**: README самодостаточен, скрипт ничего сверх него не делает.

---

# подготовка лабораторной среды

1. подготовьте среду kubernetes (см. инструкцию в папке `kubernetes`)
   ```bash
   cd ../kubernetes
   ```
2. `terraform init`
3. `terraform apply`
4. вернитесь в инструкцию kubernetes (ПУНКТ 2.6) для запуска ansible и установки kubernetes на сервера

> Инфраструктура (`main.tf`): node1 — control-plane, node2–4 — воркеры 4CPU/8GB.
> Урезанный GitLab CE (webservice + sidekiq + gitaly + раннер + envoy) плюс внешние
> postgres/redis занимают ~6–8GB и распределяются по воркерам.

> **Firewall:** в security-group Yandex Cloud откройте входящий TCP **80** на ноды —
> Envoy слушает его прямо на нодах (hostPort). TLS в лабе не используем.

> **DNS не нужен.** Стенд живёт на именах `gitlab.lab.test` / `vault.lab.test`. Зона `.test`
> зарезервирована под тесты (RFC 2606) и реальным TLD не станет. Резолвится это имя **только
> на машине студента**, через `/etc/hosts` — внешние сервисы вроде `nip.io` не используем
> (чужая зависимость, к тому же может быть недоступна). Внутри кластера имя никто не резолвит:
> раннер и Vault ходят по внутренним service-адресам, а Envoy матчит запрос по заголовку `Host`.

---

# install apps

## vault (HA на Raft)

Vault поднимаем в HA на **Integrated Storage (Raft)** — рекомендованном HashiCorp бэкенде.
Raft встроен в Vault, поэтому отдельное хранилище (etcd/Consul) поднимать не нужно.

> Реального persistent storage под кластером нет, поэтому raft-данные лежат в `emptyDir` —
> **HA мы имитируем**. При перезапуске подов данные Vault теряются (нужен заново `operator init`).
> В проде вместо этого был бы PVC (`server.dataStorage.enabled: true`).

Ставим чарт `0.34.0` (это Vault **2.0.3** — appVersion; сам чарт нумеруется как `0.x`):

```bash
helm repo add hashicorp https://helm.releases.hashicorp.com
helm repo update
helm --kube-insecure-skip-tls-verify --namespace vault upgrade --install vault \
  --create-namespace hashicorp/vault --version 0.34.0 -f helm/vault_values.yaml
kubectl --insecure-skip-tls-verify -n vault apply -f helm/vault-security-policy.yaml
```

Поды поднимутся в статусе `0/1 Running` — это нормально, Vault ещё запечатан (sealed).

## зависимости gitlab: postgresql + redis

Начиная с **чарта 10.0.0** GitLab больше **не тянет за собой** PostgreSQL, Redis и MinIO —
они обязаны быть внешними, иначе `helm` падает на проверках конфигурации.

**MinIO при этом не нужен вообще:** в `gitlab_values.yaml` мы выключаем объектное хранилище
целиком (`object_store` + `artifacts`/`lfs`/`uploads`/`packages`). GitLab сложит эти данные на
локальный диск пода — пайплайн лабы artifacts не производит, так что нам хватает.

Остаются PostgreSQL и Redis.

### postgresql

Оператор (CloudNativePG) здесь был бы оверкиллом: нам нужен **один под с базой**, а он тянет
CRD, контроллер и обязательный PVC — а значит и StorageClass, которого в kubespray нет.
Поэтому обычный манифест, как и redis:

```bash
kubectl --insecure-skip-tls-verify create namespace gitlab
kubectl --insecure-skip-tls-verify apply -f k8s/postgres.yaml
```

В манифесте: БД `gitlabhq_production`, пользователь `gitlab`, secret `postgres-app`
(на него ссылается `global.psql.password.secret` в values) и initdb-скрипт с расширениями
`pg_trgm` / `btree_gist`, которые GitLab требует при миграциях.

TEST
```bash
kubectl --insecure-skip-tls-verify -n gitlab rollout status deploy/postgres
```

### redis

Внятного не-bitnami чарта для Redis нет, а нужен он тут как обычный кэш/очередь — поэтому
простой манифест на официальном образе, без пароля и без персистентности:

```bash
kubectl --insecure-skip-tls-verify apply -f k8s/redis.yaml
```

## gitlab (официальный чарт, CE)

1. Берём IP ноды и прописываем имя в `/etc/hosts` **на своей машине**:
   ```bash
   export NODE_IP=$(grep ansible_host ../kubernetes/kubespray/inventory/mycluster/hosts.yaml \
     | tail -n1 | awk '{print $2}')

   echo "${NODE_IP} gitlab.lab.test vault.lab.test" | sudo tee -a /etc/hosts
   ```
2. Ставим чарт:
   ```bash
   helm repo add gitlab https://charts.gitlab.io
   helm repo update
   helm --kube-insecure-skip-tls-verify -n gitlab upgrade --install gitlab \
     gitlab/gitlab --version 10.1.2 \
     -f helm/gitlab_values.yaml \
     --set global.hosts.domain=lab.test
   ```
3. Ждём (первый старт 5–10 минут: миграции БД + подъём webservice):
   ```bash
   kubectl --insecure-skip-tls-verify -n gitlab get po
   ```
   OUTPUT (сокращённо)
   ```text
   NAME                              READY   STATUS      RESTARTS   AGE
   gitlab-webservice-default-...     2/2     Running     0          8m
   gitlab-sidekiq-all-in-1-...       1/1     Running     0          8m
   gitlab-gitaly-0                   1/1     Running     0          8m
   gitlab-gitlab-runner-...          1/1     Running     0          8m
   gitlab-migrations-...             0/1     Completed   0          8m
   envoy-gateway-...                 1/1     Running     0          8m
   envoy-gitlab-...                  1/1     Running     0          8m
   postgres-...                      1/1     Running     0          12m
   redis-...                         1/1     Running     0          12m
   ```

> Раннер (`gitlab-gitlab-runner-...`) идёт сабчартом и **авторегистрируется** — отдельно ставить и
> регистрировать его не нужно. В values он смотрит на GitLab по внутреннему адресу сервиса,
> т.к. `gitlab.lab.test` изнутри кластера не резолвится (его нет в CoreDNS).

### как это выставлено наружу

`ingress-nginx` выведен из эксплуатации, поэтому чарт 10 по умолчанию использует **Gateway API +
Envoy** — им и пользуемся (CRD Gateway API едут внутри чарта, ставить отдельно не надо).

Две правки под bare-metal kubespray — обе в `helm/gitlab_values.yaml`:

- `gatewayApiResources.gateway.protocol: HTTP` — дефолт чарта `HTTPS` (листенер на :443), а мы
  работаем без TLS, поэтому листенер должен быть `HTTP:80`.
- Envoy как **DaemonSet с `hostPort: 80`** вместо Service типа LoadBalancer (его в kubespray нет).
  **NodePort здесь не годится:** он даёт порт 30000–32767, а чарт не умеет порт в `external_url`
  (в `gitlab.yml` рендерятся только `host` и `https`) — GitLab всё равно считал бы, что живёт на
  :80, и после логина редиректил бы в пустоту. Envoy сам сдвигает привилегированные порты
  (80 → 10080) внутри контейнера, а :80 на хосте биндит kubelet — root контейнеру не нужен.

Проверить, что Gateway поднялся и получил адрес:

```bash
kubectl --insecure-skip-tls-verify -n gitlab get gateway,httproute
```

## vault ui через тот же envoy

Раз Envoy уже висит на :80 — прицепим к нему и Vault UI, вместо `port-forward`.

Напрямую это не работает: Gateway чарта пускает маршруты только из своего namespace
(`allowedRoutes: from: Same`), а Vault живёт в другом. Поэтому поднимаем **свой** Gateway в
namespace `vault` того же GatewayClass, а в `gitlab_values.yaml` включён **`mergeGateways: true`** —
Envoy Gateway сажает оба Gateway на один прокси. Уникальность тройки (порт, протокол, hostname)
соблюдена: `HTTP:80 + vault.<IP>` против `HTTP:80 + gitlab.<IP>`.

```bash
kubectl --insecure-skip-tls-verify apply -f k8s/vault-gateway.yaml
```

Vault UI: `http://vault.lab.test`

> **Осторожно:** это открывает Vault UI наружу по HTTP без TLS — root-токен и unseal-ключи
> пойдут по сети открытым текстом. Допустимо только в учебном стенде с одноразовыми данными.
> Не хотите светить Vault — не применяйте этот манифест и ходите через
> `kubectl -n vault port-forward svc/vault-ui 8200:8200`.

---

# prepare vault

С raft хранилище живёт внутри самих подов, поэтому **кластер надо собрать явно**: инициализируем
vault-0, а vault-1 и vault-2 присоединяем к нему через `raft join`.

## 1. Инициализируем vault-0

```bash
kubectl --insecure-skip-tls-verify -n vault exec -ti vault-0 -- sh
vault operator init
```

OUTPUT

```text
Unseal Key 1: <UNSEAL_KEY_1>
Unseal Key 2: <UNSEAL_KEY_2>
Unseal Key 3: <UNSEAL_KEY_3>
Unseal Key 4: <UNSEAL_KEY_4>
Unseal Key 5: <UNSEAL_KEY_5>

Initial Root Token: <ROOT_TOKEN>
```

**Сохраните все 5 unseal-ключей и root-токен — это единственная их копия.** Vault не хранит их
у себя, восстановить неоткуда: `rekey` и `generate-root` сами требуют unseal-ключи.

Распечатываем vault-0 (3 любых ключа) и выходим:

```bash
vault operator unseal   # Key 1
vault operator unseal   # Key 2
vault operator unseal   # Key 3
exit
```

## 2. Присоединяем vault-1 и vault-2

Для **каждого** из `vault-1`, `vault-2`:

```bash
kubectl --insecure-skip-tls-verify -n vault exec -ti vault-1 -- sh
# сначала join к лидеру, потом те же 3 ключа
vault operator raft join http://vault-0.vault-internal:8200
vault operator unseal   # Key 1
vault operator unseal   # Key 2
vault operator unseal   # Key 3
exit
```

> `operator init` выполняется **только на vault-0**. Unseal-ключи у всех нод одни и те же.

TEST

```bash
kubectl --insecure-skip-tls-verify -n vault get po
```

```text
NAME                                   READY   STATUS    RESTARTS   AGE
vault-0                                1/1     Running   0          8m
vault-1                                1/1     Running   0          8m
vault-2                                1/1     Running   0          8m
```

Проверяем, что raft-кластер действительно собрался и выбрал лидера:

```bash
kubectl --insecure-skip-tls-verify -n vault exec -ti vault-0 -- \
  sh -c 'vault login token=hvs.xxxxxxxx >/dev/null && vault operator raft list-peers'
```

OUTPUT

```text
Node       Address                        State       Voter
----       -------                        -----       -----
vault-0    vault-0.vault-internal:8201    leader      true
vault-1    vault-1.vault-internal:8201    follower    true
vault-2    vault-2.vault-internal:8201    follower    true
```

---

# configure vault

Заходим в под и логинимся root-токеном:

```bash
kubectl --insecure-skip-tls-verify -n vault exec -ti vault-0 -- sh
vault login token=hvs.xxxxxxxx
```

Кладём секрет, который потом заберёт pipeline (kv-v2):

```bash
vault secrets enable -path=kv kv-v2
vault kv put -mount=kv thp/logstash-kube keystore=ololo redis=azaza truststore=purumpurum
```

Включаем **jwt auth**. `jwks_url` — внутрикластерный адрес webservice GitLab
(Vault ходит туда за публичным ключом, не завися от внешней сети). `bound_issuer` — внешний хост
GitLab по http (именно он попадает в claim `iss` токена; **без порта**, т.к. ingress на :80):

```bash
vault auth enable jwt

vault write auth/jwt/config \
  jwks_url="http://gitlab-webservice-default.gitlab.svc.cluster.local:8181/oauth/discovery/keys" \
  bound_issuer="http://gitlab.lab.test"
```

Политика — read на секреты:

```bash
cat > /tmp/gitlab.hcl <<'EOF'
path "kv/data/thp/*" {
  capabilities = ["read"]
}
EOF
vault policy write gitlab /tmp/gitlab.hcl
```

Роль `gitlab`, привязанная к политике и **ограниченная проектом** через bound_claims.
`bound_audiences` обязателен (Vault ≥ 1.17), должен совпадать с `aud` из `.gitlab-ci.yml`:

```bash
vault write auth/jwt/role/gitlab - <<'EOF'
{
  "role_type": "jwt",
  "policies": ["gitlab"],
  "token_explicit_max_ttl": 60,
  "user_claim": "user_email",
  "bound_audiences": "http://vault.vault.svc.cluster.local:8200",
  "bound_claims_type": "glob",
  "bound_claims": {
    "project_path": ["root/*", "cybered/*"]
  }
}
EOF
```

> `bound_claims` принимает **список** — совпадение по любому значению, а `bound_claims_type: glob`
> применяет globbing к каждому. Здесь пускаем проекты и в личном namespace root (`root/*`),
> и в группе `cybered` (`cybered/*`) — GitLab на первом входе просит завести группу, поэтому
> проект обычно оказывается именно там.
>
> Для боевого сценария ужимайте до конкретного `"project_id": "<N>"` (ID виден в Settings проекта).
> Полный список claim'ов GitLab —
> в [доке](https://docs.gitlab.com/ci/secrets/id_token_authentication/#token-payload).

Выходим из пода (`exit`).

---

# gitlab: проект и pipeline

## 1. Входим в GitLab

Стартовый пароль root чарт кладёт в secret (действует 24 часа):

```bash
kubectl --insecure-skip-tls-verify -n gitlab get secret gitlab-gitlab-initial-root-password \
  -o jsonpath='{.data.password}' | base64 -d ; echo
```

Открываем в браузере `http://gitlab.lab.test`, логин `root` + пароль.

## 2. Проверяем раннер

**Admin area → CI/CD → Runners** — встроенный раннер должен быть online (зелёный).
Если его нет, создайте instance runner в UI и поставьте отдельно `gitlab/gitlab-runner`
(но по умолчанию сабчарт регистрирует его сам).

## 3. Создаём проект

GitLab на первом входе сам предложит завести группу. Создайте группу `cybered` и в ней проект
`demo` — путь получится `cybered/demo`, он попадает под `bound_claims` роли (`cybered/*`).

Итоговый адрес: `http://gitlab.lab.test/cybered/demo`

## 4. Добавляем pipeline

Файл `8/ci/.gitlab-ci.yml` в этом репозитории — **шаблон**. GitLab ищет пайплайн строго в
**корне проекта**, поэтому он должен лечь в `cybered/demo/.gitlab-ci.yml` (не в подпапку `ci/`).

```bash
# рядом с cyberED, не внутри него
git clone http://gitlab.lab.test/cybered/demo.git
cd demo

cp ../cyberED/8/ci/.gitlab-ci.yml .gitlab-ci.yml   # <- в КОРЕНЬ проекта

git add .gitlab-ci.yml
git commit -m "read vault secrets via JWT"
git push
```

Логин/пароль при `git push` — те же, что в UI (`root` + стартовый пароль).
Через Web IDE тоже можно: New file → имя `.gitlab-ci.yml` → вставить содержимое.

Файл читает
`kv/thp/logstash-kube` через JWT-логин в Vault (см. комментарии внутри).

Коммит запустит pipeline. В нём **два job'а**: секрет они получают одинаково, а обходятся с ним
по-разному.

`leak-secret` — **как делать нельзя**. Секрет добыт правильно, но выброшен в лог открытым текстом:

```text
--- так делать НЕЛЬЗЯ: секрет уходит в лог ---
keystore=ololo
redis=azaza
truststore=purumpurum
```

Лог job'а видит любой, у кого есть доступ к проекту, и он остаётся в GitLab. Это утечка.

`read-secret` — **как правильно**. Доказываем, что секрет получен и он именно тот, не раскрывая
значения:

```text
--- так правильно: значения не печатаем ---
keystore    len=5   sha256=0cb2ac8bcf60
redis       len=5   sha256=...
truststore  len=10  sha256=...
секрет получен и доступен приложению через $keystore / $redis / $truststore
```

Секрет получен из Vault без хранения `secret_id` / паролей в GitLab. 🎉

> **Почему нельзя просто включить masked.** Раннер маскирует только то, о чём ему сказал GitLab:
> CI/CD-переменные с флагом Masked или Premium-keyword `secrets:`. Значения, добытые в рантайме
> через `vault kv get`, раннеру неизвестны — маскировать ему нечего. Плюс требования к
> маскируемому значению (минимум **8 символов**, одна строка, ограниченный набор символов) наши
> `ololo` / `azaza` (по 5) всё равно бы не прошли.
>
> Вывод: **не полагайтесь на маскирование — просто не печатайте секрет.**

---

# как это работает (кратко)

1. Джоба объявляет `id_tokens: VAULT_ID_TOKEN` с `aud` = адрес Vault. GitLab подписывает JWT своим
   ключом; claim `iss` = внешний хост GitLab, `project_path`/`ref`/… описывают, что именно бежит.
2. `vault write auth/jwt/login role=gitlab jwt=$VAULT_ID_TOKEN`: Vault тянет публичный ключ из
   `jwks_url` (webservice GitLab, внутрикластерно), проверяет подпись, `iss` (=`bound_issuer`),
   `aud` (=`bound_audiences`) и `bound_claims`. Если всё сошлось — выдаёт короткоживущий Vault-токен
   с политикой `gitlab`.
3. `vault kv get` читает секрет. Токен живёт ≤ 60с (`token_explicit_max_ttl`).

---

# troubleshooting

- `audience claim does not match any expected audience` — `aud` в `.gitlab-ci.yml` ≠ `bound_audiences`
  роли. Приведите к одному значению.
- `missing role` / `role not found` — роль называется не `gitlab` или не создана.
- `invalid issuer` — `bound_issuer` в Vault ≠ внешнему хосту GitLab (схема `http://`, **без** порта).
- Vault не может достать ключи (`error fetching jwks`) — проверьте, что под Vault резолвит
  `gitlab-webservice-default.gitlab.svc.cluster.local:8181` и что webservice готов.
- Pipeline `pending`, нет раннера — гляньте `kubectl -n gitlab get po -l app=gitlab-runner` и логи;
  раннер должен был авторегистрироваться.
- Webservice долго не поднимается / OOM — уменьшите нагрузку (у нас уже `minReplicas=1`), при
  необходимости добавьте память воркерам в `main.tf`.
- Vault после перезапуска пода снова `sealed` и пустой — это ожидаемо: raft лежит в `emptyDir`.
  Пройдите `operator init` + `raft join` + unseal заново (или включите `dataStorage` с PVC).
- `vault operator raft join` ругается на уже присоединённую ноду — проверьте
  `vault operator raft list-peers`, повторный join не нужен.

---

# uninstall

```bash
# gitlab (вместе со встроенным раннером)
helm --kube-insecure-skip-tls-verify -n gitlab uninstall gitlab

# vault (raft живёт внутри подов, отдельного хранилища сносить не надо)
helm --kube-insecure-skip-tls-verify --namespace vault uninstall vault
```
