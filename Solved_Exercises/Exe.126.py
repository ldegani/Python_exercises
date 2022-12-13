# 126 - Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado

def num_digitos(num):
    num = abs(int(num))
    if num < 2:
        print(1)
    count = 0
    valor = 1
    while valor <= num:
        valor *= 10
        count += 1
    print(count)

num = int(input('Informe um número inteiro: '))
num_digitos(num)
