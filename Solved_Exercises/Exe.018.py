# 18 - Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet
#     (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

arquivo = float(input("Informe o tamanho do arquivo (em MB): "))
internet = float(input("Informe a velocidade da internet (em Mbps): "))


tempoSeg = arquivo / (internet / 8)
tempoMin = tempoSeg / 60

print("O tempo aproximado de download é de ", tempoMin, "minutos")
