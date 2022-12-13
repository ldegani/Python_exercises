# 127 - Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado.
#     Por exemplo: 127 -> 721.

def reverso(num):
    print(num[::-1])

num = input('Informe um número: ')
reverso(num)
