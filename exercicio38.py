''' 38. Um sistema do metrô sinaliza o nível de ocupação por vagão usando cores. 
Azul (vazio ou baixa ocupação) - 0 a 50
Amarela (ocupação média) - 51 a 100
Laranja (ocupação alta) - 101 a 150
Vermelha (ocupação altíssima ou lotado) - 151 a 250

Considere que cada composição tem cinco vagões e essa sinalização é feita em cada vagão.

Escreva um programa que simule uma composição do metrô utilizando um vetor. 
Mostre os valores de passageiros por carro e verifique se os vetores de entrada são adequados 
valores negativos ou acima de 250 não devem ser permitidos. 

Na saída, apresente todos os vagões com o número do carro, o número de ocupantes, a sinalização correspondente
e o total de passageiros da composição.
'''

# entrada
    # --> obter o número de pessoas por vagão
    # --> verificar se o número é válido
composicao = []
cores = []
total = 0

for carro in range(5):
    pessoas = int(input('Digite o número de pessoas no carro '+ str(carro + 1) +': '))

    if pessoas < 250 and pessoas > 0:
        composicao.append(pessoas)
    else: 
        print('Número inválido.')


# processamento
    # --> para cada vagão:
    # --> comparar o número de pessoas com as cores
    # --> somar o total de pessoas

for carro in range(5):
    total += composicao[carro]

    if(composicao[carro] < 51):            
        cores.append('Azul')
    elif(composicao[carro] < 101):
        cores.append('Amarelo')
    elif(composicao[carro] < 151):
        cores.append('Laranja')
    else:
        cores.append('Vermelho')

# saída
    # --> pessoas e cores por vagão 
    # --> total de pessoas na composição

print('Total de pessoas: ' + str(total))
for carro in range(5):
    print('carro: ' + str(carro+1) + ' cor: ' + cores[carro] + ' pessoas: ' + str(composicao[carro])) 
