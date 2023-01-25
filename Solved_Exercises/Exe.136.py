# 136 - Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.
#
#     F
#     FU
#     FUL
#     FULA
#     FULAN
#     FULANO

nome = input('Informe seu nome: ')

for i in range(0, len(nome)):
    print(nome[0:i+1].upper())