# 149 - Classe Bola: Crie uma classe que modele uma bola:
#
#     Atributos: Cor, circunferência, material
#     Métodos: trocaCor e mostraCor

class Bola:
    def __init__(self, circunferencia: int, material: str):
        self.circunferencia = circunferencia
        self.material = material

    def mostra_bola(self):
        print(f'A bola tem uma circunferência de {self.circunferencia} cm e é feita de {self.material}')

    def troca_cor(self, cor: str):
        self.cor = cor

    def mostra_cor(self):
        print(f'A cor da bola é {self.cor}')

bola = Bola(circunferencia = 15, material = 'plastico')
bola.mostra_bola()
bola.troca_cor('azul')
bola.mostra_cor()