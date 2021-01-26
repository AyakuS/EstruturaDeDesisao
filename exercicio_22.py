'''
Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo
(resto da divisão).
'''

numero = int(input('Digite um numero para saber se ele é Impar ou Par: '))

if numero % 2 == 0:
    print(f'Numero digitado {numero} é PAR !'),

elif numero % 2 == 1:
    print(f'Numero digitado {numero} é IMPAR !')
