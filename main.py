import pygame
from pygame.locals import *
from constants import BACKGROUND, screen
from functions.export import update_group, load_defenders, load_attackers, check_attacker_colisions
from intro import intro

pygame.init()

atacante_group = pygame.sprite.Group()
load_attackers(atacante_group)

defensor_group = pygame.sprite.Group()
load_defenders(defensor_group)

clock = pygame.time.Clock()

intro(clock,screen)

groups = []
groups.append(atacante_group)
groups.append(defensor_group)

while True:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    
    check_attacker_colisions(atacante_group, defensor_group, groups)
            
    screen.blit(BACKGROUND, (0, 0))

    for group in groups:
        update_group(group, screen)
          
    pygame.display.update()
