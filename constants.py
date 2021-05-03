import pygame

# Size of Screen
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Size of Rows
ROW_SPACE = 100
rows = [0, ROW_SPACE, 2*ROW_SPACE, 3*ROW_SPACE, 4*ROW_SPACE]

# Background of Game
BACKGROUND = pygame.image.load('./assets/field_game.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))