import pygame
from pygame.locals import *
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Defensor(pygame.sprite.Sprite):
    def __init__(self, position_x, position_y, resistence, power, list_image, defensor_power_group): # life between 0 and 1
        pygame.sprite.Sprite.__init__(self)
        self.position_x = position_x
        self.position_y = position_y
        self.resistence = resistence
        self.power = power
        self.defensor_power_group = defensor_power_group
        self.life = 20
        self.clock = 0
        self.attack_frequency=20
        self.contador_image = 0
        self.list_image = []
        self.image = list_image[0].convert_alpha()
        for img in list_image:
            new_img = img.convert_alpha()
            # new_img = pygame.transform.scale(new_img, (120, 160))
            self.list_image.append(new_img)
        # self.image = pygame.transform.scale(self.image, (120, 160))
        self.rect = self.image.get_rect()
    
    def update(self):
        self.contador_image = (self.contador_image + 1) % (len(self.list_image))
        self.image = self.list_image[ self.contador_image ]

        self.clock = self.clock + 1
        self.rect.center = (self.position_x, self.position_y)

        if(self.clock%self.attack_frequency == 0):
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
        return self.list_image[0]
        
