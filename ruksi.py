import pygame
import sys 
pygame.init()

koko = (600, 600)
naytto = pygame.display.set_mode(koko)

# tää kohta piirtää ruksin
musta = (0, 0, 0)
punanen = (255, 0, 0)
while True:
    naytto.fill(musta)
    pygame.draw.line(naytto, punanen, (300, 300), (100, 100), 10)
    pygame.draw.line(naytto, punanen, (300, 300), (500, 100), 10)
    pygame.draw.line(naytto, punanen, (300, 300), (100, 500), 10)
    pygame.draw.line(naytto, punanen, (300, 300), (500, 500), 10)
    pygame.display.flip()
    
    tapahtumat = pygame.event.get()
    for tapahtuma in tapahtumat:
        # tää sulkee ikkunan jos ruksi on painettu
        if tapahtuma.type == pygame.QUIT:
            sys.exit()