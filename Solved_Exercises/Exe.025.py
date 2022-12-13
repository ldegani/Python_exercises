# 25 - Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
n3 = int(input("Terceiro número: "))
list = [n1, n2, n3]
maior = max(list)
menor = min(list)

print("O maior número é o %d e o menor é o %d" %(maior, menor))
