# 142 - Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na
#     tela por extenso.

unidade = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
deze1 = ['dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove']
deze2 = ['', '', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta',
           'oitenta', 'noventa']


def num_extenso(num):
    if num < 10:
        print(unidade[num].capitalize())
    elif num < 20:
        print(deze1[num-10].capitalize())
    else:
        dezena = int(num / 10)
        print(deze2[dezena].capitalize(), end = '')
        if num % 10 != 0:
            num = num % 10
            print(f' e {unidade[num].capitalize()}')


num = int(input('Informe um número de 0 a 99: '))

if (num < 0) or (num > 99):
    print('Número inválido!')

num_extenso(num)
