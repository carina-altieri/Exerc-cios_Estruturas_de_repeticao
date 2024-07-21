# 20. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

candidato_1 = 0
candidato_2 = 0
candidato_3 = 0

votos = 0


eleitores = int(input('Informe o número total de eleitores: '))

while votos < eleitores:
    voto = int(input('Eleitor, digite seu voto: '))

    votos += 1 

    match voto: 
        case 1:
            candidato_1 += 1
        case 2:
            candidato_2 += 1
        case 3:
            candidato_3 += 1

print('Candidato 1: ', candidato_1, ' votos')
print('Candidato 2: ', candidato_2, ' votos')
print('Candidato 3: ', candidato_3, ' votos')