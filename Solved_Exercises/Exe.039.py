# 39 - Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário o valor do saque e
#     depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50
#     e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a
#     quantidade de notas existentes na máquina.
#     Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50,
#     uma nota de 5 e uma nota de 1;
#     Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50,
#     quatro notas de 10, uma nota de 5 e quatro notas de 1.

saque = int(input('Informe o valor do saque, entre 10 e 600 reais: '))

# cálculos das quantidade de cada nota
cem = int((saque / 100))
cinquenta = int((saque - (cem * 100)) / 50)
dez = int((saque - (cem * 100) - (cinquenta * 50)) / 10)
cinco = int(((saque - (cem * 100) - cinquenta * 50) - (dez * 10)) / 5)
um = int(((saque - (cem * 100) - cinquenta * 50) - (dez * 10) - (cinco * 5)))

# verificação se a entrada é valida
if (saque < 10) or (saque > 600):
    print('Valor inválido para saque!')
    exit()

print('As notas do seu saque serão: ')
if cem > 0:
    print(f'Notas de cem: {cem}')
if cinquenta > 0:
    print(f'Notas de cinquenta: {cinquenta}')
if dez > 0:
    print(f'Notas de dez: {dez}')
if cinco > 0:
    print(f'Notas de cinco: {cinco}')
if um > 0:
    print(f'Notas de um: {um}')
