# 54 - Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0

for i in range(5):
    num = int(input('Informe um número: '))
    soma += num
    media = (soma/(i+1))


print(f'A soma dos números é {soma} e a média é {media}')
