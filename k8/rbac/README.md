# hands on RBAC

1. create ns

    ```yaml
    kubectl create ns test
    ```

2. create service account and apply

    ```yaml
    kubectl apply -f serviceaccount.yaml

    ## check permission for service account
    kubectl auth can-i --as system:serviceaccount:test:foo get pods -n test
    ```

3. create role to define permissions for service account

    ```yaml
    note: clusterrole is to define permission for whole cluster

    kubectl apply -f role.yaml
    ```

4. create rolebinding to bind connection between role and service account

    ```yaml
    kubectl apply -f rolebinding.yaml

    ## check permissions to list pods
    kubectl auth can-i --as system:serviceaccount:test:foo get pods -n test

    ## check permissions to create deployment
    kubectl auth can-i --as system:serviceaccount:test:foo create deployment -n test

    ## check permissions to create pods
    kubectl auth can-i --as system:serviceaccount:test:foo create pods -n test
    ```

[YT](https://www.youtube.com/watch?v=rMVHtNNEzmE)
