# 5. Faça um programa que leia 5 números e informe a soma e a média dos números.'''

n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
n3 = float(input("Número 3: "))
n4 = float(input("Número 4: "))
n5 = float(input("Número 5: "))

lista = [n1, n2, n3, n4, n5]

soma = sum(lista)          
media = soma / len(lista)   

print(f'A média e a soma dos números informados é, respectivamente, {soma:.2f} e {media:.2f}.')