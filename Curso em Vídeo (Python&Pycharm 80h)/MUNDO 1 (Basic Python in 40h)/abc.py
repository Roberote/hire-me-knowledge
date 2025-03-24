import pygame

# Inicializa o pygame e o mixer
pygame.init()
pygame.mixer.init()

# Verifica se o mixer foi inicializado corretamente
if not pygame.mixer.get_init():
    print("Erro: O mixer do pygame não foi inicializado corretamente.")
    exit()

# Carrega o arquivo MP3
try:
    pygame.mixer.music.load('gigaloudo.mp3')  # Certifique-se de que o arquivo está no local correto
except pygame.error as e:
    print(f"Erro ao carregar o arquivo MP3: {e}")
    exit()

# Reproduz o arquivo MP3
pygame.mixer.music.play()

# Aguarda o término da reprodução
while pygame.mixer.music.get_busy():  # Verifica se o áudio ainda está tocando
    pygame.event.wait()  # Mantém o loop de eventos ativo

# Mensagem final
print("Obrigado por ouvir!")

# Finaliza o pygame
pygame.quit()