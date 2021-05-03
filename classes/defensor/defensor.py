import pygame
from pygame.locals import *

class Defensor(pygame.sprite.Sprite):
    def __init__(self, positionx, positiony, power, image): # life between 0 and 1
        pygame.sprite.Sprite.__init__(self)
        self.positionx = positionx
        self.positiony = positiony
        self.power = power
        self.life = 1
        self.clock = 0
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
    
    def update(self):
        self.clock = self.clock + 1
        self.rect[0] = self.positionx
        self.rect[1] = self.positiony
    
    def looseLife(damage):
        self.life = self.life - damage * (1 - self.power)
        