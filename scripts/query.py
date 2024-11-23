from conection.conexao import create_connection
import mysql.connector

def create_database(database):
    conn = create_connection("localhost", "root", "")
    if conn is not None and conn.is_connected():
        mycursor = conn.cursor()
        try:
            mycursor.execute(f"CREATE DATABASE {database}")
            return f"Banco de Dados {database} Criado"
        except mysql.connector.Error as err:
            return f"Erro ao criar banco de dados: {err}"
        finally:
            mycursor.close()
            conn.close()
    else:
        return "Não Conectado"

def listDB():
    conn = create_connection("localhost", "root", "")
    if conn is not None and conn.is_connected():
        mycursor = conn.cursor()
        try:
            mycursor.execute("SHOW DATABASES")
            databases = mycursor.fetchall()
            return [db[0] for db in databases]
        except mysql.connector.Error as err:
            return f"Erro ao listar bancos de dados: {err}"
        finally:
            mycursor.close()
            conn.close()
    else:
        return "Não Conectado!"

def createTable(db, table, colunas):
    conn = create_connection("localhost", "root", "", db)
    if conn is not None and conn.is_connected():
        mycursor = conn.cursor()
        try:
            colunas_str = ", ".join(colunas)
            mycursor.execute(f"CREATE TABLE {table} ({colunas_str})engine=InnoDB")
            return f"Tabela {table} Criada"
        except mysql.connector.Error as err:
            return f"Erro ao criar tabela: {err}"
        finally:
            mycursor.close()
            conn.close()
    else:
        return "Não Conectado!"

def listTable(db):
    conn = create_connection("localhost", "root", "", db)
    if conn is not None and conn.is_connected():
        mycursor = conn.cursor()
        try:
            mycursor.execute("SHOW TABLES")
            tables = mycursor.fetchall()
            return [t[0] for t in tables]
        except mysql.connector.Error as err:
            return f"Erro ao listar tabelas: {err}"
        finally:
            mycursor.close()
            conn.close()
    else:
        return "Não Conectado!"

def getColumn(db, table):
    conn = create_connection("localhost", "root", "", db)
    if conn is not None and conn.is_connected():
        mycursor = conn.cursor()
        try:
            mycursor.execute(f"""SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = '{db}' AND TABLE_NAME = '{table}' AND EXTRA NOT LIKE '%auto_increment%'""")
            columns = mycursor.fetchall()
            return [c[0] for c in columns]
        except mysql.connector.Error as err:
            return f"Erro ao obter colunas: {err}"
        finally:
            mycursor.close()
            conn.close()
    else:
        return "Não Conectado!"

def insertDados(db, table, columns, dados):
    conn = create_connection("localhost", "root", "", db)
    if conn is not None and conn.is_connected():
        mycursor = conn.cursor()
        try:
            dados_str = ", ".join(f"'{str(dado).replace('\'', '\'\'')}'" if isinstance(dado, str) else str(dado) for dado in dados)
            col = ", ".join(columns)
            mycursor.execute(f"INSERT INTO {table} ({col}) VALUES ({dados_str})")
            conn.commit()
            return "Dados Inseridos"
        except mysql.connector.Error as err:
            return f"Erro ao inserir dados: {err}"
        finally:
            mycursor.close()
            conn.close()
    else:
        return "Não Conectado!"

def dropDB(db):
    conn = create_connection("localhost", "root", "")
    if conn is not None and conn.is_connected():
        mycursor = conn.cursor()
        try:
            mycursor.execute(f"DROP DATABASE {db}")
            conn.commit()
            return "Banco de Dados Excluído"
        except mysql.connector.Error as err:
            return f"Erro ao excluir Banco de Dados: {err}"
        finally:
            mycursor.close()
            conn.close()
