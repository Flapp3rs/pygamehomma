import pygame
import sys 
pygame.init()

koko = (600, 600)
naytto = pygame.display.set_mode(koko)

musta = (0, 0, 0)

hj = pygame.image.load("hahmo1.png")
# hj = haamu juttu
sijainti = [0,0]
while True:
    naytto.fill(musta)
    naytto.blit(hj, sijainti)
    
    pygame.display.flip()

    tapahtumat = pygame.event.get()
    for tapahtuma in tapahtumat:
        # tää sulkee ikkunan jos ruksia on painettu
        if tapahtuma.type == pygame.QUIT:
            sys.exit()
        elif tapahtuma.type == pygame.KEYDOWN:
            
            if tapahtuma.key == pygame.K_w:
                sijainti[1] = sijainti[1] - 10
            if tapahtuma.key == pygame.K_a:
                 sijainti[0] = sijainti[0] - 10
            if tapahtuma.key == pygame.K_s:
                 sijainti[1] = sijainti[1] + 10
            if tapahtuma.key == pygame.K_d:
                 sijainti[0] = sijainti[0] + 10
            
            if sijainti[0] < 0:
                sijainti[0] = 0
            if sijainti[1] < 0:
                sijainti[1] = 0
            if sijainti[0] > koko[0]:
                sijainti[0] = koko[0]
            if sijainti[1] > koko[1]:
                sijainti[1] = koko[1]            