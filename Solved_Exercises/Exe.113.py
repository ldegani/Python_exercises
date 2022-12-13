# 113 - Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor
#     jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa,
#     que será utilizado pelas telefonistas, para a computação dos votos. Para computar cada voto, a telefonista
#     digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. Um número de jogador igual zero,
#     indica que a votação foi encerrada. Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma
#     breve mensagem de aviso, e voltando a pedir outro número. Após o final da votação, o programa deverá exibir:
#     O total de votos computados; Os números e respectivos votos de todos os jogadores que receberam votos;
#     O percentual de votos de cada um destes jogadores; O número do jogador escolhido como o melhor jogador da partida,
#     juntamente com o número de votos e o percentual de votos dados a ele.
#     Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado
#     pelo número do jogador. O programa deve fazer uso de arrays.
#     Enquete: Quem foi o melhor jogador?
#
#     Número do jogador (0=fim): 9
#     Número do jogador (0=fim): 10
#     Número do jogador (0=fim): 9
#     Número do jogador (0=fim): 10
#     Número do jogador (0=fim): 11
#     Número do jogador (0=fim): 10
#     Número do jogador (0=fim): 50
#     Informe um valor entre 1 e 23 ou 0 para sair!
#     Número do jogador (0=fim): 9
#     Número do jogador (0=fim): 9
#     Número do jogador (0=fim): 0
#
#     Resultado da votação:
#
#     Foram computados 8 votos.
#
#     Jogador Votos           %
#     9               4               50,0%
#     10              3               37,5%
#     11              1               12,5%
#     O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.


votos = [0] * 23
soma_votos = 0
voto = 1

print('Enquete: Quem foi o melhor jogador?\n')

while voto != 0:
    voto = int(input('Número do jogador (0 = fim): '))

    if (voto < 0) or (voto > 23) or (voto == '') or (voto == ' '):
        print('Informe um valor entre 1 e 23 ou 0 para sair!')
    elif (voto != 0):
        indice = voto
        indice -= 1
        votos[indice] += 1
        soma_votos += 1

print(f'''
Resultado votação:
\nForam computados {soma_votos} votos.
\nJogador     Votos       %
''')

for i in range(0, 23):
    if votos[i] > 0:
        print(f'{i + 1}\t{votos[i]}\t{(votos[i] / soma_votos) * 100:.2f}%')

reverso = sorted(votos, reverse = True)

for i in range(0,23):
    if votos[i] == reverso[0]:
        print(f'\nO melhor jogador foi o número {i + 1}, com {reverso[0]} votos, '
              f'correspondendo a {(reverso[0] / soma_votos) * 100:.2f} % do total de votos.')
