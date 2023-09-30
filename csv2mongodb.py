import pandas as pd
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


df = pd.read_csv('data/coconut ingredients - Sheet1.csv')

# Create a new client and connect to the server
client = MongoClient()

database = 'ingredients'
collection = 'ingredients'

db = client[database]
db.ingredients.insert_many(df.to_dict('records'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)