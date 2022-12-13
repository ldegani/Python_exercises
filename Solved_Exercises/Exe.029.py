# 29 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e
#     lhe contraram para desenvolver o programa que calculará os reajustes.
#     Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
#     baseado no salário atual:
#     salários até R$ 280,00 (incluindo) : aumento de 20%
#     salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#     salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#     salários de R$ 1500,00 em diante : aumento de 5%
#     Após o aumento ser realizado, informe na tela:
#     o salário antes do reajuste;
#     o percentual de aumento aplicado;
#     o valor do aumento;
#     o novo salário, após o aumento.

sal = float(input('Informe o valor do salário do colaborador: '))

if sal <= 280:
    aj = 20
    au = sal * 0.20
    rj = sal * aj
elif sal <= 700:
    aj = 15
    au = sal * 0.15
    rj = sal * aj
elif sal <= 1500:
    aj = 10
    au = sal * 1.10
    rj = sal * aj
else:
    aj = 5
    au = sal * 0.05
    rj = sal * aj

print(f'''
O salário antes do reajuste era de R${sal}.
O ajuste foi de {aj}%.
O aumento foi de R${au}.
O novo salário é R${rj}.
''' )

#%(sal, aj, au, rj)
