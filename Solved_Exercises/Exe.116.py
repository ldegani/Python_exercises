# Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL,
#     VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses
#     carros faz com um litro de combustível. Calcule e mostre:
#     O modelo do carro mais econômico;
#     Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000
#     quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela
#     de exemplo. A disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e
#     podem mudar a cada execução do programa.
#     Comparativo de Consumo de Combustível
#
#     Veículo 1
#     Nome: fusca
#     Km por litro: 7
#     Veículo 2
#     Nome: gol
#     Km por litro: 10
#     Veículo 3
#     Nome: uno
#     Km por litro: 12.5
#     Veículo 4
#     Nome: Vectra
#     Km por litro: 9
#     Veículo 5
#     Nome: Peugeout
#     Km por litro: 14.5
#
#     Relatório Final
#      1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
#      2 - gol             -   10.0 -  100.0 litros - R$ 225.00
#      3 - uno             -   12.5 -   80.0 litros - R$ 180.00
#      4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
#      5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
#     O menor consumo é do peugeout.


CARRO, CONSUMO = [], []
GASOLINA = 2.25

for i in range(1, 6):
    print(f'Veículo {i}')
    CARRO.append(input(f'Nome: '))
    CONSUMO.append(float(input('Km por litro: ')))

print('Relátorio Final: \n')
for i in range(0, 5):
    DISTANCIA = 1000 / CONSUMO[i]
    GASTO = DISTANCIA * GASOLINA
    print(f'{i + 1} - {CARRO[i]}  - {CONSUMO[i]} km/L \t{DISTANCIA:.1f} litros  \t R$ {GASTO:.2f}')
    if ('MENOR_CONSUMO' not in vars()) or (CONSUMO[i] > CONSUMO[MENOR_CONSUMO]):
        MENOR_CONSUMO = i

print(f'\nO menor consumo é do {CARRO[MENOR_CONSUMO]}')
