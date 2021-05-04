import pygame
from pygame.locals import *

class Atacante(pygame.sprite.Sprite):
    def __init__(self, positionx, positiony, velx, vely, resistence, power, list_image): # life between 0 and 1
        # image is the path to the image
        
        pygame.sprite.Sprite.__init__(self)
        
        self.positionx = positionx
        self.positiony = positiony
        self.velx = velx
        self.vely = vely
        self.stop = False
        self.resistence = resistence
        self.power = power
        self.life = 3

        self.contador_image = 0

        self.clock = 0

        self.listImage = []
        self.image = pygame.image.load(list_image[0]).convert_alpha()
        self.rect = self.image.get_rect()
        for img in list_image:
            new_img = pygame.image.load(img).convert_alpha()
            new_img = pygame.transform.scale(new_img, (120, 160))
            self.listImage.append(new_img)
    
    def update(self):
        self.contador_image = (self.contador_image + 1) % (len(self.listImage))
        self.image = self.listImage[ self.contador_image ]

        self.clock = self.clock + 1

        if not self.stop:
            self.positionx -= self.velx
            self.positiony -= self.vely

            self.rect[0] = self.positionx
            self.rect[1] = self.positiony
        self.stop = False
    
    def looseLife(self, damage, groups):
        self.life = self.life - damage * (1 - self.resistence)
        if(self.life < 0):
            self.die(groups)

    def die(self, groups):
        for group in groups:
            if self in group:
                group.remove(self)

    def attacker_stop(self):
        self.stop = True
       