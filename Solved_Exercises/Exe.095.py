# 95 - Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

n = int(input('Informe o número de termos: '))
termo = 1
soma = 0

print('H = ', end = '')

for i in range(1, n + 1):
    print(f'{termo}/{i} ', end = '')
    if i < n and n > 1:
        print('+ ', end = '')

    soma += termo/i


print(f' = {soma}')
