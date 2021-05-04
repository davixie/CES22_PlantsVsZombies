import pygame
from pygame.locals import *
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Defensor(pygame.sprite.Sprite):
    def __init__(self, positionx, positiony, power, image): # life between 0 and 1
        pygame.sprite.Sprite.__init__(self)
        self.positionx = positionx
        self.positiony = positiony
        self.power = power
        self.life = 100
        self.clock = 0
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (120, 160))
        self.rect = self.image.get_rect()
    
    def update(self):
        self.clock = self.clock + 1
        self.rect[0] = self.positionx
        self.rect[1] = self.positiony
    
    def looseLife(self, damage, groups):
        self.life = self.life - damage * (1 - self.power)

        if(self.life < 0):
            self.die(groups)

    def die(self, groups):
        for group in groups:
            if self in group:
                group.remove(self)

    def getMyImage(self):
        return self.image
        
