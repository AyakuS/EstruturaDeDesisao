'''
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão
é sempre pelo mais barato.
'''
produto_1 = input('Digite o valor do produto 1: ')
produto_2 = input('Digite o valor do produto 2: ')
produto_3 = input('Digite o valor do produto 3: ')

if produto_1 < produto_2 and produto_1 < produto_3:
    print('Comprar o Produto 1: R${}'.format(produto_1))
elif produto_2 < produto_1 and produto_2 < produto_3:
    print('Comprar o Produto 2: R${}'.format(produto_2))
elif produto_3 < produto_1 and produto_3 < produto_2:
    print('Comprar o Produto 3: R${}'.format(produto_3))
    