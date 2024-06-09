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
 ansible-playbook installing-kubeadm-kubelet-kubectl-master.yml
```
```
 ansible-playbook configure-calico.yml
```
```
 ansible-playbook ansible-Install-helm.yml
```

```
 ansible-playbook fetching-new-kubeadm-join-command.yml
```
```
 ansible-playbook installing-kubelet-worker.yml
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


WARNING: You installed plugins from the krew-index plugin repository.
   These plugins are not audited for security by the Krew maintainers.
   Run them at your own risk. 
dont deploy this 
```
 ansible-playbook ansible-kubectl-krew-plugin.yml
```












