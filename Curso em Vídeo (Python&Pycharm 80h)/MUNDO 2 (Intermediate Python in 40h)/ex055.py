# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maiorpeso = 0
menorpeso = 0

for p in range(1,6):
    peso = float(input(f'Digite o peso da {p}° pessoa: '))
    if p == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso

print(f'O Maior peso é {maiorpeso}Kg. \nO Menor peso é {menorpeso}Kg.')
