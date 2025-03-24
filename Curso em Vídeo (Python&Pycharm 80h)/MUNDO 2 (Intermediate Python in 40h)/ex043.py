# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

altura= float(input('Diga sua altura: '.strip()))
peso= float(input('Diga seu peso: '.strip()))

imc = (peso / (altura*altura))

print(f'{imc:.1f}')

if imc > 40:
    print('Obesidade Mórbida')
elif imc > 30:
    print('Obesidade')
elif imc > 25:
    print('Sobrepeso')
elif imc > 18.5:
    print('Peso Ideal.')
else:
    print('Abaixo do peso')
