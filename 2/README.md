# Харденинг Ubuntu24.04

Лабораторная работа представляет из себя формирование переменных для настройки роли cis_ubuntu2404, с последующим
применением роли на сервере.

1. откройте файл main.yml и проверьте переменные.
2. установите переменные согласно политикам вашей оргиназации (используя существующие и добавляя новые)
3. какие переменные в примере выставлены с нарушением политик безопасности?
4. примените ansible роль к серверу (см. техническая реализация)
5. выполните перезагрузку сервера и проверьте что всё работает
6. в качестве отчёта о выполнении ДЗ выступают:
   а) скриншоты о выполнении харденинга (cis: ok=384 changed=172 unreachable=0 failed=0 skipped=323 rescued=0 ignored=0)
   б) пример выставленных переменных из п.2
   в) пример переменных из п.3

# техническая реализация лабы

1. terraform init
2. terraform apply
3. ansible-galaxy install -r requirements.yml
4. ansible-playbook -i hosts main.yml -bD

# задание со *

примените сканер openscap для ubuntu24.04 и сверьтесь с отчётом. Возможно вы найдёте несколько фальш-позитивов в отчете?
(задание со * не предполагает расшифровки что делать)

# задание с ** (выполнять ПОСЛЕ лекции 8 про vault)

**Disclaimer: это пример работы с vault. мы допускаем использование root токена в целях обучения. для рабочих окружений
стоит создавать политики, регулирующие доступ к секретам и отдельные персональные УЗ**

требования: развёрнутый vault по лабе 8

задача: развернуть этот же playbook, но спрятав секреты в vault

1. устанавливаем vault клиента, например, так:
   ```bash
   pip install hvac # для ansible всё равно ставить придётся
   ```
   ИЛИ
   ```bash
   brew install vault
   ```
2. заводим переменные для подключения. Это самый простой способ, вариантов как это сделать масса.
   ```bash
   export VAULT_ADDR="http://127.0.0.1:8200"
   export VAULT_TOKEN="s.your_root_token_here"
   ```
3. проверяем доступ
   ```bash
   kubectl --insecure-skip-tls-verify --namespace vault port-forward svc/vault-ui 8200:8200 &
   vault status
   curl $VAULT_ADDR/v1/sys/health # OR by curl
   ```

4. заводим key value хранилище, записываем секрет
   ```bash
   vault secrets enable -path=cis kv-v2
   vault kv put cis/golden_images/ubuntu24 \
     grub_password_hash="grub.pbkdf2.sha512.10000.69a2402d73b3a7aaedf97f57b5a824145c4472f16a07dc1dedd7e38faedd1e5306cbece3a77f4bd469053836257803acfbb66c1a2b4ca27c3ef120cdc757ed260ab58b2f4cbe6e537636f597f296d336"
   vault kv get secret/cis/ubuntu24 # проверка
   ```
5. в main.yml меняем ubtu24cis_bootloader_password_hash на следующий, работающий с vault
   ```yaml
   ubtu24cis_bootloader_password_hash: >-
     {{ lookup('community.hashi_vault.hashi_vault',
       'secret=cis/data/golden_images/ubuntu24:grub_password_hash',
       url=lookup('env','VAULT_ADDR'),
       token=lookup('env','VAULT_TOKEN')
     ) }}
   ```
6. предлагается запускать харденинг по виртуалкам k8s
   ```bash
   ansible-playbook -i ../kubernetes/kubespray/inventory/mycluster/hosts.yaml main.yml -bD
   ```
