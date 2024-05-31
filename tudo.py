# criar
# inserir
# consultar
# atualizar
# excluir
import mysql.connector

def conectar():
    return mysql.connector.connect(
        host='localhost',
        user='seu_usuario',
        password='sua_senha',
        database='meu_banco_de_dados'
    )

def criar_tabela(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            idade INT NOT NULL
        )
    ''')
    conn.commit()

def inserir_usuario(conn, nome, idade):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO usuarios (nome, idade) VALUES (%s, %s)
    ''', (nome, idade))
    conn.commit()

def consultar_usuarios(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios')
    return cursor.fetchall()

def atualizar_usuario(conn, idade, nome):
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE usuarios SET idade = %s WHERE nome = %s
    ''', (idade, nome))
    conn.commit()

def excluir_usuario(conn, nome):
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM usuarios WHERE nome = %s
    ''', (nome,))
    conn.commit()

if __name__ == '__main__':
    conn = conectar()
    criar_tabela(conn)
    
    inserir_usuario(conn, 'Alice', 25)
    inserir_usuario(conn, 'Bob', 30)
    
    usuarios = consultar_usuarios(conn)
    print('Usuários:', usuarios)
    
    atualizar_usuario(conn, 26, 'Alice')
    
    excluir_usuario(conn, 'Bob')
    
    usuarios = consultar_usuarios(conn)
    print('Usuários após atualização e exclusão:', usuarios)
    
    conn.close()
