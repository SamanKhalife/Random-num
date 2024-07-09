### this project is not fully complete be patient please 
# Random num

Random num generator is an app with helps you to understand how A Modern App Deployment to the infrastructure from base on the linux servers 

# So How It Working:

* 1- Creating 3 Ubuntu servers Using Terraform
* 2- build an Kubernetes Cluster Using Ansible
* 3- building A Docker Image of App and Push it to docker hub
* 4- Try to deploy The app to kubernetes Cluster
* 5- Setting up Monitoring Tool's
* 6- set up firewalls to protect Service's 

##  languages, commponnets, and tools Used in a project
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

## Create Servers Using Terraform

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
ssh-config file
```
~/.ssh/config
```
moving file from directory to etc
```
mv ansible/* ansible/.ansible-lint /etc/ansible/ && cd /etc/ansible/playbooks
```
```
ansible-playbook cluser.yml
```
deployment by ansible using tags
```
ansible-playbook -i hosts playbook.yml --tags "tag,tag,..." 
```

## Tag selection for ansible

ansible tasks and tags:


| Role Name               | Tags                   | Role-Location    |  which Node deployed | 
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






## map port usege

|kubernetes(master)|kubernetes(worker)|rabbitmq|node-exporter|prometheus|mariadb|elastic| kinbana| grafana | fluentd |
| ---------------- | ---------------- | ------ | ----------- | -------- | ----- | ----- | ------ | ------- | ------- | 
|6443     |10250      |5672,5671        |9100 |9090|3306|9200|5601|3000|9880 |
|2379-2380|10256      |5552,5551        |     |    |    |9300|    |    |24224|
|10250    |30000-32767|6000 through 6500|     |    |    |    |    |    |     |
|10259    |           |25672            |     |    |    |    |    |    |     |
|10257    |           |15672, 15671     |     |    |    |    |    |    |     |









