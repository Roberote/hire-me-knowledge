# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

print(f'{'\033[31m'}',('-='*10),'GERADOR DE PA',('-='*10),f'{'\033[m'}')

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

termo = primeiro
cont = 1

while cont <= 10:
    print(f'{termo} → ', end='')
    cont += 1
    termo += razao
print('Fim')
