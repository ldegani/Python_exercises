# 98 - Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []
media = 0

for i in range(4):
    notas.append(float(input('Informe a nota: ')))

media = sum(notas)
media /= 4

print(notas)
print(media)

