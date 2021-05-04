import pygame
from pygame.locals import *
from constants import BACKGROUND, screen
from functions.export import update_group, load_defenders, load_attackers, check_attacker_colisions, check_defensor_power_colision, load_player
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

groups = []
groups.append(atacante_group)
groups.append(defensor_group)
groups.append(defensor_power_group)

while True:
    clock.tick(10)
    screen.blit(BACKGROUND, (0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        else:
            player.verify_event(event,buybuttons,defensor_group, defensor_power_group,atacante_group,screen)

    check_attacker_colisions(atacante_group, defensor_group, groups)
    check_defensor_power_colision(defensor_power_group, atacante_group, groups)

    screen.blit(BACKGROUND, (0, 0))

    for group in groups:
        update_group(group, screen)
          
    player.drawn_vaccines_score(screen)
    player.update_time()

        
    pygame.display.update()
