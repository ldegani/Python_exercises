# 99 - Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

lst = []
count = 0

for i in range(6):
    letra = (input('Informe um caractere(letra): ')).lower()
    if letra != 'a' and letra != 'e' and letra != 'i' and letra != 'o' and letra != 'u':
        lst.append(letra)
        count += 1

print(lst)
print(count)
