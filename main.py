import pygame
from pygame.locals import *
from constants import BACKGROUND, screen
from functions.export import update_group, load_defenders, load_attackers,load_player
from intro import intro

from pygame import font

from menu_compra.buttons import Button_medico


pygame.init()

atacante_group = pygame.sprite.Group()
load_attackers(atacante_group)


defensor_group = pygame.sprite.Group()
player=load_player()

defensor_group = pygame.sprite.Group()


size = (140,72)
defensor_power_group = pygame.sprite.Group()
button_medico = Button_medico(0, 224, size)
buybuttons = [button_medico]


clock = pygame.time.Clock()

intro(clock,screen)

while True:
    clock.tick(10)
    print(pygame.mouse.get_pos())
    screen.blit(BACKGROUND, (0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        else:
            player.verify_event(event,buybuttons,defensor_group, defensor_power_group,atacante_group,screen)

    update_group(atacante_group, screen)
    update_group(defensor_group, screen)
    update_group(defensor_power_group, screen)

    player.drawn_vaccines_score(screen)

        
    pygame.display.update()
