from dotenv import find_dotenv, load_dotenv
from pymongo import MongoClient
import os

class MongoDB_DAL:

    def __init__(self):
        load_dotenv(find_dotenv())
        self.HOST = os.getenv('MONGODB_HOST')
        self.PORT = os.getenv('MONGODB_PORT')
        self.ConnectionString = os.getenv('MONGODB_CONNECTION_STRING')

        self.DB = os.getenv('MONGODB_DB')
        self.Collection = os.getenv('MONGODB_COLLECTION')

        self.connection = None

    def open_connection(self):
        if self.connection is None:
            self.connection = MongoClient(self.ConnectionString)
        return self.connection

    def close_connection(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    def insert_one(self, doc):
        connection = self.open_connection()

        connection[self.DB][self.Collection].insert_one(doc)

        self.close_connection()

    def update_one(self, doc):
        connection = self.open_connection()

        connection[self.DB][self.Collection].update_one(doc)

        self.close_connection()

    def read_one(self, doc):
        connection = self.open_connection()

        connection[self.DB][self.Collection].find_one(doc)

        self.close_connection()

    def delete_one(self, doc):
        connection = self.open_connection()

        connection[self.DB][self.Collection].delete_one(doc)

        self.close_connection()