# Escreva um programa que leia um número inteiro qualquer e peça para o usuário
# qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal


print('DIGITE APENAS NUMEROS INTEIROS PARA A CONVERSÃO')

valor = int(input('Digite um número: '))



binario = bin(valor)
octal = oct(valor)
hexa = hex(valor)

conversao = input('Deseja converter para Binário, Octal ou Hexadecimal? \n-> ').title().strip()


if conversao == 'Binário' or conversao == 'Binario':
    print(f'Conversão para Binário feita! \n-> {binario}')
elif conversao == 'Hexadecimal':
    print(f'Conversão para Hexadecimal feita! \n-> {hexa}')
elif conversao == 'Octal':
    print(f'Conversão para Hexadecimal feita! \n-> {octal}')
else:
    print(f'Só aceitamos a conversão para Binário, Octal e Hexadecimal!')

quit()
