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


# use ansible to setup k8s Cluster

```
cd etc/ansible/playbooks
```
```
ansible-playbook cluser.yml
```


## what ansible will do for us ???  

ansible tasks and tags:


| Role Name               | Tags                   | Role-Location    |  whichh Node deployed | 
| ------------------------| -----------------------| ---------------- | ---------------- | 
| updating system         | full,update            | update_system    | master,worker1,work2 |
| unabling swap           | full,disable_swap      | update_system    | master,worker1,work2 | 
| installing prometheus   | full,monitoring        | monitoring       | master,worker1,work2 | 
| installing grafana      | full,monitoring        | monitoring       | helm deploy on k8s|
| installing docker       | full,docker            | docker           | master,worker1,work2 |
| installing kubernetes   | full,K8s               | Kubernetes       | master,worker1,work2 | 
| installing calico       | full,network_policy    | Kubernetes       | master|
| installing helm         | full,package_management| Kubernetes       | master|
| deploying EFK           | full,logging           | logging          | helm deploy on k8s|
| deploying elasticsearch | full,logging           | logging          | helm deploy on k8s|
| deploying kibana        | full,logging           | logging          | helm deploy on k8s|
| deploying rabbitmq      | full,messaging         | messaging        | helm deploy on k8s|
| deploying postgres      | full,database          | database         | helm deploy on k8s|
| installing haproxy.ingress| full,haproxy_ingress | haproxy_ingress | master |



deployment by ansible using tags
```
ansible-playbook -i hosts playbook.yml --tags "tag,tag,..." 
```


## host port usege map

|kubernetes(master)|kubernetes(worker)|rabbitmq|node-exporter|prometheus|mariadb|elastic| kinbana| grafana | fluentd |
| ---------------- | ---------------- | ------ | ----------- | -------- | ----- | ----- | ------ | ------- | ------- | 
|6443     |10250      |5672,5671        |9100 |9090|3306|9200|5601|3000|9880 |
|2379-2380|10256      |5552,5551        |     |    |    |9300|    |    |24224|
|10250    |30000-32767|6000 through 6500|     |    |    |    |    |    |     |
|10259    |           |25672            |     |    |    |    |    |    |     |
|10257    |           |15672, 15671     |     |    |    |    |    |    |     |



ssh-config file
```
~/.ssh/config
```





