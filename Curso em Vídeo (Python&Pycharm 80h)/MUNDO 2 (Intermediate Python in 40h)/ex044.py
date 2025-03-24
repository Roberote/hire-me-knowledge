# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – 1 à vista dinheiro/cheque: 10% de desconto
# – 2 à vista no cartão: 5% de desconto
# – 3 em até 2x no cartão: preço formal
# – 4 3x ou mais no cartão: 20% de juros

produto = input('Digite o produto que deseja comprar: ')
quantidade = int(input(f'Digite a quantidade de {produto} que deseja comprar: '))
preco = float(input(f'Digite o preço de 1x {produto}: '))

print(f'Para comprar {'\033[0;32m'}{quantidade}x{'\033[m'} de {'\033[0;32m'}{produto}{'\033[m'}, você pode optar por algumas opções de pagamento com condições específicas para cada uma delas. \n-> À vista no dinheiro/cheque: 10% de desconto. - {'\033[0;31m'}1 {'\033[m'} \n-> À vista no Cartão: 5% de desconto. - {'\033[0;31m'}2 {'\033[m'} \n-> Em até 2x no Cartão: Preço original - {'\033[0;31m'}3 {'\033[m'} \n-> Em 3x ou mais no Cartão: 20% de juros - {'\033[0;31m'}4 {'\033[m'}')
forma = int(input(f'Digite o  - {'\033[0;31m'}NÚMERO {'\033[m'} da opção desejada: '))

valorcompra = (quantidade * preco)

formaum = valorcompra * 0.90

formadois = valorcompra * 0.95

formaquatro = valorcompra * 1.20

if forma == 1:
    print(f'O Valor final de {'\033[0;33m'}{quantidade}x{'\033[m'} {'\033[0;33m'}{produto}{'\033[m'} é: {'\033[0;32m'}R${formaum:.2f}')

elif forma == 2:

        print(f'O Valor final de {'\033[0;33m'}{quantidade}x{'\033[m'} {'\033[0;33m'}{produto}{'\033[m'} é: {'\033[0;32m'}R${formadois:.2f}')

elif forma == 3:

            print(f'O Valor final de {'\033[0;33m'}{quantidade}x{'\033[m'} {'\033[0;33m'}{produto}{'\033[m'} é: {'\033[0;32m'}R${quantidade * preco:.2f}')

else:

    print(f'O Valor final de {'\033[0;33m'}{quantidade}x{'\033[m'} {'\033[0;33m'}{produto}{'\033[m'} é: {'\033[0;32m'}R${formaquatro:.2f}')

