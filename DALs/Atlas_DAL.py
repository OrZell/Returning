from dotenv import find_dotenv, load_dotenv
from pymongo import MongoClient
import os

class Atlas_DAL:

    def __init__(self):
        load_dotenv(find_dotenv())
        self.User = os.getenv('ATLAS_USER')
        self.Password = os.getenv('ATLAS_PASSWORD')
        self.DB = os.getenv('ATLAS_DB')
        self.Collection = os.getenv('ATLAS_COLLECTION')
        self.ConnectString = os.getenv('ATLAS_CONNECT_STRING')

        self.connection = None

    def open_connection(self):
        if self.connection is None:
            self.connection = MongoClient(self.ConnectString)
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