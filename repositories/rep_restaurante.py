from banco.db import conectar

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
