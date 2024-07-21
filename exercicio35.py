''' 35. O cardápio de uma lanchonete é o seguinte:

Especificação / Código / Preço

Cachorro Quente / 100 / R$ 1,20
Bauru Simples / 101 / R$ 1,30
Bauru com ovo / 102 / R$ 1,50
Hambúrguer / 103 / R$ 1,20
Cheeseburguer / 104 / R$ 1,30
Refrigerante / 105 / R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. '''

quant = int(input('Informe a quantidade: '))

precos = {
    100: 1.20,
    101: 1.30,
    102: 1.50,
    103: 1.20,
    104: 1.30,
    105: 1.00,
}

valores_por_item = []

cont = 0

for i in range(quant):

    codigo = int(input('Informe o código do item: '))
    preco = float(input(f'Preço item R$: '))
    cont += 1

    if codigo in precos:
        valor = precos[codigo] * quant
         
        valores_por_item.append
    
        print(f'Valor a ser pago pelo item {codigo}: R${valor:.2f}', )
        cont += 1

print('Total do pedido: ', sum(valores_por_item)) 