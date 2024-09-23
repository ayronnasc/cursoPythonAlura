class Restaurante:
    restaurantes = []

    def __init__(self,nome,categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self) # todas as vezes que o objeto for instanciado, será colocado na list restaurantes

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        print('')

restaurante_praca = Restaurante('Praca', 'Gourmet')
restaurante_pizza = Restaurante('Pizza', 'Italiano')

print(restaurante_pizza) 
print(restaurante_praca) 
