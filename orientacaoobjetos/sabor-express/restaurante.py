class Restaurante:
    restaurantes = []

    def __init__(self,nome,categoria):
        self._nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False # o _ torna o atributo ativo privado
        Restaurante.restaurantes.append(self) # todas as vezes que o objeto for instanciado, será colocado na list restaurantes

    def __str__(self):
        return f'{self._nome} | {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls): # cls é usado por convenção quando é um metodo da classe
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Ativo'.ljust(25)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')
    
    @property #Modifica a forma como o atributo será lido
    def ativo(self):
        return '☑' if self._ativo else '☐'

    def alternar_estado(self):
        self._ativo = not self._ativo

restaurante_praca = Restaurante('Praca', 'Gourmet')
restaurante_pizza = Restaurante('Pizza', 'Italiano')
restaurante_praca.alternar_estado()

Restaurante.listar_restaurantes()
