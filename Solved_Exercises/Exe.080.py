# 80 - Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia.
#     Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número
#     inteiro e determine se ele é ou não um número primo.

primo = int(input('Informe o número: '))
cont = 0

for i in range(2, primo):
    if primo % i == 0:
        cont += 1

if cont > 0:
    print('Não é primo!')
else:
    print('É primo!')
