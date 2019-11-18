import pygame
import sys 
import pelaajaluokka
pygame.init()

koko = (1280, 720)
naytto = pygame.display.set_mode(koko)

pelaaja = pelaajaluokka.Pelaaja()

while True:
    naytto.fill([0,0,0])
    pelaaja.piirra(naytto)

    tapahtumat = pygame.event.get()
    for tapahtuma in tapahtumat:
        # tää sulkee ikkunan jos ruksi on painettu
        if tapahtuma.type == pygame.QUIT:
            sys.exit()
        elif tapahtuma.type == pygame.KEYDOWN:
            if tapahtuma.key == pygame.K_w:
                pass
            if tapahtuma.key == pygame.K_a:
                pelaaja.vasenmalle()
            if tapahtuma.key == pygame.K_s:
                pass
            if tapahtuma.key == pygame.K_d:
                pelaaja.oikealle()

pygame.display.flip