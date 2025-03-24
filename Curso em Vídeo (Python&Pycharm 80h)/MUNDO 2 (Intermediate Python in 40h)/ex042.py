# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

# Exibe uma mensagem em letras maiúsculas pedindo ao usuário para digitar os três lados do triângulo.
print(('Digite as 3 distancias de um triangulo.').upper())

# Solicita ao usuário que insira o valor do primeiro lado e converte o valor para float (número decimal).
l1 = float(input('Digite o valor do primeiro lado: '.strip()))
# Solicita ao usuário que insira o valor do segundo lado e converte o valor para float (número decimal).
l2 = float(input('Digite o valor do segundo lado: '.strip()))
# Solicita ao usuário que insira o valor do terceiro lado e converte o valor para float (número decimal).
l3 = float(input('Digite o valor do terceiro lado: '.strip()))

# Verifica se os valores fornecidos podem formar um triângulo.
# A condição de existência de um triângulo é que a soma de dois lados seja maior que o terceiro lado.
if (l1 + l2 > l3):
    # Se a soma de l1 e l2 for maior que l3, verifica a próxima condição.
    if l3 + l2 > l1:
        # Se a soma de l3 e l2 for maior que l1, verifica a última condição.
        if l2 + l1 > l3:
            # Se todas as condições forem atendidas, exibe que é um triângulo.
            print('É um triângulo: Sim!')
            # Define a variável 'naoe' como 'e' para indicar que é um triângulo.
            naoe = 'e'
        else:
            # Se a última condição não for atendida, ainda exibe que é um triângulo.
            print('É um triângulo: Sim!')
            # Define a variável 'naoe' como 'e' para indicar que é um triângulo.
            naoe = 'e'
    else:
        # Se a segunda condição não for atendida, ainda exibe que é um triângulo.
        print('É um triângulo: Sim!')
        # Define a variável 'naoe' como 'e' para indicar que é um triângulo.
        naoe = 'e'
else:
    # Se a primeira condição não for atendida, exibe que não é um triângulo.
    print('É um triângulo: Não!')
    # Define a variável 'naoe' como 'naoe' para indicar que não é um triângulo.
    naoe = 'naoe'

########################################

# Verifica o valor da variável 'naoe' para decidir se o programa deve continuar.
if naoe == 'naoe':
    # Se 'naoe' for 'naoe', encerra o programa, pois não é um triângulo.
    quit()
# Se for um triângulo, verifica o tipo de triângulo.
elif l1 == l2 and l1 == l3:
    # Se todos os lados forem iguais, classifica como EQUILÁTERO.
    print('Classificação: Equilátero!')
elif (l1 == l2) or (l2 == l3) or (l1 == l3):
    # Se pelo menos dois lados forem iguais, classifica como ISÓSCELES.
    print('Classificação: Isóceles!')
else:
    # Se todos os lados forem diferentes, classifica como ESCALENO.
    print('Classificação: Escaleno!')

