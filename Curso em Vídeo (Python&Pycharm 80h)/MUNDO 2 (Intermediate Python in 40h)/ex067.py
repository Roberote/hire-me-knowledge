# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

print(f'{'\033[31m'}-={'\033[m'}'*30)
print(f'DESCUBRA A TABUADA DE QUALQUER NÚMERO! \nPARA PARAR O PROGRAMA DIGITE QUALQUER NÚMERO NEGATIVO.')
print(f'{'\033[31m'}-={'\033[m'}'*30)


cont = 0

while True:
    n = int(input('Digite o valor: '))
    if n <= -1:
        break
    while cont <= 9:

        cont += 1
        # tabuada
        print(f'{n} X {cont} = {n*cont}')

    print(f'{'\033[32m'}-='*15,f'FIM DA TABUADA DO NUMERO {n}',f'-='*15,f'{'\033[m'}')
    cont = 0
    if n <= -1:
        break

print(f'{'\033[31m'}PROGRAMA FECHANDO...{'\033[m'}')