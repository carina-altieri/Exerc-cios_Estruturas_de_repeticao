# 3. Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. 
# Depois modifique o programa para que ele mostre os números um ao lado do outro.

num = 1

while num < 21:
    print(num)
    num += 1


# programa modificado:

valor = 1

while valor < 21:
    print(valor, end=' ')
    valor += 1