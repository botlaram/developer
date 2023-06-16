# Table for commands

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
