'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende
do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não
é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa
deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
    No exemplo o valor da hora é 5 e a quantidade de hora é 220.

    Salário Bruto: (5 * 220)            : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
'''
salario_hr = float(input('Valor do salario hora: R$'))
qtd_hr_trab = float(input('Quantidade de horas trabalhadas: '))

salario_bruto = salario_hr*qtd_hr_trab
sindicato = salario_bruto*0.03
fgts = salario_bruto*0.11

print(f'Salario Bruto : R${salario_bruto}')

if salario_bruto <= 900:
    inss = (salario_bruto * 0.10)
    total_desconto = sindicato + inss
    salario_liquido = salario_bruto - total_desconto

    print('(-) IR (5%): ISENTO')
    print(f'(-) INSS (10%): {inss}')
    print(f'FGTS (11%): {fgts}')
    print(f'Total dos Descontos {total_desconto}')
    print(f'Salário Liquido: {salario_liquido}')

elif salario_bruto >= 901 and salario_bruto <= 1500:

    ir = salario_bruto * 0.05
    inss = (salario_bruto * 0.10)
    total_desconto = sindicato + inss + ir
    salario_liquido = salario_bruto - total_desconto

    print(f'(-) IR (5%): {ir}')
    print(f'(-) INSS (10%): {inss}')
    print(f'FGTS (11%): {fgts}')
    print(f'Total dos Descontos {total_desconto}')
    print(f'Salário Liquido: {salario_liquido}')

elif salario_bruto >= 2500 :

    ir = salario_bruto * 0.10
    inss = (salario_bruto * 0.10)
    total_desconto = sindicato + inss + ir
    salario_liquido = salario_bruto - total_desconto

    print(f'(-) IR (10%): {ir}')
    print(f'(-) INSS (10%): {inss}')
    print(f'FGTS (11%): {fgts}')
    print(f'Total dos Descontos {total_desconto}')
    print(f'Salário Liquido: {salario_liquido}')




