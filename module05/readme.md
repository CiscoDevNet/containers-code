# Deployments

The version of the python app in this directory shows the container hostname instead of a welcome message.

When we use a deployment, we can create a needed number of `replicas`, which will be load balanced between our service.

Repeated calls to the web app will show different names as we hit different replicas.

```
MATJOHN2-M-J0PL:3-Slide43 matjohn2$ cat deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-deployment
  labels:
    app: myapp
spec:
  replicas: 4
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: myapp
        image: trxuk/clus-1999-app3:latest
        ports:
        - containerPort: 5000
```

```
MATJOHN2-M-J0PL:3-Slide43 matjohn2$ kubectl create -f deployment.yaml
deployment "app-deployment" created


MATJOHN2-M-J0PL:3-Slide43 matjohn2$ kubectl get deployment
NAME             DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
app-deployment   4         4         4            1           4s


MATJOHN2-M-J0PL:3-Slide43 matjohn2$ kubectl get po
NAME                              READY     STATUS    RESTARTS   AGE
app-deployment-645c69fdb4-2pfg4   1/1       Running   0          8s
app-deployment-645c69fdb4-kvxtf   1/1       Running   0          8s
app-deployment-645c69fdb4-m2l2h   1/1       Running   0          8s
app-deployment-645c69fdb4-tzkv2   1/1       Running   0          8s
myapp                             1/1       Running   2          51m
```

```
MATJOHN2-M-J0PL:latam-demos matjohn2$ kubectl describe service myapp-service
Name:                     myapp-service
Namespace:                default
Labels:                   <none>
Annotations:              <none>
Selector:                 app=myapp
Type:                     NodePort
IP:                       10.106.188.233
LoadBalancer Ingress:     localhost
Port:                     <unset>  5000/TCP
TargetPort:               5000/TCP
NodePort:                 <unset>  30057/TCP
Endpoints:                10.1.0.26:5000,10.1.0.27:5000,10.1.0.28:5000 + 1 more...
Session Affinity:         None
External Traffic Policy:  Cluster
Events:                   <none>
```

Notice the multiple endpoints, four in total.

Use `kubectl edit deployment app-deployment` to increase the number of replicas!
