---
hide:
  - navigation
  - tags
---

# Commands

### Git commands

| Execute                                          | Command
| ------------------------------------------------ | ------------------------------------------------
| Git configuration/set username                   | `git config--global user.name "<User name>"`
| Git configuration/set email                      | `git config --global user.email "xyz123@gmail.com"`
| Git configuration list                           | `git config-list`
| Git init                                         | ` git init <Repo Name>`
| Git clone                                        | `git clone <remote Url>`
| Create branch                                    | `git branch <branch name>`
| List all branch names                            | `git branch -a` <br> `git branch --list ` 
| Checkout branch                                  | `git checkout <branch name>`
| Checkout and switch to new branch                | `git checkout -b <branchname>`
| Git add single file                              | `git add <Filename> <Filename>`
| Git add all files                                | `git add .`
| Git status                                       | `git status`
| Git commit                                       | `git commit -m " Commit Message"`
| Git add+commit                                   | `git commit -am " Commit Message"`
| Git push                                         | `git push`
| Delete branch                                    | `git branch -d <branch_name>`
| Delete remote branch                             | `git push origin-delete <branch name>`
| Git commit history                               | `git log`
| Rename branch                                    | `git branch -m <old branch name> <new branch name>`
| Merge branch  | `vscode >` <br> `git clone url` <br> `git checkout main branch` <br> `git pull` <br> `git checkout feature branch` <br> `git merge main_branch` <br> ## if you want to update feature branch with main <br> ## you will get merge conflicts in vscode <br> ## resolve merge conflicts <br> `git commit` <br> ##check branch name and commit to your feature branch <br> `git push feature branch`
| Display the modified files                       | `git log --stat`
| Display the modification on each line of a file  | `git blame <filename> `
| Track changes that have not been staged          | `git diff`
| Track changes that have staged but not committed | `git diff --staged`
| Track the changes after committing a file        | `git diff HEAD`
| Track the changes between two commits            | `git diff <commit1-sha> <commit2-sha>`
| Git Diff Branches                                | `git diff <branch 1> < branch 2>`

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