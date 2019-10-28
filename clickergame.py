import pygame
import sys 
import random
pygame.init()

koko = (600, 600)
naytto = pygame.display.set_mode(koko)

sijainti = [0, 0]

musta = (0, 0, 0)
punanen = (255, 0, 0)

pisteet = 0

kolikko = pygame.image.load("kolikko.png")
kolikko = pygame.transform.scale(kolikko, (60, 60))

while True:
    naytto.fill(musta)
   
    naytto.blit(kolikko, sijainti)

    tapahtumat = pygame.event.get()
    for tapahtuma in tapahtumat:
        # tää sulkee ikkunan jos ruksi on painettu
        if tapahtuma.type == pygame.QUIT:
            sys.exit()

        elif tapahtuma.type == pygame.MOUSEBUTTONDOWN:
            paikka = tapahtuma.pos

            if paikka[0] >= sijainti[0] and paikka[0] <= sijainti[0] + 60 and paikka[1] >= sijainti[1] and paikka[1] <= sijainti[1] + 60:
                sijainti[0] = random.randint(0, koko[0])
                sijainti[1] = random.randint(0, koko[1])
                pisteet += 1
                print (pisteet)

    pygame.display.flip()