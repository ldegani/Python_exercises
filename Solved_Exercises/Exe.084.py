# 84 - Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo
#     representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo.
#     Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

cont = 0
maior_altura, maior_aluno, menor_aluno = 0, 0, 0
menor_altura = 500


while cont < 10:
    aluno = int(input('Informe o número do aluno: '))
    altura = int(input('Informe a altura do aluno(em centímetros): '))
    cont += 1

    if altura > maior_altura:
        maior_altura = altura
        maior_aluno = aluno
    elif altura < menor_altura:
        menor_altura = altura
        menor_aluno = aluno

print(f'O maior aluno é o aluno de número {maior_aluno} e sua altura é de {maior_altura} centímetros')
print(f'O menor aluno é o aluno de número {menor_aluno} e sua altura é de {menor_altura} centímetros')
