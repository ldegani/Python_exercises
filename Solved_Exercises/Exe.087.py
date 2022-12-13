# 87 - Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos
#     seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um
#     número negativo.


num = 0
cont1, cont2, cont3, cont4 = 0, 0, 0, 0

while num >= 0:
    num = int(input('Informe um número de 0 a 100(digite um negativo para parar): '))

    if (num >= 0) and (num <= 25):
        cont1 += 1
    elif (num > 25) and (num <= 50):
        cont2 += 1
    elif (num > 50) and (num <= 75):
        cont3 += 1
    elif (num > 75) and (num < 101):
        cont4 += 1

print(f'''Quantidades:
[0 - 25] : {cont1}
[26 - 50] : {cont2}
[51 - 75] : {cont3}
[76 - 100] : {cont4}
''')
