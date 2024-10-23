import psycopg2

conexao = psycopg2.connect(
database = 'postgres',
host = 'amply-winged-bat.data-1.use1.tembo.io',
user = 'postgres',
password = 'ycxf7w5ecVuixXNx',
port = '5432')

print(conexao.info)
print(conexao.status)

cursor = conexao.cursor()
cursor.execute('select * from teste')
print(cursor.fetchall())
