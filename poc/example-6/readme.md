
> run all commmand in single command prompt


before start

```
minikube start
eval $(minikube -p minikube docker-env)
docker run -d -p 5000:5000 --restart=always --name registry registry:2 

```

After the source code change in main.py

```
      docker build -t fastapi-app .
      docker tag fastapi-app localhost:5000/fastapi-app:latest
      docker push localhost:5000/fastapi-app:latest
      kubectl delete deployment fastapi-deployment -n poc-kubernetes
      kubectl apply -f fastapi-deployment.yaml 
      kubectl get service
      minikube service fastapi-service

```

      call `http://192.168.39.56-minikubeip:30000/create-item-table` to create item table

      run `pyhton3 client.py` to insert a new item to 'item' table

      call `http://192.168.39.56:30000/items` in browser to see the result 

      minikube ip
      minikube service list

