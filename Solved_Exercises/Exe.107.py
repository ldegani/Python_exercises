# 107 - Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com
#     mais de 13 anos possuem altura inferior à média de altura desses alunos.

idade, altura = [], []
soma,cont, j = 0, 0, 0

for i in range(0, 5):
    idade.append(int(input('Qual a idade do aluno: ')))
    altura.append(int(input('Qual a altura do aluno(em centímetros): ')))

for i in altura:
    soma += i

media = soma / len(altura)

for id in idade:
    if (id > 13) and (altura[j] <= media):
        cont +=1
    j += 1

print(soma)
print(media)
print(len(altura))
print(cont)
