# 65 - Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

num = int(input('Informe o tamanho do conjunto de números(entre 0 e 1000): '))
cont, max, min, soma, num2 = 0, 0, 0, 0, 0

while cont < num:
    num2 = int(input('Informe um número: '))
    if (num2 < 0) or (num2 > 1000):
        print('Número fora dos parâmetros, insira um número entre 0 e 1000!')
    else:
        cont += 1
        soma = soma + num2
        if num > max:
            max = num
        elif num < min:
            min = num

print(f'O maior número é {max}, o menor número é {min} e a soma dos números é igual a {soma}')
