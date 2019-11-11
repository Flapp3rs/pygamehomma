import pygame
import sys 
pygame.init()

koko = (1280, 720)
naytto = pygame.display.set_mode(koko)

while True:


     tapahtumat = pygame.event.get()
    for tapahtuma in tapahtumat:
        # tää sulkee ikkunan jos ruksi on painettu
        if tapahtuma.type == pygame.QUIT:
            sys.exit()

pygame.display.flip