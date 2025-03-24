#O EX020 É UMA EXTENSÃO DO EX019
import random # importando o módulo inteiro pois não sabia qual ia usar, no caso a gnt poderia importar apenas com -> from random import choice que também funcionaria
texto = 'BEM VINDO AO SORTEADOR DE ALUNOS!'
print(f'{texto:=^103}')
print('Use o sorteador para sortear um aluno específico e depois sorteie uma ordem de apresentação dos alunos!')
al1=input('Digite o nome do primeiro aluno: ')  #Nome do aluno 1
al2=input('Digite o nome do segundo aluno: ')   #Nome do aluno 2
al3=input('Digite o nome do terceiro aluno: ')  #Nome do aluno 3
al4=input('Digite o nome do quarto aluno: ')    #Nome do aluno 4

sorteado = al1, al2, al3, al4  #Sistema para organizar os alunos em uma TUPLA, pois o comando que iremos utilizar (random.choice ou choice) sorteia itens de uma lista, e não itens avulsos

print(f'O Aluno sorteado é o aluno {random.choice(sorteado)}!')        #Mostra a lista sendo executada pelo comando. random.choice --- SORTEIA ENTRE ---> {(lista)}

#================================================================================================================================================

# Daqui pra baixo é o comando pra sortear a ordem de apresentação

#================================================================================================================================================
# Com o comando random.sample ficaria:
apresentacao = random.sample(sorteado, k=len(sorteado)) #random.sample retorna uma nova lista embaralhada, enquanto random.shuffle modifica a lista original.
#↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#apresentacao = embaralhamento da (lista sorteado, pela quantidade "k"), ali ao invés da quantidade k ser um numero, ele é a quantidade do tamanho da lista sorteado, ou seja, length da(sorteado).

#================================================================================================================================================


#================================================================================================================================================

# Agora com o random.shuffle ficaria:
sorteadolist = [al1, al2, al3, al4]
#a diferença desse pro primeiro lá em cima é que ali é uma TUPLA. Tuplas não podem ser alteradas, uma lista pode.
# o sample ele sorteia itens, então a tupla serve pq só vai mostrar os itens pra ele, já o não pode embaralhar uma tupla, somente uma lista

# METODO ERRADO DE USO apresentacaoshuffle = (random.shuffle(sorteadolist))

#A função random.shuffle não retorna uma nova lista. Em vez disso, ela modifica a lista original diretamente.
#Por isso, quando você tenta imprimir o resultado de random.shuffle(sorteadolist), ele retorna None, porque a função não tem um valor de retorno.
#forma correta de usar:
random.shuffle(sorteadolist)
#================================================================================================================================================

print(f'A Ordem de apresentação será a seguinte: {apresentacao}')           #Mostra a lista e sorteia os 4 nomes da lista em ordem de apresentação usando o comando random.sample(tupla, k=quantidade de itens da tupla).

print(f'A Ordem de apresentação será a seguinte: {sorteadolist}')           #Mostra a lista e sorteia os 4 nomes da lista em ordem de apresentação usando o comando random.shuffle(lista).
