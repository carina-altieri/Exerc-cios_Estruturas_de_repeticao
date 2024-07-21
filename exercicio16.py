# 16 . Altere o programa de cálculo do fatorial
# permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

while True:
    n = int(input('Digite um número inteiro menor do que 16 para calcular o seu fatorial: '))

    fatorial = 1

    if n >= 0 and n < 16:

        for i in range(n, 0, -1):
            fatorial *= i

    print(f'{n}! = {fatorial}')