# 112 - Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será
#     determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco
#     distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos.
#     O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme
#     o exemplo abaixo:
#     Atleta: Rodrigo Curvêllo
#
#     Primeiro Salto: 6.5 m
#     Segundo Salto: 6.1 m
#     Terceiro Salto: 6.2 m
#     Quarto Salto: 5.4 m
#     Quinto Salto: 5.3 m
#
#     Resultado final:
#     Atleta: Rodrigo Curvêllo
#     Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
#     Média dos saltos: 5.9 m

num = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']
saltos = []
nome = ' '

print('Para finalizar, deixe o nome em branco e tecle ENTER.')
while nome != '':
    atletas = []
    soma_saltos = 0
    nome = input('Atleta: ')
    if nome != '':
        atletas.append(nome)
        for i in range(0, 5):
            salto = float(input(f'{num[i]} Salto: '))
            atletas.append(salto)
            soma_saltos += salto

        media_salto = soma_saltos / 5
        atletas.append(media_salto)

        saltos.append(atletas)


for i in range(0, len(saltos)):
    print('Resultado Final:')
    print(f'Atleta: {saltos[i][0]}')
    print(f'Saltos: {saltos[i][1]} - {saltos[i][2]} - {saltos[i][3]} - {saltos[i][4]},'
          f' - {saltos[i][5]}')
    print(f'Média dos Saltos: {saltos[i][6]} m')