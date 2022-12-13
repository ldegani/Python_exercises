# 114 - Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de
#     organizações:
#     "Qual o melhor Sistema Operacional para uso em servidores?"
#
#     As possíveis respostas são:
#
#     1- Windows Server
#     2- Unix
#     3- Linux
#     4- Netware
#     5- Mac OS
#     6- Outro
#     Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado
#     da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não
#     deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções
#     devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a
#     percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa,
#     e é o seguinte:
#     Sistema Operacional     Votos   %
#     -------------------     -----   ---
#     Windows Server           1500   17%
#     Unix                     3500   40%
#     Linux                    3000   34%
#     Netware                   500    5%
#     Mac OS                    150    2%
#     Outro                     150    2%
#     -------------------     -----
#     Total                    8800
#
#     O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.


print('Qual o melhor sistema operacional para uso em servidores?')
print('''
1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
''')

# Listas
sistemas = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']
votos = [0] * 6

# Variáveis
voto = 1
soma_votos, maior_voto = 0, 0

while voto != 0:
    voto = int(input('Informe seu voto: '))
    if (voto < 0) or (voto > 6) or (voto == '') or (voto == ' '):
        print('Voto inválido! Escolha uma opção entre 1 e 6!')
    elif voto == 0:
        print('Finalizado!')
    else:
        ind = voto - 1
        votos[ind] += 1
        soma_votos += 1


print('Sistema Operacional\t\tVotos\t\t%')
print('-------------------\t\t-----\t\t-')

for i in range(0, 6):
    print(f'{sistemas[i]}\t\t{votos[i]}\t\t{(votos[i] / soma_votos) * 100:.2f} %')

print('-------------------\t\t-----\t\t-')
print(f'Total\t\t{soma_votos}\t\t100%')

for i in range(0, 6):
    if (votos[i] > maior_voto):
        maior_voto = votos[i]
        ind_maior = i

print(f'O sistema operacional mais votado foi o {sistemas[ind_maior]}, com '
      f'{votos[ind_maior]} votos, correspondendo a '
      f'{(votos[ind_maior] / soma_votos) * 100:.2f} % dos votos.')
