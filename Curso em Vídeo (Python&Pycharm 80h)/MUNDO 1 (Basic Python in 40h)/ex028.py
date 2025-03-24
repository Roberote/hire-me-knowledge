# ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR "PENSAR" EM UM NÚMERO INTEIRO ENTRE
# 0 E 5 E PEÇA PARA O USUÁRIO TENTAR DESCOBRIR QUAL FOI O NÚMERO ESCOLHIDO PELO COMPUTADOR.
# O PROGRAMA DEVERÁ ESCREVER NA TELA SE O USUÁRIO VENCEU OU PERDEU!
import random

num = random.randint(0,5)

nome = input('Qual o seu nome? ')
print(f'Ok {nome.title()}! Vamos começar o desafio! ')
print('O Computador vai pensar em um numero de 0 a 5, você deverá adivinhar o número!')
print('Você terá duas chances!')

resp1 = int(input('Primeira tentativa! \b-> '))

if num > resp1:
    if num == resp1:
        print('Você acertou de primeira, que jogador bom! ')
    else:
        print('Você errou! O Numero é maior, tente novamente! ')
else:
    print('Você errou! O Numero é menor, tente novamente! ')

resp2 = int(input('Segunda tentativa! \b-> '))

if resp2 == num:
    print(f'Você venceu! Acertou o Numero {num}!')
else:
    print(f'Você perdeu, o numero era {num}! Recomece o jogo.')
