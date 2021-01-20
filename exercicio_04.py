'''
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

'''
letra = input('Digite uma letra: ')
vogal = ['a', 'e', 'i', 'o', 'u']

for n in vogal:
    
    if letra == n:
        print('Está letra é uma vogal !')
        break
    else:
        print('Está letra é uma consoante !')
        break
