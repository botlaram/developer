add workflow diagram #todo

1. deploy ArgoCD in k8 cluster
2. Configure AgoCD to Track with Git Repo

## demo

1. create argocd namespace

> kubectl create namespace argocd

2. > kubectl get namespaces   ##display namespace

3. install argo-cd

> kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

4. swtich to the agrocd namespace to get status of running pod

> kubectl config set-context --current --namespace="namespace"

5. > kubectl get pod  ##display pod

6. > kubectl get svc -n argocd        ##display svc

7. port forward to use UI of argocd

> kubectl port-forward svc/argocd-server -n argocd 8080:443

8. copy password to login in Agrocd , username will be default admin

secret key will be stored in "argocd-initial-admin-secret"

> kubectl get secret argocd-initial-admin-secret -n agrocd -o yaml

9. decode password

> "password" | base64 --decode      

Note: in encoding password dont copy %

> kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 --decode && echo
