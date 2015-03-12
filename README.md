# kafka-python-template
Example kafka-based app, for deployment to CoreOS.

# Usage
```
docker build -t mfaulk/kafka-python-template .
docker run 
```

# CoreOS
`kafka-app.service` provides an example Fleet service file. This assumes that the IP address of a Kafka broker has been written to etcd under `/service/kafka`