# 30 - Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do
#     Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato
#     e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
#     O Salário Líquido corresponde ao Salário Bruto menos os descontos.
#     O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#     Desconto do IR:
#     Salário Bruto até 900 (inclusive) - isento
#     Salário Bruto até 1500 (inclusive) - desconto de 5%
#     Salário Bruto até 2500 (inclusive) - desconto de 10%
#     Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações,
#     dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#         Salário Bruto: (5 * 220)        : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00
#         (-) INSS ( 10%)                 : R$  110,00
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00

horas = float(input('Informe a quantidade de horas trabalhadas no mês: '))
vh = float(input('Informe o valor da hora trabalhada: '))

sal = horas * vh
fgts = 0.11 * sal
sind = 0.03 * sal
inss = 0.10 * sal

if sal <= 900:
    desc = '0%'
    ir = sal * 0
elif sal <= 1500:
    desc = '5%'
    ir = sal * 0.05
elif sal <= 2500:
    desc = '10%'
    ir = sal * 0.10
else:
    desc = '20%'
    ir = sal * 0.20

descontos = inss + ir
sal2 = sal - descontos

print(f'''
Salário Bruto ({vh} * {horas})  = R${sal}
(-) IR ({desc})                 = R${ir}
(-) INSS(10%)                   = R${inss}
FGTS (11%)                      = R${fgts}
Total Descontos                 = R${descontos}
Salário Líquido                 = R${sal2}
''')
