from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self._tamanho = tamanho
    def __str__(self):
        return super().__str__()
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.08) # subtraindo 5% do preço do produto