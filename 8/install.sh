#!/usr/bin/env bash
#
# Лабораторная 8 — Vault + GitLab CI в Kubernetes.
# Разворачивает весь стенд: Vault(raft) -> Postgres/Redis -> GitLab -> Vault UI -> Vault JWT.
#
# Предполагается, что кластер kubernetes уже поднят (см. ../kubernetes) и kubectl в него смотрит.
#
# Скрипт идемпотентен: можно перезапускать, установленное не ломается.
#
# Usage:
#   ./install.sh                # поставить всё
#   ./install.sh --reset-vault  # снести и переинициализировать ТОЛЬКО Vault (GitLab не трогает)
#   ./install.sh --uninstall    # снести всё
#
# Про vault-init.json: в нём единственная копия unseal-ключей и root-токена. Vault их у себя
# не хранит — потеряли файл, значит в этот Vault больше не войти (generate-root и rekey сами
# требуют unseal-ключи). Для лабы это не беда: всё содержимое Vault создаёт этот же скрипт,
# а raft лежит в emptyDir. Потеряли ключи -> ./install.sh --reset-vault.
#
set -euo pipefail

cd "$(dirname "$0")"

KUBECTL="kubectl --insecure-skip-tls-verify"
HELM="helm --kube-insecure-skip-tls-verify"

GITLAB_CHART_VERSION="10.1.2"   # GitLab 19.1.2
VAULT_CHART_VERSION="0.34.0"    # Vault 2.0.3

LAB_DOMAIN="lab.test"               # .test зарезервирована под тесты (RFC 2606)
VAULT_INIT_FILE="vault-init.json"   # сюда лягут unseal-ключи и root-токен

# ---------------------------------------------------------------- helpers ---
c_info()  { printf '\n\033[1;34m==> %s\033[0m\n' "$*"; }
c_ok()    { printf '    \033[0;32m✓ %s\033[0m\n' "$*"; }
c_warn()  { printf '    \033[0;33m! %s\033[0m\n' "$*"; }
c_die()   { printf '\n\033[0;31mОШИБКА: %s\033[0m\n' "$*" >&2; exit 1; }

need() { command -v "$1" >/dev/null 2>&1 || c_die "не найден '$1' — установите его"; }

# поле из `vault status -format=json` (vault выходит с кодом 2 когда sealed — гасим)
vault_status() {
  $KUBECTL -n vault exec vault-0 -- vault status -format=json 2>/dev/null || true
}
vault_field() {
  vault_status | python3 -c "
import json,sys
try: print(json.load(sys.stdin).get('$1'))
except Exception: print('')
" 2>/dev/null || echo ''
}

vault_exec() { $KUBECTL -n vault exec vault-0 -- "$@"; }

# Добавить helm-репозиторий. Раньше тут стоял `|| true`, который прятал ошибку add —
# и падало только позже, на install, с невнятным "repo not found". Теперь громко.
# kube-флаги в repo-операциях не нужны, --force-update делает add идемпотентным.
helm_repo() {  # $1=алиас $2=url
  helm repo add "$1" "$2" --force-update >/dev/null \
    || c_die "не удалось добавить helm-репозиторий '$1' ($2)"
  helm repo list 2>/dev/null | awk 'NR>1 {print $1}' | grep -qx "$1" \
    || c_die "helm-репозиторий '$1' не зарегистрировался"
  helm repo update "$1" >/dev/null \
    || c_die "не удалось обновить helm-репозиторий '$1'"
}

# ------------------------------------------------------------- uninstall ---
if [[ "${1:-}" == "--uninstall" ]]; then
  c_info "Сношу стенд"
  $KUBECTL -n vault delete httproute vault-ui --ignore-not-found 2>/dev/null || true
  $KUBECTL -n vault delete gateway vault-gw --ignore-not-found 2>/dev/null || true
  $HELM -n gitlab uninstall gitlab 2>/dev/null || true
  $KUBECTL -n gitlab delete -f k8s/redis.yaml --ignore-not-found 2>/dev/null || true
  $KUBECTL -n gitlab delete -f k8s/postgres.yaml --ignore-not-found 2>/dev/null || true
  $HELM -n vault uninstall vault 2>/dev/null || true
  $KUBECTL delete ns gitlab vault --ignore-not-found 2>/dev/null || true
  rm -f "$VAULT_INIT_FILE"
  c_ok "готово"
  exit 0
fi

