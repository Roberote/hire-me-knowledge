# ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO.
# SE ELE ULTRAPASSAR 80KM/H, MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO.
# A MULTA CUSTA R$7,00 POR CADA KM ACIMA DO LIMITE.

km = int(input('Qual a velocidade do carro que o Radar registrou? \n-> '))

if km >= 81:
    print(f'Você foi multado! \nSua multa deverá ser paga antes do fim do mês no valor de R${float((km - 80)*7):.2f}!')
else:
    print('A Velocidade está dentro da regularidade da pista. \nNenhuma multa deverá ser aplicada.')

if km == 80:
    print(f'Mas tome muito cuidado, {km}Km/h é o limite da pista, recomendamos que diminua um pouco a sua velocidade para garantir que ficará dentro do regulamento da pista.')

