# 148 - A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de
#     arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos
#     usuarios, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele
#     conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
#     alexandre       456123789
#     anderson        1245698456
#     antonio         123456456
#     carlos          91257581
#     cesar           987458
#     rosemary        789456125
#     Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que
#     gere um relatório, chamado "relatório.txt", no seguinte formato:
#     ACME Inc.               Uso do espaço em disco pelos usuários
#     ------------------------------------------------------------------------
#     Nr.  Usuário        Espaço utilizado     % do uso
#
#     1    alexandre       434,99 MB             16,85%
#     2    anderson       1187,99 MB             46,02%
#     3    antonio         117,73 MB              4,56%
#     4    carlos           87,03 MB              3,37%
#     5    cesar             0,94 MB              0,04%
#     6    rosemary        752,88 MB             29,16%
#
#     Espaço total ocupado: 2581,57 MB
#     Espaço médio ocupado: 430,26 MB
#     O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de
#     forma a agilizar a execução do programa. A conversão do espaço ocupado em disco, de bytes para megabytes deverá
#     ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de
#     uso também deverá ser feito através de uma função, que será chamada pelo programa principal.


# Le o arquivo
arquivo = open('Usuarios.txt', 'r')

# Coloca a informação do arquivo na memória
usuarios = arquivo.readlines()

# Fecha o arquivo
arquivo.close()

# Cria um dicionário vazio
dicionario = {}


# Coloca os dados do arquivo em um dicionário com chave:valor
for lines in usuarios:
    line = lines.split()
    dicionario[line[0]] = int(line[1])


# Função para converter bytes em megabytes e gravar no dicionário corretamente
def converte(dicionario):
    for chave in dicionario:
        mb = round(dicionario[chave] / 1048576, 2)
        dicionario[chave] = mb


def percentual(dicionario):
    soma = 0
    for i in dicionario:
        soma += dicionario[i]

    percent = 0
    num = 1
    for j in dicionario:
        percent = round((dicionario[j] / soma) * 100, 2)
        arq_Saida.write(f'\n{num}   {j}      {dicionario[j]} MB      {percent} %')
        num += 1

    tam = len(dicionario)
    arq_Saida.write(
        f'\nEspaço total ocupado: {soma:.2f} MB'
        f'\nEspaço médio ocupado: {soma/tam:.2f} MB'
    )

# Chama a função com o dicionário como parâmetro
converte(dicionario)

# Abre o arquivo pra saida
arq_Saida = open('Saida_Usuarios.txt', 'w')

arq_Saida.write(
    'ACME Inc.             Uso do espaco em disco pelos usuarios\n'
'------------------------------------------------------------------------'
    '\nNr.  Usuario        Espaco utilizado      % do uso'
)

# Chama a função de percentual, com o dicionário como parâmetro
percentual(dicionario)

arq_Saida.close()