# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
from os.path import split

print('Programa da PA (Progressão Aritmética)')
firsttermo = int(input('Diga o primeiro termo da PA: '))
razao = int(input('Diga a razão da PA: '))
cont = 1
for c in range (firsttermo,firsttermo+(razao*10),razao):
        a = (f'{cont}° Termo: {c}')
        cont += 1

        print(f'{c}', ' → ')
print('ACABOU')

