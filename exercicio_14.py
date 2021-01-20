'''
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule
a sua média. A atribuição de conceitos obedece à tabela abaixo:

    Média de Aproveitamento  Conceito
         Entre 9.0 e 10.0        A
         Entre 7.5 e 9.0         B
         Entre 6.0 e 7.5         C
         Entre 4.0 e 6.0         D
         Entre 4.0 e zero        E

'''
n1 = float(input('Digite a N1 do aluno: '))
n2 = float(input('Digite a N2 do aluno: '))

media = (n1+n2)/2

if media > 9 and media <=10:
    print(f'Media = {media} ----- Conceito = A\n'
          f'APROVADO !')

elif media >= 7.5 and media < 9:
    print(f'Media = {media} ----- Conceito = B\n'
          f'APROVADO !')
elif media >= 6 and media < 7.5:
    print(f'Media = {media} ----- Conceito = C\n'
          f'APROVADO !')
elif media >= 4 and media < 6:
    print(f'Media = {media} ----- Conceito = D\n'
          f'REPROVADO !')
elif media >= 0 and media < 4:
    print(f'Media = {media} ----- Conceito = E\n'
          f'REPROVADO !')
else:
    print('Digite notas validas, entre 0 a 10 !')
