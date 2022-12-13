# 122 - Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’,
#     se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def arg(a):
    if a > 0:
        print('P')
    else:
        print('N')

a = float(input('Informe um valor: '))

arg(a)
