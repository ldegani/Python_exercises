# 159 - Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:
#
#     Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível
#     no tanque. O consumo é especificado no construtor e o nível de combustível inicial é 0.
#     Forneça um método andar() que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de
#     combustível no tanque de gasolina.
#     Forneça um método get_gasolina(), que retorna o nível atual de combustível.
#     Forneça um método adicionar_gasolina(), para abastecer o tanque. Exemplo de uso:
#     meuFusca = Carro(15);           # 15 quilômetros por litro de combustível.
#     meuFusca.adicionar_gasolina(20); # abastece com 20 litros de combustível.
#     meuFusca.andar(100);            # anda 100 quilômetros.
#     meuFusca.get_gasolina()        # Imprime o combustível que resta no tanque.

class Carro:

    def __init__(self, consumo):
        self.consumo = consumo
        self.quantidade_combustivel = 0

    def adicionar_gasolina(self, litros):
        self.quantidade_combustivel += litros

    def andar(self, km):
        if self.quantidade_combustivel == 0:
            print(f'Veículo sem gasolina!')
        else:
            self.quantidade_combustivel -= km / self.consumo

    def get_gasolina(self):
        return f'Gasolina no veículo: {self.quantidade_combustivel:.2f} litros.'

def main():
    meu_fusca = Carro(15)

    meu_fusca.adicionar_gasolina(20)
    meu_fusca.andar(100)
    print(meu_fusca.get_gasolina())

    meu_gol = Carro(12)

    meu_gol.adicionar_gasolina(0)
    meu_gol.andar(100)
    print(meu_gol.get_gasolina())

main()
