# 94 - Faça um programa que mostre os n termos da Série a seguir:
#   S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
#   Imprima no final a soma da série.

n = int(input('Informe quantos termos deve ter a série: '))
termo = 1
soma = 0

print('S = ', end = '')
for i in range(1, n + 1):
    print(f'{i}/{termo} ', end = '')
    if i < n and n > 1:
        print('+ ', end = '')
    soma += i/termo
    termo += 2

print(f'= {soma}')
