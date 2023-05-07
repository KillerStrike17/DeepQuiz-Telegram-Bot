import pymongo, json
import pandas as pd
from credentials import *

class databaseConnect:
        def __init__(self,  db_database, client_url) -> None:
                self.db_database = db_database
                self.client_url = client_url
                self.db = self.db_connect()
        
        def collection_connect(self, db_collection):        
                self.col = self.db.get_collection(db_collection)
        
        def db_connect(self):
                self.client = pymongo.MongoClient(self.client_url)
                db = self.client.get_database(self.db_database)
                return db
                
        
        def insert_data(self,data):
                json_data = json.loads(data.to_json(orient = 'records'))
                result = self.col.insert_many(json_data)
        
        def update_data(self,myquery,newvalues):
                self.col.update_one(myquery, newvalues)


        def fetch_data(self, query_string=""):
                if query_string:
                        data = self.col.find_one({"date":query_string})
                else:
                        data = self.col.find_one()
                if data:
                        return data
                return  ""
        


                
        

        # def upload_data(self, data):

# def upload_data(db_collection,db_database):
#         client = pymongo.MongoClient('mongodb+srv://shubhamagnihotri:test@telegrambot.fdd25em.mongodb.net/test')
#         db = client.get_database(db_database)
#         col = db.get_collection(db_collection)
#         df = pd.read_csv('questions.csv')
#         data = json.loads(df.to_json(orient = 'records'))
#         result = col.insert_many(data)

# def upload_ids(db_collection,db_database, group_ids):
#         client = pymongo.MongoClient('mongodb+srv://shubhamagnihotri:test@telegrambot.fdd25em.mongodb.net/test')
#         db = client.get_database(db_database)
#         col = db.get_collection(db_collection)
#         # df = pd.read_csv('questions.csv')
#         data = json.loads(group_ids.to_json(orient = 'records'))
#         result = col.insert_many(data)
        
# # upload_data(db_quiz,db_database)

# def fetch_data(query_string,db_collection,db_database):
#         client = pymongo.MongoClient('mongodb+srv://shubhamagnihotri:test@telegrambot.fdd25em.mongodb.net/test')
#         db = client.get_database(db_database)
#         col = db.get_collection(db_collection)
#         data = col.find_one({"date":query_string})
#         if data:
#                 return {'question':data['question'],'options':[data['option1'],data['option2'],data['option3'],data['option4']],
#                         'correctOption':data['correct_answer'],'explaination':data['explaination']}
#         return ""

# # print(fetch_data('30-04-2023',db_collection,db_database))


# def fetch_ids(query_string,db_collection,db_database):
#         client = pymongo.MongoClient('mongodb+srv://shubhamagnihotri:test@telegrambot.fdd25em.mongodb.net/test')
#         db = client.get_database(db_database)
#         col = db.get_collection(db_collection)
#         data = col.find_one({"value":query_string})
#         # print(data['data'])

#         # print(type(data['data']))
#         return data

#         # if data:
#         #         return {'question':data['question'],'options':[data['option1'],data['option2'],data['option3'],data['option4']],
#         #                 'correctOption':data['correct_answer'],'explaination':data['explaination']}
#         # return ""