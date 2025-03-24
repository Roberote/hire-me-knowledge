# Faça um programa que leia um número inteiro e
# diga se ele é ou não um número primo.
from math import sqrt
print(f'{'\033[0;31m'}Atenção: {'\033[m'}Um número primo é aquele que só é divisível por 1 ou por ele mesmo!')
num = int(input('Digite um número INTEIRO para saber se é primo: '))

if num <= 1:
    print('O número 1 ou números inferiores a ele não são primos.')
    quit()
else:
    eprimo = True
    for c in range(2,int(sqrt(num)) + 1):
        if num % c == 0:
            eprimo = False
            break
if eprimo:
    print(f'{num} {'\033[0;32m'}é primo{'\033[m'}!')
else:
    print(f'{num} {'\033[0;31m'}não é primo{'\033[m'}!')

