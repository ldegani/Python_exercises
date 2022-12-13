# 42 - Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
#     O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#     par ou ímpar;
#     positivo ou negativo;
#     inteiro ou decimal.

num1 = float(input('Informe o primeiro número: '))
num2 = float(input('Informe o segundo número: '))
opr = input('Qual tipo de operação você gostaria de fazer(adição(+), subtração(-), (/)) ou multiplicação(*)): ')

if opr == '+':
    res = num1 + num2
elif opr == '-':
    res = num1 - num2
elif opr == '/':
    res = num1 / num2
elif opr == '*':
    res = num1 * num2
else:
    print('Não é uma operação válida!')
    exit()

if res % 2 ==0:
    tipo1 = 'Par'
else:
    tipo1 = 'Impar'

if res > 0:
    tipo2 = 'Positivo'
else:
    tipo2 = 'Negativo'

if round(res) == res:
    tipo3 = 'Inteiro'
else:
    tipo3 = 'Decimal'

print(f'O resultado da operação é igual a {res}, que é um número {tipo1}, {tipo2} e {tipo3}')
