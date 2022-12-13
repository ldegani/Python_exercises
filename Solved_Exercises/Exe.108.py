# 108 - Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
#     Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
#     e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', ' Setembro',
         'Outubro', 'Novembro', 'Dezembro']
temperaturas = []

for i in range(0, 12):
    temperaturas.append(
        float(input(f"Digite a temperatura de {meses[i]} em ºC: "))
    )

media_temp = sum(temperaturas) / 12

print(f'A média de temperatura no ano foi de {media_temp} ºC.')
for i in range(0, 12):
    if temperaturas[i] > media_temp:
        print(f'{i+1} - {meses[i].capitalize()} com {temperaturas[i]:.2f}ºC')
