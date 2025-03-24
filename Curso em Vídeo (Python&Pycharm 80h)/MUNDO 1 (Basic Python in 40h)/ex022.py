# CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO
# DE UMA PESSOA E MOSTRE:
# > O NOME COM TODAS AS LETRAS MAIÚSCULAS
# > O NOME COM TODAS AS LETRAS MINÚSCULAS
# > QUANTAS LETRAS NO TOTAL (SEM CONSIDERAR ESPAÇOS)
# > QUANTAS LETRAS TEM O PRIMEIRO NOME.

nome = input('Digite o seu nome completo! \n>>>>> ')

print(f'Nome completo com todas as letras maiúsculas! \n>>>>> {nome.upper()}') #Transforma todas as letras do nome em maiúsculas.
print('')
print(f'Nome completo com todas as letras minúsculas! \n>>>>> {nome.lower()}') #Transforma todas as letras do nome em minúsculas.
print('')
primeironome = nome.split() #Remove os espaços (Separa somente as palavras do input).
nomereescrito = '0'.join(primeironome) #Transforma os espaços removidos em zeros (0).
count0 = (nomereescrito.count('0')) #Cria uma variável que conta a quantidade de zero pra remover na conta de letras do nome.
print(f'O Nome completo possúi {len(nome)} caracteres incluindo espaços!') #Conta todos os caracteres digitados.
print('')
print(f'O Nome completo possúi {int(len(nomereescrito)) - count0} letras!') #Conta todas as letras. Int para transformar de string pra numeros, depois a conta com a quantidade total de caracteres - os espaços transformados em 0 que foram contados na variável count0.
print('')

print(f'O Primeiro nome possúi {len(primeironome[0])} letras!') #Pega o split e somente a primeira palavra(0), no caso o primeiro nome.
