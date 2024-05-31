import mysql.connector

# Conectando ao banco de dados
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='meu_banco_de_dados'
)

cursor = conn.cursor()

# Atualizando dados
cursor.execute('''
    UPDATE usuarios SET idade = %s WHERE nome = %s
''', (26, 'Alice'))

# Salvando as alterações
conn.commit()
conn.close()
