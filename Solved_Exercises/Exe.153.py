# 153 - Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os
#     seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes:
#     alterarNome, depósito e saque;
#     No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.

class Conta_Corrente:

    def __init__(self, conta, correntista):
        self.conta = conta
        self.correntista = correntista
        self.saldo = 0

    def alterar_nome(self, nome):
        self.correntista = nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor

    def get_correntista(self):
        return self.correntista

    def get_conta(self):
        return self.conta

    def get_saldo(self):
        return self.saldo

    def get_infos(self):
        return f'\nCorrentista: {self.correntista}\n' \
               f'Conta: {self.conta}\n' \
               f'Saldo: {self.saldo}\n'


def main():
    print('Informe os dados de cadastro: ')
    nome = input('Nome do Correntista: ')
    conta = int(input('Número da conta: '))

    conta1 = Conta_Corrente(conta, nome)
    print(conta1.get_infos())


main()
