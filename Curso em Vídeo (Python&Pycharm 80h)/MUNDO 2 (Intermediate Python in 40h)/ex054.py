# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
totalmaior = 0
totalmenor = 0
for pess in range(1,8):

    atual = date.today().year
    nasc = int(input(f'Digite o ano de nascimento da {pess}° pessoa: '))
    idade = atual - nasc
    if idade >= 18:
        totalmaior += 1
    else:
        totalmenor += 1

print(f'Ao todo tivemos {totalmaior} pessoas maior de idade. \nTambém tivemos {totalmenor} pessoas menor de idade.')

