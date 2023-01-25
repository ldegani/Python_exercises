# 162 - Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) que
#     aumente o salário do funcionário em uma certa porcentagem.
#     Exemplo de uso:
#     harry=funcionário("Harry",25000)
#     harry.aumentarSalario(10)


class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumenta_salario(self, porcentagem):
        self.salario = self.salario + (self.salario * (porcentagem /100))

    def get_nome(self):
        return f'O nome do funcionário é {self.nome}'

    def get_salario(self):
        return f'Salário no valor de: R${self.salario:.2f}'


def main():
    funcionario1 = Funcionario('Harry', 25000)

    print(funcionario1.get_nome())
    print(funcionario1.get_salario())
    funcionario1.aumenta_salario(10)
    print(funcionario1.get_salario())


main()
