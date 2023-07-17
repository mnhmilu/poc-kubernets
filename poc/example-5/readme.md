
### Key Take away

- Minikube and docker env sync
- Reason behind the imagepullbackoff in minikube's own docker env
- How to run simple FastAPI in minikube environment
- How to see events easily in minikube dashboard
- How to check minikube's kubernet config file


```
  kubectl create deployment hello-fastapi --image=registry.hub.docker.com/noahgift/fastapi-kube
  kubectl expose deployment hello-fastapi --type=LoadBalancer --port=8080
  kubectl get service hello-fastapi
  minikube service hello-fastapi --url
  curl http://192.168.39.56:31960
```

  But the connection refused due to Imagepull backoff problem



  ### Troubleshoot
  
  To view events open the exposed url by calling `minikube dashboard --url`

  To view minikube kubernet config file use `cat ~/.kube/config`

  To solve the problem use `minikube ssh docker pulll image-name`

  or

  use host docker env to minikube by   `eval $(minikube docker-env)`



  ### Tutorial followed 

  [Run Simple FastAPI in minikube](https://www.youtube.com/watch?v=WsWlX4wQ7B0)

  [Details Reason here ](https://github.com/mnhmilu/poc-kubernets/wiki/TroubleShoot)

  [minikube common problem](https://github.com/mnhmilu/poc-kubernets/wiki/Minikube-common-problem)
