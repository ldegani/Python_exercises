# 79 - O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia um conjunto
#      indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas,
#      bem como a média das temperaturas.

n = int(input('Quantas temperaturas você gostaria de informar: '))
cont = 0
tmax, tmin, tmed = 0, 0, 0

while cont < n:
    t = float(input('Informe a temperatura: '))
    cont += 1
    tmed += t

    if t < tmax:
        tmax = t
    elif t < tmin:
        tmin = t

tmed = tmed / n

print(f'{tmax}, {tmin}, {tmed}')


