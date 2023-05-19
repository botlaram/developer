## Karthik Gaekwad linkedin > Getting started with kubernetes

# Microservices  ...?

Microservices are a software development approach that structures an application as a collection of small, independent services that are loosely coupled and can be deployed and scaled independently. In this architecture, each service is responsible for a specific task or set of tasks, and communicates with other services through well-defined APIs.

## Common Microservices Patterns
### 12 The Twelve-Factor App (this methodology help to get for microservices paltform)
1. Codebase

Codebase must be tracked in Version Control and will have many deploys.

2. Dependencies

Instead of copy/pasting , Consider reusable of functions or shared libraries
 
3. Configurations

To store configuration in the environment.

Configurations intregration should never go into the Source Code , it should be part of the environment.

Add configuration via environment variables or config files.

4. Backend Storage Service

Eg : SQL database , Email server

Must be attached for storage and easy in deploy and change

5. Build, Release and Run 

DEVOPS part

6. Processes

Execute the application as stateless process.

7. Port Bindings

Services should be expose with port bindings.

8. Concurrency

Scale out with process model.

9. Disposability

Quick application startup and shutdown times

10. DEV/PROD parity

Application should treated the same way in dev staging or production staging

11. Log Management

Should be able to debug and maintain logs

12. Admin Tasks

Treated the same way in like the rest of the application

Are allowed to run against a released version

# Learning Kubernetes by Kim Schlesinger
# K8 docs

https://kubernetes.io/docs/home/

# KEDA

https://keda.sh/docs/2.1/concepts/

# Auto Scaling Azure Pipeline Using Keda

https://keda.sh/blog/2021-05-27-azure-pipelines-scaler/#:~:text=You%20can%2C%20however%2C%20use%20a%20workaround%20to%20register,the%20placeholder%20agent%20registered%20in%20the%20agent%20pool.

# K8 architecture 

![Architecture](./k8_architecture.jpg)


![IBM K8 Architecture](./k8explainibm.png)


![K8 Work flow Architecture](./k8_workflow_architect.PNG)

# k8 cheat scr templates

https://github.com/bfreuden/kubernetes-cheat-sheet/tree/master/src

# Cloud Native ...?

Cloud Native technologies empowers organizations to build and run scalable applications in modern and dynamic environments such as public, private and hybrid cloud.

Containers, service meshes, microservices, immutable infrastructure and declarative APIs exemplify this approach.

# Minikube 

Minikube is a lightweight Kubernetes implementation that creates a VM on your local machine and deploys a simple cluster containing only one node. Minikube is available for Linux, macOS, and Windows systems.

# Cluster

A Kubernetes cluster is a set of nodes that run containerized applications. Containerizing applications packages an app with its dependences and some necessary services. 

# Control Plane

the control plane refers to the set of components responsible for managing and controlling the cluster's overall operation. It acts as the brain of the Kubernetes cluster, making decisions and maintaining the desired state of the system.

The control plane components work together to provide key functionalities such as scheduling, scaling, maintaining cluster state, handling API requests, and ensuring the overall health and availability of the cluster. These components include:

# API Server

 The Kubernetes API server is the front-end component that exposes the Kubernetes API, which allows users and other components to interact with the cluster. It handles API requests, authentication, and authorization, and serves as the primary entry point for managing the cluster.

# Scheduler

 The scheduler is responsible for placing pods onto suitable nodes in the cluster. It considers factors like resource requirements, node conditions, and affinity/anti-affinity rules when making scheduling decisions. The scheduler ensures optimal resource allocation and even distribution of workloads across the cluster.

# Controller Manager:

 The controller manager runs various controllers that continuously monitor the cluster's state and take actions to maintain the desired state. Some of the built-in controllers include the ReplicaSet controller, Deployment controller, Service controller, and Node controller. Each controller is responsible for managing specific resources or aspects of the cluster.

# etcd

etcd is a distributed key-value store that serves as the cluster's persistent data store. It stores the configuration and state information of the cluster, including cluster-wide settings, object definitions, and runtime data. The control plane components read from and write to etcd to maintain a consistent and up-to-date view of the cluster.


# Worker nodes 

has three components

# kubelet

Kubelet is an agent that runs on every worker node. It makes sure that containers in a pod are running and healthy. It communicate directly with API-server in the contrl plane.

its Kubectl task to pull the image for the container
 
# Container Runtime

A kubelet assigned to new pod starts a container using Container Runtime Interface (CRI). This CRI encables the Kubelet to create containers with the engines

Engines >  Containerd, CRI-o, Kata Containers, AWS firecracker

# KubeProxy

Makes sure that pods and services can communicate with other nodes 
# Nodes

A Node is a worker machine in Kubernetes and may be either a virtual or a physical machine, depending on the cluster. Each Node is managed by the control plane. A Node can have multiple pods, and the Kubernetes control plane automatically handles scheduling the pods across the Nodes in the cluster.

# Namespaces

Namespaces are a way to organize clusters into virtual sub-clusters — they can be helpful when different teams or projects share a Kubernetes cluster. Any number of namespaces are supported within a cluster, each logically separated from others but with the ability to communicate with each other.
A Kubernetes namespace provides the scope for Pods, Services, and Deployments in the cluster. Users interacting with one namespace do not see the content in another namespace

# Services

A Kubernetes Service is an abstraction layer that defines a logical set of Pods (a group of one or more containers) and a policy for accessing them. In other words, a Kubernetes Service is a way to expose an application running on a set of Pods as a network service.

Kubernetes Services allow you to decouple your application from the network by providing a stable IP address and DNS name that can be used to access the application. This allows you to deploy your application in a distributed, scalable way, without having to worry about the underlying network infrastructure.

# LoadBalancer in Service

A LoadBalancer is a type of service that provides external access to the services running inside a cluster. It automatically provisions a load balancer in the cloud provider's infrastructure and maps a unique external IP address to the service, enabling traffic to be distributed across multiple pods.

# Data Storage

There are two ways to store and connect with DataBase by using

1. Connecting database outside the Cluster for eg: Sql DataBase, Azure Sql, Amazon RDS or Google Cloud SQL and configure with cluster

2. K8 Persistent Volume

It is a type of Data Storage the exists within the Cluster , even after the Pods get destroyed.

# ConfigMap 

a configmap is the kubernetes object the store the sensitive data i.e port numbers, env values.

# Secrets

k8 secrets is use to store password and ssh keys

# to start with

Download Minikube install exe file

minikube documentation
https://minikube.sigs.k8s.io/docs/start/


## minikube commands

to create a minikube cluster

> minikube start

explore and check the cluster

> kubectl cluster-info

k8s objects and  display apiVersions and kind

> kubectl api-resources

every resources runs in pods

> kubectl get pods -n kube-system    # for minikube cluster

Etcd logs

> kubectl logs etcd-minikube -n kube-system | jq .     # for minikube


to get detail about the cluster

> kubectl cluster-info dump

to check nodes/worker

> kubectl get nodes

check k8 namespace

> kubectl get namespaces

> kubectl get ns

check k8 pods

> kubectl get pods

> kubectl get pods -A  #-A to check pods in every namespace

check k8 services

> kubectl get services

> kubectl get services -A

create a new namespace using namespace.yaml file

> kubectl apply -f namespace.yaml

delete a namespace

> kubectl delete -f namespace.yaml

> kubectl delete ns "namespace"

create a deployment using deployment.yaml file

> kubectl apply -f deployment.yaml

to check deployment with namespace

> kubectl get deployments -n "namespace"  #kubectl get deployments -n development

check pods for particular namespace

> kubectl get pods -n "namespace"   #kubectl get pods -n development 

Note: namespace is provide in namespace.yaml

delete pods with particular namespace

> kubectl delete pod "pod-name" -n "namespace" #get podname with kubectl get pods -n "namespace"

Note : after deleting the pod, immediately it will create a new pod because in yaml we give replicas as 3

check logs of pods

> kubectl describe pod "pod-name" -n "namespace"

## install busybox with yaml file

Use busybox to test the application can accept traffic from inside the container

> kubectl apply -f busybox.yaml 

to check the busybox installation

> kubectl get pods

IP address of pods , in order to make a request

> kubectl get pods -n "namespace" -o wide

Note : -o wide provides more details about pod along with IP address

Execute commands in container/ interact with container

> kubectl exec -it "pod-name" -- /bin/sh

Inside the busybox container
1. verify with command "wget"

2. in new cmd copy the ip address of any of the one pod, using the following command 

> kubectl get pods -n "namespace" -o wide

3. in busybox container

> wget "ip-address"

Note : you may get error as

> Connecting to 10.244.0.5 (10.244.0.5:80)
> wget: can't connect to remote host (10.244.0.5): Connection refused

In the error ip address is connected with port 80 and in deployment.yaml we mentioned different port numbers , use the port number and follow the below command


> wget "ip-address":"port-number"    #wget 10.244.0.5:3000

> cat index.html  #you can see configuration with pod name

> exit

View application logs

> kubectl get pods -n "namespace"  # list all pods in particular namespace

> kubectl logs "pod-name" -n "namespace"

create a service using service.yaml

Minikube Tunnel start

> minikube tunnel

install service yaml

Kubernetes service assist to configure to External IP address 

> kubectl apply -f service.yaml

find the external ip address to verify the request

> kubectl get services -n "namespace"

Note : it will display along with interna and external ip address 

click on external ip address to visit webpage.

add resources to pods in deployment.yaml

delete k8 resources using yaml file names

Note: delete the files in following order , and delete namespace.yaml file last

> kubectl delete -f deployment.yaml

> kubectl delete -f service.yaml

> kubectl delete -f namespace.yaml

delete minikube cluster

> minikube delete