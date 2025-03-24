idade = int(input('Quantos anos você tem? '))


if idade >= 18:
    if idade >= 40:
        print(f'Você é uma MÁQUINA DA ANTIGUIDADE, pois sua idade é {idade}!')
    else:
        print(f'Você é maior de idade pois sua idade é {idade}.')
else:
    print(f'Você é um mucilon, pois sua idade é {idade}, não é maior de idade!')

idadeamigo = int(input('Idade do seu amigo: '))
print(f'Seu amigo é uma MAQUINA DA ANTIGUIDADE com seus {idadeamigo}' if idadeamigo>=40 else f'Você é maior de idade pois sua idade é {idade}.' if idadeamigo>= 18  else f"Seu amigo não é maior de idade pois tem {idadeamigo}, mucilonzinho")
