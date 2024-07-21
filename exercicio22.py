# 22 . Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs 
# e o valor médio gasto em cada um deles.
# O usuário deverá informar a quantidade de CDs e o valor para em cada um.'''

quantidade = int(input('Informe a quantidade de CDs: '))

total_investido = []

cont = 0   # inicia o contador de cds

for cd in range(1, quantidade+1):
    valor = float(input('Informe o valor do CD: '))
    total_investido.append(valor)                    
    cont += 1

# valor total investido:
soma = sum(total_investido)

# média de gastos:
media = sum(total_investido)/len(total_investido)

print('O total investido pelo colecionador foi de R${:.2f}, enquanto o valor médio gasto em cada um deles foi de R${:.2f}.'.format(soma, media))