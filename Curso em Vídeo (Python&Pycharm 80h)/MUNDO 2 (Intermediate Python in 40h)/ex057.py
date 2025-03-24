# Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

female = 0
male = 0
contador = 0

while contador < 1:
    sexo = input('Digite o seu sexo [M/F]: ').strip().lower()
    if sexo != 'm' and sexo != 'f':
        print(f'{'\033[0;31m'}Somente "M" para MASCULINO ou "F" para FEMININO. Digite novamente!{'\033[m'}')
    else:
        if sexo == 'm':
            male += 1
            contador += 1
        elif sexo == 'f':
            female += 1
            contador += 1

if male == 1:
    print(f'Sexo escolhido: {'\033[0;32m'}Masculino{'\033[m'}')
elif female == 1:
    print(f'Sexo escolhido: {'\033[0;32m'}Feminino{'\033[m'}')
