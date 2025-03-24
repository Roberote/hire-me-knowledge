# Desenvolva um programa que pergunta a distância de uma viagem em KM.
# Calcule o preço da passagem, cobrando R$0.50 por Km rodado para viagens até 200Km.
# E R$0.45 para viagens mais longas do que 200Km.

local1 = input('Para onde vai viajar? ').title().strip()
local2 = input('De onde vai partir? ').title().strip()


distancia = float(input('Qual a distância da viagem em KM? \n-> '))

if distancia <= 200:
    preco = float(distancia * 0.50)
else:
    preco = float(distancia * 0.45)


if distancia <= 200:
    print(f'A viagem de {local1} até {local2} levará {distancia}Km! \nPorém, por ser uma distância de até 200km, a promoção não será aplicada. Portanto, o valor total da viagem será R${preco}!')
else:
    print(f'A viagem de {local1} até {local2} levará {distancia}Km! \nPor ser uma distância acima de 200km, a promoção será aplicada. Portanto, o valor total da viagem será apenas R${preco}!')

print('A equipe de aviação deseja uma ótima viagem a todos!')
