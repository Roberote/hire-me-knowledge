# CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA EM REAIS
# E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR
#
# --=Considere US$1.00 = R$3,27
print('Pedimos que, por gentileza, faça uso apenas de "." para divisão de reais e centavos.')
reais = float(input('Digite quantos reais tem na sua carteira: '))

dolar = float(reais*(1/3.27)) #o valor de reais que o usuario colocou vezes a cotação do dólar, escrevemos desse jeito pois é UM dolar que vale 3,27 reais

print(f'Você pode comprar US${dolar:.2f} com os seus R${reais:.2f}!') # :.2f eu uso pra mostrar apenas duas casas depois do float, ou seja, 1.4242424242 = 1.42
print('Lembrando que estamos usando a cotação de 2017 para a conversão! >>> (US$1.00 = R$3.27)')
