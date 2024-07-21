''' 26. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. 

A saída deve ser conforme o exemplo abaixo:

Fatorial de: 5

5! = 5 . 4 . 3 . 2 . 1 = 120 '''

n = int(input('Informe um número inteiro para calcular seu fatorial: '))

fatorial = 1

fatores = []

for i in range(n, 0, -1):
    fatorial *= i

    fatores.append(str(i))

fatores_Str = ' x '.join(fatores)

print(f'{n}! = {fatores_Str} =', fatorial)