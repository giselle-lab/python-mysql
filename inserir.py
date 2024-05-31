import mysql.connector

# Conectando ao banco de dados
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='meu_banco_de_dados'
)

cursor = conn.cursor()

# Inserindo dados na tabela
cursor.execute('''
    INSERT INTO usuarios (nome, idade) VALUES (%s, %s)
''', ('Alice', 25))

cursor.execute('''
    INSERT INTO usuarios (nome, idade) VALUES (%s, %s)
''', ('Bob', 30))

# Salvando as alterações
conn.commit()
conn.close()
