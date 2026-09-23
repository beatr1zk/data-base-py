from banco.db import conectar
from models.cardapio.itemcardapio import ItemCardapio
from models.cardapio.prato import Prato
from models.cardapio.bebida import Bebida
from models.cardapio.sobremesa import Sobremesa


def tabela_item_cardapio():
    conexao = conectar()
    cursor = conexao.cursor()
    criar_tabela_item_cardapio = """
        CREATE TABLE IF NOT EXISTS item_cardapio(
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_restaurante INT NOT NULL,
            nome_item VARCHAR(100) NOT NULL,
            preco FLOAT(6,2) NOT NULL,
            tipo_item VARCHAR(45) NOT NULL,
            descricao TEXT,
            tamanho VARCHAR(45),
            sabor VARCHAR(45),
            FOREIGN KEY (id_restaurante) REFERENCES restaurantes(id)
            )
    """
    cursor.execute(criar_tabela_item_cardapio)
    conexao.commit()
    conexao.close()


def criar_item_cardapio(id_restaurante, item):
    if isinstance(item, Prato):
        tipo_item = 'prato'
        descricao = item.descricao
        tamanho = None
        sabor = None
    elif isinstance(item, Bebida):
        tipo_item = 'bebida'
        descricao = None
        tamanho = item.tamanho
        sabor = None
    else:
        tipo_item = 'sobremesa'
        descricao = None
        tamanho = None
        sabor = item.sabor


    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO item_cardapio(id_restaurante, nome_item, preco, tipo_item, descricao, tamanho, sabor)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (id_restaurante, item._nome, item._preco, tipo_item, descricao, tamanho, sabor))
    conexao.commit()
    conexao.close()