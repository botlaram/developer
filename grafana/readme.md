# host garafana

## clone repo

https://github.com/iam-veeramalla/observability-zero-to-hero

## start minikube

`minikube start`

## install prometheus

## Install prometheus using Helm

### Add helm repo

`helm repo add prometheus-community https://prometheus-community.github.io/helm-charts`

### Update helm repo

`helm repo update`

### Install prometheus helm

`helm install prometheus prometheus-community/prometheus`

### Expose Prometheus Service

This is required to access prometheus-server using your browser.

`kubectl expose service prometheus-server --type=NodePort --target-port=9090 --name=prometheus-server-ext`

`minikube service prometheus-server-ext`

## Install grafana using Helm

### install grafana helm repo

`helm repo add grafana https://grafana.github.io/helm-charts`

### Update helm repo for grafana

`helm repo update`

### Install helm

`helm install grafana grafana/grafana`

### Expose Grafana Service

`kubectl expose service grafana — type=NodePort — target-port=3000 — name=grafana-ext`
