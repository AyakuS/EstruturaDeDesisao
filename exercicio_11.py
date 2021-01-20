'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o
programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o
seguinte critério, baseado no salário atual:
    A. salários até R$ 280,00 (incluindo) : aumento de 20%
    B. salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    C. salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    D. salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    E. O salário antes do reajuste;
    F. O percentual de aumento aplicado;
    G. o valor do aumento;
    H. o novo salário, após o aumento.
'''

salario_atual = float(input('Digite seu salario: R$'))
print(f'Salario Atual: {salario_atual}')

if salario_atual <= 279:

    novo_salario = (salario_atual*0.20)+salario_atual
    vlr_aumento = (salario_atual*0.20)

    print(f'Você recebeu um aumento de 20% !\n'
          f'Salario com Reajuste: R${novo_salario}\n'
          f'Valor do aumento: R${vlr_aumento}')

elif salario_atual >= 280 and salario_atual <= 699:

    novo_salario = (salario_atual*0.15)+salario_atual
    vlr_aumento = (salario_atual * 0.15)

    print(f'Você recebeu um aumento de 15%!\n'
          f'Salario com Reajuste: R${novo_salario}\n'
          f'Valor do aumento: R${vlr_aumento}')

elif salario_atual >= 700 and salario_atual <= 1499:

    novo_salario = (salario_atual*0.10)+salario_atual
    vlr_aumento = (salario_atual * 0.10)

    print(f'Você recebeu um aumento de 10%!\n'
          f'Salario com Reajuste: R${novo_salario}\n'
          f'Valor do aumento: R${vlr_aumento}')

elif salario_atual >= 1500:

    novo_salario = (salario_atual * 0.05) + salario_atual
    vlr_aumento = (salario_atual * 0.05)

    print(f'Você recebeu um aumento de 5%!\n'
          f'Salario com Reajuste: R${novo_salario}\n'
          f'Valor do aumento: R${vlr_aumento}')