# ESCREVA UM PROGRAMA QUE PERGUNTE O SALÁRIO DE UM FUNCIONÁRIO E CALCULE O VALOR DO SEU AUMENTO
# PARA SALÁRIOS SUPERIORES A R$1.250,00 CALCULE UM AUMENTO DE 10%.
# PARA SALÁRIOS INFERIORES OU IGUAIS, O AUMENTO É DE 15%.

nome = input('Digite o nome do(a) funcionário(a): ').title().strip()
salario = float(input(f'Salário de {nome}: '))

if salario <= 1250:
    print(f'O aumento do salário de {nome} será de 15%. \nO aumento acrescentará R${salario * 15 / 100:.2f}. \n-> O novo salário de {nome} é {(salario * 15 / 1000) + salario:.2f}')
elif salario >= 1251:
    print(f'O aumento do salário de {nome} será de 10%. \nO aumento acrescentará R${salario * 10 / 100:.2f}. \n-> O novo salário de {nome} é {(salario * 10 / 1000) + salario:.2f}')

