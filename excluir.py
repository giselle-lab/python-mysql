import mysql.connector

# Conectando ao banco de dados
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='meu_banco_de_dados'
)

cursor = conn.cursor()

# Excluindo dados
cursor.execute('''
    DELETE FROM usuarios WHERE nome = %s
''', ('Bob',))
# exluir alice 
cursor.execute('''
    DELETE FROM usuarios WHERE nome = %s
''', ('Alice',))


# Salvando as alterações
conn.commit()
conn.close()
