''' 12. A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
Faça um programa que gere a série até que o valor seja maior que 500.


 cada termo a partir do terceiro é a soma dos dois antecessores
(0, 1, 1, 2, 3, 5, 8...)
n3 = n2 + n1
n4 = n3 + n2
n5 = n4 + n3
n6 = n5 + n4
... 
'''

a = 0 
b = 1 

while a <= 500:   
    print(a)
    c = a + b 
    a = b
    b = c