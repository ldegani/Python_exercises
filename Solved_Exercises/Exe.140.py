# 140 - Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para
#     esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação
#     são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados.
#     Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.

palindro = input('Informe um palíndromo: ')

contra = palindro[::-1]

# Tira os espaços em branco caso seja uma frase
palindro = palindro.replace(' ', '')
contra = contra.replace(' ','')

if palindro.lower() == contra.lower():
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')
