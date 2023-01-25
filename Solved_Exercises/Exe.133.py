# 133 - Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
#     Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
#
#     Compara duas strings
#     String 1: Brasil Hexa 2026
#     String 2: Brasil! Hexa 2026!
#     Tamanho de "Brasil Hexa 2026": 16 caracteres
#     Tamanho de "Brasil! Hexa 2026!": 18 caracteres
#     As duas strings são de tamanhos diferentes.
#     As duas strings possuem conteúdo diferente.

str1 = 'Brasil Hexa 2026'
str2 = 'Brasil! Hexa 2026!'

l1 = len(str1)
l2 = len(str2)

print(f'A string: "{str1}" tem {l1} caracteres.')
print(f'A string: "{str2}" tem {l2} caracteres.')

if l1 != l2:
    print('As strings são de tamanhos diferente.')

if str1 != str2:
    print('As strings possuem conteúdos diferente.')
