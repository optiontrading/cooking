import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# uri = "mongodb+srv://gauravchopracg:07aug1998@cluster0.1tjlccb.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient()

database = 'cooking'
collection = 'recipes'

db = client[database]
collection_batches = db[collection]

batch = {}
batch["Recipe Name"] = 'PIÑA COLADA SMOOTHIE'
batch["Ingredients"] = ['1 cup pineapple chunks','1 cup coconut milk','1⁄2 medium banana','1⁄4 cup ice cubes','2 dates, seedless','1⁄8 teaspoon vanilla bean powder (optional)']
batch["Diet Type"] = 'Satvic'
batch["Meal Type"] = 'Breakfast'
print(batch)

collection_batches.insert_one(batch)
collection_batches.create_index([("cooking", pymongo.ASCENDING)])

batch = {}
batch["Recipe Name"] = 'BANANA DATE SHAKE'
batch["Ingredients"] = ['11⁄2 cups coconut milk','3 bananas','6 dates, seedless', '4 ice cubes', '1⁄2 teaspoon cinnamon powder']
batch["Diet Type"] = 'Satvic'
batch["Meal Type"] = 'Breakfast'
print(batch)

collection_batches.insert_one(batch)
collection_batches.create_index([("cooking", pymongo.ASCENDING)])

batch = {}
batch["Recipe Name"] = 'TROPICAL SMOOTHIE'
batch["Ingredients"] = ['1 cup coconut water','1 cup chopped spinach','1 cup chopped apple', '1 cup mango chunks', '1⁄2 teaspoon lemon juice']
batch["Diet Type"] = 'Satvic'
batch["Meal Type"] = 'Breakfast'
print(batch)

collection_batches.insert_one(batch)
collection_batches.create_index([("cooking", pymongo.ASCENDING)])

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
