from db_connection import create_connection

connection= create_connection()
mycursor= connection.cursor()
query= "CREATE TABLE IF NOT EXISTS table1 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)"
mycursor.execute(query)
connection.commit()
connection.close()