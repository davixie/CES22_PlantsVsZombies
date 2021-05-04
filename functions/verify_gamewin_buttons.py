import pygame
from pygame.locals import *
from menu_compra.buttons import Play_again,Exit_button

def verify_gamewin_buttons(event):

    play_again = Play_again(800, 700, 300, 100)
    exit_button = Exit_button(1400, 800, 200, 200)
    if event.type == MOUSEBUTTONDOWN:
        if play_again.rect.collidepoint(event.pos):
            play_again.action()
        if exit_button.rect.collidepoint(event.pos):
            pygame.quit()
