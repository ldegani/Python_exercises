# 56 - Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo
#     compreendido por eles.

num1 = int(input('Informe o primeiro número inteiro: '))
num2 = num1
while num2 <= num1:
    num2 = int(input('Informe o segundo número inteiro: '))
    if num2 <= num1:
        print('Nùmero inválido! Deve ser maior que o primeiro número!')

for i in range(num1, num2 + 1):
    print(i, end = ' ')