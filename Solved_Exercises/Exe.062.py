# 62 - A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
#     Faça um programa que gere a série até que o valor seja maior que 500.

a1 = 1
a2 = 1
a3 = 0

print(a1)
while a1 < 500:
    print(a2)
    a3 = a1 + a2
    a1 = a2
    a2 = a3

