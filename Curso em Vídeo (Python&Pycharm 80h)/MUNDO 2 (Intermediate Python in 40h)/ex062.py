# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

print(f'{'\033[31m'}',('-='*10),'GERADOR DE PA',('-='*10),f'{'\033[m'}')

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

contador = 1

termo = primeiro


while contador <= 10:
    print(f'{termo} → ', end='')
    contador += 1
    termo += razao
print('PAUSA')

amais = 1
contador2 = 0
contador3 = 0
contadordeamais = 0

if contador >= 10:
    while amais != -1:
        amais = int(input('Quantos termos a mais você quer ver? \n-> '))-1

        while contador2 <= amais:

            print(f'{termo} → ', end='')
            termo += razao
            contador2 += 1
            contador3 += 1
            contadordeamais += 1
        print('PAUSA')
        contador2 = 0
print(f'{'\033[4;32m'}{contadordeamais}{'\033[m'} termos foram mostrados além dos {'\033[4;32m'}10{'\033[m'} iniciais!')
print(f'{'\033[4;31m'}Programa Fechando...{'\033[m'}')


