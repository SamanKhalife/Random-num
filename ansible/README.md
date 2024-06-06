 # testing play book one by one

```
 ansible-playbook ansible-ping-servers.yml
```
```
 ansible-playbook ansible-change-dns.yml
```
```
 ansible-playbook ansible-disabling-swap.yml
```
```
 ansible-playbook ansible-Install-docker.yml
```
```
 ansible-playbook ansible-configuring-containerd.yml
```
```
 ansible-playbook installing-k8s-dependencies.yml
```
```
 ansible-playbook installing_kubeadm_kubelet_kubectl_master.yml
```
```
 ansible-playbook configure_calico.yml
```
```
 ansible-playbook ansible-Install-helm.yml
```
```
 ansible-playbook fetching_new_kubeadm_join_command.yml
```
```
 ansible-playbook installing_kubelet_worker.yml
```
```
 ansible-playbook worker-join-cluster.yml
```
```
 ansible-playbook ansible-helm-deploy-haproxy.yml
```
```
 ansible-playbook ansible-helm-deploy-nginx-Ingress.yml
```
```
 ansible-playbook ansible-helm-deploy-postgress.yml
```
```
 ansible-playbook ansible-helm-deploy-rabbitmq.yml
```
```
 ansible-playbook ansible-helm-deploy-elasticsearch.yml
```
```
 ansible-playbook Ansible-Deploy-Fluentd-Deomonset.yml
```
```
 ansible-playbook ansible-deploy-fluentd-deomonset.yml
```
```
 ansible-playbook deploy-kubernetes-dashboard.yml
```


## or all in one seprate for master and worker nodes
```
ansible-playbook Ansible-Install-Kubernetes-Master.yml
```
```
ansible-playbook Ansible-Install-Kubernetes-Worker.yml
```















