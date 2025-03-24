# FAÇA UM ALGORITMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO
# E MOSTRE SEU NOVO SALÁRIO, COM 15% DE AUMENTO.
funcionario = input('Nome do funcionário: ')
salario = float(input(f'Salário atual do {funcionario}: '))
porcentagem_aumento = float(input('Aumento em %: '))
aumento = float(salario * porcentagem_aumento / 100)

salarionovo = float(salario + aumento)

print(f'O Salário do {funcionario} de R${salario:.2f} recebeu um aumento de {porcentagem_aumento:.0f}%! \n Agora o salário do {funcionario} é R${salarionovo:.2f}.')
