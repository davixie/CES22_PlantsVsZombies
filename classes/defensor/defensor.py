import pygame
from pygame.locals import *
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Defensor(pygame.sprite.Sprite):
    def __init__(self, position_x, position_y, resistence, power, image, defensor_power_group): # life between 0 and 1
        pygame.sprite.Sprite.__init__(self)
        self.position_x = position_x
        self.position_y = position_y
        self.resistence = resistence
        self.power = power
        self.defensor_power_group = defensor_power_group
        self.life = 20
        self.clock = 0
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (120, 160))
        self.rect = self.image.get_rect()
    
    def update(self):
        self.clock = self.clock + 1
        self.rect.center = (self.position_x, self.position_y)

        if(self.clock%20 == 0):
            self.atack(self.defensor_power_group)
    
    def looseLife(self, damage, groups):
        print(self.life)
        self.life = self.life - damage * (1 - self.resistence)
        if(self.life < 0):
            self.die(groups)

    def die(self, groups):
        for group in groups:
            if self in group:
                group.remove(self)

    def getMyImage(self):
        return self.image
        
