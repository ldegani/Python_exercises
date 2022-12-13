# 128 - Jogo de Craps. Faça um programa que implemente um jogo de Craps. O jogador lança um par de dados, obtendo um
#     valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou
#     12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9
#     ou 10, este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente.
#     Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.

import random

def jogo():
    lancamento1 = random.randint(1, 6)
    lancamento2 = random.randint(1, 6)
    total = lancamento1 + lancamento2
    return total

acabou = False
quantidade_jogadas = 1
ponto = None

while not acabou:
    jogada = jogo()
    print(jogada)
    if quantidade_jogadas == 1:
        if (jogada == 7) or (jogada == 11):
            print(f'Seu lançamento deu {jogada}. \nVocê fez um natural! Ganhou! Parabéns!')
            acabou = True
        elif (jogada == 2) or (jogada == 3) or (jogada == 12):
            print(f'Seu lançamento deu {jogada}. \nVocê fez um craps! Perdeu! Tente novamente!')
            acabou = True
        else:
            print(f'Sua primeira jogada foi um total de: {jogada} pontos')
            ponto = jogada
    else:
        if ponto == jogada:
            print('Parabéns! Você ganhou!')
            acabou = True
        elif jogada == 7:
            print('Você perdeu! Tente novamente')
            acabou = True
    quantidade_jogadas += 1
