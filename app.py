from models.restaurante import Restaurante
from repositories.rep_cardapio import criar_item_cardapio, tabela_item_cardapio
from repositories.rep_restaurante import criar_restaurante, tabela_restaurante, listar_restaurantes
from repositories.rep_avaliacao import criar_avaliacao, tabela_avaliacoes, listar_avaliacoes

tabela_restaurante()
tabela_avaliacoes() 
tabela_item_cardapio()

def main():
    tabela_item_cardapio()
    criar_item_cardapio()

criar_restaurante(Restaurante("Mada", "Italiana"))
criar_restaurante(Restaurante("Coconono", "Tropical"))

criar_avaliacao(1, "Heron", 4.8)

print("\nRestaurantes:")
listar_restaurantes()

print("\nAvaliações:")
listar_avaliacoes()