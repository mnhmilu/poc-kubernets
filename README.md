
# Kubernetes-based microservice 

[Road Map with Milestone](https://docs.google.com/spreadsheets/d/1zxBIoNyymyXTqIBEPrSyXTuE0egg7BfGt3JbsUjvN-M/edit#gid=0)


## Learning Trail

[Example 7](https://github.com/mnhmilu/poc-kubernets/tree/main/poc/example-7)

Topic: FastAPI with Postgres database using Docker compose
```
Key Takeaway: 

- Deploy Postgresql database
- Deploy fast API API set with CRUD operation 
- ORM used for Postgres connectivity

```

`docker-compose up -d --build`

`docker-compose logs app`


[Source](https://fastapi.tiangolo.com/tutorial/sql-databases/#create-a-sessionlocal-class)

---

[Example 6](https://github.com/mnhmilu/poc-kubernets/tree/main/poc/example-6)

Topic: FastAPI in minikube with Postgres database
```
Key Takeaway: 

- Deploy Postgresql database
- Deploy fast API API set with CRUD operation with load balancer
- Python client added for database entry
- Learned how to resolve 'ImpagePullBackoff' problem by running and push in local registry
- Docker Registry created, build an image with name and tag and push to local docker repository
```

---

[Example 5](https://github.com/mnhmilu/poc-kubernets/blob/main/poc/example-5/readme.md)

Topic: FastAPI in minikube
```
Key Takeaway: 
Minikube and docker env sync
Reason behind the imagepullbackoff in minikube's own docker env
How to run simple FastAPI in minikube environment
How to see events easily in minikube dashboard
How to check minikube's kubernet config file
```

---


[Example 4](https://github.com/mnhmilu/poc-kubernets/blob/main/poc/example-4/k8s-commands.md) [Youtube](https://www.youtube.com/watch?v=X48VuDVv0do)

Topic: Mongo Express with Mongo DB

```
Key Takeaway: 
- How to deploy MongoDB image in Kubernetes with deployment and service without exposing the external world
- How to deploy MongoDB express with exposed service
- How to use Kubernetes Config
- How to use Kubernetes Secret 

```


<!-- ROADMAP -->
## Roadmap

  -  [MongoDB with exposed service](https://github.com/mnhmilu/poc-kubernets/tree/main/poc/example-4)
      -  [Kubernetes Tutorial for Beginners by Nana ](https://www.youtube.com/watch?v=X48VuDVv0do)
      -  [Dockerizing FastAPI with Postgres, Uvicorn, and Traefik](https://testdriven.io/blog/fastapi-docker-traefik/)
          - [git-poc-reference](https://github.com/mnhmilu/poc-python/tree/main/fastapi/fastapi-postgre)    

  - [Kuberntes -BaicCronJob](https://github.com/mnhmilu/poc-kubernets/tree/main/poc/cronjob)
  
  - [ISTIO Setup - Sample Book Info- Visualiging Service Mesh](https://istio.io/latest/docs/examples/bookinfo/)
   
    Docker Registry
   
    [ Terraform](https://github.com/mnhmilu/poc-kubernets/tree/main/poc/terraform)
   
    [AWS EKS](https://github.com/mnhmilu/poc-kubernets/tree/main/poc/eksctl)


    
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Resources</summary>
  <ol>
    <li>
      <a href="https://github.com/mnhmilu/microservice/blob/main/learn-plan.MD">Learning Plan Details</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Concepts</a>
      <ul>
        <li><a href="https://github.com/mnhmilu/microservice/blob/main/poc/cronjob/Readme.MD">CronJob</a></li>
        <li><a href="https://www.youtube.com/watch?v=X48VuDVv0do">Persistence Volume</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

### Resoureces

[Learn Plan](https://github.com/mnhmilu/microservice/blob/main/learn-plan.MD)

[Resources](https://github.com/mnhmilu/microservice/blob/main/README.md#resoureces)

[Readme](https://github.com/mnhmilu/microservice/blob/main/poc/cronjob/Readme.MD)


[Persistence Volume](https://www.youtube.com/watch?v=X48VuDVv0do)

[Kubernetics Full Courses](https://www.youtube.com/watch?v=VnvRFRk_51k&list=PLy7NrYWoggjziYQIDorlXjTvvwweTYoNC)

[How to write a good Readme ](https://github.com/othneildrew/Best-README-Template)


### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [![React](https://github.com/mnhmilu/microservice/blob/main/images/kubernet.png)](https://reactjs.org)
* [![React](https://github.com/mnhmilu/microservice/blob/main/images/gitlab.png)](https://reactjs.org)
* [![React](https://github.com/mnhmilu/microservice/blob/main/images/docker.png)](https://reactjs.org)
* [![React](https://github.com/mnhmilu/microservice/blob/main/images/istio.png)](https://reactjs.org)


### Buy me a Coffee! 


<img src="https://github.com/mnhmilu/microservice/blob/main/bmc_qr.png"  width="30%" height="30%">




