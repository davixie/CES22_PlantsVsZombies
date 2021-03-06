import os
import pygame
from constants import BACKGROUND, screen,SCREEN_WIDTH, SCREEN_HEIGHT
from pygame import mixer

def intro(clock,screen):

    game_icon=pygame.image.load(os.path.join('assets','icon.png'))
    pygame.display.set_icon(game_icon)
    pygame.display.set_caption('QUARENTINE: THE PANDEMIC GAME')


    mixer.music.load(os.path.join('assets','alexander-nakarada-chase.ogg'))
    mixer.music.play(-1)

    for i in range(1,20):
        clock.tick(20)
        if i<10:
            image='ezgif-frame-00{}.png'.format(str(i))
        else:
            image='ezgif-frame-0{}.png'.format(str(i))
        image=pygame.image.load(os.path.join('assets','Intro I', image))
        image=pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(image, (0, 0))
        pygame.display.update()

    for i in range(1,51):
        clock.tick(100)
        if i<10:
            image='ezgif-frame-00{}.png'.format(str(i))
        else:
            image='ezgif-frame-0{}.png'.format(str(i))
        image=pygame.image.load(os.path.join('assets','Intro II', image))
        image=pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(image, (0, 0))
        pygame.display.update()

    background = pygame.Surface(screen.get_size())
    background = background.convert()

    for i in range(0,15):
        clock.tick(20)
        possibleColors=[(250, 250, 250),(250, 0, 0),(0, 0, 0)]
        background.fill(possibleColors[i%3])
        screen.blit(background, (0, 0))
        pygame.display.update()

    start=False
    while(not start):
        clock.tick(10)
        image=pygame.image.load(os.path.join('assets','Quarantine The Pandemic Game.png'))
        image=pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(image, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                x,y=pygame.mouse.get_pos()
                if x>=600*SCREEN_WIDTH/1600 and x<=880*SCREEN_WIDTH/1600:
                    if y>=710*SCREEN_HEIGHT/900 and y<=830*SCREEN_HEIGHT/900:
                        start=True
            if event.type == pygame.QUIT:
                pygame.quit()
    for i in range(1,126):
        if i==22:
            clock.tick(0.5)
        elif i==47:
            clock.tick(0.5)
        elif i==73:
            clock.tick(0.5)
        elif i==96:
            clock.tick(0.2)
        else:
            clock.tick(15)
        if i<10:
            image='ezgif-frame-00{}.png'.format(str(i))
        elif i<100:
            image='ezgif-frame-0{}.png'.format(str(i))
        else:
            image='ezgif-frame-{}.png'.format(str(i))
        image=pygame.image.load(os.path.join('assets','Inicio do Jogo', image))
        image=pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(image, (0, 0))
        pygame.display.update()


    