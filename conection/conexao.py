import mysql.connector
from mysql.connector import Error

def create_connection(host, user, password, database=None):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )
        if connection.is_connected():
            print("Conexão Realizada Com Sucesso!")
    except Error as e:
        print(f"Error: {e}")
    return connection