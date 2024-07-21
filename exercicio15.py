# 15. Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

lista = []
cont = 0
num = 0

quantidade = int(input('Digite quantos números você quer que tenha a sua lista: '))


while cont < quantidade:
    if num >= 0 and num <= 1000:
        n = lista.append(float(input('Digite um número entre 0 e 1000: ')))
        cont += 1
    else:
        break


maiorValor = max(lista)
menorValor = min(lista)
soma = sum(lista)


print('Maior valor: ', format(maiorValor))
print('Menor valor: ', format(menorValor))
print('Soma dos valores: ', format(soma))