# 105 - Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
#     cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

vet1, vet2, vet3, = [], [], []

for i in range(0, 10):
    vet1.append(int(input('Informe um valor inteiro para o primeiro vetor: ')))

for i in range(0, 10):
    vet2.append(int(input('Informe um valor inteiro para o segundo vetor: ')))

for i in range(0, 10):
    vet3.append(vet1[i])
    vet3.append(vet2[i])

print(vet1)
print(vet2)
print(vet3)
