# 53 - Faça um programa que leia 5 números e informe o maior número.

ma = 0
me = None

for i in range(0, 5):
    num = int(input('Informe um número: '))
    if num > ma:
        ma = num


#    ma = ma if ma != None and ma > num else num

print(f'O maior número é {ma}')


