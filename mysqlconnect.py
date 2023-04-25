import mysql.connector

# replace the values below with your own credentials
db_host = 'shubhamagnihotri.mysql.pythonanywhere-services.com'
db_user = 'shubhamagnihotri'
db_password = 'Ki!!erStr1ke'
db_name = 'telegramquiz'

# connect to the database
cnx = mysql.connector.connect(
  host=db_host,
  user=db_user,
  password=db_password,
  database=db_name
)

# execute a query
cursor = cnx.cursor()
query = 'SELECT * FROM quiz'
cursor.execute(query)

# fetch the results and print them
results = cursor.fetchall()
for row in results:
  print(row)

# CREATE operation
# insert a new row into the quiz table
insert_query = ("INSERT INTO quiz "
                "(date, question, answers, correct_answer, explanation) "
                "VALUES (%s, %s, %s, %s, %s)")
data = ('2023-04-25', 'What is the capital of France?', '["Paris", "Rome", "Madrid", "Berlin"]', 0, 'Paris is the capital of France')
cursor.execute(insert_query, data)
cnx.commit()

# READ operation
# fetch all rows from the quiz table
select_query = "SELECT * FROM quiz"
cursor.execute(select_query)
rows = cursor.fetchall()
for row in rows:
  print(row)

# UPDATE operation
# update the correct answer for a specific question
update_query = ("UPDATE quiz "
                "SET correct_answer = %s "
                "WHERE question = %s")
data = (0, 'What is the capital of France?')
cursor.execute(update_query, data)
cnx.commit()

# DELETE operation
# delete a row from the quiz table
delete_query = ("DELETE FROM quiz "
                "WHERE question = %s")
data = ('What is the capital of France?',)
cursor.execute(delete_query, data)
cnx.commit()

# close the cursor and connection objects
cursor.close()
cnx.close()

# # close the connection
# cursor.close()
# cnx.close()
