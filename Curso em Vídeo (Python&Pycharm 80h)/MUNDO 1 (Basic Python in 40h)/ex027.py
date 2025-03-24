# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
# o primeiro e o ultimo nome separadamente.
# Exemplo: Ana Maria de Souza
# primeiro nome = Ana
# Ultimo nome = Souza


nome = input('Digite seu nome: ')

nomefrmt = nome.title()

nomediv = nomefrmt.split()

print(f'-> Nome: {nomefrmt}')

print(f'-> O primeiro nome é {nomediv[0]}! \n-> O último nome é {nomediv[len(nomediv) - 1]}!')
