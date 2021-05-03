import pygame
from pygame.locals import *
from constants import BACKGROUND, screen
from functions.export import update_group, load_defenders, load_attackers

pygame.init()

atacante_group = pygame.sprite.Group()
load_attackers(atacante_group)

defensor_group = pygame.sprite.Group()
load_defenders(defensor_group)

clock = pygame.time.Clock()

while True:
    clock.tick(10)

    for event in pygame.eve+nt.get():
        if event.type == QUIT:
            pygame.quit()
    
    screen.blit(BACKGROUND, (0, 0))

    update_group(atacante_group, screen)
    update_group(defensor_group, screen)
        
    pygame.display.update()
