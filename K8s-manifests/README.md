to deploy the app go to the directory manually and run ::
```
kubectl apply -k .
``` 

## helm 

for you don't know you can use helm charts to deploy apps to kubernetes:

here is the step by step process to install mariadb:

```
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
```
Install the MariaDB Helm Chart
```
helm install mariadb bitnami/mariadb \
  --set architecture=replication \
  --set replicaCount=3 \
  --set rootUser.password=your-root-password
```
Verify Deployment
```
kubectl get pods
kubectl get svc
```
