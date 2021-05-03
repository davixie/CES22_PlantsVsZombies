import pygame
from pygame.locals import *


class Buttons():
    def _init_(self, positionx, positiony, size):
        #posicao x,y do topo esquerdo do botao: a depender da arte do jogo

        self.surface = pygame.Surface(size)
        self.rect = pygame.Rect(positionx, positiony, size[0], size[1])

        self.flag = 0

class Button_medico(Buttons):

    def _init_(self, positionx, positiony,size):

        super()._init_(positionx, positiony,size)
        self.name = "medico"

    def create(self,pos):
        1



class Button_enfermeira(Buttons):

    def _init_(self, positionx, positiony,size):

        super()._init_(positionx, positiony)
        self.name = "enfermeira"

    def create(self, pos):
        1
