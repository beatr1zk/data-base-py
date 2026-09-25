from models.avaliacoes import Avaliacoes
from models.cardapio.itemcardapio import ItemCardapio
class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria, localizacao, quantidade_funcionarios):
        self.nome = nome
        self.categoria = categoria
        self.localizacao = localizacao
        self.quantidade_funcionarios = quantidade_funcionarios
        self._status = False
        self._avaliacoes = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"Nome: {self.nome} \n|Rua: {self.localizacao} \n|Tipo de Comida: {self.categoria} \n|Quantidade de Funcionários: {str(self.quantidade_funcionarios)} \n|Status: {self.ativo}"
    @classmethod
    def listar_restaurante(cls):
            for restaurante in cls.restaurantes:
                print(f"Nome: {restaurante.nome} \n|Rua: {restaurante.localizacao} \n|Tipo de Comida: {restaurante.categoria} \n|Quantidade de Funcionários: {str(restaurante.quantidade_funcionarios)} \n|Avaliações: {restaurante.media_avaliacoes}|Status: {restaurante.ativo}")
    @property
    def ativo(self):
        return 'Ativo' if self._status else 'Inativo'
    @property
    def media_avaliacoes(self):
        if not self._avaliacoes:
            return 0
        notas_somadas = sum(avaliacao._nota for avaliacao in self._avaliacoes)
        quantidade_avaliacoes = len(self._avaliacoes)
        media = round(notas_somadas/quantidade_avaliacoes,1)
        return media

    @property
    def exibir_cardapio(self):
        print(f"Cardápio do Restaurante: {self.nome}")
        for i,item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem_prato = f"{i}. Nome: {item._nome} \n| Preço: {item._preco} \n| Descrição: {item.descricao}"
                print(mensagem_prato)
            elif hasattr(item, "sabor"):
                mensagem_sobremesa = f"{i}. Nome: {item._nome} \n| Preço: {item._preco} \n| Sabor: {item.sabor}"
                print(mensagem_sobremesa)
            else:
                mensagem_bebida = f"{i}. Nome: {item._nome} \n| Preço: {item._preco} \n| Tamanho: {item.tamanho}"
                print(mensagem_bebida)




    def alterar_estado(self):
        self._status = not self._status

    def receber_avaliacoes(self, cliente, nota):
        avaliacao = Avaliacoes(cliente, nota)
        self._avaliacoes.append(avaliacao)

    def adicionar_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
    