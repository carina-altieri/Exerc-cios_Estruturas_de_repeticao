# 19. Faça um programa que calcule o mostre a média aritmética de N notas.

lista = []
cont = 0
quant = int(input('Digite a quantidade de notas que deseja-se verificar: '))


while cont < quant:
    notas = lista.append(float(input(f'Digite a nota {cont + 1}: '))) 
    cont += 1
    
media = sum(lista)/len(lista)

print('Média aritmética das notas: {:.1f} '.format(media))