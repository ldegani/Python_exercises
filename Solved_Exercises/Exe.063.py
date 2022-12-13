# 63 - Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

fact = int(input('Informe de qual número você quer o fatorial: '))
resp = 1
x = 1

if fact == 0:
    resp = 1

for i in range(0, fact):
    resp = x * resp
    x += 1

print(resp)