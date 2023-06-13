# Kubernetes: Package Management with Helm by Kim Schlesinger

# Helm 

Helm is the Pacakge management for kubernetes. Helm deploys all Kubernetes manifests at once and allows you to version and rollback deployments.

# Helm Docs

https://helm.sh/docs/

# Helm hub

https://hub.helm.sh

# kube-state-metrics Package

this package collects data from the kube API Server about objects like Nodes, Deployment, Pods and ConfigMaps. Views CPU and memory usage. this Package assist to check the health ofo the cluster and objects.

## install kube-state-metrics from helm hub

> helm repo add bitnami https://charts.bitnami.com/bitnami 

> helm repo update      # to access the latest version of package

> helm repo list        # to check the package installation

## install kube-state-metrics chart in k8 Cluster

> minikube start 

> kubectl create ns metrics  # kubectl create ns "namespace"

## install Helm Chart in the name of above metrics namepace

> helm install kube-state-metrics bitnami/kube-state-metrics -n metrics      #helm install k"release-name" "pull from the repo"/"name of the helm chart" -n "namespace"

## check installation 

> helm ls -n "namespace"

## check all kind of objects that the chart created in namespace  

> kubectl get all -n metrics

## check logs of pods

> kubectl logs kube-state-metrics-784cfc5f4f-scgkb -n metrics   # kubectl logs "pod-name" -n "namespace"

## check the data that kube-state-metrics is collecting

> kubectl port-forward svc/kube-state-metrics 8080:8080 -n metrics   # kubectl port-forward svc/kube-state-metrics 8080:8080 -n "namespace"

note : in browser type > localhost:8080  && control+C in terminal to exit

## explore the charts from the CmdLine

> helm show chart bitnami/kube-state-metrics  # helm show chart "repo-name"/"chart-name"

## check the values of Chart

> helm show values "repo-name"/"chart-name"  # helm show values bitnami/kube-state-metrics

note : to read this value by copying in a file >> helm show values bitnami/kube-state-metrics > values.yaml

## version of helm chart 

> helm ls -n "namespace" 

note : we can upgrade with latest or previous version of helm

## to use previous version of Helm

> helm upgrade kube-state-metrics bitnami/kube-state-metrics --version 0.4.0 -n metrics          # helm upgrade "release-chart" "flag" --version 0.4.0 -n "namespace"

## delete helm install

> helm delete "release-name"

## create a helm chart

> helm create "chart-name"   # helm create demo

## Deploy configmap in k8 using helm

create a configmap i.e kubernetes object to store env, port values

1. Create configmap.yaml in templates folder and snippet of configmap

2. after that hit the below command

3. we can change version of configmap, if we made diff commits

> helm install first-chart .

## Upgrade the helm

> helm upgrade "release-name" .

## display the changes of configmap.yaml 

> kubectl describe cm "release-name"-configmap

## check release of config map

> kubectl get cm

## debug the yaml files and syntax check

> helm lint .

> helm install --dry-run --debug .

## Deploy secrets in K8 using helm

1. create a secret.yaml and add snipet for secret

2. after helm upgrade

## Display the secret values

> kubectl get secrets

> kubectl describe secret "release-name"

## history of helm logs i.r helm rollback

> helm history first-chart   # helm history first-chart

## Upgrade helm with previous version ir. helm rollback

> helm rollback "release-name"

> helm roolback "release-name" "revision-number"    # to rollback to specific revision number

> helm history first-chart                          # to check the version

## if condition

```
{{if "condition" }}
{{else}}
"condition" 
{{end}}
``` 

## function in helm can be defined by adding in _helpers.tpl file 

eg: 
```
{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "axivion.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "axivion.labels" -}}
helm.sh/chart: {{ include "axivion.chart" . }}
{{ include "axivion.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
responsible: "PhoenixTeam"
# {{- range $key, $value := .Values.labels }}
#   {{ $key }}: {{ $value }}
# {{- end }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "axivion.selectorLabels" -}}
app.kubernetes.io/name: {{ include "axivion.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

```

## update the values of Values.yaml while installtion

> helm install "release-name" --set data.type="9090" 

# Table for commands

| Execute                                           | Commands |
| ------------------------------------------------- | -------- |
| Helm repo add bitnami                             | `helm repo add bitnami https://charts.bitnami.com/bitnami` |
| Helm repo update                                  | `helm repo update` |
| Helm repo list                                    | `helm repo list` |
| Minikube start                                    | `minikube start` |
| Kubectl create namespace                          | `kubectl create ns "namespace"` |
| Helm install kube-state-metrics                   | `helm install kube-state-metrics bitnami/kube-state-metrics -n metrics` |
| Helm create chart                                 | `helm create "chart-name"` |
| Helm lint                                         | `helm lint .` |
| Helm template with debug                          | `helm template --dry-run --debug "release-name" .` |
| Helm install status                               | `helm ls -n "namespace"` |
| Kubectl get all                                   | `kubectl get all -n "namespace"` |
| Helm install with namespace                       | `helm install demo-001 . -n development` |
| Helm upgrade                                      | `helm upgrade "release-name" .` |
| Helm upgrade with namespace                       | `helm upgrade demo-001 . -n development` |
| Helm history                                      | `helm history "release-name"` |
| Helm rollback                                     | `helm rollback "release-name"` |
| Helm rollback with revision                       | `helm rollback "release-name" "revision-number"` |
| Helm upgrade with specific version                | `helm upgrade kube-state-metrics bitnami/kube-state-metrics --version 0.4.0 -n metrics` |
| Helm delete                                       | `helm delete "release-name"` |
| Helm install with updated values                  | `helm install "release-name" --set data.type="9090"` |
| Kubectl port-forward for kube-state-metrics        | `kubectl port-forward svc/kube-state-metrics 8080:8080 -n metrics` |
| Helm show chart                                   | `helm show chart bitnami/kube-state-metrics` |
| Helm show values                                  | `helm show values bitnami/kube-state-metrics` |
| Helm uninstall                                    | `helm uninstall "release-name" . -n "namespace"` |
