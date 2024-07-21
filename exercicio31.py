''' 31. Uma academia deseja fazer um senso entre seus clientes para descobrir:
o mais alto, o mais baixo, o mais gordo e o mais magro, para isto você deve fazer um programa que pergunte
a cada um dos clientes da academia seu código, sua altura e seu peso. 
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código.
Ao encerrar o programa também deve ser informados os códigos e valores do cliente mais alto,
do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes'''

codigos = []
alturas = []
pesos = []

cont = 0

while True: 
        codigo = int(input(f'Aluno {cont+1}, informe seu código: '))
        codigos.append(codigo)
        
        if codigo != 0:

          altura = alturas.append(float(input(f'Aluno {cont+1}, informe sua altura: ')))

          peso = pesos.append(float(input(f'Aluno {cont+1}, informe seu peso: ')))

          cont += 1

        else:
             break
        
media_altura = sum(alturas)/len(alturas)
media_peso = sum(pesos)/len(pesos)

indice_mais_alto = alturas.index(max(alturas))
indice_mais_baixo = alturas.index(min(alturas))
indice_mais_gordo = pesos.index(max(pesos))
indice_mais_magro = pesos.index(min(pesos))

print('Média das alturas dos clientes: ', media_altura,' m.   ' 'Média dos pesos dos clientes: ', media_peso, ' kg.')
print('Dados do cliente mais alto - Código: ', codigos[indice_mais_alto], ' Altura: ', alturas[indice_mais_alto], ' Peso: ', pesos[indice_mais_alto])
print('Dados do cliente mais baixo - Código: ', codigos[indice_mais_baixo], ' Altura: ', alturas[indice_mais_baixo], ' m  ', ' Peso: ', pesos[indice_mais_baixo], ' kg')
print('Dados do cliente mais gordo - Código: ', codigos[indice_mais_gordo], ' Altura: ', alturas[indice_mais_gordo], ' m  ', ' Peso: ', pesos[indice_mais_gordo], ' kg')
print('Dados do cliente mais magro - Código: ', codigos[indice_mais_magro], ' Altura: ', alturas[indice_mais_magro], ' m  ', ' Peso: ', pesos[indice_mais_magro], ' kg') 
