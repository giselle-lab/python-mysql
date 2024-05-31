import mysql.connector

# Conectando ao servidor MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password=''
)

# Criando um cursor para interagir com o banco de dados
cursor = conn.cursor()

# Criando um banco de dados
cursor.execute('CREATE DATABASE IF NOT EXISTS meu_banco_de_dados')

# Selecionando o banco de dados
cursor.execute('USE meu_banco_de_dados')

# Criando uma tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        idade INT NOT NULL
    )
''')

# Fechando a conexão
conn.close()
