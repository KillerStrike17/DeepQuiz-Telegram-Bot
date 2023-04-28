import pymongo, json
import pandas as pd
from credentials import *

def upload_data(db_collection,db_database):
        client = pymongo.MongoClient('mongodb+srv://shubhamagnihotri:test@telegrambot.fdd25em.mongodb.net/test')
        db = client.get_database(db_database)
        col = db.get_collection(db_collection)
        df = pd.read_csv('questions.csv')
        data = json.loads(df.to_json(orient = 'records'))
        result = col.insert_many(data)
        
        
# upload_data(db_quiz,db_database)

def fetch_data(query_string,db_collection,db_database):
        client = pymongo.MongoClient('mongodb+srv://shubhamagnihotri:test@telegrambot.fdd25em.mongodb.net/test')
        db = client.get_database(db_database)
        col = db.get_collection(db_collection)
        data = col.find_one({"date":query_string})
        if data:
                return {'question':data['question'],'options':[data['option1'],data['option2'],data['option3'],data['option4']],
                        'correctOption':data['correct_answer'],'explaination':data['explaination']}
        return ""

# print(fetch_data('30-04-2023',db_collection,db_database))


def fetch_ids(query_string,db_collection,db_database):
        client = pymongo.MongoClient('mongodb+srv://shubhamagnihotri:test@telegrambot.fdd25em.mongodb.net/test')
        db = client.get_database(db_database)
        col = db.get_collection(db_collection)
        data = col.find_one({"value":query_string})
        # print(data['data'])

        # print(type(data['data']))
        return data

        # if data:
        #         return {'question':data['question'],'options':[data['option1'],data['option2'],data['option3'],data['option4']],
        #                 'correctOption':data['correct_answer'],'explaination':data['explaination']}
        # return ""