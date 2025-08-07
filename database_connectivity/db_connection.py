import mysql.connector

def create_connection():
    connect= mysql.connector.connect(
        host='localhost',
        user='root',
        password='Sai@2003',
        databae='sample'
    )
    return connect