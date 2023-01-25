# 158 - Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
#
#     Possua uma classe chamada bomba_combustível, com no mínimo esses atributos:
#     tipo_combustivel, valor_litro, quantidade_combustivel
#     Possua no mínimo esses métodos:
#     abastecer_valor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi
#     colocada no veículo
#     abastecer_litro( ) – método onde é informado a quantidade em litros de combustível e mos  tra o valor a ser pago
#     pelo cliente.
#     alterar_valor( ) – altera o valor do litro do combustível.
#     alterar_combustivel( ) – altera o tipo do combustível.
#     alterar_quantidade_combustivel( ) – altera a quantidade de combustível restante na bomba.
#     OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.

class BombaCombustivel:

    def __init__(self, combustivel, valor_litro, quantidade_combustivel):
        self.combustivel = combustivel    # tipo do combustível na bomba
        self.valor_litro = valor_litro    # valor do litro na bomba
        self.quantidade_combustivel = quantidade_combustivel    # combustivel na bomba

    def abastecer_valor(self, valor):
        self.quantidade_combustivel -= valor / self.valor_litro
        return f'Quantidade total abastecida com R${valor}: {valor / self.valor_litro:.2f} litros.'

    def abastecer_litro(self, litros):
        self.quantidade_combustivel -= litros
        return f'Valor total para {litros}: R${self.valor_litro * litros:.2f}.'

    def alterar_valor(self, valor):
        self.valor_litro = valor
        return f'Valor do litro alterado para R${self.valor_litro}'

    def alterar_combustivel(self, combustivel):
        self.combustivel = combustivel
        return f'Tipo do combustível alterado para {self.combustivel}'

    def alterar_quantidade_combustivel(self, quantidade):
        self.quantidade_combustivel = quantidade
        return f'Quantidade atual de combustível na bomba: {self.quantidade_combustivel}'

    def get_quantidade_combustivel(self):
        return f'Quantidade de {self.combustivel}: {self.quantidade_combustivel} litros.'

def main():
    bomba1 = BombaCombustivel("Gasolina", 2.50, 500)

    print(bomba1.abastecer_valor(100))
    print(bomba1.get_quantidade_combustivel())
    print(bomba1.abastecer_valor(30))
    print(bomba1.get_quantidade_combustivel())
    print(bomba1.abastecer_litro(25))
    print(bomba1.get_quantidade_combustivel())


main()
