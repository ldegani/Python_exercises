# 73 - Faça um programa que calcule o número médio de alunos por turma.
#      Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
#      As turmas não podem ter mais de 40 alunos.

turmas = int(input('Informe a quantidade de turmas: '))
cont = 0
media = 0

while cont < turmas:
    alunos = int(input('Informe quantos alunos tem nesta sala: '))
    if alunos > 40:
        print('Quantidade errado, turma não pode ter mais de 40 alunos!')
    else:
        media = media + alunos
        cont += 1

media = round(media / turmas)

print(f'A média de alunos por sala é de {media} alunos.')
