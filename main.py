import pygame
from pygame.locals import *
from constants import BACKGROUND, screen
from functions.export import update_group, load_defenders, load_attackers
from intro import intro
from menu_compra.buttons import Button_medico

pygame.init()

atacante_group = pygame.sprite.Group()
load_attackers(atacante_group)

defensor_group = pygame.sprite.Group()

size = (70,36)
button_medico = Button_medico(0, 112, size)
buybuttons = [button_medico]

clock = pygame.time.Clock()

intro(clock,screen)

while True:
    clock.tick(10)
    print(pygame.mouse.get_pos())

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        #check_buy(event)
        for button in buybuttons:
            if event.type == MOUSEBUTTONDOWN:
                if button.rect.collidepoint(event.pos):
                    button.flag = 1
            if event.type == MOUSEBUTTONUP and button.flag == 1:
                button.flag = 0
                button.create(event.pos, defensor_group)
    
    screen.blit(BACKGROUND, (0, 0))

    update_group(atacante_group, screen)
    update_group(defensor_group, screen)
        
    pygame.display.update()
