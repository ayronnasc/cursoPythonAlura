from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio): # com isso a classe prato irá herdar de ItemCardapio
    def __init__(self, nome, preco, desc):
        super().__init__(nome,preco) # super permite que acesse informações da classe item_cardapio
        self._descricao = desc
    def __str__(self):
        return super().__str__()
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)
