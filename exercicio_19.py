'''
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do
mesmo.Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
'''
condicao = True
while (condicao):

    num = int(input('Digite um numero menor que 1000: '))

    if num < 1000:

        txt = str(num)
        casas_num = []

        for n in range (len(txt)):          #Laço faz a inserção e transformação para inteiro para a lista casas_num
            casas_num.append(int(txt[n]))

        if len(txt) == 3:

            if casas_num[0] == 1: # Valida uma centena

                if casas_num[1] == 1: # Valida uma dezena

                    if casas_num[2] == 1: # Valida uma unidade
                        print(f'{casas_num[0]} Centena, {casas_num[1]} Dezena e {casas_num[2]} Unidade')

                    elif casas_num[2] >= 2: # Valida mais que uma unidade
                        print(f'{casas_num[0]} Centena, {casas_num[1]} Dezena e {casas_num[2]} Unidades')

                    elif casas_num[2] == 0: # Valida o Zero da unidade
                        print(f'{casas_num[0]} Centena, {casas_num[1]} Dezena')

                elif casas_num[1] == 0: # Valida o zero da dezena

                    if casas_num[2] == 1:  # valida Unidade
                        print(f'{casas_num[0]} Centena e {casas_num[2]} Unidade')

                    elif casas_num[2] >= 2:
                        print(f'{casas_num[0]} Centena e {casas_num[2]} Unidades')

                elif casas_num[1]>=2: # Valida as Dezenas e unidades

                    if casas_num[2] == 1:
                        print(f'{casas_num[0]} Centena, {casas_num[1]} Dezena e {casas_num[2]} Unidade')

                    elif casas_num[2] >= 2:
                        print(f'{casas_num[0]} Centena, {casas_num[1]} Dezenas e {casas_num[2]} Unidades')

                    elif casas_num[2] == 0:
                        print(f'{casas_num[0]} Centena e {casas_num[1]} Dezenas')

            elif casas_num[0] >= 2: # Valida as centenas de igual ou acima de 2

                if casas_num[1] == 1:

                    if casas_num[2] == 1:
                        print(f'{casas_num[0]} Centenas, {casas_num[1]} Dezena e {casas_num[2]} Unidade')

                    elif casas_num[2] >= 2:
                        print(f'{casas_num[0]} Centenas, {casas_num[1]} Dezena e {casas_num[2]} Unidades')

                    elif casas_num[2] == 0:
                        print(f'{casas_num[0]} Centenas e {casas_num[1]} Dezena')

                elif casas_num[1] == 0: # Valida o zero da dezena

                    if casas_num[2] == 1:  # valida Unidade
                        print(f'{casas_num[0]} Centenas e {casas_num[2]} Unidade')

                    elif casas_num[2] >= 2:
                        print(f'{casas_num[0]} Centenas e {casas_num[2]} Unidades')

                    elif casas_num[2] == 0:
                        print(f'{casas_num[0]} Centenas ')

                elif casas_num[1] >= 2:

                    if casas_num[2] == 1:
                        print(f'{casas_num[0]} Centenas, {casas_num[1]} Dezenas e {casas_num[2]} Unidade')

                    elif casas_num[2] >= 2:
                        print(f'{casas_num[0]} Centenas, {casas_num[1]} Dezenas e {casas_num[2]} Unidades')

                    elif casas_num[2] == 0:
                        print(f'{casas_num[0]} Centenas e {casas_num[1]} Dezenas')

        elif len(txt) == 2:

            if casas_num[0] == 1:

                if casas_num[1]==0:
                    print(f'{casas_num[0]} Dezena')

                elif casas_num[1] == 1:
                    print(f'{casas_num[0]} Dezena e {casas_num[1]} Unidade')

                else:
                    print(f'{casas_num[0]} Dezena e {casas_num[1]} Unidades')

            elif casas_num[0] >= 2 :

                if casas_num[1] == 1:
                    print(f'{casas_num[0]} Dezenas e {casas_num[1]} Unidade')

                elif casas_num[1]>=2:
                    print(f'{casas_num[0]} Dezenas e {casas_num[1]} Unidades')

                else:
                    print(f'{casas_num[0]} Dezenas')


        elif len(txt) == 1:

            if casas_num[0] == 1:
                print(f'{casas_num[0]} Unidade')
            else:
                print(f'{casas_num[0]} Unidades')

    else:
        print('Digite um numero valido !')

    continuar = True
    while (continuar):

        decicao = str.upper(input('Deseja continuar? S/N: '))

        if decicao == 'S':
            continuar = False

        elif decicao == 'N':
            continuar = False
            condicao = False

        else:
            print('Digite um valor valido!')
