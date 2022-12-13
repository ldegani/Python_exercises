# 67 - Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
#     Um número primo é aquele que é divisível somente por ele mesmo e por 1.

num = 0
cont=0

while num <= 0:
    num = int(input('Informe um número que deseja verificar se é primo: '))
    if num <= 0:
        print('Número inválido! Fora dos parâmetros!')

    for i in range(1, 10):
        if num % i == 0:
            cont +=1

        if cont == 2:
            resp = 'É primo'
        else:
            resp = 'Não é primo'

    print(resp)
