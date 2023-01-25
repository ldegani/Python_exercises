# 143 - Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e
#     escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.
#
#     Digite uma letra: A
#     -> Você errou pela 1ª vez. Tente de novo!
#
#     Digite uma letra: O
#     A palavra é: _ _ _ _ O
#
#     Digite uma letra: E
#     A palavra é: _ E _ _ O
#
#     Digite uma letra: S
#     -> Você errou pela 2ª vez. Tente de novo!

from random import randint

# Abre o arquivo
arquivo = open('Palavras.txt', 'r')

# Salva todas as palavras
palavras = arquivo.readlines()

# Fecha o arquivo
arquivo.close()

# Seleciona uma palavra aleatória da lista de palavras
palavra = palavras[randint(0, len(palavras) - 1)].upper().strip()

# Cria uma lista com as letras da palavra
lst_palavra = list(map(str, palavra))

# Variável para saber o tamanho da palavra
tam = len(lst_palavra)

# Inicia as listas
letras_usadas = []
forca = ['_'] * tam

# Inicia variáveis
acertos, erros = 0, 0
chances = 6

while acertos != tam:
    for i in forca:
        print(f'{i} ', end='')

    letra = input('\nDigite uma letra: ').upper()

    # Verifica se a letra já foi digitada
    if letra not in letras_usadas:
        letras_usadas.append(letra)

        if letra in lst_palavra:
            conta_letra = lst_palavra.count(letra)
            acertos += conta_letra
            for i in range(conta_letra):
                ind = lst_palavra.index(letra)
                forca[ind] = letra
                lst_palavra[ind] = ('..')
            # Mensagem caso ganhe!
            if acertos == tam:
                print('Parabéns! Você acertou a palavra e ganhou!')
                print('A palavra era: ')
                for i in forca:
                    print(f'{i} ', end='')

        else:
            erros += 1
            print(erros)
            if erros < chances:
                print(f'--> Você errou pela {erros}ª vez. Você ainda tem {chances - erros} tentativas!')

            # Mensagem caso perca!
            if erros == chances:
                print('-- > Você errou o máximo de tentativas possíveis, foi enforcado!')
                exit()
    else:
        print('Você já tentou esta letra, tente outra!')
