# 129 - Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no
#     formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

import re

# Lista com meses
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
         'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']


def valida_data(dia, mes, ano):
    # Valida o dia
    if (dia < 0) or (dia > 31):
        return False

    # Valida os meses
    if (mes < 0) or (mes > 12):
        return False

    # Valida mês com 30 dias
    mes30 = (4, 6, 9, 11)
    if mes in mes30:
        if dia > 30:
            return False

    # Valida Fevereiro e ano bissexto
    if mes == 2:
        if dia > 28:
            if ano % 4 != 0:
                return False
            elif (ano % 100 == 0) and (ano % 1000 != 0):
                return False

    return True


def mes_extenso(data):
    # valida o formato da data por extenso regular
    reg = re.compile('^[0-9]{2}/[0-9]{2}/[0-9]{4}$')
    if not (reg.match(data)):
        print('Data inválida!')
        return None

    if not (valida_data(dia, mes, ano)):
        print('Data inválida')
        return None

    return f'{dia} de {meses[mes - 1]} de {ano}'


# Fluxo principal
data = input('Informe a data(dd/mm/aaa): ')
dia, mes, ano = map(int, data.split('/'))

print(mes_extenso(data))
