# Simple nginx setup role

## Задача (общее описание)

Поднять любое "приложение" на 2 серверах (одинаковое), выполнить доступ к этому приложению через балансировщик с
авторизацией через сертификаты.

### Поднимаем приложение

1. terraform apply - поднимаем 3 ВМ. информацию об именах и ip адресах можно увидеть в ansible/hosts
2. запускаем ansible-playbook -i ansible/hosts ansible/main.yaml -bD (Далее - под запускаем ansible везде будет
   подразумеваться эта команда)

   так мы настраиваем nginx на 3 серверах. произведя curl <nginx-1> несколько раз добжны получать nginx-2, nginx-3 в
   ответах.

4. Генерируем сертификаты (где угодно, где есть openssl)

   4.1 Создание сертификатов УЦ
   ```bash
   openssl genrsa -out ca.key 2048
   openssl req -new -x509 -days 3650 -key ca.key -out ca.crt
   ```

   4.2 Создание сертификата сервера.

   Создадим конфигурационный файл server.cnf (в конце указываем nginx-1 ip)
   ```bash
   cat >server.cnf <<EOF
   [req]
   prompt = no
   distinguished_name = dn
   req_extensions = ext
   
   [dn]
   CN = nginx-1.local
   emailAddress = my.email@example.com
   O = Private person
   OU = Alter ego dept
   L = Korolyov
   C = RU
   
   [ext]
   subjectAltName = DNS:nginx-1.local,IP:127.0.0.1,IP:<nginx-1>
   EOF
   ```

   4.3 Создание запроса на сертификат для сервера.

   ```bash
   openssl req -new -utf8 -nameopt multiline,utf8 -config server.cnf -newkey rsa:2048 -keyout server.key -nodes -out server.csr
   ```

   4.4 Создание сертификата по запросу из пункта 4.3.

   ```bash
   openssl x509 -req -days 3650 -in server.csr -CA ca.crt -CAkey ca.key -set_serial 01 -out server.crt -extfile server.cnf -extensions ext
   ```

   4.5 Создание сертификата клиента (Обязательно указываем уникальные Organization Name, Organizational Unit Name,
   Common Name для каждого клиента и они не должны совпадать с указанными для сервера или корневого УЦ)

   ```bash
   openssl req -new -utf8 -nameopt multiline,utf8 -newkey rsa:2048 -nodes -keyout client.key -out client.csr
   openssl x509 -req -days 3650 -in client.csr -CA ca.crt -CAkey ca.key -set_serial 01 -out client.crt
   ```

   4.6 Проверка

   В результате вы должны получить следующий набор файлов:
    - Корневые сертификат и ключ (ca.crt, ca.key)
    - Сертификат, ключ и запрос для клиента (client.crt, client.csr, client.key)
    - Сертификат, ключ и запрос для сервера (server.key, server.crt, server.csr)
    - Конфиг для генерирования сертификатов (server.cnf)

5. Подготовливаем сертификаты для загрузки на сервер.

   Для этого мы запишем сертификаты в переменную nginx_ssl_certs расположив ее в host_vars/nginx-1.yaml. В данном
   примере пропущены значения сертификатов для визуальной наглядности. Конечно, в вашем случае вместо многоточия должны
   быть значения из файлов сертификатов, которые вы ранее сгенерировали.
   ```yaml
   nginx_ssl_certs:
   - name: ca.crt
     value: |
       -----BEGIN CERTIFICATE-----
       ....
       -----END CERTIFICATE-----
   - name: server.crt
     value: |
       -----BEGIN CERTIFICATE-----
       ....
       -----END CERTIFICATE-----
   - name: server.key
     value: |
       -----BEGIN PRIVATE KEY-----
       ....
       -----END PRIVATE KEY-----
   ```

6. Подготовливаем конфиг nginx для загрузки на сервер nginx-1. Для этого прописываем указанный ниже конфиг в
   ansible/host_vars/nginx-1.yaml, запускаем ansible и проверяем: curl -Lk \<nginx-1\>. где -L - follow redirect (http->
   https) а -k - игнорировать что сертификат недоверенный.

   ```yaml
   nginx_config: |
     upstream backend {
      server {{ hostvars['nginx-2']['ansible_host'] }}:80;
      server {{ hostvars['nginx-3']['ansible_host'] }}:80;
     }
     server {
       listen 80;
       server_name nginx-1.local;
       return 301 https://$host:443$request_uri;
     }
     server {
       listen 443 ssl http2;
       server_name nginx-1.local;
       ssl_certificate     ssl/server.crt;
       ssl_certificate_key ssl/server.key;
       #ssl_client_certificate ssl/ca.crt;
       #ssl_verify_client on;
       location / {
         proxy_pass http://backend;
       }
     }  

7. Раскомментируем строки ssl_client_certificate и ssl_verify_client в кинфиге, который мы принесли в п.6 и запускаем
   ansible, принося этот конфиг. Теперь у нас не получится выполнить проверку командой проверки из п.6. Для того чтобы
   теперь обратиться к серверу нужно указать сертификат. Для этого выполним такую команду:
   ```bash
    curl --cacert ssl/ca.crt --cert ssl/client.crt --key ssl/client.key -L <nginx-1>
   ```
   В данном случае -k не требуется, т.к. мы знаем всю цепочку целиком, указывая ca.crt.

   На данном этапе считаем основную часть ЛР законченной. Дальнейшие пункты могут быть выполнены по желанию и описаны
   они менее подробно, рассчитывая что это задача "со звёздочкой"

8. Ограничиваем доступ только для конкретных сертификатов.

   Для того чтобы ходить могли только конкретные сертификаты, нужно рассказать nginx какие из них доверенные. это
   сделать можно например проверяя сериал или хеш сертификата, в данном случае сериал. получаем его так:

   ```bash
   cert=filename.crt serial=$(openssl x509 -in ${cert} -text -noout | grep -A1 Serial | grep -v Serial | tr -d ' ') && \
   echo classic serial: $serial && \
   echo \$ssl_client_serial: $(echo $serial | tr -d ":" | tr '[:lower:]' '[:upper:]')
   ```

   Для этой задачи сгенерируйте еще 2 клиентских сертификата, получите serial и интегрируйте в конфиг

   ```text
   map $ssl_client_serial $reject {
    default 1;
    ..........C5CE16 0; #client1
    ..........635A2D60 0; # client2
   }
   server {
   ...
   location / {
     if ($reject) { return 403; }
     proxy_pass http://backend;
   }
   ....
   ```

   После указанных процедур, приниматься будут только те сертификаты которые указаны в map. Попробуйте поиграться с
   сертификатами добавляя и убирая строки из map чтобы понять что будет возвращать nginx для разрешённого и
   неразрешённого сертификатов.

9. Опционально попробуйте директивы allow и deny для того чтобы разрешить подключаться только с определённых адресов.