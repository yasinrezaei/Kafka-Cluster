import asyncio
from concurrent.futures import ThreadPoolExecutor
from kafka import KafkaConsumer

def kafka_consumer(consumer_id, topic_name):
    print(f"Connecting to consumer {consumer_id} ...")
    consumer = KafkaConsumer(
        topic_name,
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group'
    )
    for message in consumer:
        print(f"Consumer {consumer_id} - Partition: {message.partition} "
              f"Offset: {message.offset} Key: {message.key} Value: {message.value}")

async def main():
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as executor:
        await asyncio.gather(
            loop.run_in_executor(executor, kafka_consumer, "Consumer 1", "organizations_topic"),
            loop.run_in_executor(executor, kafka_consumer, "Consumer 2", "organizations_topic")
        )

if __name__ == "__main__":
    asyncio.run(main())
