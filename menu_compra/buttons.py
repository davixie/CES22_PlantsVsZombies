import pygame
from pygame.locals import *
from menu_compra.get_square import get_square
from constants import SCREEN_WIDTH,SCREEN_HEIGHT
from functions.load_defenders import load_defenders
from classes.defensor.medico import Medico
import os


class Buttons():
    def __init__(self, positionx, positiony, size):
        #posicao x,y do topo esquerdo do botao: a depender da arte do jogo

        self.surface = pygame.Surface(size)
        self.rect = pygame.Rect(positionx, positiony, size[0], size[1])

        self.flag = 0

class Button_medico(Buttons):

    def __init__(self, positionx, positiony,size):

        super().__init__(positionx, positiony,size)
        self.cost=25
        self.image=pygame.image.load(os.path.join('assets','artes finais','defensor 1','doctor.png')).convert_alpha()

    def create(self,pos, defensor_group, defensor_power_group):
        posx,posy = get_square(pos[0],pos[1])
        if posx > 0:
            medico = Medico(posx, posy, defensor_power_group )
            load_defenders(medico, defensor_group)



class Button_enfermeira(Buttons):

    def __init__(self, positionx, positiony,size):

        super().__init__(positionx, positiony)
        self.name = "enfermeira"

    def create(self, pos):
        1
