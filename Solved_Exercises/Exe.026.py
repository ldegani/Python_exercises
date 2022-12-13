# 26 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve
#      comprar, sabendo que a decisão é sempre pelo mais barato.

n1 = float(input("Qual o valor do primeiro produto: "))
n2 = float(input("Qual o valor do segundo produto: "))
n3 = float(input("Qual o valor do terceiro produto: "))

if n1 < n2 and n1 < n3:
    print("Você deve comprar o primeiro produto, pois é o mais barato!")
elif n2 < n1 and n2 < n3:
    print("Você deve comprar o primeiro produto, pois é o mais barato!")
else:
    print("Você deve comprar o primeiro produto, pois é o mais barato!")
