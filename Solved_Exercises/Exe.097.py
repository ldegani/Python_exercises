# 97 - Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

# Inicia lista vazia
vet = []

# Loop para solicitar os valores
for i in range(0, 10):
    vet.append(int(input('Informe um valor inteiro: ')))

print(vet[::-1])

# Outro modo, usando método de lista:
vet.reverse()
print(vet)
