'''
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e
presentar:
    A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
    A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
    A mensagem "Aprovado com Distinção", se a média for igual a 10.
'''
n1 = float(input('Digite a N1 do Aluno: '))
n2 = float(input('Digite a N1 do Aluno: '))
n3 = float(input('Digite a N1 do Aluno: '))
media = (n1+n2+n3)/3


if media == 10:
    print(f'Aprovado com Distinção, sua média é: {media}')
elif media < 7 :
    print('Aluno Reprovado, sua média é: {:.2f}'.format(media))
elif media >= 7:
    print('Aluno Aprovado, sua média é: {:.2f}'.format(media))
