import pygame
from pygame.locals import *
from assets.export import nurse_power_images_list

class Nurse_Power(pygame.sprite.Sprite):
    def __init__(self, position_x, position_y, power):
        pygame.sprite.Sprite.__init__(self)
        list_image = nurse_power_images_list
        self.image = list_image[0].convert_alpha()
        self.rect = self.image.get_rect()

        self.position_x = position_x
        self.position_y = position_y
        self.power = power
        self.velocity_x = 5
        self.velocity_y = 0
        self.rect.center = (self.position_x, self.position_y)
        # self.rect[0] = self.position_x
        # self.rect[1] = self.position_y

    def update(self):
        self.position_x += self.velocity_x

        self.rect.center = (self.position_x, self.position_y)
        # self.rect[0] = self.position_x
        # self.rect[1] = self.position_y