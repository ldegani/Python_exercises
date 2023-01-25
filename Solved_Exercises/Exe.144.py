# 144 - Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no
#     caso deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem
#     o traço separador.
#
#     Valida e corrige número de telefone
#     Telefone: 461-0133
#     Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
#     Telefone corrigido sem formatação: 34610133
#     Telefone corrigido com formatação: 3461-0133

telefone = str(input('Informe seu telefone: '))

if (telefone.isdigit()) and (len(telefone) < 8):
    p1 = telefone[0:3]
    p2 = telefone[3:]
    corr1 = ('3' + telefone)
    corr2 = ('3' + p1 + '-' + p2)
    print('Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.')
    print(f'Telefone corrigido sem formatação: {corr1}')
    print(f'Telefone corrigido com formatação: {corr2}')

else:
    rep_telefone = telefone.replace('-', '')
    if (len(rep_telefone) < 8):
        print('Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.')
        novo_telefone1 = ('3' + telefone)
        novo_telefone2 = ('3' + rep_telefone)
        print(f'Telefone corrigido sem formatação: {novo_telefone2}')
        print(f'Telefone corrigido com formatação: {novo_telefone1}')
