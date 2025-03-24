# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep

sec = int(input('Quantos segundos a contagem deve ter? -> '))

for c in range (sec, -1 , -1):
    print(c)
    sleep(1)
print(f'{'\033[0;31m'}B{'\033[0;32m'}O{'\033[0;33m'}O{'\033[0;34m'}O{'\033[0;35m'}O{'\033[0;36m'}M{'\033[m'}')