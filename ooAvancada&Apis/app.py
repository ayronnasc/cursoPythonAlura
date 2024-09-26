from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
suco = Bebida('Laranja', 3.5, 'Grande')
miojo = Prato('Miojo de Carne', 10, 'Macarrão pré-pronto de sabor carne')

restaurante_praca.adicionar_no_cardapio(suco)
restaurante_praca.adicionar_no_cardapio(miojo)

suco.aplicar_desconto()
miojo.aplicar_desconto()


def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()