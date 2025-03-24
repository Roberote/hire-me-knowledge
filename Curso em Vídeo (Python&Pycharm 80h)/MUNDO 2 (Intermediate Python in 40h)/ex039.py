# FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME, DE ACORDO COM SUA IDADE:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
print(f'Siga o exemplo: {'\033[0;31m'}(xx/xx/xxxx){'\033[m'}')
nasc = input('Digite seu ano de nascimento: ')

nsepnasc = nasc.split('/')

nascdia = nsepnasc[0]
nascmes = nsepnasc[1]
nascano = int(nsepnasc[2])

hoje = '02/03/2025'

nsephoje = hoje.split('/')

hojedia = nsephoje[0]
hojemes = nsephoje[1]
hojeano = int(nsephoje[2])

if (hojeano - nascano) == 18:
    print(f'Você faz 18 anos esse ano, vá se alistar agora mesmo!')
elif (hojeano - nascano) > 18:
    print(f'O prazo de alistamento já passou, você nasceu em {nascano} e hoje você tem {(hojeano - nascano)} anos ({(hojeano - nascano) - 18} anos de atraso). você deverá comparecer a uma junta militar o quanto antes!')
else:
    print(f'Você tem {(hojeano - nascano)} anos e irá se alistar somente daqui {((18 - (hojeano - nascano) ))} anos, não se preocupe!')
