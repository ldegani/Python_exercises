# 35 - Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano
#     é ou não bissexto.

ano = int(input('Informar o ano: '))

divisa = ano % 4

if divisa == 0:
    print(f'O ano de {ano} é um ano bisexto!')
else:
    print(f'O ano de {ano} não é um ano bisexto!')
