import pygame
from pygame.locals import *

class Buttons(pygame.sprite.Sprite):
    def __init__(self, positionx, positiony, sizex, sizey):
        #posicao x,y do topo esquerdo do botao: a depender da arte do jogo

        pygame.sprite.Sprite.__init__(self)

        self.positionx = positionx
        self.positiony = positiony
        self.velx = sizex
        self.vely = sizey


        self.rect = pygame.Rect(positionx, positiony, sizex,sizey)

buybuttons = pygame.sprite.Group()

buy_medico = Buttons(10,40,50,40)
buy_bomba = Buttons(60,40,50,40)

buybuttons.add(buy_bomba)
buybuttons.add(buy_medico)

