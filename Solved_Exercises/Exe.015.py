# 15 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o
# Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# a) salário bruto.
# b) quanto pagou ao INSS.
# c) quanto pagou ao sindicato.
# d) o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

salBruto = float(input("Informe o seu salário bruto: "))

vInss = salBruto * 0.08
vSind = salBruto * 0.05
vIr = salBruto * 0.11
vSalLiq = salBruto - vInss - vSind - vIr

print("Seu salário brunto é R$", salBruto)
print("O valor do desconto do IR é de R$", vIr)
print("O valor do desconto do INSS é de R$", vInss)
print("O valor do desconto do Sindicato é de R$", vSind)
print("O valor do seu salário liquido é de R$", vSalLiq)

