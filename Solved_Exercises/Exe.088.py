# 88 - O cardápio de uma lanchonete é o seguinte:
#     Especificação   Código  Preço
#     Cachorro Quente 100     R$ 1,20
#     Bauru Simples   101     R$ 1,30
#     Bauru com ovo   102     R$ 1,50
#     Hambúrguer      103     R$ 1,20
#     Cheeseburguer   104     R$ 1,30
#     Refrigerante    105     R$ 1,00
#     Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
#     Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.
#     Considere que o cliente deve informar quando o pedido deve ser encerrado.


codigo = 100
valor_total = 0

while codigo != 0:
    codigo = int(input('Informe o código do produto ou digite 0 (zero) para encerrar: '))

    if codigo != 0 :
        quantidade = int(input('Informe a quantidade deste produto: '))
        if codigo == 100:
            item = quantidade * 1.20
            print('Total de R$%.2f' %item)
        elif codigo == 101:
            item = quantidade * 1.30
            print('Total de R$%.2f' %item)
        elif codigo == 102:
            item = quantidade * 1.50
            print('Total de R$%.2f' %item)
        elif codigo == 103:
            item = quantidade * 1.20
            print('Total de R$%.2f' %item)
        elif codigo == 104:
            item = quantidade * 1.30
            print('Total de R$%.2f' %item)
        elif codigo == 105:
            item = quantidade * 1.00
            print('Total de R$%.2f' %item)
        valor_total += item

print('O total da compra é de: R$%.2f' %valor_total)
