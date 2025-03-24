print('Olá! Calcule aqui a sua média entre 5 notas!') #FLOAT POIS A MÉDIA E AS NOTAS PODEM SER ESCRITAS EM DECIMAL!
n1 = float(input('Digite a sua primeira nota: ')) #FLOAT POIS A MÉDIA E AS NOTAS PODEM SER ESCRITAS EM DECIMAL!
n2 = float(input('Digite a sua segunda nota: ')) #FLOAT POIS A MÉDIA E AS NOTAS PODEM SER ESCRITAS EM DECIMAL!
n3 = float(input('Digite a sua terceira nota: ')) #FLOAT POIS A MÉDIA E AS NOTAS PODEM SER ESCRITAS EM DECIMAL!
n4 = float(input('Digite a sua quarta nota: ')) #FLOAT POIS A MÉDIA E AS NOTAS PODEM SER ESCRITAS EM DECIMAL!
n5 = float(input('Digite a sua quinta nota: ')) #FLOAT POIS A MÉDIA E AS NOTAS PODEM SER ESCRITAS EM DECIMAL!

n_de_materias = 5

total = float(n1+n2+n3+n4+n5) #FLOAT POIS A MÉDIA E AS NOTAS PODEM SER ESCRITAS EM DECIMAL!
media = float(total/n_de_materias) #FLOAT POIS A MÉDIA E AS NOTAS PODEM SER ESCRITAS EM DECIMAL!

# A MUDANÇA DE CÓDIGO AQUI É PARA SEPARAR AS CONTAS, MAS UMA FORMA DE DIMINUIR O CÓDIGO É TROCAR O TOTAL/N_DE_MATERIAS POR UMA LINHA SÓ: media = float((n1+n2+n3+n4+n5)/5) -- Já que sabemos o total de materias (5) e podemos fazer a soma e a divisão em uma linha só.


print(f'A sua média entre as notas é {media}!', end=' >>>> ')
print('Segue o boletim: ')
print(f'Matéria A:{n1}')
print(f'Matéria B:{n2}')
print(f'Matéria C:{n3}')
print(f'Matéria D:{n4}')
print(f'Matéria E:{n5}')
print(f'Média geral: {media}')
