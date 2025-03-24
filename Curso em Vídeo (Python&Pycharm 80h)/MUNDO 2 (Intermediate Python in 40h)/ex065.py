# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

contador = 0
soma = 0
continuar = 's'
menornum = 0
maiornum = 0

while contador != -1:
    if continuar == 's':
        num = int(input('Digite um valor: '))
        soma += num
        contador += 1
        if contador == 1:
            menornum = num
            maiornum = num
        else:
            if menornum > num:
                menornum = num
            if maiornum < num:
                maiornum = num

        continuar = input('Quer continuar? [S/N]').lower().strip()

    elif continuar == 'n':
        print(f'Finalizando o Programa...')
        break

print(f'A média entre os números digitados é igual a: {(soma / contador):.2f}')
print(f'O menor número de todos que foram digitados é o {menornum}, já o maior é o {maiornum}!')
