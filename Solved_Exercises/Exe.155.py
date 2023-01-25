# 155 - Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
#     Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e
#     Idade Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor
#     é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo
#     para armazenar esta informação por que ela pode ser calculada a qualquer momento.


class BichinhoVirtual:

    def __init__(self, nome):
        self.nome = nome
        self.fome = 5
        self.saude = 5
        self.idade = 0

    def dar_comida(self, valor):
        self.fome -= valor

    """Metodos para setar os valores"""

    def set_nome(self, nome):
        self.nome = nome

    """Metodos para retornar os valores"""

    def get_nome(self):
        return self.nome

    def get_fome(self):
        return self.fome

    def get_saude(self):
        return self.saude

    def get_idade(self):
        return self.idade

    def get_humor(self):
        return self.fome + self.saude


def main():
    nome = input('Nome do Tamagochi: ')
    tamaguchi = BichinhoVirtual(nome)
    tamaguchi.dar_comida(1)

    print(f'Nível de fome:{tamaguchi.get_fome()}')
    print(f'Nível de saúde:{tamaguchi.get_saude()}')
    print(f'Humor: {tamaguchi.get_humor()}')


main()
