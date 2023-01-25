# 138 - Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data
#     com o nome do mês por extenso.
#     Data de Nascimento: 29/10/1973
#     Você nasceu em  29 de Outubro de 1973.

# Lista com meses
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
         'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

data = input('Informe a data no formato dd/mm/aaaa: ')

dia, mes, ano = map(int, data.split('/'))

print(f'{dia} de {meses[mes-1]} de {ano}')
