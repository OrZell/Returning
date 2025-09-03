from elasticsearch import Elasticsearch, helpers
from dotenv import find_dotenv, load_dotenv
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

    def insert_one(self, doc):
        connection = self.open_connection()

        connection.index(index=self.IndexName, body=doc)

        self.close_connection()

    def search_word_in_text(self, word):
        connection = self.open_connection()

        query = {
            "query": {
                "match": {
                    "text": word
                }
            }
        }
        result = connection.search(index=self.IndexName, body=query)

        self.close_connection()
        return result

    def delete_list_of_docs(self, docs):
        connection = self.open_connection()

        new_docs = []
        for doc in docs:
            new_docs.append({
                '_op_type': 'delete',
                '_index': self.IndexName,
                '_id': doc['_id']
            })

        helpers.bulk(connection, new_docs)