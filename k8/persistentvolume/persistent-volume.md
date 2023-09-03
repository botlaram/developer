# About Persistent Volume & PVC

For full documentation visit [persistent-volume](https://jhooq.com/how-to-use-persistent-volume-and-persistent-claims-kubernetes/).

## Persistent Volume Architecture

![pvc](/docs/png/pvc-architecture.png)

![pvc](/docs/png/pvc-architecture.png)

    kubectl apply -f .\persistent-volume.yaml

    kubectl get pv

    kubectl apply -f .\persistent-volume-claim.yaml

    kubectl apply -f .\pod.yaml

