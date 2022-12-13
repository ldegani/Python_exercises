# 118 - Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um
#     vetor. Depois, mostre quantas vezes cada valor foi conseguido.
#     Dica: use um vetor de contadores(1-6).

# Importa o módulo random

import random

dado = [0] * 6

for i in range(0, 100):
    lancamento = random.randint(0, 5)
    dado[lancamento] += 1

print('Lado - Quantidade')
for i in range(0, 6):
    print(f'{i+1}    -    {dado[i]}')
