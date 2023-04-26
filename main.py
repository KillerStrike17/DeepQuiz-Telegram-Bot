from telegrambot import getChatIds,sendPoll
from mysqlconnect import create_connection
from credentials import update_URL, poll_URL,db_host, db_user, db_password, db_name
from datetime import datetime

# current dateTime
now = datetime.now()
date_time_str = now.strftime("%Y-%m-%d")

cnx = create_connection(db_host, db_user, db_password, db_name)


allGroups = getChatIds(update_URL)
sendPoll(poll_URL,allGroups)