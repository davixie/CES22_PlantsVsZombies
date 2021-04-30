# import pygame
# from pygame.locals import *

# class Defensor(pygame.sprite.Sprite):
#     def __init__(self, positionx, positiony, velx, vely, power, list_image): # life between 0 and 1
#         # image is the path to the image
        
#         pygame.sprite.Sprite.__init__(self)
        
#         self.positionx = positionx
#         self.positiony = positiony
#         self.velx = velx
#         self.vely = vely
#         self.power = power
#         self.life = 1

#         self.contador_image = 0

#         self.clock = 0

#         self.listImage = []
#         self.image = pygame.image.load(list_image[0]).convert_alpha()
#         self.rect = self.image.get_rect()
#         for img in list_image:
#             self.listImage.append(pygame.image.load(img).convert_alpha())
    
#     def update(self):
#         self.contador_image = (self.contador_image + 1) % (len(self.listImage))
#         self.image = self.listImage[ self.contador_image ]

#         self.clock = self.clock + 1

#         self.positionx += self.velx
#         self.positiony += self.vely

#         self.rect[0] = self.positionx
#         self.rect[1] = self.positiony
    
#     def looseLife(damage):
#         self.life = self.life - damage * (1 - self.power)
#         self.velx = self.velx - damage * (1 - self.power) # 0 < slower < 1