# 103 - Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
#     Imprima a idade e a altura na ordem inversa a ordem lida.

idade, altura = [], []

for i in range(0, 5):
    idade.append(int(input('Informe a idade: ')))
    altura.append(int(input('Informe a altura: ')))

idade.reverse()
altura.reverse()

print(idade)
print(altura)
