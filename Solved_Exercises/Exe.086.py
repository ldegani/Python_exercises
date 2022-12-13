# 86 - Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados:
#     valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
#     Os juros e a quantidade de parcelas seguem a tabela abaixo:
#     Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
#     1       0
#     3       10
#     6       15
#     9       20
#     12      25
#     Exemplo de saída do programa:
#     Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
#     R$ 1.000,00     0               1                       R$  1.000,00
#     R$ 1.100,00     100             3                       R$    366,00
#     R$ 1.150,00     150             6                       R$    191,67


divida = int(input('Informe o valor da dívida: '))
juros = 0
parcela = 1

print('Valor Dívida  Valor Juros  Quantidade Parcelas  Valor Parcela')
# print(f'{divida}              {juros}              {parcela}            {divida / parcela}')
for i in (1, 3, 6, 9, 12):
    valor_juros = divida * (juros /100)
    valor_divida = divida + valor_juros
    valor_parcela = valor_divida / i

    if i == 1:
        juros = 10
    else:
        juros += 5

    print(f'{valor_divida}          {valor_juros}            {i}               {valor_parcela}')