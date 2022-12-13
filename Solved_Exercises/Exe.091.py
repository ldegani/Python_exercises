# 91 - Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
#     No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados.
#     O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa que receba a
#     nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos conforme a
#     descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). Os saltos são informados
#     na ordem da execução, portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta.
#     A saída do programa deve ser conforme o exemplo abaixo:
#     Atleta: Rodrigo Curvêllo
#     Primeiro Salto: 6.5 m
#     Segundo Salto: 6.1 m
#     Terceiro Salto: 6.2 m
#     Quarto Salto: 5.4 m
#     Quinto Salto: 5.3 m
#     Melhor salto:  6.5 m
#     Pior salto: 5.3 m
#     Média dos demais saltos: 5.9 m
#     Resultado final:
#     Rodrigo Curvêllo: 5.9 m

atleta = ' '
maior_salto, menor_salto = 0, 50

while atleta != '':
    atleta = input('Atleta: ')

    if atleta != '':
        salto1 = float(input('Primeiro salto: '))
        salto2 = float(input('Segundo salto: '))
        salto3 = float(input('Terceiro salto: '))
        salto4 = float(input('Quarto salto: '))
        salto5 = float(input('Quinto salto: '))

        soma_saltos = salto1 + salto2 + salto3 + salto4 + salto5

        if salto1 > maior_salto:
            maior_salto = salto1
        if salto2 > maior_salto:
            maior_salto = salto2
        if salto3 > maior_salto:
            maior_salto = salto3
        if salto4 > maior_salto:
            maior_salto = salto4
        if salto5 > maior_salto:
            maior_salto = salto5

        if salto1 < menor_salto:
            menor_salto = salto1
        if salto2 < maior_salto:
            menor_salto = salto2
        if salto3 < maior_salto:
            menor_salto = salto3
        if salto4 < maior_salto:
            menor_salto = salto4
        if salto5 < maior_salto:
            menor_salto = salto5

        soma_saltos = soma_saltos - maior_salto - menor_salto

        print('A soma dos saltos é de: %.2f m' %soma_saltos)
        print('Melhor salto: %.2f m' %maior_salto)
        print('Pior salto: %.2f m' %menor_salto)
        print('Média dos demais saltos: %.2f m' %((soma_saltos) / 3))
        print('%s : %.2f m' %(atleta, (soma_saltos / 3)))
