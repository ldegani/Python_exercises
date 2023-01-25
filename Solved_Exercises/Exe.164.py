# 164 - Crie uma "porta escondida" no programa do programa do bichinho virtual que mostre os valores exatos dos
#     atributos do objeto. Consiga isto mostrando o objeto quando uma opção secreta, não listada no menu, for informada
#     na escolha do usuário. Dica: acrescente um método especial str() à classe Bichinho.


class BichinhoVirtual:

    def __init__(self, nome):
        self.nome = nome
        self.fome = 5
        self.saude = 5
        self.humor = 2
        self.idade = 0

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
        return f'Você brincou por {tempo} minutos! Humor melhoro em {tempo * 0.2}'

    """Metodos para setar os valores"""

    def set_nome(self, nome):
        self.nome = nome

    """Metodos para retornar os valores"""

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

    nome = 'Bolinha'
    tamaguchi = BichinhoVirtual(nome)
    print(tamaguchi.da_comida())
    print(tamaguchi.get_fome())

    print(f'Humor: {tamaguchi.get_humor()}')
    print(tamaguchi.brinca(5))
    print(f'Humor: {tamaguchi.get_humor()}')
    print(tamaguchi.brinca(5))
    print(f'Humor: {tamaguchi.get_humor()}')

    tamaguchi.__str__()

main()