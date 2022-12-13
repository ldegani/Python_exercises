# 24 - Faça um Programa que leia três números e mostre o maior deles.

num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))
num3 = float(input("Infome o terceiro número: "))

if num1 > num2 and num1 > num3:
    print("O primeiro número informaco, número ", num1, ", é o maior número entre eles.")
elif num2 > num1 and num2 > num3:
    print("O segundo número informado, número ", num2,", é o maior número entre eles.")
else:
    print("O terceiro nmero informado, número ", num3, ", é o maior número entre eles.")
