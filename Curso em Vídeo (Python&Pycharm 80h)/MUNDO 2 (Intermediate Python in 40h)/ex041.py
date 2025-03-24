# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

ano = int(input('Digite o ano de nascimento: '))

anohj = int(2025)

idade = anohj - ano

conta = anohj - idade

if idade < 0:
    print(f'Esse ser vivo ainda nem nasceu, seu arrombado.')
elif idade <= 9:
    print(f'IDADE: {idade} \nCLASSIFICAÇÃO: MIRIM')
elif idade <= 14:
    print(f'IDADE: {idade} \nCLASSIFICAÇÃO: INFANTIL')
elif idade <= 19:
    print(f'IDADE: {idade} \nCLASSIFICAÇÃO: JÚNIOR')
elif idade <= 25:
    print(f'IDADE: {idade} \nCLASSIFICAÇÃO: SÊNIOR')
else:
    print(f'IDADE: {idade} \nCLASSIFICAÇÃO: MASTER')

