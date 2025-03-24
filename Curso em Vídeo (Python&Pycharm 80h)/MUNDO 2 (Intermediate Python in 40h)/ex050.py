# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

soma = 0 # Aplicando uma variavel pra usar na soma dos numeros pares
cont = 0 # Aplicando uma contagem de quantos numeros eram pares
for c in range (1,7): # iniciando uma repetição
    a = int(input(f'Digite o {c}° numero: ')) # usuario vai digitar esses numeros, o {c}° é pra usar o 1 a 6 da repetição pra fazer "1°, 2° e etc.
    if a % 2 == 0: # Se o numero q foi digitado no A nessa volta da repetição for divisivel por 2, ou seja, dividido por 2 resto == a zero, ele vai somar o numero na variavel soma
        soma += a # aqui eu falo q NESSA repetição, if variavel "a" for divisivel por 2, ou seja, se for par, ele vai somar a zero. Isso repete sempre que um numero par é digitado, então se eu digito 2, depois 4, ele vai somar 2 + 4 + proximo par da repetição + 0 (esse zero é a base da variavel soma, que é zero, colocamos no inicio)
        cont += 1 # aqui ele vai adcionar 1 na cont (contagem) sempre que o if for ativado.

print(f'Você informou {cont} numeros pares e a soma deles é igual a: {soma}') # fala o resultado final e a contagem de pares


