# 60 - Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a
#     quantidade de números impares.

num = 0
par = 0
imp = 0

while num < 10:
    num2 = int(input('Informe um número inteiro: '))
    num += 1
    if num % 2 == 0:
        par += 1
    else:
        imp += 1
r4
print(f'Total de {par} números pares e {imp} números ímpares!')
