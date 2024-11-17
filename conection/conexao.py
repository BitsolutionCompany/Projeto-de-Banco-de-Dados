# import mysql.connector

# connection = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = ""
# )

# print(connection)
import mysql.connector
from mysql.connector import Error

def create_connection(host, user, password, database=None):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
        database=database
        )
        if connection.is_connected():
            print("Successfully connected to the database")
    except Error as e:
        print(f"Error: {e}")
    return connection