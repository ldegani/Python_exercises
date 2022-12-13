# 45 - Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                           Até 5 Kg           Acima de 5 Kg
#     Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#     Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#     Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um
#     desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade
#     (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.


# Variables
strawberry = int(input('Inform the quantity of strawberrys bought(kg):' ))
apple = int(input('Inform the quantity of apples bought(kg): '))

if strawberry <= 5:
    strawberry_Price = strawberry * 2.5
else:
    strawberry_Price = strawberry* 2.20

if apple <= 5:
    apple_Price = apple * 1.8
else:
    apple_Price = apple * 1.5

if (strawberry + apple) > 8 or (strawberry_Price + apple_Price) > 25:
    final_Price = (strawberry_Price + apple_Price) * 0.9
else:
    final_Price = strawberry_Price + apple_Price

print(f'The total price is: R${final_Price}')
