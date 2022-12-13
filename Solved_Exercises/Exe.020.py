# 20 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num = float(input("Informe um número: "))

if num > 0:
    print("O número ", num, " é positivo!")
elif num < 0:
    print("O número ", num, " é negativo!")
else:
    print("O número ", num, " é zero e zero não existe negativo ou positivo!")
