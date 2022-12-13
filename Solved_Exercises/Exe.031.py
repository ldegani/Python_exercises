# 35 - Faça um Programa que leia um número e exiba o dia correspondente da semana.
#     (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

dia = int(input('Informe o número do dia da semana: '))

if dia == 1:
    print('Hoje é domingo.')
elif dia == 2:
    print('Hoje é segunda.')
elif dia == 3:
    print('Hoje é terça.')
elif dia == 4:
    print('Hoje é quarta.')
elif dia == 5:
    print('Hoje é quinta.')
elif dia == 6:
    print('Hoje é sexta.')
elif dia == 7:
    print('Hoje é sábado.')
else:
    print('Dia inválido!')
