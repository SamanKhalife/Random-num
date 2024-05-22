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









































