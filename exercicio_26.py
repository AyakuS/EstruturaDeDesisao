'''
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
    Álcool:
    A.até 20 litros, desconto de 3% por litro
    B.acima de 20 litros, desconto de 5% por litro
    Gasolina:
    A.até 20 litros, desconto de 4% por litro
    B.acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de
    combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente
    sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90
'''
print('Posto de Combustivel !\n'
      'Valor do Alcool: R$1,90\n'
      'Valor da Gasolina: R$2,50\n')

combustivel = str.upper(input('Digite o tipo de combustivel, A-Álcool e G-Gasolina: '))
abastecido = float(input('Digite a quantida de litros abastecido: '))

if combustivel == 'A':

    if abastecido <= 20:
        preco = abastecido * (1.90-(1.90*0.03))
        print('Valor a pagar: R${:.2f}'.format(preco))
    else:
        preco = abastecido * (1.90-(1.90*0.05))

elif combustivel == 'G':

    if abastecido <= 20:
        preco = abastecido * (2.50-(2.50*0.04))
        print('Valor a pagar: R${:.2f}'.format(preco))
    else:
        preco = abastecido * (2.50-(2.50*0.06))

elif combustivel >= 60:

    print('Digite o valor abastecido corretamente ! ')

