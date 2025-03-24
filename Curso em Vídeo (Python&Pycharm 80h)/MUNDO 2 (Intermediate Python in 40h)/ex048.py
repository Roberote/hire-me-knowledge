# Faça um programa que calcule a soma entre todos os números que
# são múltiplos de três e que se encontram no intervalo de 1 até 500.

from time import sleep

basezero = 0

for c in range (3,501,3):
    sleep(0)

print(f'{'\033[0;36m'}Calculando...{'\033[m'}')
sleep(2)

print(f'A somatória entre todos os números que são múltiplos de três e que se encontram entre 1 e 500 é igual a: {'\033[0;32m'}{c+basezero}{'\033[m'}')
