import pygame
from pygame.locals import *

def get_groups(groups):
    return groups[0], groups[1], groups[2], groups[3]

def check_colisions(groups):
    check_attacker_colisions(groups)
    check_defensor_power_colision(groups)
    check_last_defenders_colision(groups)

def check_attacker_colisions(groups):
    atacante_group, defensor_group, defensor_power_group, final_defensor_group = get_groups(groups)

    attacker_colisions = pygame.sprite.groupcollide(atacante_group, defensor_group, False, False)

    if attacker_colisions:
        for attacker, defensores in attacker_colisions.items():
            attacker.attacker_stop()
            for defensor in defensores:
                defensor.looseLife(attacker.power, groups)

def check_defensor_power_colision(groups):
    atacante_group, defensor_group, defensor_power_group, final_defensor_group = get_groups(groups)

    power_colisions = pygame.sprite.groupcollide(defensor_power_group, atacante_group, True, False)

    if power_colisions:
        for power, attackers in power_colisions.items():
            for attacker in attackers:
                attacker.looseLife(power.power, groups)

def check_last_defenders_colision(groups):
    atacante_group, defensor_group, defensor_power_group, final_defensor_group = get_groups(groups)

    last_defense_colision = pygame.sprite.groupcollide(final_defensor_group, atacante_group, True, True)