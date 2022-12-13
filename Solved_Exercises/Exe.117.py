# 117 - Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de
#     fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200
#     mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar
#     deles.
#     Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um
#     número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
#     necessita da esfera; necessita de limpeza; necessita troca do cabo ou conector; quebrado ou inutilizado.
#     Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
#     Quantidade de mouses: 100
#
#     Situação                        Quantidade              Percentual
#     1- necessita da esfera                  40                     40%
#     2- necessita de limpeza                 30                     30%
#     3- necessita troca do cabo ou conector  15                     15%
#     4- quebrado ou inutilizado              15                     15%

PROBLEMAS = ['01 - Necessita de Esfera', '02 - Necessita de Limpeza', '03 - Troca do '
             'Cabo ou Conector', '04 - Quebrado ou Inutilizado']
IDENT = []
PROB = [0] * 4
IDENTIF = 1

print('Os problemas com o mouse são os seguintes: \n')
for problema in PROBLEMAS:
    print(problema)

print('\nInforme o número de identificação e o problema do mouse, de acordo com o índice.'
      '\nPara sair, informe 0(zero) no número de identificação.\n')
while IDENTIF != 0:
    IDENTIF = int(input('Número de identificação: '))
    if IDENTIF != 0:
        IDENT.append(IDENTIF)
        PROBLEMA = int(input('Informe o problema(1 - 4): '))
        if (PROBLEMA > 4) or (PROBLEMA < 1):
            print('Problema inválido!')
        else:
            PROB[PROBLEMA - 1] += 1

QTDE = sum(PROB)

print(f'Quantidade de mouses: {QTDE}')
print('Situação  \t\t\t\t\t  Quantidade  \t\t\t  Percentual')
for i in range(0, len(PROBLEMAS)):
    PERCENT = (PROB[i] / QTDE) * 100
    print(f'{PROBLEMAS[i]}      \t      {PROB[i]}      \t      {PERCENT:.2f} %')
