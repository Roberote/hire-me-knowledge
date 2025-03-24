# FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO ADJACENTE
# DE UM TRIÂNGULO RETÂNGULO, CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA.

from math import sqrt, pow #Importamos a funcionalidade de raíz quadrada(sqrt) e de potência(pow) do módulo Math.

cateto_a = float(input('Digite o valor do cateto adjacente: '))    #Lê o valor do cateto A.
cateto_o = float(input('Digite o valor do cateto oposto: '))       #Lê o valor do cateto B.
hipotenusa = float(sqrt(pow(cateto_a,2) + (pow(cateto_o,2))))      # Aplica o teorema de Pitágoras (Fórmula para descobrir a hipotenusa com os valores dos catetos).
print(f'A Hipotenusa desse triângulo é: {hipotenusa}. \n-> Simplificado: {hipotenusa:.2f}') #Mostra na tela o resultado de forma crua e de forma um pouco mais limpa.
