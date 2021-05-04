import pygame
from pygame.locals import *
from constants import BACKGROUND, screen
from functions.export import update_group, load_defenders, load_attackers,load_player
from intro import intro
from pygame import font



pygame.init()

atacante_group = pygame.sprite.Group()
load_attackers(atacante_group)

#defensor_group = pygame.sprite.Group()
#load_defenders(defensor_group)
player=load_player()
clock = pygame.time.Clock()

intro(clock,screen)

while True:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == CLICK:
            player.verify_click(defensor_group,atacante_group)
    
    screen.blit(BACKGROUND, (0, 0))

    update_group(atacante_group, screen)
    #update_group(defensor_group, screen)
    player.drawn_vaccines_score(screen)
        
    pygame.display.update()
