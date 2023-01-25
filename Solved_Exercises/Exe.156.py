# 156 - Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os
#     métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos dois
#     macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada
#     refeição. Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?

class Macaco:

    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)

    def ver_bucho(self):
        return f'Bucho: {self.bucho}'

    def digerir(self):
        if len(self.bucho) > 0:
            self.bucho.pop(0)


# Teste
def main():
    macaco1 = Macaco('Uga')
    macaco1.comer("banana")
    print(macaco1.ver_bucho())
    macaco1.comer("morango")
    print(macaco1.ver_bucho())
    macaco1.comer("caju")
    print(macaco1.ver_bucho())

    macaco2 = Macaco('Plin')
    macaco2.comer("melao")
    print(macaco2.ver_bucho())
    macaco2.comer("alface")
    print(macaco2.ver_bucho())
    macaco2.comer(macaco1)
    print(macaco2.ver_bucho())

    print(macaco1.ver_bucho())
    print(macaco2.ver_bucho())


main()
