import pygame
import sys 
import random
import time
pygame.init()
pygame.font.init()

koko = (1000, 800)
naytto = pygame.display.set_mode(koko)

sijainti = [0, 0]

alkuaika = time.time()

musta = (0, 0, 0)
punanen = (255, 0, 0)

Arial = pygame.font.SysFont("Arial", 30)

pisteet = 0

kolikko = pygame.image.load("kolikko.png")
kolikko = pygame.transform.scale(kolikko, (60, 60))

while True:
    naytto.fill(musta)
    
    nyt = time.time()
    peliaika = int(nyt - alkuaika)
    
    naytto.blit(kolikko, sijainti)
    tekstikuva = Arial.render("Pisteet: " + str(pisteet), True, punanen)
    naytto.blit(tekstikuva, (10, 10))
    kello = Arial.render("Aika: " + str(peliaika), True, punanen)
    naytto.blit(kello, (10, 50))

    tapahtumat = pygame.event.get()
    for tapahtuma in tapahtumat:
        # tää sulkee ikkunan jos ruksi on painettu

        if tapahtuma.type == pygame.QUIT:
            sys.exit()

        elif tapahtuma.type == pygame.MOUSEBUTTONDOWN:
            if peliaika > 10:
                continue 
            paikka = tapahtuma.pos

            #tää laittaa kuvan jonnekkin

            if paikka[0] >= sijainti[0] and paikka[0] <= sijainti[0] + 60 and paikka[1] >= sijainti[1] and paikka[1] <= sijainti[1] + 60:
                sijainti[0] = random.randint(0, koko[0] - 60)
                sijainti[1] = random.randint(0, koko[1] - 60)
                pisteet += 1

            
            
    if peliaika > 10:
        naytto.fill(musta)
        loppu = Arial.render("Peli loppu", True, punanen)
        cps = Arial.render("Cps: " + str(pisteet/10), True, punanen)
        naytto.blit(cps, (500, 450))
        naytto.blit(loppu, (500, 400))

    pygame.display.flip()