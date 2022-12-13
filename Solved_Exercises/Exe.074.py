# 74 - Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs
#     e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

cds = int(input("Informe a quantidade de CD's da sua coleção: "))
cont, total, media = 0, 0, 0

while cont < cds:
    valor = float(input('Informe o valor do CD: '))
    total = total + valor
    cont += 1

media = total / cds

print(f'A soma do valor total é de R${total}, dando uma média de R${media} por CD.')