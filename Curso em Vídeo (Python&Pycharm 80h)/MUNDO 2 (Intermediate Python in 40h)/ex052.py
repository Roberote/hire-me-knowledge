# Faça um programa que leia um número inteiro e
# diga se ele é ou não um número primo.
from math import sqrt

num = int(input('Digite um numero inteiro para saber se é primo ou não: '))

if (num <= 1):
    print('ta de saca né paizão, digita um numero direito, imbecil.')
else:
    eprimo = True
    for c in range(2, int(sqrt(num) + 1)):
        if num % c == 0:
            eprimo = False
            break
if eprimo:
    print(f'{num} é primo!')
else:
    print(f'{num} não é primo!')
