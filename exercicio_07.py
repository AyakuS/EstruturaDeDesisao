'''
Faça um Programa que leia três números e mostre o menor deles
'''
n1 = int(input('Digite um Numero: '))
n2 = int(input('Digite outro Numero: '))
n3 = int(input('Digite mais um Numero: '))

if n1 < n2 and n1 < n3:
    print('O numero {} ,digitado é menor!'.format(n1))
elif n2 < n1 and n2 < n3:
    print('O numero {} ,digitado é menor!'.format(n2))
elif n3 < n2 and n3 < n1:
    print('O numero {} ,digitado é menor!'.format(n3))
elif n1 == n2 and n1 == n3:
    print('Todos os numeros são iguais !')
else:
    print('Algum numero foi duplicado, por favor digite numeros diferentes !')