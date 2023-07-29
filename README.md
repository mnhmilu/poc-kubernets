
# Kubernetes-based microservice 

[Road Map with Milestone](https://docs.google.com/spreadsheets/d/1zxBIoNyymyXTqIBEPrSyXTuE0egg7BfGt3JbsUjvN-M/edit#gid=0)


## Learning Trail



---

[Example 8 ](https://github.com/mnhmilu/poc-kubernets/tree/main/poc/example-8)

Topic: FastAPI in Docker swarm with Postgres database + ORM
```
Key Takeaway: 

- How to configure Docker Swarm by creating a master and worker node 
- How to deploy a FastAPI backend with ORM and Postgres server to run in configured Docker Swarm

```

Steps:

```

Make sure all worker node are ready if not update iptable to allow connect and leave and join again to master 

docker pull postgres:15-alpine // will pull posgres image 

docker-compose build // it will build app image for local

docker stack deploy -c docker-compose.yml nahid_apps  //deploy the stack in docker swarm

now call swagger http://192.168.0.121:8000/docs

table will auto created

user swagger to create a new sample user and get a list to see if it added a new user

for any error see the service logs 

docker service ls

docker service logs nahid_apps_db

```

Commit Ref: 

Readme : [Wiki](https://github.com/mnhmilu/poc-kubernets/wiki/Docker-Swarm-Configuration-in-Home)

---

### Upcoming: Update example 7 with config map, secret and use middleware 


---

[Example 6 updated](https://github.com/mnhmilu/poc-kubernets/tree/main/poc/example-6)

Topic: FastAPI in minikube with Postgres database with configmap and secret
```
Key Takeaway: 

- How to apply configmap and secret in kubernets in deployment file as db user ,password , db host etc
- How to troubleshoot CrashLoopBackOff
  use `kubectl describe pod x ` and then `kubectl logs pods to identify problem
- How to use base64 encoded db username and password in a secret file and how to decode in main.py 

```
Commit Ref: dc1c52e9f6ad98d7e988e9ab3316f5d5fa47b201

---

[Example 7](https://github.com/mnhmilu/poc-kubernets/tree/main/poc/example-7)

Topic: FastAPI with Postgres database using Docker compose and ORM
```
Key Takeaway: 

- Deploy Postgresql database
- Deploy fast API API set with CRUD operation 
- ORM used for Postgres connectivity
- SQLite in database.py for in-memory database
- Service declared in docker-compose file, where fast API connect with db

```

`docker-compose up -d --build`

`docker-compose logs app`

after run:

from browser `http://localhost:8000/docs ` for swagger 


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


[Example 4](https://github.com/mnhmilu/poc-kubernets/blob/main/poc/example-4/k8s-commands.md) 

Topic: Mongo Express with Mongo DB

```
Key Takeaway: 
- How to deploy MongoDB image in Kubernetes with deployment and service without exposing the external world
- How to deploy MongoDB express with exposed service
- How to use Kubernetes Config
- How to use Kubernetes Secret 

```

[Source](https://www.youtube.com/watch?v=X48VuDVv0do)

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




