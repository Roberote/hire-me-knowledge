# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

n = int(input('Digite um número para saber seu fatorial: '))
nbase = n

contador = n

while contador != 1:
    if contador > 1:
        contador = contador - 1
        n = n * (contador)
    else:
        print(n)

if contador == 1:
    print(f'O resultado de {nbase}! é: {n}')