# 70 - Faça um programa que calcule o mostre a média aritmética de N notas.

n_Notas = int(input('Informe a quantidade de notas que você quer calcular a média: '))
cont = 0
media = 0

while cont < n_Notas:
    nota = int(input('Informe a nota: '))
    media = media + nota
    cont += 1

media = media / n_Notas

print(media)