# 11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite um número real: '))

r1 = (n1 * 2) / (n2 / 2)
r2 = (3 * n1) + n3
r3 = (n3 ** 3)

print('Os resultados são: %d, %d e %d' % (r1, r2, r3))
