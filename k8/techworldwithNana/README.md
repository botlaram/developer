## Use Minikube Cluster

> minikube start

## display nodes

> kubectl get nodes

## display services 

> kubectl get services

## display pods

> kubectl get pods

## create deployment by using commands

> kubectl create deployment "nameofdeployment" --image="imagename" [--dry-run] [options]  ## kubectl create deployment nginx-deploy --image=nginx

## display deployment

> kubectl get deployment

## display ReplicaSet

> kubectl get replicaset

## display deployment file snippet which is deployed using cmd

> kubectl edit deployment "deployment-name"

## debug pods

> kubectl get pods

> kubectl describe pod "pod-name"

## execute inside container 

> kubectl exec -it "pod-name" -- bin/bash

## delete deployments

> kubectl delete deployment "deployment-name"

## deploy using yaml file

> kubectl apply - f deployment.yaml

> kubectl apply -f service.yaml

## debug service

> kubectl describe service "service-name"

## debug pods-name with external IP address

> kubectl get pod -o wide
