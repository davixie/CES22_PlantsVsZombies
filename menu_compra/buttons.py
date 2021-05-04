import pygame
from pygame.locals import *
from menu_compra.get_square import get_square
from constants import SCREEN_WIDTH,SCREEN_HEIGHT
from functions.load_defenders import load_defenders
from classes.defensor.medico import Medico
from classes.defensor.enfermeiro import Enfermeiro
from classes.defensor.mascara import Mascara
from classes.defensor.alcool_e_gel import Alcool_E_Gel
from classes.defensor.cientista import Cientista

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
        self.cost=175
        self.image=pygame.image.load(os.path.join('assets','artes finais','defensor 1','doctor.png')).convert_alpha()

    def create(self,pos, defensor_group, defensor_power_group):
        posx,posy = get_square(pos[0],pos[1])
        if posx > 0:
            medico = Medico(posx, posy, defensor_power_group)
            load_defenders(medico, defensor_group)

class Button_enfermeiro(Buttons):

    def __init__(self, positionx, positiony,size):

        super().__init__(positionx, positiony,size)
        self.cost=25
        self.image=pygame.image.load(os.path.join('assets','artes finais','defensor 2','nurse.png')).convert_alpha()

    def create(self,pos, defensor_group, defensor_power_group):
        posx,posy = get_square(pos[0],pos[1])
        if posx > 0:
            enf = Enfermeiro(posx, posy, defensor_power_group)
            load_defenders(enf, defensor_group)


class Button_mascara(Buttons):

    def __init__(self, positionx, positiony,size):

        super().__init__(positionx, positiony,size)
        self.cost=50
        self.image=pygame.image.load(os.path.join('assets','artes finais','defensor 4','mask.png')).convert_alpha()

    def create(self,pos, defensor_group, defensor_power_group):
        posx,posy = get_square(pos[0],pos[1])
        if posx > 0:
            defensor = Mascara(posx, posy, defensor_power_group)
            load_defenders(defensor, defensor_group)


class Button_alcool(Buttons):

    def __init__(self, positionx, positiony,size):

        super().__init__(positionx, positiony,size)
        self.cost=100
        self.image=pygame.image.load(os.path.join('assets','artes finais','defensor 3','alcohol.png')).convert_alpha()

    def create(self,pos, defensor_group, defensor_power_group):
        posx,posy = get_square(pos[0],pos[1])
        if posx > 0:
            defensor = Alcool_E_Gel(posx, posy, defensor_power_group)
            load_defenders(defensor, defensor_group)


class Button_cientista(Buttons):

    def __init__(self, positionx, positiony,size):

        super().__init__(positionx, positiony,size)
        self.cost=100
        self.image=pygame.image.load(os.path.join('assets','artes finais','defensor 5','scientist.png')).convert_alpha()

    def create(self,pos, defensor_group, defensor_power_group):
        posx,posy = get_square(pos[0],pos[1])
        if posx > 0:
            defensor = Cientista(posx, posy, defensor_power_group)
            load_defenders(defensor, defensor_group)


class Play_again():
    def __init__(self, posx, posy, sizex, sizey):
        #posicao x,y do topo esquerdo do botao: a depender da arte do jogo

        self.surface = pygame.Surface(size)
        self.rect = pygame.Rect(posx, posy, sizex, sizey)

    def action(self):
        #implementar

class Exit_button():
    def __init__(self, posx, posy, sizex, sizey):
        #posicao x,y do topo esquerdo do botao: a depender da arte do jogo

        self.surface = pygame.Surface(size)
        self.rect = pygame.Rect(posx, posy, sizex, sizey)