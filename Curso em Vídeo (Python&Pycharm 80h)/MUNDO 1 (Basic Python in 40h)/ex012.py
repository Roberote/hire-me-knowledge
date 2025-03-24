# FAÇA UM ALGORITMO QUE LEIA O PREÇO
# DE UM PRODUTO E MOSTRE SEU NOVO
# PREÇO, COM 5% DE DESCONTO.
preco = float(input('Qual o valor do produto? \n->'))
descontopct = float(input('Quanto de desconto será aplicado em %? \n->'))

desconto = float(preco*descontopct/100)
valorfinal = float(preco-desconto)

print(f'O produto que custa R${preco:.2f} com um desconto de {desconto}%, estará custando agora R${valorfinal:.2f}!')
