# FAÇA UM PROGRAMA EM PYTHON QUE REPRODUZA UM ARQUIVO MP3.
# Vamos usar o pygame e a sua função de tocar sons. Já que o pygame é feito para jogos, existem diversas funcionalidades como essa. Para imagens, para sons, para videos, etc.
from pygame import mixer, event, init, quit

# Inicializa o pygame e o mixer
init()
mixer.init()

# Carrega o arquivo MP3
mixer.music.load('gigaloudo.mp3')  # Certifique-se de que o arquivo está no local correto

# Reproduz o arquivo MP3
mixer.music.play()

# Permite que o comando pygame.event.wait funcione
input()
# Aguarda o término da reprodução
event.wait()
print("Olá, obrigado por ouvir esse som!") #não ta rodando pq não passa do input, por algum motivo, vou aprender mais pra frente


