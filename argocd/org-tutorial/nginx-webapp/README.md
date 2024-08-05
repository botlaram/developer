# deployment k8 nginx-webapp

> kubectl create ns demo
> helm template --dry-run --debug webgui .
> helm install webgui .
> kubectl get pods -A
> kubectl get svc -A
> minikube service "service-name" -n=demo