```
  kubectl create deployment hello-fastapi --image=registry.hub.docker.com/noahgift/fastapi-kube
  kubectl expose deployment hello-fastapi --type=LoadBalancer --port=8080
  kubectl get service hello-fastapi
  minikube service hello-fastapi --url
  curl http://192.168.39.56:31960
```

  But connection refused due to Imagepull backoff problem



  ### Trouble shoot
  
  To view events open exposed url by calling `minikube dashboard --url`

  To view minikube kubernet config file use `cat ~/.kube/config`

  To resole the problem use `minikube ssh docker pulll image-name`



  ### Tutorial followed 

  [Run Simple FastAPI in minikube](https://www.youtube.com/watch?v=WsWlX4wQ7B0)

  [Details Reason here ](https://github.com/mnhmilu/poc-kubernets/wiki/TroubleShoot)
