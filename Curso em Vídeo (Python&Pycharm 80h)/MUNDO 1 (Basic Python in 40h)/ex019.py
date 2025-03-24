# UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS
# PARA APAGAR O QUADRO. FAÇA UM PROGRAMA QUE AJUDE ELE,
# LENDO O NOME DELES E ESCREVENDO O NOME DO ESCOLHIDO.
import random # importando o módulo inteiro pois não sabia qual ia usar, no caso a gnt poderia importar apenas com -> from random import choice que também funcionaria
print('BEM VINDO AO SORTEADOR DE ALUNOS!')
al1=input('Digite o nome do primeiro aluno: ')  #Nome do aluno 1
al2=input('Digite o nome do segundo aluno: ')   #Nome do aluno 2
al3=input('Digite o nome do terceiro aluno: ')  #Nome do aluno 3
al4=input('Digite o nome do quarto aluno: ')    #Nome do aluno 4

sorteado = al1, al2, al3, al4       #Sistema para organizar os alunos em uma lista, pois o comando que iremos utilizar (random.choice ou choice) sorteia itens de uma lista, e não itens avulsos

print(f'O Aluno sorteado é o aluno {random.choice(sorteado)}!') #Mostra a lista sendo executada pelo comando. random.choice --- SORTEIA ENTRE ---> {(lista)}
