# 18. Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. 
# O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. 
# Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.'''

n = int(input('Informe um número inteiro: '))
primos = []
divisoes = 0


for i in range(2, n):
    primo = True                   

   
    for j in range(2, i):          
       divisoes += 1
    
       
       if i % j == 0:
           primo = False
           break
       
    if primo:
        primos.append(i)   
    

print('Primos: ', primos)

print('Número de divisões: ', divisoes)