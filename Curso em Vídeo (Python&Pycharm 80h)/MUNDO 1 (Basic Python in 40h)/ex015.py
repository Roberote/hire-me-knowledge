# ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM PERCORRIDOS POR UM CARRO ALUGADO E A
# QUANTIDADE DE DIAS PELOS QUAIS ELE FOI ALUGADO. CALCULE O PREÇO A PAGAR, SABENDO QUE O
# CARRO CUSTA R$60 POR DIA E R$0.15 POR KM RODADO.

preco_por_dia = float(60)
preco_por_km = float(0.15)

dias = int(input('Por quantos dias o carro foi alugado? \n-> '))
km = float(input('Quantos KM foram rodados com o carro? \n-> '))
pagar = float((dias*preco_por_dia)+(km*preco_por_km))

print(f'O preço total a pagar pelo aluguel é R${pagar:.2f}!')
