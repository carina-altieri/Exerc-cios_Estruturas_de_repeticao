#  33. Faça um programa que leia dez conjuntos de dois valores
# o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros.
# Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

cont = 0
codigos = []
alturas = []

# conjunto = {numero_aluno, altura_cm}

for i in range(1, 3):

    numero_aluno = codigos.append(int(input(f'Informe o número do aluno {cont+1}: ')))
    altura_cm = alturas.append(float(input(f'Informe a altura do aluno {cont+1}: ')))
    cont += 1         # move o índice para o próximo elemento da lista

indice_mais_alto = alturas.index(max(alturas))
indice_mais_baixo = alturas.index(min(alturas))

print('Código do aluno mais alto:', codigos[indice_mais_alto], '   Altura:', alturas[indice_mais_alto], 'cm')
print('Código do aluno mais baixo:', codigos[indice_mais_baixo],'  Altura:', alturas[indice_mais_baixo],'cm')