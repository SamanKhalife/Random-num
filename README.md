# Random-num-test-project
test project to start working with Kubernetes, Rabbitmq, Mariadb, Fluentd and Elasticsearch.

## project used commponnets and tools
```
python
docker
kubernetes
ansible
terraform
gitlab ci
kernel tunning
rabbitmq
elastic
kinbana
grafana
prometheus-node exporter
fluentd
mariadb
```

## applying terraform

```
cd /random-num/terraform
```
Initializing Terraform: to Downloads and installs plugins , Validates and downloads modules 
```
terraform init
```
Creating an execution plan
```
terraform plan
```
 Applying the execution plan
```
terraform apply
```

If needed, destroy all resources managed by this configuration
```
terraform destroy
```

## what ansible will do for us ???  

ansible tasks and tags:


| Role Name               | Tags                   | Role-Location    | 
| ------------------------| -----------------------| ---------------- |
| updating system         | full,update            | update_system    |
| unabling swap           | full,disable_swap      | update_system    |
| installing prometheus   | full,monitoring        | monitoring       |
| installing grafana      | full,monitoring        | monitoring       |
| configuring grafana     | full,monitoring        | monitoring       |
| installing docker       | full,docker            | docker           |
| installing kubernetes   | full,K8s               | Kubernetes       |
| installing calico       | full,network_policy    | Kubernetes       |
| installing helm         | full,package_management| Kubernetes       |
| deploying EFK           | full,logging           | logging          |
| deploying elasticsearch | full,logging           | logging          |
| deploying kibana        | full,logging           | logging          |
| deploying rabbitmq      | full,messaging         | messaging        |
| deploying postgres      | full,database          | database         |
| installing haproxy.ingress| full,haproxy_ingress | haproxy_ingress |



deployment by ansible using tags
```
ansible-playbook -i hosts playbook.yml --tags "tag,tag,..." 
```


## host port usege map

|   kubernetes | ansible      | terraform    | gitlab ci    | rabbitmq     | elastic      | kinbana      | grafana      | fluentd      | mariadb      | prometheus-node exporter |
| ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ |
|              |              |              |              |              |              |              | 3000         |              |              |              |
|              |              |              |              |              |              |              |              |              |              |              |
|              |              |              |              |              |              |              |              |              |              |              |







