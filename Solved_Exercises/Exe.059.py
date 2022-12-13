# 59 - Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado
#     ao segundo número. Não utilize a função de potência da linguagem.

base = int(input('Informe o número base: '))
expo = int(input('Informe o expoente: '))
result = base

for i in range(expo - 1):
    result = result * base

print(result)
