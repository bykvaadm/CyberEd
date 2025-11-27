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

# подготовка заданий

1. git clone https://github.com/madhuakula/kubernetes-goat.git
2. cd kubernetes-goat
3. chmod +x setup-kubernetes-goat.sh && chmod +x access-kubernetes-goat.sh
4. ./setup-kubernetes-goat.sh --insecure --kubeconfig ~/.kube/config
5. ./access-kubernetes-goat.sh --insecure --kubeconfig ~/.kube/config

# scenarios

https://madhuakula.com/kubernetes-goat/docs/scenarios
