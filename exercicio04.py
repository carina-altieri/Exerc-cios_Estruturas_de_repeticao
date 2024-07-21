# 4. Faça um programa que leia 5 números e informe o maior número.

n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite um número inteiro: "))
n3 = int(input("Digite um número inteiro: "))
n4 = int(input("Digite um número inteiro: "))
n5 = int(input("Digite um número inteiro: "))


lista = [n1, n2, n3, n4, n5]
print('O maior número é o número ', max(lista))