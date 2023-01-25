# 141 - Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato
#     xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da validação dos dígitos verificadores e dos
#     caracteres de formatação.

import re


def verifica(cpf):
    soma = 0
    for i in range(0, 9):
        valor = num_cpf[i] * (10 - i)
        soma += valor
    mod = soma % 11
    dig1 = 11 - mod
    if dig1 >= 10:
        dig1 = 0

    if dig1 == num_cpf[9]:
        soma2 = 0
        for j in range(0, 10):
            valor2 = num_cpf[j] * (11 - j)
            soma2 += valor2
        mod2 = soma2 % 11
        dig2 = 11 - mod2
        if dig2 >= 10:
            dig2 = 0
        if dig2 == num_cpf[10]:
            print('CPF é válido!')
        else:
            print('CPF inválido!')
    else:
        print('CPF inválido!')
        exit()


# Entrada dos dados
cpf = input('Informe seu cpf(formato xxx.xxx.xxx-xx): ')
# Verificar se o CPF foi digitado num formato válido
x_cpf = re.search('^[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}$', cpf)
if x_cpf:
    print('Entrada válida!')
else:
    print('Entrada incorreta!')
    exit()

# Retorna apenas os digitos da string e coloca numa lista
num_cpf = re.findall('\d', cpf)
# Transforma a lista de string para int
num_cpf = list(map(int, num_cpf))

print(num_cpf)
verifica(cpf)
