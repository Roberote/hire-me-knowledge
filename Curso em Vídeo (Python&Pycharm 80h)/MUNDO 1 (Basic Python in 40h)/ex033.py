# FAÇA UM PROGRAMA QUE LEIA TRÊS NUMEROS E MOSTRE QUAL É O MAIOR E QUAL É O MENOR.
numa = float(input('Digite um numero: '))
numb = float(input('Digite outro numero: '))
numc = float(input('Digite outro numero: '))


#DESCOBRIR O MAIOR:
if numa > numb and numa > numc:
    print(f'{numa:.2f} é o maior numero!')
elif numb > numa and numb > numc:
    print(f'{numb:.2f} é o maior numero!')
elif numc > numa and numc > numb:
    print(f'{numc:.2f} é o maior numero!')


# DESCOBRIR O MENOR:
if numa < numb and numa < numc:
    print(f'{numa:.2f} é o menor numero!')
elif numb < numa and numb < numc:
    print(f'{numb:.2f} é o menor numero!')
elif numc < numa and numc < numb:
    print(f'{numc:.2f} é o menor numero!')

