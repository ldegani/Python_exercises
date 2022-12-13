# 69 - Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
#     O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.

num = 0
div = 0
count = 0

while num <= 0:
    num = int(input('Informe até qual número primo você deseja verificar: '))
    if num <= 0:
        print('Não é um valor dentro do parâmetro!')

    if num == 1:
        print('Não existem número primos até este parâmetro')

    for i in range(2, num + 1):
        for j in range(2, num + 1):
            div += 1
            if i % j == 0:
                count += 1

        if count > 1:
            print(f'Num {j} não é primo')
        else:
            print(f'Num {j} é primo')


print(f'Foram feitas {div} divisões')


