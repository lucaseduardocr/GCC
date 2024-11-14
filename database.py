import psycopg2
from psycopg2 import OperationalError

class databaseManager():
    
    def create_connection(self):
        connection = None
        try:
            connection = psycopg2.connect(
                database = '',
                host = '',
                user = 'postgres',
                password = '',
                port = '5432')
            print("Conexão realizada com sucesso")
        except OperationalError as e:
            print(f"O erro '{e} ocorreu")
        return connection

    def list_tables(self):
        connection_database = self.create_connection()
        c = connection_database.cursor()
        lista = None
        try:
            tables = c.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'""")
            tables = c.fetchall()
            tables_names = [table[0] for table in tables]
            print(f"Tabelas encontradas:{tables_names}")
            return tables_names
        except Exception as e:
            print(f"Erro: {e}")
        finally:
            c.close()
            conection.close()
        return lista
        
    
    def table_users(self):
        connection_database = self.create_connection()
        c = connection_database.cursor()
        list = self.list_tables()
        list_table = []
        
        for table in list:
            list_table.append(table)

        if 'users' in list_table:
            print("Já existe a tabela 'users' no banco de dados")
        else:
            try:
                connection_database = self.create_connection()
                c = connection_database.cursor()
                create_table_users = c.execute("CREATE TABLE users (user_id SERIAL PRIMARY KEY, name VARCHAR(255), email VARCHAR(255) UNIQUE, password VARCHAR(255));")
                connection_database.commit()
                print("Tabela 'users' foi criada com sucesso!")
                print(f"{list_table}")
            finally:
                c.close()
            


        


database = databaseManager()
conection = database.create_connection()
create_tables = database.table_users()