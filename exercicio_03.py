'''
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
F - Feminino, M - Masculino, Sexo Inválido.

'''

sexo = str.upper(input('Digite seu Sexo F para Feminino e M para Masculino: '))

if sexo == 'F':
    print('Sexo Feminino !')
elif sexo == 'M':
    print('Sexo Masculino !')
else:
    print('Valor Digitado não é valido !')