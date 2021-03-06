import pygame
import random
from constants import SCREEN_WIDTH, SCREEN_HEIGHT,rows
from classes.atacante.export import Virus, PessoaContagiada,Variante
from math import exp

def create_enemys(atacante_group,player):
    virus_probability=random.uniform(0,1)
    if virus_probability<0.6*(1-exp(-player.time/10000)):
        line=random.randint(0,4)
        virus_kind=random.randint(1,3)

        if virus_kind==1:
            virus=Virus(SCREEN_WIDTH, 120+int(120+140*(line-1)), 3, 0)
            atacante_group.add(virus)
        if virus_kind==2:
            virus=PessoaContagiada(SCREEN_WIDTH, 130+int(120+140*(line-1)), 3, 0)
            atacante_group.add(virus)
        if virus_kind==3:
            virus=Variante(SCREEN_WIDTH, 120+int(120+140*(line-1)), 3, 0)
            atacante_group.add(virus)

            

        
