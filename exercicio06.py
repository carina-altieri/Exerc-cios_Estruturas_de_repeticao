# 9. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

n = 1

while n >= 1 and n <= 50:
    if n % 2 != 0:
        print(n)
    n += 2
