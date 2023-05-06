from telegrambot import telegramBot
from mongodbconnect import databaseConnect
from credentials import update_URL, poll_URL,db_quiz,db_ids, db_database,client_url
from datetime import datetime

# current dateTime

if __name__ =="__main__":
    now = datetime.now()
    date_time_str = str(now.strftime("%d-%m-%Y"))
    date_time_str = "27-04-2023"
    deepQuiz = databaseConnect(db_database, client_url)
    deepQuiz.collection_connect(db_quiz)
    data = deepQuiz.fetch_data(date_time_str)
    quiz_question =  {'question':data['question'],
                      'options':[data['option1'],data['option2'],data['option3'],data['option4']],
                      'correctOption':data['correct_answer'],'explaination':data['explaination']}
    print(quiz_question)
    # groupid_db = databaseConnect(db_database, client_url)
    deepQuiz.collection_connect(db_ids)
    data = deepQuiz.fetch_data()
    group_ids = data['all_ids']
    print("group_ids:",group_ids)
    deepAIBot = telegramBot(update_URL,poll_URL)
    update_ids = deepAIBot.getChatIds()
    print("Update Ids:",update_ids)




    # if quiz_question:
    #     deepAIBot.sendPoll(group_ids,quiz_question)





#                         'correctOption':data['correct_answer'],'explaination':data['explaination']}
#         return ""
    # quiz = fetch_data(date_time_str,db_quiz, db_database)

    # id_data = fetch_ids("all ids",db_ids,db_database)
    # # print(ids)
    # allGroups = getChatIds(update_URL)


# if quiz !="":
#     sendPoll(poll_URL,['-853327273','-911283524'],quiz)