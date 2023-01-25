# 150 - Classe Quadrado: Crie uma classe que modele um quadrado:
#
#     Atributos: Tamanho do lado
#     Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:

    'Define um Quadrado'

    def __init__(self, lado: int):
        self.lado = lado

    def area(self):
        area = self.lado * self.lado
        return 'A área é {}'.format(area)


entrada = int(input('Informe o valor do lado: '))

quad_1 = Quadrado(entrada)
print(quad_1.area())
print(Quadrado.area(quad_1))