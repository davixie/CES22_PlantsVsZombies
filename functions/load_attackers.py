from classes.atacante.export import Virus, PessoaContagiada
from constants import SCREEN_WIDTH

def load_attackers(atacante_group):
    virus = Virus(SCREEN_WIDTH, 200, 5, 0)
    doente = PessoaContagiada(SCREEN_WIDTH, 100, 4, 0)
    atacante_group.add(virus)
    atacante_group.add(doente)
