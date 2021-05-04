import pygame
from pygame.locals import *
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class FinalDefensor(pygame.sprite.Sprite):
    def __init__(self, position_x, position_y, power, image): # life between 0 and 1
        pygame.sprite.Sprite.__init__(self)
        self.position_x = position_x
        self.position_y = position_y
        self.power = power
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = position_x
        self.rect[1] = position_y

    def update(self):
        return 