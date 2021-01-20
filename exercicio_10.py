'''
Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''
turno = str.upper(input('Qual turno você estuda?'
              '\n M- Matutino'
              '\n V- Vespertino'
              '\n N- Noturno'
              '\n Digite o turno: '))

if turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Boa tarde!')
elif turno == 'N':
    print('Noa noite')