# 61 - A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
#     Faça um programa capaz de gerar a série até o n−ésimo termo.

num = int(input('Informe até qual termo deve ser gerado fibonacci: '))
res = 0
a1 = 1
a2 = 0

for i in range(num + 1):
    res = a2 + a1
    a2 = a1
    a1 = res
    print(res, end = ' ')
