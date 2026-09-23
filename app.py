from banco.db import tabela_restaurante, tabela_avaliacoes, criar_restaurante,  criar_avaliacao, listar_restaurantes, listar_avaliacoes

tabela_restaurante()
tabela_avaliacoes() #Cade esse caraio que não existia

# criar_restaurante("Mada", "Italiana")
# criar_restaurante("Coconono", "Tropical")

# criar_avaliacao(1, "Heron", 4.8)

print("\nRestaurantes:")
listar_restaurantes()

print("\nAvaliações:")
listar_avaliacoes()