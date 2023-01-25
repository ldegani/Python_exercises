# 161 - Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string) e um
#     salário(um double). Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e
#     salário. Escreva um pequeno programa que teste sua classe.

class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def get_nome(self):
        return f'O nome do funcionário é {self.nome}'

    def get_salario(self):
        return f'Salário no valor de: R${self.salario}'


def main():
    funcionario1 = Funcionario('Harry', 25000)

    print(funcionario1.get_nome())
    print(funcionario1.get_salario())


main()
