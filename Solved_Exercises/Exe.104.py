# 104 - Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos
#     quadrados dos elementos do vetor.

num = []
somaquad = 0

for i in range(0, 10):
    num.append(int(input('Informe um número: ')))

for i in num:
    quad = i ** 2
    somaquad += quad

soma = sum(num)

print(num)
print(soma)
print(somaquad)
