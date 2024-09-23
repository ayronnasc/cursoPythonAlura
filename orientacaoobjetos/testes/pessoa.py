class Pessoa: 
    _nome   = ''
    _idade  = int
    profissao = ''
    apelido = ''

    def __init__(self, nome, idade):
        self._nome  = nome
        self._idade = idade

    def empregar(self, profissao):
        self.profissao = profissao
        return '{self.nome} foi contratado como {profissao} com Sucesso!'
    
    def apelidar(self, apelido):
        self.apelido = apelido 
        return f'{self._nome} agora será chamado de {apelido}!'
    
    def __str__(self):
        return f'{self._nome} tem {self._idade} anos e atualmente trabalha como {self.profissao}' if self.profissao != '' else f'{self._nome} tem {self._idade} anos e atualmente está desempregado'
    
    def saudacao(self):
        match self.profissao:
            case 'Medico':
                print(f'Olá meu amigo/a ! sou o Doutor {self._nome} e estou a sua disposição para lhe atender!')
            case 'Engenheiro':
                print(f'Olá, sou {self._nome} e tenho uma construtora, que tal fazer um orçamento para a construção de uma casa comigo?')
            case 'Advogado':
                print(f'Olá! como posso tratar seu caso? sou {self._nome} e estou pronto para resolver seu problema na corte judicial!')    
            case _: 
                print(f'Olá! me chamo {self._nome}, tenho {self._idade} e trabalho como {self.profissao}')
        return True

carlos = Pessoa('Carlos',21)
carlos.empregar('Medico')
carlos.apelidar('Carlinhos')

carlos.saudacao()