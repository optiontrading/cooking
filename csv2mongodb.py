import pandas as pd
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


df = pd.read_csv('data/ingredients - Sheet1.csv')

# Create a new client and connect to the server
client = MongoClient()

database = 'ingredients'
collection = 'ingredients'

db = client[database]
db.ingredients.insert_many(df.to_dict('records'))
