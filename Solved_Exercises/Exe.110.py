# 110 - Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
#     encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).
#     Após esta entrada de dados, faça:
#     Mostre a quantidade de valores que foram lidos;
#     Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
#     Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
#     Calcule e mostre a soma dos valores;
#     Calcule e mostre a média dos valores;
#     Calcule e mostre a quantidade de valores acima da média calculada;
#     Calcule e mostre a quantidade de valores abaixo de sete;
#     Encerre o programa com uma mensagem;

nota = None
notas = []

print('Para finalizar, digite a nota: "-1"')
while nota != -1:
    nota = int(input('Informe a nota: '))
    notas.append(nota)

del notas[-1]

media = sum(notas) / len(notas)
tam = len(notas)

count1, count2 = 0, 0
for i in range(0, tam):
    if notas[i] >= media:
        count1 += 1

    if notas[i] < 7:
        count2 += 1

print(len(notas))
print(notas)
notas.reverse()
for i in notas:
    print(i)
print(sum(notas))
print(media)
print(count1)
print(count2)
print('Este programa está encerrado! Bom dia para você!')
