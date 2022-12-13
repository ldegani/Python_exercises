# 102 - Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

num = []
produto = 1

for i in range(0, 5):
    num.append(int(input('Informe um número inteiro: ')))

for i in num:
    produto *= i

soma = sum(num)

print(num)
print(soma)
print(produto)


