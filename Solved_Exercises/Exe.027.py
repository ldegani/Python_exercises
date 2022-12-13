# 27 - Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
n3 = int(input("Terceiro número: "))
num = [n1, n2, n3]
num.sort(reverse= True)

print(f'Os números em ordem decrescente são: {num}.')
