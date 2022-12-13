# 111 - Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões.
#     O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo,
#     um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja,
#     um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores
#     receberam salários nos seguintes intervalos de valores:
#     $200 - $299 / $300 - $399 / $400 - $499 / $500 - $599 / $600 - $699 / $700 - $799 / $800 - $899 / $900 - $999
#     $1000 em diante
#     Desafio: Crie uma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.


faixas = [0] * 9
sal_base = 200

vend = int(input('Informe quantos vendedores são: '))

for i in range(0, vend):
    val_venda = int(input(f'Informe quanto o vendedor {i+1} vendeu: R$'))
    sal = val_venda * 0.09 + sal_base
    indice = int(sal / 100) - 2    # 200 / 100 = 2 ; 2 - 2 = 0
    if indice > 9:
        indice = 9

    faixas[indice] += 1

print(faixas)

for i in range(0, 9):
    print(f'{i * 100 + 200}, {i * 100 + 299}, {faixas[i]}')
