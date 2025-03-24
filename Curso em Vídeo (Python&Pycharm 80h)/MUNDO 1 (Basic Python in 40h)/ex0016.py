# CRIE UM PROGRAMA QUE LEIA UM NÚMERO REAL
# QUALQUER PELO TECLADO E MOSTRE NA TELA
# A SUA PORÇÃO INTEIRA.
# EX: Digite um numero: 6,217 -> O Numero 6,217 tem a parte inteira 6.
# (Desafio extra: Faça da maneira mais compacta possível)
from math import trunc
n=float(input('Digite um número real (decimal): '))   #Comando para receber/ler o número.
print(f'O número {n} tem a parte inteira {trunc(n)}') #Aqui usamos a funcionalidade TRUNC da biblioteca MATH, essa funcionalidade limpa as casas depois da virgula.

# Mais compacto:

print(f'O numero {n} tem a parte inteira {n:.0f}')    #Aqui para manter uma linha de código mais compacta e, por consequência, um código inteiramente menor, nós trocamos a funcionalidade TRUNC e colocamos a permissão de
                                                      #exibir uma certa quantidade de um número float, no caso zero, transformando tudo que tenha depois da vírgula em nada, o número se torna um falso "int"