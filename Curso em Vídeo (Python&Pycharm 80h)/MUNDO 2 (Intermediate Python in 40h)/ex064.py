# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

print('-='*30)
print(f'{'\033[4;31m'}SOMANDO NÚMEROS!{'\033[m'}')
print('-='*30)

num = 0
contnum = 0
soma = 0
while num != 999:
    num = int(input('Digite um valor: '))
    contnum += 1
    soma += num

print(f'A soma dos valores digitados é igual a : {soma} \nO total de números digitados foi: {contnum}')
