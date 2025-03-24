# Desenvolva um programa que leia o comprimento de
# três retas e diga ao usuário se elas podem ou não
# formar um triângulo.

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('Seja bem-vindo ao analisador de triângulo!')
print('Você deverá digitar os valores de 3 retas, e o programa irá te falar se é possível ou não montar um triângulo com elas!')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

reta1 = float(input('Digite o valor da primeira reta: '))
reta2 = float(input('Digite o valor da segunda reta: '))
reta3 = float(input('Digite o valor da terceira reta: '))

if reta1 + reta2 > reta3:

    if reta1 + reta3 > reta2:

        if reta2 + reta3 > reta1:
          print('dá pra fazer triangulo')
        else:
            print('dá pra fazer triangulo')
    else:
        print('dá pra fazer triangulo')
else:
    print('nao da')

