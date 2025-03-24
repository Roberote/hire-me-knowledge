# Agora o desafio é fazer mostrar todas as variaveis na conta.
primeironumero = int(input('Digite um número: '))
segundonumero = int(input('Digite outro número: '))

resultado = primeironumero+segundonumero

print(f'O resultado da soma entre {primeironumero} e {segundonumero} é ---> {resultado}!')
# Você também pode fazer dessa maneira:
print('O resultado da soma entre {} e {} é ---> {}!'.format(primeironumero, segundonumero, resultado))

msgfinal = 'A mensagem está repetida pois são 2 comandos diferentes que podem ser feitos para a mesma coisa.'
print(f'{msgfinal}')
print(msgfinal)
