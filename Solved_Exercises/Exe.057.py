# 57 - Altere o programa anterior para mostrar no final a soma dos números.

num1 = int(input('Informe o primeiro número inteiro: '))
num2 = num1
soma = 0
while num2 <= num1:
    num2 = int(input('Informe o segundo número inteiro: '))
    if num2 <= num1:
        print('Nùmero inválido! Deve ser maior que o primeiro número!')

for i in range(num1, num2 + 1):
    soma += i
    print(i, end = ' ')

print(f'A soma dos números é {soma}')
