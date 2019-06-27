# CCP API From the CLI - Notes

## We need some variables

```
CRED_API_IP=198.18.1.110
CCP_API_USER=admin
CCP_API_PASSWORD=Cisco123
CCP_API_IP=198.18.1.110
```

## First things first! We need to authenticate to the CCP API
Auth to CCP API as new user, get auth token as cookie.
```
curl -k -c ./temp/cookie.txt -H \"Content-Type:application/x-www-form-urlencoded\" -d \"username=$CCP_API_USER&password=$CCP_API_PASSWORD\" https://${CRED_API_IP}/2/system/login/
```

## Now we can get the UUID of the first cluster the user has access too!
```
echo Get the cluster UUID for ${CCP_API_USER}
cluster_uuid=`curl -k -b ./temp/cookie.txt https://${CRED_API_IP}/2/clusters| jq -r '.[]|.name, .uuid' | grep -A1 ${CCP_API_USER} | sed -n 2p`\n
echo ${cluster_uuid}
echo ${cluster_uuid} > .clusteruuid
```

## Now we can request the Kubeconfig (Authentication details to a kubernetes cluster for kubectl to use)
Download our clusters kubeconfig file using UUID
```
curl -k -X GET -b ./temp/cookie.txt https://${CRED_API_IP}/2/clusters/${cluster_uuid}/env > ~/.kube/ccp-config
```

## Now we have credentials for our Kubernetes cluster from CCP, we can use the kubernetes API's and CLI's
```
kubectl --kubeconfig=~/.kube/ccp-config get nodes
kubectl --kubeconfig=~/.kube/ccp-config get deployments
```

# Further Hints

We "POST"-ed a request to the API to create a new cluster with a big blob of JSON data in module 6.
Im pretty sure using the above authentication to CCP, we could easily POST the same (or similar, maybe a cluster name change?) request via a `curl` command to create a new cluster...
