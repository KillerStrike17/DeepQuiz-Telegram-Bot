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
import pymongo
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
db = client.get_database('NewDatabase')
col = db.get_collection('student')  
docs = [{'name': 'David', 'age': 20},
        {'name': 'Alice', 'age': 25},
        {'name': 'Tyler', 'age': 23}]
result = col.insert_many(docs)
print(result.inserted_ids)