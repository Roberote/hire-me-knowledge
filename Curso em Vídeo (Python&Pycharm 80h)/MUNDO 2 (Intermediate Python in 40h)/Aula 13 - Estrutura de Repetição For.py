qntsn = int(input('Quantidade de numeros para somar: '.strip()))

base = 0

for c in range(1,qntsn+1):
    a = int(input(f'Fala os numeros para somar aí {'\033[0;31m'}dog{'\033[m'}: '))
    base = base+a
print(f'Fim da contagem. A Somatória de todos os valors é: {base}')
