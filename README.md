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

ansible tasks:
```
updating system
unabling swap
installing prometheus
installing grafana
configuring grafana
instaliing docker
installing helm
installing kubernetes and dependencies
deploying EFK
deploying elasticsearch
deploying kibana
deploying rabbitmq
deploying postgres
installing haproxy.ingress
```

## host port usege map

|   kubernetes | ansible      | terraform    | gitlab ci    | rabbitmq     | elastic      | kinbana      | grafana      | fluentd      | mariadb      | prometheus-node exporter |
| ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ |
|              |              |              |              |              |              |              | 3000         |              |              |              |
|              |              |              |              |              |              |              |              |              |              |              |
|              |              |              |              |              |              |              |              |              |              |              |







