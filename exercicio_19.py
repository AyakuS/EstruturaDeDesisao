num = int(input('Digite um numero menor que 1000: '))

if num < 1000:

    txt = str(num)
    casas_num = []

    for n in range (len(txt)):          #Laço faz a inserção e transformação para inteiro para a lista casas_num
        casas_num.append(int(txt[n]))

    if len(txt) == 3:

        if casas_num[0] == 1:
            print(f'{casas_num[0]} Centena')
            if casas_num[1] == 1:
                print(f'{casas_num[1]} Dezena')
                if casas_num[2] == 1:
                    print(f'{casas_num[2]} Unidade')
                elif casas_num[2] >= 2:
                    print(f'{casas_num[2]} Unidades')

            elif casas_num[1]>=2:
                print(f'{casas_num[1]} Dezenas')
                if casas_num[2] == 1:
                    print(f'{casas_num[2]} Unidade')
                elif casas_num[2] >= 2:
                    print(f'{casas_num[2]} Unidades')
        elif casas_num[0] >= 2:
            
            print(f'{casas_num[0]} Centenas')
            if casas_num[1] == 1:
                print(f'{casas_num[1]} Dezena')
                if casas_num[2] == 1:
                    print(f'{casas_num[2]} Unidade')
                elif casas_num[2] >= 2:
                    print(f'{casas_num[2]} Unidades')

            elif casas_num[1] >= 2:
                print(f'{casas_num[1]} Dezenas')
                if casas_num[2] == 1:
                    print(f'{casas_num[2]} Unidade')
                elif casas_num[2] >= 2:
                    print(f'{casas_num[2]} Unidades')
    
    elif len(txt) == 2:
        print()

else:
    print('Digite um numero valido !')
