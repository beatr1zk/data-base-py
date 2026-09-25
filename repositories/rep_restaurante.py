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
            localizacao VARCHAR(150) NOT NULL,
            quantidade_funcionarios INT NOT NULL,
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
        INSERT INTO restaurantes(nome, categoria, localizacao, quantidade_funcionarios)
        VALUES (%s, %s, %s, %s)
    """, (restaurante.nome, restaurante.categoria, restaurante.localizacao, restaurante.quantidade_funcionarios))
    conexao.commit()
    conexao.close()

def listar_restaurantes():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT * FROM restaurantes
    """)
    resultado = cursor.fetchall()
    conexao.commit()
    conexao.close()
    restaurantes = []
    for id, nome, categoria, localizacao, quantidade_funcionarios, ativo in resultado:
        restaurante = Restaurante(nome, categoria, localizacao, quantidade_funcionarios)
        restaurante._ativo = bool(ativo)
        restaurante.id = id
        restaurantes.append(restaurante)
    return restaurantes

def buscar_por_id(id):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT id, nome, categoria, localizacao, quantidade_funcionarios, ativo FROM restaurantes
        WHERE id = %s
    """, (id,))
    resultado = cursor.fetchone()
    conexao.close()

    if resultado is None:
        return None
    id_banco, nome, categoria, localizacao, quantidade_funcionarios, ativo = resultado
    restaurante = Restaurante(nome, categoria, localizacao, quantidade_funcionarios)
    restaurante._ativo = bool(ativo)
    restaurante.id = id_banco
    return restaurante

def listar_completo(id):
    from repositories import avaliacao_repository, cardapio_repository

    restaurante = buscar_por_id(id)
    if restaurante is None:
        return None
    else:
        for avaliacao in avaliacao_repository.listar_por_restaurante(id):
            restaurante._avaliacoes.append(avaliacao)
        for item in cardapio_repository.listar_por_restaurante(id):
            restaurante._cardapio.append(item)
        return restaurante