# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

cont18 = 0
contmale = 0
contfemalesub20 = 0

while True:
    nome = input('Digite o nome da {}° pessoa: ')
    print('-=' * 20)
    print('"M" para Masculino e "F" para Feminino.')
    print('-='*20)
    sexo = input('Digite o sexo da {}° pessoa: ').lower().strip()
    if sexo != 'm' and sexo != 'f':
        print(f'{'\033[4;31m'}APENAS "M" OU "F". \nReiniciando o programa, tente novamente.{'\033[m'}')
    if sexo =='m':
        contmale += 1
    idade = int(input('Digite a idade da {}° pessoa: '))
    if idade >= 18:
        cont18 += 1
    if sexo == 'f' and idade > 20:
        contfemalesub20 += 1
    continuar = input('Deseja continuar?[Y/N] \n-> ').lower()
    if continuar == 'n':
        break
    # A
print(f'Dentre as pessoas cadastradas, existem {cont18} pessoas maiores de idade. (18+) ')
    # B
print(f'Dentre as pessoas cadastradas, existem {contmale} homens cadastrados. ')
    # C
print(f'Dentre as pessoas cadastradas, existem {contfemalesub20} mulheres com menos de 20 anos de idade. ')
