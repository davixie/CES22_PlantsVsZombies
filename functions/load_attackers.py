from classes.atacante.export import Virus, PessoaContagiada

def load_attackers(atacante_group):
    virus = Virus(0, 200, 5, 0)
    doente = PessoaContagiada(0, 100, 4, 0)
    atacante_group.add(virus)
    atacante_group.add(doente)
