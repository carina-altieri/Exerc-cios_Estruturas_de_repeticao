''' 32. Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. 

Foram obtidos os seguintes dados:

Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999). 

Deseja-se saber:
Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio. '''

cidades = []
veiculos = []
acidentes = []
menor_2000 = []

for i in range(1,6):
    ddd = cidades.append(int(input('DDD: ')))
    veiculos_passeio = veiculos.append(int(input('Veículos de passeio: ')))
    acidentes_com_vitimas = acidentes.append(int(input('Acidentes de trânsito com vítimas: ')))

media_veiculos = sum(veiculos)/len(veiculos)

if veiculos_passeio < 2000:
    menor_2000.append(veiculos_passeio)

if len(menor_2000) > 0:
    media_acidentes = sum(menor_2000)/len(menor_2000)
else:
    media_acidentes = 0
    

print('Média de veículos nas cinco cidades juntas: ', media_veiculos)

print('Média de acidentes de trânsito nas cidades com menos de 2000 veículos de passeio: ', media_acidentes)

