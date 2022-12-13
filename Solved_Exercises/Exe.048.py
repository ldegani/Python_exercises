# 48 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
#     mostrando uma mensagem de erro e voltando a pedir as informações.

nome = input('Informe o nome do usuário: ')
senha = input('Informe a senha: ')

while nome == senha:
    print('Senha não pode ser igual o nome do usuário!')
    nome = input('Informe o nome do usuário: ')
    senha = input('Informe a senha: ')

print('Usuário e senha cadastrados!')