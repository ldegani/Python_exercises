# 163 - Classe Bichinho Virtual++: Melhore o programa do bichinho virtual, permitindo que o usuário especifique quanto
#     de comida ele fornece ao bichinho e por quanto tempo ele brinca com o bichinho. Faça com que estes valores afetem
#     quão rapidamente os níveis de fome e tédio caem. * Humor aumenta.


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


main()
