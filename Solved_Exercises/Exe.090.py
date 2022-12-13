# 90 - Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões.
#     O programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e
#     assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa).
#     Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema.
#     Após todos os alunos terem respondido informar:
#     Maior e Menor Acerto;
#     Total de Alunos que utilizaram o sistema;
#     A Média das Notas da Turma.
#
#     Gabarito da Prova:
#     01 - A / 02 - B / 03 - C / 04 - D / 05 - E / 06 - E / 07 - D / 08 - C / 09 - B / 10 - A

sist = 's'
acertos, alunos, notas = 0, 0, 0

while sist.lower() == 's':
    resp1 = input('Resposta questão 1: ').upper()
    if resp1 == 'A':
        acertos += 1
    resp2 = input('Resposta questão 2: ')
    if resp2 == 'B':
        acertos += 1
    resp3 = input('Resposta questão 3: ')
    if resp3 == 'C':
        acertos += 1
    resp4 = input('Resposta questão 4: ')
    if resp4 == 'D':
        acertos += 1
    resp5 = input('Resposta questão 5: ')
    if resp5 == 'E':
        acertos += 1
    resp6 = input('Resposta questão 6: ')
    if resp6 == 'E':
        acertos += 1
    resp7 = input('Resposta questão 7: ')
    if resp7 == 'D':
        acertos += 1
    resp8 = input('Resposta questão 8: ')
    if resp8 == 'C':
        acertos += 1
    resp9 = input('Resposta questão 9: ')
    if resp9 == 'B':
        acertos += 1
    resp10 = input('Resposta questão 10: ')
    if resp10 == 'A':
        acertos += 1

    print(f'Total de acertos: {acertos}')

    alunos += 1
    notas += acertos

    if ('maior' not in vars()) or (acertos > maior):
        maior = acertos
    if ('menor' not in vars()) or (acertos < menor):
        menor = acertos

    sist = input('Você quer cadastrar a resposta de outro aluno (s/n): ')

media = notas / alunos


print(f'Total de alunos: {alunos}')
print(f'Média de notas da turma: {media}')
print(f'Maior nota: {maior}')
print(f'Menor nota: {menor}')
