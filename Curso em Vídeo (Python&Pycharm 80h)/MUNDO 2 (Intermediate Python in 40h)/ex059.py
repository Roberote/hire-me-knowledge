# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa

import re, regex

opcao = ''
contag = 0
fimdoloop = 0


valor1 = int(input('Digite o 1° valor: '))
valor2 = int(input('Digite o 2° valor: '))

while fimdoloop == 0:
    print(f'')
    print(f'{'\033[31m'}-------------- ESCOLHA UMA OPÇÃO --------------{'\033[m'}')
    print(f'')
    print(f'[ {'\033[31m'}1{'\033[m'} ] Somar \n[ {'\033[31m'}2{'\033[m'} ] Multiplicar \n[ {'\033[31m'}3{'\033[m'} ] Descobrir Maior \n[ {'\033[31m'}4{'\033[m'} ] Novos Números \n[ {'\033[31m'}5{'\033[m'} ] Sair do Programa')
    opcao = int(input('Digite a opção desejada: '))
    if opcao != (1) and opcao != (2) and opcao != (3) and opcao != (4) and opcao != (5):
        print(f'{opcao} não é uma opção válida.')
        contag += 1
    if opcao == (1) or opcao == (2) or opcao == (3) or opcao == (4) or opcao == (5):
        print(f'-> Prosseguindo para a opção: {opcao}')
        if opcao == 1:
            print(f'A soma dos valores é igual a: {valor1 + valor2}')
        elif opcao == 2:
            print(f'A razão dos valores é igual a: {valor1 * valor2}')
        elif opcao == 3:
            if valor1 > valor2:
                print(f'O maior número entre os dois valores é: {valor1}')
            if valor2 > valor1:
                print(f'O maior número entre os dois valores é: {valor2}')
            if valor1 == valor2:
                print(f'Os números são iguais!')
        elif opcao == 4:
            valor1 = int(input('Digite o 1° valor: '))
            valor2 = int(input('Digite o 2° valor: '))
        elif opcao == 5:
            print(f'{'\033[31m'}PROGRAMA FECHANDO...{'\033[m'}')
            quit()
