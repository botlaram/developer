## demo for connection b/w web application and database

https://www.youtube.com/watch?v=X48VuDVv0do&t=6595s


app>  mongo-express 
request to db>  mongodb

## encode value with base64

> echo -n "value" | base64

note: deploy secret.yaml before deployment

> kubectl apply -f mongo-service.yaml

## deploy

> kubectl apply -f mongo.yaml

## get IP Address ie. Endpoint value

> kubectl get service

> kubectl describe service "service-name"


## create mongo-express and deploy

> kubectl apply -f config.yaml   ## deploy config file

> kubectl apply -f mongo-express.yaml   ## deploy yaml

## minikube service is use for sign in for external ip Add.

> minikube service mongo-express-service