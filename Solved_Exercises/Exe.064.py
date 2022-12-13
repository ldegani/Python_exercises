# 64 - Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

num = int(input('Informe o tamanho do conjunto de números: '))
cont, max, min, soma, num2 = 0, 0, 0, 0, 0

while cont < num:
    num2 = int(input('Informe um número: '))
    cont += 1
    soma = soma + num2
    if num > max:
        max = num
    elif num < min:
        min = num

print(f'O maior número é {max}, o menor número é {min} e a soma dos números é igual a {soma}')

