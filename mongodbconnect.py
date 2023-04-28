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
import pandas as pd
from credentials import *

def upload_data(db_collection,db_database):
        client = pymongo.MongoClient('localhost', 27017)
        db = client.get_database(db_database)
        col = db.get_collection(db_collection)
        df = pd.read_csv('questions.csv')
        data = json.loads(df.to_json(orient = 'records'))
        result = col.insert_many(data)
        
        
# upload_data(db_collection,db_database)

def fetch_data(query_string,db_collection,db_database):
        client = pymongo.MongoClient('localhost', 27017)
        db = client.get_database(db_database)
        col = db.get_collection(db_collection)
        data = col.find_one({"date":query_string})
        if data:
                return {'question':data['question'],'options':[data['option1'],data['option2'],data['option3'],data['option4']],
                        'correctOption':data['correct_answer'],'explaination':data['explaination']}
        return ""

# print(fetch_data('30-04-2023',db_collection,db_database))
