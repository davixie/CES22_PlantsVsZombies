import pygame
from pygame.locals import *

def check_attacker_colisions(atacante_group, defensor_group, groups):
    attacker_colisions = pygame.sprite.groupcollide(atacante_group, defensor_group, False, False)

    if attacker_colisions:
        for attacker, defensores in attacker_colisions.items():
            attacker.attacker_stop()
            defensores[0].looseLife(attacker.power, groups)

def check_defensor_power_colision(defensor_power_group, atacante_group, groups):
    power_colisions = pygame.sprite.groupcollide(defensor_power_group, atacante_group, True, False)

    if power_colisions:
        for power, attackers in power_colisions.items():
            attackers[0].looseLife(power.power, groups)