1. подключиться к яндекс облаку и создать базовую структуру облако-каталог default
2. активировать грант
3. установить и настроить [yc](https://yandex.cloud/ru/docs/cli/quickstart)
4. установить и
   настроить [terraform](https://yandex.cloud/ru/docs/tutorials/infrastructure-management/terraform-quickstart)

```bash
yc iam service-account create --name cyber-ed # создать сервисный аккаунт cyber-ed
yc iam service-account list # забрать ID, используем в конце следующей команды

yc resource-manager cloud \
add-access-binding <cloud ID, i.e. b1gu8iam2n4hclueenvn> 
--role editor \
--subject serviceAccount:<service-account-id, i.e. aje8e53t99lgldml9eju>

yc iam key create \
  --service-account-id <service-account-id, i.e. aje8e53t99lgldml9eju> \
  --folder-name <имя_каталога_с_сервисным_аккаунтом, i.e. default> \
  --output key.json
  
yc config profile create sa-terraform

yc config set service-account-key key.json
yc config set cloud-id <идентификатор_облака, i.e. b1gu8iam2n4hclueenvn>
yc config set folder-id <идентификатор_каталога, i.e. b1g468ndv61u9tkh3f17>
```

5. пишем скрипт или добавляем в автозапуск строки

```bash
export YC_TOKEN=$(yc iam create-token)
export YC_CLOUD_ID=$(yc config get cloud-id)
export YC_FOLDER_ID=$(yc config get folder-id) 
```

6. запускаем эти команды выбранным способом и проверяем: env | grep YC. Переменные должны быть не пустыми
7. terraform init
8. в файле meta.txt укажите ваш ssh ключ в 8й строчке
9. terraform apply -> yes # должны создаться объекты. можно их посмотреть в облаке

Если всё сделано правильно и приватный ключ ssh лежит по стандартному пути или добавлен в ssh-agent, то после запуска vm
начнется установка docker, как описано в main.tf в строках 84-95. И также если у вм есть выход в интернет, то установка
пройдёт успешно. В конце terraform напишет "Apply complete! Resources: 6 added, 0 changed, 0 destroyed." и выведет
external_ip_address_vm_1 - внешний ip, по которому можно зайти с помощью ключа по ssh:

```bash
ssh debian@84.201.159.107 sudo docker run hello-world
...
Hello from Docker!
This message shows that your installation appears to be working correctly.
...
```

Если вы получили сообщение с приветствием от docker - всё настроено корректно и лабораторная работа считается выполненой

В качестве отчета следует представить скриншот с "Apply complete!" и "Hello from Docker!" - этого будет достаточно.

# Прочее, не относящееся к лабе

Для экономии гранта мы используем автовыключаемые вм. они на 30% дешевле и выключаются яндексом раз в сутки, и далее
играют по модели "pay as you go" - за вычислительные ресурсы не платим пока она выключена, только за диск, но там
копейки.

чтобы вручную убить всё - нужно ввести 
```bash
terraform destroy
```

если у кого-то будет ошибка при terraform init, что мол провайдер не существует, то есть 2 варианта:

1. https://yandex.cloud/ru/docs/tutorials/infrastructure-management/terraform-quickstart#configure-provider
2. включите впн на время terraform init
