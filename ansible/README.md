 # testing play book one by one

```
 ansible-playbook cluster.yml
```
tested done


```
 ansible-playbook deploy-kubernetes-dashboard.yml
```
```
 ansible-playbook ansible-deploy-fluentd-deomonset.yml
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







WARNING: You installed plugins from the krew-index plugin repository.
   These plugins are not audited for security by the Krew maintainers.
   Run them at your own risk.
dont deploy this
```
 ansible-playbook ansible-kubectl-krew-plugin.yml
```












