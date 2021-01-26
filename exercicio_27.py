'''
Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto
de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg)
de maças adquiridas e escreva o valor a ser pago pelo cliente.

'''
macas = float(input('Quantos KG de maça: '))
morangos = float(input('Qauntos KG de morango: '))

if macas <= 5 and morangos <= 5:
    valor_macas = macas * 1.80
    valor_morangos = morangos * 2.50
    valor_total = valor_morangos+valor_macas

    if valor_total >= 25:
        desconto = valor_total*0.10
        print('Valor Maças: R${:.2f}\n'
              'valor Morangos: R${:.2f}\n'
              'Desconto de 10%: R${:.2f}\n'
              'Total a pagar: R${:.2f}\n'
              ''.format(valor_macas, valor_morangos, desconto, valor_total - desconto))
    else:
        print('Valor Maças: R${:.2f}\n'
              'valor Morangos: R${:.2f}\n'
              'Total a pagar: R${:.2f}\n'
              ''.format(valor_macas, valor_morangos, valor_total))


elif macas < 8 and morangos < 8 :

    valor_macas = macas * 1.50
    valor_morangos = morangos * 2.20
    valor_total = valor_morangos + valor_macas

    if valor_total >= 25:
        desconto = valor_total*0.10
        print('Valor Maças: R${:.2f}\n'
              'valor Morangos: R${:.2f}\n'
              'Desconto de 10%: R${:.2f}\n'
              'Total a pagar: R${:.2f}\n'
              ''.format(valor_macas, valor_morangos, desconto, valor_total - desconto))
    else:
        print('Valor Maças: R${:.2f}\n'
              'valor Morangos: R${:.2f}\n'
              'Total a pagar: R${:.2f}\n'
              ''.format(valor_macas, valor_morangos, valor_total))

elif macas >= 8 and morangos >= 8:
    valor_macas = macas * 1.50
    valor_morangos = morangos * 2.20
    valor_total = valor_morangos + valor_macas
    desconto = valor_total * 0.10
    print('Valor Maças: R${:.2f}\n'
          'valor Morangos: R${:.2f}\n'
          'Desconto de 10%: R${:.2f}\n'
          'Total a pagar: R${:.2f}\n'
          ''.format(valor_macas, valor_morangos, desconto, valor_total - desconto))
