from dotenv import find_dotenv, load_dotenv
from kafka import KafkaProducer
import json
import os

class Producer:

    def __init__(self):
        load_dotenv(find_dotenv())
        self.Host = os.getenv('KAFKA_HOST')
        self.Port = os.getenv('KAFKA_PORT')
        self.URI = os.getenv('KAFKA_CONNECT_STRING')

    def publish_message(self, topic, message):
        producer = self.get_producer_config()
        producer.send(topic=topic, value=message)
        producer.flush()

    def publish_message_with_key(self, topic, key, message):
        producer = self.get_producer_config()
        producer.send(topic, key=key, value=message)

    def get_producer_config(self):
        producer = KafkaProducer(bootstrap_servers=[self.URI],
                                 value_serializer=lambda x:
                                  json.dumps(x).encode('utf-8'))
        return producer

