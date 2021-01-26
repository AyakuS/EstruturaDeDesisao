'''

Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da
operação deve ser acompanhado de uma frase que diga se o número é:
    A.par ou ímpar;
    B.positivo ou negativo;
    C.inteiro ou decimal.

'''
n1 = float(input('Digite um numero: '))
n2 = float(input('Digite um numero: '))

print('Digite selecione uma das opções abaixo !')
print('Deseja saber se esse numero é impar ou par? Digite PAR')
print('Deseja saber se esses numeros são negativos ou positivos? Digite POSITIVO ')
print('Deseja saber se esses numeros são inteiro ou decimal? Digite CONJUNTO ')

decisao = str.upper(input('Desejo: '))

if decisao == 'PAR':

    if n1 % 2 == 0 and n2 % 2 == 0:
        print(f'Os numeros({n1}, {n2}) são pares! ')
    elif n1 % 2 == 0 and n2 % 2 != 0:
        print(f'Par {n1}, Impar{n2}')
    else:
        print(f'Os numeros({n1}, {n2}) são impares! ')

elif decisao == 'POSITIVO':

    if n1 < 0 and n2 < 0:
        print(f'Os numeros({n1}, {n2}) são negativos')
    elif n1 < 0 and n2 > 0:
        print(f'Os numeros {n1} Negativo {n2}) Positivo')
    elif n1 > 0 and n2 < 0 :
        print(f'Os numeros {n1} Positivo {n2}) Negativo')
    else:
        print(f'Os numeros({n1}, {n2}) são posotivos')

elif decisao == 'CONJUNTO':

    aux1 = round(n1)
    aux2 = round(n2)

    if n1 == aux1 and n2 == aux2:
        print('Os numeros digitados são inteiros !')

    elif n1 != aux1 and n2 == aux2:
        print(f'O numero {n1} é decimal. O Numero {n2} é inteiro.')

    elif n1 == aux1 and n2 != aux2:
        print(f'O numero {n1} é inteiro. O Numero {n2} é decimal..')

    else:
        print(f'Os numeros digitados possuem casa decimal, os numeros arrendodos são: {aux1},{aux2} ')

else:
    print('Digite um valor valido ! ')


