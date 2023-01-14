# milvus helm getting-started guide

```bash
$ brew install minikube

$ minikube start # start cluster 

$ kubectl get sc # check the k8s cluster status

$ brew install helm

$ helm repo add milvus https://milvus-io.github.io/milvus-helm/ 

$ helm repo update # update my local repository

## start milvus

$ helm install my-release milvus/milvus --set cluster.enabled=false --set etcd.replicaCount=1 --set minio.mode=standalone --set pulsar.enabled=false

$ kubectl get pods

NAME                                               READY   STATUS      RESTARTS   AGE
my-release-etcd-0                                  1/1     Running     0          30s
my-release-milvus-standalone-54c4f88cb9-f84pf      1/1     Running     0          30s
my-release-minio-5564fbbddc-mz7f5                  1/1     Running     0          30s

$ kubectl port-forward service/my-release-milvus 27017:19530 # port forward
```

# reference

- https://milvus.io/docs/install_standalone-helm.md


