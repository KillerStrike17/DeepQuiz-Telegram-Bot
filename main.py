from telegrambot import getChatIds,sendPoll
from mongodbconnect import fetch_data,fetch_ids
from credentials import update_URL, poll_URL,db_quiz,db_ids, db_database
from datetime import datetime

# current dateTime
now = datetime.now()
date_time_str = str(now.strftime("%d-%m-%Y"))

quiz = fetch_data(date_time_str,db_quiz, db_database)

# id_data = fetch_ids("all ids",db_ids,db_database)
# print(ids)
# allGroups = getChatIds(update_URL)


if quiz !="":
    sendPoll(poll_URL,['-853327273','-911283524'],quiz)