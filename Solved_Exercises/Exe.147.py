# 147 - Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo
#     um relatório dos endereços IP válidos e inválidos.
#     O arquivo de entrada possui o seguinte formato:
#     200.135.80.9
#     192.168.1.1
#     8.35.67.74
#     257.32.4.5
#     85.345.1.2
#     1.2.3.4
#     9.8.234.5
#     192.168.0.256
#     O arquivo de saída possui o seguinte formato:
#     [Endereços válidos:]
#     200.135.80.9
#     192.168.1.1
#     8.35.67.74
#     1.2.3.4
#
#     [Endereços inválidos:]
#     257.32.4.5
#     85.345.1.2
#     9.8.234.5
#     192.168.0.256

# Le o arquivo
arquivo = open('IP.txt', 'r')

# Coloca a informação do arquivo na memória
ips = arquivo.readlines()

# Fecha o arquivo
arquivo.close()

ip_Valido, ip_Invalido = [], []

for i in ips:
    p1, p2, p3, p4 = map(int, i.split('.'))

    if (p1 <= 0) or (p1 >= 224) or (p1 == 127):
        ip_Invalido.append(i)
    elif p1 <= 126:
        if (p2 < 0) or (p2 > 255) or (p3 < 0) or (p3 > 255) or (p4 < 0) or (p4 > 255):
            ip_Invalido.append(i)
        elif (p2 == 0) and (p3 == 0) and (p4 == 0):
            ip_Invalido.append(i)
        elif (p2 == 255) and (p3 == 255) and (p4 == 255):
            ip_Invalido.append(i)
        else:
            ip_Valido.append(i)
    elif (p1 >= 128) and (p1 <= 191):
        if (p2 < 0) or (p2 > 225) or (p3 < 0) or (p3 > 255) or (p4 < 0) or (p4 > 255):
            ip_Invalido.append(i)
        elif (p3 == 0) and (p4 == 0):
            ip_Invalido.append(i)
        elif (p2 == 255) and (p3 == 255) and (p4 == 255):
            ip_Invalido.append(i)
        else:
            ip_Valido.append(i)
    elif p1 >= 192:
        if (p2 < 0) or (p2 > 225) or (p3 < 0) or (p3 > 225) or (p4 <= 0) or (p4 >= 255):
            ip_Invalido.append(i)
        else:
            ip_Valido.append(i)
    else:
        ip_Valido.append(i)

arquivoSaida = open('IP_Saida.txt', 'w')

arquivoSaida.write('[IP Válidos]\n')
for ip in ip_Valido:
    arquivoSaida.write(f'{ip}')

arquivoSaida.write('\n[IP Inválidos]\n')
for ip in ip_Invalido:
    arquivoSaida.write(f'{ip}')

arquivoSaida.close()
