from banco.db import conectar
from models.restaurante import Restaurante

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

def criar_restaurante(restaurante):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO restaurantes(nome, categoria, localizacao, tipo_comida)
        VALUES (%s, %s, %s, %s)
    """, (restaurante.nome, restaurante.categoria, restaurante.localizacao, restaurante.tipo_comida))
    conexao.commit()
    conexao.close()


def listar_restaurantes():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT * FROM restaurantes
    """)
    restaurantes = cursor.fetchall()
    conexao.commit()
    conexao.close()
    return [Restaurante(nome,categoria) for nome,categoria in restaurantes]