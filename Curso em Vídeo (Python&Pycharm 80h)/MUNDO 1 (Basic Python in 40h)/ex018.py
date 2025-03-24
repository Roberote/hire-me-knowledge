# FAÇA UM PROGRAMA QUE LEIA UM ÂNGULO QUALQUER E MOSTRE NA TELA
# O VALOR DO SENO, COSSENO E TANGENTE DESSE ÂNGULO.
from math import cos, sin, tan #Importando funcionalidades de coseno (cos), seno (sin) e tangente (tan)
ang = float(input('Digite o valor de um ângulo: '))
sen = float(sin(ang))
cos = float(cos(ang))
tang = float(tan(ang))

print(f'O ângulo {ang} possui: \n-> seno de {sen}° \n-> um coseno de {cos}° \n-> uma tangente de {tang}°')


