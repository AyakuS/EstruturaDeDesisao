'''
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do
mesmo.Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
'''

numero = int(input('Digite um numero inteiro menor que 1000 : '))

if numero <= 1000:

    if numero == 100 or numero == 200  or numero == 300  or numero == 400  or numero == 500 \
            or numero == 600  or numero == 700  or numero == 800  or numero == 900:

        if numero >= 200:
            txt = str(numero)
            print(f'{txt[0]} Centenas')
        else:
             txt = str(numero)
             print(f'{txt[0]} Centena')

    elif numero == 10 and numero == 20 or numero == 30 or numero == 40 or numero == 50 \
            or numero == 60 or numero == 70 or numero == 80 or numero == 90:

        if numero >= 20:
            txt = str(numero)
            print(f'{txt[0]} Dezenas')
        else:
            txt = str(numero)
            print(f'{txt[0]} Dezena')
    elif numero <= 9:

        if numero == 1:
            txt = str(numero)
            print(f'{txt[0]} Unidade')
        else:
            txt = str(numero)
            print(f'{txt[0]} Unidades')

    elif numero == 11 or numero == 21 or numero == 31 or numero == 41 or numero == 51\
            or numero == 61 or numero == 71 or numero == 81 or numero == 91:

        if numero == 11:

            txt = str(numero)
            print(f'{txt[0]} Dezena e {txt[1]} unidade')

        else:
            txt = str(numero)
            print(f'{txt[0]} Dezenas e {txt[1]} unidade')

    elif numero >= 12 and numero < 20:

        txt = str(numero)
        print(f'{txt[0]} Dezena e {txt[1]} Unidades')

    elif numero > 21:

        txt = str(numero)
        print(f'{txt[0]} Dezenas e {txt[1]} Unidades')

    elif numero > 100 and numero <= 199:

        print('Parei aqui aaaaaaaaah !')

else:
    print('Numero digitado não é valido')
