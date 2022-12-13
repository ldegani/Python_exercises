# 100 - Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR
#     e os números IMPARES no vetor impar. Imprima os três vetores.

num, par, imp = [], [], []

for i in range (0, 10):
    num.append(int(input('Informe um número: ')))

for i in range(0, 10):
    if num[i] % 2 == 0:
        par.append(num[i])
    else:
        imp.append(num[i])

print(num)
print(par)
print(imp)
