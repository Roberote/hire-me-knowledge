# EXCREVA UM PROGRAMA QUE LEIA DOIS NUMEROS INTEIROS E COMPARE-OS, MOSTRANDO
# NA TELA UMA MENSAGEM:
# -O PRIMEIRO VALOR É MAIOR
# O SEGUNDO VALOR É MAIOR
# NÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS

numero = int(input('Digite um numero inteiro: '))
numero2 = int(input('Digite outro numero inteiro: '))

if numero > numero2:
    print(f'O primeiro número ({numero}) é maior. ')
elif numero2 > numero:
    print(f'O segundo número ({numero2}) é maior. ')
else:
    print(f'Não existe número maior, {numero} e {numero2} são iguais. ')
