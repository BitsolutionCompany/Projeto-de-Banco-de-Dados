from conection.conexao import create_connection

def create_database(database):
    conn = create_connection("localhost", "root", "")
    if conn is not None and conn.is_connected():
        mycursor = conn.cursor()
        mycursor.execute(f"CREATE DATABASE {database}")
        mycursor.close()
        conn.close()
        return f"Database {database} created"
    else:
        return "Not Connected"
    
def listDB():
    conn = create_connection("localhost", "root", "")
    if conn is not None and conn.is_connected():
        mycursor = conn.cursor()
        mycursor.execute("SHOW DATABASES")
        databases = mycursor.fetchall()
        mycursor.close()
        conn.close()
        return [db[0] for db in databases]  # Retorna uma lista com os nomes dos bancos de dados
    else:
        return "Not Connected"