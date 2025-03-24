nome = input('Digite seu nome: ').strip()

nomediv = nome.title().split()

if 'Silva' in nomediv:
    print(f'O Nome {nome.title()} tem Silva.')
else:
    print(f'O Nome {nome.title()} não tem Silva.')
print('xD')
