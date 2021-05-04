import pygame
import os
from pygame.locals import *
from constants import BACKGROUND, screen
from functions.export import update_groups, load_defenders, load_attackers, check_colisions, load_player, load_final_defenses, check_game_over
from intro import intro
from pygame import font
from menu_compra.buttons import Button_medico

pygame.init()

atacante_group = pygame.sprite.Group()
load_attackers(atacante_group)

defensor_group = pygame.sprite.Group()

final_defensor_group = pygame.sprite.Group()
load_final_defenses(final_defensor_group)

player = load_player()


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
groups.append(final_defensor_group)
game_over = False
while not game_over:
    clock.tick(100)
    screen.blit(BACKGROUND, (0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        player.verify_event(event,buybuttons,defensor_group, defensor_power_group,atacante_group,screen)

    check_colisions(groups)
    game_over = check_game_over(atacante_group)

    screen.blit(BACKGROUND, (0, 0))

    update_groups(groups, screen)
    player.drawn_vaccines_score(screen)
    player.update_time()
    pygame.display.update()

game_over_image = os.path.join('assets', 'artes finais', 'game over.png')
if game_over:
    while True:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
        screen.blit(pygame.image.load(game_over_image), (0, 0))
        pygame.display.update()