

## frequently used commands


```bash
$ minikube start

$ helm delete my-release

$ helm install my-release milvus/milvus --set cluster.enabled=false --set etcd.replicaCount=1 --set minio.mode=standalone --set pulsar.enabled=false

$ kubectl get pods
NAME                                            READY   STATUS    RESTARTS   AGE
my-release-etcd-0                               1/1     Running   0          97s
my-release-milvus-standalone-6649fff666-5kgf9   1/1     Running   0          97s
my-release-minio-5f9c4b459b-kdtf9               1/1     Running   0          97s

$ kubectl port-forward service/my-release-milvus 27017:19530

$ docker run -p 8000:3000 -e MILVUS_URL=host.docker.internal:27017 zilliz/attu:latest

```