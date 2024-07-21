''' 36. Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.

Exemplo:

12376489

=> 98467321 '''

# passar o número para str

num = str(input('Digite um a sequência de números inteiros positivos: '))
print(num[::-1])