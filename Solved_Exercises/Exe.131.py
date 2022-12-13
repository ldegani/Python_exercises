# 131 - Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função
#     deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor
#     máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de
#     forma elegante.

def retangulo(linhas, colunas):
    conta = linhas + 2
    print('+ ' + '-' * linhas + ' +')
    for i in range(colunas):
        print('|' + ' ' * conta + '|')
    print('+ ' + '-' * linhas + ' +')


linhas = int(input('Informe o tamanho de linhas: '))
colunas = int(input('Informe o tamanho das colunas: '))

if linhas < 1:
    linhas = 1
elif linhas > 20:
    linhas = 20

if colunas < 1:
    colunas = 1
elif colunas > 20:
    colunas = 20

retangulo(linhas, colunas)
