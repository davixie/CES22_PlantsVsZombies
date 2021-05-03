from classes.atacante.atacante import Atacante
from assets.export import first_attacker_images_list

class PessoaContagiada(Atacante):
    def __init__(self, positionx, positiony, velx, vely):
        list_image = first_attacker_images_list
        resistence = 0.8 # 0 < resistence < 1
        power = 0.8 # 0 < power < 1
        super().__init__(positionx, positiony, velx, vely, resistence, power, list_image)
        self.rect[0] = self.positionx
        self.rect[1] = self.positiony
