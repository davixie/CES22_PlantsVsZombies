from classes.atacante.atacante import Atacante

class PessoaContagiada(Atacante):
    def __init__(self, positionx, positiony, velx, vely):
        list_image = ['./assets/atacante1/walk1.png', './assets/atacante1/walk2.png', './assets/atacante1/walk3.png', './assets/atacante1/walk4.png']
        resistence = 0.8 # 0 < resistence < 1
        power = 0.8 # 0 < power < 1
        super().__init__(positionx, positiony, velx, vely, resistence, power, list_image)
        self.rect[0] = self.positionx
        self.rect[1] = self.positiony
