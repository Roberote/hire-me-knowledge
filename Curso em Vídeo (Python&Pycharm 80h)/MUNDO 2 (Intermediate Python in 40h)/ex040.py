# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO

nota1 = float(input('Digite a sua nota do 1° Bimestre: '))
nota2 = float(input('Digite a sua nota do 2° Bimestre: '))

nota = float((nota1 + nota2)/2)

if nota <= 4.9:
    print(f'O Aluno está {'\033[0;31m'}REPROVADO{'\033[m'}!')
elif (nota >= 5.0) and (nota < 7.0):
        print(f'O Aluno está de {'\033[0;33m'}RECUPERAÇÃO{'\033[m'}!')
else:
    print(f'O Aluno está {'\033[0;32m'}APROVADO!')
