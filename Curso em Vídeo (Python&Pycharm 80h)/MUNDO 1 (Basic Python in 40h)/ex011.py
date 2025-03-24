# FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS, CALCULE
# A SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTÁ-LA, SABENDO QUE
# CADA LITRO DE TINTA, PINTA UMA ÁREA DE 2m²

print('---=BEM-VINDO AO PROGRAMA QUE IRÁ AJUDAR OS PINTORES DO BRASIL!=---')
print('Vamos te ajudar a calcular quanto de tinta você irá comprar pra pintar a parede toda!')
print('Considere que cada litro de tinta pinta 2m².')
print('============================================================================')

altura = float(input('Altura da parede em metros: '))
largura = float(input('Largura da parede em metros: '))
cor = input('Qual cor você deseja pintar a parede? \n -> ')
loja = input('Em qual loja vai comprar? \n -> ')
area = float(altura*largura)
litros = float(area/2)

print(f'A parede possui {area:.1f}m², para pintá-la completamente com a tinta {cor} da loja {loja}, \nvocê precisará comprar {litros}L de tinta!')
