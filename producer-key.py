from time import sleep
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda x: dumps(x).encode('utf-8'),
                        key_serializer=str.encode )

for e in range(1000):
    data = {'users' : e}
    producer.send('organizations_topic', value=data, key= str(e))
    print(f"Sending data : {data}")
    sleep(1)
