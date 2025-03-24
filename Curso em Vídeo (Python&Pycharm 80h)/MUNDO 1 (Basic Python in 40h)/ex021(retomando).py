import pygame
pygame.init()
pygame.mixer.music.load('gigaloudo.mp3')

pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.event.wait()

