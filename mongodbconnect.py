# import pymongo,datetime

# client = pymongo.MongoClient("mongodb://localhost:27017/")
# print(client)

# db = client["DeepAIBot"]
# collection = db["quiz"]
# print(collection)

# # insertThese = [
# #     {"date":"123","question":"test2","answer":["1","2","3","4"],"correct_answer":0},
# #     {"date":"321","question":"test2","answer":["1","2","3","4"],"correct_answer":0}
# # ]

# # collection.insert_many(insertThese)
# # new_posts = [{"author": "Mike",
# #               "text": "Another post!",
# #               "tags": ["bulk", "insert"],
# #               "date": datetime.datetime(2009, 11, 12, 11, 14)},
# #              {"author": "Eliot",
# #               "title": "MongoDB is fun",
# #               "text": "and pretty easy too!",
# #               "date": datetime.datetime(2009, 11, 10, 10, 45)}]
# result = collection.insert_one({"date":"123","question":"test2","answer":["1","2","3","4"],"correct_answer":0})
# result.inserted_ids
# Insert documentd into the collection
# from collections.abc import MutableMapping

import pymongo, json
from credentials import db_collection,db_database
import pandas as pd

def upload_data():
        client = pymongo.MongoClient('localhost', 27017)
        db = client.get_database(db_database)
        col = db.get_collection(db_collection)
        df = pd.read_csv('questions.csv')
        data = json.loads(df.to_json(orient = 'records'))
        result = col.insert_many(data)
        
        
upload_data()