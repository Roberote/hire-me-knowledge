'''for c in range(1,5):
    n = int(input('Digite um valor: '))
print('Fim')'''

par = 0
impar = 0
n = 1

while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar +=1

print('Acabou')
print(f'{par} números foram pares e {impar} números foram ímpares!')