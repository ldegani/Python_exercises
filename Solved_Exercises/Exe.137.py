# 137 - Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.
#
# FULANO
# FULAN
# FULA
# FUL
# FU
# F

nome = input('Informe seu nome: ')

for i in range(len(nome), -1, -1):
    print(nome[0:i].upper())