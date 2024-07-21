# 13. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120 '''

n = int(input('Digite um número inteiro: '))


fatorial = 1

for i in range(n, 0, -1):
    fatorial *= i

print(f'{n}! = {fatorial}')