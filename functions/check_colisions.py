import pygame
from pygame.locals import *

def check_attacker_colisions(atacante_group, defensor_group, groups):
    attacker_colisions = pygame.sprite.groupcollide(atacante_group, defensor_group, False, False)

    if attacker_colisions:
        for attacker, defensores in attacker_colisions.items():
            attacker.attacker_stop()
            defensores[0].looseLife(attacker.power, groups)
            