# 68 - Altere o programa de cálculo dos números primos, informando, caso o número não seja primo,
#     por quais número ele é divisível.

num = 0
cont = 0
div = 0

while num <= 0:
    num = int(input('Informe um número que deseja verificar se é primo: '))
    if num <= 0:
        print('Número inválido! Fora dos parâmetros!')

    for i in range(1, 10):
        if num % i == 0:
            cont +=1
            print('O número é divisível por: ')
            print(i)

        if cont == 2:
            resp = 'É primo'
        else:
            resp = 'Não é primo'

    print(resp)
