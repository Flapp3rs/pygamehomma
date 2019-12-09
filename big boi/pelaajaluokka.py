import pygame

class Pelaaja():
    def __init__(self):
        self.x = 640
        self.y = 460
        self.nopeus = 2.5
        self.koko = 64
        self.laskin = 0
        self.saako_nousta = True
        self.animaatio_osa = 0
        self.spritesheet_nimi = "pelaaja123.png"
        self.spritesheet = None
        self.kuva = None

        self.lataa_sprite_sheet()
        self.lataa_kuva(0, 0)
    
    def lataa_sprite_sheet(self):
        self.spritesheet = pygame.image.load(self.spritesheet_nimi)

    def lataa_kuva(self, rivi, sarake):
        self.kuva = pygame.image.load("tyhjyys.png")
        aloitusy = rivi * self.koko
        aloitusx = sarake * self.koko
        lopetusy = aloitusy + self.koko
        lopetusx = aloitusx + self.koko
        # Kopio spritesheetistä määrätyn alueen
        self.kuva.blit(self.spritesheet, (0,0), (aloitusx, aloitusy, lopetusx, lopetusy))

    def animoi(self, animaatio_numero):
        self.laskin += 1
        if self.laskin < 12:
            return


        self.laskin = 0
        self.animaatio_osa += 1
        if self.animaatio_osa == 4:
            self.animaatio_osa = 0

        self.lataa_kuva(animaatio_numero, self.animaatio_osa)

    def piirra(self, minne):
        minne.blit(self.kuva, [self.x, self.y])
    
    def oikealle(self):
        self.x += self.nopeus

    def vasenmalle(self):
        self.x -= self.nopeus

    def hyppy(self):
        self.y -= self.nopeus

    def putoa(self):
        self.y += self.nopeus