from os import getenv

from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient


class Database:

    def __init__(self, collection_name='monsters'):
        """
        Initializing statement, initiates connection with MongoDB and 
        sets collection name
        """
        load_dotenv()
        db_url = getenv('DB_URL')
        db_name = getenv('DB_NAME')

        self.database = MongoClient(db_url, tlsCAFile=where())[db_name]
        self.collection = self.database[collection_name]

    def seed(self, amount):
        """
        Inserts the specified number of random monsters into the collection
        """
        monsters = [Monster().to_dict() for _ in range(amount)]
        return self.collection.insert_many(monsters)

    def reset(self):
        """
        Deletes all documents from the collection
        """
        return self.collection.delete_many({})

    def count(self) -> int:
        """
        Returns the number of documents in the collection
        """
        return self.collection.count_documents({})

    def dataframe(self) -> DataFrame:
        """
        Returns a DataFrame containing all documents in the collection
        """
        documents = self.collection.find(())
        df = DataFrame(documents)
        df = df.drop('_id', axis=1)
        return df

    def html_table(self) -> str:
        """
        Returns an HTML table representation of the DataFrame, 
        or None if the collection is empty
        """
        if self.count() == 0:
            return "None"
        return self.dataframe().to_html()
