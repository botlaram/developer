# use the link provided by MS for playground

Here are some commonly used OpenShift commands:

oc login - Log in to the OpenShift cluster.

oc new-project <project-name> - Create a new project.

oc project <project-name> - Switch to a specific project.

oc status - Display the current status of the project.

oc get pods - List all pods in the current project.

oc describe pod <pod-name> - Describe a specific pod.

oc logs <pod-name> - View the logs of a specific pod.

oc get svc - List all services in the current project.

oc describe svc <service-name> - Describe a specific service.

oc expose svc <service-name> - Expose a service to the internet.

oc delete svc <service-name> - Delete a specific service.

oc new-app - Create a new application.

oc edit dc <deployment-config> - Edit a deployment configuration.

oc scale dc <deployment-config> --replicas=<number> - Scale a deployment configuration.

oc rollout latest <deployment-config> - Roll out the latest version of a deployment configuration.


# oc commands
oc
oc login --token=sha**** --server=https://app****  #copy from op gui
oc project

# k8
kubectl get nodes
kucectl get pods
kubectl proxy

# op commands
> oc project <projectname> #ocp110016

# helm commands
trigger in dashboard folder of helm
> helm install azp-demo .

debug
> helm template --dry-run --debug <release-name> .

# check cronjob logs
1. To list all the CronJobs in the current namespace:
> kubectl get cronjobs

2. To get detailed information about a specific CronJob:
> kubectl describe cronjob <cronjob-name>

3. To check the status of the most recent job of a specific CronJob:
> kubectl describe job <job-name>

4. To view the logs of a specific job:
> kubectl logs <pod-name>

5. To view the status of a specific job:
> kubectl describe job <job-name>



# persistent volume claims

persistent volumes are used if you want some data to persist when a pod is terminated or re-scheduled

# selectors in kubernetes

The selector field in the Deployment YAML is used to select which pods the deployment should manage, whereas the selector field in the CronJob YAML is used to select which pods the CronJob should create and manage. If you don't specify a selector in the CronJob YAML, Kubernetes will use a default one that selects all pods with the same name as the CronJob.


