
import pygame
import sys 
pygame.init()

koko = (600, 600)
naytto = pygame.display.set_mode(koko)

musta = (0, 0, 0)
punanen = (255, 0, 0)
while True:


     tapahtumat = pygame.event.get()
    for tapahtuma in tapahtumat:
        # tää sulkee ikkunan jos ruksi on painettu
        if tapahtuma.type == pygame.QUIT:
            sys.exit()

pygame.display.flip