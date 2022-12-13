# 85 - Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito.
#     Foram obtidos os seguintes dados:
#     Código da cidade;
#     Número de veículos de passeio (em 1999);
#     Número de acidentes de trânsito com vítimas (em 1999).
#     Deseja-se saber:
#         Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
#         Qual a média de veículos nas cinco cidades juntas;
#         Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

cont, cont_acid = 0, 0
maior_acid, cod_maior_acid, cod_menor_acid = 0, 0, 0
menor_acid = 10000000000
media_veic = 0
media_acid = 0

while cont < 5:
    cod = int(input('Qual o código da cidade: '))
    num_veic = int(input('Qual o número de veículos de passeio: '))
    num_acid = int(input('Qual o número de acidentes com vítimas: '))
    cont += 1
    media_veic += num_veic

    if num_acid > maior_acid:
        maior_acid = num_acid
        cod_maior_acid = cod
    elif num_acid < menor_acid:
        menor_acid = num_acid
        cod_menor_acid = cod

    if num_veic < 2000:
        media_acid += num_acid
        cont_acid += 1

media_veic = media_veic / cont
media_acid = media_acid / cont_acid

print(f'Cidade com mais acidentes cód: {cod_maior_acid}, total de {maior_acid} acidentes.')
print(f'Cidade com menos acidentes cód: {cod_menor_acid}, total de {menor_acid} acidentes.')
print(f'A média de veículos nas cinco cidades é de {media_veic}.')
print(f'A média de acidentes nas cidades com menos de 2000 veículos é de {media_acid} acidentes.')
