# 151 - Classe Retangulo: Crie uma classe que modele um retangulo:
#
#     Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
#     Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
#     Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
#     Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o
#     local.

class Retangulo:

    """Define e molda um retângulo"""

    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def get_comprimento(self):
        return self.comprimento

    def get_largura(self):
        return self.largura

    def calcula_area(self):
        return self.comprimento * self.largura

    def calcula_perimetro(self):
        return self.comprimento * 2 + self.largura * 2

    def calcula_pisos(self):
        area = self.calcula_area()
        sobra = 1.10
        area_piso = 1.8
        return round(area * sobra * area_piso)

    def calcula_rodape(self):
        comp = self.get_comprimento()
        larg = self.get_largura()
        rodape = 0.15
        sobra = 1.10
        return round((2*(comp/rodape) + 2*(larg/rodape)) * sobra, 2)


def main():
    print('Informe as medidas (em metros) abaixo.')
    comprimento = int(input('Informe o comprimento: '))
    largura = int(input('Informe a largura: '))

    retangulo = Retangulo(comprimento, largura)
    print(f'A área é de: {retangulo.calcula_area()} metros.')
    print(f'O perímetro é de: {retangulo.calcula_perimetro()} metros.')
    print(f'Você irá precisar de {retangulo.calcula_pisos()} unidades de piso.')
    print(f'Você irá precisar de {retangulo.calcula_rodape()} metros de rodapé.')


main()
