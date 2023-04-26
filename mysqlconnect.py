import mysql

# Create a connection to the database
def create_connection(db_host,db_user,db_password,db_name):
    cnx = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name,
    )
    return cnx

# Create a new record
def create_record(db_host,db_user,db_password,db_name,question, answers, correct_answer, explanation):
    try:
        cnx = create_connection(db_host,db_user,db_password,db_name)
        cursor = cnx.cursor()
        add_record = "INSERT INTO questions (question, answers, correct_answer, explanation) VALUES (%s, %s, %s, %s)"
        data_record = (question, answers, correct_answer, explanation)
        cursor.execute(add_record, data_record)
        cnx.commit()
        print("Record added successfully")
    except mysql.connector.Error as error:
        print(f"Failed to add record to database: {error}")
    finally:
        cursor.close()
        cnx.close()

# Read all records
def read_all_records(db_host,db_user,db_password,db_name):
    try:
        cnx = create_connection(db_host,db_user,db_password,db_name)
        cursor = cnx.cursor()
        select_all = "SELECT * FROM questions"
        cursor.execute(select_all)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except mysql.connector.Error as error:
        print(f"Failed to read records from database: {error}")
    finally:
        cursor.close()
        cnx.close()

# Read a single record by ID
def read_record_by_id(db_host,db_user,db_password,db_name,id):
    try:
        cnx = create_connection(db_host,db_user,db_password,db_name)
        cursor = cnx.cursor()
        select_record = "SELECT * FROM questions WHERE id = %s"
        cursor.execute(select_record, (id,))
        row = cursor.fetchone()
        print(row)
    except mysql.connector.Error as error:
        print(f"Failed to read record from database: {error}")
    finally:
        cursor.close()
        cnx.close()

# Update a record by ID
def update_record_by_id(db_host,db_user,db_password,db_name,id, question, answers, correct_answer, explanation):
    try:
        cnx = create_connection(db_host,db_user,db_password,db_name)
        cursor = cnx.cursor()
        update_record = "UPDATE questions SET question = %s, answers = %s, correct_answer = %s, explanation = %s WHERE id = %s"
        data_record = (question, answers, correct_answer, explanation, id)
        cursor.execute(update_record, data_record)
        cnx.commit()
        print("Record updated successfully")
    except mysql.connector.Error as error:
        print(f"Failed to update record in database: {error}")
    finally:
        cursor.close()
        cnx.close()

# Delete a record by ID
def delete_record_by_id(db_host,db_user,db_password,db_name,id):
    try:
        cnx = create_connection(db_host,db_user,db_password,db_name)
        cursor = cnx.cursor()
        delete_record = "DELETE FROM questions WHERE id = %s"
        cursor.execute(delete_record, (id,))
        cnx.commit()
        print("Record deleted successfully")
    except mysql.connector.Error as error:
        print(f"Failed to delete record from database: {error}")
    finally:
        cursor.close()
        cnx.close()
