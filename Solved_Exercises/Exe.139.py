# 139 - Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco),
#     conte:
#
#     quantos espaços em branco existem na frase.
#     quantas vezes aparecem as vogais a, e, i, o, u.

conta_vogais = 0

frase = input('Digite uma frase: ')

espacos = frase.count(' ')


for i in frase.lower():
    if i in "aeiou":
        conta_vogais += 1

print(espacos)
print(conta_vogais)
