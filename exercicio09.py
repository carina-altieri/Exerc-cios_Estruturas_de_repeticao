# 9. Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. 
# Não utilize a função de potência da linguagem.


base = int(input('Digite a base: '))
expoente = int(input('Digite o expoente: '))

resultado = 1
contador = 0 

while contador < expoente:
    resultado *= base
    contador += 1


print(resultado)
