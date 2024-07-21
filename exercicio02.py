# 2. Altere o programa anterior, permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
# Valide a entrada e permita repetir a operação.

pais_A = int(input('Informe a população inicial do país A: '))   # taxa anual 3% (a cada ano a pop aumenta 3%)
pais_B = int(input('Informe a população inicial do país B: '))  # taxa anual 1.5% (a cada ano a pop aumenta 1.5%

taxa_A = float(input('Iforme a taxa de crescimento do país A: '))
taxa_B = float(input('Iforme a taxa de crescimento do país B: '))
ano = 0 

while pais_A < pais_B:
    pais_B *= (taxa_B / 100)  
    pais_A *= (taxa_A / 100)  

    ano += 1   # isso a cada ano

print('São necessários ', ano, ' anos para que a população do país A ultrapasse ou se iguale à populaçao do país B.')