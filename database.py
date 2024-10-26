import psycopg2

conexao = psycopg2.connect(
database = 'postgres',
host = '',
user = 'postgres',
password = '',
port = '5432')

print(conexao.info)
print(conexao.status)

cursor = conexao.cursor()
cursor.execute('select * from teste')
print(cursor.fetchall())
