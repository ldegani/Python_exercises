# 9 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura
# em graus Celsius.  C = 5 * ((F-32) / 9).

temperatura = float(input('Qual a temperatura (em Fahrenheit)? '))

celsius = 5 * ((temperatura - 32) / 9)

print('A temperatura em graus Celsius é ', celsius)
