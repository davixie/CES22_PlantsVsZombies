from classes.atacante.atacante import Atacante
from assets.export import second_attacker_images_list

class Virus(Atacante):
    def __init__(self, positionx, positiony, velx, vely):
        list_image = second_attacker_images_list
        resistence = 0.6 # 0 < resistence < 1
        power = 0.5 # 0 < power < 1
        super().__init__(positionx, positiony, velx, vely, resistence, power, list_image)
        self.rect[0] = self.positionx
        self.rect[1] = self.positiony
