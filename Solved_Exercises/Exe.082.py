# 82 - Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo,
#     a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes
#     da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário
#     digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do
#     clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes

sair = None
altura, peso, alto, gordo, med_altura, med_peso = 0, 0, 0, 0, 0, 0
baixo, magro = 100, 100
a_alto, a_baixo, a_gordo, a_magro = 0, 0, 0, 0
cont = 0

while sair != 0:
    cod = int(input('Informe o código do aluno: '))
    altura = float(input('Informe a altura do aluno: '))
    peso = float(input('Informe o peso do aluno: '))
    cont += 1
    med_altura += altura
    med_peso += peso

    if altura > alto:
        alto = altura
        a_alto = cod
    elif altura < baixo:
        baixo = altura
        a_baixo = cod

    if peso > gordo:
        gordo = peso
        a_gordo = cod
    elif peso < magro:
        magro = peso
        a_magro = cod

    sair = int(input('Para sair digite 0(zero), para cadastrar novo aluno, digite qualquer tecla: '))

med_altura = med_altura / cont
med_peso = med_peso / cont

print(f'O aluno mais alto é o código: {a_alto}, sua altura é de {alto} metros.')
print(f'O aluno mais baixo é o código: {a_baixo}, sua altura é de {baixo} metros.')
print(f'O aluno mais pesado é o código: {a_gordo}, seu peso é de {gordo} kgs.')
print(f'O aluno menos pesado é o código: {a_magro}, seu peso é de {magro} kgs.')
print(f'A média total das alturas é de {med_altura} metros')
print(f'A média total dos pesos é de {med_peso}')
