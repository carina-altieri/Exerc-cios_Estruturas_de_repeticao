''' 37. Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:

1 , 2, 3, 4 - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:

O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A porcentagem de votos nulos sobre o total de votos;
A porcentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero. '''

import random

eleitores = int(input('Digite o número total de eleitores: '))

candidato1 = 0
candidato2 = 0
candidato3 = 0
votoBranco = 0
votoNulo = 0


cont = 1
    
while cont <= eleitores:
    print('Eleitor', cont, 'de', eleitores)  

    voto = random.randint(1, 6)   

    print('eleitor votou: ', voto)

  

    match voto:             
        case  1:           
            candidato1 += 1
        case 2:
            candidato2 += 1
        case 3:
            candidato3 += 1
        case 4:
            votoBranco += 1
        case _:              
            votoNulo += 1

    cont += 1 


if candidato1 > candidato2 and candidato1 > candidato3 and candidato1 > votoBranco and candidato1 > votoNulo:
    print('O candidato 1 venceu a eleição.')
elif candidato2 > candidato1 and candidato2 > candidato3 and candidato2 > votoBranco and candidato1 > votoNulo:
    print('O candidato 2 venceu a eleição')
elif candidato3 > candidato1 and candidato3 > candidato2 and candidato3 > votoBranco and candidato3 > votoNulo:
    print('O candidato 3 venceu a eleição.')
elif candidato1 == candidato2 == candidato3 and candidato1 > votoBranco and candidato1 > votoNulo:
    print('Empate entre os 3 candidatos.')
elif candidato1 == candidato2 and candidato1 > candidato3 and candidato1 > votoBranco and candidato1 > votoNulo:
    print('Empate entre os candidatos 1 e 2.')
elif candidato2 == candidato3 and candidato2 > candidato3 and candidato2 > votoBranco and candidato2> votoNulo:
    print('Empate entre os candidatos 2 e 3.')
elif candidato1 == candidato3 and candidato1 > candidato2 and candidato1 > votoBranco and candidato1 > votoNulo:
    print('Empate entre os candidatos 1 e 3.')
else:
    print('Nenhum candidato foi eleito.')



# exibir porcentagem de votos válidos (1, 2 e 3):

votos_validos = eleitores - (votoNulo - votoBranco)

print('O candidato 1 recebeu ', candidato1, 'votos.', ' Ou seja: ', (candidato1 / votos_validos) * 100, '%.')
print('O candidato 2 recebeu ', candidato2, 'votos.', ' Ou seja: ', (candidato2 / votos_validos) * 100, '%.') 
print('O candidato 3 recebeu ', candidato3, 'votos.', ' Ou seja: ', (candidato3 / votos_validos) * 100, '%.') 


# Total de votos nulos e total de brancos

print('Total de votos nulos: ', votoNulo)

print('Total de votos brancos: ', votoBranco)

# porcentagem votos em branco e nulos sobre o total de votos computados

percentual_branco_nulos = ((votoBranco + votoNulo) / eleitores) * 100
print('Percentual de votos em branco e nulos:  ', percentual_branco_nulos, '%.')