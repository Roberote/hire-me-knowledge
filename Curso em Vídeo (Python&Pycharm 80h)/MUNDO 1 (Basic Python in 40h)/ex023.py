# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO DE 0 A 9999 E MOSTRE
# NA TELA CADA UM DOS DIGITOS SEPARADOS.
# EX> Digite um numero: 1834 >>>> unidade = 4, dezena = 3, centena = 8, milhar = 1

n = int(input('Digite um numero de 0 a 9999: '))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10


print(f'O Numero digitado foi {n}')


print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
