#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

palavra = input('Digite uma palavra para saber se é um palíndromo: ').lower().strip().split().


palavras0 = ('').join(palavra)
palavras0inv = palavras0[::-1]

letras = len(palavras0)

if len(palavras0) <= 1:
    print(f'Isso não é uma palavra!')
    quit()
else:
    palindromo = False
    for c in range (0,int(letras)):
        if str(palavras0) == str(palavras0inv):
            palindromo = True
            break

    if palindromo:
        print((f'O inverso de {palavras0} é {palavras0inv}. \nTemos um palíndromo!'))
    else:
        print(f'O inverso de {palavras0} é {palavras0inv}. \nNão temos um palíndromo!')
