'''

Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

'''

print(' Ano Bissexto ')

ano = int(input('Digite o ano: '))

if ano % 4 == 0:
    bissexto = ano%100

    if bissexto != 0:
        print(f'O ano {ano} é bissexto !')
    else:
        print(f'Ano {ano} não é bissexto !')

elif ano % 400 == 0:
    print(f'O ano {ano} é bissexto !')
else:
    print('Ano não é bissexto !')

