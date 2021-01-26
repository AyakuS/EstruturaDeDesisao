'''
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''

print('O crime !')
count_crime = []
contador = 0
a = count_crime.append(str.upper(input('Telefonou para a vitima? S/N: ')))
b = count_crime.append(str.upper(input('Esteve no local do crime? S/N: ')))
c = count_crime.append(str.upper(input('Mora pero da vitima? S/N: ')))
d = count_crime.append(str.upper(input('Devia para a vitima? S/N: ')))
e = count_crime.append(str.upper(input('Já trabalhou com a vitima? S/N: ')))

for n in count_crime:
    if n == 'S':
        contador = contador + 1

if contador == 2:
    print('Pessoa é suspeita de assasinato !')

elif contador == 3 or contador == 4:
    print('Pessoa é Cúmplice de assasinato !')

elif contador == 5:
    print('Pessoa é o assasino !')

else:
    print('Pessoa é inocente!')