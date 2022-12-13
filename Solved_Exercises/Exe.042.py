# 43 - Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#     "Telefonou para a vítima?"
#     "Esteve no local do crime?"
#     "Mora perto da vítima?"
#     "Devia para a vítima?"
#     "Já trabalhou com a vítima?"
#     O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
#     Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
#     entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

print('Responda as perguntas a seguir com "sim" ou "não"')
p1 = input('Telefonou para a vítima: ')
p2 = input('Esteve no local do crime: ')
p3 = input('Mora perto da vítima: ')
p4 = input('Devia para a vítima: ')
p5 = input('Você já trabalhou com a vítima: ')
pall = (p1 + p2 + p3 + p4 + p5)

contador = pall.count('sim')

if contador == 5:
    print('Assassino')
elif contador > 2:
    print('Cúmplice')
elif contador == 2:
    print('Suspeito')
else:
    print('Inocente')
