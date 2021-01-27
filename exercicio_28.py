'''
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há
limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um
desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo
usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de
pagamento, valor do desconto e valor a pagar.
'''


print('         ======= Hipermercado Tabajara =======')
print('         ======= Promoção de Carnes =======')
print('                      Até 5 Kg           Acima de 5 Kg\n'
      'File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg\n'
      'Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg\n'
      'Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg\n')
print('OBS: Cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há\n'
      'limites para a quantidade de carne por cliente. Pagamentos com Cartões Tabajara desconto\n'
      'de %5 no total de compra! ')
tipo_carne = True
while tipo_carne:
    carne_valor = True
    while carne_valor:
        carne = str.upper(input('Qual carne deseja comprar?\n'
                                'F - File Duplo\n'
                                'A - Alcatra\n'
                                'P - Picanha\n'
                                'Qual opção: '))
        if carne == 'A' or carne == 'F' or carne == 'P':
            carne_valor = False
        else:
            print('Digite um valor valido! \n')

    peso = float(input('Digite o peso comprado: '))
    print('Pagamentos com Cartões Tabajara desconto de %5 no total de compra!')

    forma_pagamento = True
    while forma_pagamento:

        pagamento = str.upper(input('Qual é forma de pagamento?: '))

        if pagamento == 'TABAJARA':
            forma_pagamento = False

        elif pagamento == 'DEBITO' or pagamento == 'CREDITO':
            forma_pagamento = False
        else:
            print('Digite uma forma de pagamento valida\n'
                  'Debito, Credito ou Cartões Tabajara')
    print('\n')

    if carne == 'F':
        if peso <= 5:

            preco_picanha = peso * 4.90
            if pagamento == 'TABAJARA':

                desconto = preco_picanha * 0.05
                print('Tipo de Carne: File Duplo, {} KG\n'
                      'Desconto de R${:.2f}\n'
                      'Total a Pagar R${:.2f}\n'
                      ''.format(peso, desconto, preco_picanha - desconto))
            else:
                print('Tipo de Carne: File Duplo KG {}\n'
                      'Total a Pagar R${:.2f}\n'
                      'Forma de Pagamento: {}'.format(peso, preco_picanha, pagamento))
        elif peso > 5:

            preco_picanha = peso * 5.80
            if pagamento == 'TABAJARA':

                desconto = preco_picanha * 0.05
                print('Tipo de Carne: File Duplo, {} KG\n'
                      'Desconto de R${:.2f}\n'
                      'Total a Pagar R${:.2f}\n'
                      'Forma de pagamento: Cartão {}'.format(peso, desconto, preco_picanha - desconto, pagamento))
            else:
                print('Tipo de Carne: File Duplo KG {}\n'
                      'Total a Pagar R${:.2f}\n'
                      'Forma de pagamento: Cartão {}'.format(peso, preco_picanha, pagamento))
        print('\n')
        desejo = str.upper(input('Deseja fazer outra compra? S/N: '))
        if desejo == 'S':
            tipo_carne = True
        elif desejo == 'N':
            tipo_carne = False

    elif carne == 'A':

        if peso <= 5:

            preco_alcatra = peso * 5.90
            if pagamento == 'TABAJARA':

                desconto = preco_alcatra * 0.05
                print('Tipo de Carne: File Duplo, {} KG\n'
                      'Desconto de R${:.2f}\n'
                      'Total a Pagar R${:.2f}\n'
                      ''.format(peso,desconto,preco_alcatra-desconto))
            else:
                print('Tipo de Carne: File Duplo KG {}\n'
                      'Total a Pagar R${:.2f}\n'
                      'Forma de Pagamento: {}'.format(peso, preco_alcatra,pagamento))
        elif peso > 5:

            preco_alcatra = peso * 5.90
            if pagamento == 'TABAJARA':

                desconto = preco_alcatra * 0.05
                print('Tipo de Carne: Alcatra, {} KG\n'
                      'Desconto de R${:.2f}\n'
                      'Total a Pagar R${:.2f}\n'
                      'Forma de pagamento: Cartão {}'.format(peso,desconto,preco_alcatra-desconto,pagamento))
            else:
                print('Tipo de Carne: Alcatra, KG {}\n'
                      'Total a Pagar R${:.2f}\n'
                      'Forma de pagamento: Cartão {}'.format(peso, preco_alcatra, pagamento))
        print('\n')
        desejo = str.upper(input('Deseja fazer outra compra? S/N: '))
        if desejo == 'S':
            tipo_carne = True
        elif desejo == 'N':
            tipo_carne = False

    elif carne == 'P':

        if peso <= 5:
            preco_picanha = peso * 4.90
            if pagamento == 'TABAJARA':

                desconto = preco_picanha * 0.05
                print('Tipo de Carne: Picanha, {} KG\n'
                      'Desconto de R${:.2f}\n'
                      'Total a Pagar R${:.2f}\n'
                      ''.format(peso, desconto, preco_picanha - desconto))
            else:
                print('Tipo de Carne: Picanha, {}KG \n'
                      'Total a Pagar R${:.2f}\n'
                      'Forma de Pagamento: {}'.format(peso, preco_picanha, pagamento))
        elif peso > 5:

            preco_picanha = peso * 5.80
            if pagamento == 'TABAJARA':

                desconto = preco_picanha * 0.05
                print('Tipo de Carne: Picanha, {} KG\n'
                      'Desconto de R${:.2f}\n'
                      'Total a Pagar R${:.2f}\n'
                      'Forma de pagamento: Cartão {}'.format(peso, desconto, preco_picanha - desconto, pagamento))
            else:
                print('Tipo de Carne: Picanha {} KG\n'
                      'Total a Pagar R${:.2f}\n'
                      'Forma de pagamento: Cartão {}'.format(peso, preco_picanha, pagamento))
        print('\n')
        desejo = str.upper(input('Deseja fazer outra compra? S/N: '))
        if desejo == 'S':
            tipo_carne = True
        elif desejo == 'N':
            tipo_carne = False
