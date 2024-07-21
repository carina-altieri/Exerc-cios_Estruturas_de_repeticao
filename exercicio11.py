# 11. A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
# Faça um programa capaz de gerar a série até o n-ésimo termo.

n = int(input("Digite quantos termos você quer mostrar para gerar uma sequência fibonacci: "))

a = 0
b = 1

cont = 1

while cont <= n:
    print(a)
    c = a + b
    a = b
    b = c
    cont += 1
    

print('fim')