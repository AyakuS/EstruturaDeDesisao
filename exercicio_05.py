'''
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno
e apresentar:
    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''

n1 = float(input('Digite a n1 do aluno: '))
n2 = float(input('Digite a n2 do aluno: '))

media = (n1+n2)/2

if media >= 7 and media <= 9:
    print('Aluno Aprovado, sua nota {} ! '.format(media))
elif media < 7:
    print('Aluno Reprovado, sua nota {} ! '.format(media))
elif media == 10:
    print('Aprovado com distinção, sua nota {} ! '.format(media))