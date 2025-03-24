n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1+n2

print(f'A soma dos numeros {n1} e {n2} é igual a {s}!')

tantofaz = input('Digite "OK" para confirmar a analise do resultado {}!'.format(s))

inicioanalise = 'Análise iniciando!'
print(inicioanalise)
print(type(s))
print('É um resultado que possúi incógnita? R:', (f'{s}'.isalpha()))
print('')
print('Obrigado por utilizar o nosso sistema de soma e análise de resultado!')
