from banco.db import conectar

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

def criar_item_cardapio(id_restaurante, nome_item, preco):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO item_cardapio(id_restaurante, nome_item, preco)
        VALUES (%s, %s, %s)
    """, (id_restaurante, nome_item, preco))
    conexao.commit()
    conexao.close()