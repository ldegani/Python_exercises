# 34 - Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
#     O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#     Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer
#     pedir os demais valores, sendo encerrado;
#     Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#     Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#     Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

import math

va = float(input('Informe o valor de a: '))
vb = float(input('Informe o valor de b: '))
vc = float(input('Informe o valor de c:' ))

delta = ((vb**2) - (4*va*vc))

if va == 0:
    print('O valor de A não pode ser zero, pois não é uma equação de segundo grau!')
elif delta < 0:
    print(f'O valor de delta é {delta}, a equação não possui valores reais!')
elif delta == 0:
    rquadrada = math.sqrt(delta)
    raiz1 = (-vb + rquadrada) / (2 * va)
    print(f'Como delta é igual a zero, a equação possui apenas uma raiz real, que é {raiz1}')
else:
    rquadrada = math.sqrt(delta)
    raiz1 = (-vb + rquadrada) / (2*va)
    raiz2 = (-vb - rquadrada) / (2*va)
    print(f'O valor de delta é {delta} e suas raizes são: {raiz1} e {raiz2}.')

