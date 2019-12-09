#älä poista tätä(
import pygame
import sys 
import pelaajaluokka
pygame.init()
#)
koko = (1280, 720)
naytto = pygame.display.set_mode(koko)

tausta = pygame.image.load("tausta.png")
pelaaja = pelaajaluokka.Pelaaja()

while True:

    tapahtumat = pygame.event.get()
    for tapahtuma in tapahtumat:
        # tää sulkee ikkunan jos ruksi on painettu
        if tapahtuma.type == pygame.QUIT:
            sys.exit()

    pygame.image.load("tausta.png")

    nappaimisto = pygame.key.get_pressed()
    # jos on ilmassa animaatio rivi 4 pyörii ja pelaa ja tippuu paitsi jos w on painettu
    if pelaaja.y < 460:
        pelaaja.animoi(3)
        if nappaimisto[pygame.K_w] == True and pelaaja.y > 400 and pelaaja.saako_nousta == True:
            pelaaja.hyppy()
        else:
            pelaaja.saako_nousta = False
            pelaaja.putoa()
    #mitä napit tekee
    else:
        pelaaja.saako_nousta = True
        if nappaimisto[pygame.K_d] == True:
            if pelaaja.x > 1280 - pelaaja.koko/2:
                pelaaja.x = -pelaaja.koko/2
            pelaaja.oikealle()
            pelaaja.animoi(2)
        elif nappaimisto[pygame.K_a] == True:
            if pelaaja.x < -pelaaja.koko/2:
                pelaaja.x = 1280 - pelaaja.koko/2
            pelaaja.vasenmalle()
            pelaaja.animoi(1)
        elif nappaimisto[pygame.K_w]:
            pelaaja.hyppy()
            pelaaja.animoi(3)
      
        else:        
            pelaaja.animoi(0)
        
    #älä poista tätä
    naytto.fill([0,0,0])
    naytto.blit(tausta, [0,0])
    pelaaja.piirra(naytto)
    pygame.display.flip()