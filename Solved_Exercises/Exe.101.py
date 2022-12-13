# 101 - Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
#     imprima o número de alunos com média maior ou igual a 7.0.

v_media, v_media_maior = [], []

for i in range(1, 4):
    print(f'Aluno {i}')
    media = 0
    for j in range(0, 4):
        nota = float(input('Informe a nota: '))
        media += nota

    media = media / 4
    v_media.append(media)
    if media >= 7:
        v_media_maior.append(media)

count = len(v_media_maior)

print(v_media)
print(v_media_maior)
print(count)
