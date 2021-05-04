from classes.defensor.defensor import Defensor
from classes.defensor.power.nurse_power import Nurse_Power
from assets.export import nurse_images_list

class Enfermeiro(Defensor):
    def __init__(self, position_x, position_y, defensor_power_group):
        list_image = nurse_images_list
        power = 0.8
        resistence = 0.8
        super().__init__(position_x, position_y, resistence, power, list_image, defensor_power_group)
        self.rect[0] = self.position_x
        self.rect[1] = self.position_y

    def atack(self, defensor_power_group):
        defensor_power = Nurse_Power(self.position_x, self.position_y, self.power)
        defensor_power_group.add(defensor_power)