# ----------------------------------------------------------- reset-vault ---
# Сносит только Vault (GitLab остаётся). Нужен, когда потеряны unseal-ключи:
# войти в такой Vault уже нельзя, а данные в нём одноразовые — их создаёт этот скрипт.
if [[ "${1:-}" == "--reset-vault" ]]; then
  c_info "Сношу Vault (GitLab не трогаю)"
  $KUBECTL -n vault delete httproute vault-ui --ignore-not-found 2>/dev/null || true
  $KUBECTL -n vault delete gateway vault-gw --ignore-not-found 2>/dev/null || true
  $HELM -n vault uninstall vault 2>/dev/null || true
  $KUBECTL delete ns vault --ignore-not-found 2>/dev/null || true
  $KUBECTL delete mutatingwebhookconfiguration vault-agent-injector-cfg \
    --ignore-not-found >/dev/null 2>&1 || true
  rm -f "$VAULT_INIT_FILE"
  c_ok "Vault снесён. Запустите ./install.sh — он поднимет и настроит его заново"
  exit 0
fi

# ------------------------------------------------------------- preflight ---
c_info "Проверка окружения"
need kubectl; need helm; need python3
$KUBECTL get nodes >/dev/null 2>&1 || c_die "kubectl не достучался до кластера"
c_ok "kubectl, helm, python3, кластер доступен"

# IP ноды нужен только для строчки в /etc/hosts на машине студента
INVENTORY="../kubernetes/kubespray/inventory/mycluster/hosts.yaml"
[[ -f "$INVENTORY" ]] || c_die "нет inventory: $INVENTORY (сначала terraform apply)"
NODE_IP="$(grep ansible_host "$INVENTORY" | tail -n1 | awk '{print $2}')"
[[ -n "$NODE_IP" ]] || c_die "не смог вытащить IP ноды из $INVENTORY"
export NODE_IP

# Внешний DNS не используем (nip.io/sslip.io — чужой сервис, к тому же может быть
# недоступен). Имя фиксированное, в зарезервированной под тесты зоне .test (RFC 2606),
# и резолвится через /etc/hosts на машине студента. Внутри кластера его никто не
# резолвит: раннер и Vault ходят по внутренним service-адресам, а Envoy матчит по Host.
GITLAB_HOST="gitlab.${LAB_DOMAIN}"
VAULT_HOST="vault.${LAB_DOMAIN}"
GITLAB_URL="http://${GITLAB_HOST}"
HOSTS_LINE="${NODE_IP} ${GITLAB_HOST} ${VAULT_HOST}"
c_ok "NODE_IP=${NODE_IP}  ->  ${GITLAB_URL}"

# резолвится ли имя в нужный IP на ЭТОЙ машине
host_resolves() {
  python3 -c "
import socket,sys
try: sys.exit(0 if socket.gethostbyname('$1') == '$NODE_IP' else 1)
except Exception: sys.exit(1)"
}

if host_resolves "$GITLAB_HOST"; then
  c_ok "/etc/hosts: ${GITLAB_HOST} -> ${NODE_IP}"
else
  c_warn "${GITLAB_HOST} не резолвится в ${NODE_IP}"
  c_warn "браузер не откроет GitLab, пока не добавите строчку в /etc/hosts:"
  printf '\n      \033[1mecho "%s" | sudo tee -a /etc/hosts\033[0m\n\n' "$HOSTS_LINE"
  c_warn "на установку в кластер это не влияет — продолжаю"
fi

# ------------------------------------------------------------------ vault ---
c_info "Vault (HA на Raft, chart ${VAULT_CHART_VERSION} = Vault 2.0.3)"
helm_repo hashicorp https://helm.releases.hashicorp.com

# Наследие прежних прогонов, когда agent-injector был включён: контроллер vault-k8s сам
# вписывает caBundle в этот вебхук и становится владельцем поля, а helm 4 (server-side apply)
# при следующем upgrade получает conflict. Инжектор нам не нужен (секреты берём по JWT) —
# сносим вебхук, если он остался с прошлого раза.
$KUBECTL delete mutatingwebhookconfiguration vault-agent-injector-cfg \
  --ignore-not-found >/dev/null 2>&1 || true

$HELM -n vault upgrade --install vault hashicorp/vault \
  --create-namespace --version "$VAULT_CHART_VERSION" \
  -f helm/vault_values.yaml

# поды поднимутся 0/1 (sealed) — ждём Running, а не Ready
for i in 0 1 2; do
  for _ in $(seq 1 60); do
    $KUBECTL -n vault get "pod/vault-${i}" >/dev/null 2>&1 && break
    sleep 5
  done
  $KUBECTL -n vault wait --for=jsonpath='{.status.phase}'=Running "pod/vault-${i}" --timeout=300s
