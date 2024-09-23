from avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self,nome,categoria):
        self._nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False # o _ torna o atributo ativo privado
        self._avaliacao = [] # lista de avaliações
        Restaurante.restaurantes.append(self) # todas as vezes que o objeto for instanciado, será colocado na list restaurantes

    def __str__(self):
        return f'{self._nome} | {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls): # cls é usado por convenção quando é um metodo da classe
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'.ljust(25)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} |{restaurante.ativo}')
    
    @property #Modifica a forma como o atributo será lido
    def ativo(self):
        return '☑' if self._ativo else '☐'

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if not self._ativo:
             return 0 
        else:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property # é necessario ler essas informações
    def media_avaliacoes(self):
        if not self._avaliacao or not self._ativo:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
                        # Pegue somente as notas de cada avaliação e some
        quantidade_de_notas = len(self._avaliacao)
        media_de_notas = round(soma_das_notas / quantidade_de_notas, 1) # so quero uma casa depois da virgurla
        return media_de_notas



