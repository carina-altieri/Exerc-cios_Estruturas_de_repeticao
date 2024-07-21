# 34. Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos:
# [0-25], [26-50], [51-75] e [76-100].
# A entrada de dados deverá terminar quando for lido um número negativo. 

quant = int(input('Quantos números deseja digitar: '))
cont = 0 
positivos = []

while quant > cont:
    num = int(input(f'Digite o número {cont+1}: ')) 

    if 0 <= num <= 100:       # if 0 <= num <= 25 or 26 <= num <= 50 or 51 <= num <= 75 or 76 <= num <= 100:
        positivos.append(num)
        cont += 1
    
    elif num < 0:
        break

print('Números positivos dentro dos intervalos determinados: ', positivos)