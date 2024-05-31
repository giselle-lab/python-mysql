import mysql.connector

# Conectando ao banco de dados
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='meu_banco_de_dados'
)

cursor = conn.cursor()

# Consultando dados
cursor.execute('SELECT * FROM usuarios')

# Recuperando e imprimindo os dados
for row in cursor.fetchall():
    print(row)

# Fechando a conexão
conn.close()
