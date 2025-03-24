frase = input('Digite a frase: ').strip().lower()

countA = frase.count('a')
firstA = frase.find('a')
lastA = frase.rfind('a')

print(f'A Frase possui {countA} "A"s, sendo o primeiro na {firstA + 1}ª posição e o ultimo na {lastA + 1}ª posição.')
