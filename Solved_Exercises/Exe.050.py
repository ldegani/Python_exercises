# 50 - Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento
#     de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
#     Faça um programa que calcule e escreva o número de anos necessários para que a população do país
#     A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

# Inicia variáveis
pop_A = 80000
pop_B = 200000
taxa_A = 0.03
taxa_B = 0.015
ano = 0

# Loop while
while pop_A < pop_B:
    pop_A = round(pop_A + (pop_A * taxa_A))
    pop_B = round(pop_B + (pop_B * taxa_B))
    ano = ano + 1

print(f'Levará {ano} anos para que a cidada A ser igual ou maior a cidade B')
print(f'População cidade A: {pop_A}')
print(f'População cidade B: {pop_B}')
