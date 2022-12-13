# 36 - Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

uData = input('Informe a data(dd/mm/aaaa): ')

# faz o split do input e transforma em número
dia, mes, ano = map(int, uData.split("/"))

if mes > 12:
    print('Não é uma data válida!')
    exit()

if mes == 2:
    if (ano % 4 == 0) and (ano % 4 != 0 or ano % 400 ==0) and (dia <= 29):
        print('É uma data válida!')
    elif dia <= 28:
        print('É uma data válida!')
    else:
        print('Não é uma data válida!')
    exit()

if mes in (1, 3, 5, 7, 9, 11): #mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 9 or mes == 11:
    if dia <= 31:
        print('É uma data válida!')
    else:
        print('Não é uma data válida!')
    exit()
elif dia <= 30:
    print('É uma data válida!')
else:
    print('Não é uma data válida!')
