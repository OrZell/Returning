from dotenv import find_dotenv, load_dotenv
from elasticsearch import Elasticsearch, helpers
import os

class Elastic:

    def __init__(self):
        load_dotenv(find_dotenv())
        self.Host = os.getenv('ELASTICSEARCH_HOTS')
        self.Port = os.getenv('ELASTICSEARCH_PORT')
        self.ConnectString = os.getenv('ELASTICSEARCH_CONNECTION_STRING')
        self.IndexName = os.getenv('ELASTICSEARCH_INDEX')

        self.connection = None

        self.Map = {
            'properties': {
                'text': {
                    'type': 'text'
                },
                'createdate': {
                    'type': 'datetime',
                    'format': 'yyyy-MM-dd HH:mm:ss'
                },
                'antisemitic': {
                    'type': 'integer'
                },
                'sentiment': {
                    'type': 'keyword'
                },
                'weapons_detected': {
                    'type': 'keyword'
                },
                'num_of_weapons': {
                    'type': 'integer'
                }
            }
        }



    def open_connection(self):
        if self.connection is None:
            self.connection = Elasticsearch(self.ConnectString)
        return self.connection

    def close_connection(self):
        if self.connection:
            self.connection.close()
            self.connection = None