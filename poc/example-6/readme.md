
> run all commmand in single command prompt


before start

```
minikube start
eval $(minikube -p minikube docker-env)
docker run -d -p 5000:5000 --restart=always --name registry registry:2
kubectl create  namespace poc-kubernetes
kubectl config set-context --current --namespace=poc-kubernetes

```


To generate Base64 dbuser name and password

`echo -n 'nahid' | base64`

`echo -n 'admin' | base64`

To apply secret and configmap 

`kubectl apply -f postgres-configmap.yaml`

`kubectl apply -f postgres-secret.yaml`

To give permission for configmap and secret 

```
      kubectl apply -f configmaps-reader-clusterrole.yaml
      kubectl apply -f configmaps-reader-clusterrolebinding.yaml
      kubectl apply -f secrets-reader-clusterrole.yaml
      kubectl apply -f secrets-reader-clusterrolebinding.yaml
```


Deploy the DB 

```
kubectl apply -f postgres-deployment.yaml


```

Deploy the fast-API service or after the source code change in main.py

```
      docker build -t fastapi-app .
      docker tag fastapi-app localhost:5000/fastapi-app:latest
      docker push localhost:5000/fastapi-app:latest

      kubectl delete deployment fastapi-deployment -n poc-kubernetes
      kubectl apply -f fastapi-deployment.yaml 
      kubectl get service
      minikube service fastapi-service -n poc-kubernetes

```

Test the fast-api

      call `http://192.168.39.56-minikubeip:30000/create-item-table` to create item table

      run `pyhton3 client.py` to insert a new item to 'item' table

      call `http://192.168.39.56-minikubeip:30000/items` in browser to see the result 

About minikube ops

```
      kubectl get configmap
      kubectl get deployment
      minikube ip
      minikube service list
      http://192.168.39.56:30000/docs // for swagger docs

```
