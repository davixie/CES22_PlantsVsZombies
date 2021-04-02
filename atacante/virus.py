from atacante.atacante import Atacante

class Virus(Atacante):
    def __init__(self, positionx, positiony, velx, vely, list_image):
        super().__init__(positionx, positiony, velx, vely, list_image)
        self.rect[0] = self.positionx
        self.rect[1] = self.positiony

    def printPosition(self):
        print(self.positionx)