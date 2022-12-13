# 71 - Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de
#     idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa,
#     conforme a média calculada.

pessoas = int(input('Quantas pessoas você quer calcular a média das idades: '))
cont = 0
media = 0

while cont < pessoas:
    idade = int(input('Informe a idade: '))
    media = media + idade
    cont += 1

media = media / pessoas

if media < 26:
    print(f'A média das idades é de {media}, a turma é joven!')
elif media < 60:
    print(f'A média das idades é de {media}, a turma é adulta!')
else:
    print(f'A média das idades é de {media}, a turma é idosa!')