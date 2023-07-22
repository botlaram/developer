---
hide:
  - navigation
  - tags
---

# Devops 

## persistent volume claims

persistent volumes are used if you want some data to persist when a pod is terminated or re-scheduled

## selectors in kubernetes

The selector field in the Deployment YAML is used to select which pods the deployment should manage, whereas the selector field in the CronJob YAML is used to select which pods the CronJob should create and manage. If you don't specify a selector in the CronJob YAML, Kubernetes will use a default one that selects all pods with the same name as the CronJob.

## Commands

### OpenShift commands

Log in to the OpenShift cluster.

    oc login

Create a new project.

    oc new-project <project-name>

Switch to a specific project.

    oc project <project-name>

Display the current status of the project.

    oc status 

List all pods in the current project.

    oc get pods 

Describe a specific pod.

    oc describe pod <pod-name> 

View the logs of a specific pod.

    oc logs <pod-name> 

List all services in the current project.

    oc get svc 

Describe a specific service.

    oc describe svc <service-name> 

Expose a service to the internet.

    oc expose svc <service-name> 


Delete a specific service.

    oc delete svc <service-name> 

Create a new application.

    oc new-app 

Edit a deployment configuration.

    oc edit dc <deployment-config> 

Scale a deployment configuration.

    oc scale dc <deployment-config> --replicas=<number> 

Roll out the latest version of a deployment configuration.

    oc rollout latest <deployment-config> 

### Kubernetes commands

| Execute                                          | Command
| ------------------------------------------------ | ------------------------------------------------
| To start Minikube                                | `minikube start`
| Create a namespace                               | `kubectl create namespace development`
| Create a deployment using kubectl command         | `kubectl create deployment "nameofdeployment" --image="imagename"`<br>Example: `kubectl create deployment nginx-deploy --image=nginx`
| Deploy using a YAML file                          | `kubectl apply -f deployment.yaml`
| Display nodes                                    | `kubectl get nodes`
| Display services                                 | `kubectl get services`
| Display pods                                     | `kubectl get pods`
| Display describe pods                            | `kubectl describe pod "pod-name"`
| Display pods with a specific namespace           | `kubectl get pods -n "namespace"`
| Display deployments                              | `kubectl get deployment`
| Display ReplicaSets                              | `kubectl get replicaset`
| Display config maps                              | `kubectl get cm`
| Display Get Jobs                                 | `kubectl get jobs -n namespace`
| Display Scaled Jobs                              | `kubectl describe scaledjob <scaledjob-name> -n <namespace>`
| Display Secret Provider class                    | `kubectl get secretproviderclass`
| Display service status                           | `kubectl describe service "service-name"`
| Display changes of a config map                   | `kubectl describe cm "release-name"-configmap`
| Switch to a different namespace                   | `kubectl config set-context --current --namespace="namespace"`
| Display deployment file snippet in VS Code        | `$env:KUBE_EDITOR="code --wait" > kubectl edit deployment "deployment-name"`
| Display pod status                               | `kubectl get pods`<br>`kubectl describe pod "pod-name"`
| Display Secrets                                  | `kubectl get secret`
| Display describe secrets                         | `kubectl describe secret "secret-name"`
| Debug pod status with a specific namespace       | `kubectl describe pod "pod-name" -n development`
| Debug pods with external IP addresses             | `kubectl get pod -o wide`
| Display pod logs                                 | `kubectl logs "pod-name" -n development`
| Interact with pods                               | `kubectl exec -it "pod-name" -- /bin/bash`
| Delete all pods                                  | `kubectl delete pods --all -n development`
| Delete deployments                               | `kubectl delete deployment "deployment-name"`

### Helm commands

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
