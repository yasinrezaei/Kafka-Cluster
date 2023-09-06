# Apache Kafka
Open source distributed event streaming platform

- high perfomrmance data pipelines
 
- Streaming analytics

- Data integration

- Mission Critical applications

---

- High Throughput

- Low Latency

- Fault Tolerant

- Durability

- Scalability


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


---

Each consumer -> one broker 

---

### 3 partitions 

Topic A:

- Part1 

- Part2

- Part3


### Kafka cluster(Rep-Fac = 2,L = leader , F = follower) 

BROKER 1 : (L)Part 3 - (F)Part 1


BROKER 2 : (L)Part 1 - (F)Part 2


BROKER 3 : (L)Part 2 - (F)Part 3


