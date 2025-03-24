# Escreva um programa para aprovar o empréstimo de uma casa. O programa vai perguntar
# O valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
# O empréstimo será negado.
valorcasa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do salário: '))
anos = float(input('Digite em quantos anos será feito o pagamento: '))
meses = float(anos * 12)
prest_mensal = valorcasa / meses

prctg_minima = (salario * 30 / 100)

if prest_mensal > prctg_minima:
    print(f'As prestações excedem o limite de 30% do salário, por tanto o empréstimo está {'\033[1;31m'}NEGADO ')
    quit()
else:
    print(f'O empréstimo foi {'\033[1;32m'}aceito{'\033[m'}! \nO valor que deverá ser pago mensalmente será de {'\033[1;32m'}R${valorcasa / meses:.2f}{'\033[m'}, totalizando {'\033[1;32m'}R${valorcasa:.2f}{'\033[m'}!')
