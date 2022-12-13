# 46 - O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                           Até 5 Kg           Acima de 5 Kg
#     File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#     Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#     Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#     Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
#     porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o
#     cliente receberá ainda um desconto de 5% sobre o total da compra.
#     Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
#     contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do
#     desconto e valor a pagar.

# Variáveis
tipo_carne = input('Informe o tipo da carne entre File Duplo, Alcatra ou Picanha: ')
quantidade_carne = float(input('Informe a quantidade total: '))
cartao = input('Cliente possui o cartão Tabajara? ')

if tipo_carne == 'File Duplo':
    if quantidade_carne <= 5:
        preco = quantidade_carne * 4.9
    else:
        preco = quantidade_carne * 5.8
elif tipo_carne == 'Alcatra':
    if quantidade_carne <= 5:
        preco = quantidade_carne * 5.9
    else:
        preco = quantidade_carne * 6.80
elif tipo_carne == 'Picanha':
    if quantidade_carne <= 5:
        preco = quantidade_carne * 6.9
    else:
        preco = quantidade_carne * 7.8
else:
    print('Dados inválidos!')
    exit()

if cartao == 'Sim' or cartao == 'sim':
    preco_desc = preco * 0.05
else: preco_desc = 0.00

print(f'''
Tipo da carne: {tipo_carne};
Quantidade: {quantidade_carne};
Total: R${preco};
Desconto: R${preco_desc};
Total a pagar: R${preco - preco_desc}.
''')
