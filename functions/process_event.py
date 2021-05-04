import pygame
from pygame.locals import *

def check_buy(event, buybuttons):
    for button in buybuttons:
        if event.type == MOUSEBUTTONDOWN:
            if button.rect.collidepoint(event.pos):
                button.flag = 1
        if event.type == MOUSEBUTTONUP and button.flag == 1:
            button.flag = 0
            button.create(event.pos)