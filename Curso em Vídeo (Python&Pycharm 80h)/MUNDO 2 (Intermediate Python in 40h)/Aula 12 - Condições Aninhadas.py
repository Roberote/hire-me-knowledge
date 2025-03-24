nome = input('Qual é seu nome? ').title().strip()
if nome == 'Robert':
    print('Que nome bonito!')
elif nome == 'Arthur' or nome == 'Pedro' or nome == 'Murilo':
    print('Tenho um amigo com esse nome!')
elif nome in 'Marcela Yamada Mazinha':
    print('O NOME DO AMOR DA MINHA VIDA!')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia {nome}!')
