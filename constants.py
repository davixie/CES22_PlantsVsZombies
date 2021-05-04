import pygame
import os

# Size of Screen
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Size of Rows
ROW_SPACE = 100
COLUMN_SPACE =300
rows = [0, ROW_SPACE, 2*ROW_SPACE, 3*ROW_SPACE, 4*ROW_SPACE]
columns = [0, COLUMN_SPACE, 2*COLUMN_SPACE, 3*COLUMN_SPACE, 4*COLUMN_SPACE]

# Background of Game
BACKGROUND = pygame.image.load(os.path.join('assets','background.png'))
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))

INITIAL_VACCINES=100