#################################################################
# Crie um programa que faça o computador jogar Jokenpô com você.#
#################################################################

import random

resetcor = '\033[m'
print(f'{'\033[1m'}Para jogar Jokenpô, escolha entre uma das opções, em seguida o bot irá revelar o que ele já jogou!{resetcor} \n OPÇÕES PARA JOGAR: \n-> {'\033[0;37m'}PEDRA{resetcor} - {'\033[0;31m'}1{'\033[m'} \n-> {'\033[0;32m'}TESOURA{resetcor} - {'\033[0;31m'}2{'\033[m'} \n-> {'\033[m'}PAPEL{resetcor} - {'\033[0;31m'}3{resetcor}')
print(f'Coloque o {'\033[4;31m'}NÚMERO{resetcor} correspondente com a opção que você quer jogar!')
opcao = int(input('Selecione a opção: '))

if opcao > 3 or opcao < 1:
    print(f'{'\033[2;31m'}APENAS OPÇÕES 1, 2 OU 3!{resetcor} ')
    quit()

decisao = random.randint(1,3)
corvoce = '\033[1;35m'
corbot = '\033[1;33m'

# 1=pedra 2=tesoura 3=papel
if decisao == 1:
    print(f'{corbot}Bot Jonas:{resetcor} Pedra!')
elif decisao == 2:
    print(f'{corbot}Bot Jonas:{resetcor} Tesoura!')
else:
    print(f'{corbot}Bot Jonas:{resetcor} Papel!')

print(f'{'\033[1;31m'}---------------=VS=---------------{resetcor}')

if opcao == 1:
    print(f'{corvoce}Você:{resetcor} Pedra!')
elif opcao == 2:
    print(f'{corvoce}Você:{resetcor} Tesoura!')
else:
    print(f'{corvoce}Você:{resetcor} Papel!')


if (opcao == 1 and decisao == 1):
    print(f'{'\033[0;33m'}EMPATE!{resetcor}')
elif (opcao == 2 and decisao ==1 ):
    print(f'{'\033[2;31m'}VOCÊ PERDEU!{resetcor}')
elif (opcao == 3 and decisao == 1):
    print(f'{'\033[0;32m'}VOCÊ VENCEU!{resetcor}')
elif (opcao == 1 and decisao == 2):
    print(f'{'\033[0;32m'}VOCÊ VENCEU!{resetcor}')
elif (opcao == 2 and decisao == 2):
    print(f'{'\033[0;33m'}EMPATE!{resetcor}')
elif (opcao == 3 and decisao == 2):
    print(f'{'\033[2;31m'}VOCÊ PERDEU!{resetcor}')
elif (opcao == 1 and decisao == 3):
    print(f'{'\033[2;31m'}VOCÊ PERDEU!{resetcor}')
elif (opcao == 2 and decisao == 3):
    print(f'{'\033[0;32m'}VOCÊ VENCEU!{resetcor}')
elif (opcao == 3 and decisao == 3):
    print(f'{'\033[0;33m'}EMPATE!{resetcor}')

