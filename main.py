import pygame
from pygame.locals import *
from classes.atacante.export import Virus, Variante, PessoaContagiada
from constants import BACKGROUND, screen
# from classes.defensor.defensor import Defensor

pygame.init()

atacante_group = pygame.sprite.Group()
virus = Virus(0, 200, 5, 0)
doente = PessoaContagiada(0, 100, 4, 0)
atacante_group.add(virus)
atacante_group.add(doente)

clock = pygame.time.Clock()

while True:

    clock.tick(10)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    
    screen.blit(BACKGROUND, (0, 0))

    atacante_group.update()
    atacante_group.draw(screen)

    pygame.display.update()
