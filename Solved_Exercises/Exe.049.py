# 49 - Faça um programa que leia e valide as seguintes informações:
#     Nome: maior que 3 caracteres;
#     Idade: entre 0 e 150;
#     Salário: maior que zero;
#     Sexo: 'f' ou 'm';
#     Estado Civil: 's', 'c', 'v', 'd';


nome = input('Informe o nome: ')
while len(nome) < 4:
    print('Nome menor que 3 carateres!')
    nome = input('Informe o nome: ')

idade = int(input('Informe a idade: '))
while (idade < 0) or (idade > 150):
    print('Idade inválida!')
    idade = int(input('Informe a idade: '))

salario = float(input('Informe o salário: '))
while salario < 0:
    print('Salário inválido!')
    salario = float(input('Informe o salário: '))

sexo = input('Informe o sexo(m/f): ')
while sexo not in('f', 'm'):
    print('Sexo inválido!')
    sexo = input('Informe o sexo(m/f): ')

civil = input('Informe o estado civil(s, c, v, d): ')
while civil not in('s', 'c', 'v', 'd'):
    print('Estado civil inválido!')
    civil = input('Informe o estado civil(s, c, v, d): ')
