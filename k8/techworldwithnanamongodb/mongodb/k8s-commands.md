# this README is regarding demo project using MongoDB and MongoExpress

- TASK **[url](https://youtu.be/X48VuDVv0do?t=4705)**

## Workflow of this TASK

### Workflow1
![image](i./../../../docs/png/mongodbworkflow1.png)

### Workflow2
![image](./../../docs/png/mongodbworkflow2.png)

### kubectl apply commands in order
    
    kubectl apply -f mongo-secret.yaml
    kubectl apply -f mongo.yaml
    kubectl apply -f mongo-configmap.yaml 
    kubectl apply -f mongo-express.yaml

### kubectl get commands

    kubectl get pod
    kubectl get pod --watch
    kubectl get pod -o wide
    kubectl get service
    kubectl get secret
    kubectl get all | grep mongodb

### kubectl debugging commands

    kubectl describe pod mongodb-deployment-xxxxxx
    kubectl describe service mongodb-service
    kubectl logs mongo-express-xxxxxx

### give a URL to external service in minikube

    minikube service mongo-express-service