done
$KUBECTL -n vault apply -f helm/vault-security-policy.yaml
c_ok "поды vault-0..2 запущены (пока sealed)"

# --- init ---
c_info "Vault: init / unseal / raft join"
if [[ "$(vault_field initialized)" == "True" ]]; then
  c_ok "уже инициализирован"
  if [[ ! -f "$VAULT_INIT_FILE" ]]; then
    # Vault не хранит unseal-ключи у себя — восстановить их неоткуда.
    # Но данные в нём одноразовые (их создаёт этот же скрипт), поэтому просто пересоздаём.
    c_warn "Vault инициализирован, но ${VAULT_INIT_FILE} потерян — ключей нет."
    c_warn "Восстановить их невозможно (rekey/generate-root сами требуют unseal-ключи)."
    c_warn "Данные в Vault одноразовые, так что просто пересоздайте его:"
    printf '\n      \033[1m./install.sh --reset-vault && ./install.sh\033[0m\n\n'
    c_die "нужен сброс Vault"
  fi
else
  vault_exec vault operator init -format=json -key-shares=5 -key-threshold=3 > "$VAULT_INIT_FILE"
  chmod 600 "$VAULT_INIT_FILE"
  c_ok "инициализирован, ключи -> $VAULT_INIT_FILE"
fi

ROOT_TOKEN="$(python3 -c "import json;print(json.load(open('$VAULT_INIT_FILE'))['root_token'])")"

# без readarray/mapfile — их нет в bash 3.2 (штатный bash на macOS)
UNSEAL_KEYS=()
while IFS= read -r _key; do
  UNSEAL_KEYS+=("$_key")
