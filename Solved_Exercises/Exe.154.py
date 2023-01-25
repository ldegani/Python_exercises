# 154 - Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de
#     informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do
#     volume permanecem dentro de faixas válidas.

class Televisao:

    def __init__(self):
        self.canal = 1
        self.volume = 10

    def set_canal(self, canal):
        if (canal >= 0) and (canal <= 30):
            self.canal = canal

    def aumenta_volume(self, volume):
        if self.volume < 20:
            self.volume += 1

    def diminui_volume(self, volume):
        if self.volume > 0:
            self.volume -= 1

    def get_canal(self):
        return self.canal

    def get_volume(self):
        return self.volume


def main():
    tv = Televisao()
    tv.set_canal(5)
    print(tv.get_canal())
    tv.aumenta_volume(4)
    print(tv.get_volume())


main()
