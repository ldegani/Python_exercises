# 89 - Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código.
#     Os códigos utilizados são:
#     1 , 2, 3, 4  - Votos para os respectivos candidatos
#     (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
#     5 - Voto Nulo
#     6 - Voto em Branco
#     Faça um programa que calcule e mostre:
#     O total de votos para cada candidato;
#     O total de votos nulos;
#     O total de votos em branco;
#     A percentagem de votos nulos sobre o total de votos;
#     A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.

print('''Candidatos a eleição:
1 - Lucas / 2 - Luiza / 3 - Bruna / 4 - Marcos
5 - Voto Nulo / 6 - Voto em Branco / 0 - para finalizar''')

cand = 1
cand1, cand2, cand3, cand4, total_votos = 0, 0, 0, 0, 0
nulo, branco = 0, 0

while cand != 0:
    cand = int(input('Informe qual seu voto: '))

    if cand > 6:
        print('Você é burro! Não tem essa opção!')

    if (cand > 0) and (cand < 6):
        total_votos += 1

    if cand == 1:
        cand1 += 1
    elif cand == 2:
        cand2 += 1
    elif cand == 3:
        cand3 += 1
    elif cand == 4:
        cand4 += 1
    elif cand == 5:
        nulo += 1
    elif cand == 6:
        branco += 1


print(f'''Tivemos um total de {total_votos} votos.
Candidato 1: {cand1} votos
Candidato 2: {cand2} votos
Candidato 3: {cand3} votos
Candidato 4: {cand4} votos
Nulo: {nulo} votos sendo um total de {(nulo / total_votos) * 100}%
Branco: {branco} votos, sendo um total de {(branco / total_votos) * 100}%
''')
