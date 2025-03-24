# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

somaidades = 0
maioridade = 0
menoridade = 0
maioridadehomem = 0
nomehomemvelho = ''

for p in range(1,5):
    print(f'{'\033[2;31m'}--------------- {p}° PESSOA ---------------{'\033[m'}')
    nome = input(f'Digite o nome da {p}° pessoa: ')
    idade = int(input(f'Digite a idade da {p}° pessoa: '))
    sexo = input(f'Digite o sexo[M/F] da {p}° pessoa: ').strip().lower()
    # MÉDIA DE IDADE:

    somaidades += idade
    # VER QUEM É O HOMEM MAIS VELHO


    if not sexo in 'mf':
        print(f'{'\033[2;31m'}Q sexo é esse, orelhudo do caralho \nDigite M para HOMEM e F para MULHER!{'\033[m'}')
        quit()
    if sexo == 'm':
        if p == 1:
            maioridadehomem = idade
            nomehomemvelho = nome
        else:
            if idade > maioridadehomem:
                maioridadehomem = idade
                nomehomemvelho = nome

    # Para saber quantas mulheres com menos de 20 anos tem
    else:
        if idade < 20:
            menoridade += 1
        else:
            menoridade += 0


# Fora do laço

# Resposta para a média de idade:
print(f'A média de idades é: {'\033[1;32m'}{(somaidades / 4):.2f}{'\033[m'}')
# Resposta para quantas mulheres tem menos de 20 anos:
print(f'Existem {'\033[1;32m'}{menoridade}{'\033[m'} mulheres com menos de 20 anos.')
# Resposta para qual o nome do homem mais velho:
print(f'Homem mais velho: {'\033[1;32m'}{nomehomemvelho}{'\033[m'}')

