# FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.

frase = input('Digite uma frase: ')

frase_formtd = frase.upper()

print(f'Na frase {frase}, a letra "A" aparece {frase_formtd.count('A')} vezes.' )

print(f'Na frase {frase}, o primeiro "A" aparece na {frase_formtd.find('A') + 1}ª posição.')

print(f'Na frase {frase}, o ultimo "A" aparece na {frase_formtd.rfind('A') + 1}ª posição.')
