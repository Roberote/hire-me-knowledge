# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random

print(f'{'\033[31m'}-='*30,f'{'\033[m'}')
print(f'{'\033[32m'}               VAMOS JOGAR PAR OU ÍMPAR!                 {'\033[m'}')
print(f'{'\033[31m'}-='*30,f'{'\033[m'}')

contador = 0

while True:
    n = int(input('Digite um valor: '))

    parouimpar = input('Par ou Ímpar? [P/I]').lower().strip()
    if parouimpar != 'p' and parouimpar != 'i':
        print(f'{'\033[31m'}APENAS "P" PARA PAR OU "I" PARA IMPAR!{'\033[m'}')
        print(f'{'\033[31m'}Reinicie o programa e tente novamente.{'\033[m'}')
        quit()
    nbot = random.randint(0,9)
    print(f'O {'\033[4;32m'}Bot Jonas{'\033[m'} jogou {'\033[4;32m'}{nbot}{'\033[m'}!')
    print(f'{'\033[31m'}-='*30,f'{'\033[m'}')
    if (nbot+n) % 2 == 0 and parouimpar == 'p':
        print(f'{n+nbot} é {'\033[32m'}PAR!{'\033[m'}')
        print(f'Você venceu, {'\033[4m'}MAIS UM JOGO!{'\033[m'}')
        contador += 1
        print(f'{'\033[31m'}-=' * 30, f'{'\033[m'}')
    elif (nbot+n) % 2 > 0 and parouimpar == 'i':
        print(f'{n + nbot} é {'\033[32m'}ÍMPAR!{'\033[m'}')
        print(f'Você venceu, {'\033[4m'}MAIS UM JOGO!{'\033[m'}')
        contador += 1
        print(f'{'\033[31m'}-=' * 30, f'{'\033[m'}')
    elif (nbot+n) % 2 == 0 and parouimpar == 'i':
        print(f'{n+nbot} é {'\033[31m'}PAR!{'\033[m'}')
        break
    elif (nbot+n) % 2 > 0 and parouimpar == 'p':
        print(f'{n + nbot} é {'\033[31m'}ÍMPAR!{'\033[m'}')
        break
print(f'Você perdeu, {'\033[31m'}FIM DE JOGO!{'\033[m'}')
print(f'Você jogou {'\033[4;33m'}{contador + 1}{'\033[m'} partidas e ganhou {'\033[4;32m'}{contador}{'\033[m'} delas!')
