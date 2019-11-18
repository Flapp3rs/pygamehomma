import pygame

class Pelaaja():
    def __init__(self):
        self.x = 100
        self.y = 100
        self.nopeus = 10
        self.koko = 64
        self.spritesheet_nimi = "pelaaja123.png"
        self.spritesheet = None
        self.kuva = None

        self.lataa_sprite_sheet()
        self.lataa_kuva()
    
    def lataa_sprite_sheet(self):
        self.spritesheet = pygame.image.load(self.spritesheet_nimi)

    def lataa_kuva(self):
        self.kuva = pygame.image.load("tyhjyys.png")
        # Kopio spritesheetistä määrätyn alueen
        self.kuva.blit(self.spritesheet, (0,0), (0, 0, self.koko, self.koko))

    def piirra(self, minne):
        minne.blit(self.kuva, [self.x, self.y])
    
    def oikealle(self):
        self.x =+ self.nopeus

    def vasenmalle(self):
        self.x =- self.nopeus