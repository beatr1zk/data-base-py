from models.cardapio.itemcardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, sabor):
        super().__init__(nome, preco)
        self.sabor = sabor
        
    def __str__(self):
        return self._nome 