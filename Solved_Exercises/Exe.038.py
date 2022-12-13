# 38 - Faça um Programa para leitura de três notas parciais de um aluno.
#     O programa deve calcular a média alcançada por aluno e presentar:
#     A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#     A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#     A mensagem "Aprovado com Distinção", se a média for igual a 10.

notas = input('Informe as 3 notas paricias (n1, n2, n3): ')

n1, n2, n3 = map(float, notas.split(','))

media = round((n1 + n2 + n3) / 3, 2)

if (media == 10):
    print(f'Aprovado com distinção! Média {media}')
elif (media >= 7):
    print(f'Aprovado com média {media}!')
else:
    print(f'Reprovado com média {media}')
