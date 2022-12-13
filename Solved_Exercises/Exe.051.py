# 51 - Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
#      Valide a entrada e permita repetir a operação.

# Inicia variáveis
pop_A, pop_B, taxa_A, taxa_B, ano = 0, 0, 0, 0, 0

# Solicita e verifica as informações
while pop_A <= 0:
    pop_A = int(input('Informar a população da cidade A: '))
    if pop_A <= 0:
        print('A população deve ser maior do que zero!')
while taxa_A <= 0:
    taxa_A = float(input('Informar a taxa de crescimento da cidade A(em %): '))
    if taxa_A <= 0:
        print('A taxa de crescimento deve ser maior do que zero!')
while pop_B <= pop_A:
    pop_B = int(input('Informar a população da cidade B: '))
    if pop_B <= pop_A:
        print('A população deve ser maior do que a da cidade A!')

# Deixa as taxas iguais para poder fazer o loop e o if
taxa_B = taxa_A
while taxa_B >= taxa_A:
    taxa_B = float(input('Informar a taxa de crescimento da cidade B(em %): '))
    if taxa_B >= taxa_A:
        print('A taxa de crescimento deve ser menor do que a taxa da cidade A!')

    # Transforma as taxas em número inteiros para cálculo
taxa_A = taxa_A / 100
taxa_B = taxa_B / 100

# Cálculo das taxas até que a uma cidade ultrapasse a outra
while pop_A <= pop_B:
    pop_A = round(pop_A + (pop_A * taxa_A))
    pop_B = round(pop_B + (pop_B * taxa_B))
    ano = ano + 1

print(f'Levará {ano} anos para que a cidada A tenha uma população igual ou maior a cidade B')
print(f'População cidade A: {pop_A}')
print(f'População cidade B: {pop_B}')
