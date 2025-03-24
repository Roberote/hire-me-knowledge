valora = input('Digite valor A: ')
valorb = input('Digite valor B: ')

cores = {'limpa': '/033[m',
         'vermelho':'\033[31m',
         'pretoebranco': '\033[7;30m'}

print(f'SALVE {cores['vermelho']}{valora}')
