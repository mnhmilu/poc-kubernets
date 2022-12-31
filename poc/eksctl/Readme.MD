
### Overview

1) Setup or preparation steps
 - create AWS account
 - create a VPC - virtual private space
 - create an IAM role with Security Group (or in other words: create AWS user with list of permissions)
2) Create Cluster Control Plane - Master Nodes
 - choose basic information like cluster name and k8s version
 - choose region and VPC for your cluster
 - set security
3) Create Worker Nodes and connect to cluster
The Worker Nodes are some EC2 instances with CPU and storage resources.
 - Create as a Node Group
 - Choose cluster it will attach to
 - Define Security Group, select instance type etc.



```
eksctl create cluster \
--name test-cluster \
--version 1.20 \
--region ap-southeast-1 \
--nodegroup-name linux-nodes \
--node-type t2.micro \
--nodes 2
```


``` kubectl get nodes

``` eksctl delete cluster --name test-cluster



### References

[eksctl](https://www.youtube.com/watch?v=p6xDCz00TxU)
