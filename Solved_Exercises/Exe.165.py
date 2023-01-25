# 165 - Crie uma Fazenda de Bichinhos instanciando vários objetos bichinho e mantendo o controle deles através de uma
#     lista. Imite o funcionamento do programa básico, mas ao invés de exigir que o usuário tome conta de um único
#     bichinho, exija que ele tome conta da fazenda inteira. Cada opção do menu deveria permitir que o usuário
#     executasse uma ação para todos os bichinhos (alimentar todos os bichinhos, brincar com todos os bichinhos, ou
#     ouvir a todos os bichinhos). Para tornar o programa mais interessante, dê para cada bichinho um nivel inicial
#     aleatório de fome e tédio.

from random import randint

class BichinhoVirtual:

    def __init__(self, nome):
        self.nome = nome
        self.fome = randint(1, 10)
        self.saude = randint(1, 10)
        self.humor = randint(1, 10)
        self.idade = randint(1, 10)

    def da_comida(self):
        self.fome -= 1
        self.humor += 0.5
        return f'Você alimentou o {self.nome}!' \
               f'Seu humor melhorou em 0.5!'

    def brinca(self, tempo):
        if tempo > 10:
            tempo = 10
            self.humor += (tempo * 0.2)
        else:
            self.humor += (tempo * 0.2)
        return f'Você brincou por {tempo} minutos! Humor melhorou em {tempo * 0.2}'

    """ Metodos para setar os valores """

    def set_nome(self, nome):
        self.nome = nome

    """ Metodos para retornar os valores """

    def get_nome(self):
        return self.nome

    def get_fome(self):
        return f'Nível de fome: {self.fome}.'

    def get_saude(self):
        return f'Nível de saúde: {self.saude}'

    def get_idade(self):
        return self.idade

    def get_humor(self):
        return self.humor

    """ Backdoor """

    def __str__(self):
        print('\nNome: ', self.get_nome())
        print('Idade: ', self.get_idade())
        print('Fome: ', self.get_fome())
        print('Humor: ', self.get_humor())


def main():

    tamaguchi1 = BichinhoVirtual('Bolinha')
    tamaguchi2 = BichinhoVirtual('Miko')
    tamaguchi3 = BichinhoVirtual('Doug')
    tamaguchi4 = BichinhoVirtual('Cleber')

    tamaguchi1.__str__()
    tamaguchi2.__str__()
    tamaguchi3.__str__()
    tamaguchi4.__str__()

    fazenda = [tamaguchi1, tamaguchi2, tamaguchi3, tamaguchi4]

    jogo = True

    while jogo == True:

        acao = int(input('\nQual ação você quer fazer:'
                     '\n1 - Dar comida'
                     '\n2 - Brincar por 5 minutos'
                     '\n3 - Ver bicinhos'
                     '\nAção: '))

        for i in fazenda:
            if acao == 1:
                print(i.da_comida())
                print(i.get_humor())
            elif acao == 2:
                print(i.brinca(5))
                print(i.get_humor())
            elif acao == 3:
                print(i.__str__())

        continua = input('Continuar? S/N - \n')
        if continua.upper() == 'S':
            jogo = True
        else:
            jogo = False

main()