# 160 - Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria, com
#     a diferença de que se adicione um atributo taxaJuros. Forneça um construtor que configure tanto o saldo inicial
#     como a taxa de juros. Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta.
#     Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%.
#     Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante.

class ContaInvestimento:

    def __init__(self, conta, correntista):
        self.conta = conta
        self.correntista = correntista
        self.saldo = 0
        self.juros = 0

    def alterar_nome(self, nome):
        self.correntista = nome

    def taxa_juros(self, valor):
        self.juros = valor

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor

    def adiciona_juros(self):
        self.saldo = self.saldo + (self.saldo * ((self.juros/12)/100))

    def get_correntista(self):
        return self.correntista

    def get_conta(self):
        return self.conta

    def get_saldo(self):
        return f'Saldo de: {self.saldo:.2f} reais.'

    def get_infos(self):
        return f'\nCorrentista: {self.correntista}\n' \
               f'Conta: {self.conta}\n' \
               f'Saldo: {self.saldo:.2f}\n' \
               f'Juros: {self.juros:.2f}% a.a.\n' \
               f'Juros: {self.juros/12:.2f}% a.m.\n'


def main():
    print('Informe os dados de cadastro: ')
    nome = 'Lucas'
    conta = 123456

    conta1 = ContaInvestimento(conta, nome)
    conta1.deposito(1000)
    conta1.taxa_juros(10)
    print(conta1.get_infos())
    conta1.adiciona_juros()
    print(conta1.get_saldo())
    conta1.adiciona_juros()
    print(conta1.get_saldo())
    conta1.adiciona_juros()
    print(conta1.get_saldo())
    conta1.adiciona_juros()
    print(conta1.get_saldo())
    conta1.adiciona_juros()
    print(conta1.get_saldo())

main()
