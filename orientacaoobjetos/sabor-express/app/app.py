from restaurante import Restaurante 
# de (pasta.arquivo) importe a (classe)

praca = Restaurante('praca', 'Gourmet')

praca.alternar_estado()

praca.receber_avaliacao('Ayron', 10)
praca.receber_avaliacao('Salomao', 7)
praca.receber_avaliacao('Pablo', 2)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()