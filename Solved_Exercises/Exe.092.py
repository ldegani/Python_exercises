# 92 - Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas.
#     A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas
#     dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima
#     informada (retirar a melhor e pior nota depois calcular a média com as notas restantes). As notas não são informadas
#     ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
#     Atleta: Aparecido Parente
#     Nota: 9.9
#     Nota: 7.5
#     Nota: 9.5
#     Nota: 8.5
#     Nota: 9.0
#     Nota: 8.5
#     Nota: 9.7
#
#     Resultado final:
#     Atleta: Aparecido Parente
#     Melhor nota: 9.9
#     Pior nota: 7.5
#     Média: 9,04

soma_notas = 0

atleta = input('Atleta: ')

for i in range(1, 8):
    nota = float(input(f'Nota {i} :'))
    soma_notas += nota

    if ('maior_nota' not in vars()) or (nota > maior_nota):
        maior_nota = nota

    if ('menor_nota' not in vars()) or (nota < menor_nota):
        menor_nota = nota

        soma_notas -= maior_nota
        soma_notas -= menor_nota

print('Resultado Final: ')
print(f'Atleta: {atleta}')
print('Maior nota: %d' % maior_nota)
print('Menor nota: %d' % menor_nota)
print('Média: %.2f' % (soma_notas / 7))

