# 33. O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que:
# leia um conjunto indeterminado de temperaturas;
# informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

temperaturas = []

cont = 0

quant_temperaturas = int(input('Informe quantas temperaturas deseja informar para o programa: '))

while cont < quant_temperaturas:
    t = temperaturas.append(float(input('Digite a temperatura: ')))
    cont += 1

media = sum(temperaturas)/len(temperaturas)

print('Maior temperatura: ', max(temperaturas), ' Menor temperatura: ', min(temperaturas),' Média das temperaturas: ', media)