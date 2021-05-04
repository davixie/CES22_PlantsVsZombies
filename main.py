import pygame
from pygame.locals import *
from constants import BACKGROUND, GAME_WIN, screen
from functions.export import update_groups, load_defenders, load_attackers, check_colisions, load_player,verify_end_time,write_screen_game_win
from intro import intro
from menu_compra.buttons import Button_medico, Button_enfermeiro,Button_mascara,Button_alcool,Button_cientista,Play_again


pygame.init()

atacante_group = pygame.sprite.Group()
load_attackers(atacante_group)

defensor_group = pygame.sprite.Group()
player = load_player()

defensor_group = pygame.sprite.Group()


size = (140,72)

defensor_power_group = pygame.sprite.Group()
button_medico = Button_medico(0, 77*2, size)
button_enfermeiro = Button_enfermeiro(0,114*2,size)
button_alcool = Button_alcool(0,153*2,size)
button_mascara = Button_mascara(0,188*2,size)
button_cientista = Button_cientista(0,226*2,size)
buybuttons = [button_medico, button_alcool, button_mascara, button_enfermeiro, button_cientista]

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
        player.verify_event(event,buybuttons,defensor_group, defensor_power_group,atacante_group,screen)

    check_colisions(groups)

    update_groups(groups, screen)
          
    player.drawn_vaccines_score(screen)
    player.update_time()

    # FIM DE JOGO: GAME WIN
    if verify_end_time(player):
        write_screen_game_win(screen)
        buybuttons=[]
        for event in pygame.event.get():
            verify_gamewin_buttons(event)



    pygame.display.update()
