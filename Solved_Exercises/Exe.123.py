# 123 - Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto,
#     que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto.
#     A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxaImposto, custo):
    print(taxaImposto * custo + custo)

taxaImposto = float(input('Informe o valor do imposto (em %): '))
custo = float(input('Informe o custo do produto: '))

somaImposto(taxaImposto, custo)
