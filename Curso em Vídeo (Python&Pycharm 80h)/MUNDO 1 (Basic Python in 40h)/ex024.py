# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE
# E DIGA SE ELA COMEÇA OU NÃO COM A PALAVRA "SANTO".

cidade = input('Digite o nome de uma cidade: ')

santo = 'Santo '
santomin = (santo.lower())
cidade_formatada = cidade.title()

if cidade_formatada.find(santo) == 0:
    print(f'A Cidade {cidade_formatada} começa com {santo}')
else:
    print(f'A cidade {cidade_formatada} não começa com {santo}')


if cidade_formatada.find('Santos') == 0:
    print('Na verdade essa cidade é apenas Santos, não "Santo ----"')
else:
     print('')
