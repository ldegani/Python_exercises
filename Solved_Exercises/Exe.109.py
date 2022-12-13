# 109 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#     "Telefonou para a vítima?"
#     "Esteve no local do crime?"
#     "Mora perto da vítima?"
#     "Devia para a vítima?"
#     "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no
#     crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
#     entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

resp = []

print('Responda as perguntas a seguir com "S" para sim ou "N" para não.')
resp.append(input('Telefonou para a vítima? '))
resp.append(input('Esteve no local do crime? '))
resp.append(input('Mora perto da vítima? '))
resp.append(input('Devia para a vítima? '))
resp.append(input('Já trabalhou com a vítima? '))

resp = [element.upper() for element in resp]
count = resp.count('S')

if count <= 2:
    print('Classificação: Suspeita!')
elif count <= 4:
    print('Classificação: Cúmplice!')
elif count == 5:
    print('Classificação: Assassino!')
else:
    print('Classificação: Inocente!')
