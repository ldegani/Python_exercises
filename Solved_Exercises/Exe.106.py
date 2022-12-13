# 106 - Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

vet1, vet2, vet3, vet4 =[], [], [], []

print('Montando vetor 1')
for i in range(0, 10):
    vet1.append(int(input('Informe um valor inteiro: ')))

print('Montando vetor 2')
for i in range(0, 10):
    vet2.append(int(input('Informe um valor inteiro: ')))

print('Montando vetor 3')
for i in range(0, 10):
    vet3.append(int(input('Informe um valor inteiro: ')))

for i in range(0, 10):
    vet4.append(vet1[i])
    vet4.append(vet2[i])
    vet4.append(vet3[i])

print(vet1)
print(vet2)
print(vet3)
print(vet4)
