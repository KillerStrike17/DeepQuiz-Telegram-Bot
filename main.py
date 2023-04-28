from telegrambot import getChatIds,sendPoll
from mysqlconnect import create_connection
from mongodbconnect import fetch_data
from credentials import update_URL, poll_URL,db_collection, db_database
from datetime import datetime

# current dateTime
now = datetime.now()
date_time_str = str(now.strftime("%d-%m-%Y"))

quiz = fetch_data(date_time_str,db_collection, db_database)
# print(quiz)
if quiz !="":
    allGroups = getChatIds(update_URL)
    sendPoll(poll_URL,allGroups,quiz)