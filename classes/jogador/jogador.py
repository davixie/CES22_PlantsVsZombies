import pygame
from constants import SCREEN_WIDTH,SCREEN_HEIGHT

class Jogador:
    def __init__(self, vaccines):
        self.vaccines=vaccines
        self.time=0
        self.selecting=False
        self.image_selected=''

    def update_vaccines(variation):
        self.vaccines+=variation
    
    def drawn_vaccines_score(self,screen):
        txt=str(self.vaccines)
        fonte=pygame.font.get_default_font()              
        fontesys=pygame.font.SysFont(fonte, int(70))          
        txttela = fontesys.render(txt, 1, (255,255,255))  
        screen.blit(txttela,(120*SCREEN_WIDTH/1600,45*SCREEN_HEIGHT/900))

    def update_selection(self,selection):
        self.selecting=selection    
        
    
