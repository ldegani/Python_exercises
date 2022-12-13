# 44 - Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#     Álcool: até 20 litros, desconto de 3% por litro
#     acima de 20 litros, desconto de 5% por litro
#     Gasolina: até 20 litros, desconto de 4% por litro
#     acima de 20 litros, desconto de 6% por litro.
#     Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
#     (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente
#     sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

litros = float(input('Informe a quantidade de litros vendido: '))
combust = input('Informe se é Gasolina (G) ou Álcool (A): ')

if combust == 'G' and litros > 20:
    valor = (litros * 2.5) * 0.94
elif combust == 'G' and litros <= 20:
    valor = (litros * 2.5) * 0.96
elif combust == 'A' and litros > 20:
    valor = (litros * 1.9) * 0.95
else:
    valor = (litros * 1.9) * 0.97

round(valor, 2)

print(f'O valor a ser pago é de R${valor}')
