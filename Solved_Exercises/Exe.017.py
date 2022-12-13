# 17 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados
#     da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
#     que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros,
#     que custam R$ 25,00.
#     Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#     comprar apenas latas de 18 litros;
#     comprar apenas galões de 3,6 litros;
#     misturar latas e galões, de forma que o desperdício de tinta seja menor.
#     Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

from math import ceil

areaPintura = float(input("Informe o tamanho da área a ser pintada (em metros quadrados): "))

lLata = 18
lGalao = 3.6

litros = (areaPintura / 6) * 1.10
latas = ceil(litros / lLata)
galoes = ceil(litros / lGalao)


precoLatas = latas * 80
precoGaloes = galoes * 25
checkLitros = latas / galoes
checkPreco = precoLatas / precoGaloes

# Calculo misturando latas e galoes


print("Cobertura tinta: ", litros, "litros.")
print("O total de latas seria de: ", latas, "unidades.")
print("O valor dos galões seria de R$", precoLatas)
print("O total de galões seria de: ", galoes, "unidades.")
print("O valor dos galões seria de R$", precoGaloes)

