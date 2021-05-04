from classes.atacante.export import Virus, PessoaContagiada
from constants import SCREEN_WIDTH, rows

def load_attackers(atacante_group):
    
    virus = Virus(SCREEN_WIDTH, rows[0], 5, 0)
    doente = PessoaContagiada(SCREEN_WIDTH, rows[1], 4, 0)
    atacante_group.add(virus)
    atacante_group.add(doente)
    
