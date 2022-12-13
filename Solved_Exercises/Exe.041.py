# 41 - Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
#     Dica: utilize uma função de arredondamento.


num = float(input('Informe um número qualquer: '))
x = round(num)

if x == num:
    print(f'O número {num} é um número inteiro!')
else:
    print(f'O número {num} é decimal')
