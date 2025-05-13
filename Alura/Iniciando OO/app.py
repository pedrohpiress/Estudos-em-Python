from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'gourmet')

bebida_suco = Bebida('Suco de morango', 5.0, 'Grande')
prato_pao = Prato('Pao com queijo', 2.0, 'Pao com queijo e requeijão')
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_pao)
bebida_suco.aplicar_desconto()
prato_pao.aplicar_desconto()

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()    