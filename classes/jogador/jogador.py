import pygame
from constants import SCREEN_WIDTH,SCREEN_HEIGHT
from pygame.locals import *
from menu_compra.get_square import get_square
from menu_compra.get_square_index import get_square_index
import random

class Jogador:
    def __init__(self, vaccines):
        self.vaccines=vaccines
        self.time=0
        self.selecting=False
        self.image_selected=''
        self.board=[[0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0]]

    def update_vaccines(self,variation):
        self.vaccines+=variation
    
    def drawn_vaccines_score(self,screen):
        txt=str(self.vaccines)
        fonte=pygame.font.get_default_font()              
        fontesys=pygame.font.SysFont(fonte, int(70))          
        txttela = fontesys.render(txt, 1, (255,255,255))  
        screen.blit(txttela,(120*SCREEN_WIDTH/1600,45*SCREEN_HEIGHT/900))

    def update_selection(self,selection):
        self.selecting=selection

    def update_time(self):
        self.time+=1
        if random.uniform(0,1)<0.1:
            self.update_vaccines(7)

    def verify_places(self,defensor_group):
        self.board=[[0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0]]
        for defensor in defensor_group:
            index_x,index_y=get_square_index(defensor.position_x,defensor.position_y)
            self.board[index_x][index_y]=1

    def verify_event(self,event,buybuttons,defensor_group, defensor_power_group,atacante_group,screen):
        for button in buybuttons:
            if event.type == MOUSEBUTTONDOWN:
                if button.rect.collidepoint(event.pos):
                    if self.vaccines-button.cost>=0:
                        button.flag = 1
                        self.image_selected=button.image
            if event.type == MOUSEBUTTONUP and button.flag == 1:
                button.flag = 0
                x=pygame.mouse.get_pos()[0]
                y=pygame.mouse.get_pos()[1]
                if get_square(x,y)[0]>0:
                    x_index=get_square_index(x,y)[0]
                    y_index=get_square_index(x,y)[1]
                    if self.board[x_index][y_index]==0:
                        button.create(event.pos, defensor_group,defensor_power_group)
                        self.update_vaccines(-button.cost)
                        self.board[x_index][y_index]=1

            if button.flag == 1:
                x=pygame.mouse.get_pos()[0]
                y=pygame.mouse.get_pos()[1]
                screen.blit(self.image_selected, (x, y))

    
        
    
