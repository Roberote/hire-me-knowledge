import re

nome = input('Digite seu nome: ')

nome_formatado = nome.title()

if re.search(r'\bSilva\b', nome_formatado):
    if re.search(r'-Silva\b|\bSilva-', nome_formatado):
        print(f'O nome {nome_formatado} tem Silva, porém conectado a outro nome por hífen.')
    else:
        print(f'O nome {nome_formatado} tem Silva.')
else:
    print(f'O nome {nome_formatado} não tem Silva.')

