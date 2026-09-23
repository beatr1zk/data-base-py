from models.avaliacoes import Avaliacoes
from models.cardapio.itemcardapio import ItemCardapio

class Restaurante:
    restaurantes = []
    avaliacoes = []

    def __init__(self, nome_restaurante, localizacao, tipo_comida, qntd_funcionarios):
        self.nome_restaurante = nome_restaurante
        self.localizacao = localizacao
        self.tipo_comida = tipo_comida
        self.qntd_funcionarios = qntd_funcionarios
        self._status = False
        self._avaliacoes = []
        self._cardapio = []

        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"Nome: {self.nome_restaurante} \nRua: {self.localizacao} \nTipo de comida: {self.tipo_comida} \nQuantidade de funcionários: {self.qntd_funcionarios} \nStatus: {self.ativo}"


    @classmethod
    def listar_restaurantes(cls):
        for restaurante in cls.restaurantes:
            print(f"\nNome: {restaurante.nome_restaurante} \n| Rua: {restaurante.localizacao} \n| Tipo de Comida: {restaurante.tipo_comida} \n| Quantidade de Funcionários: {str(restaurante.qntd_funcionarios)} \n| Avaliações: {restaurante.media_avaliacoes} \n| Status: {restaurante.ativo} \n\n---------------------------------------------------")


    @property
    def ativo(self):
        return 'Ativo' if self._status else 'Inativo'

    @property
    def media_avaliacoes(self):
        if not self._avaliacoes:
            return 0
        notas_somadas = sum(avaliacao._nota for avaliacao in self._avaliacoes)
        quantidade_avaliacoes = len(self._avaliacoes)
        media = round(notas_somadas/quantidade_avaliacoes, 1)
        return media

    @property
    def exibir_cardapio(self):
        print(f"Cardápio do restaurante: {self.nome_restaurante}")
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem_prato = f"{i}. Nome: {item._nome} \n| Preço: {item._preco} \n| Descrição: {item.descricao} \n"
                print(mensagem_prato)
            elif hasattr(item, 'sabor'):
                mensagem_sobremesa = f"{i}. Nome: {item._nome} \n| Preço: {item._preco} \n| Sabor: {item.sabor} \n"
                print(mensagem_sobremesa)
            else:
                mensagem_bebida = f"{i}. Nome: {item._nome} \n| Preço: {item._preco} \n| Tamanho: {item.tamanho} \n"
                print(mensagem_bebida)


    def alterar_status(self):
        self._status = not self._status

    def receber_avaliacoes(self, cliente, nota):
        avaliacao = Avaliacoes(cliente, nota)
        self._avaliacoes.append(avaliacao)

    def adicionar_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)