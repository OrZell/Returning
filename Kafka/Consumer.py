from dotenv import find_dotenv, load_dotenv
from kafka import KafkaConsumer
import json
import os

class Consumer:

    def __init__(self):
        load_dotenv(find_dotenv())
        self.Host = os.getenv('KAFKA_HOST')
        self.Port = os.getenv('KAFKA_PORT')
        self.URI = os.getenv('KAFKA_CONNECT_STRING')

    def get_consumer_events(self, topic):
        consumer = KafkaConsumer(*topic,
                                 group_id='my-group',
                                 value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                                 bootstrap_servers=[self.URI])

        # consumer_timeout_ms = 10000 optional

        return consumer