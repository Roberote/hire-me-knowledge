# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random

nbot = random.randint(1,10)
tentativas = 0


print(f'{'\033[0;31m'}------------ ADIVINHE ------------{'\033[m'}')
print(f'{'\033[0;31m'}O Bot já pensou em um número! Tente acertar com tentativas ilimitadas!{'\033[m'}')


adivinhar = int(0)

while adivinhar != nbot:
    adivinhar = int(input(f'Digite um número: '))

    if adivinhar > nbot:
        print(f'{'\033[0;33m'}Tente um número MENOR!{'\033[m'}')
        tentativas += 1
    if adivinhar < nbot:
        print(f'{'\033[0;33m'}Tente um número MAIOR!{'\033[m'}')
        tentativas += 1

if adivinhar == nbot:
    print(f'Você acertou! \n{'\033[0;31m'}------------ FIM DE JOGO ------------{'\033[m'}')

tentativafinal = 1 + tentativas
print(f'Você acertou na {tentativafinal}° tentativa! ')