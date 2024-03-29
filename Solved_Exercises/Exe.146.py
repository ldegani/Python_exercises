# 146 - Leet spek generator. Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das
#     letras, como números por exemplo. A própria palavra leet admite muitas variações, como l33t ou 1337. O uso do leet
#     reflete um subcultura relacionada ao mundo dos jogos de computador e internet, sendo muito usada para confundir os
#     iniciantes e afirmar-se como parte de um grupo. Pesquise sobre as principais formas de traduzir as letras. Depois,
#     faça um programa que peça uma texto e transforme-o para a grafia leet speak.

# Dicionário com letras leet
leet = {
    'A': '4',
    'B': '8',
    'C': '<',
    'Ç': 'Ç',
    'D': '[)',
    'E': '&',
    'F': 'ph',
    'G': '6',
    'H': '#',
    'I': '1',
    'J': 'j',
    'K': '|<',
    'L': '|_',
    'M': '|\/|',
    'N': '/\/',
    'O': '0',
    'P': '|*',
    'Q': '9',
    'R': 'l2',
    'S': '5',
    'T': '7',
    'U': 'v',
    'V': 'V',
    'W': 'vv',
    'X': '><',
    'Y': '`/',
    'Z': '2'
}

# Entrada do texto
texto = input('Informe o texto que você quer transformar: ').upper()
l_texto = list(texto)

for i in l_texto:
    if i.isalpha():
       print(leet[i], end='')
    elif i == ' ':
        print(' ', end='')
    else:
        ''
print(f'\n{texto}')