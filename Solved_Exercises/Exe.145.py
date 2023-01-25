# 145 - Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será
#     mostrada com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá
#     uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser
#     mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.

from random import sample
from random import randint

# Abre o arquivo para leitura
arquivo = open('Palavras.txt', 'r')

# Pega todas as palavras e coloca na memória
palavras = arquivo.readlines()

# Fecha o arquivo
arquivo.close()

# Seleciona uma palavra aleatória da lista de palavras
palavra = palavras[randint(0, len(palavras) -1)].upper().strip()

embaralhada = ''.join(sample(palavra, len(palavra)))

print(f'A palavra embaralha é: {embaralhada}')
print('Você tem 6 tentativas para tentar acertar.')

tentativas = 0

while tentativas != 6:
    jogada = input('Qual a palavra: ')
    jogada = jogada.upper()
    if jogada == palavra:
        print('Parabéns! Você acertou a palavra!')
        break
    else:
        tentativas += 1
        print(f'Esta é sua tentativa número {tentativas}')

    if tentativas == 6:
        print('Você errou 6 vezes e perdeu!')
        print(f'A palavra era: {palavra}')
