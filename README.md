# Apache Kafka
Open source distributed event streaming platform

---
### Concepts

- record/message 

- broker 

- producer

- consumer

- consumer-group

- topic

- partition

- zookeeper

### Commands

```bash

- docker exec -it <container_id> /bin/bash

- kafka-topics --create --topic <topic_name> c --bootstrap-server broker:29092 --partitions 1 --replication-factor 1

- kafka-console-producer --broker-list broker:29092 --topic <topic_name>

- kafka-console-consumer --bootstrap-server broker:29092 --topic <topic_name> --from-beginning

- kafka-topics --bootstrap-server  broker:9092 --describe --topic <topic_name>

```





