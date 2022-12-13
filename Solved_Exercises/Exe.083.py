# 83 - Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
#     Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
#     Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
#     A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
#     Faça um programa que determine o salário atual desse funcionário.
#     Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.

sal = int(input('Qual o salário inicial do funcionário: '))
aumento = float(input('Qual a primeira taxa de aumento do funcionário: '))
i_contrato = int(input('Informe o ano de contrato do funcionário: '))
ano_atual = int(input('Informe o ano atual: '))
anos_corridos = ano_atual - i_contrato

for i in range(0, anos_corridos + 1):
    sal = sal + (sal * (aumento / 100))
    i_contrato +=1
    print('Ano %s, salário de R$%.2f Percentual de aumento %.2f' %(i_contrato, sal, aumento))
    aumento *= 2



