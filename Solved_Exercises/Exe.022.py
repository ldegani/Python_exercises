# 22 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Informe uma letra: ")

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("A letra ", letra, " é uma vogal.")
else:
    print("A letra ", letra, " é uma consoante.")
