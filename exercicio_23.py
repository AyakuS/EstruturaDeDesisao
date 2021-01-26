'''

Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de
arredondamento.

'''
import math

numero = float(input('Digite um numero: '))
aux = round(numero)
if numero == aux:
    print('numero digitado é inteiro')
else:
    print(f'Numero digitado é possui casa decimal, numero arrendodo é: {aux} ')
