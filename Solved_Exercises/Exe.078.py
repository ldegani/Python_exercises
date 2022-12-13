# 78 - Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120.
#     A saída deve ser conforme o exemplo abaixo:
#     Fatorial de: 5
#     5! =  5 . 4 . 3 . 2 . 1 = 120

fatorial = int(input('Fatorial de: '))
fat = 1

print('%s! = ' % fatorial, end = '')
for i in reversed(range(2, fatorial + 1)):
    print('%d . ' % i, end = '')
    fat *= i

print('1 = %d' % fat)
