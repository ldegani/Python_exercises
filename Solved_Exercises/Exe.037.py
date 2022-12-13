# 37 - Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e
#      unidades do mesmo.
#      Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#      326 = 3 centenas, 2 dezenas e 6 unidades
#      12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

# input
numero = int(input('Informe um número inteiro, positivo, menor ou igual a 1000: '))

# cálculos
uni = int(numero % 10)
dez = int(((numero - uni) / 10) % 10)
cent = int(numero / 100)

# inicia a string
saida = 'O número possui '

# verificações
if (cent > 0):
    saida = saida + str(cent)
    if (cent > 1):
        saida = saida + ' centenas '
    else:
        saida = saida + ' centena '

if (dez > 0):
    if (uni == 0) and (cent != 0):
        saida = saida + ' e '
    saida = saida + str(dez)
    if (dez > 1):
        saida = saida + ' dezenas '
    else:
        saida = saida + ' dezena '

if (uni > 0):
    if (cent != 0) or (dez != 0):
        saida = saida + ' e '
    saida = saida + str(uni)
    if (uni > 1):
        saida = saida + ' unidades'
    else:
        saida = saida + ' unidade'

print (saida)
