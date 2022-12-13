# 132 - Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no
#     qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números
#     de 1 a 9:
#
#     8  3  4    [0, 1, 2]
#     1  5  9    [3, 4, 5]
#     6  7  2    [6, 7, 8]
#     Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima.
#     Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. Usar um vetor de
#     1 a 9 parece ser mais simples que usar uma matriz 3x3.

vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def quadrado_magico():
    for i in vetor:

