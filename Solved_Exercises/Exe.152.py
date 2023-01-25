# 152 - Classe Pessoa: Crie uma classe que modele uma pessoa:
#
#     Atributos: nome, idade, peso e altura
#     Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo
#     a idade dela menor que 21 anos, ela deve crescer 0,5 cm.


class Pessoa:
    """Define e modela uma pessoa"""

    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, envelhece):
        self.idade += envelhece
        if self.idade <= 21:
            self.altura += 0.5

    def engorda(self, kg):
        self.peso += kg

    def emagrece(self, kg):
        self.peso -= kg

    def cresce(self, cm):
        self.altura += cm

    def get_peso(self):
        return self.peso

    def get_altura(self):
        return self.altura

    def get_dados(self):
        return f'\nNome:   {self.nome}\n' \
               f'Idade:  {self.idade}\n' \
               f'Altura: {self.altura}cm\n' \
               f'Peso:   {self.peso}kg\n'


def main():
    print('Informe os dados da pessoa: ')
    nome = 'Lucas'
    idade = 32
    peso = 99
    altura = 182

    pessoa1 = Pessoa(nome, idade, peso, altura)
    print(pessoa1.get_dados())
    pessoa1.envelhecer(1)
    pessoa1.engorda(3)
    print(pessoa1.get_dados())


main()
