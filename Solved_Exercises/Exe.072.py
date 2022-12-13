# 72 - Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
#     Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

eleitores = int(input('Informe a quantidade de eleitores: '))
cont = 0
c1, c2, c3 = 0, 0, 0

while cont < eleitores:
    voto = int(input('Qual candidato você quer votar(1, 2, 3): '))

    if voto == 1:
        c1 += 1
        cont += 1
    elif voto == 2:
        c2 += 1
        cont += 1
    elif voto == 3:
        c3 += 1
        cont += 1
    else:
        print('Candidato inválido!')

print(f'''
Total de votos para cada candidato:
Candidato 1: {c1}
Candidato 2: {c2}
Candidato 3: {c3}
''')