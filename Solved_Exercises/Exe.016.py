# 16 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área
#  a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta
#  é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta
#  a serem compradas e o preço total.

areaPintura = float(input("Informe a área total a ser pintada (em metros quadrados): "))

totalLitros = areaPintura / 3
totalLatas = totalLitros / 18

if totalLatas % 18 != 0:
    totalLatas += 1

precoTotal = totalLatas * 80

print("Você irá precisar de %d latas de tinta" % totalLatas)
print("O valor total é de R$", precoTotal)
