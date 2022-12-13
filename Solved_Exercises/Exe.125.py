# 125 - Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma
#     conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes
#     valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a
#     chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir
#     outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste
#     momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de
#     prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso,
#     cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

multa = 0.03
juros_dia = 0.001
valor_prestacao = 1

def valorPagamento(valor_prestacao, dias_atraso):
    if (valor_prestacao < 0) or (dias_atraso < 0):
        print('Valores informados são inválidos!')
        return None

    if dias_atraso == 0:
        print(f'R$ {valor_prestacao}')
    else:
        valor_total = valor_prestacao + (valor_prestacao * multa) + (valor_prestacao * juros_dia * dias_atraso)
        print(f'R$ {valor_total}')

print('Entrada das informações do dia, informe 0 reais de prestação para finalizar.')
while valor_prestacao != 0:
    valor_prestacao = float(input('Informe o valor da prestação: R$ '))
    if valor_prestacao != 0:
        dias_atraso = int(input('Informe quantos dias de atraso: '))
        valorPagamento(valor_prestacao, dias_atraso)
