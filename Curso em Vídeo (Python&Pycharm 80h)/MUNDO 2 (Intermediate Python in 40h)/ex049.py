# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

base = float(input('Digite um número INTEIRO para saber a tabuada completa dele: '))

posbase = ('')

for c in range (1,11):
    print(f'{c:.0f} X {base} = {base * c}')
print('VAMO, dale')
