# 14. Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.


lista = []
cont = 0  

quantidade = int(input('Digite quantos números você quer que tenha a sua lista: '))

while cont < quantidade:
    num = float(input('Digite um número: '))
    lista.append(num)
    cont += 1


maiorValor = max(lista)
menorValor = min(lista)
soma = sum(lista)


print('Maior valor: ', format(maiorValor))
print('Menor valor: ', format(menorValor))
print('Soma dos valores: ', format(soma))