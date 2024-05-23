
## kubernetes-dashboard 

[kubernetes-dashboard](https://artifacthub.io/packages/helm/k8s-dashboard/kubernetes-dashboard)




## Grafana Helm Chart

[grafana](https://artifacthub.io/packages/helm/grafana/grafana)



## prometheus Helm Chart

[prometheus](https://artifacthub.io/packages/helm/prometheus-community/prometheus)



## Kibana Helm Chart

[kibana](https://artifacthub.io/packages/helm/elastic/kibana)



## Elasticsearch Helm Chart

[elasticsearch](https://artifacthub.io/packages/helm/elastic/elasticsearch)



## ingress-nginx

[ingress-nginx](https://artifacthub.io/packages/helm/ingress-nginx/ingress-nginx)



## HAProxy Ingress helm chart

[haproxy-ingress](https://artifacthub.io/packages/helm/haproxy-ingress/haproxy-ingress)



## mariadb Helm Chart

[mariadb](https://artifacthub.io/packages/helm/bitnami/mariadb)
 


## Bitnami package for RabbitMQ

[rabbitmq](https://artifacthub.io/packages/helm/bitnami/rabbitmq)










if you know nothing about helm here is some explanations
helm search hub:
```
helm search hub nameyouwant-or-app
```


all repos:
```
helm search repo brigade
```
add brige to another repo 
```
helm repo add brigade https://brigadecore.github.io/charts
```

```
helm repo update
```

```
helm install stable/mysql
```
## grafana
```
helm search hub grafana
```

```
helm repo add grafana https://grafana.github.io/helm-charts
```

```
helm repo update
```

```
helm show values grafana/grafana
```

```
helm install grafana grafana/grafana
```

```
helm list
```


```
kubectl get pods
```

```
helm upgrade grafana  grafana/grafana --set replicas=3 --reuse-values
```

```
kubectl get secret --namespace default grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
```

```
kubectl --namespace default port-forward $POD_NAME 3000
```
















