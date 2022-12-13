# 13 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu
#      peso ideal, utilizando as seguintes fórmulas:
#      Para homens: (72.7*h) - 58
#      Para mulheres: (62.1*h) - 44.7

sexo = input('Você é homem ou mulher? (h/m): ')
altura = float(input('Digite sua altura em metros: '))
peso = float(input('Informe seu peso (em kg): '))

if sexo == "h":
    pideal = (72.7 * altura) -58
else:
    pideal = (62.1 * altura) - 44.7

if pideal > peso:
    print('Você está acima do seu peso ideal, que seriam %dkgs.', %pideal)
else pideal <= peso:
    print('Você está dentro do seu peso ideal, que seria de até %dkgs.', %pideal)
