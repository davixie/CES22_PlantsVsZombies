import pygame

from pygame.locals import *

from atacante.virus import Virus

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BACKGROUND = pygame.image.load('./assets/field_game.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))

virus_group = pygame.sprite.Group()
virus = Virus(0, 200, 5, 0, 1)
zumbi = Virus(0, 100, 4, 0, 1)
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
