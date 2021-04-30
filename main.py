import pygame
from pygame.locals import *
from classes.atacante.export import Atacante
from classes.atacante.export import Virus
from constants import BACKGROUND, screen
# from classes.defensor.defensor import Defensor

pygame.init()

virus_group = pygame.sprite.Group()
virus = Virus(0, 200, 5, 0)
zumbi = Virus(0, 100, 4, 0)
virus_group.add(virus)
virus_group.add(zumbi)

clock = pygame.time.Clock()

while True:

    clock.tick(10)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    
    screen.blit(BACKGROUND, (0, 0))

    virus_group.update()
    virus_group.draw(screen)

    pygame.display.update()
