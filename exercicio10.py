# 10. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

par = 0       
impar = 0     

n = 1

while n <= 10:
    numeros = int(input('Digite um número inteiro: '))
    n += 1

    if n % 2 == 0:
        par += 1      
    else:
        impar += 1    
print("Pares: ", par, " Impares: ", impar)