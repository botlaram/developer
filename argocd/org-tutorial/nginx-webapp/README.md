# deployment k8 nginx-webapp

> kubectl create ns demo

> helm template --dry-run --debug webgui .

> helm install webgui .

> kubectl get pods -A

> kubectl get svc -A

> minikube service "service-name" -n=demo

# install argocd

> kubectl create ns argocd

> kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

> kubectl get svc -A

> kubectl port-forward svc/argocd-server -n argocd 9090:443

> kubectl get secret argocd-initial-admin-secret -n argocd -o yaml

> create project in argocd add repo

> connect repo

> in create application choose helm, it should provide path of argocd
