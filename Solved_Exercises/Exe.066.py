# 66 - Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes
#     e limitando o fatorial a números inteiros positivos e menores que 16.

qtde = 0
while qtde <= 0:
    qtde = int(input('Informe quantos fatoriais você quer calcular: '))
    if qtde < 0:
        print('Quantidade deve ser maior que zero!')

for i in range(0, qtde):
    termo = 0
    termo = int(input('Informe um número positivo até 16 para calcular o fatorial: '))
    if (termo <= 0) or (termo > 16):
        print('Número fora dos parâmetros!')

    fatorial = 1
    for i in range(1, termo + 1):
        fatorial *= i

    print(fatorial)
