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

def tabela_avaliacoes():
    conexao = conectar()
    cursor = conexao.cursor()
    criar_tabela_avaliacao = """
        CREATE TABLE IF NOT EXISTS avaliacoes(
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_restaurante INT NOT NULL,
            nome_usuario VARCHAR(100) NOT NULL,
            nota FLOAT(2,1) NOT NULL,
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

def criar_avaliacao(id_restaurante, nome_usuario, nota):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO avaliacoes(id_restaurante, nome_usuario, nota)
        VALUES (%s, %s, %s)
    """, (id_restaurante, nome_usuario, nota))
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

def listar_avaliacoes(): 
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT restaurantes.nome , avaliacoes.nome_usuario, avaliacoes.nota FROM avaliacoes
        JOIN restaurantes ON avaliacoes.id_restaurante = restaurantes.id
    """)
    avaliacoes = cursor.fetchall()
    for avaliacao in avaliacoes:
        print(avaliacao)
    conexao.commit()
    conexao.close()

def tabela_item_cardapio():
    conexao = conectar()
    cursor = conexao.cursor()
    criar_tabela_item_cardapio = """
        CREATE TABLE IF NOT EXISTS item_cardapio(
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_restaurante INT NOT NULL,
            nome_item VARCHAR(100) NOT NULL,
            preco FLOAT(6,2) NOT NULL,
            FOREIGN KEY (id_restaurante) REFERENCES restaurantes(id)
            )
    """
    cursor.execute(criar_tabela_item_cardapio)
    conexao.commit()
    conexao.close()

def criar_avaliacao(id_restaurante, nome_item, preco):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO item_cardapio(id_restaurante, nome_item, preco)
        VALUES (%s, %s, %s)
    """, (id_restaurante, nome_item, preco))
    conexao.commit()
    conexao.close()