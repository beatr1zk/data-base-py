import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Bia@2008ksql",
        database = "ifood2"
    )
    return conexao

def tabela_restaurante():
    conexao = conectar()
    cursor = conexao.cursor()
    criar_tabela_restaurante = """
        CREATE TABLE IF NOT EXISTS restaurantes(
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            categoria VARCHAR(45) NOT NULL,
            ativo BOOLEAN DEFAULT FALSE NOT NULL
            )
    """
    cursor.execute(criar_tabela_restaurante)
    conexao.commit()
    conexao.close()

def tabela_avaliacao():
    conexao = conectar()
    cursor = conexao.cursor()
    criar_tabela_avaliacao = """
        CREATE TABLE IF NOT EXISTS avaliacoes(
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome_usuario VARCHAR(100) NOT NULL,
            nota FLOAT NOT NULL,
            id_restaurante INT NOT NULL,
            FOREIGN KEY (id_restaurante) REFERENCES restaurantes(id)
            )
    """
    cursor.execute(criar_tabela_avaliacao)
    conexao.commit()
    conexao.close()

def criar_restaurante(nome, categoria):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO restaurantes(nome, categoria)
        VALUES (%s, %s)
    """, (nome, categoria))
    conexao.commit()
    conexao.close()

def listar_restaurantes():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT * FROM restaurantes
    """)
    restaurantes = cursor.fetchall()
    for restaurante in restaurantes:
        print(restaurante)
    conexao.commit()
    conexao.close()