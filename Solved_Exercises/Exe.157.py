# 157 - Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:
#     Possua uma classe chamada Ponto, com os atributos x e y.
#     Possua uma classe chamada Retangulo, com os atributos largura e altura.
#     Possua uma função para imprimir os valores da classe Ponto
#     Possua uma função para encontrar o centro de um Retângulo.
#     Você deve criar alguns objetos da classe Retangulo.
#     Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser
#     um objeto da classe Ponto.
#     A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os
#     valores de x e y para o centro do objeto.
#     O valor do centro do objeto deve ser mostrado na tela
#     Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.

class Ponto:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_pontos(self):
        return f'Ponto x: {self._x} e Ponto y: {self._y}'


class Retangulo(Ponto):
    def __init__(self, largura, altura, x, y):
        super().__init__(x, y)
        self.largura = largura
        self.altura = altura
        self._x = x
        self._y = y

    def centro_retangulo(self):
        largura_centro = self.largura / 2
        altura_centro = self.altura / 2
        return f'O centro do retângulo está na posição:' \
               f' Largura:{largura_centro:.1f} e Altura: {altura_centro:.1f}'

    def retangulo_vertice(self):
        largura = self._x + self.largura
        altura = self._y + self.altura
        return f'Retângulo de largura: {largura} e altura {altura}.'

    def centro_ponto(self):
        largura = (self._x + self.largura) / 2
        altura = (self._y + self.altura) / 2
        return f'O centro do retângulo está na posição:' \
               f'Largura: {largura:.1f} e Altura {altura:.1f}.'

    def get_retangulo(self):
        return f'O retângulo tem as medidas: Largura {self.largura} e Altura: {self.altura}'


def main():
    retangulo1 = Retangulo(10, 15, 5, 10)

    print(retangulo1.get_pontos())
    print(retangulo1.get_retangulo())
    print(retangulo1.centro_retangulo())
    print(retangulo1.retangulo_vertice())
    print(retangulo1.centro_ponto())


main()