done < <(python3 -c "
import json
print('\n'.join(json.load(open('$VAULT_INIT_FILE'))['unseal_keys_b64'][:3]))")

unseal_pod() {  # $1 = имя пода
  local pod="$1" sealed key
  sealed="$($KUBECTL -n vault exec "$pod" -- vault status -format=json 2>/dev/null | \
    python3 -c "import json,sys; print(json.load(sys.stdin).get('sealed'))" 2>/dev/null || echo True)"
  if [[ "$sealed" == "False" ]]; then
    c_ok "$pod уже распечатан"
    return
  fi
  for key in "${UNSEAL_KEYS[@]}"; do
    $KUBECTL -n vault exec "$pod" -- vault operator unseal "$key" >/dev/null 2>&1 || true
  done
  c_ok "$pod распечатан"
}

unseal_pod vault-0

# vault-1/2: сперва join к лидеру, потом те же ключи.
# join идемпотентен по факту: если нода уже в кластере — просто ругнётся, гасим.
for i in 1 2; do
  pod="vault-${i}"
  $KUBECTL -n vault exec "$pod" -- \
    vault operator raft join http://vault-0.vault-internal:8200 >/dev/null 2>&1 || true
  sleep 2
  unseal_pod "$pod"
done

sleep 5
c_info "Raft peers"
vault_exec sh -c "VAULT_TOKEN='${ROOT_TOKEN}' vault operator raft list-peers" || \
  c_warn "list-peers не отработал — проверьте вручную"

# ------------------------------------------------- зависимости gitlab ---
c_info "PostgreSQL (один под, без оператора)"
$KUBECTL create namespace gitlab --dry-run=client -o yaml | $KUBECTL apply -f -
$KUBECTL apply -f k8s/postgres.yaml
$KUBECTL -n gitlab rollout status deploy/postgres --timeout=300s
c_ok "postgres готов (БД gitlabhq_production + расширения)"

c_info "Redis"
$KUBECTL apply -f k8s/redis.yaml
$KUBECTL -n gitlab rollout status deploy/redis --timeout=300s
c_ok "redis готов"

# ----------------------------------------------------------------- gitlab ---
c_info "GitLab CE (chart ${GITLAB_CHART_VERSION} = GitLab 19.1.2)"
helm_repo gitlab https://charts.gitlab.io
$HELM -n gitlab upgrade --install gitlab gitlab/gitlab \
  --version "$GITLAB_CHART_VERSION" \
  -f helm/gitlab_values.yaml \
  --set global.hosts.domain="${LAB_DOMAIN}"

c_ok "ждём миграции БД и webservice (первый старт 5–10 минут)"
$KUBECTL -n gitlab rollout status deploy/gitlab-webservice-default --timeout=20m
c_ok "GitLab поднялся"

# ------------------------------------------- vault ui через тот же envoy ---
c_info "Vault UI через Envoy (mergeGateways)"
$KUBECTL apply -f k8s/vault-gateway.yaml
c_ok "http://${VAULT_HOST}"

# ------------------------------------------------- vault: kv + jwt auth ---
# Делается ПОСЛЕ GitLab: Vault на этом шаге ходит за ключами в /oauth/discovery/keys.
c_info "Vault: kv-секрет + jwt auth под GitLab"

JWKS_URL="http://gitlab-webservice-default.gitlab.svc.cluster.local:8181/oauth/discovery/keys"
VAULT_AUD="http://vault.vault.svc.cluster.local:8200"

# rollout завершился — но JWKS может отдаваться не сразу, а Vault полезет за ним прямо сейчас
c_ok "жду, пока GitLab начнёт отдавать JWKS"
_jwks_ok=""
for _ in $(seq 1 60); do
  if $KUBECTL -n vault exec vault-0 -- wget -q -O- "$JWKS_URL" >/dev/null 2>&1; then
    _jwks_ok=1; break
  fi
  sleep 5
done
[[ -n "$_jwks_ok" ]] || c_die "GitLab не отдаёт $JWKS_URL — Vault не сможет проверять подпись JWT"

$KUBECTL -n vault exec -i vault-0 -- sh -s <<EOF
set -e
export VAULT_TOKEN='${ROOT_TOKEN}'

# kv-v2 + секрет, который потом заберёт pipeline
vault secrets enable -path=kv kv-v2 2>/dev/null || true
vault kv put -mount=kv thp/logstash-kube \
  keystore=ololo redis=azaza truststore=purumpurum >/dev/null

# jwt auth: ключи проверки подписи берём у GitLab внутри кластера,
# а iss сверяем со внешним адресом (именно он попадает в токен)
vault auth enable jwt 2>/dev/null || true
vault write auth/jwt/config \
  jwks_url="${JWKS_URL}" \
  bound_issuer="${GITLAB_URL}" >/dev/null

vault policy write gitlab - >/dev/null <<'HCL'
path "kv/data/thp/*" {
  capabilities = ["read"]
}
HCL

vault write auth/jwt/role/gitlab - >/dev/null <<'JSON'
{
  "role_type": "jwt",
  "policies": ["gitlab"],
  "token_explicit_max_ttl": 60,
  "user_claim": "user_email",
  "bound_audiences": "${VAULT_AUD}",
  "bound_claims_type": "glob",
  "bound_claims": {
    "project_path": ["root/*", "cybered/*"]
  }
}
JSON
EOF
c_ok "kv/thp/logstash-kube создан, роль jwt 'gitlab' настроена"

# ------------------------------------------------------------------ итог ---
# base64 -d ведёт себя по-разному в GNU/BSD — декодируем питоном, он уже в зависимостях
ROOT_PW="$($KUBECTL -n gitlab get secret gitlab-gitlab-initial-root-password \
  -o jsonpath='{.data.password}' 2>/dev/null | python3 -c \
  'import sys,base64; sys.stdout.write(base64.b64decode(sys.stdin.read()).decode())' \
  || echo '<не найден>')"

cat <<SUMMARY

$(printf '\033[1;32m═══ Стенд готов ═══\033[0m')

  Если ещё не добавили — строчка в /etc/hosts (иначе браузер не откроет):
    echo "${HOSTS_LINE}" | sudo tee -a /etc/hosts

  GitLab    ${GITLAB_URL}
            login: root
            pass:  ${ROOT_PW}

  Vault UI  http://${VAULT_HOST}
            token: $(printf '\033[0;33m%s\033[0m' "$ROOT_TOKEN")
            (unseal-ключи и токен: ./${VAULT_INIT_FILE}, chmod 600)

  Осталось руками (2 минуты):
    1. Создать группу 'cybered' и в ней проект 'demo'
       (GitLab сам предложит группу на первом входе)
       путь cybered/demo — попадает под bound_claims роли ["root/*", "cybered/*"]
    2. Положить шаблон 8/ci/.gitlab-ci.yml в КОРЕНЬ проекта:
         cybered/demo/.gitlab-ci.yml   (не в подпапку ci/ — GitLab ищет только в корне)
    3. Коммит запустит pipeline. В нём два job'а:
         leak-secret — печатает секрет в лог (как делать НЕЛЬЗЯ, это утечка)
         read-secret — печатает только len+sha256 (как правильно)

  Раннер регистрируется сам (сабчарт gitlab-runner) — проверьте:
    Admin area -> CI/CD -> Runners

$(printf '\033[0;33m!\033[0m') Vault UI открыт наружу по HTTP без TLS — учебный стенд, не прод.

  Снести всё:  ./install.sh --uninstall

SUMMARY
